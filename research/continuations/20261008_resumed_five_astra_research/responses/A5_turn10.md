> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A centered integer elimination for the complete $K$-column  
## New coefficient-content theorem; the paid factorial-excess bound remains open

### Abstract and proof status

The original index set is retained:


$$
\mathcal N=\{N_u=9^{18+32u}:u\in\mathbb Z_{\ge0}\}.
$$


All producer statements below concern these same indices. Internal coordinates are changed, but neither the producer nor its physical terminal $2N$ is changed.

The primary obligation


$$
\prod_{p\notin\{2,3,5,17\}}
p^{\max\{0,\,
\min(v_p(U_N),v_p(V_N)+v_p(y_{K,N}))-v_p(N!)\}}
\le e^{CN}
\tag{FE}
$$


is **not proved or disproved** here. In particular, no bound for its unpaid large-prime product is obtained.

There is, however, a new evaluated integer elimination. It uses the complete polynomial


$$
\mathcal H(t)=t(1-t)(1+t^2)^2,
$$


both original exponential boundaries, and all the constant terms. It reduces the complete $K$-column to coefficient polynomials of degree at most three in


$$
x=4(N-3)^2.
$$


An explicit integer Bézout identity for those polynomials then proves the following exact theorem for the original thirteen-weight source row:


$$
\boxed{
\gcd\bigl(\mathsf A(2N),\mathsf B(2N),\mathsf C_U(2N)\bigr)
=
2^{11}\gcd(83,2N-6).
}
\tag{A}
$$


Equivalently,


$$
\boxed{
\gcd\bigl(4096U_N,\mathsf A(2N),\mathsf B(2N)\bigr)
=
2^{11}\gcd(83,2N-6).
}
\tag{B}
$$



This is an **ALL-prime, all-depth numerical gcd statement about the actual complete source row**. It is not a replacement of a numerical gcd by a polynomial gcd.

It removes simultaneous $K$-row collapse as an unpaid issue: if an odd prime $p\mid U_N$, then the two original boundary-lift slopes can both vanish only when


$$
p=83,\qquad 83\mid 2N-6,
$$


and even that row-content exponent is exactly one. In particular, every prime $p>N$ dividing $U_N$ has a noncollapsed $K$-row.

That conclusion still does **not** exclude affine cancellation against $V_N$ or $y_{K,N}$. The already proved original prime-$5$ exception is precisely a warning against that inference. The remaining issue is synchronization of the actual boundary values and actual paid Gaussian coefficients, not degeneration of the complete $K$-coefficient row.

No tools were used. A new bounded polynomial-arithmetic receipt, with explicit expected outputs, is specified in Section 8.

---

## 1. Retained producer, complete normalization, and proof scope

### 1.1 The original integer objects

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


where


$$
C_0=1,\qquad C_1=2t-1,\qquad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$



The source functional is


$$
\eta(H)=\int_{-\infty}^{1}e^{t-1}H(t)\,dt
       =\sum_{r\ge0}[z^r]H(1-z)\,r!.
\tag{1.1}
$$


The factorial weights after $z=1-t$ are positive.

Retain


$$
d=a_Nb_{N-1}-a_{N-1}b_N,\qquad
B=b_{N-1}C_N-b_NC_{N-1},
$$


and make the actual paid division


$$
g_B=\gcd(b_{N-1},b_N)>0,\qquad
\alpha=\frac{b_{N-1}}{g_B},\quad
\beta=\frac{b_N}{g_B},\quad
\delta=\frac d{g_B}.
$$


Thus


$$
F=\alpha C_N-\beta C_{N-1},\qquad
F(i)=F(-i)=\delta,\qquad \gcd(\alpha,\beta)=1.
$$



Put


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad
K=\mathcal H C_{N-3}^2,
$$




$$
U=-\eta(K),\qquad V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$


The proved content formula is


$$
h=\operatorname{cont}(W_{\rm raw})=g_B^2c,
$$


where


$$
W_{\rm raw}=UB^2+\bigl(\eta(B^2)-d^2\bigr)K.
$$


Consequently,


$$
\tau=\frac Uc,\qquad \nu=\frac Vc,\qquad
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2.
\tag{1.2}
$$



The positivity and nonvanishing proofs in the supplied audit apply for $N\ge256$, hence at every original index. In particular,


$$
U>0,\qquad V>0,\qquad M>0.
$$



The content proof is genuinely ALL-prime: $F(0)$ and $F(1)$ are coprime, while $K$ is primitive. It does not use an unpaid raw square column in place of $V$.

### 1.2 Complete endpoints, both arcs, and both least clearers

For $H\in\mathbb Z[t]$, let


$$
E(H)=\sum_{r=0}^{\deg H}(-1)^rr![t^r]H.
$$


Retain


$$
E_F=E(F^2),\qquad E_K=E(K),
$$




$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$



The least simultaneous column clearer is


$$
D=\operatorname{lcm}\bigl(\operatorname{den}(R_F),
                         \operatorname{den}(R_K)\bigr),
$$


with both fractions first reduced completely. Define


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
\tag{1.3}
$$



Independently, reduce the single aggregate arc:


$$
\tau R_F+\nu R_K=\frac b\lambda,\qquad
\gcd(b,\lambda)=1,\quad\lambda>0.
$$


Then


$$
E=\tau E_F+\nu E_K,\qquad A=\lambda E-b,\qquad G=\gcd(M,A),
$$


and the actual primitive pair is


$$
\boxed{
q=\frac{\lambda M}{G},\qquad p=\frac A G.
}
\tag{1.4}
$$


Here $G$ is the final gcd over **all primes**.

The exact reconciliation is


$$
\tau X+\nu Y=\frac D\lambda A,
$$




$$
\gcd(D\tau\delta^2,\tau X+\nu Y)=\frac D\lambda G.
\tag{1.5}
$$


The raw-interface identity remains


$$
\gcd(A_{\rm raw},B_{\rm raw})
=\frac{L_{\rm aff}h}{\lambda}G,\qquad
L_{\rm aff}=\operatorname{lcm}(1,\ldots,2N-1).
$$



The physical polynomial terminal is $2N$. Both monic arc quotients have degree at most $2N-2$, so


$$
D\mid L_{\rm aff},\qquad D<256^N.
\tag{1.6}
$$



### 1.3 The actual reduced $K$-arc

With


$$
x=4(N-3)^2,
$$


reuse the complete evaluated fraction


$$
R_K=\frac{A_K(x)}{30L(x)},
$$


where


$$
L(x)=(x-1)(x-9)(x-25),
$$




$$
A_K(x)=13x^3-455x^2+3502x-5850.
\tag{1.7}
$$


Its actual reduction is


$$
g_{\rm arc}=\gcd(A_K(x),30L(x)),\qquad
a_K=\frac{A_K(x)}{g_{\rm arc}},\qquad
d_K=\frac{30L(x)}{g_{\rm arc}}.
$$


The proved cancellation cap


$$
g_{\rm arc}\mid31\,806\,000
\tag{1.8}
$$


is retained without recomputation.

Set


$$
y_K=d_KE_K-a_K,\qquad \mu=\frac D{d_K}.
$$


Then


$$
Y=\mu y_K.
$$


For


$$
\mathfrak J^0=\gcd(U,Vy_K),\qquad
\mathfrak J=\gcd(U,VY),
$$


the exact comparisons are


$$
\mathfrak J^0\mid\mathfrak J\mid\mu\mathfrak J^0,
\qquad
\boxed{\frac U{\mathfrak J}\mid q.}
\tag{1.9}
$$


These include primes dividing $D,\delta,g_B,\Delta$, or $g_{\rm arc}$.

### 1.4 The same positive whole error

The rational polynomial remains


$$
P_N(t)=\frac{F(t)^2+(V/U)K(t)}{\delta^2}.
$$


At every original index,


$$
\epsilon_N=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0,
$$


and


$$
\boxed{q_N(e+\pi)-p_N=q_N\epsilon_N>0.}
\tag{1.10}
$$



The audited estimates give


$$
\epsilon_N\asymp R^{-2N},\qquad
R=1+\sqrt2+\sqrt{2+2\sqrt2},
$$




$$
\log U_N=2N\log N+O(N),\qquad
\log c_N\le N\log N+O(N).
\tag{1.11}
$$


The closed critical Bessel/midpoint calculation is not repeated.

The complete rational error enclosure is also retained. With


$$
m=N-3,\qquad j_r=(1-4r^2)^{-1}=j_{-r},
$$


put


$$
J_F=
\alpha^2\frac{2N^2-1}{4N^2-1}
+\beta^2\frac{2(N-1)^2-1}{4(N-1)^2-1},
$$




$$
J_K=\frac{61}{420}
+\frac{
916j_m-399(j_{m+1}+j_{m-1})
-58(j_{m+2}+j_{m-2})
-(j_{m+3}+j_{m-3})
}{8192},
$$




$$
J_N=\frac{J_F+(V/U)J_K}{\delta^2}.
$$


Then


$$
3J_N<\epsilon_N<7J_N,\qquad
q_NJ_N=\frac{\lambda_N}{G_N}
       (\tau_NJ_F+\nu_NJ_K).
\tag{1.12}
$$


Neither positive summand has been discarded.

---

## 2. Original forced columns and retained arithmetic evidence

### 2.1 Both original boundaries and the thirteen weights

Write $n=2N$. The integral coordinates are


$$
\eta(C_j)=1-2j\Theta_j,\qquad
E(C_j)=(-1)^j-2j\Phi_j,
$$


where


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



Keep the complete weight vector


$$
(w_0,\ldots,w_{12})
=(1,8,58,168,399,-176,-916,-176,399,168,58,8,1).
$$


The fixed local evaluator is


$$
r_0=1,\ s_0=0,\qquad r_1=0,\ s_1=1,
$$




$$
r_{k+1}=r_{k-1}+4(n-k)r_k,\qquad
s_{k+1}=s_{k-1}+4(n-k)s_k,
$$


and


$$
\kappa_0=\kappa_1=\omega_0=\omega_1=0,
$$




$$
\kappa_{k+1}=\kappa_{k-1}+4(n-k)\kappa_k-2,
$$




$$
\omega_{k+1}=\omega_{k-1}+4(n-k)\omega_k-2(-1)^k,
\qquad 1\le k\le11.
\tag{2.2}
$$


Thus


$$
\mathsf A=\sum_{k=0}^{12}w_k(n-k)r_k,\qquad
\mathsf B=\sum_{k=0}^{12}w_k(n-k)s_k,
$$




$$
\mathsf C_U=679936-\sum_{k=0}^{12}w_k(n-k)\kappa_k,
$$




$$
\mathsf C_E=-1\,849\,344+
\sum_{k=0}^{12}w_k(n-k)\omega_k.
$$


The complete $K$-columns are


$$
4096U=\mathsf C_U-\mathsf A\Theta_n-\mathsf B\Theta_{n-1},
$$




$$
4096E_K=\mathsf A\Phi_n+\mathsf B\Phi_{n-1}+\mathsf C_E.
\tag{2.3}
$$



For the actual paid square column, retain


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


so that


$$
V=\mathsf C_V-\mathsf P\Theta_n-\mathsf Q\Theta_{n-1},
$$




$$
E_F=\mathsf C_F^E-\mathsf P\Phi_n-\mathsf Q\Phi_{n-1}.
\tag{2.4}
$$


No Gaussian coefficient is frozen in an index lift.

### 2.2 Complete arc and integer returns

The square arc is still obtained from


$$
R_j(t)=\frac{C_j(t)-a_j-b_jt}{1+t^2},\qquad
\xi_j=4\int_0^1R_j,\qquad
\upsilon_j=4\int_0^1tR_j,
$$


with zero initial values at $j=0,1$, and


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
(1-j^2)^{-1},&j\text{ even}.
\end{cases}
$$


Then


$$
R_F=\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
                  -2\alpha\beta\xi_{n-1}}2.
\tag{2.5}
$$



Let


$$
\Delta=\mathsf A\mathsf Q-\mathsf B\mathsf P<0.
$$


The source return remains


$$
z_n=4096\mathsf Q U-\mathsf B V,\qquad
z_{n-1}=\mathsf A V-4096\mathsf P U,
$$




$$
z_j=-\Delta\Theta_j+r_j,
$$




$$
z_{j-1}=z_{j+1}+4jz_j,\qquad
r_{j-1}=r_{j+1}+4jr_j-2\Delta.
\tag{2.6}
$$


Its terminal constants are


$$
r_n=\mathsf Q\mathsf C_U-\mathsf B\mathsf C_V,\qquad
r_{n-1}=\mathsf A\mathsf C_V-\mathsf P\mathsf C_U.
$$



For the complete endpoint pair,


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
\tag{2.7}
$$


These are integer identities, including at $p\mid2\Delta$.

Their determinant is


$$
z_nw_{n-1}-z_{n-1}w_n
=-4096\Delta(UX+VY).
\tag{2.8}
$$


It is not a small-height certificate for $\mathfrak J^0$. The complete numerator on the right cannot be silently substituted for the desired factorial-paid remainder.

### 2.3 Reuse of the prime-$5$, prime-$17$, and boundary-lift results

The supplied boundary formula


$$
T_j(c)=\sum_{r=0}^{j-1}c^rr!\binom{j+r}{2r+1},
\qquad
T_0=0,\quad T_1=1,
$$


does satisfy


$$
T_{j+1}=cjT_j+T_{j-1}+2.
$$


Thus its application to the original boundaries $c=\pm4$ is correctly scoped.

The dual-slope evaluation


$$
H_a^-H_{a-1}^+ +H_{a-1}^-H_a^+\equiv-2\pmod p
\tag{2.9}
$$


uses the original forcing and Wilson’s theorem; it is not a statement about arbitrary initial states. The higher-lift proof for $p\ge5$ correctly pays the tail using


$$
v_p(r!)\ge\lfloor\log_p(2r+1)\rfloor\qquad(r\ge p).
$$


It does not authorize higher-depth freezing of $\alpha,\beta,\delta$.

The original prime-$5$ conclusion is reused:


$$
v_5(\mathfrak J^0_{N_u})
=\mathbf1_{u\equiv21\pmod{25}}.
\tag{2.10}
$$


The source proof pays the relevant division in the cubic source jet, retains the reduced arc, and obtains $U\equiv10\pmod{25}$ on the exceptional branch. There


$$
5\nmid2g_B\Delta d_K,\qquad 5\nmid V.
$$


This is a genuine affine cancellation exception despite unit determinant data.

The prime-$17$ theorem and the supplied closed receipt are likewise reused:


$$
17\nmid\mathfrak J^0,
$$




$$
v_{17}(\mathfrak J)
=\min\{v_{17}(U),v_{17}(D)-v_{17}(2N-9)\}.
\tag{2.11}
$$


The receipt checks its bounded arithmetic. Uniformity in the original indices comes from the stated recurrence returns and exponent congruence, not from finite extrapolation.

Together with the established binary and ternary conclusions,


$$
v_2(\mathfrak J^0)=2,\qquad 3\nmid\mathfrak J^0,
$$


these give


$$
\mathfrak J^0
=4\cdot5^{\mathbf1_{u\equiv21\ (25)}}\,
\mathfrak J_{\rm rem},
\qquad
\gcd(\mathfrak J_{\rm rem},2\cdot3\cdot5\cdot17)=1.
\tag{2.12}
$$


No new finite-prime table is introduced.

---

## 3. New complete $K$-column reduction

The useful new coordinate is


$$
\ell=2N-6=2(N-3),\qquad x=\ell^2.
$$


It lies inside the original finite range. The degree of
$\mathcal H C_\ell$ is still $\ell+6=2N$.

Because


$$
C_{N-3}^2=\frac{1+C_\ell}{2},
$$


we have


$$
U=166-\frac12\eta(\mathcal H C_\ell),
\qquad
E_K=-\frac{903}{2}+\frac12E(\mathcal H C_\ell).
\tag{3.1}
$$


Here the complete constants


$$
\eta(\mathcal H)=-332,\qquad E(\mathcal H)=-903
$$


are essential.

### 3.1 A moment recurrence using both actual boundaries

For $b\in\{0,1\}$, define


$$
\mathcal L_b(H)=\int_{-\infty}^{b}e^{t-b}H(t)\,dt,
\qquad
M_k^{(b)}=\mathcal L_b(t^kC_\ell).
$$


Thus $\mathcal L_1=\eta$ and $\mathcal L_0=E$.

Since $\ell$ is even,


$$
C_\ell(0)=C_\ell(1)=1.
$$


The shifted Chebyshev differential equation is


$$
t(1-t)C_\ell''+\left(\frac12-t\right)C_\ell'+xC_\ell=0.
\tag{3.2}
$$



For any polynomial $H$,


$$
\mathcal L_b(H')=H(b)-\mathcal L_b(H).
$$


Applying this twice to (3.2), after multiplication by $t^k$, gives


$$
\boxed{
M_{k+2}^{(b)}
=-2(k+1)M_{k+1}^{(b)}
+\left(x+\frac12-k^2\right)M_k^{(b)}
+k\left(k+\frac12\right)M_{k-1}^{(b)}
+\left(b-\frac12\right)b^k.
}
\tag{3.3}
$$


At $k=0$, the term involving $M_{-1}$ is absent and the final term is $b-\tfrac12$.

For clarity, the boundary contribution before simplification is


$$
-\left(k+\frac12\right)b^k+kb^{k+1}+b^{k+2}
=\left(b-\frac12\right)b^k
$$


for $b=0,1$. Thus neither boundary forcing has been suppressed.

### 3.2 Evaluating the six moments

Put


$$
r=x+\frac12,\qquad s=b-\frac12.
$$


Write


$$
M_j^{(b)}=p_jM_0^{(b)}+q_jM_1^{(b)}+f_j^{(b)}.
$$


Starting from $p_0=1,q_0=0,p_1=0,q_1=1$, recurrence (3.3) gives:



$$
\begin{array}{c|l|l|l}
j&p_j&q_j&f_j^{(b)}/s\\ \hline
2&r&-2&1\\
3&-4r+\frac32&r+7&b-4\\
4&r^2+20r-9&-8r-29&r+20-5b\\
5&-12r^2-112r+\frac{117}{2}
 &r^2+62r+148
 &-12r-\frac{227}{2}+(r+32)b\\
6&r^3+124r^2+719r-414
 &-18r^2-503r-890
 &r^2+124r+743-(15r+221)b
\end{array}
\tag{3.4}
$$



Now


$$
\mathcal H=t-t^2+2t^3-2t^4+t^5-t^6.
$$


Combining the six evaluated moments yields the following integer polynomials:


$$
\boxed{
\begin{aligned}
\mathcal P(x)&=-8x^3-1116x^2-8150x+151,\\
\mathcal Q(x)&=76x^2+2408x+5637,\\
\mathcal F(x)&=4x^2+492x+5463,\\
\mathcal G(x)&=4x^2+556x-3325.
\end{aligned}}
\tag{3.5}
$$



The complete reductions are


$$
\boxed{
16U=\mathcal F(x)
-\mathcal P(x)\eta(C_\ell)
-2\mathcal Q(x)\eta(tC_\ell),
}
\tag{3.6}
$$




$$
\boxed{
16E_K=\mathcal G(x)
+\mathcal P(x)E(C_\ell)
+2\mathcal Q(x)E(tC_\ell).
}
\tag{3.7}
$$



All divisions in the moment calculation have been paid in these integer identities. The different source and endpoint constants in (3.5) are not interchangeable.

### 3.3 Return to the original integral coordinates

The Chebyshev product identity gives


$$
tC_\ell=\frac{C_{\ell+1}+2C_\ell+C_{\ell-1}}4.
$$


Using the original forced recurrences,


$$
\eta(tC_\ell)
=\ell\bigl((2\ell+1)\Theta_\ell-\Theta_{\ell-1}-1\bigr),
$$




$$
E(tC_\ell)
=\ell\bigl((2\ell+1)\Phi_\ell-\Phi_{\ell-1}\bigr)-(\ell+1).
\tag{3.8}
$$



Define


$$
\widetilde{\mathsf A}
=2\ell\bigl((2\ell+1)\mathcal Q-\mathcal P\bigr),
\qquad
\widetilde{\mathsf B}=-2\ell\mathcal Q,
$$




$$
\widetilde{\mathsf C}_U
=\mathcal F-\mathcal P+2\ell\mathcal Q,
$$




$$
\widetilde{\mathsf C}_E
=\mathcal G+\mathcal P-2(\ell+1)\mathcal Q,
\tag{3.9}
$$


with all four polynomials evaluated at $x=\ell^2$. Then


$$
\boxed{
16U=\widetilde{\mathsf C}_U
-\widetilde{\mathsf A}\Theta_\ell
-\widetilde{\mathsf B}\Theta_{\ell-1},
}
\tag{3.10}
$$




$$
\boxed{
16E_K=\widetilde{\mathsf C}_E
+\widetilde{\mathsf A}\Phi_\ell
+\widetilde{\mathsf B}\Phi_{\ell-1}.
}
\tag{3.11}
$$



The complete reduced endpoint is therefore


$$
\boxed{
16y_K
=d_K\bigl(
\widetilde{\mathsf C}_E
+\widetilde{\mathsf A}\Phi_\ell
+\widetilde{\mathsf B}\Phi_{\ell-1}
\bigr)-16a_K.
}
\tag{3.12}
$$


This keeps the actual reduction $a_K/d_K$, including every exceptional prime of $g_{\rm arc}$.

---

## 4. An evaluated integer Bézout identity

The crucial new algebra is


$$
\boxed{
\mathcal B_F(x)\mathcal F(x)
+\mathcal B_Q(x)\mathcal Q(x)
+\mathcal B_P(x)\mathcal P(x)=1,
}
\tag{4.1}
$$


with explicit integer coefficient polynomials of degree at most five.

This is stronger than asserting that three polynomials have no common factor over $\mathbb Q[x]$. It is an identity over $\mathbb Z[x]$, and therefore controls their numerical gcd after every integer evaluation.

### 4.1 Two evaluated elimination identities

Direct expansion gives


$$
(6593x+115642)\mathcal F
-(347x+37773)\mathcal Q
=418\,825\,845,
\tag{4.2}
$$


and


$$
1735\mathcal P+4753\mathcal Q
+(3470x-33052)\mathcal F
=-153\,508\,430.
\tag{4.3}
$$


The scalar Euclidean identity is


$$
4\,548\,519\cdot418\,825\,845
-12\,409\,985\cdot153\,508\,430=5.
\tag{4.4}
$$



Accordingly, define


$$
Z_F=
4\,548\,519(6593x+115642)
+12\,409\,985(3470x-33052),
$$




$$
Z_Q=
-4\,548\,519(347x+37773)
+12\,409\,985\cdot4753,
$$




$$
Z_P=12\,409\,985\cdot1735.
$$


Then


$$
Z_F\mathcal F+Z_Q\mathcal Q+Z_P\mathcal P=5.
\tag{4.5}
$$



A second evaluated relation is


$$
(2x^2+4x+1)\mathcal Q-(x+3)\mathcal P=4+5H(x),
\tag{4.6}
$$


where


$$
\boxed{
H(x)=32x^4+1252x^3+6496x^2+9851x+1036.
}
\tag{4.7}
$$


There is no unevaluated division by $5$ here.

Set


$$
\mathcal B_F=(1+H)Z_F,
$$




$$
\mathcal B_Q=(1+H)Z_Q-(2x^2+4x+1),
$$




$$
\mathcal B_P=(1+H)Z_P+(x+3).
\tag{4.8}
$$


Combining (4.5) and (4.6) gives


$$
5(1+H)-(4+5H)=1,
$$


which proves (4.1).

All coefficients are fixed integers. For example, the displayed factorizations immediately give a coefficient bound $10^{17}$ for the three polynomials in (4.8). Thus their evaluated heights are polynomial in $N$, not factorial in $N$.

### 4.2 Integer elimination of the centered coefficient row

From (3.9),


$$
2\ell\mathcal Q=-\widetilde{\mathsf B},
$$




$$
2\ell\mathcal P
=-\widetilde{\mathsf A}-(2\ell+1)\widetilde{\mathsf B},
$$




$$
2\ell\mathcal F
=2\ell\widetilde{\mathsf C}_U
-\widetilde{\mathsf A}-\widetilde{\mathsf B}.
\tag{4.9}
$$


Multiplying (4.1) by $2\ell$ gives the explicit integer identity


$$
\boxed{
\begin{aligned}
2\ell={}&
2\ell\mathcal B_F\,\widetilde{\mathsf C}_U
-(\mathcal B_F+\mathcal B_P)\widetilde{\mathsf A}\\
&-\bigl(\mathcal B_F+\mathcal B_Q
 +(2\ell+1)\mathcal B_P\bigr)\widetilde{\mathsf B}.
\end{aligned}}
\tag{4.10}
$$


Every coefficient in this identity has polynomial height in $N$.

It follows, at actual integer values, that


$$
\gcd(\widetilde{\mathsf A},
     \widetilde{\mathsf B},
     \widetilde{\mathsf C}_U)\mid2\ell.
\tag{4.11}
$$



---

## 5. Exact ALL-prime content of the complete $K$-row

### Theorem 5.1 — Centered coefficient-content theorem

For every original index $N$, with $\ell=2N-6$,


$$
\boxed{
\gcd(\widetilde{\mathsf A},
     \widetilde{\mathsf B},
     \widetilde{\mathsf C}_U)
=
8\gcd(83,\ell).
}
\tag{5.1}
$$


Equivalently,


$$
\boxed{
\gcd(16U,\widetilde{\mathsf A},\widetilde{\mathsf B})
=
8\gcd(83,\ell).
}
\tag{5.2}
$$



#### Proof

Let the gcd in (5.1) be $g$. Identity (4.10) gives $g\mid2\ell$.

Since $x=\ell^2$,


$$
\widetilde{\mathsf C}_U
\equiv \mathcal F(0)-\mathcal P(0)
=5463-151=5312=2^6\cdot83
\pmod\ell.
\tag{5.3}
$$


Therefore the odd part of $g$ divides $\gcd(83,\ell)$.

Conversely, if $83\mid\ell$, then both
$\widetilde{\mathsf A}$ and $\widetilde{\mathsf B}$ are divisible by $83$, and (5.3) makes
$\widetilde{\mathsf C}_U$ divisible by $83$. Thus the odd part is exactly $\gcd(83,\ell)$, including its depth.

For the binary part, every original $N$ satisfies $N\equiv1\pmod8$, so


$$
\ell=2N-6\equiv12\pmod{16},\qquad v_2(\ell)=2.
$$


Since $\mathcal Q(\ell^2)$ is odd,


$$
v_2(\widetilde{\mathsf B})=v_2(2\ell)=3.
$$


Also $\mathcal P(\ell^2)$ and $\mathcal Q(\ell^2)$ are odd, so
$\widetilde{\mathsf A}$ is divisible by $16$. Finally,


$$
\widetilde{\mathsf C}_U
=\mathcal F-\mathcal P+2\ell\mathcal Q
$$


is divisible by $8$, because $\mathcal F-\mathcal P$ is divisible by $16$ at $x=\ell^2$, while $2\ell\mathcal Q$ is divisible by $8$.

Hence $v_2(g)=3$. This proves (5.1).

Equation (3.10) shows


$$
\gcd(\widetilde{\mathsf A},
     \widetilde{\mathsf B},
     \widetilde{\mathsf C}_U)
=
\gcd(\widetilde{\mathsf A},
     \widetilde{\mathsf B},16U),
$$


proving (5.2). ∎

### 5.1 Reconciliation with the original terminal and thirteen-weight row

This is an internal change of coordinates, not a new producer.

Let


$$
H_j=
\begin{pmatrix}
-4j&1\\
1&0
\end{pmatrix},
\qquad
M_\ell=H_{\ell+5}H_{\ell+4}\cdots H_\ell.
$$


There are exactly six factors, and


$$
\det M_\ell=1.
$$


Define the complete six-step forcing vectors by


$$
f_0^-=f_0^+=0,
$$




$$
f_{r+1}^-=H_{\ell+r}f_r^-+\binom20,
$$




$$
f_{r+1}^+=H_{\ell+r}f_r^+
+\binom{2(-1)^{\ell+r}}0,
\qquad 0\le r\le5.
\tag{5.4}
$$


Then


$$
\binom{\Theta_n}{\Theta_{n-1}}
=M_\ell\binom{\Theta_\ell}{\Theta_{\ell-1}}+f_6^-,
$$




$$
\binom{\Phi_n}{\Phi_{n-1}}
=M_\ell\binom{\Phi_\ell}{\Phi_{\ell-1}}+f_6^+.
\tag{5.5}
$$



Substitution into the thirteen-weight evaluator gives the exact polynomial comparisons


$$
\boxed{
(\mathsf A,\mathsf B)M_\ell
=256(\widetilde{\mathsf A},\widetilde{\mathsf B}),
}
\tag{5.6}
$$




$$
\boxed{
\mathsf C_U-(\mathsf A,\mathsf B)f_6^-
=256\widetilde{\mathsf C}_U,
}
\tag{5.7}
$$




$$
\boxed{
\mathsf C_E+(\mathsf A,\mathsf B)f_6^+
=256\widetilde{\mathsf C}_E.
}
\tag{5.8}
$$



These identities can be verified directly by the fixed local recurrences (2.2): the homogeneous row is propagated through six steps, while (5.7) and (5.8) retain respectively every constant and alternating forcing term. Equations (3.4)–(3.11) supply the evaluated normal form. A bounded coefficient-array check of precisely these new comparisons is included in Section 8.

Because $M_\ell$ is integer unimodular and the constant columns differ by integer row combinations, (5.6)–(5.8) imply


$$
\gcd(\mathsf A,\mathsf B,\mathsf C_U)
=
256\gcd(\widetilde{\mathsf A},
        \widetilde{\mathsf B},
        \widetilde{\mathsf C}_U).
$$


Theorem 5.1 therefore proves


$$
\boxed{
\gcd(\mathsf A,\mathsf B,\mathsf C_U)
=2^{11}\gcd(83,2N-6).
}
\tag{5.9}
$$


Using the complete source identity (2.3) also gives


$$
\boxed{
\gcd(4096U,\mathsf A,\mathsf B)
=2^{11}\gcd(83,2N-6).
}
\tag{5.10}
$$



The factor $256$ is thus an evaluated integral coordinate factor, not an unpaid modular division.

### 5.2 Consequence for the two original lift slopes

At an odd prime, the original dual Wronskian makes


$$
\binom{u_1}{e_1}
=
\begin{pmatrix}
-H_a^-&-H_{a-1}^-\\
-H_a^+&H_{a-1}^+
\end{pmatrix}
\binom{\mathsf A}{\mathsf B}
$$


an invertible transformation, its determinant being $2$.

Consequently, if $p\mid U$,


$$
u_1=e_1=0
\quad\Longleftrightarrow\quad
p\mid\mathsf A,\mathsf B.
$$


Equation (5.10) proves


$$
\boxed{
p\mid U,\quad u_1=e_1=0
\quad\Longleftrightarrow\quad
p=83\ \text{and}\ 83\mid2N-6.
}
\tag{5.11}
$$



This is not a new finite-prime table. The number $83$ arises from the evaluated constant


$$
\mathcal F(0)-\mathcal P(0)=2^6\cdot83
$$


and an integer Bézout identity valid at all integer inputs.

In particular, for every $p>N$ dividing $U_N$, at least one of the two $K$-boundary slopes is a unit modulo $p$.

---

## 6. Why this elimination does not prove the factorial allowance

The new identity (4.10) has a small right side and polynomially bounded integer coefficients. Nevertheless, its generators are


$$
\widetilde{\mathsf C}_U,\quad
\widetilde{\mathsf A},\quad
\widetilde{\mathsf B},
$$


not


$$
U,\quad Vy_K.
$$



Substituting the actual boundary values replaces
$\widetilde{\mathsf C}_U$ by


$$
16U+\widetilde{\mathsf A}\Theta_\ell
+\widetilde{\mathsf B}\Theta_{\ell-1}.
$$


This does not make the two remaining row coefficients multiples of $Vy_K$. It therefore does not produce an identity


$$
a_NU+b_NV y_K=N!B_N
$$


with the required small $B_N$.

That is the precise obstruction to treating the new coefficient elimination as the desired numerical gcd elimination.

### 6.1 Affine intersections remain possible

The complete equations are


$$
16U=\widetilde{\mathsf C}_U
-\widetilde{\mathsf A}\Theta_\ell
-\widetilde{\mathsf B}\Theta_{\ell-1},
$$




$$
16y_K=
d_K\bigl(\widetilde{\mathsf C}_E
+\widetilde{\mathsf A}\Phi_\ell
+\widetilde{\mathsf B}\Phi_{\ell-1}\bigr)-16a_K,
$$


together with the actual paid $V$-equation.

A primitive coefficient row does not prevent either pair of affine equations


$$
U\equiv V\equiv0\pmod{p^k},
\qquad\text{or}\qquad
U\equiv y_K\equiv0\pmod{p^k}
$$


from holding at the original boundary values.

The original prime-$5$ exception already demonstrates this at a good determinant prime:


$$
5\nmid2g_B\Delta d_K,\qquad
v_5(U)=1,\qquad 5\nmid V,\qquad 5\mid y_K.
$$


Thus even the stronger all-depth coefficient-content theorem does not imply affine coprimality.

### 6.2 What is newly paid, and what remains unpaid

The new theorem pays the complete $K$-row degeneration:


$$
\gcd(4096U,\mathsf A,\mathsf B)
=2^{11}\gcd(83,2N-6).
$$



It does **not** pay:

* the product of primes for which the actual nondegenerate affine equations meet;
* their higher common depths;
* synchronization with the changing, actually divided Gaussian coefficients;
* the branches $p\mid\Delta$;
* the contribution of every $p>N$, for which $v_p(N!)=0$.

For those large primes, the result says that the row is nondegenerate, not that the actual outputs are coprime.

No original-family countermechanism disproving (FE) has been established either. Arbitrary-initial-state constructions are not original counterexamples.

---

## 7. Exact open obligation and its conditional effect on the actual $q$

Define the actual factorial excess


$$
\mathcal E_N=
\frac{\mathfrak J_N^0}
     {\gcd(\mathfrak J_N^0,N!)}.
\tag{7.1}
$$


At every original index, the already established $2,3,5,17$ valuations are fully paid by $N!$. Thus (FE) is exactly


$$
\boxed{\mathcal E_N\le e^{CN}.}
\tag{7.2}
$$



The unresolved assertion concerns the **numerical values** of the original sequences:


$$
\mathcal E_N
=
\prod_{p\notin\{2,3,5,17\}}
p^{\max\{0,\,
\min(v_p(U_N),v_p(V_N)+v_p(y_{K,N}))
-v_p(N!)\}}.
$$


It is not closed by naming this product or by the new coefficient-content theorem.

If (7.2) were proved, then


$$
\mathfrak J_N^0\le N!e^{CN}
=e^{O(N)}U_N^{1/2}.
$$


Since $\mu\le D<256^N$,


$$
q_N\ge\frac{U_N}{\mathfrak J_N}
\ge\frac{U_N}{\mu_N\mathfrak J_N^0}
\ge e^{-O(N)}U_N^{1/2}.
$$


Using the same positive whole error,


$$
\log(q_N\epsilon_N)
\ge N\log N-O(N)\longrightarrow+\infty.
\tag{7.3}
$$



More generally, any proved bound


$$
\mathfrak J_N^0\le e^{CN}U_N^{1-\delta_0},
\qquad\delta_0>0,
$$


would give


$$
q_N\epsilon_N\longrightarrow+\infty
\qquad(N\in\mathcal N).
$$



These deductions use


$$
q_N=\lambda_NM_N/G_N
$$


after the actual content, least aggregate clearer, and final ALL-prime reduction. They would retire this signed producer only. They would not establish that $e+\pi$ is rational.

### Literature gate

No external gcd theorem is imported. The archived fixed-$S$ obstruction remains applicable: an unremoved factorial has outside-$S$ height


$$
\log(N!)-O(N)
$$


for every fixed finite $S$. The present objects have not been represented as suitable fixed-base exponential or almost-$S$-unit points with checked exceptional-set avoidance. The cited abstracts do not supply the missing original-family estimate.

---

## 8. New bounded exact-arithmetic receipt

This is a genuinely different follow-on from fixed-prime tables: it checks a complete integer coefficient elimination and its reconciliation with the original finite source row.

It requires no enormous original Gaussian recurrence and no recomputation of $h,\lambda,G,q$.

### 8.1 Bounded inputs

1. The four explicitly evaluated polynomials
   

$$
\mathcal P,\mathcal Q,\mathcal F,\mathcal G
$$


   in (3.5), of degree at most three.

2. The moment recurrence (3.3), only for $k=0,1,2,3,4$, at the two symbolic boundaries $b=0,1$.

3. The fixed integers and polynomials in (4.2)–(4.8).

4. For the original-row comparison, the already available coefficient arrays for
   

$$
\mathsf A,\mathsf B,\mathsf C_U,\mathsf C_E,
$$


   together with $\ell=n-6$, the six matrices $H_\ell,\ldots,H_{\ell+5}$, and the two six-step forcing vectors (5.4). The closed source arrays should be reused.

5. The symbolic original-domain congruence
   

$$
N\equiv1\pmod8,\qquad \ell\equiv12\pmod{16}.
$$



All polynomial degrees in the comparison are bounded by $20$. The Bézout portion has degree at most five in $x$.

### 8.2 Expected verifiable outputs

**Complete moment reduction**

Zero coefficient residuals for


$$
16U-\mathcal F+\mathcal P\,\eta(C_\ell)
+2\mathcal Q\,\eta(tC_\ell),
$$


and


$$
16E_K-\mathcal G-\mathcal P\,E(C_\ell)
-2\mathcal Q\,E(tC_\ell),
$$


when the formal moments are reduced by (3.3). This checks both boundary constants, not only the homogeneous row.

**First elimination constants**


$$
(6593x+115642)\mathcal F
-(347x+37773)\mathcal Q
=418825845,
$$




$$
1735\mathcal P+4753\mathcal Q
+(3470x-33052)\mathcal F
=-153508430.
$$



**Scalar Euclidean residual**


$$
4548519\cdot418825845
-12409985\cdot153508430-5=0.
$$



**Paid division residual**


$$
(2x^2+4x+1)\mathcal Q-(x+3)\mathcal P-4
=
5(32x^4+1252x^3+6496x^2+9851x+1036).
$$



**Integer unit certificate**

A zero coefficient array for


$$
\mathcal B_F\mathcal F
+\mathcal B_Q\mathcal Q
+\mathcal B_P\mathcal P-1.
$$



**Original finite-row reconciliation**

Zero coefficient arrays for


$$
(\mathsf A,\mathsf B)M_\ell
-256(\widetilde{\mathsf A},\widetilde{\mathsf B}),
$$




$$
\mathsf C_U-(\mathsf A,\mathsf B)f_6^-
-256\widetilde{\mathsf C}_U,
$$




$$
\mathsf C_E+(\mathsf A,\mathsf B)f_6^+
-256\widetilde{\mathsf C}_E.
$$



**Content constants**

The exact outputs


$$
\mathcal F(0)-\mathcal P(0)=5312=64\cdot83,
$$




$$
v_2(\widetilde{\mathsf B})=3
\quad\text{under }\ell\equiv12\pmod{16},
$$


and the symbolic identity (4.10).

These outputs verify fixed polynomial identities. Their universal use is justified by the identities and the original-domain congruence, not by extrapolation from sampled $N$.

The receipt would not verify (FE), an aggregate cancellation bound, producer retirement, or a decision about $e+\pi$.

---

## 9. Final conclusions

### New proved result

The complete $K$-source and endpoint admit the evaluated centered forms (3.6)–(3.12), with all source and endpoint constants retained. The coefficient polynomials satisfy an explicit identity over $\mathbb Z[x]$:


$$
\mathcal B_F\mathcal F+\mathcal B_Q\mathcal Q+\mathcal B_P\mathcal P=1.
$$



This yields the exact original-row theorem


$$
\boxed{
\gcd(4096U_N,\mathsf A(2N),\mathsf B(2N))
=
2^{11}\gcd(83,2N-6).
}
$$


It controls every prime and every depth of complete $K$-row collapse.

### What has not been proved

Neither the paid factorial-excess lemma nor any strict intrinsic bound


$$
\mathfrak J_N^0\le e^{CN}U_N^{1-\delta_0}
$$


has been established. No paid original-family counterexample to that lemma has been found.

### Exact remaining bottleneck

After the new elimination, the unresolved cancellation occurs on **nondegenerate affine branches**. One must still control the aggregate prime-power mass of the actual simultaneous conditions


$$
U_N\equiv V_N\equiv0
\quad\text{or}\quad
U_N\equiv y_{K,N}\equiv0,
$$


using the original boundaries and actual paid Gaussian data. This includes every $p>N$, where $N!$ contributes no valuation, and all relevant $p\mid\Delta$ branches.

The original prime-$5$ exception shows why nondegeneracy alone cannot supply that control.

Throughout, the original index set, terminal $2N$, thirteen weights, both forced returns, complete cubic arc, actual Gaussian divisions, contents, least simultaneous and aggregate clearers, final ALL-prime $G$, actual primitive denominator, and positive whole error remain unchanged.

**The new result is an evaluated integer coefficient-elimination theorem. It is not the requested factorial-excess theorem, not retirement of the signed producer, and not an unconditional proof of rationality or irrationality of $e+\pi$.**
