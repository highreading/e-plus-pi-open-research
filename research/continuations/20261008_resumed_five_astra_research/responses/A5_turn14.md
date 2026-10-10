> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An all-prime affine cofactor separation in the original signed producer

## Abstract and status

The unconditional rationality or irrationality of $e+\pi$ remains unresolved. This report also does **not** prove the requested strict intrinsic-content estimate


$$
\log \mathfrak J_N^0\le (2-\varepsilon)N\log N+O(N),
\qquad
\mathfrak J_N^0=\gcd(U_N,V_Ny_{K,N}).
$$



The new proved result is narrower: an **evaluated all-prime separation between the residual intrinsic endpoint content and the actual primitive exponential endpoint**.

Write


$$
\gamma_N=\gcd(\tau_N,y_{K,N}),\qquad
T_N=E_N-M_N.
$$


Thus $\mathfrak J_N^0=c_N\gamma_N$. At every original index,


$$
\boxed{
\gcd(\gamma_N,T_N)
=\gcd(\gamma_N,a_{K,N})
=\gcd(\tau_N,E_{K,N},a_{K,N}).
}
\tag{0.1}
$$


The actual reduced arc numerator is positive and satisfies


$$
\boxed{0<a_{K,N}<10N^6.}
\tag{0.2}
$$


Consequently,


$$
\boxed{
\gcd\!\left(\mathfrak J_N^0,c_NT_N\right)
<c_N\,10N^6.
}
\tag{0.3}
$$


This is a numerical all-prime statement, not a polynomial-row content bound.

The proof also evaluates the actual affine integer


$$
\boxed{
\mathcal C_N=d_{K,N}T_N-\nu_Na_{K,N}
=d_{K,N}\tau_N(E_{F,N}-\delta_N^2)+\nu_Ny_{K,N}.
}
\tag{0.4}
$$


It satisfies


$$
\boxed{
\frac34d_{K,N}\tau_N\delta_N^2
<\mathcal C_N
<2d_{K,N}\tau_N\delta_N^2
}
\tag{0.5}
$$


on the full original domain, and


$$
\boxed{\gcd(\tau_N,\mathcal C_N)=\gamma_N.}
\tag{0.6}
$$



After removing the explicitly bounded common part in (0.1), every remaining endpoint-content depth is a cancellation depth between **two units in the actual affine expression**


$$
d_{K,N}(T_N/b_N^\circ)-\nu_N(a_{K,N}/b_N^\circ).
$$


Here $b_N^\circ$ is an auxiliary cofactor defined below; it is not the numerator of the aggregate arc.

This pays one specific joint-depth component uniformly. It does **not** bound the remaining source-weighted unit-collision mass. In particular, it does not yet improve the leading $2N\log N$ bound for the whole $\mathfrak J_N^0$.

The passed analytic audits are reused without repetition. The audited canonical endpoint/gcd theorem is also reused. No unrestricted Bézout-row optimization, TDC assertion, numerical prime scan, or computation at an enormous original index is used.

---

## 1. Scope and unchanged original objects

Throughout,


$$
\boxed{
N=9^{18+32u},\qquad u\in\mathbb Z_{\ge0},
}
$$


and


$$
n=2N,\qquad m=N-3,\qquad \ell=2N-6.
$$


Every such $N$ is odd. The physical polynomial terminal remains $n=2N$.

The passed pairwise-Jensen, spread, and SAME-$H$ comparisons retain their established scope and unchanged cutoff $k\ge512$. They are not re-audited here and are not used as numerical gcd estimates.

### 1.1 Actual Gaussian division and source content

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


with


$$
C_0=1,\quad C_1=2t-1,\quad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$


Retain the actual integers


$$
d=a_Nb_{N-1}-a_{N-1}b_N,
\qquad
g_B=\gcd(b_{N-1},b_N)>0,
$$




$$
\alpha=\frac{b_{N-1}}{g_B},\qquad
\beta=\frac{b_N}{g_B},\qquad
\delta=\frac d{g_B}.
$$


Thus


$$
F=\alpha C_N-\beta C_{N-1},\qquad
F(i)=F(-i)=\delta,\qquad \gcd(\alpha,\beta)=1.
$$



For an integer polynomial $H$, put


$$
\eta(H)=\int_{-\infty}^{1}e^{t-1}H(t)\,dt,
\qquad
E(H)=\sum_{j=0}^{\deg H}(-1)^jj![t^j]H.
$$


The full degree-six multiplier and source are


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad
K=\mathcal H C_m^2,
$$




$$
U=-\eta(K),\qquad V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$



The established content identity is retained:


$$
h=\operatorname{cont}(W_{\rm raw})=g_B^2c.
$$


Hence


$$
\tau=\frac Uc,\qquad \nu=\frac Vc,\qquad
\gcd(\tau,\nu)=1,
$$




$$
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2.
$$


On the original domain,


$$
U,V,M>0.
$$



No undivided Gaussian square is substituted for $F^2$, $V$, or these contents.

### 1.2 Both arcs, both least clearers, and the actual primitive pair

Retain


$$
E_F=E(F^2),\qquad E_K=E(K),
$$




$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


Both monic quotient polynomials have degree at most $2N-2$.

The least simultaneous clearer is


$$
D=\operatorname{lcm}\bigl(\operatorname{den}(R_F),
                         \operatorname{den}(R_K)\bigr),
$$


where the two arcs are first reduced completely. Set


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$



Independently reduce the aggregate arc:


$$
\tau R_F+\nu R_K=\frac b\lambda,\qquad
\gcd(b,\lambda)=1,\quad \lambda>0.
$$


Then


$$
E=\tau E_F+\nu E_K,\qquad
A=\lambda E-b,\qquad G=\gcd(M,A).
$$


The actual primitive output remains


$$
\boxed{
p=\frac AG,\qquad q=\frac{\lambda M}{G}.
}
\tag{1.1}
$$


Here $G$ is the final gcd over **all primes**.

The exact reconciliations are


$$
\tau X+\nu Y=\frac D\lambda A,
$$




$$
\gcd(D\tau\delta^2,\tau X+\nu Y)=\frac D\lambda G,
$$




$$
D\mid\operatorname{lcm}(1,\ldots,2N-1),\qquad D<256^N.
\tag{1.2}
$$



None of the auxiliary divisions introduced later changes $W_{\rm prim}$, $D$, $\lambda$, $G$, $p$, or $q$.

### 1.3 The actual reduced $K$-arc

Put


$$
x=\ell^2,\qquad
L(x)=(x-1)(x-9)(x-25),
$$




$$
A_K(x)=13x^3-455x^2+3502x-5850.
$$


The established original-domain reduction is


$$
R_K=\frac{A_K(x)}{30L(x)}=\frac{a_K}{d_K},
$$


where


$$
g_{\rm arc}
=90\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}},
$$




$$
\varepsilon_5=\mathbf1_{u\equiv1\ (5)},\quad
\varepsilon_{19}=\mathbf1_{u\equiv3\ (9)},\quad
\varepsilon_{31}=\mathbf1_{u\equiv5,7\ (15)},
$$


and


$$
a_K=\frac{A_K(x)}{g_{\rm arc}},\qquad
d_K=\frac{30L(x)}{g_{\rm arc}}.
$$


Thus


$$
\gcd(a_K,d_K)=1,\qquad
0<d_K<\frac{64}{3}N^6.
\tag{1.3}
$$



Define


$$
y_K=d_KE_K-a_K,\qquad \mu=D/d_K.
$$


Then


$$
\boxed{\gcd(d_K,y_K)=1,\qquad Y=\mu y_K.}
\tag{1.4}
$$



The intrinsic divisors are


$$
\mathfrak J^0=\gcd(U,Vy_K),\qquad
\mathfrak J=\gcd(U,VY).
$$


The established exact relations are


$$
\boxed{
\mathfrak J^0=c\gcd(\tau,y_K),\qquad
\mathfrak J^0\mid\mathfrak J\mid\mu\mathfrak J^0,\qquad
U/\mathfrak J\mid q.
}
\tag{1.5}
$$


In particular, $\mu<256^N$. These assertions include denominator primes and primes dividing the Gaussian data.

---

## 2. Complete forced columns and finite boundaries

This section records the original objects in which the new cofactor is evaluated. No centered coefficient-content theorem is used to bound a numerical gcd.

### 2.1 Original boundary states and all thirteen weights

The two endpoint coordinates are


$$
\eta(C_j)=1-2j\Theta_j,\qquad
E(C_j)=(-1)^j-2j\Phi_j,
$$


with


$$
\Theta_0=\Phi_0=0,\qquad \Theta_1=\Phi_1=1,
$$




$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
\tag{2.1}
$$


These recurrences are used only within the finite terminal $0\le j\le n$.

The affine third coordinates can be displayed explicitly:


$$
\begin{pmatrix}\Theta_{j+1}\\ \Theta_j\\1\end{pmatrix}
=
\begin{pmatrix}-4j&1&2\\1&0&0\\0&0&1\end{pmatrix}
\begin{pmatrix}\Theta_j\\\Theta_{j-1}\\1\end{pmatrix},
$$




$$
\begin{pmatrix}\Phi_{j+1}\\ \Phi_j\\(-1)^{j+1}\end{pmatrix}
=
\begin{pmatrix}-4j&1&2\\1&0&0\\0&0&-1\end{pmatrix}
\begin{pmatrix}\Phi_j\\\Phi_{j-1}\\(-1)^j\end{pmatrix},
\qquad 1\le j\le n-1.
\tag{2.2}
$$


The respective initial vectors at $j=1$ are


$$
(1,0,1)^t,\qquad (1,0,-1)^t.
$$


Neither forcing coordinate is suppressed.

The complete weights remain


$$
(w_0,\ldots,w_{12})
=(1,8,58,168,399,-176,-916,-176,399,168,58,8,1).
$$


For exactly $1\le k\le11$, retain


$$
r_{k+1}=r_{k-1}+4(n-k)r_k,\qquad
s_{k+1}^*=s_{k-1}^*+4(n-k)s_k^*,
$$




$$
\kappa_{k+1}=\kappa_{k-1}+4(n-k)\kappa_k-2,
$$




$$
\omega_{k+1}=\omega_{k-1}+4(n-k)\omega_k-2(-1)^k,
$$


with


$$
(r_0,s_0^*)=(1,0),\quad(r_1,s_1^*)=(0,1),\quad
\kappa_0=\kappa_1=\omega_0=\omega_1=0.
$$


Put


$$
\mathsf A=\sum_{k=0}^{12}w_k(n-k)r_k,\qquad
\mathsf B=\sum_{k=0}^{12}w_k(n-k)s_k^*,
$$




$$
\mathsf C_U=679936-\sum_{k=0}^{12}w_k(n-k)\kappa_k,
$$




$$
\mathsf C_E=-1849344+\sum_{k=0}^{12}w_k(n-k)\omega_k.
$$


The complete columns are


$$
4096U=\mathsf C_U-\mathsf A\Theta_n-\mathsf B\Theta_{n-1},
$$




$$
4096E_K=\mathsf C_E+\mathsf A\Phi_n+\mathsf B\Phi_{n-1}.
\tag{2.3}
$$



For the actually divided square, retain


$$
\mathsf P=n\alpha^2+(n-2)\beta^2,
$$




$$
\mathsf Q=4(n-1)(n-2)\beta^2-2(n-1)\alpha\beta,
$$




$$
\mathsf C_V=\alpha^2+(2n-3)\beta^2-\delta^2,
$$




$$
\mathsf C_F^E=\alpha^2+(5-2n)\beta^2+4\alpha\beta.
$$


Then


$$
V=\mathsf C_V-\mathsf P\Theta_n-\mathsf Q\Theta_{n-1},
$$




$$
E_F=\mathsf C_F^E-\mathsf P\Phi_n-\mathsf Q\Phi_{n-1}.
\tag{2.4}
$$


Both $-\delta^2$ and $4\alpha\beta$ remain present.

### 2.2 Local rational interfaces and their payments

For $j\ge1$, put


$$
S_j=\eta(C_j),\qquad s_j=S_j/j=\frac1j-2\Theta_j.
$$


The original nonsingular recurrence is


$$
s_{j-1}=s_{j+1}+4js_j+\frac2{j^2-1},
\qquad 2\le j\le n-1,
\tag{2.5}
$$


with


$$
S_0=1,\qquad s_1=-1,\qquad s_2=\frac92.
$$



The local affine constants are exactly


$$
s_{n-k}=r_ks_n+s_k^*s_{n-1}+e_k,
$$




$$
e_k=\frac1{n-k}-\frac{r_k}{n}
-\frac{s_k^*}{n-1}-2\kappa_k.
\tag{2.6}
$$


Thus the displayed local divisions are paid by


$$
Q_{\rm loc}(n)=\prod_{r=0}^{12}(n-r).
$$


Globally, $\mathcal L_n=\operatorname{lcm}(1,\ldots,n)$ pays the forcing through


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}.
$$


These are auxiliary interface payments, not replacements for the least $D$.

The complete affine constants satisfy


$$
\mathsf E
=2\mathsf C_U-\frac{\mathsf A}{n}-\frac{\mathsf B}{n-1},
$$




$$
2\mathsf C_V
=\frac{\mathsf P}{n}+\frac{\mathsf Q}{n-1}+\mathsf T,
\qquad
\mathsf T=(\alpha+\beta)^2-2\delta^2+\frac{2\beta^2}{n}.
\tag{2.7}
$$


Hence the source columns refer to the same actual adjacent affine state.

### 2.3 Retained source, endpoint, and square-arc returns

Let


$$
\Delta=\mathsf A\mathsf Q-\mathsf B\mathsf P.
$$


The source return remains


$$
z_n=4096\mathsf Q U-\mathsf B V,\qquad
z_{n-1}=\mathsf A V-4096\mathsf P U,
$$




$$
z_j=-\Delta\Theta_j+\varrho_j,\qquad
z_{j-1}=z_{j+1}+4jz_j,
$$




$$
\varrho_{j-1}=\varrho_{j+1}+4j\varrho_j-2\Delta,
$$


with


$$
\varrho_n=\mathsf Q\mathsf C_U-\mathsf B\mathsf C_V,\qquad
\varrho_{n-1}=\mathsf A\mathsf C_V-\mathsf P\mathsf C_U.
$$


In the rational interface,


$$
2z_j=\Delta s_j+\rho_j,\qquad
\rho_j=2\varrho_j-\Delta/j,
$$


so


$$
\rho_{j-1}
=\rho_{j+1}+4j\rho_j-\frac{2\Delta}{j^2-1}.
\tag{2.8}
$$


This is the actual forced third coordinate, not a homogeneous pair from another producer.

For the complete endpoint pair, retain


$$
k_E=D\mathsf C_E-4096DR_K,\qquad
f_E=D\mathsf C_F^E-DR_F,
$$




$$
w_n=4096\mathsf QY+\mathsf B X,\qquad
w_{n-1}=-4096\mathsf PY-\mathsf A X,
$$




$$
w_j=D\Delta\Phi_j+\sigma_j,
$$




$$
\sigma_n=\mathsf Qk_E+\mathsf Bf_E,\qquad
\sigma_{n-1}=-\mathsf Pk_E-\mathsf Af_E,
$$




$$
w_{j-1}=w_{j+1}+4jw_j,\qquad
\sigma_{j-1}=\sigma_{j+1}+4j\sigma_j+2D\Delta(-1)^j.
$$


Thus


$$
z_nw_{n-1}-z_{n-1}w_n
=-4096\Delta(UX+VY).
\tag{2.9}
$$


No division by $\Delta$ is made.

Finally, the full square-arc return is


$$
\xi_{j+1}=4\upsilon_j-2\xi_j-\xi_{j-1}+16b_j,
$$




$$
\upsilon_{j+1}
=-4\xi_j-2\upsilon_j-\upsilon_{j-1}+16(\ell_j-a_j),
$$


where


$$
\ell_j=
\begin{cases}
0,&j\text{ odd},\\
(1-j^2)^{-1},&j\text{ even},
\end{cases}
$$


and the initial values at $j=0,1$ are zero. Its original evaluation is


$$
R_F=\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
                  -2\alpha\beta\xi_{n-1}}2.
\tag{2.10}
$$



---

## 3. Established canonical endpoint theorem: exact scope of reuse

Let $P_r^{\mathrm H},Q_r^{\mathrm H}$, $0\le r\le N$, be the paid Hermite endpoint integers


$$
P_0^{\mathrm H}=Q_0^{\mathrm H}=1,\qquad
P_1^{\mathrm H}=3,\quad Q_1^{\mathrm H}=1,
$$




$$
Z_{r+1}=(4r+2)Z_r+Z_{r-1}.
$$


They are positive odd integers, and


$$
P_{r+1}^{\mathrm H}Q_r^{\mathrm H}
-P_r^{\mathrm H}Q_{r+1}^{\mathrm H}=2(-1)^r,
\qquad
\gcd(Q_r^{\mathrm H},Q_{r+1}^{\mathrm H})=1.
$$



Define the actual signed returns


$$
\mathcal R_{r;N}
=d_KP_r^{\mathrm H}U+Q_r^{\mathrm H}y_K.
$$


The audited theorem gives, at every original $N$,


$$
\boxed{
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
}
$$




$$
\boxed{
|\mathcal R_{N-1;N}|,\ |\mathcal R_{N;N}|
<d_K36^N N!,
}
\tag{3.1}
$$


and


$$
\gcd(\mathcal R_{N-1;N},\mathcal R_{N;N})
=\gcd(U,y_K).
$$


The binary determinant factor has already been paid in the actual objects; it is not silently treated as a unimodular determinant.

Put


$$
s_r=\gcd(c,Q_r^{\mathrm H}).
$$


The exact canonical factorization is


$$
\boxed{
\mathfrak J^0
=c\gcd\left(
\tau,\frac{\mathcal R_{N-1;N}}{s_{N-1}},
     \frac{\mathcal R_{N;N}}{s_N}
\right).
}
\tag{3.2}
$$



For clarity, the full original-boundary expression is obtained by setting


$$
\Psi_j^{(r)}=Q_r^{\mathrm H}\Phi_j-P_r^{\mathrm H}\Theta_j.
$$


Then


$$
\Psi_0^{(r)}=0,\qquad
\Psi_1^{(r)}=Q_r^{\mathrm H}-P_r^{\mathrm H},
$$




$$
\Psi_{j+1}^{(r)}+4j\Psi_j^{(r)}-\Psi_{j-1}^{(r)}
=2\bigl(Q_r^{\mathrm H}(-1)^j-P_r^{\mathrm H}\bigr),
$$


and


$$
\begin{aligned}
4096\mathcal R_{r;N}
={}&d_K\bigl(
P_r^{\mathrm H}\mathsf C_U+Q_r^{\mathrm H}\mathsf C_E
+\mathsf A\Psi_n^{(r)}+\mathsf B\Psi_{n-1}^{(r)}
\bigr)\\
&-4096Q_r^{\mathrm H}a_K.
\end{aligned}
\tag{3.3}
$$


Both constants, both forcings, both seeds, and the full reduced arc term are retained.

The established size information used below is


$$
\log U=2N\log N+O(N),\qquad
c\le N!e^{O(N)},
\tag{3.4}
$$


and


$$
2^{4N-16}(2N)!<U<50\cdot36^{N-3}(2N)!.
\tag{3.5}
$$



---

## 4. The new evaluated affine cofactor

Write


$$
E_L=E_F-\delta^2,\qquad
T=E-M=\tau E_L+\nu E_K.
$$


Introduce


$$
\boxed{
\mathcal C=d_KT-\nu a_K.
}
\tag{4.1}
$$



### 4.1 Exact original-source identity

Using $y_K=d_KE_K-a_K$,


$$
\begin{aligned}
\mathcal C
&=d_K(\tau E_L+\nu E_K)-\nu a_K\\
&=d_K\tau E_L+\nu y_K.
\end{aligned}
$$


Therefore


$$
\boxed{
c\mathcal C=d_KUE_L+Vy_K.
}
\tag{4.2}
$$


This is an integer identity in the actual generators of $\mathfrak J^0$. In particular,


$$
\mathfrak J^0\mid c\mathcal C.
$$



It is also completely evaluated in the retained columns:


$$
\begin{aligned}
4096T={}&
4096\tau(\mathsf C_F^E-\delta^2)+\nu\mathsf C_E\\
&+(\nu\mathsf A-4096\tau\mathsf P)\Phi_n
+(\nu\mathsf B-4096\tau\mathsf Q)\Phi_{n-1},
\end{aligned}
\tag{4.3}
$$


and


$$
4096\mathcal C=4096d_KT-4096\nu a_K.
\tag{4.4}
$$


Here $\tau,\nu$ are still obtained from the actual changing divided Gaussian source. They have not been replaced by independent parameters.

For comparison, the same coefficients satisfy the actual source relation


$$
\begin{aligned}
&(\nu\mathsf A-4096\tau\mathsf P)\Theta_n
+(\nu\mathsf B-4096\tau\mathsf Q)\Theta_{n-1}\\
&\hspace{25mm}
=\nu\mathsf C_U-4096\tau\mathsf C_V,
\end{aligned}
\tag{4.5}
$$


because $\tau V=\nu U$. Equations (4.3)–(4.5) reconcile the two forcing constants in the same original affine state.

### 4.2 Uniform sign and size

Put


$$
I_F=\int_0^1e^tF(t)^2\,dt,\qquad
I_K=\int_0^1e^tK(t)\,dt,
$$


and retain the complete positive $K$-endpoint contribution


$$
T_K=I_K+R_K.
$$


Integration by parts gives


$$
E_L=eV+(e-1)\delta^2-I_F,\qquad
E_K=-eU-I_K.
$$


Since $\tau V=\nu U$,


$$
T=\tau\delta^2(e-1)-\tau I_F-\nu I_K.
$$


Consequently,


$$
\boxed{
\mathcal C
=d_K\tau\delta^2\bigl(e-1-\epsilon_{\rm mix}\bigr),
}
\tag{4.6}
$$


where


$$
\epsilon_{\rm mix}
=\frac{I_F+(V/U)T_K}{\delta^2}>0.
\tag{4.7}
$$



The following explicit estimates from the supplied original-source proofs are used at their stated scope:


$$
\frac{I_F}{\delta^2}<2^{14-4N},\qquad
\frac{V}{U\delta^2}<2^{28-2N},\qquad
0<T_K<\frac{61}{30}<3
\qquad(N\ge16).
\tag{4.8}
$$


Their Gaussian ratio estimate uses the actual cancellation of $g_B$ in


$$
\frac{|\alpha|+|\beta|}{|\delta|}
=\frac{|b_{N-1}|+|b_N|}{|d|};
$$


it does not freeze or invert any Gaussian datum modulo a prime. No recurrence run is needed here.

Thus, for $N\ge16$,


$$
0<\epsilon_{\rm mix}
<2^{14-4N}+3\cdot2^{28-2N}
\le 2^{-50}+\frac3{16}<\frac14.
$$


Every original $N$ lies in this range. Since $2<e<3$, (4.6) proves


$$
\boxed{
\frac34d_K\tau\delta^2<\mathcal C<2d_K\tau\delta^2.
}
\tag{4.9}
$$


In particular, $\mathcal C$ is nonzero at every original index.

This is not a small-height intrinsic certificate:


$$
\log(c\mathcal C)=2N\log N+O(N).
\tag{4.10}
$$


The useful new information will instead be the all-prime separation proved next.

---

## 5. New theorem: polynomially bounded shared cofactor

### Theorem 5.1 — Original affine cofactor separation

At every original index, let


$$
\gamma=\gcd(\tau,y_K),\qquad \mathfrak J^0=c\gamma,
$$


and define


$$
b^\circ=\gcd(\gamma,a_K).
$$


Then:

1. The exact common depth with the primitive exponential endpoint is
   

$$
\boxed{
   \gcd(\gamma,T)
   =b^\circ
   =\gcd(\tau,E_K,a_K).
   }
   \tag{5.1}
$$



2. The actual reduced numerator provides the explicit cap
   

$$
\boxed{
   1\le b^\circ\le a_K<10N^6.
   }
   \tag{5.2}
$$



3. In terms of the turn13 multiplier $B_{\rm can}=c(M-E)=-cT$,
   

$$
\boxed{
   \gcd(\mathfrak J^0,|B_{\rm can}|)
   =c\,b^\circ<10cN^6.
   }
   \tag{5.3}
$$



4. After the paid auxiliary divisions
   

$$
r^\circ=\gamma/b^\circ,\quad
   T^\circ=T/b^\circ,\quad
   a^\circ=a_K/b^\circ,\quad
   \tau^\circ=\tau/b^\circ,
$$


   one has
   

$$
\boxed{
   r^\circ
   =\gcd\left(\tau^\circ,d_KT^\circ-\nu a^\circ\right),
   }
   \tag{5.4}
$$


   and
   

$$
\boxed{
   \gcd(r^\circ,d_K\nu T^\circ a^\circ)=1.
   }
   \tag{5.5}
$$



5. The same residual factor is expressed by the unchanged canonical returns:
   

$$
\boxed{
   r^\circ=
   \gcd\left(
   \frac{\tau}{b^\circ},
   \frac{\mathcal R_{N-1;N}}{s_{N-1}b^\circ},
   \frac{\mathcal R_{N;N}}{s_Nb^\circ}
   \right).
   }
   \tag{5.6}
$$


   Every displayed division is integral.

#### Proof

Because $\gamma\mid\tau$ and $\gcd(\tau,\nu)=1$,


$$
\gcd(\gamma,\nu)=1.
$$


Because $\gamma\mid y_K$ and $\gcd(d_K,y_K)=1$,


$$
\gcd(\gamma,d_K)=1.
\tag{5.7}
$$



Equation (4.1), together with


$$
\mathcal C=d_K\tau E_L+\nu y_K,
$$


shows that $\gamma\mid\mathcal C$. Reducing $d_KT-\nu a_K=\mathcal C$ modulo $\gamma$ gives


$$
d_KT\equiv\nu a_K\pmod\gamma.
$$


Both $d_K$ and $\nu$ are units modulo $\gamma$, by (5.7). Hence


$$
\gcd(\gamma,T)=\gcd(\gamma,a_K)=b^\circ.
\tag{5.8}
$$



Moreover,


$$
b^\circ=\gcd(\tau,y_K,a_K)
=\gcd(\tau,d_KE_K,a_K).
$$


Since $\gcd(d_K,a_K)=1$, this is


$$
b^\circ=\gcd(\tau,E_K,a_K).
$$


This proves (5.1), at every prime and depth.

For the explicit cap, the original $x=(2N-6)^2$ is at least $36$. On this range,


$$
13x^3-455x^2=x^2(13x-455)>0,
$$


and $3502x-5850>0$, so $A_K(x)>0$. Also


$$
13x^3-A_K(x)=455x^2-3502x+5850>0.
$$


Thus


$$
0<A_K(x)<13x^3.
$$


Since $g_{\rm arc}\ge90$,


$$
0<a_K<\frac{13}{90}(2N)^6
=\frac{416}{45}N^6<10N^6.
$$


This proves (5.2).

Now $\mathfrak J^0=c\gamma$ and $|B_{\rm can}|=cT$, so


$$
\gcd(\mathfrak J^0,|B_{\rm can}|)
=c\gcd(\gamma,T)=cb^\circ.
$$


This proves (5.3).

For the normalized assertions, first note that $b^\circ$ divides


$$
\gamma,\ \tau,\ y_K,\ T,\ a_K,\ \mathcal C.
$$


All auxiliary divisions are therefore integral. Furthermore,


$$
\gcd(\tau,\mathcal C)
=\gcd(\tau,d_K\tau E_L+\nu y_K)
=\gcd(\tau,y_K)=\gamma,
\tag{5.9}
$$


where $\gcd(\tau,\nu)=1$ pays the only cancellation. Dividing both arguments in (5.9) by $b^\circ$ gives (5.4).

From $b^\circ=\gcd(\gamma,T)=\gcd(\gamma,a_K)$,


$$
\gcd(r^\circ,T^\circ)=\gcd(r^\circ,a^\circ)=1.
$$


Equation (5.7) gives $\gcd(r^\circ,d_K\nu)=1$, proving (5.5).

Finally, the audited factorization (3.2) says


$$
\gamma=
\gcd\left(
\tau,\mathcal R_{N-1;N}/s_{N-1},
     \mathcal R_{N;N}/s_N
\right).
$$


Since $b^\circ\mid\gamma$, it divides every argument. Dividing all three arguments by $b^\circ$ proves (5.6). ∎

### 5.1 What this theorem actually pays

The new estimate


$$
\log b^\circ\le6\log N+\log10
\tag{5.10}
$$


pays the **entire shared numerical depth** of $\gamma$ and $T$, over all primes.

This is stronger information than either:

- separate height bounds for $c$ and the canonical returns; or
- the identity $B_{\rm can}=-cT$, whose divisibility by $c$ was automatic.

In particular, despite the factorial-scale height of $T$, its shared depth with the residual endpoint content is controlled by the actual degree-six arc numerator.

The limitation is equally important. The theorem bounds a specified overlap of the intrinsic content, not the whole intrinsic content:


$$
\mathfrak J^0=c\,b^\circ r^\circ.
\tag{5.11}
$$


It removes a polynomial-size component and supplies additional coprimality conditions on the residual. It does not prove a leading-exponent saving for $c\,r^\circ$.

---

## 6. Exact remaining prime depths: genuine affine unit collisions

The theorem gives a useful all-prime description without discarding denominator, Gaussian, or large primes.

For a prime $p$, write


$$
t_p=v_p(\tau),\quad
a_p=v_p(a_K),\quad
z_p=v_p(\mathcal C).
$$


By (5.9),


$$
v_p(\gamma)=\min(t_p,z_p).
$$


Therefore


$$
\boxed{
v_p(r^\circ)
=\max\{0,\min(t_p,z_p)-a_p\}.
}
\tag{6.1}
$$



Suppose $v_p(r^\circ)>0$. Then


$$
v_p(\gamma)>a_p.
$$


Equation (5.1) forces


$$
\boxed{v_p(T)=a_p.}
\tag{6.2}
$$


Also $p\nmid d_K\nu$. Dividing


$$
\mathcal C=d_KT-\nu a_K
$$


by the paid factor $p^{a_p}$ yields a difference of two $p$-adic units:


$$
d_K\frac{T}{p^{a_p}}
-\nu\frac{a_K}{p^{a_p}}.
$$


Its congruence depth is at least $v_p(r^\circ)$:


$$
\boxed{
d_K\frac{T}{p^{a_p}}
\equiv
\nu\frac{a_K}{p^{a_p}}
\pmod{p^{\,v_p(r^\circ)}}.
}
\tag{6.3}
$$



Thus the remaining depths are not shared factors of the two affine summands. Their shared factors have already been paid by $b^\circ$. They are cancellations between units in the actual changing source.

This includes every $p>N$. For example, if $p>N$ and $p\nmid a_K$, a remaining depth has


$$
p\nmid d_K\nu T a_K,
\qquad
d_KT\equiv\nu a_K\pmod{p^{v_p(r^\circ)}}.
$$


No factorial allowance is available at such a prime, and none is asserted.

### 6.1 The evaluated cofactor after the intrinsic division

Since $\gamma\mid\mathcal C$, (4.9) gives


$$
\boxed{
\frac34d_K\delta^2\,\frac{U}{\mathfrak J^0}
<
\frac{\mathcal C}{\gamma}
<
2d_K\delta^2\,\frac{U}{\mathfrak J^0}.
}
\tag{6.4}
$$


The quotient is an integer, and the comparison is valid at every original index.

This identifies its size exactly enough to prevent a false height argument. The quotient is exponentially comparable to the missing intrinsic denominator factor $U/\mathfrak J^0$; its integrality alone does not force that factor to grow factorially.

### 6.2 Why an apparent extra division is not paid

The displayed intrinsic certificate is


$$
d_KE_L\,U+1\cdot(Vy_K)=c\mathcal C.
\tag{6.5}
$$


Its displayed coefficient row has gcd $1$, because its second coefficient is $1$.

Although $\gamma\mid\mathcal C$, dividing (6.5) by $\gamma$ is **not** a certificate in the original generators $U,Vy_K$: it introduces $U/\gamma$ and $Vy_K/\gamma$. The canonical returns divided by $b^\circ$ in (5.6) do not authorize this unpaid division.

This is a precise obstruction to extracting a strict intrinsic saving merely by normalizing the new affine determinant. No claim is made about optimizing all other possible certificate rows.

---

## 7. The smaller remaining obligation and a concrete follow-on lemma

The paid and unpaid factors now have the exact form


$$
\boxed{
\mathfrak J^0=c\,b^\circ r^\circ,\qquad
b^\circ<10N^6,
}
$$


where $r^\circ$ satisfies both the original signed-return formula (5.6) and the unit-collision conditions (5.4)–(5.5).

The smaller remaining numerical factor is therefore


$$
c\,r^\circ.
$$


The reduction is substantive at the shared-depth level: the entire overlap with the actual primitive exponential endpoint has been bounded explicitly. But it is not yet a reduction of the leading asymptotic height, because $b^\circ$ can be small.

Using only established bounds still gives


$$
c\le N!e^{O(N)},\qquad
r^\circ\le\gamma\le N!e^{O(N)},
$$


and hence only


$$
\log(c\,r^\circ)\le2N\log N+O(N).
\tag{7.1}
$$



### 7.1 Joint affine unit-collision saving — open follow-on lemma

A concrete sufficient next lemma is:

> **Joint affine unit-collision lemma.**  
> For the actual original source, prove that a constant $C$ exists such that
> 

$$
> \boxed{
> r_N^\circ\sqrt{c_N}\le N!e^{CN}
> }
> \tag{JUC}
>
$$


> for every original $N=9^{18+32u}$.
>
> Equivalently, with the fully evaluated $\mathcal C_N$ from (4.1)–(4.4),
> 

$$
> \frac12\log c_N+
> \sum_p
> \max\!\left\{
> 0,\,
> \min\bigl(v_p(\tau_N),v_p(\mathcal C_N)\bigr)
> -v_p(a_{K,N})
> \right\}\log p
> \le\log(N!)+CN.
> \tag{7.2}
>
$$



The sum in (7.2) is a statement of the **open obligation**, not an evaluated proof. Equations (5.1)–(6.3) are the proved reduction that identifies which depths remain.

This is a joint tradeoff: it asks the endpoint collision mass to decrease when the actual source content $c_N$ is large. It does not require the fixed turn13 row to capture an additional factorial, and it does not require HC itself.

A proof would have to use the actual dependence


$$
\nu_N=\frac{\eta(F_N^2)-\delta_N^2}{c_N}
$$


inside the unit congruences (6.3), together with the original forced boundaries. Adjacent Hermite coprimality, coefficient-row primitivity, and separate archimedean heights do not supply this tradeoff.

### 7.2 Conditional consequence of (JUC)

If (JUC) holds, then


$$
\begin{aligned}
\mathfrak J^0
&=c\,b^\circ r^\circ\\
&\le10N^6\sqrt c\,(N!e^{CN})\\
&\le (N!)^{3/2}e^{O(N)}.
\end{aligned}
$$


Using $\log U=2N\log N+O(N)$,


$$
\boxed{
\text{(JUC)}
\quad\Longrightarrow\quad
\mathfrak J^0\le U^{3/4}e^{O(N)}.
}
\tag{7.3}
$$


This would give the requested form with


$$
\varepsilon=\frac12
\quad\text{in}\quad
\log\mathfrak J^0\le(2-\varepsilon)N\log N+O(N).
$$



This is conditional. No bound of the form (JUC) is proved here.

---

## 8. Actual denominator and positive whole error

The original positive polynomial remains


$$
P_N(t)=\frac{F(t)^2+(V/U)K(t)}{\delta^2}.
$$


Its whole error is


$$
\boxed{
\epsilon_N=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0,
}
$$


and the same actual primitive pair satisfies


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0,
\qquad
q_N=\frac{\lambda_NM_N}{G_N}.
}
\tag{8.1}
$$



The auxiliary $\epsilon_{\rm mix}$ used to estimate $\mathcal C$ is not substituted for this whole error. In fact,


$$
\epsilon_N
=\epsilon_{\rm mix}
+\frac4{\delta^2}\int_0^1\frac{F(t)^2}{1+t^2}\,dt,
$$


and the omitted term in the cofactor estimate is retained in every producer conclusion.

For completeness, retain the full rational enclosure


$$
3J_N<\epsilon_N<7J_N,
\qquad
J_N=\frac{J_F+(V/U)J_K}{\delta^2},
$$


where


$$
J_F=
\alpha^2\frac{2N^2-1}{4N^2-1}
+\beta^2\frac{2(N-1)^2-1}{4(N-1)^2-1},
$$


and, with $j_r=(1-4r^2)^{-1}$,


$$
J_K=\frac{61}{420}
+\frac{
916j_m-399(j_{m+1}+j_{m-1})
-58(j_{m+2}+j_{m-2})
-(j_{m+3}+j_{m-3})
}{8192}.
$$


Thus


$$
q_NJ_N=\frac{\lambda_N}{G_N}
       (\tau_NJ_F+\nu_NJ_K).
\tag{8.2}
$$


Neither positive summand is discarded.

If (JUC) were proved, then (1.5), $\mu<256^N$, and (7.3) would give


$$
q_N\ge\frac{U_N}{\mathfrak J_N}
\ge e^{-O(N)}U_N^{1/4}.
$$


The retained estimate


$$
\epsilon_N\asymp R^{-2N},
\qquad
R=1+\sqrt2+\sqrt{2+2\sqrt2},
$$


would imply


$$
\boxed{
\log(q_N\epsilon_N)
\ge\frac12N\log N-O(N)\longrightarrow+\infty.
}
\tag{8.3}
$$



That would retire this producer only. It would not establish rationality or irrationality of $e+\pi$.

---

## 9. Proof-status ledger

| Item | Status and exact scope |
|---|---|
| Pairwise-Jensen, spread, and SAME-$H$ improvement | Established reuse, unchanged cutoff; not re-audited |
| Original contents, reduced arcs, least $D,\lambda$, final all-prime $G$, actual $q$ | Retained unchanged |
| Canonical signed returns and exact factorization (3.2) | Audited established reuse |
| Affine identity $\mathcal C=d_KT-\nu a_K=d_K\tau E_L+\nu y_K$ | Proved here in the actual original columns |
| Uniform positivity and comparison (4.9) | Proved on the full original domain using explicit original-source bounds |
| Exact all-prime separation $\gcd(\gamma,T)=\gcd(\tau,E_K,a_K)$ | Proved here |
| Polynomial cap $b^\circ<10N^6$ | Proved here by evaluating the actual reduced arc numerator |
| Residual unit-collision description (5.4)–(6.3) | Proved here, including every prime and depth |
| Strict bound for the whole $\mathfrak J^0$ | **Not proved** |
| Joint affine unit-collision lemma (JUC) | **Open** |
| HC | **Open**; neither proved nor disproved |
| Fixed-row TDC | **Open**; not investigated or used here |
| Producer retirement | Conditional on a strict intrinsic saving such as (JUC) |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

The cofactor theorem should not be overstated. It controls a specified actual overlap at polynomial height; it does not control the leading joint mass of $c_N$ and $r_N^\circ$.

---

## 10. Bounded arithmetic and final conclusion

No new bounded computation is indispensable for the proved claims in this report. The new identities are verified by the displayed substitutions and gcd arguments, and the only new numerical cap uses


$$
0<A_K(x)<13x^3,\qquad g_{\rm arc}\ge90,\qquad x=(2N-6)^2.
$$


No old source table, Gaussian recurrence run, centered elimination, or arbitrary-prime scan is requested.

In particular, exact computation at finitely many original $u$-values could test those values but could not establish (JUC), HC, or the desired uniform intrinsic saving.

### Final result

The new proved all-prime statement is


$$
\boxed{
\gcd\!\left(
\frac{\mathfrak J_N^0}{c_N},
E_N-M_N
\right)
=
\gcd(\tau_N,E_{K,N},a_{K,N})
<10N^6.
}
$$


It separates the remaining endpoint content from the factorial-scale primitive exponential endpoint and identifies the surviving depths as actual affine unit collisions involving the changing divided Gaussian source.

### Exact remaining bottleneck

After this paid separation,


$$
\mathfrak J_N^0=c_Nb_N^\circ r_N^\circ,\qquad b_N^\circ<10N^6,
$$


and the unresolved task is a quantitative tradeoff between $c_N$ and the residual collision factor $r_N^\circ$. A concrete sufficient target is


$$
r_N^\circ\sqrt{c_N}\le N!e^{CN}.
$$


Every prime, including $p>N$, remains in that obligation through (6.1)–(6.3).

**This turn proves a limited original-source cofactor separation, not the requested full intrinsic-content saving. The intrinsic-content gate, retirement of this producer, and an unconditional determination of the rationality or irrationality of $e+\pi$ remain open.**
