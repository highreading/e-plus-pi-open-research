> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 Turn 22 — Independent audit of A5 Turns 20–22

## Mixed forcing, primitive arithmetic height, and fourth-precision arithmetic

### Executive conclusion

The central new mathematical claims in the three supplied reports **pass at their exact stated hypotheses**:

1. **FULL20:** the residual-relative mixed determinant, its four-defect Hermite seed, its inhomogeneous return, the corrected-column elimination, and both determinant-critical-safe charts are correct.
2. **FULL21:** the actual least simultaneous mixed clearer is correctly identified, and the pointwise bounds
   

$$
\max(|A_{\rm mix}|,|B_{\rm mix}|)
   \ge N^{(p-1)/2}e^{-16N},
   \qquad
   D_{\rm mix}\ge N^{(p-1)/2}e^{-28N}
$$


   follow from the actual original objects. They obstruct the specified exponential primitive mixed-normalization mechanism, but do **not** establish an infinite family of eligible pairs.
3. **FULL22:** the upper-half normalization against the actual Hermite coefficient, all cubic reciprocal-power and Fermat-quotient terms, all four anchored-defect formulas, the integer continuant, the signed cubic remainder, and the four complete columns modulo $p^4$ are correct.

No correction to the substantive formulas is required. A bookkeeping qualification is necessary: statements that “all denominators are units” must refer to the **remaining denominators after the explicitly paid divisions**. The divisions by $p$, by $p^3$ after an actual third collision, and by the actual Gaussian content are not unit divisions.

The outstanding assertion remains


$$
\boxed{
p^{\,4+B_p+j_p}\nmid \gcd(16U,\zeta_{p,N}),
\qquad j_p=v_p(J_N^{\rm aff}).
}
$$


It is neither proved nor refuted by these reports. Fourth precision alone does not decide this assertion when $B_p+j_p>0$.

This audit does not undertake A5 Turn 23’s assigned noncoincidence problem. It verifies that problem’s actual arithmetic inputs and identifies exactly what they do—and do not—prove. The rationality or irrationality of $e+\pi$ remains unresolved.

---

# 1. Audit contract and unchanged original objects

## 1.1 Original domain, Gaussian division, and source content

Throughout,


$$
\boxed{
N=9^{18+32u}=3^{36+64u},\qquad u\in\mathbb Z_{\ge0},
}
$$


and


$$
n=2N,\qquad m=N-3,\qquad \ell=2N-6.
$$


The physical terminal is always $n=2N$. No residual index is substituted for $N$.

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


with


$$
C_0=1,\qquad C_1=2t-1,\qquad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$


The actual Gaussian division is


$$
g_B=\gcd(b_{N-1},b_N)>0,
$$




$$
\alpha=\frac{b_{N-1}}{g_B},\qquad
\beta=\frac{b_N}{g_B},\qquad
\delta=\frac{a_Nb_{N-1}-a_{N-1}b_N}{g_B}.
$$


Thus


$$
F=\alpha C_N-\beta C_{N-1},\qquad
F(\pm i)=\delta,\qquad \gcd(\alpha,\beta)=1.
$$



For an integer polynomial $H$, define


$$
\eta(H)=\sum_jj![z^j]H(1-z),\qquad
E(H)=\sum_j(-1)^jj![t^j]H(t).
$$


Retain


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad K=\mathcal H C_m^2,
$$




$$
U=-\eta(K),\qquad V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V),
$$


and the already established actual content statement


$$
\operatorname{cont}(W_{\rm raw})=g_B^2c.
$$


The primitive source data remain


$$
\tau=U/c,\qquad \nu=V/c,\qquad
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2,
$$


with


$$
U,V,M>0.
$$



All valuations below concern these **divided** objects. An undivided Gaussian quadratic column is not interchangeable with the actual column.

The retained safe Gaussian bound is


$$
H_G:=\alpha^2+\beta^2+\delta^2
<\frac{5^{4N}}{g_B^2}.
$$



## 1.2 Both finite forced systems

The original states are defined only on $0\le j\le n$, with


$$
\Theta_0=\Phi_0=0,\qquad \Theta_1=\Phi_1=1,
$$


and, for exactly $1\le j\le n-1$,


$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
$$


Their complete affine matrices are


$$
\begin{pmatrix}\Theta_{j+1}\\\Theta_j\\1\end{pmatrix}
=
\begin{pmatrix}-4j&1&2\\1&0&0\\0&0&1\end{pmatrix}
\begin{pmatrix}\Theta_j\\\Theta_{j-1}\\1\end{pmatrix},
$$




$$
\begin{pmatrix}\Phi_{j+1}\\\Phi_j\\(-1)^{j+1}\end{pmatrix}
=
\begin{pmatrix}-4j&1&2\\1&0&0\\0&0&-1\end{pmatrix}
\begin{pmatrix}\Phi_j\\\Phi_{j-1}\\(-1)^j\end{pmatrix}.
$$


Neither forcing coordinate is suppressed.

## 1.3 Complete corrected columns

At $x=\ell^2$, put


$$
\begin{aligned}
\mathcal P(x)&=-8x^3-1116x^2-8150x+151,\\
\mathcal Q(x)&=76x^2+2408x+5637,\\
\mathcal F(x)&=4x^2+492x+5463,\\
\mathcal G(x)&=4x^2+556x-3325,
\end{aligned}
$$


and


$$
\mathscr A=2\ell((2\ell+1)\mathcal Q-\mathcal P),\qquad
\mathscr B=-2\ell\mathcal Q,
$$




$$
\mathscr C_U=\mathcal F-\mathcal P+2\ell\mathcal Q,\qquad
\mathscr C_E=\mathcal G+\mathcal P-2(\ell+1)\mathcal Q.
$$


The complete $K$-columns are


$$
16U=\mathscr C_U-\mathscr A\Theta_\ell-\mathscr B\Theta_{\ell-1},
$$




$$
16E_K=\mathscr C_E+\mathscr A\Phi_\ell+\mathscr B\Phi_{\ell-1}.
$$



At the physical terminal,


$$
V=C_V-P\Theta_n-Q\Theta_{n-1},
$$




$$
E_F=C_F^E-P\Phi_n-Q\Phi_{n-1},
$$


where


$$
P=n\alpha^2+(n-2)\beta^2,
$$




$$
Q=4(n-1)(n-2)\beta^2-2(n-1)\alpha\beta,
$$




$$
\boxed{C_V=\alpha^2+(2n-3)\beta^2-\delta^2,}
$$




$$
\boxed{C_F^E=\alpha^2+(5-2n)\beta^2+4\alpha\beta.}
$$



In particular, the source subtraction $-\delta^2$ and the endpoint term $4\alpha\beta$ remain present.

The already passed six-step transport is reused, not re-audited. Its exact finite definition is


$$
T_j=\begin{pmatrix}-4j&1\\1&0\end{pmatrix},\qquad
T=T_{\ell+5}\cdots T_\ell,
$$


with zero initial forcing vectors and six updates


$$
f_{j+1}=T_{\ell+j}f_j+\binom20,\qquad
g_{j+1}=T_{\ell+j}g_j+\binom{2(-1)^j}{0},
\quad 0\le j\le5.
$$


Then


$$
(\Pi,\Omega)=(P,Q)T,
$$




$$
C^{\rm s}=C_V-(P,Q)f_6,\qquad
C^{\rm e}=C_F^E-(P,Q)g_6,
$$


and


$$
V=C^{\rm s}-\Pi\Theta_\ell-\Omega\Theta_{\ell-1},
$$




$$
E_F=C^{\rm e}-\Pi\Phi_\ell-\Omega\Phi_{\ell-1}.
$$


The final recurrence step is exactly $\ell+5=n-1$.

Retain


$$
\Delta=\mathscr A\Omega-\mathscr B\Pi<0,
$$




$$
\mathscr I_1=\Pi\mathscr C_U-\mathscr A C^{\rm s},\qquad
\mathscr I_2=\Omega\mathscr C_U-\mathscr B C^{\rm s},
$$




$$
J_N^{\rm aff}=\gcd(\mathscr I_1,\mathscr I_2)>0.
$$


The explicit older bounds sufficient for this audit are


$$
|\Delta|,\ J_N^{\rm aff}
<
10^{10}n^{15}\frac{5^{4N}}{g_B^2},
$$


and


$$
|\mathscr A|,|\mathscr B|,|\mathscr C_U|,|\mathscr C_E|
<10^5n^7,
$$




$$
|\Pi|,|\Omega|,|C^{\rm s}|,|C^{\rm e}|
<10^5n^8H_G.
$$



The separately obtained sharper $\Delta$-conditioning estimate can be used at its established scope. Nothing here requires reopening it. Its stronger height bill still does not bound source contact.

## 1.4 Actual arc credit and remaining branch

Let


$$
L(x)=(x-1)(x-9)(x-25),\qquad
A_K(x)=13x^3-455x^2+3502x-5850.
$$


The retained lowest-term $K$-arc is


$$
R_K=\frac{A_K(\ell^2)}{30L(\ell^2)}=\frac{a_K}{d_K},
$$


where


$$
g_{\rm arc}=90\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}},
$$




$$
\varepsilon_5=\mathbf1_{u\equiv1\pmod5},\quad
\varepsilon_{19}=\mathbf1_{u\equiv3\pmod9},\quad
\varepsilon_{31}=\mathbf1_{u\equiv5,7\pmod{15}},
$$


and


$$
a_K=A_K(\ell^2)/g_{\rm arc},\qquad
d_K=30L(\ell^2)/g_{\rm arc}.
$$


Thus


$$
\gcd(a_K,d_K)=1.
$$


Put


$$
y_K=d_KE_K-a_K,\qquad
\gamma=\gcd(\tau,y_K),\qquad
b^\circ=\gcd(\gamma,a_K),\qquad r^\circ=\gamma/b^\circ.
$$


For every prime,


$$
c_p=\min(v_p(U),v_p(V)),\qquad t_p=v_p(U)-c_p,
$$




$$
z_p=v_p(y_K),\qquad b_p=v_p(b^\circ),\qquad
h_p=v_p(Q_{N-1}^{\rm H}Q_N^{\rm H}),
$$


and


$$
\boxed{H_p=h_p+2b_p+2(z_p-t_p)_+.}
$$


The Hermite credit remains at $N-1,N$.

The branch under audit is


$$
\mathcal S_N=
\left\{
\begin{array}{l|l}
p&
N<p<2N,\quad p\nmid L(\ell^2),\\
&d_{p,N}^{\rm block}=p^2,\quad
v_p(\Delta)\le v_p(J_N^{\rm aff})
\end{array}
\right\}.
$$


In particular,


$$
p^2\mid U,V.
$$


Write


$$
r=n-p,\qquad s=r-6=\ell-p,\qquad
a=\frac{p-1}{2},\qquad k=a+1.
$$


The retained boundaries are


$$
13\le r<N,\qquad s\ge7,\qquad r,s\ \text{odd},\qquad k\le N-6,
$$


and $p\nmid d_K$.

Set


$$
B_p=(H_p-2)_+,\qquad
e_p=[c_p-2-B_p]_+,\qquad
j_p=v_p(J_N^{\rm aff}).
$$


The first two layers are already paid:


$$
\sum_{p\in\mathcal S_N}[2-H_p]_+\log p\le4N\log2.
$$



---

# 2. FULL20: mixed forcing, polynomial elimination, and critical-safe charts

## 2.1 Exact mixed signs and seed — PASS

Define


$$
x_j=\Theta_{p+j}-\Theta_j,\qquad
y_j=\Phi_{p+j}+\Phi_j,\qquad 0\le j\le r.
$$


The plus sign in $y_j$ is essential because $p$ is odd. Direct subtraction gives


$$
x_{j+1}+4(p+j)x_j-x_{j-1}=-4p\Theta_j,
$$




$$
y_{j+1}+4(p+j)y_j-y_{j-1}=4p\Phi_j.
$$


These are not homogeneous systems.

Let


$$
\mathfrak D_{j;p}=x_jy_{j-1}-x_{j-1}y_j.
$$


At $j=1$,


$$
x_1=-4p\Theta_p+\Theta_{p-1}+1,
$$




$$
y_1=-4p\Phi_p+\Phi_{p-1}-1.
$$


Consequently,


$$
\boxed{
\mathfrak D_{1;p}
=(\Theta_{p-1}+1)\Phi_p-\Theta_p(\Phi_{p-1}-1).
}
$$



Using the two forced recurrences,


$$
\begin{aligned}
\mathfrak D_{j+1;p}
&=-\mathfrak D_{j;p}
-4p(\Theta_jy_j+\Phi_jx_j)\\
&=-\mathfrak D_{j;p}
-4p(\Theta_j\Phi_{p+j}+\Phi_j\Theta_{p+j}).
\end{aligned}
$$


Thus, with


$$
\mathfrak M_{j;p}
=-(\Theta_j\Phi_{p+j}+\Phi_j\Theta_{p+j}),
$$


the correct evolution is


$$
\boxed{
\mathfrak D_{j+1;p}=-\mathfrak D_{j;p}+4p\mathfrak M_{j;p}.
}
$$



The previously passed Hermite anchor is reused. The Hermite sequence is defined on $0\le b\le N$ by


$$
P_0^{\rm H}=Q_0^{\rm H}=1,\qquad
P_1^{\rm H}=3,\quad Q_1^{\rm H}=1,
$$




$$
Z_{b+1}=(4b+2)Z_b+Z_{b-1},\qquad 1\le b\le N-1.
$$


Put $\chi=2k!$. All four actual defects are


$$
\sigma_0^+=\frac{\Theta_p-\chi Q_a^{\rm H}}p,\qquad
\sigma_1^+=\frac{\Theta_{p-1}+1+\chi Q_k^{\rm H}}p,
$$




$$
\sigma_0^-=\frac{\Phi_p-\chi P_a^{\rm H}}p,\qquad
\sigma_1^-=\frac{\Phi_{p-1}-1+\chi P_k^{\rm H}}p.
$$


Their integrality is reused; they are not free parameters.

Expanding the seed with these four defects gives


$$
\boxed{
\mathfrak D_{1;p}
=2(-1)^a\chi^2+p\chi\Lambda_\sigma+p^2\Xi_\sigma,
}
$$


where


$$
\Lambda_\sigma=
P_k^{\rm H}\sigma_0^+
+P_a^{\rm H}\sigma_1^+
-Q_k^{\rm H}\sigma_0^-
-Q_a^{\rm H}\sigma_1^-,
$$




$$
\Xi_\sigma=\sigma_1^+\sigma_0^--\sigma_0^+\sigma_1^-.
$$


The constant term uses


$$
P_k^{\rm H}Q_a^{\rm H}-P_a^{\rm H}Q_k^{\rm H}=2(-1)^a.
$$



Since $k<p$, $\chi$ is a $p$-adic unit. Hence


$$
\boxed{p\nmid\mathfrak D_{j;p}\qquad(1\le j\le r).}
$$



For the full return, define


$$
\mathfrak f_{1;p}=0,\qquad
\mathfrak f_{j+1;p}=\mathfrak M_{j;p}-\mathfrak f_{j;p}.
$$


Then


$$
\mathfrak D_{j;p}=(-1)^{j-1}\mathfrak D_{1;p}+4p\mathfrak f_{j;p}.
$$


Because $s$ is odd,


$$
\boxed{
\mathfrak D_{s;p}
=2(-1)^a\chi^2+p\chi\Lambda_\sigma+p^2\Xi_\sigma
+4p\mathfrak f_{s;p}.
}
$$


Equivalently,


$$
\mathfrak f_{s;p}
=-\sum_{t=1}^{s-1}(-1)^t
(\Theta_t\Phi_{p+t}+\Phi_t\Theta_{p+t}).
$$



Every shifted state has index at most $p+r=n$; every recurrence step has index at most $n-1$.

## 2.2 Positivity and factorial bounds — PASS

To avoid confusing state magnitudes with Gaussian coordinates, write


$$
\vartheta_j=(-1)^{j-1}\Theta_j,\qquad
\varphi_j=(-1)^{j-1}\Phi_j.
$$


Then


$$
\vartheta_{j+1}=4j\vartheta_j+\vartheta_{j-1}+2(-1)^j,
$$




$$
\varphi_{j+1}=4j\varphi_j+\varphi_{j-1}+2,
$$


with


$$
\vartheta_1=\varphi_1=1,\qquad
\vartheta_2=2,\quad\varphi_2=6.
$$


Induction gives


$$
0<\vartheta_j\le\varphi_j,
$$


and, for $j\ge2$,


$$
2\,3^{j-2}(j-1)!
\le\vartheta_j\le\varphi_j
\le6^{j-1}(j-1)!.
$$



For the seed estimate, let


$$
C_j^\ast=\vartheta_j\varphi_{j-1}
-\vartheta_{j-1}\varphi_j.
$$


Its recurrence is


$$
C_{j+1}^\ast=-C_j^\ast+2(-1)^j\varphi_j-2\vartheta_j.
$$


It follows that $C_j^\ast>0$ for odd $j\ge3$ and $C_j^\ast<0$ for even $j\ge2$. The growth of $\vartheta_j+\varphi_j$ gives


$$
|C_p^\ast|
\le2\sum_{j=1}^{p-1}(\vartheta_j+\varphi_j)
<4(\vartheta_{p-1}+\varphi_{p-1})
\le\frac23(\vartheta_p+\varphi_p).
$$


For odd $p$,


$$
\mathfrak D_{1;p}
=\vartheta_p+\varphi_p+C_p^\ast,
$$


so


$$
0<\mathfrak D_{1;p}<2(\vartheta_p+\varphi_p).
$$



Opposite parity of $j$ and $p+j$ gives


$$
\mathfrak M_{j;p}
=\vartheta_j\varphi_{p+j}
+\varphi_j\vartheta_{p+j}>0.
$$


Moreover,


$$
\mathfrak M_{1;p}\ge3p(\vartheta_p+\varphi_p),
\qquad
\mathfrak M_{j+1;p}\ge2\mathfrak M_{j;p}.
$$


The determinant recurrence therefore yields


$$
2p\mathfrak M_{j-1;p}
<\mathfrak D_{j;p}
<4p\mathfrak M_{j-1;p}
\qquad(j\ge2).
$$



At $j=s$,


$$
\mathfrak M_{s-1;p}
=\vartheta_{s-1}\varphi_{\ell-1}
+\varphi_{s-1}\vartheta_{\ell-1}.
$$


Substitution of the state bounds proves exactly


$$
\boxed{
16p\,3^{\ell+s-6}(\ell-2)!(s-2)!
<
\mathfrak D_{s;p}
<
8p\,6^{\ell+s-4}(\ell-2)!(s-2)!.
}
$$


Thus the stated constants and strict positivity pass.

The proposed factorial cancellation fails for the stated arithmetic reason:


$$
\ell-2=p+s-2,\qquad 0<s-2<p,\qquad \ell-2<2p.
$$


Therefore


$$
v_p((\ell-2)!(s-2)!)=1,
\qquad
v_p(\mathfrak D_{s;p})=0.
$$


The quotient by that factorial product is not integral at the prime being studied.

## 2.3 Actual mixed columns and source/endpoint subtraction — PASS

Write


$$
\mathbf t_j=\binom{\Theta_j}{\Theta_{j-1}},\qquad
\mathbf f_j=\binom{\Phi_j}{\Phi_{j-1}},
$$




$$
\mathsf M_c=
\begin{pmatrix}\mathscr A&\mathscr B\\\Pi&\Omega\end{pmatrix},
\qquad
\mathbf C=\binom{\mathscr C_U}{C^{\rm s}},\qquad
\mathbf u=\binom{16U}{V}.
$$


Then


$$
\mathbf u=\mathbf C-\mathsf M_c\mathbf t_\ell.
$$



The actual residual source column is


$$
\mathbf R=\mathbf C-\mathsf M_c\mathbf t_s.
$$


The complete relative endpoint is


$$
\mathbf E=
\binom{
16E_K-\mathscr C_E+\mathscr A\Phi_s+\mathscr B\Phi_{s-1}
}{
C^{\rm e}-E_F+\Pi\Phi_s+\Omega\Phi_{s-1}
}.
$$


The signs and subtractions give


$$
\boxed{\mathbf E=\mathsf M_c(\mathbf f_\ell+\mathbf f_s).}
$$



Consequently,


$$
\mathsf M_c(\mathbf t_\ell-\mathbf t_s)=\mathbf R-\mathbf u,
$$


and


$$
\det(\mathbf R-\mathbf u,\mathbf E)=\Delta\mathfrak D_{s;p}.
$$



Define


$$
\mathfrak A_{p,N}=\det(\mathbf R,\mathbf u),
\qquad
\mathfrak B_{p,N}=\det(\mathbf u,\mathbf E).
$$


Then


$$
\boxed{
\mathfrak B_{p,N}=R_1E_2-R_2E_1-\Delta\mathfrak D_{s;p}.
}
$$


The complete seed and forcing expansion is therefore


$$
\boxed{
\begin{aligned}
\mathfrak B_{p,N}
={}&R_1E_2-R_2E_1\\
&-\Delta\left(
2(-1)^a\chi^2+p\chi\Lambda_\sigma+p^2\Xi_\sigma
+4p\mathfrak f_{s;p}\right).
\end{aligned}
}
$$



A two-dimensional determinant identity, without any division, gives


$$
(\mathbf R-\mathbf u)\mathfrak B_{p,N}
+\mathbf E\,\mathfrak A_{p,N}
=\Delta\mathfrak D_{s;p}\mathbf u.
$$


Since $\Delta\ne0$, $\mathfrak D_{s;p}>0$, and $16U>0$, the two mixed minors are not both zero as integers.

Expanding the other minor gives


$$
\boxed{
\begin{aligned}
\mathfrak A_{p,N}
={}&\mathscr I_1(\Theta_s-\Theta_\ell)
+\mathscr I_2(\Theta_{s-1}-\Theta_{\ell-1})\\
&+\Delta(\Theta_s\Theta_{\ell-1}
-\Theta_{s-1}\Theta_\ell).
\end{aligned}
}
$$



These formulas use coefficients at the actual original $N$. They do not form a new producer by replacing $N$ with $s$.

## 2.4 Corrected $K$-row primitivity and elimination — PASS

Suppose $p\in\mathcal S_N$. First, $p\nmid\ell$: since $0<\ell<2p$, divisibility would force $\ell=p$, impossible because $\ell$ is even and $p$ is odd.

If $p\mid\mathscr A,\mathscr B$, the definitions imply


$$
\mathcal Q(\ell^2)\equiv\mathcal P(\ell^2)\equiv0\pmod p.
$$


Because $p\mid U$, the corrected source constant gives


$$
\mathscr C_U\equiv0\pmod p,
$$


hence also


$$
\mathcal F(\ell^2)\equiv0\pmod p.
$$



The exact polynomial eliminations are


$$
\mathcal Q-19\mathcal F=-20(347x+4908),
$$




$$
\mathcal P+(2x+33)\mathcal F=2(9506x+90215).
$$


Thus a common zero would force


$$
347x+4908\equiv0,\qquad
9506x+90215\equiv0\pmod p.
$$


Elimination without dividing by either leading coefficient gives


$$
p\mid347\cdot90215-9506\cdot4908=-15\,350\,843.
$$


But $p>N\ge3^{36}>15\,350\,843$. Therefore


$$
\boxed{\min(v_p(\mathscr A),v_p(\mathscr B))=0.}
$$



This argument genuinely uses the corrected $\mathscr C_U$. A determinant of the two coefficient rows alone would not prove it.

## 2.5 Both critical-safe charts — PASS, but not source noncollision

The matrix


$$
\begin{pmatrix}
x_s&y_s\\x_{s-1}&y_{s-1}
\end{pmatrix}
$$


has determinant $\mathfrak D_{s;p}$, a unit modulo $p$.

If $R_1\equiv E_1\equiv0\pmod p$, then $16U\equiv0\pmod p$ and the first row of the two column identities would force


$$
(\mathscr A,\mathscr B)
\begin{pmatrix}
x_s&y_s\\x_{s-1}&y_{s-1}
\end{pmatrix}
\equiv(0,0)\pmod p.
$$


This contradicts $K$-row primitivity. Hence


$$
\boxed{\min(v_p(R_1),v_p(E_1))=0.}
$$



Choose


$$
\zeta_{p,N}=
\begin{cases}
\mathfrak A_{p,N},&p\nmid R_1,\\
\mathfrak B_{p,N},&p\mid R_1.
\end{cases}
$$


In the first chart,


$$
(u_1,u_2)\longmapsto(u_1,R_1u_2-R_2u_1)
$$


has unit determinant $R_1$. In the second,


$$
(u_1,u_2)\longmapsto(u_1,E_2u_1-E_1u_2)
$$


has unit determinant $-E_1$. Therefore


$$
\boxed{
c_p=\min(v_p(16U),v_p(\zeta_{p,N})),
}
$$


and, after the proved double collision,


$$
\boxed{
c_p-2
=\min\left(v_p(16U/p^2),v_p(\zeta_{p,N}/p^2)\right).
}
$$



This proof never inverts $\Delta$. It applies at determinant-critical primes.

However, the unit chart is **not** noncollision of the source pair. It is an invertible change of contact coordinates. It remains compatible with arbitrarily deep common divisibility of the two source entries unless further arithmetic information is supplied.

## 2.6 All-prime gcd identities and exact contact comparison — PASS

Let


$$
g_0=\gcd(16U,V),\qquad \mathbf w=\mathbf u/g_0.
$$


The integer vector $\mathbf w$ is primitive. Set


$$
j_{p,N}
=\gcd(\det(\mathbf R,\mathbf w),\det(\mathbf w,\mathbf E)).
$$


Then


$$
\boxed{
\gcd(\mathfrak A_{p,N},\mathfrak B_{p,N})
=g_0j_{p,N}.
}
$$



Dividing the determinant identity by $g_0$ gives an integer identity whose right side is


$$
\Delta\mathfrak D_{s;p}\mathbf w.
$$


Since the coordinates of $\mathbf w$ are coprime,


$$
\boxed{j_{p,N}\mid\Delta\mathfrak D_{s;p}.}
$$


Thus, at the selected prime,


$$
0\le v_p(j_{p,N})\le v_p(\Delta).
$$



The conditioning-free gcd is


$$
I_{p,N}=\gcd(16U,\mathfrak A_{p,N},\mathfrak B_{p,N}).
$$


Reduction modulo the first gcd entry gives the all-prime identity


$$
\boxed{
I_{p,N}
=g_0\gcd\left(\frac{16U}{g_0},R_1,E_1\right).
}
$$


The unit-chart result therefore yields


$$
\boxed{v_p(I_{p,N})=c_p.}
$$



The distinction at $2$ is retained: $g_0$ need not equal $c$. The actual source content remains $c=\gcd(U,V)$.

Since $p^2\mid I_{p,N}$, the division


$$
Z_{p,N}=I_{p,N}/p^2
$$


is integral. Moreover,


$$
\boxed{
v_p\!\left(
\frac{Z_{p,N}}{\gcd(Z_{p,N},p^{B_p})}
\right)=e_p.
}
$$


This is the complete conditioning-free post-credit comparison. It does not drop $h_p$, $b_p$, $z_p$, or $t_p$.

A useful audit consequence is that the two-minor contact has only a conditioning discrepancy:


$$
\min(v_p(\mathfrak A_{p,N}),v_p(\mathfrak B_{p,N}))
=c_p+v_p(j_{p,N}),
$$


where $0\le v_p(j_{p,N})\le v_p(\Delta)$. Applying the $1$-Lipschitz function $x\mapsto[x-2-B_p]_+$ shows that the corresponding paid masses differ by at most


$$
\sum_{p\in\mathcal S_N}v_p(\Delta)\log p\le\log|\Delta|.
$$


This bounds a **difference of contact masses**, not either mass absolutely.

## 2.7 Mixed-minor height and Gaussian homogeneity — PASS

Let


$$
F_j^\ast=1+\vartheta_j+\varphi_j+\vartheta_{j-1}+\varphi_{j-1}.
$$


The coefficient bounds imply residual estimates at scale $F_s^\ast$, terminal estimates at scale $F_\ell^\ast$, and


$$
|\Delta|\le2\cdot10^{10}n^{15}H_G.
$$


Using


$$
\mathfrak D_{s;p}<4nF_s^\ast F_\ell^\ast
$$


in the additive expression for $\mathfrak B$, rather than bounding two terminal products separately, gives


$$
\boxed{
|\mathfrak A_{p,N}|,\ |\mathfrak B_{p,N}|
<10^{12}n^{16}H_GF_s^\ast F_\ell^\ast.
}
$$



Each minor contains exactly one Gaussian quadratic row. Accordingly,


$$
\mathfrak A_{\rm raw}=g_B^2\mathfrak A_{p,N},\qquad
\mathfrak B_{\rm raw}=g_B^2\mathfrak B_{p,N}.
$$


This does not authorize putting the same raw factor into the $K$-source coordinate $16U$. The actual Gaussian division must precede the mixed gcd or contact test.

---

# 3. FULL21: actual primitive normalization and factorial-height obstruction

## 3.1 Least simultaneous clearer — PASS over all primes

Define


$$
d_{\rm mix}
=\gcd(\mathfrak D_{s;p},\mathfrak A_{p,N},\mathfrak B_{p,N}),
$$




$$
A_{\rm mix}=\mathfrak A_{p,N}/d_{\rm mix},\quad
B_{\rm mix}=\mathfrak B_{p,N}/d_{\rm mix},\quad
D_{\rm mix}=\mathfrak D_{s;p}/d_{\rm mix}.
$$


Then


$$
\gcd(A_{\rm mix},B_{\rm mix},D_{\rm mix})=1.
$$



For any prime $q$, the least exponent needed to clear both rational numbers


$$
\frac{\mathfrak A_{p,N}}{\mathfrak D_{s;p}},
\qquad
\frac{\mathfrak B_{p,N}}{\mathfrak D_{s;p}}
$$


is


$$
v_q(\mathfrak D_{s;p})
-\min\bigl(v_q(\mathfrak D_{s;p}),
v_q(\mathfrak A_{p,N}),v_q(\mathfrak B_{p,N})\bigr).
$$


This is exactly $v_q(D_{\rm mix})$. Thus $D_{\rm mix}$ is the actual least simultaneous clearer, including the prime $2$.

At the selected prime,


$$
\boxed{v_p(d_{\rm mix})=v_p(D_{\rm mix})=0.}
$$


The normalization removes none of the selected prime’s source contact.

The term “primitive mixed pair” must not be read as
$\gcd(A_{\rm mix},B_{\rm mix})=1$. It is the **triple**
$(A_{\rm mix},B_{\rm mix},D_{\rm mix})$ that is primitive.

## 3.2 Moment comparison and residual sign — PASS

The retained finite moment identities are


$$
\eta(C_j)=1-2j\Theta_j,\qquad
E(C_j)=(-1)^j-2j\Phi_j.
$$


Finite integration by parts gives


$$
\int_0^1e^tH(t)\,dt=e\,\eta(H)-E(H).
$$


Hence


$$
\boxed{
\rho_j:=\Phi_j-e\Theta_j
=\frac{\int_0^1e^tC_j(t)\,dt-e+(-1)^j}{2j}.
}
$$


Since $|C_j(t)|\le1$ on $[0,1]$,


$$
|\rho_j|\le e/j<3/j.
$$



The sign of $R_1$ is also correct. At $x=\ell^2\ge1$,


$$
\mathcal P<0,\qquad \mathcal Q>0,\qquad\mathcal F>0,
$$


so $\mathscr A>0$ and $\mathscr B<0$. Furthermore,


$$
\mathscr A-\mathscr C_U
=4\ell^2\mathcal Q-(2\ell-1)\mathcal P-\mathcal F,
$$


and


$$
4x\mathcal Q-\mathcal F
=304x^3+9628x^2+22056x-5463>0.
$$


Thus $\mathscr A>\mathscr C_U$. Since $s$ is odd,


$$
\Theta_s\ge1,\qquad\Theta_{s-1}<0,
$$


and therefore


$$
\boxed{R_1<0.}
$$



## 3.3 Primitive integer relation: a division-free derivation — PASS

Put


$$
\mathbf v=\operatorname{adj}(\mathsf M_c)\mathbf C
=\binom{\mathscr I_2}{-\mathscr I_1},
$$




$$
\mathbf x=\mathbf t_\ell-\mathbf t_s,\qquad
\mathbf y=\mathbf f_\ell+\mathbf f_s,
$$


and


$$
\mathbf z=\operatorname{adj}(\mathsf M_c)\mathbf u
=\mathbf v-\Delta\mathbf t_\ell.
$$



For any $2\times2$ matrix $M$,


$$
\det(Mx,u)=\det(x,\operatorname{adj}(M)u).
$$


It follows directly that


$$
\mathfrak A_{p,N}=\det(\mathbf x,\mathbf z),\qquad
\mathfrak B_{p,N}=\det(\mathbf z,\mathbf y).
$$


The elementary vector identity


$$
\mathbf x\det(\mathbf z,\mathbf y)
+\mathbf y\det(\mathbf x,\mathbf z)
=\mathbf z\det(\mathbf x,\mathbf y)
$$


now gives


$$
\mathfrak B_{p,N}\mathbf x+\mathfrak A_{p,N}\mathbf y
=\mathfrak D_{s;p}(\mathbf v-\Delta\mathbf t_\ell).
$$


Division only by the proved common divisor $d_{\rm mix}$ yields


$$
\boxed{
\Delta D_{\rm mix}\mathbf t_\ell
+B_{\rm mix}(\mathbf t_\ell-\mathbf t_s)
+A_{\rm mix}(\mathbf f_\ell+\mathbf f_s)
=D_{\rm mix}\mathbf v.
}
$$


This proof uses no inverse of $\Delta$, even temporarily.

## 3.4 Denominator controlled by numerator height — PASS

Let


$$
H_{\rm num}=\max(|A_{\rm mix}|,|B_{\rm mix}|),\qquad
T=|\Theta_\ell|,\qquad S=\Theta_s.
$$


The state signs and growth give


$$
0<S<T,\qquad |x_s|=T+S<2T.
$$


Also,


$$
|y_s|=\varphi_\ell-\varphi_s<\varphi_\ell<3T,
$$


the last inequality following from $\varphi_\ell\le eT+3/\ell$ on the original domain.

The coefficient bounds give


$$
|\mathscr I_2|<2\cdot10^{10}n^{15}H_G<e^{8N}.
$$


On the other hand,


$$
T\ge(2N-7)!\ge(N-3)^{N-3}>e^{20N}.
$$


The final inequality follows, for example, from


$$
N-3\ge3N/4,\qquad \log(N-3)>35
$$


on $N\ge3^{36}$. Thus $|\mathscr I_2|<T/2$.

The first coordinate of the integer relation gives


$$
D_{\rm mix}(\Delta\Theta_\ell-\mathscr I_2)
=-B_{\rm mix}x_s-A_{\rm mix}y_s.
$$


Since $\Delta$ is a nonzero integer,


$$
|\Delta\Theta_\ell-\mathscr I_2|>T/2.
$$


Therefore


$$
\boxed{D_{\rm mix}\le10H_{\rm num}.}
$$



All constants here are genuine bounds on the original domain, not merely asymptotic notation.

## 3.5 Nonzero integer linear form and corrected residual sign — PASS

Set


$$
W_0=B_{\rm mix}+\Delta D_{\rm mix}.
$$


If $A_{\rm mix}=W_0=0$, the primitive integer relation gives


$$
\mathbf v=\Delta\mathbf t_s.
$$


Multiplication by $\mathsf M_c$ then gives


$$
\mathbf C=\mathsf M_c\mathbf t_s,
$$


contradicting $R_1<0$. Hence


$$
\boxed{(A_{\rm mix},W_0)\ne(0,0).}
$$



Using $\Phi_j=e\Theta_j+\rho_j$ in the first coordinate gives the exact identity


$$
\boxed{
(W_0+eA_{\rm mix})\Theta_\ell
=D_{\rm mix}\mathscr I_2
+(B_{\rm mix}-eA_{\rm mix})\Theta_s
-A_{\rm mix}(\rho_\ell+\rho_s).
}
$$


In particular, the residual coefficient is


$$
B_{\rm mix}-eA_{\rm mix},
$$


not $B_{\rm mix}+eA_{\rm mix}$.

Since $s\ge7$,


$$
|\rho_\ell+\rho_s|<1.
$$


Thus, with


$$
F_0=10|\mathscr I_2|+4S+1,
$$




$$
\boxed{
|W_0+eA_{\rm mix}|\le H_{\rm num}\frac{F_0}{T}.
}
$$



## 3.6 Finite adjacent Hermite separation — PASS

Define


$$
f_j(t)=\frac{t^j(1-t)^j}{j!},\qquad
I_j=\int_0^1e^tf_j(t)\,dt.
$$


For $j\ge1$,


$$
f_{j+1}''=f_{j-1}-(4j+2)f_j.
$$


Both $f_{j+1}$ and $f_{j+1}'$ vanish at the endpoints, so two integrations by parts give


$$
I_{j+1}=I_{j-1}-(4j+2)I_j.
$$


With


$$
I_0=e-1,\qquad I_1=3-e,
$$


comparison with the specified Hermite recurrence proves


$$
\boxed{
Q_j^{\rm H}e-P_j^{\rm H}
=\frac{(-1)^j}{j!}\int_0^1e^tt^j(1-t)^j\,dt.
}
$$


Consequently,


$$
|Q_j^{\rm H}e-P_j^{\rm H}|
<\frac{3j!}{(2j+1)!},
\qquad
Q_j^{\rm H}\le6^jj!.
$$



At the admissible adjacent indices $a,k=a+1$, define


$$
J_j=W_0Q_j^{\rm H}+A_{\rm mix}P_j^{\rm H}.
$$


The determinant


$$
P_k^{\rm H}Q_a^{\rm H}-P_a^{\rm H}Q_k^{\rm H}=2(-1)^a
$$


shows that $J_a,J_k$ cannot both vanish. For a nonzero one,


$$
\begin{aligned}
1
&\le |J_j|\\
&\le H_{\rm num}\left(
Q_k^{\rm H}\frac{F_0}{T}
+\frac{3a!}{(2a+1)!}\right).
\end{aligned}
$$


Hence


$$
\boxed{
H_{\rm num}\ge
\left(
Q_k^{\rm H}\frac{F_0}{T}
+\frac{3a!}{(2a+1)!}\right)^{-1}.
}
$$



This is ordinary integer separation. No determinant-$2$ factor is inverted modulo a prime.

## 3.7 Constants $16$ and $28$ — PASS

The source estimates give


$$
S\le e^{2N}N^s,\qquad F_0\le e^{9N}N^s.
$$


Also,


$$
T\ge(\ell-1)!\ge N^\ell e^{-3N}.
$$


Thus


$$
\frac{F_0}{T}\le e^{12N}N^{-p}.
$$


Since $k\le N-6$,


$$
Q_k^{\rm H}\le e^{2N}N^k,
$$


and therefore


$$
Q_k^{\rm H}\frac{F_0}{T}
\le e^{14N}N^{-a}.
$$


Because $N,p$ are odd and $p>N$, $a>N/2$, so


$$
\frac{3a!}{(2a+1)!}
\le3\left(\frac2N\right)^{a+1}
\le e^{2N}N^{-a}.
$$


The evaluated separation bound consequently gives the slightly stronger intermediate estimate


$$
H_{\rm num}\ge N^ae^{-15N},
$$


and hence the stated


$$
\boxed{H_{\rm num}\ge N^ae^{-16N}.}
$$



For the actual real quotient, the state estimates imply


$$
F_j^\ast\le3\cdot6^{j-1}(j-1)!.
$$


Combining the mixed-minor upper bound with the determinant lower bound gives


$$
\begin{aligned}
\frac{\max(|\mathfrak A_{p,N}|,|\mathfrak B_{p,N}|)}
{\mathfrak D_{s;p}}
&<
\frac{729}{64}\,10^{12}n^{16}H_G
\frac{(\ell-1)(s-1)}p\,2^{\ell+s}\\
&<10^{14}n^{18}H_G\,2^{\ell+s}\\
&<e^{12N}.
\end{aligned}
$$


Primitive normalization preserves this quotient. Therefore


$$
\boxed{
D_{\rm mix}>e^{-12N}H_{\rm num}
\ge N^ae^{-28N}.
}
$$



The bounds are pointwise and uniform on the stated original scope. They do not use the double-collision or determinant-depth parts of $\mathcal S_N$, although those hypotheses remain necessary for the contact applications.

## 3.8 What the height theorem actually obstructs

For any unbounded family of eligible original pairs,


$$
\frac{\log H_{\rm num}}N
\ge\frac12\log N-16,
$$




$$
\frac{\log D_{\rm mix}}N
\ge\frac12\log N-28.
$$


Thus no fixed exponential upper bound $e^{CN}$ can hold for the actual primitive numerator pair or actual least simultaneous clearer on such a family.

This does **not** assert that eligible pairs occur for infinitely many original $N$.

The all-prime statement is


$$
\log D_{\rm mix}
=\sum_q\left(
v_q(\mathfrak D_{s;p})
-\min(v_q(\mathfrak D_{s;p}),v_q(\mathfrak A_{p,N}),
v_q(\mathfrak B_{p,N}))
\right)\log q
\ge a\log N-28N.
$$


The chosen prime contributes zero. The surviving denominator mass is at other primes, without any claimed classification of them.

### Additional proved audit corollary: normalization rigidity

Suppose integers $A',B'$ and $D'>0$ represent the same two mixed ratios. By least simultaneous clearing,


$$
D'=tD_{\rm mix}
$$


for some positive integer $t$, and then


$$
A'=tA_{\rm mix},\qquad B'=tB_{\rm mix}.
$$


Consequently every integral realization of these same two ratios satisfies


$$
\max(|A'|,|B'|)\ge N^ae^{-16N},\qquad
D'\ge N^ae^{-28N}.
$$



Thus merely choosing a different common integer clearer cannot repair the failed height mechanism. A successful repair would have to change the auxiliary or supply a separately proved, credit-aware arithmetic reduction.

## 3.9 Norm and credit implications — PASS, with no mass bound

At $p\in\mathcal S_N$,


$$
p^{c_p}\mid A_{\rm mix},B_{\rm mix}.
$$


The nonzero integer


$$
\mathcal N_{p,N}=A_{\rm mix}^2+B_{\rm mix}^2
$$


therefore satisfies $v_p(\mathcal N_{p,N})\ge2c_p$. Hence


$$
\mathcal N_{p,N}^{(2)}=\mathcal N_{p,N}/p^4\in\mathbb Z_{>0}.
$$


Define the actually paid quotient


$$
\mathcal C_{p,N}
=\frac{\mathcal N_{p,N}^{(2)}}
{\gcd(\mathcal N_{p,N}^{(2)},p^{2B_p})}.
$$


Then


$$
\boxed{p^{2e_p}\mid\mathcal C_{p,N}.}
$$



Only a lower valuation bound is used. A sum of two squares may have additional $p$-adic cancellation.

The height lower bounds give


$$
\log\mathcal N_{p,N}^{(2)}
\ge(p-1)\log N-33N,
$$


and


$$
\boxed{
\log\mathcal C_{p,N}
\ge(p-1)\log N-33N-2B_p\log p.
}
$$


No upper bound on $B_p$ is proved. Therefore this does not show that every fully credited quotient remains factorially large.

For any $\mathcal T\subseteq\mathcal S_N$,


$$
\prod_{p\in\mathcal T}p^{2e_p}
\mid\prod_{p\in\mathcal T}\mathcal C_{p,N}.
$$


This is a valid divisor statement, but it has no proved $O(N)$ aggregate height bill. The auxiliaries vary with $p$.

---

# 4. FULL22: actual Hermite normalization and cubic defects

## 4.1 Arithmetic setting and exact coefficient normalization

All congruences in this section are in $\mathbb Z_{(p)}$. Rational denominators remaining after the explicitly paid cancellations are units at $p$.

For $0\le h\le a$, define


$$
\mathsf h_{a,h}=\frac{(2a-h)!}{(a-h)!\,h!}.
$$


These are actual integer Hermite coefficients. For $1\le j\le a$, define


$$
\mathsf b_j=\frac{4^jj!((j-1)!)^2}{2(2j)!}.
$$


Since $2j\le p-1$, these are $p$-adic units, with


$$
\mathsf b_1=1,\qquad
\mathsf b_{j+1}=\frac{2j^2}{2j+1}\mathsf b_j.
$$



Let


$$
Y_a(x)=\sum_{j=0}^a\frac{(a+j)!}{j!(a-j)!}x^j.
$$


The factorial coefficient recurrence gives


$$
Y_{a+1}(x)=(4a+2)xY_a(x)+Y_{a-1}(x).
$$


Its initial values identify


$$
P_a^{\rm H}=Y_a(1),\qquad
Q_a^{\rm H}=(-1)^aY_a(-1).
$$


Reversal of coefficients therefore proves


$$
\boxed{
P_a^{\rm H}=\sum_{h=0}^a\mathsf h_{a,h},\qquad
Q_a^{\rm H}=\sum_{h=0}^a(-1)^h\mathsf h_{a,h}.
}
$$



Now let


$$
q(z)=T_p(1-2z).
$$


The Chebyshev differential equation gives the coefficient recursion


$$
(j+1)\left(j+\frac12\right)[z^{j+1}]q
+(p^2-j^2)[z^j]q=0.
$$


Starting from $q(0)=1$, this yields


$$
[z^j]q
=(-4)^j\frac{p^2\prod_{v=1}^{j-1}(p^2-v^2)}{(2j)!}.
$$


Define the exact rational number


$$
w_j=-\frac{j![z^j]q}{2p}.
$$


The complete moment identities give


$$
\Theta_p=\sum_{j=1}^pw_j,\qquad
\Phi_p=\sum_{j=1}^p(-1)^{j+1}w_j.
$$


For the lower half,


$$
\boxed{
w_j=p\mathsf b_j
\prod_{v=1}^{j-1}\left(1-\frac{p^2}{v^2}\right),
\qquad 1\le j\le a.
}
$$


The leading term and ratio are


$$
w_p=4^{p-1}(p-1)!,
$$




$$
\frac{w_{j+1}}{w_j}
=\frac{2(j^2-p^2)}{2j+1}.
$$



Put


$$
R_h(x)=\prod_{t=1}^h
\frac{1-x/(2t-1)}{1-x/t}.
$$


Backward multiplication of the exact ratio gives


$$
w_{p-h}
=(-1)^h4^{p-1}(p-1)!
\frac{(2h)!}{4^h(h!)^3}R_h(2p).
$$


Since


$$
\chi=2(a+1)!=(p+1)a!,
$$


the actual Hermite coefficient satisfies


$$
\chi\mathsf h_{a,h}
=(p+1)(p-1)!
\frac{(2h)!}{4^h(h!)^3}R_h(p).
$$


Therefore


$$
\boxed{
w_{p-h}
=(-1)^h\chi\mathsf h_{a,h}
\frac{4^{p-1}}{p+1}\frac{R_h(2p)}{R_h(p)}.
}
$$



This exact normalization passes. The common terminal factor cancels between these two explicitly identified coefficient expressions. It is not a divisor statement about $U$, $V$, a mixed minor, or the original producer.

## 4.2 Every cubic reciprocal-power and Fermat term — PASS

Write


$$
H_t^{(d)}=\sum_{v=1}^t v^{-d},\qquad H_0^{(d)}=0.
$$


All indices here are at most $p-1$. Define


$$
L_{1,h}=\frac32H_h^{(1)}-H_{2h}^{(1)},
$$




$$
L_{2,h}=\frac{15}{4}H_h^{(2)}-3H_{2h}^{(2)},
$$




$$
L_{3,h}=\frac{63}{8}H_h^{(3)}-7H_{2h}^{(3)},
$$




$$
E_{2,h}=\frac{L_{1,h}^2+L_{2,h}}2,
$$




$$
E_{3,h}=
\frac{L_{1,h}^3+3L_{1,h}L_{2,h}+2L_{3,h}}6.
$$



The actual Fermat quotient and scalar are


$$
q_p(4)=\frac{4^{p-1}-1}{p},\qquad
\mu_p=\frac{q_p(4)-1}{p+1}.
$$


Fermat’s theorem pays the first division, and


$$
\frac{4^{p-1}}{p+1}=1+p\mu_p
$$


is exact.

The logarithm of the product ratio, used only as a finite formal expansion through degree three, is


$$
\log\frac{R_h(2p)}{R_h(p)}
=
\sum_{d\ge1}\frac{(2^d-1)p^d}{d}
\left(H_h^{(d)}-\sum_{t=1}^h(2t-1)^{-d}\right).
$$


Since


$$
\sum_{t=1}^h(2t-1)^{-d}
=H_{2h}^{(d)}-2^{-d}H_h^{(d)},
$$


the first three logarithmic coefficients are


$$
pL_{1,h}+\frac{p^2}2L_{2,h}+\frac{p^3}3L_{3,h}.
$$


Exponentiation gives


$$
\frac{R_h(2p)}{R_h(p)}
\equiv1+pL_{1,h}+p^2E_{2,h}+p^3E_{3,h}\pmod{p^4}.
$$


Consequently,


$$
\boxed{
\frac{
\displaystyle\frac{4^{p-1}}{p+1}\frac{R_h(2p)}{R_h(p)}-1
}{p}
\equiv
\mu_p+L_{1,h}
+p(E_{2,h}+\mu_pL_{1,h})
+p^2(E_{3,h}+\mu_pE_{2,h})
\pmod{p^3}.
}
$$



Thus the report’s


$$
\mathcal J_{p,h}
=\mu_p+L_{1,h}
+p(E_{2,h}+\mu_pL_{1,h})
+p^2(E_{3,h}+\mu_pE_{2,h})
$$


contains every required cubic term.

As an independent check, expanding $(p+1)^{-1}$ gives the equivalent expression


$$
\begin{aligned}
\mathcal J_{p,h}\equiv{}&
q_p(4)-1+L_{1,h}\\
&+p\bigl(E_{2,h}+(q_p(4)-1)(L_{1,h}-1)\bigr)\\
&+p^2\bigl(E_{3,h}
+(q_p(4)-1)(E_{2,h}-L_{1,h}+1)\bigr)
\pmod{p^3}.
\end{aligned}
$$


No quadratic Fermat-quotient term is missing: the prefactor is exactly $1+p\mu_p$.

Neither $q_p(4)$ nor $\mu_p$ is assumed to be a unit.

## 4.3 Weighted neighboring Hermite identities — PASS

Define


$$
A_h^+=2h^2-p(2h+1),
$$




$$
\widetilde A_h^-=2h(h-2)-p(2h-1),
$$


and


$$
A_j^-=2j(j+2)-p(2j+3).
$$



Let


$$
R_a(z)=\sum_{h=0}^a\mathsf h_{a,h}z^h,\qquad
D_z=z\frac d{dz}.
$$


The coefficient ratio


$$
\frac{\mathsf h_{a,h}}{\mathsf h_{a,h-1}}
=\frac{a-h+1}{h(p-h)}
$$


proves


$$
D_z^2R_a-(p+z)D_zR_a+azR_a=0.
$$


The first-order coefficient identity for $Y_a$ gives


$$
Q_k^{\rm H}=(2p-1)Q_a^{\rm H}-2D_zR_a(-1),
$$




$$
P_k^{\rm H}=(2p+1)P_a^{\rm H}-2D_zR_a(1).
$$


Applying the differential equation at $z=-1$ and $z=1$ yields


$$
\boxed{
\sum_{h=0}^a(-1)^hA_h^+\mathsf h_{a,h}
=Q_k^{\rm H}-2pQ_a^{\rm H},
}
$$




$$
\boxed{
\sum_{h=0}^a\widetilde A_h^-\mathsf h_{a,h}
=P_k^{\rm H}-2pP_a^{\rm H}.
}
$$



The neighboring Chebyshev identity is


$$
T_{p-1}(1-2z)
=(1-2z)q(z)-\frac2p z(1-z)q'(z).
$$


Applying the nonalternating factorial functional gives


$$
\eta(C_{p-1})=-1-2\sum_{j=1}^pA_j^+w_j,
$$


and applying the alternating functional gives


$$
E(C_{p-1})=3-2\sum_{j=1}^p(-1)^{j+1}A_j^-w_j.
$$


Therefore


$$
\boxed{
\Theta_{p-1}+1
=\frac{p+\sum_{j=1}^pA_j^+w_j}{p-1},
}
$$




$$
\boxed{
\Phi_{p-1}-1
=\frac{-p+\sum_{j=1}^p(-1)^{j+1}A_j^-w_j}{p-1}.
}
$$



This independently checks the two different constants $+p$ and $-p$, as well as the endpoint subtraction.

For the upper half,


$$
A_{p-h}^+=A_h^+,\qquad
A_{p-h}^-=\widetilde A_h^-.
$$


These are the required neighboring weights.

## 4.4 All four actual defects modulo $p^3$ — PASS

The lower-half product gives


$$
\frac{w_j}{p}
\equiv\mathsf b_j(1-p^2H_{j-1}^{(2)})\pmod{p^3}.
$$


Combining it with the exact upper-half normalization proves


$$
\boxed{
\begin{aligned}
\sigma_0^+\equiv{}&
\chi\sum_{h=0}^a(-1)^h\mathsf h_{a,h}\mathcal J_{p,h}\\
&+\sum_{j=1}^a\mathsf b_j(1-p^2H_{j-1}^{(2)})
\pmod{p^3},
\end{aligned}
}
$$




$$
\boxed{
\begin{aligned}
\sigma_0^-\equiv{}&
\chi\sum_{h=0}^a\mathsf h_{a,h}\mathcal J_{p,h}\\
&+\sum_{j=1}^a(-1)^{j+1}\mathsf b_j(1-p^2H_{j-1}^{(2)})
\pmod{p^3}.
\end{aligned}
}
$$



For the neighboring defects, the anchor and weighted identities give


$$
\boxed{
\begin{aligned}
\sigma_1^+\equiv\frac1{p-1}\Bigg\{&
1+\chi(Q_k^{\rm H}-2Q_a^{\rm H})\\
&+\chi\sum_{h=0}^a(-1)^hA_h^+\mathsf h_{a,h}\mathcal J_{p,h}\\
&+\sum_{j=1}^aA_j^+\mathsf b_j(1-p^2H_{j-1}^{(2)})
\Bigg\}\pmod{p^3},
\end{aligned}
}
$$




$$
\boxed{
\begin{aligned}
\sigma_1^-\equiv\frac1{p-1}\Bigg\{&
-1+\chi(P_k^{\rm H}-2P_a^{\rm H})\\
&+\chi\sum_{h=0}^a
\widetilde A_h^-\mathsf h_{a,h}\mathcal J_{p,h}\\
&+\sum_{j=1}^a(-1)^{j+1}A_j^-\mathsf b_j
(1-p^2H_{j-1}^{(2)})
\Bigg\}\pmod{p^3}.
\end{aligned}
}
$$



There are no $p$-base states on the right-hand sides. These are explicit finite arithmetic evaluations, not unspecified factorial moments.

### Exact product version

Replacing $\mathcal J_{p,h}$ by


$$
\frac{
\displaystyle\frac{4^{p-1}}{p+1}\frac{R_h(2p)}{R_h(p)}-1
}{p}
$$


and replacing the lower-half truncation by


$$
\mathsf b_j\prod_{v=1}^{j-1}\left(1-\frac{p^2}{v^2}\right)
$$


makes all four formulas exact identities in $\mathbb Z_{(p)}$, equal to the actual integer defects.

This exact version is valid for higher precision without invoking a logarithmic series beyond its safe denominator range.

---

# 5. FULL22: integer continuant and complete fourth precision

## 5.1 Reused signed quotient systems

The admitted third-precision lift is reused without another audit.

For the residual operator


$$
\mathcal L_jZ=Z_{j+1}+4jZ_j-Z_{j-1},
\qquad 1\le j\le r-1,
$$


the homogeneous columns have seeds


$$
(\mathcal A_0,\mathcal A_1)=(1,0),\qquad
(\mathcal B_0,\mathcal B_1)=(0,1).
$$


The first corrections satisfy


$$
\mathcal L_j\mathcal D=-4\mathcal A_j,\quad
\mathcal L_j\mathcal E=-4\mathcal B_j,\quad
\mathcal L_j\mathcal T=-4\Theta_j,\quad
\mathcal L_j\mathcal W=-4\Phi_j,
$$


with $(\mathcal D_0,\mathcal D_1)=(0,-4)$ and zero seeds for the other three.

The retained complete anchored columns are


$$
Z_{0,j}^+
=\chi(\mathcal A_jQ_a^{\rm H}-\mathcal B_jQ_k^{\rm H})+\Theta_j,
$$




$$
Z_{1,j}^+
=\chi(\mathcal D_jQ_a^{\rm H}-\mathcal E_jQ_k^{\rm H})
+\mathcal T_j+\mathcal A_j\sigma_0^++\mathcal B_j\sigma_1^+,
$$




$$
Z_{0,j}^-
=\chi(\mathcal A_jP_a^{\rm H}-\mathcal B_jP_k^{\rm H})-\Phi_j,
$$




$$
Z_{1,j}^-
=\chi(\mathcal D_jP_a^{\rm H}-\mathcal E_jP_k^{\rm H})
-\mathcal W_j+\mathcal A_j\sigma_0^-+\mathcal B_j\sigma_1^-.
$$


Put $Z_j^\pm=Z_{0,j}^\pm+pZ_{1,j}^\pm$.

The actual integer quotient systems are


$$
\Theta_{p+j}=Z_j^++p^2\mathfrak e_j^+,\qquad
\Phi_{p+j}=Z_j^-+p^2\mathfrak e_j^-,
$$




$$
\mathfrak e_0^\pm=0,\qquad
\mathfrak e_1^\pm=-4\sigma_0^\pm,
$$




$$
\mathfrak e_{j+1}^\pm+4(p+j)\mathfrak e_j^\pm-\mathfrak e_{j-1}^\pm
=-4Z_{1,j}^\pm.
$$



The second corrections have zero seeds and satisfy


$$
\mathcal L_j\mathcal D^{\langle2\rangle}=-4\mathcal D_j,\quad
\mathcal L_j\mathcal E^{\langle2\rangle}=-4\mathcal E_j,
$$




$$
\mathcal L_j\mathcal T^{\langle2\rangle}=-4\mathcal T_j,\quad
\mathcal L_j\mathcal W^{\langle2\rangle}=-4\mathcal W_j.
$$


Thus


$$
\begin{aligned}
Y_j^+={}&\mathcal D_j\sigma_0^++\mathcal E_j\sigma_1^+\\
&+\chi(\mathcal D_j^{\langle2\rangle}Q_a^{\rm H}
-\mathcal E_j^{\langle2\rangle}Q_k^{\rm H})
+\mathcal T_j^{\langle2\rangle},
\end{aligned}
$$




$$
\begin{aligned}
Y_j^-={}&\mathcal D_j\sigma_0^-+\mathcal E_j\sigma_1^-\\
&+\chi(\mathcal D_j^{\langle2\rangle}P_a^{\rm H}
-\mathcal E_j^{\langle2\rangle}P_k^{\rm H})
-\mathcal W_j^{\langle2\rangle}.
\end{aligned}
$$


They satisfy


$$
\mathcal L_jY^\pm=-4Z_{1,j}^\pm,\qquad
Y_0^\pm=0,\quad Y_1^\pm=-4\sigma_0^\pm.
$$



## 5.2 Explicit integer continuant — PASS

Define


$$
\mathcal K_m(x)=
\sum_{v=0}^{\lfloor m/2\rfloor}
\binom{m-v}{v}(-4)^{m-2v}(x+v+1)_{m-2v},
\qquad m\ge0,
$$


and $\mathcal K_{-1}=0$.

Each $\mathcal K_m$ is an integer polynomial. Its recurrence is


$$
\boxed{
\mathcal K_m(x)
=-4(x+m)\mathcal K_{m-1}(x)+\mathcal K_{m-2}(x),
}
$$


with


$$
\mathcal K_0=1,\qquad \mathcal K_1=-4(x+1).
$$



For a direct coefficient verification, fix $v$, put $d=m-2v$, and set


$$
A=\binom{m-1-v}{v},\qquad
B=\binom{m-1-v}{v-1}.
$$


After extracting the common rising factorial, the recurrence reduces to


$$
(A+B)(x+m-v)=A(x+m)+B(x+v),
$$


which is equivalent to


$$
vA=dB.
$$


That is precisely


$$
v\binom{m-1-v}{v}
=(m-2v)\binom{m-1-v}{v-1}.
$$


The $d=0$ boundary term is separately the constant $1$, so no negative rising factorial is required.

Thus $\mathcal K_{j-t-1}(p+t)$ is exactly the impulse kernel from forcing at residual step $t$ to state $j$.

## 5.3 Exact signed cubic remainder — PASS

Subtracting the equations for $\mathfrak e^\pm$ and $Y^\pm$ gives


$$
(\mathfrak e-Y)_{j+1}^\pm
+4(p+j)(\mathfrak e-Y)_j^\pm
-(\mathfrak e-Y)_{j-1}^\pm
=-4pY_j^\pm,
$$


with zero initial difference at $0,1$.

The continuant therefore proves the exact identities


$$
\boxed{
\Theta_{p+j}
=Z_j^++p^2Y_j^+
-4p^3\sum_{t=1}^{j-1}
\mathcal K_{j-t-1}(p+t)Y_t^+,
}
$$




$$
\boxed{
\Phi_{p+j}
=Z_j^-+p^2Y_j^-
-4p^3\sum_{t=1}^{j-1}
\mathcal K_{j-t-1}(p+t)Y_t^-.
}
$$


The sign $-4p^3$ is the same in both systems.

Modulo $p^4$, integer polynomiality permits


$$
\mathcal K_{j-t-1}(p+t)\equiv\mathcal K_{j-t-1}(t)\pmod p.
$$


No kernel division occurs.

## 5.4 All four columns modulo $p^4$ — PASS

Put


$$
B_U=\mathscr C_U-\mathscr A Z_s^+-\mathscr B Z_{s-1}^+,
$$




$$
B_V=C_V-PZ_r^+-QZ_{r-1}^+,
$$


and


$$
W_{U,t}
=\mathscr A\mathcal K_{s-t-1}(t)
+\mathscr B\mathcal K_{s-t-2}(t),
\quad 1\le t\le s-1,
$$




$$
W_{V,t}
=P\mathcal K_{r-t-1}(t)
+Q\mathcal K_{r-t-2}(t),
\quad 1\le t\le r-1.
$$


The convention $\mathcal K_{-1}=0$ supplies the exact final boundary term.

Substitution into the complete original columns gives


$$
\boxed{
\begin{aligned}
16U\equiv{}&
B_U-p^2(\mathscr A Y_s^++\mathscr B Y_{s-1}^+)\\
&+4p^3\sum_{t=1}^{s-1}W_{U,t}Y_t^+
\pmod{p^4},
\end{aligned}
}
$$




$$
\boxed{
\begin{aligned}
V\equiv{}&
B_V-p^2(PY_r^++QY_{r-1}^+)\\
&+4p^3\sum_{t=1}^{r-1}W_{V,t}Y_t^+
\pmod{p^4},
\end{aligned}
}
$$




$$
\boxed{
\begin{aligned}
16E_K\equiv{}&
\mathscr C_E+\mathscr A Z_s^-+\mathscr B Z_{s-1}^-\\
&+p^2(\mathscr A Y_s^-+\mathscr B Y_{s-1}^-)\\
&-4p^3\sum_{t=1}^{s-1}W_{U,t}Y_t^-
\pmod{p^4},
\end{aligned}
}
$$




$$
\boxed{
\begin{aligned}
E_F\equiv{}&
C_F^E-PZ_r^--QZ_{r-1}^-\\
&-p^2(PY_r^-+QY_{r-1}^-)\\
&+4p^3\sum_{t=1}^{r-1}W_{V,t}Y_t^-
\pmod{p^4}.
\end{aligned}
}
$$



The alternating endpoint signs pass. In particular, the square source retains $-\delta^2$, and the square endpoint retains $4\alpha\beta$.

## 5.5 Both actual third-collision divisions — conditional PASS

Assume now the **actual** third collision


$$
p^3\mid U,V.
$$


Only under that hypothesis are the following divided carries integral:


$$
\boxed{
\begin{aligned}
\frac{16U}{p^3}\equiv{}&
\frac{B_U-p^2(\mathscr A Y_s^++\mathscr B Y_{s-1}^+)}{p^3}\\
&+4\sum_{t=1}^{s-1}W_{U,t}Y_t^+
\pmod p,
\end{aligned}
}
$$




$$
\boxed{
\begin{aligned}
\frac{V}{p^3}\equiv{}&
\frac{B_V-p^2(PY_r^++QY_{r-1}^+)}{p^3}\\
&+4\sum_{t=1}^{r-1}W_{V,t}Y_t^+
\pmod p.
\end{aligned}
}
$$


Their numerator divisibility follows from the exact cubic remainder, or already from the complete congruences modulo $p^4$. Their residues require the numerators **before division** modulo $p^4$.

If this fourth pair is nonzero, then


$$
\boxed{c_p=3,\qquad e_p=[1-B_p]_+\le1.}
$$


The formulas do not prove that it is always nonzero.

## 5.6 Full additive endpoint chart modulo $p^4$ — PASS

In the residual-source chart, the exact formula remains


$$
\begin{aligned}
\zeta_{p,N}={}&
\mathscr I_1(\Theta_s-\Theta_\ell)
+\mathscr I_2(\Theta_{s-1}-\Theta_{\ell-1})\\
&+\Delta(\Theta_s\Theta_{\ell-1}
-\Theta_{s-1}\Theta_\ell).
\end{aligned}
$$


The exact state formulas evaluate it modulo $p^4$ without dividing either $\mathscr I_i$ or $\Delta$.

In the endpoint chart,


$$
\boxed{
\begin{aligned}
\zeta_{p,N}\equiv{}&
R_1E_2-R_2E_1\\
&-\Delta\Bigg[
2(-1)^a\chi^2+p\chi\Lambda_\sigma+p^2\Xi_\sigma\\
&\qquad
-4p\sum_{t=1}^{s-1}(-1)^t
\Bigl\{
\Theta_t(Z_t^-+p^2Y_t^-)
+\Phi_t(Z_t^++p^2Y_t^+)
\Bigr\}
\Bigg]\pmod{p^4}.
\end{aligned}
}
$$


The endpoint factors in the first line are obtained from the complete endpoint columns above.

Inside the mixed return, the states are needed only modulo $p^3$, because the return is multiplied by $p$. Omitting their $-4p^3$ terms **inside this one return** changes the whole expression only modulo $p^4$. Those terms are not omitted from the source or endpoint columns themselves.

After an actual third collision, the fourth-digit chart transformations are explicitly


$$
\frac{\mathfrak A_{p,N}}{p^3}
\equiv
R_1\frac V{p^3}-R_2\frac{16U}{p^3}\pmod p,
$$




$$
\frac{\mathfrak B_{p,N}}{p^3}
\equiv
E_2\frac{16U}{p^3}-E_1\frac V{p^3}\pmod p.
$$


The selected transformation has unit determinant. Thus fourth-pair nonvanishing is faithfully represented in either available chart, including determinant-critical primes.

---

# 6. Precision ledger and the exact unpaid premise

## 6.1 Fourth precision

A sufficient consistent precision profile is:

| Object | Required precision |
|---|---:|
| Actual divided Gaussian coefficients | $p^4$ |
| Hermite data at $a,k$ | $p^4$ |
| Actual defects $\sigma^\pm$ | $p^3$ |
| $Z_{0,j}^\pm$ | $p^4$ |
| $Z_{1,j}^\pm$ | $p^3$ |
| $Y_j^\pm$ | $p^2$ |
| Cubic kernel contractions | $p$ |
| Numerators divided by $p^3$ | $p^4$ before division |

For $\mu_p\bmod p^3$, the integer $4^{p-1}-1$ must first be known modulo $p^4$, followed by the paid division by $p$.

If


$$
a_G=v_p(g_B),
$$


then a divided linear Gaussian coordinate modulo $p^h$ requires its actual numerator modulo $p^{a_G+h}$. A raw quadratic column divided afterwards by $g_B^2$ requires precision


$$
\boxed{p^{2a_G+h}.}
$$


In particular, raw quadratic precision $p^4$ is insufficient when $a_G>0$.

The upper-half factorial expressions are manipulated as exact rational identities before reduction. Their apparent factorial denominators are not inverted illegally modulo $p$. The final normalized products have unit denominators, and their differences from $1$ have the explicitly proved factor $p$.

## 6.2 The target can exceed fourth precision

The assigned depth is


$$
\mathsf d=4+B_p+j_p.
$$


When $\mathsf d>4$, the fourth-digit formulas do not decide the target. One must instead use:

1. the exact product versions of the four defect formulas;
2. normalized product numerators modulo $p^{\mathsf d}$ before division by $p$;
3. the exact kernels $\mathcal K_m(p+t)$;
4. complete divided Gaussian columns modulo $p^{\mathsf d}$, or raw quadratic precision $p^{2a_G+\mathsf d}$;
5. the exact critical-safe chart.

The values $B_p$ themselves require the actual


$$
h_p,\ b_p,\ z_p,\ t_p.
$$


A finite residue computation cannot determine a valuation that continues beyond its modulus.

Also, a unit $E_1$ does not imply $z_p=0$. Indeed,


$$
E_1=
\frac{
16y_K+16a_K-d_K\mathscr C_E
+d_K\mathscr A\Phi_s+d_K\mathscr B\Phi_{s-1}
}{d_K},
$$


and the other terms can produce a unit even when $p\mid y_K$.

## 6.3 Exact open saturation statement

The remaining assertion is


$$
\boxed{
16U\ \text{and}\ \zeta_{p,N}
\text{ are not both divisible by }p^{\,4+B_p+j_p}.
}
$$


By the exact unit-chart comparison, this is equivalent to


$$
c_p\le3+B_p+j_p.
$$


If proved, it would imply


$$
e_p\le1+j_p.
$$



For $N<p<2N$,


$$
v_p\binom{2N}{N}=1.
$$


Therefore the assertion would give the genuine fixed-$N$ divisor


$$
\boxed{
\prod_{p\in\mathcal S_N}p^{e_p}
\mid J_N^{\rm aff}\binom{2N}{N},
}
$$


with logarithmic bill


$$
\log J_N^{\rm aff}+2N\log2=O(N).
$$



This implication passes. Its nondivisibility premise remains open.

The earlier FULL20 implication from universal third-depth avoidance also remains conditional. Using the already passed complementary-branch payments, it would give


$$
\prod_{\substack{N<p<2N\\p\nmid L(\ell^2)}}p^{[c_p-H_p]_+}
\mid J_N^{\rm aff}\binom{2N}{N}^{\,2},
$$


and the stated bound


$$
10^{10}n^{15}\frac{10000^N}{g_B^2}.
$$


This audit does not validate the missing avoidance premise or reopen the complementary payments.

## 6.4 What no proved result supplies

None of the following is supplied:

- universal nonvanishing of the fourth source pair;
- an absolute paid depth cap;
- quantified fixed-$N$ coverage of primes with a nonzero fourth pair;
- an $O(N)$ bound for $\sum_{p\in\mathcal S_N}e_p\log p$;
- an applicable non-Wieferich, Wilson, or Kurepa theorem.

A fixed-prime original-index count is not fixed-$N$ interval coverage. Successive original indices differ by $3^{64}>2$, so at most one original $N$ can satisfy $N<p<2N$ for a fixed $p$. This observation gives no count of eligible primes for one fixed original $N$.

---

# 7. Preservation of the complete original producer

## 7.1 Source and endpoint balances and returns

The source balance remains


$$
\begin{aligned}
&(\nu\mathscr A-16\tau\Pi)\Theta_\ell
+(\nu\mathscr B-16\tau\Omega)\Theta_{\ell-1}\\
&\hspace{12mm}=\nu\mathscr C_U-16\tau C^{\rm s}.
\end{aligned}
$$


For


$$
T_{\rm end}=\tau(E_F-\delta^2)+\nu E_K,
$$


the full endpoint is


$$
\begin{aligned}
16T_{\rm end}={}&
16\tau(C^{\rm e}-\delta^2)+\nu\mathscr C_E\\
&+(\nu\mathscr A-16\tau\Pi)\Phi_\ell
+(\nu\mathscr B-16\tau\Omega)\Phi_{\ell-1}.
\end{aligned}
$$



The source return is


$$
z_\ell=16\Omega U-\mathscr B V,\qquad
z_{\ell-1}=\mathscr A V-16\Pi U,
$$




$$
z_j=-\Delta\Theta_j+\varrho_j,
$$




$$
\varrho_\ell=\mathscr I_2,\qquad
\varrho_{\ell-1}=-\mathscr I_1,
$$




$$
\varrho_{j-1}=\varrho_{j+1}+4j\varrho_j-2\Delta.
$$


Thus $z_{j-1}=z_{j+1}+4jz_j$.

After the actual arc clearing below, set


$$
k_E=D\mathscr C_E-16DR_K,\qquad
f_E=DC^{\rm e}-DR_F.
$$


The endpoint return is


$$
w_\ell=16\Omega Y+\mathscr B X,\qquad
w_{\ell-1}=-16\Pi Y-\mathscr A X,
$$




$$
w_j=D\Delta\Phi_j+\sigma_j^{\rm ret},
$$




$$
\sigma_\ell^{\rm ret}=\Omega k_E+\mathscr Bf_E,\qquad
\sigma_{\ell-1}^{\rm ret}=-\Pi k_E-\mathscr Af_E,
$$




$$
\sigma_{j-1}^{\rm ret}
=\sigma_{j+1}^{\rm ret}+4j\sigma_j^{\rm ret}
+2D\Delta(-1)^j.
$$


The retained return identity is


$$
\boxed{
z_\ell w_{\ell-1}-z_{\ell-1}w_\ell
=-16\Delta(UX+VY).
}
$$


It contains no division by $\Delta$.

For exactly $0\le b\le N$, the canonical Hermite returns remain


$$
\mathcal R_{b;N}=d_KP_b^{\rm H}U+Q_b^{\rm H}y_K.
$$


With


$$
\Psi_j^{(b)}=Q_b^{\rm H}\Phi_j-P_b^{\rm H}\Theta_j,
$$


their complete forcing is


$$
\Psi_{j+1}^{(b)}+4j\Psi_j^{(b)}-\Psi_{j-1}^{(b)}
=2(Q_b^{\rm H}(-1)^j-P_b^{\rm H}),
$$


and


$$
\begin{aligned}
16\mathcal R_{b;N}
={}&d_K\bigl(
P_b^{\rm H}\mathscr C_U+Q_b^{\rm H}\mathscr C_E
+\mathscr A\Psi_\ell^{(b)}
+\mathscr B\Psi_{\ell-1}^{(b)}
\bigr)\\
&-16Q_b^{\rm H}a_K.
\end{aligned}
$$


The established facts retained at $N-1,N$ are


$$
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
$$




$$
|\mathcal R_{N-1;N}|,\ |\mathcal R_{N;N}|<d_K36^NN!,
$$




$$
v_2(U)=2,\qquad v_2(y_K)=1,\qquad d_K\ \text{odd},
$$


and


$$
\boxed{
\frac{c(r^\circ)^2}{\kappa_N^{\rm prod}}
\mid\mathcal R_{N-1;N}\mathcal R_{N;N},
\qquad
v_p(\kappa_N^{\rm prod})=[c_p-H_p]_+.
}
$$



No factorial divisibility is inferred from these height estimates.

The closed thirteen-weight terminal representation is unchanged, with weights


$$
(1,8,58,168,399,-176,-916,-176,399,168,58,8,1)
$$


and its original backward steps $1\le k\le11$. It is not recomputed here. Its rational interface remains on $2\le j\le n-1$, with the already paid clearers


$$
Q_{\rm loc}(n)=\prod_{b=0}^{12}(n-b),\qquad
\mathcal L_n=\operatorname{lcm}(1,\ldots,n),
$$


including


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}.
$$


Neither clearer replaces the least arc clearer.

## 7.2 Both reduced arcs and actual primitive denominator

Retain


$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


The monic quotient degrees are at most $2N-2$.

The complete square-arc return has zero seeds at $0,1$ and


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
0,&j\ \text{odd},\\
(1-j^2)^{-1},&j\ \text{even}.
\end{cases}
$$


Its physical output is


$$
R_F=
\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
-2\alpha\beta\xi_{n-1}}2.
$$


No step beyond $n-1$ is used.

After reducing both arcs completely,


$$
\boxed{
D=\operatorname{lcm}(\operatorname{den}R_F,\operatorname{den}R_K).
}
$$


Set


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$


Independently reduce


$$
\tau R_F+\nu R_K=\frac b\lambda,\qquad
\gcd(b,\lambda)=1,\quad\lambda>0.
$$


Then


$$
E=\tau E_F+\nu E_K,\qquad A=\lambda E-b,
$$




$$
\boxed{G=\gcd(M,A),}
$$


with the gcd over **all primes**, and


$$
\boxed{
p_N=A/G,\qquad q_N=\lambda M/G.
}
$$


Because $\gcd(\lambda,A)=1$, this is the actual primitive rational pair.

No mixed clearer, harmonic denominator, local chart, or coefficient gcd replaces $D,\lambda,G$, or $q_N$.

## 7.3 Nonzero whole error at the same original indices

The original polynomial is


$$
P_N(t)=\frac{F(t)^2+(V/U)K(t)}{\delta^2}
=\frac{W_{\rm prim}(t)}M.
$$


It is nonnegative and not identically zero. The whole error is


$$
\boxed{
\epsilon_N=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0.
}
$$



The source balance gives


$$
\eta(W_{\rm prim})
=\tau(\delta^2+V)-\nu U=M.
$$


Hence


$$
\int_0^1e^tW_{\rm prim}(t)\,dt=eM-E,
$$


while both complete arcs give


$$
4\int_0^1\frac{W_{\rm prim}(t)}{1+t^2}\,dt
=\pi M+\frac b\lambda.
$$


Therefore


$$
\epsilon_N=e+\pi-\frac{A}{\lambda M},
$$


and


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0.
}
$$



The whole rational enclosure is


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


and, with $j_b=(1-4b^2)^{-1}$,


$$
J_K=\frac{61}{420}
+\frac{
916j_m-399(j_{m+1}+j_{m-1})
-58(j_{m+2}+j_{m-2})
-(j_{m+3}+j_{m-3})
}{8192}.
$$


Both $J_F$ and $J_K$ are positive, being the corresponding nonzero nonnegative polynomial integrals. Thus


$$
\boxed{
q_NJ_N=\frac{\lambda_N}{G_N}
\bigl(\tau_NJ_F+\nu_NJ_K\bigr)
}
$$


retains **both positive summands**.

The lower bound for $D_{\rm mix}$ is not a bound for $q_N$. No conclusion about $q_N\epsilon_N$, producer retirement, or irrationality follows from it alone.

---

# 8. Audit ledger, new consequence, and remaining bottleneck

## 8.1 Status ledger

| Claim | Audit status |
|---|---|
| Original domain, divided Gaussian data, actual source content | Retained unchanged |
| Actual six-step transport, Hermite anchor, third-precision quotient systems | Previously passed; reused without repeating that audit |
| Mixed determinant signs and four-defect seed | **PASS** |
| Complete mixed forcing return | **PASS** |
| Positivity and stated factorial bounds | **PASS** |
| Factorial division obstruction at the selected prime | **PASS** |
| Corrected $K$-row elimination and constant $15\,350\,843$ | **PASS** |
| Both critical-safe charts | **PASS**, not source noncollision |
| All-prime mixed gcd identities | **PASS** |
| Conditioning-free full post-credit comparison | **PASS** |
| Actual least simultaneous mixed clearer | **PASS** |
| Primitive integer relation | **PASS**, with a division-free derivation above |
| Moment residual sign and $R_1<0$ | **PASS** |
| Finite adjacent Hermite separation | **PASS** |
| Numerator and clearer lower bounds with constants $16,28$ | **PASS**, pointwise on the stated original scope |
| Infinite occurrence of eligible pairs | **Not asserted or proved** |
| Norm/credit divisor implications | **PASS**, without an aggregate height bound |
| Exact upper-half normalization against actual Hermite coefficients | **PASS** |
| Every cubic harmonic/Fermat term | **PASS** |
| All four defects modulo $p^3$ and exact product version | **PASS** |
| Integer continuant and exact cubic signed remainder | **PASS** |
| All complete source/endpoints modulo $p^4$ | **PASS** |
| Both divisions by $p^3$ | **PASS only after an actual third collision** |
| Full additive endpoint chart, including mixed forcing | **PASS** |
| “All denominators are units” as a literal blanket statement | **Wording repair:** exclude the explicitly paid nonunit divisions |
| Universal fourth-pair nonvanishing | **OPEN** |
| Nondivisibility at depth $4+B_p+j_p$ | **OPEN** |
| Fixed-$N$ aggregate divisor from saturation | **Conditional PASS** |
| $O(N)$ surviving contact mass | **OPEN** |
| Smaller-prime and $p>2N$ obligations | **Separate and OPEN** |
| Producer retirement or a decision about $e+\pi$ | **Not established** |

## 8.2 New proved consequence of this audit

Besides independently validating the formulas, the normalization-rigidity corollary proves a slightly broader negative statement:

> Every integral realization of the same two actual mixed ratios is an integer multiple of the stated primitive triple. Therefore no alternative integer clearer for those unchanged ratios can evade the pointwise bounds
> 

$$
> \max(|A'|,|B'|)\ge N^{(p-1)/2}e^{-16N},
> \qquad
> D'\ge N^{(p-1)/2}e^{-28N}.
>
$$



This is an unconditional statement about the specified original objects. It does not assume infinitely many eligible pairs, and it does not rule out a genuinely different auxiliary or a separately justified credit-aware reduction.

## 8.3 Exact mathematical bottleneck

The verified fourth-precision calculation leaves a specific arithmetic cancellation unpaid. After an actual third collision, the Gaussian carries


$$
\frac{B_U-p^2(\mathscr A Y_s^++\mathscr B Y_{s-1}^+)}{p^3},
\qquad
\frac{B_V-p^2(PY_r^++QY_{r-1}^+)}{p^3}
$$


may still cancel against the corresponding explicit cubic forcing contractions.

The four base defects are no longer independent unknowns: their actual arithmetic is constrained by the proved harmonic formulas. Nevertheless, no theorem supplied here excludes simultaneous cancellation.

For $B_p+j_p=0$, nonzero fourth-pair separation would settle the local saturation target. For $B_p+j_p>0$, the exact product and continuant formulas must be controlled at the larger depth


$$
4+B_p+j_p.
$$


Alternatively, a quantified weaker estimate sufficient to prove


$$
\sum_{p\in\mathcal S_N}e_p\log p=O(N)
$$


would close this interval obligation.

That is the concrete follow-on lemma already assigned to A5’s next task. This audit supplies verified inputs, not a replacement proof by unit charts, small real quotients, conditioning estimates, or fixed-prime counts.

## 8.4 Exact arithmetic and computation status

No numerical computation was performed or is required for the proofs in this audit. All new checks are written finite algebraic derivations:

- the degree-three polynomial elimination;
- the Hermite coefficient and weighted identities;
- the cubic product expansion;
- the integer continuant recurrence;
- the determinant and valuation identities.

No original-size solve, prime scan, old certificate, or optional tiny check is requested. There is therefore no pending computational input/output task for the coordinator.

A future finite evaluation of selected original pairs would establish only those selected values. It would not prove the universal saturation assertion or fixed-$N$ aggregate coverage.

---

# Final conclusion

The different audit confirms the main new mathematics of FULL20–22 at its exact scope. The mixed forcing formulas, corrected-column charts, primitive-height obstruction, harmonic defect evaluations, and fourth-precision source and endpoint formulas are sound.

The failed mechanism is now precisely delimited: the actual primitive normalization of the two mixed ratios retains factorial arithmetic height. A small real mixed quotient is not a small-height integer certificate, and choosing a different integer clearer for the same ratios cannot repair that failure.

The unresolved issue is the actual, credit-aware source cancellation at depth


$$
\boxed{4+B_p+j_p,}
$$


or a quantified weaker bound with a genuine fixed-$N$, $O(N)$-height aggregate payment. A unit chart and an $O(N)$ conditioning bill do not supply that bound.

All original contents, finite boundaries, forcings, returns, reduced arcs, least $D$ and $\lambda$, the **all-prime** final gcd $G$, the actual primitive denominator $q_N$, and the strictly positive whole error remain unchanged at


$$
N=9^{18+32u}.
$$



**No producer retirement and no unconditional proof or disproof of irrationality of $e+\pi$ follows from the audited work.**
