> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Integral endpoint transfer and an evaluated prime-$17$ separation for the actual joint divisor

## Abstract and proof status

The index domain remains


$$
\mathcal N=\{N_u=9^{18+32u}:u\ge 0\}.
$$


Every statement about the producer below refers to these original indices, without replacing them by a subsequence.

This report does **not** prove the requested uniform estimate


$$
\gcd(U_N,V_NY_N)\le e^{CN}U_N^{1-\delta_0},
\qquad \delta_0>0.
$$


It does, however, prove an evaluated, source-specific arithmetic statement about this **joint** divisor, using the original source boundary, the alternating exponential-endpoint forcing, the actual signed Gaussian coefficients, and the complete rational arc.

The principal new original-index congruences are


$$
\boxed{
\begin{aligned}
U_{N_u}&\equiv 4+6u\pmod {17},\\
g_{B,N_u}^{\,2}V_{N_u}&\equiv 11+7u\pmod {17},\\
E_{K,N_u}&\equiv 16+13u\pmod {17}.
\end{aligned}}
\tag{A}
$$


Here $17\nmid g_{B,N_u}$, proved below from the actual Gaussian recurrence. In particular,


$$
\boxed{17\nmid c_{N_u},\qquad 17\nmid\gcd(U_{N_u},E_{K,N_u})}
\tag{B}
$$


for every original $u$.

The arc cannot be omitted when passing from $E_K$ to $Y$. Let


$$
d_K=\operatorname{den}(R_K),\qquad
\mu=\frac{D}{d_K},
$$


with $R_K$ reduced completely and $D$ the actual least simultaneous column clearer. Put


$$
s_u=v_{17}(2N_u-9),\qquad e_u=v_{17}(D_{N_u}).
$$


Then


$$
\boxed{
v_{17}(d_K)=s_u\ge1,\qquad
v_{17}\gcd(U,VY)=
\min\{v_{17}(U),\,e_u-s_u\}.
}
\tag{C}
$$


Thus all prime-$17$ cancellation in the joint divisor is accounted for by the **excess simultaneous clearing** $D/d_K$; it does not come from intrinsic cancellation against either $V$ or the reduced complete $K$-endpoint column.

Consequently,


$$
\boxed{
\bigl(\gcd(U,VY)\bigr)_{17}
\le 17^{\lfloor\log_{17}(2N-1)\rfloor-s_u}
\le \frac{2N-1}{17^{s_u}}.
}
\tag{D}
$$


This is a uniform, quantitatively bounded part of the actual joint cancellation. It is not an ALL-prime estimate of the required strength.

A second new calculation evaluates the complete $K$-arc denominator. With $x=4(N-3)^2$,


$$
R_K=
\frac{13x^3-455x^2+3502x-5850}
     {30(x-1)(x-9)(x-25)},
$$


and the cancellation between this displayed numerator and denominator divides the fixed integer


$$
\boxed{31\,806\,000=2^4\,3^3\,5^3\,19\,31.}
\tag{E}
$$


This supplies an ALL-prime treatment of the arc-denominator exceptions rather than discarding modular poles.

The report also derives an explicit two-minor separation criterion for the original source and endpoint coordinates. The remaining follow-on obligation is to prove that the primes passing this evaluated separation test carry a positive proportion of $\log U_N$. That aggregate estimate is open.

No tools or computations have been executed. A small bounded arithmetic receipt is specified at the end. The global rationality or irrationality of $e+\pi$, and retirement of this signed producer, remain unresolved.

---

## 1. Exact producer, normalization, and whole error

### 1.1 Original source and paid square column

Write


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


where


$$
C_0=1,\quad C_1=2t-1,\quad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$



At an original index $N$, retain


$$
d=a_Nb_{N-1}-a_{N-1}b_N,
\qquad
B=b_{N-1}C_N-b_NC_{N-1}.
$$


The source functional is


$$
\eta(H)=\int_{-\infty}^{1}e^{t-1}H(t)\,dt.
$$


The corrected $x=1-t$ formula, already proved and audited, is


$$
\eta(H)=\sum_{r\ge0}[x^r]H(1-x)\,r!.
$$


No additional alternating sign is introduced.

Set


$$
K=t(1-t)(1+t^2)^2C_{N-3}^2,\qquad U=-\eta(K),
$$


and make the actual paid division


$$
g_B=\gcd(b_{N-1},b_N)>0,
$$




$$
\alpha=\frac{b_{N-1}}{g_B},\qquad
\beta=\frac{b_N}{g_B},\qquad
F=\alpha C_N-\beta C_{N-1},\qquad
\delta=\frac d{g_B}.
$$


Thus


$$
F(i)=F(-i)=\delta,\qquad \gcd(\alpha,\beta)=1.
$$



The source gcd remains


$$
V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V)>0.
$$


The established content theorem is reused at its proved scope:


$$
\boxed{
h=\operatorname{cont}(W_{\rm raw})=g_B^2c.
}
$$


Accordingly,


$$
\tau=\frac Uc,\qquad \nu=\frac Vc,\qquad
W_{\rm prim}=\tau F^2+\nu K,\qquad
M=\tau\delta^2.
$$


All original indices satisfy the already audited hypotheses $N\ge256$, so


$$
U>0,\qquad V>0,\qquad M>0.
$$



Nothing below replaces $c$ by a gcd involving the unpaid raw square column.

### 1.2 Complete columns and the two different clearers

For $H\in\mathbb Z[t]$, define the complete exponential endpoint


$$
E(H)=\sum_{r=0}^{\deg H}(-1)^rr![t^r]H.
$$


Retain


$$
E_F=E(F^2),\qquad E_K=E(K),
$$


and the complete monic-division arcs


$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,
\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$



The least simultaneous column clearer is


$$
D=\operatorname{lcm}\bigl(\operatorname{den}(R_F),
                         \operatorname{den}(R_K)\bigr),
$$


with each column reduced before its denominator is taken. Define


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$



Independently, reduce the **single aggregate arc**


$$
\tau R_F+\nu R_K=\frac b\lambda,
\qquad \gcd(b,\lambda)=1,\quad \lambda>0.
$$


This $\lambda$, not $D$, is the actual least aggregate clearer. Put


$$
E=\tau E_F+\nu E_K,\qquad
A=\lambda E-b,\qquad
G=\gcd(M,A).
$$


The actual primitive pair remains


$$
\boxed{
q=\frac{\lambda M}{G},\qquad p=\frac A G.
}
\tag{1.1}
$$



The exact reconciliation of the two clearers is


$$
\tau X+\nu Y=\frac D\lambda A,
$$




$$
\boxed{
\gcd(D\tau\delta^2,\tau X+\nu Y)=\frac D\lambda G.
}
\tag{1.2}
$$


Thus excess simultaneous clearing returns inside the final ALL-prime gcd. It is never silently substituted for $\lambda$.

Likewise, the retained raw-interface identity is


$$
\gcd(A_{\rm raw},B_{\rm raw})
=\frac{L_{\rm aff}h}{\lambda}G,
\qquad
L_{\rm aff}=\operatorname{lcm}(1,\ldots,2N-1).
$$



The physical polynomial terminal is $2N$. The monic arc quotients have degree at most $2N-2$, so all integration denominators stop at $2N-1$.

### 1.3 The actual joint divisor reaches the actual denominator

Let


$$
\mathfrak J=\gcd(U,VY).
$$


The established surviving-divisor theorem gives


$$
\frac{\tau}{\gcd(\tau,Y)}\mid q.
$$


Prime by prime,


$$
c\,\gcd(U/c,Y)=\gcd(U,VY).
$$


Hence


$$
\boxed{\frac U{\mathfrak J}\mid q.}
\tag{1.3}
$$



For clarity, this divisibility is compatible with every prime dividing $D$, $\delta$, or a recurrence coefficient. If a prime has $t=v_p(\tau)>v_p(Y)$, then $\nu$ is a unit at that prime and


$$
v_p(\tau X+\nu Y)=v_p(Y).
$$


Reduction of


$$
\frac{\tau X+\nu Y}{D\tau\delta^2}
$$


therefore leaves at least $t-v_p(Y)$ powers of that prime in its denominator. The remaining cases impose no positive surviving exponent. This proves the stated divisor without replacing the final gcd by a selected-prime gcd.

### 1.4 The same nonzero whole error

The rational polynomial remains


$$
P=\frac{F^2+(V/U)K}{\delta^2}.
$$


At every original index,


$$
\epsilon_N=
\int_0^1P(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0,
$$


and the audited ordinary-error estimate is


$$
\epsilon_N\asymp R^{-2N},
\qquad
R=1+\sqrt2+\sqrt{2+2\sqrt2}.
$$


The exact normalized error is


$$
\boxed{q_N(e+\pi)-p_N=q_N\epsilon_N>0.}
\tag{1.4}
$$



The complete rational enclosure is also retained. Put $m=N-3$ and


$$
j_r=\frac1{1-4r^2}=j_{-r}.
$$


Then


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


Thus


$$
\boxed{
3J_N<\epsilon_N<7J_N,\qquad
q_NJ_N=\frac{\lambda_N}{G_N}
       (\tau_NJ_F+\nu_NJ_K).
}
\tag{1.5}
$$


Both positive summands of the producer remain present.

The audited critical content estimate


$$
\log c_N\le N\log N+O(N)
$$


and the already proved lower bound


$$
q_N\epsilon_N>
\frac{N^N}{512\,2400^N c_N\sqrt{119N\log_2N}}
$$


are reused. Neither is reproved here. The turn-7 Bessel decomposition and exponential crossover are not rederived.

---

## 2. Integral exponential-endpoint coordinates

### 2.1 The source coordinate is reused

Let


$$
S_j=\eta(C_j).
$$


A3’s proved and independently checked integral refinement is


$$
S_j=1-2j\Theta_j,\qquad
\Theta_0=0,\quad\Theta_1=1,
$$




$$
\boxed{
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2
\qquad(j\ge1).
}
\tag{2.1}
$$


The original boundary $(0,1)$ is retained.

### 2.2 The endpoint coordinate and its alternating forcing

Define, for $j\ge1$,


$$
\Phi_j=E\!\left(U_{j-1}(2t-1)\right),\qquad \Phi_0=0,
$$


where $U_{j-1}$ denotes the Chebyshev polynomial of the second kind.

The classical derivative identity


$$
C_j'=2j\,U_{j-1}(2t-1)
$$


pays the division by $2j$ at the polynomial level. In particular, $\Phi_j\in\mathbb Z$.

For every polynomial $H$,


$$
E(H')=H(0)-E(H).
$$


Since $C_j(0)=(-1)^j$,


$$
\boxed{\mathcal E_j:=E(C_j)=(-1)^j-2j\Phi_j.}
\tag{2.2}
$$


Substitution into the complete endpoint recurrence gives


$$
\boxed{
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j
\qquad(j\ge1),
}
\tag{2.3}
$$


with


$$
\Phi_0=0,\qquad \Phi_1=1,\qquad \Phi_2=-6.
$$


The case $j=1$ is checked directly:


$$
-6+4=-2.
$$


Thus no singular instance of the old normalized recurrence is inverted.

This is an integral coordinate change in the same complete endpoint functional. It does not homogenize the alternating forcing.

---

## 3. Complete source and endpoint planes, including returns

Put


$$
n=2N.
$$


The fixed thirteen weights are


$$
(w_0,\ldots,w_{12})
=(1,8,58,168,399,-176,-916,-176,399,168,58,8,1).
\tag{3.1}
$$


They satisfy


$$
\sum_{k=0}^{12}w_k=0,\qquad
\sum_{k=0}^{12}(-1)^kw_k=0.
$$



### 3.1 Reused integral source plane

Retain the fixed local coefficients


$$
r_0=1,\quad s_0=0,\qquad r_1=0,\quad s_1=1,
$$




$$
r_{k+1}=r_{k-1}+4(n-k)r_k,\qquad
s_{k+1}=s_{k-1}+4(n-k)s_k
\quad(1\le k\le11),
$$


and


$$
\kappa_0=\kappa_1=0,\qquad
\kappa_{k+1}=\kappa_{k-1}+4(n-k)\kappa_k-2.
$$


Define


$$
\mathsf A=\sum_{k=0}^{12}w_k(n-k)r_k,\qquad
\mathsf B=\sum_{k=0}^{12}w_k(n-k)s_k,
$$




$$
\mathsf C_U
=679936-\sum_{k=0}^{12}w_k(n-k)\kappa_k.
$$


The already checked source identities are


$$
\boxed{
4096U=\mathsf C_U-\mathsf A\Theta_n-\mathsf B\Theta_{n-1},
}
\tag{3.2}
$$




$$
\boxed{
V=\mathsf C_V-\mathsf P\Theta_n-\mathsf Q\Theta_{n-1},
}
\tag{3.3}
$$


where


$$
\mathsf P=n\alpha^2+(n-2)\beta^2,
$$




$$
\mathsf Q=4(n-1)(n-2)\beta^2-2(n-1)\alpha\beta,
$$




$$
\mathsf C_V=\alpha^2+(2n-3)\beta^2-\delta^2.
\tag{3.4}
$$


The actual signed $\alpha,\beta,\delta$, including the term $-\delta^2$, are retained.

The checked polynomial $\mathsf C_U$, its coefficient receipt, and the cancellation


$$
\mathsf E=2\mathsf C_U-\frac{\mathsf A}{n}-\frac{\mathsf B}{n-1}
$$


are reused, not recomputed as a new full symbolic normalization.

### 3.2 The complete integral $K$-endpoint plane

Let


$$
H=t(1-t)(1+t^2)^2.
$$


Its complete endpoint is


$$
E(H)=-1-2-12-48-120-720=-903.
$$


The established Chebyshev product reduction therefore gives


$$
8192E_K=-3\,698\,688-\sum_{k=0}^{12}w_k\mathcal E_{n-k}.
$$


Because $n$ is even and $\sum(-1)^kw_k=0$, equation (2.2) yields


$$
4096E_K=-1\,849\,344
+\sum_{k=0}^{12}w_k(n-k)\Phi_{n-k}.
\tag{3.5}
$$



Define the alternating local return


$$
\omega_0=\omega_1=0,
$$




$$
\boxed{
\omega_{k+1}
=\omega_{k-1}+4(n-k)\omega_k-2(-1)^k
\quad(1\le k\le11).
}
\tag{3.6}
$$


Then


$$
\Phi_{n-k}=r_k\Phi_n+s_k\Phi_{n-1}+\omega_k.
$$


Consequently,


$$
\boxed{
4096E_K=\mathsf A\Phi_n+\mathsf B\Phi_{n-1}+\mathsf C_E,
}
\tag{3.7}
$$


where the complete integer constant is


$$
\boxed{
\mathsf C_E
=-1\,849\,344+
\sum_{k=0}^{12}w_k(n-k)\omega_k.
}
\tag{3.8}
$$


Every alternating forcing term is included.

### 3.3 The complete square endpoint

Using the full product formula for $F^2$, including $\mathcal E_1=-3$, gives


$$
E_F
=\alpha^2+\beta^2+4\alpha\beta
-n\alpha^2\Phi_n-(n-2)\beta^2\Phi_{n-2}
+2(n-1)\alpha\beta\Phi_{n-1}.
$$


At the odd index $n-1$,


$$
\Phi_{n-2}=\Phi_n+4(n-1)\Phi_{n-1}+2.
$$


Thus


$$
\boxed{
E_F=\mathsf C_F^E-\mathsf P\Phi_n-\mathsf Q\Phi_{n-1},
}
\tag{3.9}
$$


where


$$
\boxed{
\mathsf C_F^E
=\alpha^2+(5-2n)\beta^2+4\alpha\beta.
}
\tag{3.10}
$$


In particular, the endpoint constant is not the source constant $\mathsf C_V$.

### 3.4 Complete arcs and an integer joint transfer

The complete arc return remains


$$
R_j(t)=\frac{C_j(t)-a_j-b_jt}{1+t^2},
\qquad
\xi_j=4\int_0^1R_j,\qquad
\upsilon_j=4\int_0^1tR_j,
$$


with zero values at $j=0,1$, and


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


The odd singular index is handled by its stated value, not by substituting into the even formula. Then


$$
R_F=\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
                  -2\alpha\beta\xi_{n-1}}2.
$$



Set


$$
k_E=D\mathsf C_E-4096DR_K,\qquad
f_E=D\mathsf C_F^E-DR_F.
$$


These are integers. Equations (3.7) and (3.9) become


$$
4096Y=D\mathsf A\Phi_n+D\mathsf B\Phi_{n-1}+k_E,
$$




$$
X=f_E-D\mathsf P\Phi_n-D\mathsf Q\Phi_{n-1}.
\tag{3.11}
$$



Let


$$
\Delta=\mathsf A\mathsf Q-\mathsf B\mathsf P.
$$


The established strict determinant theorem gives $\Delta<0$ on the present scope.

The retained source return is


$$
z_n=4096\mathsf Q U-\mathsf B V,\qquad
z_{n-1}=\mathsf A V-4096\mathsf P U,
$$




$$
z_j=-\Delta\Theta_j+r_j,
$$


with


$$
z_{j-1}=z_{j+1}+4jz_j,\qquad
r_{j-1}=r_{j+1}+4jr_j-2\Delta.
\tag{3.12}
$$


The previously checked relations $Z_j=2z_j$ and
$\rho_j=2r_j-\Delta/j$ remain in force.

For the complete endpoint pair define


$$
w_n=4096\mathsf QY+\mathsf B X,\qquad
w_{n-1}=-4096\mathsf PY-\mathsf A X.
$$


Then


$$
w_j=D\Delta\Phi_j+\sigma_j,
$$


where


$$
\sigma_n=\mathsf Qk_E+\mathsf Bf_E,\qquad
\sigma_{n-1}=-\mathsf Pk_E-\mathsf Af_E,
$$


and


$$
\boxed{
w_{j-1}=w_{j+1}+4jw_j,\qquad
\sigma_{j-1}
=\sigma_{j+1}+4j\sigma_j+2D\Delta(-1)^j.
}
\tag{3.13}
$$



These are integral equations at every prime, including primes dividing $2\Delta$. No inverse of $2\Delta$ has been used.

At the terminal,


$$
\boxed{
z_nw_{n-1}-z_{n-1}w_n
=-4096\Delta(UX+VY).
}
\tag{3.14}
$$


This identifies the joint transfer exactly. It does **not** by itself furnish a smaller integer bounding the joint divisor: its right side is a paid multiple of the already retained complete output. Unimodularity preserves this identity but does not supply the missing quantitative cancellation estimate.

---

## 4. An evaluated ALL-prime arc-denominator lemma

### 4.1 Combining the complete $K$-arc

The supplied complete formula is


$$
R_K=\frac{13}{30}
+\frac{42j_m-20(j_{m+1}+j_{m-1})
-(j_{m+2}+j_{m-2})}{128}.
$$


Put


$$
x=4m^2,
\qquad
L(x)=(x-1)(x-9)(x-25).
$$


Direct combination gives


$$
j_{m+1}+j_{m-1}
=-\frac{2(x+3)}{(x-1)(x-9)},
$$




$$
j_{m+2}+j_{m-2}
=-\frac{2(x+15)}{(x-9)(x-25)}.
$$


The numerator of the bracket over $L(x)$ is


$$
-42(x-9)(x-25)+40(x+3)(x-25)+2(x+15)(x-1)
=192(3x-65).
$$


Therefore


$$
\boxed{
R_K=\frac{A_K(x)}{30L(x)},
\qquad
A_K(x)=13x^3-455x^2+3502x-5850.
}
\tag{4.1}
$$



### Theorem 4.1 — Fixed bound for cancellation in the displayed arc fraction

For every integer $x$,


$$
\boxed{
\gcd(A_K(x),30L(x))\mid31\,806\,000.
}
\tag{4.2}
$$



#### Proof

The polynomial identities are


$$
A_K(x)=13L(x)+45(3x-65),
$$




$$
27L(x)
=(3x-65)(9x^2-120x-269)-23560.
$$


If $g=\gcd(A_K(x),30L(x))$, then


$$
g\mid1350(3x-65),\qquad g\mid30L(x).
$$


Combining the two identities gives


$$
g\mid1350\cdot23560=31\,806\,000.
$$


The factorization is


$$
31\,806\,000=2^4\,3^3\,5^3\,19\,31.
$$


No prime has been excluded. ∎

At an original index, $x=4(N-3)^2$ and $L(x)>0$. Define the actual reduced column data


$$
g_{\rm arc}=\gcd(A_K(x),30L(x)),
$$




$$
a_K=\frac{A_K(x)}{g_{\rm arc}},\qquad
d_K=\frac{30L(x)}{g_{\rm arc}}.
$$


Then


$$
R_K=\frac{a_K}{d_K},\qquad \gcd(a_K,d_K)=1,\quad d_K>0,
$$


and


$$
d_K\ge\frac{L(x)}{1\,060\,200}.
\tag{4.3}
$$



For primes outside $\{2,3,5,19,31\}$,


$$
p\mid L(x)\quad\Longrightarrow\quad v_p(d_K)=v_p(L(x)).
$$


At the five exceptional primes, the exact gcd $g_{\rm arc}$ remains in the formula; they have not been inverted away.

### 4.2 Exact effect on the joint divisor

Put


$$
y_K=d_KE_K-a_K,\qquad \mu=\frac D{d_K}.
$$


Then, exactly,


$$
\boxed{Y=\mu y_K.}
\tag{4.4}
$$


Define the intrinsic joint divisor


$$
\mathfrak J^0=\gcd(U,Vy_K).
$$


A prime-power comparison proves


$$
\boxed{
\mathfrak J^0\mid\mathfrak J\mid\mu\mathfrak J^0.
}
\tag{4.5}
$$


This is an exact ALL-prime comparison, not a substitution of $d_K$ for $D$.

At every prime dividing $d_K$, reduction of the complete arc gives


$$
p\nmid y_K.
$$


Consequently,


$$
\boxed{
v_p(\mathfrak J)
=v_p(c)+\min\{v_p(U/c),\,v_p(\mu)\}
\qquad(p\mid d_K).
}
\tag{4.6}
$$


Thus an arc-denominator prime can cancel beyond the source content only through the explicitly paid excess clearer $\mu$.

---

## 5. Evaluation at the original prime-$17$ branch

This section uses the actual source boundary and actual Gaussian data. It does not infer selected-output primitivity from full-state primitivity.

### 5.1 A boundary-specific affine lift formula

Define


$$
T_j^-=\Theta_j,\qquad
T_j^+=(-1)^{j-1}\Phi_j\quad(j\ge1),
\qquad T_0^\pm=0.
$$


Both start with


$$
T_0^\pm=0,\qquad T_1^\pm=1,
$$


and satisfy


$$
T_{j+1}^\pm=\pm4jT_j^\pm+T_{j-1}^\pm+2.
\tag{5.1}
$$



The classical second-kind coefficient formula gives


$$
\boxed{
T_j^\pm
=\sum_{r=0}^{j-1}(\pm4)^rr!\binom{j+r}{2r+1}.
}
\tag{5.2}
$$


This formula is tied to the boundary $(0,1)$; it is not valid for arbitrary initial states of the same recurrence.

Modulo an odd prime $p$, terms with $r\ge p$ vanish. Since $2r+1<2p$ for the retained terms,


$$
(1+z)^{a+p\ell+r}
\equiv(1+z)^{a+r}(1+\ell z^p)\pmod{p,z^{2p}}.
$$


Therefore


$$
\boxed{
T_{a+p\ell}^{\pm}
\equiv T_a^\pm+
\ell\bigl(T_{a+p}^\pm-T_a^\pm\bigr)\pmod p.
}
\tag{5.3}
$$


This proves the affine dependence and the required period in the lift digit. It is not a finite extrapolation.

For $p=17$, the needed boundary values, obtained from (5.1), are


$$
\begin{array}{c|rrrr}
j&8&9&25&26\\ \hline
T_j^-&2&11&15&7\\
T_j^+&14&16&10&12
\end{array}
\qquad(\bmod17).
\tag{5.4}
$$


In both rows the lift differences at $8,9$ are $13$. Hence, if


$$
n=9+17\ell,
$$


then


$$
\Theta_n\equiv11+13\ell,\qquad
\Theta_{n-1}\equiv2+13\ell.
\tag{5.5}
$$


Because the actual $n=2N$ is even,


$$
\Phi_n=-T_n^+,\qquad \Phi_{n-1}=T_{n-1}^+.
$$


Thus


$$
\boxed{
\Phi_n\equiv1-13\ell,\qquad
\Phi_{n-1}\equiv14+13\ell\pmod{17}.
}
\tag{5.6}
$$


The parity here is the parity of the original terminal, not of its residue representative $9$.

### 5.2 Evaluation of the fixed local constants

Evaluating the already established integer source polynomials at $n\equiv9\pmod{17}$ gives


$$
\boxed{
\mathsf A\equiv7,\qquad
\mathsf B\equiv1,\qquad
\mathsf C_U\equiv11\pmod{17}.
}
\tag{5.7}
$$


For the new alternating return (3.6), its values at this residue are


$$
(\omega_0,\ldots,\omega_{12})
\equiv
(0,0,2,3,8,8,2,13,6,1,8,1,2)\pmod{17}.
$$


Substitution into (3.8) gives


$$
\boxed{\mathsf C_E\equiv0\pmod{17}.}
\tag{5.8}
$$



These are evaluations of fixed integer polynomials. They do not move the actual physical terminal to $9$, nor extend the producer to negative indices.

Since $4096\equiv-1\pmod{17}$, equations (3.2), (3.7), (5.5), and (5.6) yield


$$
\boxed{
U\equiv2\ell,\qquad
E_K\equiv13+10\ell\pmod{17}.
}
\tag{5.9}
$$



### 5.3 Actual Gaussian data modulo $17$

In $\mathbb F_{17}$, the two values of $i$ are $4$ and $-4$.

At $i=4$, the Gaussian Chebyshev recurrence becomes


$$
C_{j+1}=-3C_j-C_{j-1},
\qquad C_0=1,\quad C_1=7.
$$


Its values through return of the initial pair are


$$
1,7,12,8,15,15,8,12,7,1,7.
$$


Thus it has period $9$ for this initial state.

At $i=-4$, the recurrence is


$$
C_{j+1}=-C_j-C_{j-1},
\qquad C_0=1,\quad C_1=8,
$$


with period $3$:


$$
1,8,8,1,8,\ldots.
$$



Every original $N$ is divisible by $9$. Consequently,


$$
C_N(i)\equiv1,\qquad
C_{N-1}(i)\equiv-1+2i\pmod{17}.
$$


Therefore


$$
a_N\equiv1,\quad b_N\equiv0,\quad
a_{N-1}\equiv-1,\quad b_{N-1}\equiv2.
\tag{5.10}
$$


In particular,


$$
\boxed{17\nmid g_B.}
\tag{5.11}
$$


For the actual paid quantities,


$$
\beta\equiv0,\qquad \delta\equiv\alpha\not\equiv0\pmod{17},
\qquad g_B^2\alpha^2\equiv4.
$$



Since $n\equiv9$, equations (3.3)–(3.4) now give


$$
V\equiv-9\alpha^2\Theta_n
\equiv\alpha^2(3+2\ell)\pmod{17}.
$$


Hence


$$
\boxed{g_B^2V\equiv12+8\ell\pmod{17}.}
\tag{5.12}
$$


The multiplication by $g_B^2$ is used only after proving it is a $17$-adic unit. It is not a global replacement of the paid source gcd.

### 5.4 The lift digit at every original index

Modulo $17^2=289$,


$$
9^8\equiv171,\qquad
9^{18}\equiv166,\qquad
9^{32}\equiv103=1+6\cdot17.
$$


Thus


$$
2N_u
=2\cdot9^{18}(9^{32})^u
\equiv9+17(2+3u)\pmod{289}.
$$


The lift digit in (5.9) and (5.12) is therefore


$$
\ell\equiv2+3u\pmod{17}.
$$



This proves the announced congruences


$$
\boxed{
U_{N_u}\equiv4+6u,\quad
g_{B,N_u}^{\,2}V_{N_u}\equiv11+7u,\quad
E_{K,N_u}\equiv16+13u
\pmod{17}.
}
\tag{5.13}
$$



### Theorem 5.1 — Evaluated original-source separation at $17$

For every original index,


$$
\boxed{
g_B^2V-4U\equiv12,\qquad
E_K-5U\equiv13\pmod{17}.
}
\tag{5.14}
$$


Consequently,


$$
\boxed{17\nmid c,\qquad17\nmid\gcd(U,E_K).}
\tag{5.15}
$$



More precisely,


$$
17\mid U\iff u\equiv5\pmod{17},
$$




$$
17\mid V\iff u\equiv13\pmod{17},
$$




$$
17\mid E_K\iff u\equiv4\pmod{17}.
$$


These are first-digit statements. No unstated higher valuation of $U$, $V$, or $E_K$ is inferred.

---

## 6. The complete joint cancellation at $17$

The passage from Theorem 5.1 to the actual $Y$ requires the arc calculation. Omitting it would give an incorrect modular argument.

Since


$$
x=(n-6)^2,
$$


we have


$$
L(x)
=(n-7)(n-5)(n-9)(n-3)(n-11)(n-1).
\tag{6.1}
$$


At all original indices, $n\equiv9\pmod{17}$. Exactly one factor on the right is divisible by $17$, namely $n-9$. Also


$$
A_K(9)=-1710\not\equiv0\pmod{17}.
$$


Therefore


$$
\boxed{
v_{17}(d_K)=v_{17}(n-9)=:s_u\ge1.
}
\tag{6.2}
$$



The congruence for $n$ modulo $289$ gives


$$
s_u\ge2\iff u\equiv5\pmod{17}.
\tag{6.3}
$$


Thus


$$
17\mid U\iff s_u\ge2.
$$


This equivalence concerns divisibility only, not equality of valuations.

For completeness, the higher arc-denominator branches are also controlled. Since


$$
v_{17}(9^{32}-1)=1,
$$


for every $k\ge1$ there is exactly one residue class of $u$ modulo $17^{k-1}$ for which $s_u\ge k$. Indeed, lifting
$u$ by $t17^{k-1}$ changes $n_u$, modulo $17^{k+1}$, by


$$
54t\,17^k,
$$


whose coefficient is $3\pmod{17}$, a unit. The first nontrivial branch is $u\equiv5\pmod{17}$. This is a lifting proof, not a higher-depth numerical extrapolation.

Now $17\nmid y_K$ because $17\mid d_K$ and $\gcd(a_K,d_K)=1$. Theorem 5.1 also gives $17\nmid c$. Therefore (4.6) becomes


$$
\boxed{
v_{17}(\mathfrak J)
=\min\{v_{17}(U),\,v_{17}(\mu)\}
=\min\{v_{17}(U),\,v_{17}(D)-s_u\}.
}
\tag{6.4}
$$



Since


$$
D\mid\operatorname{lcm}(1,\ldots,2N-1),
$$




$$
v_{17}(D)\le\lfloor\log_{17}(2N-1)\rfloor.
$$


Hence


$$
\boxed{
(\mathfrak J)_{17}
\le17^{\lfloor\log_{17}(2N-1)\rfloor-s_u}
\le\frac{2N-1}{17^{s_u}}.
}
\tag{6.5}
$$



Finally, the surviving-divisor theorem reaches the actual primitive denominator:


$$
\boxed{
17^{\max\{0,\ v_{17}(U)-v_{17}(D)+s_u\}}\mid q.
}
\tag{6.6}
$$



Equation (6.6) is a lower bound for the $17$-part of the actual $q$, not an equality for that part. The least aggregate $\lambda$, the target $\delta^2\tau$, and the final ALL-prime $G$ can leave further powers in $q$.

In particular, this report does **not** assert $17\nmid\mathfrak J$: excess clearing $\mu=D/d_K$ may contribute. What is proved is that such cancellation is entirely bounded by that actual paid excess.

---

## 7. A concrete all-prime separation test

The preceding calculation suggests a specific arithmetic follow-on, rather than another archimedean return-height estimate.

### 7.1 Two explicit minors at an arbitrary odd prime

Fix an original $N$ and an odd prime $p$. Write


$$
n=a+p\ell,\qquad 1\le a\le p.
$$


For the original-boundary sequences in (5.1), set


$$
H_j^\pm=T_{j+p}^\pm-T_j^\pm\pmod p.
$$


Equation (5.3) gives the actual source and endpoint values:


$$
\Theta_n=T_a^-+\ell H_a^-,
\qquad
\Theta_{n-1}=T_{a-1}^-+\ell H_{a-1}^-,
$$




$$
\Phi_n=-T_a^+-\ell H_a^+,
\qquad
\Phi_{n-1}=T_{a-1}^++\ell H_{a-1}^+
\pmod p.
$$



Evaluate all local coefficients and the **actual paid**
$\alpha,\beta,\delta$ modulo $p$. Define


$$
\begin{aligned}
u_0&=\mathsf C_U-\mathsf A T_a^--\mathsf B T_{a-1}^-,\\
u_1&=-\mathsf A H_a^--\mathsf B H_{a-1}^-,
\end{aligned}
$$




$$
\begin{aligned}
v_0&=\mathsf C_V-\mathsf P T_a^--\mathsf Q T_{a-1}^-,\\
v_1&=-\mathsf P H_a^--\mathsf Q H_{a-1}^-,
\end{aligned}
$$


and


$$
\begin{aligned}
e_0&=\mathsf C_E-\mathsf A T_a^++\mathsf B T_{a-1}^+,\\
e_1&=-\mathsf A H_a^++\mathsf B H_{a-1}^+.
\end{aligned}
$$


Then


$$
4096U=u_0+\ell u_1,\qquad
V=v_0+\ell v_1,\qquad
4096E_K=e_0+\ell e_1\pmod p.
$$



Use the actual reduced arc data to define


$$
y_0=d_Ke_0-4096a_K,\qquad y_1=d_Ke_1.
$$


Thus


$$
4096y_K=y_0+\ell y_1\pmod p.
$$



The two explicitly specified minors are


$$
\boxed{
\mathfrak m_V=u_0v_1-u_1v_0,\qquad
\mathfrak m_K=u_0y_1-u_1y_0.
}
\tag{7.1}
$$



### Proposition 7.1 — Boundary-specific prime separation

If both minors in (7.1) are nonzero modulo $p$, then


$$
\boxed{p\nmid\gcd(U,Vy_K).}
\tag{7.2}
$$



#### Proof

If $p\mid U,V$, the two affine equations for $4096U$ and $V$ have the common root $\ell$, forcing $\mathfrak m_V=0$.

If $p\mid U,y_K$, the equations for $4096U$ and $4096y_K$ force $\mathfrak m_K=0$.

But a prime dividing $\gcd(U,Vy_K)$ must satisfy one of these alternatives. ∎

There is no inversion of $\Delta$ in this criterion. It remains valid when $p\mid\Delta$. Primes dividing $g_B$ require the actual integer paid coefficients; unpaid Gaussian residues cannot be substituted.

At $p=2$, the integral equations of Sections 2–3 remain valid, but the displayed odd-prime normalization by $4096$ is not used. The final gcd continues to include that prime.

At $17$, the calculation above evaluates this test, rather than leaving it formal. In the scaled source coordinate,


$$
(u_0,u_1)=(0,15),
\qquad
(v_0,v_1)=(3\alpha^2,2\alpha^2).
$$


Hence


$$
\mathfrak m_V=6\alpha^2\ne0.
$$


Because $17\mid d_K$,


$$
(y_0,y_1)=(a_K,0)\pmod{17},
$$


and


$$
\mathfrak m_K=2a_K\ne0.
$$


This recovers


$$
17\nmid\mathfrak J^0
$$


with the complete arc included.

### 7.2 One concrete follow-on lemma

Define the explicitly tested divisor


$$
\mathcal S_N=
\prod_{\substack{
p\mid U_N,\ p\ {\rm odd}\\
\mathfrak m_V(p,N)\ne0,\ \mathfrak m_K(p,N)\ne0
}}
p^{v_p(U_N)}.
\tag{7.3}
$$


Each test uses:

* the original boundary $(T_0^\pm,T_1^\pm)=(0,1)$;
* at most $2p$ terms of the two displayed integer recurrences modulo $p$;
* the fixed complete source and endpoint coefficient rows;
* the actual paid Gaussian coefficients;
* the reduced complete arc $a_K/d_K$.

Proposition 7.1 proves


$$
\gcd(\mathcal S_N,\mathfrak J_N^0)=1.
$$


Consequently,


$$
\mathfrak J_N^0\le\frac{U_N}{\mathcal S_N},
\qquad
\mathfrak J_N\le
\mu_N\frac{U_N}{\mathcal S_N}.
$$


More precisely,


$$
\boxed{
\frac{\mathcal S_N}{\gcd(\mathcal S_N,\mu_N)}\mid q_N.
}
\tag{7.4}
$$



The following is a concrete sufficient follow-on obligation.

> **Separated-prime mass lemma — open.**  
> Prove that there are fixed $\delta_0>0$ and $C$ such that, at every sufficiently large original index,
> 

$$
> \boxed{
> \log\mathcal S_N\ge\delta_0\log U_N-CN.
> }
> \tag{7.5}
>
$$



This is stronger than merely requiring some nonvanishing minors. It asks for a positive proportion of the actual prime-power mass of $U_N$ to lie in the explicitly separated branches.

If (7.5) were proved, then $\mu_N\le D_N<256^N$ would give


$$
\mathfrak J_N\le e^{C'N}U_N^{1-\delta_0},
$$


which is the requested joint estimate. Also,


$$
q_N\ge e^{-C'N}U_N^{\delta_0}.
$$


Since


$$
\log U_N=2N\log N+O(N)
$$


and $\epsilon_N\asymp R^{-2N}$,


$$
q_N\epsilon_N\longrightarrow\infty
\qquad(N\in\mathcal N).
$$



This conditional deduction is rigorous. The mass lemma is not proved.

### 7.3 Precise remaining obstruction

The evaluated prime-$17$ theorem controls one genuine component of the actual joint divisor. It does not bound the product of the exceptional prime powers at the other primes.

In particular:

1. Nonzero minors at one fixed prime do not imply nonzero minors at arbitrary primes.
2. A vanishing first-digit minor allows an exceptional branch; it gives no bound on its higher $p$-adic depth.
3. Gaussian residue data cannot be held fixed across index lifts without proof. The uniform Gaussian behavior at $17$ was proved explicitly; no such uniform behavior is assumed elsewhere.
4. The integer joint-transfer identity (3.14) is not a new small-height certificate. Its determinant is the complete output already under investigation.
5. Bounded forcing and unimodularity still give no aggregate selected-content estimate. The new result uses the original boundary to obtain evaluated affine residue formulas; it does not contradict A3’s arbitrary-initial-state counterexample.

Thus neither the all-prime exceptional mass nor a strict saving in the coefficient of $N\log N$ has been controlled.

---

## 8. Bounded exact arithmetic receipt

No new full normalization, midpoint expansion, large prime-period table, or original-degree polynomial is needed to check the new theorem.

The following receipt is proposed for independent authorship and inspection. It has not been executed here.

### 8.1 Bounded inputs

1. Moduli $17$ and $289$.
2. The thirteen weights (3.1).
3. The already established fixed local recurrences for
   $r_k,s_k,\kappa_k$, evaluated only at $n=9\pmod{17}$.
4. The new alternating recurrence (3.6), through $k=12$.
5. The two boundary recurrences
   

$$
T_0^\pm=0,\quad T_1^\pm=1,\quad
   T_{j+1}^\pm=\pm4jT_j^\pm+T_{j-1}^\pm+2,
$$


   only through $j=26$, modulo $17$.
6. The two Gaussian recurrences over $\mathbb F_{17}$, only through return of their initial pairs.
7. The degree-three polynomials $L(x)$ and $A_K(x)$ in Section 4.

All modular sequence calculations use only small residues. No actual $h,\lambda,G,q$ normalization is an input.

### 8.2 Expected verifiable outputs

**Source and endpoint boundary values**


$$
\begin{array}{c|rrrr}
j&8&9&25&26\\ \hline
T_j^-&2&11&15&7\\
T_j^+&14&16&10&12
\end{array}
\pmod{17}.
$$



**Fixed local evaluations**


$$
(\mathsf A,\mathsf B,\mathsf C_U,\mathsf C_E)
\equiv(7,1,11,0)\pmod{17}.
$$



**Alternating local return**


$$
(\omega_0,\ldots,\omega_{12})
\equiv(0,0,2,3,8,8,2,13,6,1,8,1,2).
$$



**Gaussian outputs**


$$
(a_N,b_N,a_{N-1},b_{N-1})
\equiv(1,0,-1,2)\pmod{17}
$$


for $9\mid N$, justified by return of the displayed initial pairs.

**Original-index exponent residues**


$$
9^{18}\equiv166,\qquad 9^{32}\equiv103\pmod{289},
$$


and the symbolic affine residual


$$
2\cdot166\cdot103^u-
\bigl(9+17(2+3u)\bigr)\equiv0\pmod{289},
$$


where the last identity is checked using
$(1+6\cdot17)^u\equiv1+6u\cdot17\pmod{289}$, not by enumerating $u$.

**Arc polynomial identities**


$$
A_K-13L-45(3x-65)=0,
$$




$$
27L-(3x-65)(9x^2-120x-269)+23560=0,
$$


with zero coefficient arrays.

**Final modular residuals**


$$
U-2\ell,\qquad
g_B^2V-(12+8\ell),\qquad
E_K-(13+10\ell)
$$


all zero modulo $17$, with the Gaussian unit condition recorded separately.

Such a receipt would verify the small arithmetic used in the proof. The extension to every original index comes from the binomial lift identity, the proved Gaussian recurrence returns, and the exact original-index exponent formula—not from finite extrapolation.

It would not prove the separated-prime mass lemma, the requested ALL-prime joint estimate, a final-$q$ asymptotic, or irrationality.

---

## 9. Final conclusions

### New proved statements

For the unchanged original family:

1. The complete exponential endpoint admits the integral coordinate
   

$$
\mathcal E_j=(-1)^j-2j\Phi_j,\qquad
   \Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j,
$$


   with the original boundary and every alternating forcing term retained.

2. The complete source and endpoint columns admit the integer joint transfer of Section 3, including both arcs and all constant columns. No prime dividing $2\Delta$ is removed by inversion.

3. The complete $K$-arc reduces from an explicit cubic fraction, and cancellation in that fraction divides
   

$$
31\,806\,000.
$$



4. The evaluated original-source congruences
   

$$
U\equiv4+6u,\qquad
   g_B^2V\equiv11+7u,\qquad
   E_K\equiv16+13u\pmod{17}
$$


   hold for every original $u$.

5. Consequently,
   

$$
17\nmid c,\qquad 17\nmid\gcd(U,E_K),
$$


   and the **actual complete joint divisor** satisfies
   

$$
v_{17}\gcd(U,VY)
   =\min\{v_{17}(U),\,v_{17}(D)-v_{17}(2N-9)\}.
$$


   This bounds its $17$-primary part by the actual excess column clearing.

6. The explicit two-minor test produces a genuine surviving divisor of the actual primitive denominator, equation (7.4).

### Conditional implication

A positive prime-power mass estimate for the explicitly separated branches would imply


$$
\gcd(U_N,V_NY_N)\le e^{CN}U_N^{1-\delta_0},
$$


and hence


$$
q_N\epsilon_N\to\infty
$$


at the same infinite original indices. This would retire this signed producer only.

### Exact remaining bottleneck

What remains unproved is an **aggregate ALL-prime bound**: enough of the prime-power mass of $U_N$ must be excluded from the simultaneous source-content and complete-endpoint cancellation branches. The present evaluated prime-$17$ separation does not supply that mass, and no control of the remaining exceptional primes or their higher depths has been established.

Throughout, the actual content


$$
h=g_B^2c,
$$


the least aggregate $\lambda$, the complete-column clearer $D$, the final ALL-prime $G$, the actual primitive denominator


$$
q=\lambda M/G,
$$


and the positive whole error


$$
q(e+\pi)-p=q\epsilon_N
$$


have remained in force.

**The new result is a proved original-source joint-divisor separation and an exact arc-denominator payment, not a strict-saving theorem, not producer retirement, and not a proof of rationality or irrationality of $e+\pi$.**
