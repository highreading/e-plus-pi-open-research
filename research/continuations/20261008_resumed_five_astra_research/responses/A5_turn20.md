> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A mixed source–endpoint forcing invariant after the second collision

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains open. This report does **not** prove any of the three primary conclusions requested in the assignment:

- an $O(N)$ bound for the complete surviving contact-depth mass;
- universal nonvanishing of the actual third source pair;
- divisibility of the entire surviving product into a nonzero, fixed-$N$, exponential-height integer or norm.

The new result is instead a **different actual finite invariant**, constructed from the original source and endpoint systems after subtracting their actual residual forcings. Its initial determinant is evaluated by the supplied Hermite anchoring, including all four exact base defects. Its subsequent evolution retains the inhomogeneous forcing.

The report proves four facts about this invariant.

1. Its determinant is a $p$-adic unit at every prime in the present non-arc interval, but its **actual numerical size is factorial**, not exponential. Explicit upper and lower bounds are given. In particular, an apparent factorial normalization is not an integral division: the relevant factorial is divisible by $p$, while the determinant is not.

2. Two mixed minors involving the actual Gaussian column satisfy a complete integer divisor identity. They are not both zero. Their joint divisor is the actual joint source divisor, multiplied by an explicitly bounded conditioning factor.

3. A short elimination using the **corrected $K$-constant** proves that the $K$-coefficient row is primitive at every remaining source collision. Together with the new determinant, this gives two complementary source–endpoint charts. One chart is always available, **including at determinant-critical primes**.

4. These charts give an exact, conditioning-free expression for the full remaining source depth and its complete post-credit part. The unresolved question becomes a specific additive cancellation between a Gaussian–endpoint minor and the evaluated mixed forcing determinant. No nonvanishing of that cancellation is asserted.

Thus the report supplies the fallback requested in the assignment: a new actual finite invariant, its proved divisor direction, its normalization and height bill, and an explicit remaining additive obstruction. It does not present a unit determinant or a small real quotient as a substitute for the required arithmetic depth bound.

---

# 1. Original objects and the precise branch being continued

## 1.1 Domain, Gaussian division, and actual contents

Throughout,


$$
\boxed{N=9^{18+32u}=3^{36+64u},\qquad u\in\mathbb Z_{\ge0},}
$$


and


$$
n=2N,\qquad m=N-3,\qquad \ell=2N-6.
$$


The physical terminal is always $n$.

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


with


$$
C_0=1,\qquad C_1=2t-1,\qquad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$


The actual Gaussian normalization is


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



For integer polynomials,


$$
\eta(H)=\sum_j j![z^j]H(1-z),\qquad
E(H)=\sum_j(-1)^j j![t^j]H(t).
$$


Put


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad K=\mathcal H C_m^2,
$$




$$
U=-\eta(K),\qquad V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$


The retained original-domain normalization is


$$
\operatorname{cont}(W_{\rm raw})=g_B^2c,
$$




$$
\tau=U/c,\qquad \nu=V/c,\qquad
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2,
$$


with $U,V,M>0$.

No auxiliary gcd introduced below replaces $c$.

## 1.2 The complete reduced endpoint credit

Write


$$
L(x)=(x-1)(x-9)(x-25),\qquad
A_K(x)=13x^3-455x^2+3502x-5850.
$$


Retain the actual lowest-term reduction


$$
R_K=\frac{A_K(\ell^2)}{30L(\ell^2)}=\frac{a_K}{d_K},
$$


where


$$
g_{\rm arc}
=90\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}},
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


Set


$$
E_K=E(K),\qquad y_K=d_KE_K-a_K.
$$


Then


$$
\gcd(a_K,d_K)=\gcd(d_K,y_K)=1.
$$



The intrinsic factors remain


$$
\gamma=\gcd(\tau,y_K),\qquad
b^\circ=\gcd(\gamma,a_K),\qquad r^\circ=\gamma/b^\circ.
$$


For every prime,


$$
c_p=\min(v_p(U),v_p(V)),\qquad
t_p=v_p(U)-c_p,
$$




$$
z_p=v_p(y_K),\qquad
b_p=v_p(b^\circ),\qquad
h_p=v_p(Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}),
$$


and the exact complete credit is


$$
\boxed{H_p=h_p+2b_p+2(z_p-t_p)_+.}
$$


The actual fixed-product multiplier therefore has


$$
\boxed{k_p=[c_p-H_p]_+.}
\tag{1.1}
$$



In particular, the Hermite credit is still at $N-1,N$, not at a residual or anchoring index.

## 1.3 Both finite affine systems

The original states have


$$
\Theta_0=\Phi_0=0,\qquad \Theta_1=\Phi_1=1,
$$


and, for exactly $1\le j\le n-1$,


$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
\tag{1.2}
$$


Equivalently,


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
\tag{1.3}
$$


Both forcing coordinates are retained.

At $x=\ell^2$, let


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


The complete corrected $K$-columns are


$$
16U=\mathscr C_U-\mathscr A\Theta_\ell-\mathscr B\Theta_{\ell-1},
$$




$$
16E_K=\mathscr C_E+\mathscr A\Phi_\ell+\mathscr B\Phi_{\ell-1}.
\tag{1.4}
$$



At the physical terminal,


$$
V=C_V-P\Theta_n-Q\Theta_{n-1},
$$




$$
E_F=C_F^E-P\Phi_n-Q\Phi_{n-1},
\tag{1.5}
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
\tag{1.6}
$$



The already established six-step transport gives


$$
V=C^{\rm s}-\Pi\Theta_\ell-\Omega\Theta_{\ell-1},
$$




$$
E_F=C^{\rm e}-\Pi\Phi_\ell-\Omega\Phi_{\ell-1}.
\tag{1.7}
$$


For an exact finite definition, put


$$
T_j=\begin{pmatrix}-4j&1\\1&0\end{pmatrix},
\qquad T=T_{\ell+5}\cdots T_\ell.
$$


Starting from zero vectors, apply the six updates


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
C^{\rm e}=C_F^E-(P,Q)g_6.
$$


The largest original recurrence step is $\ell+5=n-1$.

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


The established numerical bills are


$$
|\Delta|,\ J_N^{\rm aff}
<
10^{10}(2N)^{15}\frac{5^{4N}}{g_B^2}.
\tag{1.8}
$$



These complete columns, transports and determinant bounds are reuse, not the new result.

## 1.4 The input branch

We continue precisely


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


Thus


$$
p^2\mid U,\qquad p^2\mid V.
\tag{1.9}
$$



Write


$$
r=n-p,\qquad s=r-6,\qquad k=(p+1)/2.
$$


The established boundary calculation gives


$$
\boxed{13\le r<N,\quad r\ \text{odd},\quad s\ge7,\quad s\ \text{odd},\quad k\le N-6.}
\tag{1.10}
$$


Also $p\nmid d_K$.

The actual third source pair already evaluated in turn19 is


$$
\boxed{
\mathscr L_U\equiv16U/p^2,\qquad
\mathscr L_V\equiv V/p^2\pmod p.
}
\tag{1.11}
$$


Its Hermite-anchored evaluation, both quotient recurrences, both $Y$-columns and their precision requirements are reused. They are not reproduced as a new theorem.

The first two layers are already paid:


$$
\sum_{p\in\mathcal S_N}[2-H_p]_+\log p\le4N\log2.
\tag{1.12}
$$


The outstanding depth is


$$
e_p:=\bigl[c_p-2-(H_p-2)_+\bigr]_+.
\tag{1.13}
$$


Turn19 compares its mass with $\mathfrak C_N^{\rm lift}$, with a total conditioning discrepancy at most $\log|\Delta|$. Nothing below assumes that either remaining mass is $O(N)$.

---

# 2. A new residual-relative forcing determinant

The new construction is not the old determinant of the two homogeneous source and endpoint returns. It compares the actual shifted states with their **actual residual states**, so that the difference of the two recurrence coefficients remains as an explicit forcing.

For $0\le j\le r$, define


$$
x_j=\Theta_{p+j}-\Theta_j,\qquad
y_j=\Phi_{p+j}+\Phi_j.
\tag{2.1}
$$


The plus sign in $y_j$ is forced by the oddness of $p$.

For $1\le j\le r-1$, subtraction in the original recurrences gives


$$
x_{j+1}+4(p+j)x_j-x_{j-1}=-4p\Theta_j,
$$




$$
y_{j+1}+4(p+j)y_j-y_{j-1}=4p\Phi_j.
\tag{2.2}
$$


Thus neither system has been made homogeneous by omission. Its residual forcing is explicitly a multiple of $p$.

Define the actual integer determinant


$$
\boxed{
\mathfrak D_{j;p}
=x_jy_{j-1}-x_{j-1}y_j,\qquad 1\le j\le r.
}
\tag{2.3}
$$



## Theorem 2.1 — Exact mixed-forcing evolution and Hermite seed

For every original $N$ and every prime in the non-arc interval under consideration:

1. The seed is
   

$$
\mathfrak D_{1;p}
   =(\Theta_{p-1}+1)\Phi_p
    -\Theta_p(\Phi_{p-1}-1).
   \tag{2.4}
$$



2. Put
   

$$
\mathfrak M_{j;p}
   =-\bigl(\Theta_j\Phi_{p+j}+\Phi_j\Theta_{p+j}\bigr).
   \tag{2.5}
$$


   Then
   

$$
\boxed{
   \mathfrak D_{j+1;p}
   =-\mathfrak D_{j;p}+4p\mathfrak M_{j;p},
   \qquad 1\le j\le r-1.
   }
   \tag{2.6}
$$



3. The complete Hermite-anchored seed is given by (2.9) below, including both pairs of exact base defects.

4. In particular,
   

$$
\boxed{p\nmid\mathfrak D_{j;p}\quad(1\le j\le r).}
   \tag{2.7}
$$



### Proof

At $j=1$, the original recurrence at $p$ gives


$$
x_1=-4p\Theta_p+\Theta_{p-1}+1,
$$




$$
y_1=-4p\Phi_p+\Phi_{p-1}-1.
$$


Together with $x_0=\Theta_p$, $y_0=\Phi_p$, this proves (2.4).

Using (2.2),


$$
\begin{aligned}
\mathfrak D_{j+1;p}
&=\bigl(-4(p+j)x_j+x_{j-1}-4p\Theta_j\bigr)y_j\\
&\quad-x_j\bigl(-4(p+j)y_j+y_{j-1}+4p\Phi_j\bigr)\\
&=-\mathfrak D_{j;p}
  -4p(\Theta_jy_j+\Phi_jx_j).
\end{aligned}
$$


The two residual products cancel:


$$
\Theta_jy_j+\Phi_jx_j
=\Theta_j\Phi_{p+j}+\Phi_j\Theta_{p+j}.
$$


This proves (2.6).

For the Hermite seed, retain


$$
P_0^{\mathrm H}=Q_0^{\mathrm H}=1,\qquad
P_1^{\mathrm H}=3,\quad Q_1^{\mathrm H}=1,
$$




$$
Z_{a+1}=(4a+2)Z_a+Z_{a-1},\qquad 1\le a\le N-1,
$$


and


$$
P_k^{\mathrm H}Q_{k-1}^{\mathrm H}
-P_{k-1}^{\mathrm H}Q_k^{\mathrm H}
=2(-1)^{k-1}.
$$



Let


$$
\chi=2k!.
$$


The supplied universal base identities, whose hypotheses hold by (1.10), make the following four quantities integers:


$$
\sigma_0^+
=\frac{\Theta_p-\chi Q_{k-1}^{\mathrm H}}p,\qquad
\sigma_1^+
=\frac{\Theta_{p-1}+1+\chi Q_k^{\mathrm H}}p,
$$




$$
\sigma_0^-
=\frac{\Phi_p-\chi P_{k-1}^{\mathrm H}}p,\qquad
\sigma_1^-
=\frac{\Phi_{p-1}-1+\chi P_k^{\mathrm H}}p.
\tag{2.8}
$$


These are the actual turn19 defects, not free variables.

Define


$$
\begin{aligned}
\Lambda_\sigma={}&
P_k^{\mathrm H}\sigma_0^+
+P_{k-1}^{\mathrm H}\sigma_1^+
-Q_k^{\mathrm H}\sigma_0^-
-Q_{k-1}^{\mathrm H}\sigma_1^-,\\
\Xi_\sigma={}&
\sigma_1^+\sigma_0^-
-\sigma_0^+\sigma_1^-.
\end{aligned}
$$


Expansion of (2.4) now gives the exact integer identity


$$
\boxed{
\mathfrak D_{1;p}
=2(-1)^{k-1}\chi^2
+p\chi\Lambda_\sigma+p^2\Xi_\sigma.
}
\tag{2.9}
$$


Because $k<p$, the integer $\chi$ is a $p$-adic unit. Equation (2.6) therefore yields


$$
\mathfrak D_{j;p}
\equiv(-1)^{j-1}2(-1)^{k-1}\chi^2\not\equiv0\pmod p.
$$


This proves (2.7). ∎

### 2.1 A finite evaluation of the complete forcing contribution

To avoid leaving the invariant as a named unevaluated sum, define


$$
\mathfrak f_{1;p}=0,\qquad
\mathfrak f_{j+1;p}=\mathfrak M_{j;p}-\mathfrak f_{j;p}
\quad(1\le j\le r-1).
\tag{2.10}
$$


These are exact integer updates using the two actual original systems. Induction in (2.6) gives


$$
\mathfrak D_{j;p}
=(-1)^{j-1}\mathfrak D_{1;p}+4p\mathfrak f_{j;p}.
\tag{2.11}
$$


Since $s$ is odd,


$$
\boxed{
\mathfrak D_{s;p}
=2(-1)^{k-1}\chi^2
+p\chi\Lambda_\sigma+p^2\Xi_\sigma
+4p\mathfrak f_{s;p}.
}
\tag{2.12}
$$



All indices in this calculation are physical:

- residual states have indices at most $r<N$;
- shifted states have indices at most $p+r=n$;
- recurrence steps end at $n-1$;
- the Hermite seed uses only $k-1,k\le N-6$.

---

# 3. The actual size and divisor direction of the new determinant

A unit determinant does not bound contact. Here one can say more: the determinant has a demonstrably factorial numerical size in the actual original states.

## Theorem 3.1 — Positivity and explicit factorial-scale bounds

For every odd $p$ in the present original non-arc interval,


$$
\mathfrak D_{s;p}>0,
$$


and


$$
\boxed{
16p\,3^{\ell+s-6}(\ell-2)!(s-2)!
<
\mathfrak D_{s;p}
<
8p\,6^{\ell+s-4}(\ell-2)!(s-2)!.
}
\tag{3.1}
$$


Consequently,


$$
\boxed{
\log\mathfrak D_{s;p}
=(\ell-2)\log(\ell-2)
 +(s-2)\log(s-2)+O(N),
}
\tag{3.2}
$$


uniformly over the stated interval.

### Proof

For $j\ge1$, put


$$
a_j=(-1)^{j-1}\Theta_j,\qquad
b_j=(-1)^{j-1}\Phi_j,
$$


and set $a_0=b_0=0$. The original recurrences become


$$
a_{j+1}=4ja_j+a_{j-1}+2(-1)^j,
$$




$$
b_{j+1}=4jb_j+b_{j-1}+2.
\tag{3.3}
$$


The initial values are


$$
a_1=b_1=1,\qquad a_2=2,\quad b_2=6.
$$


Induction gives


$$
0<a_j\le b_j,
$$


and, for $j\ge2$,


$$
a_{j+1}\ge(4j-1)a_j\ge3ja_j,\qquad
b_{j+1}\ge4jb_j.
$$


A second induction gives the convenient uniform bounds


$$
\boxed{
2\,3^{j-2}(j-1)!\le a_j\le b_j
\le6^{j-1}(j-1)!,\qquad j\ge2.
}
\tag{3.4}
$$



We also need a bound for the initial determinant. Let


$$
C_j=a_jb_{j-1}-a_{j-1}b_j.
$$


Directly from (3.3),


$$
C_{j+1}=-C_j+2(-1)^j b_j-2a_j.
$$


Thus $C_j>0$ for odd $j\ge3$, and $C_j<0$ for even $j\ge2$. Moreover,


$$
|C_p|\le2\sum_{j=1}^{p-1}(a_j+b_j)
<4(a_{p-1}+b_{p-1}).
$$


Because $p\ge3$,


$$
C_p<\frac23(a_p+b_p).
$$


Equation (2.4), with $p$ odd, reads


$$
\mathfrak D_{1;p}=a_p+b_p+C_p.
$$


Hence


$$
0<\mathfrak D_{1;p}<2(a_p+b_p).
\tag{3.5}
$$



The opposite parities of $j$ and $p+j$ give


$$
\mathfrak M_{j;p}=a_jb_{p+j}+b_ja_{p+j}>0.
\tag{3.6}
$$


Also


$$
\mathfrak M_{1;p}=a_{p+1}+b_{p+1}
\ge3p(a_p+b_p),
$$


and the growth bounds imply


$$
\mathfrak M_{j+1;p}\ge2\mathfrak M_{j;p}.
$$


Using (2.6) and (3.5), induction gives, for every $j\ge2$,


$$
\boxed{
2p\mathfrak M_{j-1;p}
<\mathfrak D_{j;p}
<4p\mathfrak M_{j-1;p}.
}
\tag{3.7}
$$



At $j=s$,


$$
\mathfrak M_{s-1;p}
=a_{s-1}b_{\ell-1}+b_{s-1}a_{\ell-1}.
$$


Substituting the lower and upper bounds from (3.4) into (3.7) gives exactly (3.1). Stirling’s elementary logarithmic estimate then gives (3.2). ∎

## 3.1 An original-object obstruction to an unpaid factorial division

The factorial scale in (3.1) is a magnitude estimate, **not a divisibility assertion**.

Indeed, for every prime in the present interval,


$$
\ell-2=p+s-2,\qquad 0<s-2<p,\qquad \ell-2<2p.
$$


Therefore


$$
v_p\bigl((\ell-2)!(s-2)!\bigr)=1,
$$


whereas Theorem 2.1 proves


$$
v_p(\mathfrak D_{s;p})=0.
\tag{3.8}
$$



Thus the attractive normalization


$$
\frac{\mathfrak D_{s;p}}{(\ell-2)!(s-2)!}
$$


is not an integer at the very original primes being studied. Its $p$-adic valuation is $-1$.

This is an obstruction in the actual original systems, not a free-input or auxiliary numerical example. It does **not** disprove third-depth avoidance. It disproves only the proposed unpaid use of this factorial as an integer height cancellation.

Likewise, no positive surviving contact factor at $p$ can divide $\mathfrak D_{s;p}$ itself: that determinant is a unit at $p$. The contact must enter a **difference involving the determinant**, not the determinant alone.

---

# 4. The actual Gaussian–endpoint mixed minors

We now attach the actual divided Gaussian column. All coefficients remain those of the original $N$, not coefficients obtained by replacing $N$ by a residual index.

Let


$$
\mathbf u=\binom{u_1}{u_2}:=\binom{16U}{V},
\qquad
\mathsf M=
\begin{pmatrix}
\mathscr A&\mathscr B\\
\Pi&\Omega
\end{pmatrix}.
$$


Define the residual source vector


$$
\boxed{
\begin{aligned}
R_1&=\mathscr C_U-\mathscr A\Theta_s-\mathscr B\Theta_{s-1},\\
R_2&=C^{\rm s}-\Pi\Theta_s-\Omega\Theta_{s-1},
\end{aligned}}
\tag{4.1}
$$


and the complete relative endpoint vector


$$
\boxed{
\begin{aligned}
E_1&=16E_K-\mathscr C_E
       +\mathscr A\Phi_s+\mathscr B\Phi_{s-1},\\
E_2&=C^{\rm e}-E_F
       +\Pi\Phi_s+\Omega\Phi_{s-1}.
\end{aligned}}
\tag{4.2}
$$


Write $\mathbf R=(R_1,R_2)^t$ and $\mathbf E=(E_1,E_2)^t$.

These are not substitute source or endpoint producers. For example, $R_1$ uses the coefficients at $\ell$ and the states at $s$.

The complete column identities give


$$
\boxed{
\mathsf M\binom{x_s}{x_{s-1}}=\mathbf R-\mathbf u,\qquad
\mathsf M\binom{y_s}{y_{s-1}}=\mathbf E.
}
\tag{4.3}
$$


Consequently,


$$
\det(\mathbf R-\mathbf u,\mathbf E)
=\Delta\mathfrak D_{s;p}.
\tag{4.4}
$$



Define two actual integer minors:


$$
\boxed{
\mathfrak A_{p,N}=\det(\mathbf R,\mathbf u)
=R_1V-R_2\,16U,
}
$$




$$
\boxed{
\mathfrak B_{p,N}=\det(\mathbf u,\mathbf E)
=16U\,E_2-V E_1.
}
\tag{4.5}
$$



## Theorem 4.1 — Complete additive identity and nonzero minor pair

At every original $(N,p)$ in the stated interval,


$$
\boxed{
\mathfrak B_{p,N}
=R_1E_2-R_2E_1-\Delta\mathfrak D_{s;p}.
}
\tag{4.6}
$$


More explicitly,


$$
\boxed{
\begin{aligned}
\mathfrak B_{p,N}
={}&R_1E_2-R_2E_1\\
&-\Delta\left(
2(-1)^{k-1}\chi^2
+p\chi\Lambda_\sigma+p^2\Xi_\sigma
+4p\mathfrak f_{s;p}
\right).
\end{aligned}}
\tag{4.7}
$$


The pair $(\mathfrak A_{p,N},\mathfrak B_{p,N})$ is not $(0,0)$ as an integer pair.

### Proof

Equation (4.6) is the expansion of (4.4). Equation (4.7) follows from (2.12).

Cramer’s identity, used without any division, gives


$$
\boxed{
(\mathbf R-\mathbf u)\mathfrak B_{p,N}
+\mathbf E\,\mathfrak A_{p,N}
=\Delta\mathfrak D_{s;p}\,\mathbf u.
}
\tag{4.8}
$$


If both minors were zero, the right side would be zero. But


$$
\Delta\ne0,\qquad \mathfrak D_{s;p}>0,\qquad u_1=16U>0.
$$


This is impossible. ∎

For the other minor, direct substitution in (4.1) gives the useful additive expansion


$$
\boxed{
\begin{aligned}
\mathfrak A_{p,N}
={}&\mathscr I_1(\Theta_s-\Theta_\ell)
+\mathscr I_2(\Theta_{s-1}-\Theta_{\ell-1})\\
&+\Delta\bigl(
\Theta_s\Theta_{\ell-1}-\Theta_{s-1}\Theta_\ell
\bigr).
\end{aligned}}
\tag{4.9}
$$



Equations (4.7) and (4.9) are the new additive invariants. In particular, (4.7) contains:

- the actual divided Gaussian source and endpoint coefficients;
- both complete transported constants;
- both original affine systems;
- both Hermite base-defect pairs;
- the full mixed forcing contribution.

Omitting either $-\delta^2$ from $C_V$ or $4\alpha\beta$ from $C_F^E$ changes these actual minors.

---

# 5. A new arithmetic chart lemma, including critical determinants

The unit property of $\mathfrak D_{s;p}$ alone is insufficient. The corrected $K$-constant supplies an additional arithmetic fact.

## Lemma 5.1 — The $K$-coefficient row is primitive at a source collision

If $p\in\mathcal S_N$, then


$$
\boxed{\min(v_p(\mathscr A),v_p(\mathscr B))=0.}
\tag{5.1}
$$



### Proof

First $p\nmid\ell$. Indeed, $0<\ell<2p$, and $\ell$ is even whereas $p$ is odd.

Suppose $p\mid\mathscr A,\mathscr B$. From the definitions, this implies


$$
\mathcal Q(\ell^2)\equiv\mathcal P(\ell^2)\equiv0\pmod p.
$$


Because $p\mid U$, the corrected source equation (1.4) also gives


$$
\mathscr C_U\equiv0\pmod p,
$$


and hence


$$
\mathcal F(\ell^2)\equiv0\pmod p.
$$



The following fixed polynomial identities are exact:


$$
\boxed{
\mathcal Q-19\mathcal F=-20(347x+4908),
}
\tag{5.2}
$$




$$
\boxed{
\mathcal P+(2x+33)\mathcal F=2(9506x+90215).
}
\tag{5.3}
$$


As $p>N$, the factors $2,5$ are units. Thus the common zero would imply


$$
347x+4908\equiv0,\qquad
9506x+90215\equiv0\pmod p.
$$


Eliminating $x$ without dividing by either coefficient gives


$$
p\mid
347\cdot90215-9506\cdot4908
=-15\,350\,843.
$$


But $p>N=3^{36+64u}>15\,350\,843$, a contradiction. ∎

This proof uses the actual corrected constant $\mathscr C_U$. A coefficient determinant by itself would not supply the lemma.

## Theorem 5.2 — Complementary residual-source and endpoint charts

For every $p\in\mathcal S_N$,


$$
\boxed{\min(v_p(R_1),v_p(E_1))=0.}
\tag{5.4}
$$



### Proof

Modulo $p$, the matrix


$$
\begin{pmatrix}
x_s&y_s\\
x_{s-1}&y_{s-1}
\end{pmatrix}
$$


is invertible by Theorem 2.1.

If $R_1\equiv E_1\equiv0\pmod p$, then $u_1\equiv0\pmod p$ and (4.3) imply


$$
(\mathscr A,\mathscr B)
\begin{pmatrix}
x_s&y_s\\
x_{s-1}&y_{s-1}
\end{pmatrix}
\equiv(0,0)\pmod p.
$$


Invertibility would give $\mathscr A\equiv\mathscr B\equiv0\pmod p$, contradicting Lemma 5.1. ∎

The conclusion is an actual noncollision between $R_1$ and the complete endpoint expression $E_1$. It is **not** the requested noncollision of $(\mathscr L_U,\mathscr L_V)$.

## 5.1 Exact all-prime divisor identities

The following identities are ordinary integer gcd identities. Their statements do not omit the prime $2$.

Let


$$
g_0=\gcd(16U,V)>0,\qquad
\mathbf w=\mathbf u/g_0.
$$


Thus $\mathbf w$ is a primitive integer vector. Define


$$
j_{p,N}
=\gcd\bigl(\det(\mathbf R,\mathbf w),
           \det(\mathbf w,\mathbf E)\bigr)>0.
$$


Then


$$
\boxed{
\gcd(\mathfrak A_{p,N},\mathfrak B_{p,N})
=g_0j_{p,N},
\qquad
j_{p,N}\mid\Delta\mathfrak D_{s;p}.
}
\tag{5.5}
$$



The first identity follows by factoring $g_0$. For the second, extend the primitive vector $\mathbf w$ to an integer unimodular basis. In that basis, divisibility of both displayed determinants by $j_{p,N}$ says that the second coordinates of both $\mathbf R$ and $\mathbf E$ are divisible by $j_{p,N}$. Hence


$$
j_{p,N}\mid\det(\mathbf R,\mathbf E).
$$


It also divides $\mathfrak B_{p,N}$, so (4.6) gives


$$
j_{p,N}\mid\Delta\mathfrak D_{s;p}.
$$



At a prime in $\mathcal S_N$, therefore,


$$
0\le v_p(j_{p,N})\le v_p(\Delta).
\tag{5.6}
$$


Thus the two-minor invariant has only the already paid determinant-conditioning loss. The new determinant contributes no loss at these primes.

There is also a conditioning-free identity. Define


$$
\boxed{
I_{p,N}=\gcd(16U,\mathfrak A_{p,N},\mathfrak B_{p,N})>0.
}
\tag{5.7}
$$


Then, over all primes,


$$
\begin{aligned}
I_{p,N}
&=\gcd(16U,R_1V,E_1V)\\
&=\boxed{
g_0\gcd\left(\frac{16U}{g_0},R_1,E_1\right).
}
\end{aligned}
\tag{5.8}
$$


For $p\in\mathcal S_N$, Theorem 5.2 and the oddness of $p$ give


$$
\boxed{v_p(I_{p,N})=c_p.}
\tag{5.9}
$$



The auxiliary $g_0$ can differ from $c$ at $2$. Equation (5.9) uses only the present odd primes. The actual all-prime source content remains $c$.

## 5.2 An exact scalar chart at every remaining prime

Choose the actual chart


$$
\zeta_{p,N}=
\begin{cases}
\mathfrak A_{p,N},&p\nmid R_1,\\
\mathfrak B_{p,N},&p\mid R_1.
\end{cases}
\tag{5.10}
$$


In the second case, Theorem 5.2 guarantees $p\nmid E_1$.

If $p\nmid R_1$, the transformation


$$
(u_1,u_2)\longmapsto(u_1,R_1u_2-R_2u_1)
$$


has unit determinant. If $p\nmid E_1$, the corresponding transformation


$$
(u_1,u_2)\longmapsto(u_1,E_2u_1-E_1u_2)
$$


also has unit determinant. Hence


$$
\boxed{
c_p-2
=
\min\left\{
v_p(16U/p^2),\,v_p(\zeta_{p,N}/p^2)
\right\}.
}
\tag{5.11}
$$



This formula includes determinant-critical primes and does not invert $\Delta$.

At third precision,


$$
\frac{\mathfrak A_{p,N}}{p^2}
\equiv R_1\mathscr L_V-R_2\mathscr L_U\pmod p,
$$




$$
\frac{\mathfrak B_{p,N}}{p^2}
\equiv E_2\mathscr L_U-E_1\mathscr L_V\pmod p.
\tag{5.12}
$$


Thus, in the available chart,


$$
(\mathscr L_U,\mathscr L_V)=(0,0)
$$


is equivalent to


$$
\boxed{
16U/p^2\equiv0,\qquad
\zeta_{p,N}/p^2\equiv0\pmod p.
}
\tag{5.13}
$$



This is a new actual mixed-forcing representation of the open pair, not a proof that the pair is nonzero.

## 5.3 The whole post-credit depth is retained

Since $p^2$ divides all three entries in (5.7), the integer


$$
Z_{p,N}=I_{p,N}/p^2
$$


is well defined. Equation (5.9) gives


$$
v_p(Z_{p,N})=c_p-2.
$$


Put $B_p=(H_p-2)_+$. Then the exact paid quotient


$$
\boxed{
Z_{p,N}^{\rm unpaid}
=
\frac{Z_{p,N}}{\gcd(Z_{p,N},p^{B_p})}
}
\tag{5.14}
$$


satisfies


$$
\boxed{v_p(Z_{p,N}^{\rm unpaid})=e_p.}
\tag{5.15}
$$



Every division in (5.14) is proved. Every component of $H_p$ is retained.

The limitation is important: $Z_{p,N}$ depends on $p$. Merely multiplying these integers over the interval does not produce a useful fixed-$N$, exponential-height certificate.

---

# 6. Height, primitive normalization, and why the invariant does not yet pay the mass

## 6.1 A genuine cancellation in the height estimate

The form


$$
\mathfrak B_{p,N}=16U\,E_2-VE_1
$$


has a misleading naive bound involving a product of two terminal factorial scales. The alternative form


$$
\mathfrak B_{p,N}
=R_1E_2-R_2E_1-\Delta\mathfrak D_{s;p}
$$


removes that leading terminal-by-terminal scale.

Let


$$
H_G=\alpha^2+\beta^2+\delta^2
<\frac{5^{4N}}{g_B^2}
\tag{6.1}
$$


be the retained divided Gaussian bound, and put


$$
F_j^*=1+a_j+b_j+a_{j-1}+b_{j-1}.
$$


The complete coefficient bounds from the finite six-step transport, together with the displayed $K$-polynomials, give the safe explicit estimate


$$
\boxed{
|\mathfrak A_{p,N}|,\ |\mathfrak B_{p,N}|
<
10^{12}n^{16}H_G F_s^*F_\ell^*.
}
\tag{6.2}
$$



For completeness, this follows by using bounds of the form


$$
|\mathscr A|,|\mathscr B|,|\mathscr C_U|,|\mathscr C_E|
<10^5n^7,
$$




$$
|\Pi|,|\Omega|,|C^{\rm s}|,|C^{\rm e}|
<10^5n^8H_G.
$$


They bound $R_1,R_2$ at the residual scale and $u_1,u_2,E_1,E_2$ at the terminal scale. The determinant term is bounded using


$$
\mathfrak D_{s;p}<4p\mathfrak M_{s-1;p}
\le4nF_s^*F_\ell^*.
$$


Each mixed minor contains exactly one Gaussian quadratic column, so the bound is linear in $H_G$, not quadratic in it.

Consequently,


$$
\log\max(1,|\mathfrak A_{p,N}|,|\mathfrak B_{p,N}|)
\le
2N\log N+s\log s+O(N)-2\log g_B.
\tag{6.3}
$$


This is a real cancellation in the height bill compared with the naive terminal product. It is still not $O(N)$.

## 6.2 Small real quotients are not small-height integers

Theorem 3.1 and (6.2) imply


$$
\left|\frac{\mathfrak A_{p,N}}{\mathfrak D_{s;p}}\right|
+
\left|\frac{\mathfrak B_{p,N}}{\mathfrak D_{s;p}}\right|
\le e^{O(N)}.
\tag{6.4}
$$


But (6.4) is an Archimedean size statement about rational numbers. It does not bound their reduced numerator heights by $O(N)$.

The exact normalization is as follows:


$$
d_{\rm mix}
=\gcd(\mathfrak D_{s;p},\mathfrak A_{p,N},\mathfrak B_{p,N}),
$$




$$
A_{\rm mix}=\mathfrak A_{p,N}/d_{\rm mix},\qquad
B_{\rm mix}=\mathfrak B_{p,N}/d_{\rm mix},
$$




$$
D_{\rm mix}=\mathfrak D_{s;p}/d_{\rm mix}.
\tag{6.5}
$$


Then


$$
\frac{\mathfrak A_{p,N}}{\mathfrak D_{s;p}}
=\frac{A_{\rm mix}}{D_{\rm mix}},\qquad
\frac{\mathfrak B_{p,N}}{\mathfrak D_{s;p}}
=\frac{B_{\rm mix}}{D_{\rm mix}},
$$


and


$$
\gcd(A_{\rm mix},B_{\rm mix},D_{\rm mix})=1.
$$


The integer $D_{\rm mix}$ is the **least simultaneous clearer** of these two auxiliary rationals.

It is not the original arc clearer $D$, and it does not replace $D$.

Because $p\nmid\mathfrak D_{s;p}$, neither $d_{\rm mix}$ nor $D_{\rm mix}$ contains the present prime $p$. Therefore this normalization does not discard any contact depth at $p$. However, no sufficient lower bound on $d_{\rm mix}$ is proved to make the reduced numerator pair exponential-height.

## 6.3 A nonzero norm and its exact, insufficient divisor implication

Theorem 4.1 proves


$$
\mathcal N_{p,N}=A_{\rm mix}^2+B_{\rm mix}^2>0.
\tag{6.6}
$$


Since $p^2\mid A_{\rm mix},B_{\rm mix}$, the integer


$$
\mathcal N_{p,N}^{(2)}=\mathcal N_{p,N}/p^4
$$


is positive. The full post-credit exponent satisfies the valid divisor implication


$$
\boxed{
p^{2e_p}\mid\mathcal N_{p,N}^{(2)}.
}
\tag{6.7}
$$



This is a proved direction of divisibility. It does not establish conclusion (C), for two independent reasons:

1. $\mathcal N_{p,N}^{(2)}$ varies with $p$; it is not a single fixed-$N$ certificate for the full product.
2. The proved primitive-height bill remains of factorial logarithmic scale. The exponential real-size estimate (6.4) does not remove the actual simultaneous clearer.

No bound on the full surviving mass is booked from (6.7).

---

# 7. Precision and division ledger

The new identities are exact integer identities. Their residue evaluations nevertheless require the same paid precision as the actual producer.

## 7.1 Gaussian normalization

Let


$$
a=v_p(g_B),\qquad g_B=p^ag_0,\qquad p\nmid g_0.
$$


To obtain $\alpha,\beta,\delta$ modulo $p^3$, the raw linear Gaussian data must be known modulo $p^{a+3}$, followed by the actual division by $p^ag_0$.

A raw quadratic column must instead be known modulo


$$
p^{2a+3}
$$


before division by $g_B^2$.

The new minors are homogeneous quadratic in the Gaussian data:


$$
\mathfrak A_{\rm raw}=g_B^2\mathfrak A,\qquad
\mathfrak B_{\rm raw}=g_B^2\mathfrak B.
$$


The raw and divided gcds in (5.7) are not interchangeable, because the first source coordinate $16U$ does not acquire this raw factor. The actual division must precede the contact test.

## 7.2 Hermite anchoring and the mixed determinant

The four defects in (2.8) require one paid division by $p$. To know them modulo $p^2$, their numerators must be known modulo $p^3$.

For (2.12) modulo $p^3$:

- $\chi$ and the Hermite seed data require the corresponding third precision;
- the $p\chi\Lambda_\sigma$ term requires the defects modulo $p^2$;
- the $p^2\Xi_\sigma$ term requires them modulo $p$;
- $\mathfrak f_{s;p}$ is needed modulo $p^2$.

The last item is evaluated by (2.10) from the admitted second-precision source and endpoint blocks. No third-coordinate forcing is dropped.

## 7.3 The divided mixed minors

The double source collision proves


$$
p^2\mid\mathfrak A_{p,N},\mathfrak B_{p,N}.
$$


To compute their quotients modulo $p$, their full numerators must be known modulo $p^3$.

For $\mathfrak B$, the required endpoint precision is supplied by the retained turn19 endpoint $Y$-columns. The complete constants in (4.2) remain present.

There is no division by $\Delta$ in:

- the determinant recurrence;
- the mixed-minor identity;
- the gcd identities;
- the chart selection;
- the third-digit comparison.

Thus determinant-critical primes do not require an unacknowledged determinant inversion in this new chart.

## 7.4 Endpoint credits remain actual

The integer $E_1$ may also be written


$$
E_1=
\frac{
16y_K+16a_K-d_K\mathscr C_E
+d_K\mathscr A\Phi_s+d_K\mathscr B\Phi_{s-1}
}{d_K}.
\tag{7.1}
$$


This is an exact division, paid by the definition of $y_K$. At the present primes $d_K$ is a unit.

Nevertheless, $E_1$ is not $y_K$, and Theorem 5.2 does not permit the endpoint credit to be removed. In particular, a unit $E_1$ does not imply $z_p=0$.

Third-precision information need not determine the exact $H_p$ when deeper endpoint or Hermite zeros occur. A higher-depth post-credit test must use validated information for the actual $h_p,b_p,z_p,t_p$, and correspondingly higher source precision.

---

# 8. The exact remaining additive cancellation

The new invariant identifies a definite cancellation; it does not resolve it.

At a prime where $p\mid R_1$, the available endpoint chart has $p\nmid E_1$. If the $K$-third digit vanishes, then by (5.12)


$$
\frac{\mathfrak B_{p,N}}{p^2}
\equiv-E_1\mathscr L_V\pmod p.
$$


Thus a third common collision in this chart is precisely the additive congruence


$$
\boxed{
R_1E_2-R_2E_1
\equiv
\Delta\left(
2(-1)^{k-1}\chi^2
+p\chi\Lambda_\sigma+p^2\Xi_\sigma
+4p\mathfrak f_{s;p}
\right)
\pmod{p^3},
}
\tag{8.1}
$$


together with $p^3\mid U$.

The right side is not an arbitrary target. It is the actual Hermite seed determinant, both actual defect corrections, and the exact mixed forcing return.

In the other chart, $p\nmid R_1$, and the corresponding unresolved cancellation is


$$
\boxed{
\begin{aligned}
&\mathscr I_1(\Theta_s-\Theta_\ell)
+\mathscr I_2(\Theta_{s-1}-\Theta_{\ell-1})\\
&\qquad+\Delta(
\Theta_s\Theta_{\ell-1}-\Theta_{s-1}\Theta_\ell)
\equiv0\pmod{p^3},
\end{aligned}}
\tag{8.2}
$$


again together with $p^3\mid U$.

Neither the unit determinant nor the real-size comparison in Section 6 excludes (8.1) or (8.2).

## 8.1 A concrete follow-on lemma

The new arithmetic chart lemma permits the following precise continuation target.

> **Mixed-forcing continuation lemma — open.**  
> For every original $N$ and every $p\in\mathcal S_N$ with $p^3\mid U$, choose $\zeta_{p,N}$ by (5.10). Prove
> 

$$
> \boxed{\zeta_{p,N}/p^2\not\equiv0\pmod p.}
>
$$


> In the endpoint chart, this means excluding the explicit additive cancellation (8.1). In the residual-source chart, it means excluding (8.2).

This is equivalent to third-depth avoidance after the automatically nonzero $K$-third-digit cases have been removed. It is not an accepted theorem.

A weaker full-depth objective is to bound


$$
\boxed{
\sum_{p\in\mathcal S_N}
\left[
\min\left\{
v_p(16U/p^2),v_p(\zeta_{p,N}/p^2)
\right\}
-(H_p-2)_+
\right]_+\log p
}
\tag{8.3}
$$


by $O(N)$. Unlike the adjugate contact coordinate, (8.3) has no determinant-conditioning discrepancy. It is exactly the surviving mass. No upper bound for it is proved here.

## 8.2 Conditional interval consequence

If the open continuation lemma holds, then $c_p=2$ for every $p\in\mathcal S_N$. The already established payments then give


$$
\prod_{\substack{N<p<2N\\p\nmid L(\ell^2)}}p^{k_p}
\mid
J_N^{\rm aff}\binom{2N}{N}^{\,2},
$$


and hence


$$
\prod_{\substack{N<p<2N\\p\nmid L(\ell^2)}}p^{k_p}
<
10^{10}(2N)^{15}\frac{10000^N}{g_B^2}.
\tag{8.4}
$$


This remains a conditional implication. The new finite invariant does not validate its hypothesis.

---

# 9. Preservation of the complete producer

The new determinant and its auxiliary clearer do not alter the original construction.

## 9.1 Source balance, endpoint balance, and returns

The source balance remains


$$
\begin{aligned}
&(\nu\mathscr A-16\tau\Pi)\Theta_\ell
+(\nu\mathscr B-16\tau\Omega)\Theta_{\ell-1}\\
&\hspace{15mm}=\nu\mathscr C_U-16\tau C^{\rm s}.
\end{aligned}
\tag{9.1}
$$


For


$$
T=\tau(E_F-\delta^2)+\nu E_K,
$$


the complete endpoint is


$$
\begin{aligned}
16T={}&16\tau(C^{\rm e}-\delta^2)+\nu\mathscr C_E\\
&+(\nu\mathscr A-16\tau\Pi)\Phi_\ell
+(\nu\mathscr B-16\tau\Omega)\Phi_{\ell-1}.
\end{aligned}
\tag{9.2}
$$



The source return has


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


Thus


$$
z_{j-1}=z_{j+1}+4jz_j.
$$



After the actual arc clearing below, put


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
w_j=D\Delta\Phi_j+\sigma_j,
$$




$$
\sigma_\ell=\Omega k_E+\mathscr Bf_E,\qquad
\sigma_{\ell-1}=-\Pi k_E-\mathscr Af_E,
$$




$$
\sigma_{j-1}
=\sigma_{j+1}+4j\sigma_j+2D\Delta(-1)^j.
$$


Its retained homogeneous return identity is


$$
z_\ell w_{\ell-1}-z_{\ell-1}w_\ell
=-16\Delta(UX+VY).
\tag{9.3}
$$


No division by $\Delta$ occurs.

Equation (9.3) is old reuse. It is not the new determinant (2.3).

## 9.2 Canonical Hermite returns and their paid product

For exactly $0\le a\le N$,


$$
\mathcal R_{a;N}=d_KP_a^{\mathrm H}U+Q_a^{\mathrm H}y_K.
$$


With


$$
\Psi_j^{(a)}=Q_a^{\mathrm H}\Phi_j-P_a^{\mathrm H}\Theta_j,
$$


the complete forcing is


$$
\Psi_{j+1}^{(a)}+4j\Psi_j^{(a)}-\Psi_{j-1}^{(a)}
=2\bigl(Q_a^{\mathrm H}(-1)^j-P_a^{\mathrm H}\bigr),
$$


and


$$
\begin{aligned}
16\mathcal R_{a;N}
={}&d_K\bigl(
P_a^{\mathrm H}\mathscr C_U+
Q_a^{\mathrm H}\mathscr C_E+
\mathscr A\Psi_\ell^{(a)}+
\mathscr B\Psi_{\ell-1}^{(a)}
\bigr)\\
&-16Q_a^{\mathrm H}a_K.
\end{aligned}
\tag{9.4}
$$



The established signs, heights and determinant-$2$ payment are retained:


$$
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
$$




$$
|\mathcal R_{N-1;N}|,\ |\mathcal R_{N;N}|
<d_K36^NN!,
$$


with the original binary payment


$$
v_2(U)=2,\qquad v_2(y_K)=1,\qquad d_K\ \text{odd}.
$$


The fixed-product divisor remains


$$
\frac{c(r^\circ)^2}{\kappa_N^{\rm prod}}
\mid
\mathcal R_{N-1;N}\mathcal R_{N;N}.
$$


No factorial divisibility of a return is inferred from its factorial-sized upper bound.

The rational recurrence interface remains paid by


$$
Q_{\rm loc}(n)=\prod_{a=0}^{12}(n-a),\qquad
\mathcal L_n=\operatorname{lcm}(1,\ldots,n),
$$


including the nonsingular forcing identity


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}.
$$


Neither clearer replaces the least arc clearer.

## 9.3 Both arcs and their least simultaneous clearer

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
=-4\xi_j-2\upsilon_j-\upsilon_{j-1}
+16(\ell_j-a_j),
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
\tag{9.5}
$$



After reducing both arcs completely, the actual least simultaneous clearer is


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


where the gcd is over **all primes**, and


$$
\boxed{
p_N=A/G,\qquad q_N=\lambda M/G.
}
\tag{9.6}
$$


Since $\gcd(\lambda,A)=1$, this is the actual primitive pair.

Neither $I_{p,N}$, $D_{\rm mix}$, $\Delta$, nor a local chart replaces $D,\lambda,G$, or $q_N$.

---

# 10. The complete nonzero error at the same original indices

The producer is unchanged:


$$
P_N(t)=\frac{F(t)^2+(V/U)K(t)}{\delta^2}
=\frac{W_{\rm prim}(t)}M.
$$


Its whole error is


$$
\boxed{
\epsilon_N=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0.
}
\tag{10.1}
$$



The exact rational relation can be checked directly. The source balance gives


$$
\eta(W_{\rm prim})
=\tau(\delta^2+V)-\nu U=M.
$$


Finite integration by parts gives


$$
\int_0^1e^tW_{\rm prim}(t)\,dt=eM-E.
$$


The two complete arcs give


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
q_N(e+\pi)-p_N=q_N\epsilon_N>0
}
\tag{10.2}
$$


at these same original $N$.

The whole rational enclosure remains


$$
3J_N<\epsilon_N<7J_N,\qquad
J_N=\frac{J_F+(V/U)J_K}{\delta^2},
$$


where


$$
J_F=
\alpha^2\frac{2N^2-1}{4N^2-1}
+\beta^2\frac{2(N-1)^2-1}{4(N-1)^2-1},
$$


and, with $j_a=(1-4a^2)^{-1}$,


$$
J_K=\frac{61}{420}
+\frac{
916j_m-399(j_{m+1}+j_{m-1})
-58(j_{m+2}+j_{m-2})
-(j_{m+3}+j_{m-3})
}{8192}.
$$


Hence


$$
\boxed{
q_NJ_N
=\frac{\lambda_N}{G_N}
  \bigl(\tau_NJ_F+\nu_NJ_K\bigr).
}
\tag{10.3}
$$


Both positive summands are retained.

Even a completed interval estimate would not by itself settle the all-prime content problem. The supplied future strict all-prime saving, if proved, would have its stated consequence of making $q_N\epsilon_N$ grow and retiring this producer. That would not decide the rationality of $e+\pi$.

---

# 11. Scope, computation, and final ledger

## 11.1 What has been proved here

The new results are:

1. **An exact mixed-forcing determinant**
   

$$
\mathfrak D_{j;p}
   =(\Theta_{p+j}-\Theta_j)(\Phi_{p+j-1}+\Phi_{j-1})
    -(\Theta_{p+j-1}-\Theta_{j-1})(\Phi_{p+j}+\Phi_j),
$$


   with its complete Hermite seed, both defect pairs and exact inhomogeneous evolution.

2. **Actual positivity and factorial-scale size bounds** for that determinant, together with the original-object obstruction
   

$$
v_p(\mathfrak D_{s;p})=0,\qquad
   v_p((\ell-2)!(s-2)!)=1.
$$



3. **Two nonzero actual mixed minors** satisfying
   

$$
\mathfrak B_{p,N}
   =R_1E_2-R_2E_1-\Delta\mathfrak D_{s;p},
$$


   and the complete divisor identity
   

$$
\gcd(\mathfrak A_{p,N},\mathfrak B_{p,N})
   =\gcd(16U,V)\,j_{p,N},
   \qquad
   j_{p,N}\mid\Delta\mathfrak D_{s;p}.
$$



4. **A corrected-column arithmetic lemma**
   

$$
\min(v_p(\mathscr A),v_p(\mathscr B))=0
$$


   at every remaining source collision, proved by a fixed degree-three elimination with constant $15\,350\,843$.

5. **Complementary actual source–endpoint charts**
   

$$
\min(v_p(R_1),v_p(E_1))=0,
$$


   yielding the conditioning-free exact contact formula (5.11), including critical determinant primes.

6. **A complete primitive-normalization bill** for the auxiliary rational invariant. Its small real size is not misidentified with small arithmetic height.

These are new proved finite-invariant statements. They are not a quantified solution of the primary depth problem.

## 11.2 What remains open

The exact interval bottleneck is the additive cancellation in (8.1) or (8.2), at the same original indices and after the complete credit $(H_p-2)_+$. Equivalently, the mass in (8.3) is not bounded by $O(N)$.

The determinant’s unit property does not prevent this cancellation. The new scalar norm does not give a fixed-$N$, exponential-height certificate. The actual least simultaneous clearer of the normalized invariant has not been shown to remove the factorial height.

The separate obligations for $p>2N$ and for remaining smaller primes stay open. They have not been expanded or treated as disappearing if this interval is eventually closed.

No density statement, fixed-prime index count, Kurepa nonvanishing claim, product resultant, or multiplicative Fermat-quotient rewrite is used.

## 11.3 Bounded exact arithmetic status

No numerical computation has been performed or proposed at an original enormous index. No source table, matrix solve or prime scan is needed for the proofs above.

The only new constant-size arithmetic identities are already displayed and proved by expansion:


$$
\mathcal Q-19\mathcal F=-20(347x+4908),
$$




$$
\mathcal P+(2x+33)\mathcal F=2(9506x+90215),
$$




$$
347\cdot90215-9506\cdot4908=-15\,350\,843.
$$



If the coordinator requests an independent bounded algebraic receipt, its complete inputs are the three displayed polynomials $\mathcal P,\mathcal Q,\mathcal F$, of degrees at most three, and the two integer products in the last line. The expected verifiable outputs are exactly those three identities. Such a receipt would audit only this fixed elimination; it would not establish an original-family noncollision theorem.

The turn19 optional tiny receipt is not rerun. The older $p23/a3$ receipt is not rerun or extended beyond its recorded auxiliary finite scope.

## Final conclusion

The new contribution is an **actual residual-relative source–endpoint forcing invariant**, with a complete Hermite seed, proved nonzero numerical evaluation, exact mixed-minor divisor identities, and a critical-prime-safe chart for the surviving source contact.

Its measured limitation is now explicit. The raw determinant is factorial-sized and is a unit at the primes whose excess depths must be bounded. The useful contact occurs only in the additive difference


$$
R_1E_2-R_2E_1-\Delta\mathfrak D_{s;p},
$$


or in its complementary source chart. That difference can still cancel modulo $p^3$ and at higher precision. No theorem here bounds the total depth of that cancellation after the full endpoint and Hermite credits.

Accordingly, **the primary interval objective and the global rationality question for $e+\pi$ remain open**.
