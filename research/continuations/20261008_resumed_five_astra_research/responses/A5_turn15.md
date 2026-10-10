> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A fixed signed-return product and its exact joint source-content payment

## Abstract and status

The rationality or irrationality of $e+\pi$ remains unresolved. This report does **not** prove the requested strict intrinsic-content estimate, and it does **not** prove


$$
r_N^\circ\sqrt{c_N}\le N!e^{CN}
$$


uniformly on the original index set.

The new proved statement is a limited **joint-depth capture theorem** for the fixed product of the two established canonical signed returns. It is not a separate height estimate for $c_N$ and $r_N^\circ$.

Write


$$
\gamma_N=\gcd(\tau_N,y_{K,N})=b_N^\circ r_N^\circ,
\qquad
\mathcal Q_N^{\mathrm H}=Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}.
$$


Define the actual positive integer


$$
\boxed{
\kappa_N^{\mathrm{prod}}
=
\frac{c_N}{
\gcd\!\left(
c_N,\,
\mathcal Q_N^{\mathrm H}
\left(y_{K,N}/r_N^\circ\right)^2
\right)}.
}
\tag{0.1}
$$


The division $y_{K,N}/r_N^\circ$ is integral. The new theorem proves


$$
\boxed{
\frac{c_N(r_N^\circ)^2}{\kappa_N^{\mathrm{prod}}}
\ \bigm|\ 
\mathcal R_{N-1;N}\mathcal R_{N;N},
}
\tag{0.2}
$$


with a strictly negative, explicitly bounded integer quotient. Consequently,


$$
\boxed{
r_N^\circ
\sqrt{\frac{c_N}{\kappa_N^{\mathrm{prod}}}}
<
d_{K,N}36^N N!.
}
\tag{0.3}
$$



The source-content depth captured by this theorem is evaluated exactly. At a prime $p$, put


$$
c_p=v_p(c_N),\qquad t_p=v_p(\tau_N),\qquad
z_p=v_p(y_{K,N}),
$$




$$
b_p=v_p(b_N^\circ),\qquad
h_p=v_p(\mathcal Q_N^{\mathrm H}).
$$


Then


$$
\boxed{
v_p(\kappa_N^{\mathrm{prod}})
=
\left[
c_p-h_p-2b_p-2(z_p-t_p)_+
\right]_+.
}
\tag{0.4}
$$


Thus every actual endpoint depth beyond the residual source depth $t_p$ pays **two** remaining source-content depths in this fixed product. This is a joint source/endpoint statement at every prime and depth, including $p>N$.

The limitation is essential: no uniform lower bound for this newly captured source factor is established. In particular, it has not been proved that


$$
\kappa_N^{\mathrm{prod}}\le e^{CN}.
\tag{0.5}
$$


That is a concrete sufficient follow-on lemma. It is weaker than HC because the new payment also uses the actual endpoint surplus, but it is not established merely by introducing the cofactor.

The report therefore advances an exact, quantitatively evaluated joint-depth lemma while leaving the primary uniform saving open.

---

## 1. Original objects and normalization

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


Every such $N$ is odd. The physical polynomial terminal remains $2N$. No auxiliary Hermite index larger than $N$ is used.

### 1.1 Actual divided Gaussian source

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


where


$$
C_0=1,\qquad C_1=2t-1,\qquad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$


Retain


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


Then


$$
F=\alpha C_N-\beta C_{N-1},\qquad
F(i)=F(-i)=\delta,\qquad \gcd(\alpha,\beta)=1.
$$



For an integer polynomial $H$, define


$$
\eta(H)=\int_{-\infty}^{1}e^{t-1}H(t)\,dt,
\qquad
E(H)=\sum_{j=0}^{\deg H}(-1)^jj![t^j]H.
$$


With


$$
\mathcal H(t)=t(1-t)(1+t^2)^2,\qquad
K=\mathcal H C_m^2,
$$


the actual source integers are


$$
U=-\eta(K),\qquad
V=\eta(F^2)-\delta^2,\qquad
c=\gcd(U,V).
$$



The established content identity and primitive normalization remain


$$
h=\operatorname{cont}(W_{\rm raw})=g_B^2c,
$$




$$
\tau=\frac Uc,\qquad \nu=\frac Vc,\qquad
\gcd(\tau,\nu)=1,
$$




$$
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2.
$$


On the original domain,


$$
U>0,\qquad V>0,\qquad M>0.
$$



In particular, every occurrence of $v_p(V)$ below means the valuation of the **divided** source


$$
\eta\!\left((\alpha C_N-\beta C_{N-1})^2\right)-\delta^2.
$$


It is not the valuation of an undivided Gaussian square column.

### 1.2 Both arcs and both least clearers

Retain


$$
E_F=E(F^2),\qquad E_K=E(K),
$$




$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,
\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


After the indicated monic polynomial divisions, the quotient degrees are at most $2N-2$.

Reduce both arcs completely and set


$$
D=\operatorname{lcm}\bigl(\operatorname{den}(R_F),
                         \operatorname{den}(R_K)\bigr),
$$




$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$


Independently reduce the aggregate arc:


$$
\tau R_F+\nu R_K=\frac b\lambda,
\qquad \gcd(b,\lambda)=1,\quad \lambda>0.
$$


Here $b$ is the aggregate numerator; it is unrelated to $b^\circ$.

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
\tag{1.1}
$$


The gcd $G$ is over **all primes**.

The retained exact reconciliations are


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


None of the new auxiliary divisions changes these objects.

### 1.3 The actual reduced $K$-arc

Let


$$
x=\ell^2,\qquad L(x)=(x-1)(x-9)(x-25),
$$




$$
A_K(x)=13x^3-455x^2+3502x-5850.
$$


The retained original-domain reduction is


$$
R_K=\frac{A_K(x)}{30L(x)}=\frac{a_K}{d_K},
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
a_K=\frac{A_K(x)}{g_{\rm arc}},\qquad
d_K=\frac{30L(x)}{g_{\rm arc}}.
$$


Thus


$$
\gcd(a_K,d_K)=1,\qquad
0<a_K<10N^6,\qquad
0<d_K<\frac{64}{3}N^6.
\tag{1.3}
$$



Define


$$
y_K=d_KE_K-a_K,\qquad \mu=D/d_K.
$$


Then


$$
\gcd(d_K,y_K)=1,\qquad Y=\mu y_K.
\tag{1.4}
$$



The intrinsic divisors are


$$
\mathfrak J^0=\gcd(U,Vy_K),\qquad
\mathfrak J=\gcd(U,VY).
$$


The established relations are


$$
\boxed{
\mathfrak J^0=c\gcd(\tau,y_K),\qquad
\mathfrak J^0\mid\mathfrak J\mid\mu\mathfrak J^0,\qquad
U/\mathfrak J\mid q.
}
\tag{1.5}
$$



---

## 2. Established results reused at their exact scope

No closed analytic calculation is repeated here. The spread and SAME-$H$ comparisons retain their original finite matrix boundaries and cutoff $k\ge512$; they are not used as numerical gcd estimates.

### 2.1 Canonical signed returns

Let $P_r^{\mathrm H},Q_r^{\mathrm H}$, $0\le r\le N$, be the paid Hermite endpoint integers


$$
P_0^{\mathrm H}=Q_0^{\mathrm H}=1,\qquad
P_1^{\mathrm H}=3,\quad Q_1^{\mathrm H}=1,
$$




$$
Z_{r+1}=(4r+2)Z_r+Z_{r-1}.
$$


They satisfy


$$
P_{r+1}^{\mathrm H}Q_r^{\mathrm H}
-P_r^{\mathrm H}Q_{r+1}^{\mathrm H}=2(-1)^r,
$$




$$
\gcd(Q_r^{\mathrm H},Q_{r+1}^{\mathrm H})=1.
$$



For fixed original $N$, define


$$
\mathcal R_{r;N}
=d_KP_r^{\mathrm H}U+Q_r^{\mathrm H}y_K.
\tag{2.1}
$$


The established theorem gives


$$
\boxed{
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
\qquad
|\mathcal R_{N-1;N}|,\ |\mathcal R_{N;N}|
<d_K36^N N!.
}
\tag{2.2}
$$


It also gives


$$
\gcd(\mathcal R_{N-1;N},\mathcal R_{N;N})
=\gcd(U,y_K).
\tag{2.3}
$$



The determinant is $2$, not $1$. Its payment in the original objects is retained:


$$
v_2(U)=2,\qquad v_2(y_K)=1,
$$


with $d_K$ odd. No new argument silently treats the Hermite transformation as unimodular.

With


$$
s_r=\gcd(c,Q_r^{\mathrm H}),
$$


the established exact factorization is


$$
\mathfrak J^0
=
c\gcd\left(
\tau,\frac{\mathcal R_{N-1;N}}{s_{N-1}},
     \frac{\mathcal R_{N;N}}{s_N}
\right).
\tag{2.4}
$$



The retained growth bounds are


$$
\log U=2N\log N+O(N),\qquad c\le N!e^{O(N)}.
\tag{2.5}
$$



### 2.2 Turn14 cofactor separation

Write


$$
E_L=E_F-\delta^2,\qquad
T=E-M=\tau E_L+\nu E_K,
$$




$$
\mathcal C=d_KT-\nu a_K
=d_K\tau E_L+\nu y_K.
\tag{2.6}
$$


The original-source identity is


$$
c\mathcal C=d_KUE_L+Vy_K.
\tag{2.7}
$$



The supplied proof establishes, on the full original domain,


$$
\frac34d_K\tau\delta^2<\mathcal C<2d_K\tau\delta^2.
\tag{2.8}
$$


Its positive Gaussian estimate is not repeated.

Put


$$
\gamma=\gcd(\tau,y_K),\qquad
b^\circ=\gcd(\gamma,a_K),\qquad
r^\circ=\gamma/b^\circ.
$$


The retained all-prime separation is


$$
\gcd(\gamma,T)=b^\circ=\gcd(\tau,E_K,a_K),
$$




$$
\mathfrak J^0=c\,b^\circ r^\circ,\qquad b^\circ<10N^6,
\tag{2.9}
$$


and


$$
r^\circ
=\gcd\left(\frac{\tau}{b^\circ},
          \frac{\mathcal C}{b^\circ}\right),
$$




$$
\gcd\left(
r^\circ,\,
d_K\nu(T/b^\circ)(a_K/b^\circ)
\right)=1.
\tag{2.10}
$$



These assertions retain the precise turn14 scope. Their favorable parent review is not described here as a completed different audit.

The surviving depths in (2.10) remain two-unit cancellation depths. The new result below does not reinterpret them as unpaid shared factors of the two affine summands.

---

## 3. New theorem: a fixed-product joint-depth payment

For this section, suppress the subscript $N$ and write


$$
r=r^\circ,\qquad
\mathcal Q^{\mathrm H}=Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}.
$$


Define


$$
\boxed{
f^{\mathrm{prod}}
=
\gcd\left(
c,\,
\mathcal Q^{\mathrm H}(y_K/r)^2
\right),
\qquad
\kappa^{\mathrm{prod}}=\frac{c}{f^{\mathrm{prod}}}.
}
\tag{3.1}
$$



### Theorem 3.1 — Exact source capture by the canonical return product

At every original index:

1. The auxiliary divisions
   

$$
\tau/r,\qquad y_K/r,\qquad
   \mathcal R_{N-1;N}/r,\qquad
   \mathcal R_{N;N}/r
$$


   are integral.

2. The exact source divisor of the normalized return product is
   

$$
\boxed{
   \gcd\left(
   c,\,
   \frac{\mathcal R_{N-1;N}\mathcal R_{N;N}}{r^2}
   \right)
   =f^{\mathrm{prod}}.
   }
   \tag{3.2}
$$



3. The integer
   

$$
\boxed{
   \mathscr Z_N
   =
   \frac{\mathcal R_{N-1;N}\mathcal R_{N;N}}
        {f^{\mathrm{prod}}r^2}
   =
   \frac{\kappa^{\mathrm{prod}}}
        {c r^2}
   \mathcal R_{N-1;N}\mathcal R_{N;N}
   }
   \tag{3.3}
$$


   is strictly negative.

4. The multiplier $\kappa^{\mathrm{prod}}$ is the **least positive integer** $k$ for which
   

$$
\frac{k}{c r^2}
   \mathcal R_{N-1;N}\mathcal R_{N;N}
   \in\mathbb Z.
   \tag{3.4}
$$



5. The quantitative joint bound is
   

$$
\boxed{
   r\sqrt{f^{\mathrm{prod}}}
   <d_K36^N N!,
   }
   \tag{3.5}
$$


   equivalently,
   

$$
\boxed{
   r\sqrt c
   <d_K36^N N!\sqrt{\kappa^{\mathrm{prod}}}.
   }
   \tag{3.6}
$$



#### Proof

Because


$$
r\mid\gamma=\gcd(\tau,y_K),
$$


both


$$
\sigma=\tau/r,\qquad \zeta=y_K/r
$$


are integers. The exact source normalization $U=c\tau$ gives


$$
U/r=c\sigma.
$$


Consequently, for $j=N-1,N$,


$$
\frac{\mathcal R_{j;N}}r
=d_KP_j^{\mathrm H}c\sigma+Q_j^{\mathrm H}\zeta.
\tag{3.7}
$$


This proves every division in assertion 1.

Set


$$
Z_-=\mathcal R_{N-1;N}/r,\qquad
Z_+=\mathcal R_{N;N}/r.
$$


Multiplication of the two actual expressions (3.7) gives the fully evaluated identity


$$
\begin{aligned}
Z_-Z_+
={}&
c^2d_K^2P_{N-1}^{\mathrm H}P_N^{\mathrm H}\sigma^2\\
&+cd_K\sigma\zeta
 \left(
 P_{N-1}^{\mathrm H}Q_N^{\mathrm H}
 +P_N^{\mathrm H}Q_{N-1}^{\mathrm H}
 \right)\\
&+\mathcal Q^{\mathrm H}\zeta^2.
\end{aligned}
\tag{3.8}
$$


Thus


$$
Z_-Z_+\equiv\mathcal Q^{\mathrm H}\zeta^2\pmod c,
$$


and hence


$$
\gcd(c,Z_-Z_+)
=\gcd(c,\mathcal Q^{\mathrm H}\zeta^2)
=f^{\mathrm{prod}}.
$$


This proves (3.2) and the integrality of (3.3).

The established signs in (2.2) apply at these same original indices. Since all divisors in (3.3) are positive,


$$
\mathscr Z_N<0.
$$


In particular, the quotient is not merely a formal integer expression that might vanish.

For the least-multiplier assertion, let


$$
W=Z_-Z_+,\qquad f=\gcd(c,W).
$$


Write


$$
c=fc_1,\qquad W=fW_1,\qquad \gcd(c_1,W_1)=1.
$$


Then


$$
c\mid kW
\iff c_1\mid kW_1
\iff c_1\mid k.
$$


The least positive multiplier is therefore


$$
c_1=c/f=\kappa^{\mathrm{prod}}.
$$


This proves assertion 4, at every prime and depth.

Finally, $|\mathscr Z_N|\ge1$, while the two established return bounds give


$$
\left|\mathcal R_{N-1;N}\mathcal R_{N;N}\right|
<d_K^2 36^{2N}(N!)^2.
$$


Using (3.3),


$$
f^{\mathrm{prod}}r^2
\le
\left|\mathcal R_{N-1;N}\mathcal R_{N;N}\right|
<d_K^2 36^{2N}(N!)^2.
$$


Taking positive square roots proves (3.5) and (3.6). ∎

### 3.1 What is and is not being divided

The theorem does **not** divide an unnormalized linear certificate in the original generators $U,Vy_K$ by an unproved factor.

Instead, it proves the new joint divisibility


$$
f^{\mathrm{prod}}r^2
\mid
\mathcal R_{N-1;N}\mathcal R_{N;N}
$$


directly in a fixed, nonzero product of actual numerical returns.

The source divisor $f^{\mathrm{prod}}$ is established by (3.8), and the factor $r^2$ is established separately by the integral divisions in (3.7). No coefficient-row optimization or unrestricted Bézout choice is involved.

The new content of the theorem is this joint divisibility. The return heights themselves are established reuse.

---

## 4. Exact all-prime evaluation of the newly paid depths

The factor in (3.1) can be evaluated more informatively than as an unnamed gcd.

For a prime $p$, write


$$
u_p=v_p(U),\qquad w_p=v_p(V),\qquad z_p=v_p(y_K),
$$




$$
c_p=\min(u_p,w_p),\qquad t_p=u_p-c_p=v_p(\tau),
$$




$$
g_p=\min(t_p,z_p)=v_p(\gamma),
$$




$$
b_p=\min(g_p,v_p(a_K))=v_p(b^\circ),
\qquad r_p=g_p-b_p=v_p(r^\circ),
$$


and


$$
h_p=v_p(\mathcal Q^{\mathrm H}).
$$



All these are valuations of the actual divided-source and reduced-endpoint integers.

### 4.1 Endpoint surplus after the residual division

Since $r^\circ\mid y_K$,


$$
v_p(y_K/r^\circ)=z_p-r_p.
$$


Using $r_p=g_p-b_p$ and $g_p=\min(t_p,z_p)$,


$$
\begin{aligned}
z_p-r_p
&=z_p-\min(t_p,z_p)+b_p\\
&=(z_p-t_p)_++b_p.
\end{aligned}
\tag{4.1}
$$



Therefore


$$
\boxed{
v_p(f^{\mathrm{prod}})
=
\min\left\{
c_p,\,
h_p+2b_p+2(z_p-t_p)_+
\right\},
}
\tag{4.2}
$$


and


$$
\boxed{
v_p(\kappa^{\mathrm{prod}})
=
\left[
c_p-h_p-2b_p-2(z_p-t_p)_+
\right]_+.
}
\tag{4.3}
$$



This is the claimed all-prime depth formula.

### 4.2 The genuinely joint component

The term


$$
(z_p-t_p)_+
$$


is an actual comparison between the reduced source depth and the endpoint depth.

- If $z_p\le t_p$, there is no endpoint surplus. The new product pays only the Hermite denominator depth and the already separated $b^\circ$-depth.
- If $z_p>t_p$, the endpoint has $z_p-t_p$ additional depths after the full residual source depth has been removed. The fixed product pays **twice** this surplus against the remaining source content.

Thus the new credit is not a bound on the projection of $r^\circ$ onto $T$ or $a_K$. It pays part of the source weight $c$ in the joint quantity $c(r^\circ)^2$.

### 4.3 Exact comparison with the old HC cofactor

For comparison only, put


$$
\rho_{\mathrm H}
=
\frac{c}{\gcd(c,\mathcal Q^{\mathrm H})}.
$$


Then the exact identity


$$
\boxed{
\kappa^{\mathrm{prod}}
=
\frac{\rho_{\mathrm H}}
{\gcd\!\left(\rho_{\mathrm H},(y_K/r^\circ)^2\right)}
}
\tag{4.4}
$$


follows prime by prime from (4.3).

To separate the previously paid polynomial part, define


$$
\rho_b
=
\frac{c}{\gcd(c,\mathcal Q^{\mathrm H}(b^\circ)^2)}.
$$


Since


$$
y_K/r^\circ=b^\circ(y_K/\gamma),
$$


one obtains


$$
\boxed{
\kappa^{\mathrm{prod}}
=
\frac{\rho_b}
{\gcd\!\left(\rho_b,(y_K/\gamma)^2\right)}.
}
\tag{4.5}
$$


The exact new source-depth payment beyond the old Hermite and $b^\circ$ credits is therefore


$$
\boxed{
v_p(\rho_b)-v_p(\kappa^{\mathrm{prod}})
=
\min\left\{
[c_p-h_p-2b_p]_+,\,
2(z_p-t_p)_+
\right\}.
}
\tag{4.6}
$$



This remaining cofactor is pointwise no larger than the HC cofactor. The reduction is strict precisely when the actual endpoint surplus meets some still-unpaid source depth. No assertion is made that such strictness occurs uniformly at the original indices.

### 4.4 All exceptional primes remain accounted for

There is no exceptional-prime omission in (4.2)–(4.6).

**Primes $p>N$.**  
They enter the same formulas. If


$$
h_p=b_p=0,
$$


then


$$
v_p(\kappa^{\mathrm{prod}})
=[c_p-2(z_p-t_p)_+]_+.
$$


This is an actual depth credit, not an $N!$-valuation allowance. The height bound in Theorem 3.1 does not assert factorial divisibility of either return.

**Primes of the Gaussian division.**  
The value $w_p$ is $v_p(V)$ after division by $g_B$ in $\alpha,\beta,\delta$. No Gaussian datum is inverted modulo $p$, and no raw $g_B^2$-depth is counted again as source content.

**Primes dividing $d_K$.**  
Because $\gcd(d_K,y_K)=1$, such primes have $z_p=0$, hence


$$
g_p=r_p=b_p=0.
$$


Their source depth is nevertheless still present:


$$
v_p(\kappa^{\mathrm{prod}})=[c_p-h_p]_+.
$$


They are not discarded merely because they cannot divide the residual endpoint factor.

**The binary determinant payment.**  
The established determinant-$2$ payment remains in force. The new product identity itself makes no division by $2$, $d_K$, $\Delta$, or any Hermite denominator.

---

## 5. Where the actual Gaussian and forced-state coupling enters

The new theorem uses the source factor $c$ through the actual identity


$$
U=c\tau,\qquad V=c\nu,
$$


not through a freely chosen quadratic column. Its prime-depth formula is, explicitly,


$$
\boxed{
\begin{aligned}
v_p(\kappa^{\mathrm{prod}})
=
\Bigl[
&\min\{v_p(U),v_p(V)\}
-v_p(\mathcal Q^{\mathrm H})
-2v_p(b^\circ)\\
&-2\Bigl(
v_p(y_K)
-\max\{v_p(U)-v_p(V),0\}
\Bigr)_+
\Bigr]_+.
\end{aligned}}
\tag{5.1}
$$


Here $U,V,y_K$ are the original evaluations


$$
4096U=\mathsf C_U-\mathsf A\Theta_n-\mathsf B\Theta_{n-1},
$$




$$
V=\mathsf C_V-\mathsf P\Theta_n-\mathsf Q\Theta_{n-1},
$$




$$
4096y_K
=d_K\bigl(
\mathsf C_E+\mathsf A\Phi_n+\mathsf B\Phi_{n-1}
\bigr)-4096a_K.
\tag{5.2}
$$


The changing coefficients in $V$ are


$$
\mathsf P=n\alpha^2+(n-2)\beta^2,
$$




$$
\mathsf Q=4(n-1)(n-2)\beta^2-2(n-1)\alpha\beta,
$$




$$
\mathsf C_V=\alpha^2+(2n-3)\beta^2-\delta^2.
\tag{5.3}
$$



The actual source balance also remains


$$
\begin{aligned}
&(\nu\mathsf A-4096\tau\mathsf P)\Theta_n
+(\nu\mathsf B-4096\tau\mathsf Q)\Theta_{n-1}\\
&\hspace{20mm}
=\nu\mathsf C_U-4096\tau\mathsf C_V,
\end{aligned}
\tag{5.4}
$$


while


$$
\begin{aligned}
4096T={}&
4096\tau(\mathsf C_F^E-\delta^2)+\nu\mathsf C_E\\
&+(\nu\mathsf A-4096\tau\mathsf P)\Phi_n
+(\nu\mathsf B-4096\tau\mathsf Q)\Phi_{n-1}.
\end{aligned}
\tag{5.5}
$$



The theorem does not establish a new distribution law for the depths in (5.1). That is precisely where a further source-specific mechanism is needed. The algebraic capture theorem has wider validity, but its wider validity is not evidence that the actual Gaussian source has sufficiently large endpoint surplus.

In particular, the third affine forcing coordinate in the original states cannot be omitted when trying to prove the next bound.

---

## 6. The smaller unpaid obligation

### 6.1 A concrete sufficient follow-on lemma

The new fixed-product route would prove JUC if the following statement were established.

> **Actual fixed-product payment lemma — open.**  
> There exists a constant $C$, independent of $u$, such that at every original index
> 

$$
> \boxed{
> \kappa_N^{\mathrm{prod}}\le e^{CN}.
> }
> \tag{6.1}
>
$$


> Equivalently, for the actual divided Gaussian source and complete forced endpoint,
> 

$$
> \boxed{
> \sum_p
> \left[
> c_p-h_p-2b_p-2(z_p-t_p)_+
> \right]_+\log p
> \le CN.
> }
> \tag{6.2}
>
$$



Equation (6.2) is the exact remaining unpaid sum for this fixed-product mechanism. It is an **open obligation**, not an evaluated upper bound.

Unlike the old HC sum, it removes the entire source-depth band quantified in (4.6). Unlike a new name for $\gcd(\tau,\mathcal C)$, it is the least multiplier of a different, explicitly evaluated, nonzero numerical product.

### 6.2 Conditional JUC and strict content bounds

If (6.1) holds, Theorem 3.1 and the polynomial bound for $d_K$ give


$$
r_N^\circ\sqrt{c_N}
\le N!e^{O(N)}.
$$


Thus (6.1) implies JUC.

More generally, the new unconditional inequality yields


$$
\begin{aligned}
\mathfrak J^0
&=c\,b^\circ r^\circ\\
&<b^\circ d_K36^N N!\sqrt c\,
          \sqrt{\kappa^{\mathrm{prod}}}.
\end{aligned}
$$


Using the established bound $c\le N!e^{O(N)}$,


$$
\boxed{
\log\mathfrak J^0
\le
\frac32N\log N
+\frac12\log\kappa^{\mathrm{prod}}
+O(N).
}
\tag{6.3}
$$



Consequently, even the weaker new source statement


$$
\kappa_N^{\mathrm{prod}}
\le (N!)^{1-\eta}e^{CN},
\qquad \eta>0,
\tag{6.4}
$$


would give the strict estimate


$$
\boxed{
\log\mathfrak J_N^0
\le
\left(2-\frac{\eta}{2}\right)N\log N+O(N).
}
\tag{6.5}
$$



No positive $\eta$ in (6.4) is proved here.

### 6.3 Precise obstruction to completing the argument

The unhandled configurations are explicit.

If, at an actual prime,


$$
z_p\le t_p,\qquad h_p=b_p=0,
$$


then


$$
v_p(\kappa^{\mathrm{prod}})=c_p.
\tag{6.6}
$$


The fixed product captures none of that source depth. This remains true even when $r_p>0$ and the turn14 affine cancellation is a cancellation between two units.

More generally, the unpaid depth is exactly the portion of $c_p$ exceeding


$$
h_p+2b_p+2(z_p-t_p)_+.
$$


Neither the size of $y_K/r^\circ$ nor the size of $c$ forces a large gcd between them.

The positive turn14 comparison


$$
\frac{\mathcal C}{\gamma}
\asymp d_K\delta^2\,\frac{U}{\mathfrak J^0}
$$


does not repair this deficiency. Using its integrality to force a factorial lower bound for $U/\mathfrak J^0$ would still be circular.

Likewise, the exact nonzero integer $\mathscr Z_N$ in (3.3) supplies only


$$
|\mathscr Z_N|\ge1.
$$


It does not by itself make $\kappa_N^{\mathrm{prod}}$ small.

Thus a next proof must quantitatively control the actual depths in (6.2), using the changing Gaussian data and the two forced boundary states. A coefficient-content theorem, adjacent Hermite coprimality, or an unrestricted certificate optimization does not provide that control.

HC and TDC remain open. Neither the old unit-collision obstruction nor the present fixed-product limitation disproves either condition.

---

## 7. Actual primitive denominator and complete positive whole error

The original positive polynomial is unchanged:


$$
P_N(t)
=
\frac{F(t)^2+(V/U)K(t)}{\delta^2}.
$$


Its whole error is


$$
\boxed{
\epsilon_N
=
\int_0^1P_N(t)
\left(e^t+\frac4{1+t^2}\right)\,dt>0,
}
\tag{7.1}
$$


and


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0,
\qquad
q_N=\frac{\lambda_NM_N}{G_N}.
}
\tag{7.2}
$$



No exponential-only or mixed-error quantity replaces (7.1).

The complete rational enclosure is retained:


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


Therefore


$$
\boxed{
q_NJ_N
=
\frac{\lambda_N}{G_N}
\bigl(\tau_NJ_F+\nu_NJ_K\bigr).
}
\tag{7.3}
$$


Both original positive summands are retained.

If the open bound (6.4) held, then (1.5), $\mu<256^N$, and (6.5) would give


$$
\log q_N
\ge
\frac{\eta}{2}N\log N-O(N).
$$


Using the established whole-error estimate


$$
\epsilon_N\asymp R^{-2N},
\qquad
R=1+\sqrt2+\sqrt{2+2\sqrt2},
$$


one would obtain


$$
\boxed{
\log(q_N\epsilon_N)
\ge
\frac{\eta}{2}N\log N-O(N)\longrightarrow+\infty
}
\tag{7.4}
$$


along the same original indices.

For (6.1), one may take the resulting strict-content exponent corresponding to $\eta=1$, obtaining


$$
\log(q_N\epsilon_N)\ge\frac12N\log N-O(N).
$$



This would retire this producer only. It would not prove that $e+\pi$ is rational or irrational.

---

## 8. Retained finite columns, boundaries, forcing, and returns

The new product uses the original numerical returns. For self-contained identification of those numbers, the complete finite data are recorded here without repeating their closed derivations.

### 8.1 Original forced states

For $0\le j\le n$,


$$
\eta(C_j)=1-2j\Theta_j,\qquad
E(C_j)=(-1)^j-2j\Phi_j,
$$


with


$$
\Theta_0=\Phi_0=0,\qquad \Theta_1=\Phi_1=1,
$$


and, for $1\le j\le n-1$,


$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
\tag{8.1}
$$



The full affine states are


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
\begin{pmatrix}\Phi_j\\\Phi_{j-1}\\(-1)^j\end{pmatrix},
\tag{8.2}
$$


with initial vectors


$$
(1,0,1)^t,\qquad (1,0,-1)^t.
$$


Neither third coordinate is removed.

### 8.2 All thirteen weights and complete columns

Retain


$$
(w_0,\ldots,w_{12})
=(1,8,58,168,399,-176,-916,-176,399,168,58,8,1).
$$


For exactly $1\le k\le11$,


$$
r_{k+1}=r_{k-1}+4(n-k)r_k,
\qquad
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
(r_0,s_0^*)=(1,0),\qquad(r_1,s_1^*)=(0,1),
$$




$$
\kappa_0=\kappa_1=\omega_0=\omega_1=0.
$$


Set


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


Then


$$
4096U=\mathsf C_U-\mathsf A\Theta_n-\mathsf B\Theta_{n-1},
$$




$$
4096E_K=\mathsf C_E+\mathsf A\Phi_n+\mathsf B\Phi_{n-1}.
\tag{8.3}
$$



For the divided square,


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
\mathsf C_F^E=\alpha^2+(5-2n)\beta^2+4\alpha\beta,
$$


and


$$
V=\mathsf C_V-\mathsf P\Theta_n-\mathsf Q\Theta_{n-1},
$$




$$
E_F=\mathsf C_F^E-\mathsf P\Phi_n-\mathsf Q\Phi_{n-1}.
\tag{8.4}
$$


Both $-\delta^2$ and $4\alpha\beta$ are present.

The factors $4096$ in (8.3) are paid by the exact integer polynomial identities. They are not inverted modulo $2$ in any valuation argument.

### 8.3 Centered columns

At $x=\ell^2$, retain


$$
\begin{aligned}
\mathcal P(x)&=-8x^3-1116x^2-8150x+151,\\
\mathcal Q(x)&=76x^2+2408x+5637,\\
\mathcal F(x)&=4x^2+492x+5463,\\
\mathcal G(x)&=4x^2+556x-3325.
\end{aligned}
$$


Define


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


The complete centered identities are


$$
16U=\widetilde{\mathsf C}_U
-\widetilde{\mathsf A}\Theta_\ell
-\widetilde{\mathsf B}\Theta_{\ell-1},
$$




$$
16E_K=\widetilde{\mathsf C}_E
+\widetilde{\mathsf A}\Phi_\ell
+\widetilde{\mathsf B}\Phi_{\ell-1}.
\tag{8.5}
$$


These are retained identities, not numerical gcd bounds.

### 8.4 Rational interface and its payments

For $j\ge1$,


$$
S_j=\eta(C_j),\qquad s_j=S_j/j=\frac1j-2\Theta_j.
$$


On the nonsingular range $2\le j\le n-1$,


$$
s_{j-1}=s_{j+1}+4js_j+\frac2{j^2-1},
$$


with


$$
S_0=1,\qquad s_1=-1,\qquad s_2=\frac92.
\tag{8.6}
$$


The local affine constants are


$$
s_{n-k}=r_ks_n+s_k^*s_{n-1}+e_k,
$$




$$
e_k=\frac1{n-k}-\frac{r_k}{n}
-\frac{s_k^*}{n-1}-2\kappa_k.
\tag{8.7}
$$


They are paid by


$$
Q_{\rm loc}(n)=\prod_{r=0}^{12}(n-r).
$$


Globally, $\mathcal L_n=\operatorname{lcm}(1,\ldots,n)$ pays the forcing through


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}.
$$


Neither clearer replaces the least simultaneous arc clearer $D$.

The complete affine constants remain


$$
\mathsf E
=2\mathsf C_U-\frac{\mathsf A}{n}-\frac{\mathsf B}{n-1},
$$




$$
2\mathsf C_V
=\frac{\mathsf P}{n}+\frac{\mathsf Q}{n-1}+\mathsf T,
\qquad
\mathsf T=(\alpha+\beta)^2-2\delta^2+\frac{2\beta^2}{n}.
\tag{8.8}
$$



### 8.5 Source and endpoint returns

Let


$$
\Delta=\mathsf A\mathsf Q-\mathsf B\mathsf P.
$$


The source return is


$$
z_n=4096\mathsf Q U-\mathsf B V,\qquad
z_{n-1}=\mathsf A V-4096\mathsf P U,
$$




$$
z_j=-\Delta\Theta_j+\varrho_j,
$$




$$
z_{j-1}=z_{j+1}+4jz_j,
\qquad
\varrho_{j-1}=\varrho_{j+1}+4j\varrho_j-2\Delta,
$$


with


$$
\varrho_n=\mathsf Q\mathsf C_U-\mathsf B\mathsf C_V,
\qquad
\varrho_{n-1}=\mathsf A\mathsf C_V-\mathsf P\mathsf C_U.
$$


In the rational interface,


$$
2z_j=\Delta s_j+\rho_j,\qquad
\rho_j=2\varrho_j-\Delta/j,
$$




$$
\rho_{j-1}
=\rho_{j+1}+4j\rho_j-\frac{2\Delta}{j^2-1}.
\tag{8.9}
$$



The complete endpoint return retains


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
w_{j-1}=w_{j+1}+4jw_j,
\qquad
\sigma_{j-1}=\sigma_{j+1}+4j\sigma_j+2D\Delta(-1)^j.
$$


Its determinant remains


$$
z_nw_{n-1}-z_{n-1}w_n
=-4096\Delta(UX+VY).
\tag{8.10}
$$


There is no division by $\Delta$.

### 8.6 Complete square-arc return

With zero initial values at $j=0,1$,


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
0,&j\text{ odd},\\
(1-j^2)^{-1},&j\text{ even}.
\end{cases}
$$


The actual square arc is


$$
R_F=
\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
-2\alpha\beta\xi_{n-1}}2.
\tag{8.11}
$$



### 8.7 Canonical return in the same forced states

For each $0\le r\le N$, put


$$
\Psi_j^{(r)}
=Q_r^{\mathrm H}\Phi_j-P_r^{\mathrm H}\Theta_j.
$$


Then


$$
\Psi_0^{(r)}=0,\qquad
\Psi_1^{(r)}=Q_r^{\mathrm H}-P_r^{\mathrm H},
$$




$$
\Psi_{j+1}^{(r)}+4j\Psi_j^{(r)}-\Psi_{j-1}^{(r)}
=
2\bigl(Q_r^{\mathrm H}(-1)^j-P_r^{\mathrm H}\bigr),
$$


and


$$
\begin{aligned}
4096\mathcal R_{r;N}
={}&d_K\bigl(
P_r^{\mathrm H}\mathsf C_U
+Q_r^{\mathrm H}\mathsf C_E
+\mathsf A\Psi_n^{(r)}
+\mathsf B\Psi_{n-1}^{(r)}
\bigr)\\
&-4096Q_r^{\mathrm H}a_K.
\end{aligned}
\tag{8.12}
$$


Thus the two returns in the new product retain both seeds, both forcings, both constants, and the complete reduced arc term.

---

## 9. Proof-status ledger

| Statement | Status and exact scope |
|---|---|
| Original domain, terminal $2N$, complete columns and forcing | Retained unchanged |
| Actual $g_B$-division, $h=g_B^2c$, primitive $\tau,\nu$ | Established reuse |
| Both reduced arcs, least $D$, least $\lambda$, final all-prime $G$, actual $q$ | Retained unchanged |
| Canonical return signs, nonvanishing, height bounds, and gcd theorem | Established audited reuse at the original indices |
| Turn14 polynomial cofactor and two-unit collision description | Reused at its stated proved scope; different audit not claimed complete |
| Fixed-product identity (3.8) | **New proved identity** |
| Exact source divisor and least product multiplier (3.2)–(3.4) | **New proved all-prime statement** |
| Joint inequality $r^\circ\sqrt{c/\kappa^{\rm prod}}<d_K36^NN!$ | **New proved numerical bound** |
| Double endpoint-surplus credit (4.2)–(4.6) | **New proved all-prime joint-depth formula** |
| Uniformly significant capture of $c$ by the new factor | **Not proved** |
| $\kappa_N^{\rm prod}\le e^{CN}$, or a strict fractional-factorial bound | **Open** |
| JUC and strict intrinsic-content saving | **Open** |
| HC and TDC | **Open; neither proved nor disproved** |
| Retirement of this producer | Conditional on a strict saving such as (6.4) |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

No new external gcd theorem is imported. In particular, no fixed-$S$ theorem is applied to these factorial evaluations without matching hypotheses.

---

## 10. Bounded arithmetic and final conclusion

### 10.1 Computation status

No numerical computation was performed.

No new bounded computation is mathematically indispensable for Theorem 3.1. Its new algebra is the displayed quadratic identity (3.8), followed by an exact gcd and least-multiplier argument. Its nonvanishing and numerical height use the already established canonical return theorem at its stated scope.

Accordingly, no small-prime scan, old source array, recurrence run, numerical example, or calculation at an enormous original index is requested.

A finite computation of $\kappa_N^{\mathrm{prod}}$ at finitely many original indices would establish only those finite values. It would not prove (6.1), JUC, or the strict intrinsic-content estimate.

### 10.2 New result

The new proved joint-content statement is


$$
\boxed{
\gcd\left(
c_N,\,
\frac{\mathcal R_{N-1;N}\mathcal R_{N;N}}
     {(r_N^\circ)^2}
\right)
=
\gcd\left(
c_N,\,
Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}
\left(\frac{y_{K,N}}{r_N^\circ}\right)^2
\right).
}
$$


Its nonzero numerical evaluation proves


$$
\boxed{
r_N^\circ
\sqrt{\frac{c_N}{\kappa_N^{\mathrm{prod}}}}
<
d_{K,N}36^N N!.
}
$$



The new payment is exact: after the Hermite and polynomial-overlap credits, each endpoint-surplus depth pays two source-content depths in the fixed return product.

### 10.3 Exact remaining bottleneck

The unpaid logarithmic mass for this mechanism is


$$
\boxed{
\sum_p
\left[
v_p(c_N)
-v_p(Q_{N-1}^{\mathrm H}Q_N^{\mathrm H})
-2v_p(b_N^\circ)
-2\bigl(v_p(y_{K,N})-v_p(\tau_N)\bigr)_+
\right]_+\log p.
}
$$


It includes every prime and depth.

A proof that this mass is $O(N)$ would establish JUC. A fixed positive saving from its current possible $N\log N+O(N)$ scale would already give a strict intrinsic-content estimate through (6.3).

**This turn proves a limited joint-depth capture theorem, not a uniform source-specific saving. The remaining task is to quantitatively control the displayed unpaid mass in the actual changing Gaussian source and complete forced endpoint states. The primary intrinsic-content gate, retirement of this producer, and the rationality or irrationality of $e+\pi$ remain open.**
