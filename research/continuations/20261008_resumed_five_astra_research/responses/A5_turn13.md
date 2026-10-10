> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A conditional convexity audit and an evaluated source certificate

## Abstract and proof status

The global question—whether $e+\pi$ is rational or irrational—remains unresolved.

This report has two distinct conclusions.

1. **Pairwise-Jensen audit: PASS, conditional on the explicitly stated premises of the earlier spread argument.**  
   The later corollary has the correct finite pair count, both Jensen inequalities have the correct direction, both arguments of $-\log(1-t)$ are strictly below $1$, and
   

$$
R_{\star,k}
   =\frac{k(k-1)}2
      \log\frac{85k^2-37k+6}{77k^2-43k+8}
$$


   is finite for every integer $k\ge2$. Moreover,
   

$$
\frac{R_{\star,k}}{k^2}\longrightarrow
   \frac12\log\frac{85}{77}>\frac4{85}.
$$


   The asserted SAME-$H$ improvement follows at the unchanged cutoff, provided the earlier relative-factor, moment, and SAME-$H$ comparison premises hold.

2. **A new, evaluated original-source certificate is proved, but its height requirement fails.**  
   At every original index
   

$$
N=9^{18+32u},\qquad u\ge0,
$$


   explicit canonical integer coefficients give
   

$$
a_NU_N+b_NV_N
   =Q^{\mathrm H}_{N-1}Q^{\mathrm H}_N B_N,
$$


   where
   

$$
\boxed{B_N=c_N(M_N-E_N)<0.}
$$


   Here $E_N=\tau_NE_{F,N}+\nu_NE_{K,N}$ is the original integer exponential endpoint, before either arc is subtracted. The multiplier is evaluated quantitatively:
   

$$
\boxed{\frac78U_N\delta_N^2<|B_N|<2U_N\delta_N^2.}
$$


   Consequently,
   

$$
\log|B_N|=2N\log N+O(N),
$$


   not $O(N)$. Even a natural primitive normalization of the coefficient row leaves factorial-scale height.

Thus the new certificate supplies a **source-specific obstruction to a natural Hermite-adjugate route**, not a proof or disproof of HC. A further, explicitly stated terminal-divisor lemma would make this route sufficient; that lemma remains open.

No tools or numerical computations were used.

---

# 1. Independent audit of the later pairwise-Jensen corollary

## 1.1 Exact premises and scope

This audit does **not** reconsider the earlier Laguerre/Wishart moment calculation or the base comparison. For this section, take the following as explicit premises.

For an integer $k\ge2$, let $z_1,\ldots,z_k>0$ be random variables under the stated probability law. Put


$$
g_{ij}=\frac{(z_i+z_j)^2}{4z_iz_j},\qquad
r_{ij}=\frac{z_i-z_j}{z_i+z_j},
$$


and assume


$$
\det D_k=B_k\,\mathbb E\prod_{i<j}g_{ij},
$$


where


$$
D_k(i,j)=(2k+2i+2j)!,\qquad 0\le i,j\le k-1,
$$




$$
B_k=2^{k(k-1)}
       \prod_{j=0}^{k-1}j!(3k-1+j)!.
$$


Assume also that the relative expectation is finite and that


$$
\mathbb E X\ge R_k,\qquad
X=\sum_{i<j}r_{ij}^2,
$$


with


$$
R_k=
\frac{k(4k-1)(k^2-1)}
     {85k^2-37k+6}.
$$



These are premises of the implication audited here, not conclusions of this audit.

There are exactly


$$
p=\binom{k}{2}=\frac{k(k-1)}2
$$


unordered pairs. Since $k\ge2$, $p>0$.

## 1.2 The finite-list Jensen inequality

For positive $z_i,z_j$,


$$
|z_i-z_j|<z_i+z_j.
$$


Therefore


$$
0\le r_{ij}^2<1.
$$


Moreover,


$$
1-r_{ij}^2=\frac{4z_iz_j}{(z_i+z_j)^2},
$$


so


$$
\log g_{ij}=f(r_{ij}^2),\qquad
f(t)=-\log(1-t).
$$



On $0\le t<1$,


$$
f'(t)=\frac1{1-t}>0,\qquad
f''(t)=\frac1{(1-t)^2}>0.
$$


Thus $f$ is increasing and strictly convex.

Applying Jensen to the finite list of exactly $p$ numbers $r_{ij}^2$ gives


$$
\frac1p\sum_{i<j}f(r_{ij}^2)
\ge
f\!\left(\frac1p\sum_{i<j}r_{ij}^2\right).
$$


Equivalently,


$$
\boxed{\sum_{i<j}\log g_{ij}\ge p\,f(X/p).}
\tag{1.1}
$$


This direction is correct. Repeated nodes cause no difficulty: their corresponding entry is simply $0$.

## 1.3 Integrability and the probability Jensen inequality

Write


$$
Y=\sum_{i<j}\log g_{ij}.
$$


Then $Y\ge0$, and


$$
e^Y=\prod_{i<j}g_{ij}.
$$


The assumed finiteness of $\mathbb Ee^Y$, together with $0\le Y\le e^Y$, implies


$$
\mathbb EY<\infty.
$$


By (1.1),


$$
0\le p f(X/p)\le Y,
$$


so the probability Jensen step is also integrable.

Pointwise,


$$
0\le X/p<1.
$$


In particular $X/p$ is integrable. The positive bounded random variable


$$
1-X/p
$$


has strictly positive expectation: a nonnegative random variable has expectation zero only if it is zero almost surely. Hence


$$
\boxed{\mathbb EX/p<1.}
\tag{1.2}
$$



Probability Jensen now gives


$$
\mathbb E f(X/p)\ge f(\mathbb EX/p).
$$


Using (1.1), followed by monotonicity of $f$,


$$
\boxed{
\mathbb EY
\ge p f(\mathbb EX/p)
\ge p f(R_k/p),
}
\tag{1.3}
$$


provided $R_k/p<1$. That remaining domain check is explicit below.

Finally, the outer exponential Jensen inequality gives


$$
\log\mathbb Ee^Y\ge\mathbb EY.
\tag{1.4}
$$


Its direction is also correct.

## 1.4 Exact positivity and the finite gain

Cancellation of the positive factor $k(k-1)$ gives


$$
\frac{R_k}{p}
=
\frac{2(4k-1)(k+1)}
     {85k^2-37k+6}.
$$


The difference between denominator and numerator is


$$
85k^2-37k+6-2(4k-1)(k+1)
=
77k^2-43k+8.
$$



For $k=2+h$, $h\ge0$,


$$
77k^2-43k+8
=
77h^2+265h+230>0.
$$


This proves the exact positivity at every required integer $k$, including the stated value $230$ at $k=2$. In particular,


$$
0<R_k/p<1.
$$



Combining (1.3)–(1.4) with the exact relative-factor premise yields


$$
\det D_k\ge B_k e^{R_{\star,k}},
$$


where


$$
\boxed{
R_{\star,k}
=
\frac{k(k-1)}2
\log\frac{85k^2-37k+6}{77k^2-43k+8}.
}
\tag{1.5}
$$


Both polynomials inside the ratio are positive on the required domain. Thus $R_{\star,k}$ is finite and positive.

Indeed, the finite refinement is strictly stronger than the tangent bound:


$$
R_{\star,k}>R_k,
$$


because $-\log(1-x)>x$ for $0<x<1$.

## 1.5 Limit and strict asymptotic improvement

Dividing (1.5) by $k^2$ gives


$$
\frac{R_{\star,k}}{k^2}
=
\frac12\left(1-\frac1k\right)
\log
\frac{85-37/k+6/k^2}{77-43/k+8/k^2}.
$$


Therefore


$$
\boxed{
\lim_{k\to\infty}\frac{R_{\star,k}}{k^2}
=\frac12\log\frac{85}{77}.
}
$$



At $x=8/85$,


$$
\frac12\log\frac{85}{77}
=\frac12[-\log(1-x)]
>\frac{x}{2}
=\frac4{85}.
$$


The improvement is strict, not merely nonnegative.

## 1.6 Conditional SAME-$H$ consequence

Retain the earlier SAME-$H$ comparison, including its complete source corrections, contact atom, highest factorial $(6k-4)!$, and cutoff $k\ge512$:


$$
(-1)^kH_k(e+\pi)
\ge
\left(\frac{3\Lambda_k}{64}\right)^k h_k\det D_k.
$$


Then (1.5) gives


$$
\boxed{
(-1)^kH_k(e+\pi)
\ge
\left(\frac{3\Lambda_k}{64}\right)^k
h_kB_k e^{R_{\star,k}}>0.
}
$$



Under the retained pre-spread normalization


$$
\log\left[
\left(\frac{3\Lambda_k}{64}\right)^k h_kB_k
\right]
=
4k^2\log k+
\left(15\log2-\frac92\log3\right)k^2+o(k^2),
$$


the new lower constant is exactly


$$
\boxed{
15\log2-\frac92\log3+\frac12\log\frac{85}{77}.
}
$$



**Audit verdict: PASS as a conditional algebraic corollary.**  
This verdict does not certify the earlier moment premises, supply an upper bound for the actual final gcd, or decide the arithmetic question. Any binary threshold change remains conditional on the previously stated odd-content and actual $v_2(G)$ hypotheses.

---

# 2. Original signed producer: unchanged objects and reused results

Everything below concerns the same infinite index set


$$
\mathcal N=\{9^{18+32u}:u\in\mathbb Z_{\ge0}\}.
$$


In particular, every $N\in\mathcal N$ is odd. Put


$$
n=2N,\qquad m=N-3,\qquad \ell=2N-6.
$$


The physical polynomial terminal remains $n=2N$.

## 2.1 Actual Gaussian division and source content

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


with


$$
C_0=1,\quad C_1=2t-1,\quad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$


Retain


$$
d=a_Nb_{N-1}-a_{N-1}b_N,
$$




$$
g_B=\gcd(b_{N-1},b_N)>0,
\quad
\alpha=\frac{b_{N-1}}{g_B},\quad
\beta=\frac{b_N}{g_B},\quad
\delta=\frac d{g_B}.
$$


Thus


$$
F=\alpha C_N-\beta C_{N-1},\qquad F(\pm i)=\delta.
$$



The functionals are


$$
\eta(H)=\int_{-\infty}^1e^{t-1}H(t)\,dt,
\qquad
E(H)=\sum_{j=0}^{\deg H}(-1)^jj![t^j]H.
$$


With


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad K=\mathcal H C_m^2,
$$


the actual source integers are


$$
U=-\eta(K),\qquad
V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$



The established content and normalization are retained:


$$
h=g_B^2c,\qquad
\tau=\frac Uc,\qquad \nu=\frac Vc,
$$




$$
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2.
$$


On the original domain,


$$
U>0,\qquad V>0,\qquad M>0.
$$



No raw, undivided Gaussian square is substituted for $F^2$ or $V$.

## 2.2 Both arcs and the actual primitive output

Retain


$$
E_F=E(F^2),\qquad E_K=E(K),
$$




$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,
\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


Each monic quotient has degree at most $2N-2$.

The least simultaneous column clearer is


$$
D=\operatorname{lcm}\bigl(\operatorname{den}(R_F),
                         \operatorname{den}(R_K)\bigr),
$$


after each arc is reduced. Define


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$



Independently reduce the aggregate arc:


$$
\tau R_F+\nu R_K=\frac b\lambda,\qquad
\gcd(b,\lambda)=1,\quad \lambda>0.
$$


Put


$$
E=\tau E_F+\nu E_K,\qquad A=\lambda E-b,\qquad
G=\gcd(M,A).
$$


The actual primitive output is


$$
\boxed{
p=\frac AG,\qquad q=\frac{\lambda M}{G}.
}
\tag{2.1}
$$


Here $G$ is the final gcd over **all primes**.

The exact reconciliations remain


$$
\tau X+\nu Y=\frac D\lambda A,
$$




$$
\gcd(D\tau\delta^2,\tau X+\nu Y)=\frac D\lambda G,
$$




$$
D\mid\operatorname{lcm}(1,\ldots,2N-1),\qquad D<256^N.
$$



For the reduced $K$-arc, set $x=\ell^2$ and


$$
L(x)=(x-1)(x-9)(x-25),
$$




$$
A_K(x)=13x^3-455x^2+3502x-5850.
$$


The retained exact reduction is


$$
R_K=\frac{A_K(x)}{30L(x)}=\frac{a_K}{d_K},
$$


where


$$
g_{\rm arc}
=
90\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}},
$$




$$
\varepsilon_5=\mathbf1_{u\equiv1\ (5)},\quad
\varepsilon_{19}=\mathbf1_{u\equiv3\ (9)},\quad
\varepsilon_{31}=\mathbf1_{u\equiv5,7\ (15)},
$$




$$
a_K=A_K(x)/g_{\rm arc},\qquad
d_K=30L(x)/g_{\rm arc}.
$$


Thus


$$
y_K=d_KE_K-a_K,\qquad \gcd(d_K,y_K)=1,
\qquad \mu=D/d_K,\qquad Y=\mu y_K.
$$



## 2.3 Reuse of the audited canonical endpoint/gcd theorem

The turn11 theorem is reused here without another proof or small-index example.

Let $P_r^{\mathrm H},Q_r^{\mathrm H}$ be its paid Hermite endpoint integers:


$$
P_0^{\mathrm H}=Q_0^{\mathrm H}=1,\quad
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



Retain


$$
\mathcal R_{r;N}
=d_KP_r^{\mathrm H}U+Q_r^{\mathrm H}y_K.
$$


At the same original $N$,


$$
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
$$




$$
|\mathcal R_{N-1;N}|,\ |\mathcal R_{N;N}|
<d_K36^N N!,
$$


and


$$
\gcd(\mathcal R_{N-1;N},\mathcal R_{N;N})
=\gcd(U,y_K).
$$



With


$$
s_r=\gcd(c,Q_r^{\mathrm H}),
$$


the exact factorization remains


$$
\boxed{
\mathfrak J^0
=
c\gcd\left(
\tau,\frac{\mathcal R_{N-1;N}}{s_{N-1}},
     \frac{\mathcal R_{N;N}}{s_N}
\right).
}
\tag{2.2}
$$


Also,


$$
\mathfrak J^0=\gcd(U,Vy_K),\qquad
\mathfrak J=\gcd(U,VY),
$$




$$
\mathfrak J^0\mid\mathfrak J\mid\mu\mathfrak J^0,
\qquad
\boxed{U/\mathfrak J\mid q.}
\tag{2.3}
$$



The estimates used below, also reused at their stated scope, are


$$
\log U=2N\log N+O(N),\qquad
\log c\le N\log N+O(N),
\tag{2.4}
$$




$$
2^{4N-16}(2N)!<U<50\cdot36^{N-3}(2N)!,
\tag{2.5}
$$


and


$$
0<I_K:=\int_0^1e^tK(t)\,dt<1.
\tag{2.6}
$$



---

# 3. Complete canonical boundaries and the affine third coordinate

This section records exactly which original boundary data enter the new certificate.

## 3.1 Complete original columns

Retain


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
\tag{3.1}
$$



The complete thirteen weights are


$$
(w_0,\ldots,w_{12})
=(1,8,58,168,399,-176,-916,-176,399,168,58,8,1).
$$


For the fixed local range $1\le k\le11$,


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
(r_0,s_0^*)=(1,0),\quad(r_1,s_1^*)=(0,1),
\quad \kappa_0=\kappa_1=\omega_0=\omega_1=0.
$$


Thus


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
\tag{3.2}
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
\tag{3.3}
$$


Both $-\delta^2$ and $4\alpha\beta$ remain present.

## 3.2 An exact payment of the selected $S/j$ interface

Let


$$
S_j=\eta(C_j),\qquad s_j=S_j/j=\frac1j-2\Theta_j,\qquad j\ge1.
$$


Substitution into (3.1) gives, on the original nonsingular range,


$$
s_{j-1}=s_{j+1}+4js_j+\frac2{j^2-1},
\qquad 2\le j\le n-1.
\tag{3.4}
$$


The original seeds include


$$
S_0=1,\qquad s_1=-1,\qquad s_2=\frac92.
$$


No extension of (3.4) through $j=0,1$ is made.

There is a useful explicit reconciliation of the local affine constants. If


$$
s_{n-k}=r_ks_n+s_k^*s_{n-1}+e_k,
$$


then the original $\Theta$-representation gives


$$
\boxed{
e_k=
\frac1{n-k}-\frac{r_k}{n}
-\frac{s_k^*}{n-1}-2\kappa_k.
}
\tag{3.5}
$$


Thus every local denominator is explicitly among


$$
n-k,\quad n,\quad n-1.
$$


It is cleared by the retained


$$
Q_{\rm loc}(n)=\prod_{r=0}^{12}(n-r).
$$


Globally, $\mathcal L_n=\operatorname{lcm}(1,\ldots,n)$ clears


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}.
$$



Since $\sum_{k=0}^{12}w_k=0$, the full affine constants satisfy


$$
\boxed{
\mathsf E
=2\mathsf C_U-\frac{\mathsf A}{n}
                     -\frac{\mathsf B}{n-1}.
}
\tag{3.6}
$$


Likewise, with the supplied


$$
\mathsf T=(\alpha+\beta)^2-2\delta^2+\frac{2\beta^2}{n},
$$


direct substitution gives


$$
\boxed{
2\mathsf C_V
=\frac{\mathsf P}{n}+\frac{\mathsf Q}{n-1}+\mathsf T.
}
\tag{3.7}
$$


Hence the two supplied source equations really are equations in the **same actual adjacent affine state**.

The opposite forcing is retained as well. For


$$
\Delta=\mathsf A\mathsf Q-\mathsf B\mathsf P,
$$


write the original integer return as


$$
z_j=-\Delta\Theta_j+r_j,\qquad
r_{j-1}=r_{j+1}+4jr_j-2\Delta.
$$


The selected affine return $Z_j=2z_j$ has


$$
Z_j=\Delta s_j+\rho_j,
\qquad
\boxed{\rho_j=2r_j-\Delta/j.}
\tag{3.8}
$$


Equation (3.8) gives exactly


$$
\rho_{j-1}
=\rho_{j+1}+4j\rho_j-\frac{2\Delta}{j^2-1}.
$$


Thus the third affine coordinate has not been suppressed or confused with a homogeneous sequence from another producer.

## 3.3 Centered coefficients used below

Reuse the evaluated polynomials


$$
\begin{aligned}
\mathcal P(x)&=-8x^3-1116x^2-8150x+151,\\
\mathcal Q(x)&=76x^2+2408x+5637,\\
\mathcal F(x)&=4x^2+492x+5463,\\
\mathcal G(x)&=4x^2+556x-3325.
\end{aligned}
$$


At $x=\ell^2$, put


$$
\widetilde{\mathsf A}
=2\ell((2\ell+1)\mathcal Q-\mathcal P),
\qquad
\widetilde{\mathsf B}=-2\ell\mathcal Q,
$$




$$
\widetilde{\mathsf C}_U
=\mathcal F-\mathcal P+2\ell\mathcal Q,
$$




$$
\widetilde{\mathsf C}_E
=\mathcal G+\mathcal P-2(\ell+1)\mathcal Q.
$$


Then


$$
16U=\widetilde{\mathsf C}_U
-\widetilde{\mathsf A}\Theta_\ell
-\widetilde{\mathsf B}\Theta_{\ell-1},
$$




$$
16E_K=\widetilde{\mathsf C}_E
+\widetilde{\mathsf A}\Phi_\ell
+\widetilde{\mathsf B}\Phi_{\ell-1}.
\tag{3.9}
$$


No coefficient-content statement is used as a theorem about the numerical gcd $c$.

---

# 4. New canonical Hermite-coordinate coefficients

For readability, write $P_r=P_r^{\mathrm H}$, $Q_r=Q_r^{\mathrm H}$ in Sections 4–6.

## 4.1 A polynomial origin, not a numerical Bézout choice

Introduce


$$
y=t(1-t),\qquad w=2t-1.
$$


Then


$$
w^2=1-4y.
$$



The complete degree-six multiplier has the exact decomposition


$$
\boxed{
2\mathcal H
=
y(5-8y+2y^2)+w\,y(3-2y).
}
\tag{4.1}
$$


Indeed,


$$
(1+t^2)^2=1-3y+y^2+(3-2y)t,
$$


and $t=(1+w)/2$, which proves (4.1).

Since $C_m^2$ is a symmetric polynomial in $t,1-t$, it belongs to $\mathbb Z[y]$. Consequently


$$
-2K=A_-(y)+wB_-(y),
$$


where, explicitly,


$$
\boxed{
A_-(y)=-y(5-8y+2y^2)C_m^2,\qquad
B_-(y)=-y(3-2y)C_m^2.
}
\tag{4.2}
$$


Their degrees are at most $N$ and $N-1$, respectively.

The other source polynomial is


$$
L=F^2-\delta^2.
$$


Its complete decomposition is


$$
\boxed{
L=
\left(\alpha^2C_N^2+\beta^2C_{N-1}^2-\delta^2\right)
+w\left(-2\alpha\beta\,\frac{C_NC_{N-1}}w\right).
}
\tag{4.3}
$$


Here the bracketed expressions belong to $\mathbb Z[y]$: the product $C_NC_{N-1}$ is odd in $w$, hence is divisible by $w$ in $\mathbb Z[w]$. Its quotient is even in $w$.

Thus both source polynomials have **integral** $y,w$ coordinates after the explicitly paid multiplication of $K$ by $2$. The physical degree remains at most $2N$.

Reuse the established Hermite evaluations


$$
\eta(y^r)=(-1)^r r!Q_r,\qquad
E(y^r)=(-1)^r r!P_r.
$$


The derivative identity


$$
(y^{r+1})'=-(r+1)wy^r
$$


and the zero boundary values of $y^{r+1}$ at $0,1$ imply


$$
\eta(wy^r)=(-1)^{r+1}r!Q_{r+1},
$$




$$
E(wy^r)=(-1)^{r+1}r!P_{r+1}.
\tag{4.4}
$$



Now reduce all $P_r,Q_r$, $0\le r\le N$, to the adjacent pair with indices $N-1,N$, using only the integral backward relation


$$
Z_{r-1}=Z_{r+1}-(4r+2)Z_r.
$$


This is an integral finite coordinate reduction. It is not a replacement of the original affine $s_j$-state.

For a polynomial in the integral class above, it produces the same integer coefficients for its $\eta$- and $E$-values. The determinant of the terminal $P,Q$ matrix makes these simultaneous coefficients unique.

## 4.2 Evaluated terminal coefficients

Define


$$
\boxed{
\mathsf k_r=P_rU+Q_rE_K,
}
\tag{4.5}
$$


and, with


$$
E_L=E(L)=E_F-\delta^2,
$$


define


$$
\boxed{
\mathsf f_r=\frac{P_rV-Q_rE_L}{2}.
}
\tag{4.6}
$$



Because $N$ is odd,


$$
P_NQ_{N-1}-P_{N-1}Q_N=2.
$$


The simultaneous terminal coordinates derived from (4.2)–(4.4) are therefore exactly


$$
\boxed{
-2K\longmapsto(\mathsf k_N,-\mathsf k_{N-1}),
\qquad
L\longmapsto(\mathsf f_N,-\mathsf f_{N-1}).
}
\tag{4.7}
$$


In particular,


$$
\boxed{
2U=Q_{N-1}\mathsf k_N-Q_N\mathsf k_{N-1},
}
\tag{4.8}
$$




$$
\boxed{
V=Q_{N-1}\mathsf f_N-Q_N\mathsf f_{N-1}.
}
\tag{4.9}
$$



The division by $2$ in (4.6) is paid by the integral polynomial construction. It can also be checked directly: $V\equiv E_L\pmod2$, because modulo $2$ the derivative terms of $F^2-\delta^2$ vanish and


$$
F(1)^2\equiv F(0)^2\pmod2.
$$


Since $P_r,Q_r$ are odd, $P_rV-Q_rE_L$ is even.

## 4.3 Original canonical boundary formulas for these coefficients

Define


$$
\Psi_j^{(r)}=Q_r\Phi_j-P_r\Theta_j.
$$


It has the actual seeds


$$
\Psi_0^{(r)}=0,\qquad
\Psi_1^{(r)}=Q_r-P_r,
$$


and the complete forcing


$$
\boxed{
\Psi_{j+1}^{(r)}+4j\Psi_j^{(r)}-\Psi_{j-1}^{(r)}
=
2\bigl(Q_r(-1)^j-P_r\bigr).
}
\tag{4.10}
$$



Substituting the original complete columns gives


$$
4096\mathsf k_r
=
P_r\mathsf C_U+Q_r\mathsf C_E
+\mathsf A\Psi_n^{(r)}
+\mathsf B\Psi_{n-1}^{(r)}.
\tag{4.11}
$$


Equivalently, in the smaller centered coordinates,


$$
\boxed{
16\mathsf k_r
=
P_r\widetilde{\mathsf C}_U
+Q_r\widetilde{\mathsf C}_E
+\widetilde{\mathsf A}\Psi_\ell^{(r)}
+\widetilde{\mathsf B}\Psi_{\ell-1}^{(r)}.
}
\tag{4.12}
$$



For the divided square column,


$$
\boxed{
2\mathsf f_r
=
P_r\mathsf C_V
-Q_r(\mathsf C_F^E-\delta^2)
+\mathsf P\Psi_n^{(r)}
+\mathsf Q\Psi_{n-1}^{(r)}.
}
\tag{4.13}
$$



Equations (4.12)–(4.13) are the requested original canonical boundary coefficients. They retain both affine constants, both forcings, the original seeds, and the changing paid $\alpha,\beta,\delta$. They were not obtained by choosing a Bézout representation of $c$.

---

# 5. The integer certificate and its exact evaluation

## 5.1 Explicit coefficients

Define


$$
\boxed{
a_N=2Q_N\mathsf f_{N-1},
\qquad
b_N=-Q_N\mathsf k_{N-1}.
}
\tag{5.1}
$$


Every factor is an explicitly paid integer.

Using (4.8)–(4.9),


$$
\begin{aligned}
a_NU+b_NV
&=Q_N\left(2\mathsf f_{N-1}U-\mathsf k_{N-1}V\right)\\
&=Q_{N-1}Q_N
 \left(\mathsf k_N\mathsf f_{N-1}
       -\mathsf k_{N-1}\mathsf f_N\right).
\end{aligned}
$$


Thus the desired form is obtained with


$$
B_N=
\mathsf k_N\mathsf f_{N-1}
-\mathsf k_{N-1}\mathsf f_N.
\tag{5.2}
$$



This determinant is not left unevaluated. Substitution of (4.5)–(4.6), followed by the exact terminal determinant $2$, gives


$$
\begin{aligned}
B_N
&=-\bigl(UE_L+VE_K\bigr)\\
&=-\bigl(U(E_F-\delta^2)+VE_K\bigr)\\
&=c\bigl(\tau\delta^2-\tau E_F-\nu E_K\bigr).
\end{aligned}
$$


Therefore


$$
\boxed{
a_NU+b_NV=Q_{N-1}Q_N\,c(M-E).
}
\tag{5.3}
$$



This is a source-specific certificate involving the actual divided Gaussian column.

## 5.2 Evaluating the nonzero multiplier

Put


$$
I_F=\int_0^1e^tF(t)^2\,dt,
$$


and define the exponential part of the original whole error:


$$
\epsilon_{\exp}
=
\frac{I_F+(V/U)I_K}{\delta^2}>0.
\tag{5.4}
$$


Integration by parts gives


$$
I_F=e(V+\delta^2)-E_F,\qquad
I_K=-eU-E_K.
$$


Consequently


$$
\boxed{
B_N
=
U\delta^2\bigl(\epsilon_{\exp}-(e-1)\bigr).
}
\tag{5.5}
$$



To prove its sign at every original index, a uniform bound is needed, not merely an asymptotic assertion.

### A short explicit Gaussian estimate

Let


$$
R=1+\sqrt2+\sqrt{2+2\sqrt2},
\qquad 4<R<5.
$$


Choose $\zeta=Re^{i\theta}$ satisfying


$$
\zeta+\zeta^{-1}=-2+4i.
$$


Then


$$
C_j(i)=\frac{\zeta^j+\zeta^{-j}}2,
\qquad
\sin\theta=\frac4{R-R^{-1}}>\frac45.
$$


Direct expansion of the original determinant gives


$$
d=-\frac14\left[
(R^{2N-1}-R^{-(2N-1)})\sin\theta
+(R-R^{-1})\sin((2N-1)\theta)
\right].
$$


For $N\ge2$, the first term dominates uniformly, giving


$$
|d|>\frac18R^{2N-1}.
\tag{5.6}
$$


Also,


$$
|b_j|\le |C_j(i)|<R^j.
$$


The actual $g_B$ cancels in the ratio, so


$$
\frac{|\alpha|+|\beta|}{|\delta|}
<
10R^{1-N},
$$


and hence


$$
\boxed{
\frac{(|\alpha|+|\beta|)^2}{\delta^2}
<2^{12}R^{-2N}.
}
\tag{5.7}
$$


No Gaussian coefficient is frozen, and no divisibility at a prime of $g_B$ is presumed.

On $[0,1]$,


$$
|F(t)|\le|\alpha|+|\beta|,
$$


so


$$
I_F<3(|\alpha|+|\beta|)^2.
$$


The elementary coefficient norm bound


$$
\|C_j(1-z)\|_1<6^j
$$


gives


$$
V<(|\alpha|+|\beta|)^2\,36^N(2N)!.
$$


Using the retained lower bound (2.5),


$$
\frac VU
<
2^{16}\left(\frac94\right)^N
(|\alpha|+|\beta|)^2.
$$


Together with $I_K<1$ and (5.7), this yields


$$
\epsilon_{\exp}
<
2^{14-4N}+2^{28-2N}
<\frac18
\qquad(N\ge16).
\tag{5.8}
$$


Every original $N$ lies in this range.

Since $2<e<3$, equations (5.5)–(5.8) prove


$$
\boxed{
-2U\delta^2<B_N<-\frac78U\delta^2<0.
}
\tag{5.9}
$$


Thus the certificate has a rigorously nonzero multiplier at the same original indices.

## 5.3 Exact state and height payment

Equation (5.9) also gives


$$
\boxed{\frac78M<E-M<2M.}
\tag{5.10}
$$


Thus the remaining original state factor is not an unspecified quotient: it is the positive integer $E-M$, quantitatively comparable to the actual $M=\tau\delta^2$.

Since $|\delta|<R^{2N-1}$ and $\delta$ is a nonzero integer,


$$
\log|B_N|
=\log U+2\log|\delta|+O(1)
=2N\log N+O(N).
\tag{5.11}
$$


Furthermore, (2.4) and (5.10) imply


$$
\log(E-M)
=\log U-\log c+2\log|\delta|+O(1)
\ge N\log N-O(N).
\tag{5.12}
$$


Even hypothetical free cancellation of the whole factor $c$ would therefore leave factorial-scale height.

The prime-depth accounting is exact:


$$
\boxed{
v_p(B_N)=v_p(c)+v_p(E-M)
\quad\text{for every prime }p.
}
\tag{5.13}
$$


It follows that the deduction


$$
c\mid Q_{N-1}Q_NB_N
$$


is arithmetically vacuous for HC in this unnormalized certificate: $B_N$ already contains the entire $c$ at every prime and every depth.

This is not a fixed-prime exception or a generic affine counterexample. It is an evaluated obstruction in the actual original polynomials.

No factorial divisibility is asserted. The estimates show factorial-scale **height**; they do not show $N!\mid B_N$. At each $p>N$, the factorial allowance remains zero.

---

# 6. Primitive normalization: what it pays and what it cannot pay

## 6.1 A natural coefficient-row normalization still leaves factorial height

The reused binary endpoint data give


$$
U\equiv12\pmod{16},\qquad E_K\equiv1\pmod8.
$$


Since $P_r,Q_r$ are odd,


$$
\mathsf k_r=P_rU+Q_rE_K
$$


is odd.

Define the actual numerical gcd


$$
d_N^{\rm cert}
=\gcd(\mathsf k_{N-1},\mathsf f_{N-1})>0.
\tag{6.1}
$$


This is not a polynomial-row gcd. It is odd and divides $B_N$.

The established signed Hermite error gives, because $N-1$ is even,


$$
\mathsf k_{N-1}
=-UI_{N-1}^{\mathrm H}-Q_{N-1}I_K<0.
$$


Moreover,


$$
\mathsf k_{N-1}
=\frac{\mathcal R_{N-1;N}}{d_K}+Q_{N-1}R_K.
$$


Since $R_K>0$, the reused return bound implies


$$
0<|\mathsf k_{N-1}|<36^N N!.
$$


Hence


$$
d_N^{\rm cert}<36^N N!.
\tag{6.2}
$$



Dividing (5.3) by $d_N^{\rm cert}$ is integral in every coefficient and in $B_N$. Nevertheless, from (2.5), (5.9), and (6.2),


$$
\frac{|B_N|}{d_N^{\rm cert}}
>
\frac7{8\cdot2^{16}}
\left(\frac49\right)^N
\frac{(2N)!}{N!}\,\delta^2.
\tag{6.3}
$$


In particular,


$$
\boxed{
\log\frac{|B_N|}{d_N^{\rm cert}}
\ge N\log N-O(N).
}
\tag{6.4}
$$



Thus ordinary primitive normalization of the canonical coefficient row still cannot produce the required exponential multiplier.

## 6.2 The exact additional division still available

After division by $d_N^{\rm cert}$,


$$
\gcd\left(
\frac{2\mathsf f_{N-1}}{d_N^{\rm cert}},
\frac{\mathsf k_{N-1}}{d_N^{\rm cert}}
\right)=1.
$$


Therefore the remaining common divisor of the two certificate coefficients is exactly $Q_N$.

The largest further common integer division that also preserves an integer multiplier is


$$
\boxed{
\chi_N=
\gcd\left(Q_N,\frac{B_N}{d_N^{\rm cert}}\right).
}
\tag{6.5}
$$


It produces the fully normalized certificate


$$
a_N^*U+b_N^*V=Q_{N-1}Q_N B_N^*,
$$


where


$$
a_N^*=\frac{2Q_N\mathsf f_{N-1}}{d_N^{\rm cert}\chi_N},
\qquad
b_N^*=-\frac{Q_N\mathsf k_{N-1}}{d_N^{\rm cert}\chi_N},
$$




$$
\boxed{
B_N^*=\frac{c(M-E)}{d_N^{\rm cert}\chi_N}.
}
\tag{6.6}
$$


All these divisions are integral, and


$$
\gcd(a_N^*,b_N^*,B_N^*)=1.
$$



At every prime,


$$
\boxed{
v_p(B_N^*)
=
\max\left\{
0,\,
v_p(c)+v_p(E-M)-v_p(d_N^{\rm cert})-v_p(Q_N)
\right\}.
}
\tag{6.7}
$$


This formula includes $2$, primes dividing the Gaussian data, and primes larger than $N$. It identifies the remaining unpaid depths exactly; it does not bound them.

## 6.3 A concrete follow-on lemma

The following is a specific sufficient lemma for this certificate route.

> **Terminal determinant capture lemma — open.**  
> For the actual original indices and the explicit canonical coefficients
> (4.12)–(4.13), prove that a constant $C$ exists such that
> 

$$
> \boxed{
> \frac{|c_N(M_N-E_N)|}
> {d_N^{\rm cert}
>  \gcd\!\left(Q_N^{\mathrm H},
>      c_N(M_N-E_N)/d_N^{\rm cert}\right)}
> \le e^{CN}.
> }
> \tag{TDC}
>
$$



If (TDC) holds, the normalized identity (6.6) proves HC, since


$$
\frac{c_N}{\gcd(c_N,Q_{N-1}^{\mathrm H}Q_N^{\mathrm H})}
\mid B_N^*.
$$



This lemma is substantially stronger than a coefficient-primitivity assertion. The lower bound (6.4) shows that it must capture a remaining factorial-scale multiplier by the actual $Q_N$. Moreover, since


$$
Q_N<2\cdot4^N N!,
$$


(TDC) necessarily requires


$$
d_N^{\rm cert}\ge N!e^{-O(N)}.
$$


Thus this route demands a large numerical common divisor of the two actual canonical coefficient values, together with correctly synchronized residual divisibility by $Q_N$. Neither assertion follows from their construction.

**Status:** (TDC) is a concrete follow-on obligation, not a proved theorem. Its failure would obstruct this certificate route, not disprove HC.

---

# 7. Retained returns, final denominator, and whole error

The new source-only certificate does not replace any original return or arc.

The source return remains


$$
z_n=4096\mathsf Q U-\mathsf B V,\qquad
z_{n-1}=\mathsf A V-4096\mathsf P U,
$$




$$
z_j=-\Delta\Theta_j+r_j,\qquad
z_{j-1}=z_{j+1}+4jz_j,
$$




$$
r_{j-1}=r_{j+1}+4jr_j-2\Delta,
$$


with its original complete terminal constants.

The endpoint return retains


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
\sigma_{j-1}
=\sigma_{j+1}+4j\sigma_j+2D\Delta(-1)^j,
$$


and


$$
z_nw_{n-1}-z_{n-1}w_n
=-4096\Delta(UX+VY).
$$


No division by $\Delta$ is made.

The square arc still has the complete return


$$
\xi_{j+1}=4\upsilon_j-2\xi_j-\xi_{j-1}+16b_j,
$$




$$
\upsilon_{j+1}
=-4\xi_j-2\upsilon_j-\upsilon_{j-1}+16(\ell_j-a_j),
$$


with zero initial values at $j=0,1$, where


$$
\ell_j=
\begin{cases}
0,&j\ \text{odd},\\
(1-j^2)^{-1},&j\ \text{even}.
\end{cases}
$$


Thus


$$
R_F=
\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
      -2\alpha\beta\xi_{n-1}}2.
$$



The original positive polynomial is


$$
P_N(t)=\frac{F(t)^2+(V/U)K(t)}{\delta^2}.
$$


Its whole error is


$$
\epsilon_N
=
\int_0^1P_N(t)
\left(e^t+\frac4{1+t^2}\right)\,dt>0,
$$


and


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0,
\qquad q_N=\frac{\lambda_NM_N}{G_N}.
}
\tag{7.1}
$$



For completeness, the whole rational enclosure remains


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


In particular,


$$
q_NJ_N=\frac{\lambda_N}{G_N}
       (\tau_NJ_F+\nu_NJ_K).
$$


Neither positive term is discarded.

If HC were proved, the reused exact factorization (2.2) would imply


$$
\mathfrak J_N^0\le e^{O(N)}U_N^{3/4}.
$$


Then, using (2.3) and $\mu_N<256^N$,


$$
q_N\ge e^{-O(N)}U_N^{1/4},
$$


and the retained


$$
\epsilon_N\asymp R^{-2N}
$$


would give


$$
\log(q_N\epsilon_N)
\ge\frac12N\log N-O(N)\longrightarrow+\infty.
$$



That is only a **conditional retirement of this producer**. It is not a rationality or irrationality proof for $e+\pi$.

---

# 8. Bounded exact-arithmetic receipt for the new work

No original enormous index, Gaussian recurrence run, old source table, Wick enumeration, or arbitrary-prime scan is requested.

The following fixed symbolic checks are sufficient to inspect the new algebra.

## 8.1 Inputs

1. The degree-six polynomial
   

$$
\mathcal H=t(1-t)(1+t^2)^2,
$$


   with substitutions $y=t(1-t)$, $w=2t-1$.

2. Formal integer symbols
   

$$
U,V,E_K,E_L,P_{N-1},Q_{N-1},P_N,Q_N
$$


   subject only to
   

$$
P_NQ_{N-1}-P_{N-1}Q_N=2.
$$



3. The definitions
   

$$
\mathsf k_r=P_rU+Q_rE_K,\qquad
   2\mathsf f_r=P_rV-Q_rE_L.
$$



4. The displayed fixed square coefficients
   $\mathsf P,\mathsf Q,\mathsf C_V,\mathsf C_F^E,\mathsf T$.

5. Formal adjacent symbols for the reconciliation
   

$$
\rho_j=2r_j-\Delta/j.
$$



No recurrence needs to be evaluated at a numerical original $N$.

## 8.2 Expected verifiable outputs

### Complete midpoint multiplier
A zero polynomial residual for


$$
2\mathcal H-y(5-8y+2y^2)-wy(3-2y).
$$



### Terminal coordinate identities
Zero residuals for


$$
Q_{N-1}\mathsf k_N-Q_N\mathsf k_{N-1}-2U,
$$




$$
Q_{N-1}\mathsf f_N-Q_N\mathsf f_{N-1}-V.
$$



### Evaluated determinant
After clearing the displayed factor $2$, a zero residual for


$$
\mathsf k_N\mathsf f_{N-1}
-\mathsf k_{N-1}\mathsf f_N
+UE_L+VE_K.
$$



### Full affine square constant
After multiplication by $n(n-1)$, a zero residual for


$$
2\mathsf C_V-\frac{\mathsf P}{n}
-\frac{\mathsf Q}{n-1}-\mathsf T.
$$



### Opposite forcing
After multiplication by the fixed denominator product
$j(j-1)(j+1)$, a zero residual verifying that


$$
\rho_j=2r_j-\Delta/j
$$


converts


$$
r_{j-1}=r_{j+1}+4jr_j-2\Delta
$$


into


$$
\rho_{j-1}
=\rho_{j+1}+4j\rho_j-\frac{2\Delta}{j^2-1}.
$$



### Explicit cutoff arithmetic
The positive rational difference


$$
\frac18-\left(2^{-50}+2^{-4}\right)
=
\frac{2^{46}-1}{2^{50}}>0.
$$



These outputs would verify the stated bounded algebra. They would not prove HC, (TDC), a final-gcd bound, producer retirement, or any statement about the rationality of $e+\pi$.

---

# 9. Final conclusions

## New proved results

- The later pairwise-Jensen implication **passes**, under its explicit relative-factor, integrability, and spread premises.
- The exact improved gain is
  

$$
R_{\star,k}
  =\frac{k(k-1)}2
   \log\frac{85k^2-37k+6}{77k^2-43k+8},
$$


  with limiting coefficient
  

$$
\frac12\log(85/77)>\frac4{85}.
$$


- The original signed source has an explicit canonical integer certificate
  

$$
a_NU_N+b_NV_N
  =Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}B_N,
$$


  whose coefficients are given by the complete original boundary formulas
  (4.12)–(4.13).
- Its multiplier is evaluated:
  

$$
B_N=c_N(M_N-E_N)<0,\qquad
  \frac78U_N\delta_N^2<|B_N|<2U_N\delta_N^2.
$$


- The natural coefficient-row normalization still leaves at least
  $N\log N-O(N)$ logarithmic height.

## Exact remaining bottleneck

The unnormalized determinant contains all of the source content $c_N$, at every prime and depth. Its remaining primitive endpoint factor $E_N-M_N$ is itself factorial-scale. The only further common integral division in this particular normalized certificate is the explicitly identified


$$
\chi_N=
\gcd\left(Q_N^{\mathrm H},B_N/d_N^{\rm cert}\right).
$$


Controlling the residual multiplier in (6.6), uniformly at the original indices and at all primes, is the concrete open obligation for this route.

Neither adjacent Hermite coprimality, a centered coefficient-row theorem, nor a fixed-prime exception supplies that control.

The original domain, finite terminal, complete columns, both forcings, paid Gaussian divisions, actual contents, reduced arcs, least simultaneous and aggregate clearers, final ALL-prime $G_N$, actual denominator $q_N$, and positive whole error have all been retained.

**The research advance is a passed conditional convexity audit and a proved, quantitatively evaluated source-certificate obstruction. HC, producer retirement, and an unconditional determination of the rationality or irrationality of $e+\pi$ remain open.**
