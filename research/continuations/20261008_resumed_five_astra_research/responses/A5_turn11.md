> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A canonical two-endpoint return for the original signed producer

## New numerical return and exact factorization; the aggregate cancellation bound remains open

### Abstract and status

The original index set is unchanged:


$$
\mathcal N=\{N_u=9^{18+32u}:u\in\mathbb Z_{\ge0}\}.
$$


Every producer statement below concerns these same indices, with physical polynomial terminal $2N$.

This report does **not** prove or disprove the irrationality of $e+\pi$. It also does not establish the requested factorial-excess estimate


$$
\frac{\mathfrak J_N^0}{\gcd(\mathfrak J_N^0,N!)}
\le e^{CN},
\qquad
\mathfrak J_N^0=\gcd(U_N,V_Ny_{K,N}).
\tag{0.1}
$$



There is a new, fully proved numerical return. It is different from the closed coefficient Bézout elimination: its generators include the actual values $U_N$ and $y_{K,N}$, and its size estimate uses the original canonical source and endpoint, not arbitrary recurrence states.

Let $P_r^{\mathrm H},Q_r^{\mathrm H}$ be the integer Hermite endpoint sequences


$$
P_0^{\mathrm H}=Q_0^{\mathrm H}=1,\qquad
P_1^{\mathrm H}=3,\quad Q_1^{\mathrm H}=1,
$$




$$
Z_{r+1}=(4r+2)Z_r+Z_{r-1}.
\tag{0.2}
$$


For each original $N$, define


$$
\mathcal R_{r;N}
=d_{K,N}P_r^{\mathrm H}U_N+Q_r^{\mathrm H}y_{K,N},
\qquad 0\le r\le N.
\tag{0.3}
$$


The auxiliary polynomials producing these integers have degree $2r\le2N$; no producer terminal is enlarged.

The new conclusions are:

1. The two canonical returns at $r=N-1,N$ are nonzero, with evaluated signs and bounds:
   

$$
\boxed{
   \mathcal R_{N-1;N}<0<\mathcal R_{N;N},
   \qquad
   |\mathcal R_{N-1;N}|,\ |\mathcal R_{N;N}|
   <d_{K,N}36^N N!.
   }
   \tag{0.4}
$$



2. After paying the actual reduced arc denominator and the binary determinant factor,
   

$$
\boxed{
   \gcd(U_N,y_{K,N})
   =
   \gcd(\mathcal R_{N-1;N},\mathcal R_{N;N}).
   }
   \tag{0.5}
$$


   Thus, in particular,
   

$$
\gcd(U_N,y_{K,N})
   <d_{K,N}36^N N!
   =N!e^{O(N)}.
   \tag{0.6}
$$


   This is a numerical endpoint bound, not a coefficient-content statement. It is nevertheless only a **critical-scale size bound**, not the desired exponential endpoint bound.

3. Put
   

$$
s_{r;N}=\gcd(c_N,Q_r^{\mathrm H}),\qquad c_N=\gcd(U_N,V_N).
$$


   All divisions in the following exact original-family factorization are integral:
   

$$
\boxed{
   \mathfrak J_N^0
   =
   c_N\gcd\!\left(
   \frac{U_N}{c_N},
   \frac{\mathcal R_{N-1;N}}{s_{N-1;N}},
   \frac{\mathcal R_{N;N}}{s_{N;N}}
   \right).
   }
   \tag{0.7}
$$


   Consequently,
   

$$
\boxed{
   \mathfrak J_N^0
   <
   d_{K,N}36^N N!\,
   \frac{c_N}{\max(s_{N-1;N},s_{N;N})}.
   }
   \tag{0.8}
$$



The factor $c_N/\max(s_{N-1;N},s_{N;N})$ is not controlled sufficiently here. The accepted estimate


$$
\log c_N\le N\log N+O(N)
$$


therefore does not turn (0.8) into a strict intrinsic saving.

A concrete new follow-on lemma is identified in Section 7: an all-prime capture estimate for the actual source content $c_N$ by the two explicit adjacent Hermite denominators. That lemma would give


$$
\mathfrak J_N^0\le e^{O(N)}U_N^{3/4}
$$


and hence would retire this producer. It remains an open obligation.

The parent’s centered-$83$ deduction is checked below. It removes the endpoint factor at the collapsed row, but does not bound the source/Gaussian common depth.

No tools were used. The proposed bounded arithmetic check at the end concerns only the new small Hermite identities, not old source tables, the closed centered elimination, or enormous Gaussian recurrences.

---

## 1. The retained original objects and normalization

### 1.1 Source, Gaussian division, and actual content

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


where


$$
C_0=1,\qquad C_1=2t-1,\qquad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$



For an integer polynomial $H$, retain


$$
\eta(H)=\int_{-\infty}^{1}e^{t-1}H(t)\,dt
       =\sum_{r\ge0}[z^r]H(1-z)\,r!,
$$


and


$$
E(H)=\sum_{r=0}^{\deg H}(-1)^rr![t^r]H.
$$



At an original $N$, put


$$
d=a_Nb_{N-1}-a_{N-1}b_N,
$$




$$
g_B=\gcd(b_{N-1},b_N)>0,
\qquad
\alpha=\frac{b_{N-1}}{g_B},\quad
\beta=\frac{b_N}{g_B},\quad
\delta=\frac d{g_B}.
$$


These are the actual paid Gaussian divisions. Define


$$
F=\alpha C_N-\beta C_{N-1}.
$$


Then


$$
F(i)=F(-i)=\delta,\qquad \gcd(\alpha,\beta)=1.
$$



With


$$
\mathcal H(t)=t(1-t)(1+t^2)^2,\qquad
m=N-3,\qquad K=\mathcal H C_m^2,
$$


retain


$$
U=-\eta(K),\qquad V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$



The established content identity is


$$
h=\operatorname{cont}(W_{\rm raw})=g_B^2c,
$$


and hence


$$
\tau=\frac Uc,\qquad \nu=\frac Vc,\qquad
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2.
\tag{1.1}
$$


The supplied positivity proofs apply for $N\ge256$, and therefore throughout $\mathcal N$:


$$
U>0,\qquad V>0,\qquad M>0.
$$



No step below replaces $V$ by an unpaid raw square column.

### 1.2 Both complete arcs and the actual clearers

Set


$$
E_F=E(F^2),\qquad E_K=E(K),
$$




$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


Both integrands after monic division are integer polynomials of degree at most $2N-2$.

The least simultaneous clearer is


$$
D=\operatorname{lcm}\bigl(\operatorname{den}(R_F),
                         \operatorname{den}(R_K)\bigr),
$$


where each fraction is first reduced completely. Define


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$



Independently reduce the aggregate arc:


$$
\tau R_F+\nu R_K=\frac b\lambda,\qquad
\gcd(b,\lambda)=1,\quad\lambda>0.
$$


Then


$$
E=\tau E_F+\nu E_K,\qquad A=\lambda E-b,\qquad
G=\gcd(M,A).
$$


The actual primitive numerator and denominator are


$$
\boxed{
p=\frac AG,\qquad q=\frac{\lambda M}{G}.
}
\tag{1.2}
$$


The gcd $G$ is over **all primes**. Since $\gcd(A,\lambda)=1$, no further denominator factor is concealed.

The exact reconciliation remains


$$
\tau X+\nu Y=\frac D\lambda A,
$$




$$
\gcd(D\tau\delta^2,\tau X+\nu Y)=\frac D\lambda G.
\tag{1.3}
$$


Also,


$$
D\mid L_{\rm aff}:=\operatorname{lcm}(1,\ldots,2N-1),
\qquad D<256^N.
\tag{1.4}
$$


The raw-interface identity is unchanged:


$$
\gcd(A_{\rm raw},B_{\rm raw})
=\frac{L_{\rm aff}h}{\lambda}G.
$$



### 1.3 The newly supplied exact reduced $K$-arc

Write


$$
\ell=2N-6=2m,\qquad x=\ell^2,
$$


and retain


$$
L(x)=(x-1)(x-9)(x-25),
$$




$$
A_K(x)=13x^3-455x^2+3502x-5850.
$$


Then


$$
R_K=\frac{A_K(x)}{30L(x)}.
$$



Let


$$
\varepsilon_5=\mathbf1_{u\equiv1\pmod5},
$$




$$
\varepsilon_{19}=\mathbf1_{u\equiv3\pmod9},
$$




$$
\varepsilon_{31}=\mathbf1_{u\equiv5\text{ or }7\pmod{15}}.
$$


The independent signed arc audit supplies the exact original-domain formula


$$
\boxed{
g_{\rm arc}
=90\cdot5^{\varepsilon_5}
       19^{\varepsilon_{19}}
       31^{\varepsilon_{31}}.
}
\tag{1.5}
$$


Its proof uses the fixed all-prime cancellation cap, followed by the exact valuations at the five possible cancellation primes. The original exponent congruences, rather than finite extrapolation, give the $19$- and $31$-branches.

Thus the actual reduced column is


$$
a_K=\frac{A_K(x)}{g_{\rm arc}},\qquad
d_K=\frac{30L(x)}{g_{\rm arc}}
=\frac{L(x)}
 {3\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}}}.
\tag{1.6}
$$


In particular,


$$
\frac{L(x)}{285}\le d_K\le\frac{L(x)}3
<\frac{64}{3}N^6.
\tag{1.7}
$$


The possible values of $g_{\rm arc}$ are


$$
90,\quad450,\quad1710,\quad2790,\quad8550.
$$


The size bound $g_{\rm arc}\le8550$ is not a divisibility assertion by $8550$; the uniform divisibility cap from the exact formula is $265050$.

Define


$$
y_K=d_KE_K-a_K,\qquad
\mu=\frac D{d_K}.
$$


Then


$$
Y=\mu y_K,\qquad \gcd(d_K,y_K)=1.
\tag{1.8}
$$


The last equality follows directly from $\gcd(a_K,d_K)=1$. It will be used below, with no exceptional denominator prime omitted.

For


$$
\mathfrak J^0=\gcd(U,Vy_K),\qquad
\mathfrak J=\gcd(U,VY),
$$


the exact relations are


$$
\mathfrak J^0\mid\mathfrak J\mid\mu\mathfrak J^0,
\qquad
\mathfrak J^0=c\gcd(\tau,y_K),
\qquad
\mathfrak J=c\gcd(\tau,Y).
\tag{1.9}
$$



Moreover,


$$
\boxed{\frac U{\mathfrak J}\mid q.}
\tag{1.10}
$$


For completeness, at a prime where


$$
v_p(\tau)>v_p(Y),
$$


the coprimality $\gcd(\tau,\nu)=1$ gives


$$
v_p(\tau X+\nu Y)=v_p(Y).
$$


Reduction of the fraction with denominator $D\tau\delta^2$ therefore leaves at least


$$
v_p(\tau)-v_p(Y)
$$


powers of $p$ in the actual denominator. This proves (1.10) at every prime, including primes dividing $D,\delta,g_B$, or $\Delta$.

### 1.4 The unchanged positive whole error

The polynomial used by the producer is


$$
P_N(t)=\frac{F(t)^2+(V/U)K(t)}{\delta^2}.
$$


Its normalization gives $\eta(P_N)=1$, and $P_N(\pm i)=1$. Hence


$$
\epsilon_N
=\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0,
$$


and


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0.
}
\tag{1.11}
$$



The previously established estimates are reused at their stated scope:


$$
\epsilon_N\asymp R^{-2N},\qquad
R=1+\sqrt2+\sqrt{2+2\sqrt2},
$$




$$
\log U_N=2N\log N+O(N),\qquad
\log c_N\le N\log N+O(N).
\tag{1.12}
$$


The closed source-content and critical Bessel/midpoint calculations are not repeated.

The complete rational error enclosure is retained:


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


and, with $j_r=(1-4r^2)^{-1}=j_{-r}$,


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
q_NJ_N
=\frac{\lambda_N}{G_N}
(\tau_NJ_F+\nu_NJ_K).
\tag{1.13}
$$


Neither positive summand is discarded in any conclusion about the producer.

---

## 2. The complete centered interface and the $83$-branch

### 2.1 Original boundaries and complete centered columns

The original integral coordinates are


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



The complete centered polynomials, already reduced and checked in the supplied twelve-residual receipt, are


$$
\begin{aligned}
\mathcal P(x)&=-8x^3-1116x^2-8150x+151,\\
\mathcal Q(x)&=76x^2+2408x+5637,\\
\mathcal F(x)&=4x^2+492x+5463,\\
\mathcal G(x)&=4x^2+556x-3325.
\end{aligned}
$$


Define, at $x=\ell^2$,


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
=\mathcal G+\mathcal P-2(\ell+1)\mathcal Q.
$$


Then


$$
16U=\widetilde{\mathsf C}_U
-\widetilde{\mathsf A}\Theta_\ell
-\widetilde{\mathsf B}\Theta_{\ell-1},
\tag{2.2}
$$




$$
16E_K=\widetilde{\mathsf C}_E
+\widetilde{\mathsf A}\Phi_\ell
+\widetilde{\mathsf B}\Phi_{\ell-1},
\tag{2.3}
$$


and the actual reduced endpoint is


$$
16y_K
=d_K\bigl(
\widetilde{\mathsf C}_E+
\widetilde{\mathsf A}\Phi_\ell+
\widetilde{\mathsf B}\Phi_{\ell-1}
\bigr)-16a_K.
\tag{2.4}
$$



In particular,


$$
\widetilde{\mathsf C}_U(0)=5312,\qquad
\widetilde{\mathsf C}_E(0)=-14448.
$$



The supplied certificate is evidence for twelve fixed polynomial identities, including both boundary constants and the six-step reconciliation. Its stated scope is not an aggregate gcd estimate. The different external audit of the full coefficient-content theorem remains pending; this report does not describe itself or that theorem as independently externally certified.

### 2.2 Check of the parent’s exact $83$-deduction

The modular computations are short:


$$
9^2\equiv-2,\quad 9^4\equiv4,\quad 9^{16}\equiv7\pmod{83}.
$$


Therefore


$$
9^{21}=9^{16}9^4 9\equiv7\cdot4\cdot9\equiv3\pmod{83},
$$


and $9^{41}\equiv1$. Since $41$ is prime and $9\not\equiv1$, the order of $9$ modulo $83$ is exactly $41$.

Consequently,


$$
83\mid\ell
\iff N\equiv3\pmod{83}
\iff18+32u\equiv21\pmod{41}.
$$


As $32^{-1}\equiv9\pmod{41}$,


$$
\boxed{83\mid\ell\iff u\equiv27\pmod{41}.}
\tag{2.5}
$$



On this branch, the two centered row coefficients vanish modulo $83$, so the complete endpoint constant gives


$$
16E_K\equiv-14448\equiv-6\pmod{83}.
$$


Hence


$$
E_K\equiv10\pmod{83}.
$$



At $x\equiv0\pmod{83}$,


$$
30L(x)\equiv-6750\not\equiv0\pmod{83},
$$


so the actual reduced $d_K$ is a unit at $83$. Moreover,


$$
R_K\equiv\frac{-5850}{-6750}
=\frac{13}{15}\equiv23\pmod{83}.
$$


It follows that


$$
\frac{y_K}{d_K}=E_K-R_K\equiv10-23=-13\not\equiv0\pmod{83}.
$$


Thus


$$
\boxed{
u\equiv27\pmod{41}\quad\Longrightarrow\quad83\nmid y_K.
}
\tag{2.6}
$$



This proves precisely


$$
v_{83}(\mathfrak J^0)=v_{83}(c)
$$


on the collapsed branch. It proves no upper bound on $v_{83}(U)$, $v_{83}(V)$, or $v_{83}(c)$. The row-content depth one cannot be substituted for any of those numerical depths.

---

## 3. A new canonical integer endpoint basis

The following elementary construction is used as a new auxiliary return for the complete $K$-column. It does not replace the producer.

### 3.1 Paid Hermite endpoint integers

For $r\ge0$, let


$$
f_r(t)=\frac{t^r(1-t)^r}{r!}.
$$


Although $f_r$ is rational-coefficient, all derivatives relevant to its endpoint antiderivative are integers. Indeed, put


$$
a_{r,j}=\frac{(r+j)!}{j!(r-j)!},
\qquad 0\le j\le r.
\tag{3.1}
$$


These are integers.

Define


$$
P_r^{\mathrm H}=\sum_{j=0}^{r}a_{r,j},
\qquad
Q_r^{\mathrm H}=\sum_{j=0}^{r}(-1)^{r+j}a_{r,j}.
\tag{3.2}
$$


The division by $r!$ in $f_r$ is therefore fully paid in these endpoint integers.

To verify their origin, let


$$
\mathcal A(H)=\sum_{k=0}^{\deg H}(-1)^kH^{(k)}.
$$


Then


$$
\mathcal A(H)'+\mathcal A(H)=H,
$$


so


$$
\mathcal A(H)(0)=E(H),\qquad
\mathcal A(H)(1)=\eta(H).
$$


Direct endpoint differentiation of $f_r$, using $f_r(1-t)=f_r(t)$, gives


$$
E(f_r)=(-1)^rP_r^{\mathrm H},
\qquad
\eta(f_r)=(-1)^rQ_r^{\mathrm H}.
\tag{3.3}
$$



### 3.2 Recurrence and evaluated determinant

Let


$$
b_r(z)=\sum_{j=0}^r a_{r,j}z^j.
$$


The factorial coefficients satisfy


$$
a_{r+1,j}=(4r+2)a_{r,j-1}+a_{r-1,j}.
\tag{3.4}
$$


For interior indices, this follows by taking out the common factor


$$
\frac{(r+j-1)!}{j!(r+1-j)!}
$$


and using


$$
(r+j)(r+j+1)-(r+1-j)(r-j)=j(4r+2).
$$


The endpoint coefficients satisfy the same identity with out-of-range coefficients interpreted as zero.

Thus


$$
b_{r+1}(z)=(4r+2)z\,b_r(z)+b_{r-1}(z).
$$


Evaluating at $z=1,-1$ proves (0.2):


$$
P_{r+1}^{\mathrm H}=(4r+2)P_r^{\mathrm H}+P_{r-1}^{\mathrm H},
$$




$$
Q_{r+1}^{\mathrm H}=(4r+2)Q_r^{\mathrm H}+Q_{r-1}^{\mathrm H}.
\tag{3.5}
$$



All these integers are positive and odd. The determinant changes sign at each step and starts at $2$, hence


$$
\boxed{
P_{r+1}^{\mathrm H}Q_r^{\mathrm H}
-P_r^{\mathrm H}Q_{r+1}^{\mathrm H}
=2(-1)^r.
}
\tag{3.6}
$$


Also, the recurrence with $Q_0^{\mathrm H}=Q_1^{\mathrm H}=1$ gives


$$
\boxed{\gcd(Q_r^{\mathrm H},Q_{r+1}^{\mathrm H})=1.}
\tag{3.7}
$$



### 3.3 Exact signed error and explicit bounds

Let


$$
I_r^{\mathrm H}=\int_0^1e^t f_r(t)\,dt.
$$


From (3.3),


$$
I_r^{\mathrm H}=(-1)^r(eQ_r^{\mathrm H}-P_r^{\mathrm H}),
$$


or


$$
\boxed{
P_r^{\mathrm H}-eQ_r^{\mathrm H}
=(-1)^{r+1}I_r^{\mathrm H}.
}
\tag{3.8}
$$



The beta integral evaluates the required magnitude:


$$
\int_0^1 f_r(t)\,dt=\frac{r!}{(2r+1)!}.
$$


Since $1<e^t<3$ on $0<t<1$,


$$
\boxed{
\frac{r!}{(2r+1)!}
<I_r^{\mathrm H}
<\frac{3r!}{(2r+1)!}.
}
\tag{3.9}
$$



There is also a convenient integer-height bound. Relative to the last coefficient,


$$
\frac{a_{r,r-j}}{a_{r,r}}
=\frac1{j!}\prod_{k=0}^{j-1}\frac{r-k}{2r-k}
\le\frac{2^{-j}}{j!}.
$$


Therefore


$$
0<Q_r^{\mathrm H}\le P_r^{\mathrm H}
<2\frac{(2r)!}{r!}
\le2\cdot4^r r!.
\tag{3.10}
$$



These are explicit estimates, not an appeal to an unevaluated approximation theorem.

---

## 4. The complete centered canonical return

### 4.1 Integer identity in the actual numerical generators

For fixed original $N$ and $0\le r\le N$, define


$$
\boxed{
\mathcal R_{r;N}
=d_KP_r^{\mathrm H}U+Q_r^{\mathrm H}y_K.
}
\tag{4.1}
$$


This is an integer linear combination of the actual source and the actual reduced endpoint.

It also has a complete centered forced-return representation. Define


$$
\Psi_j^{(r;N)}
=Q_r^{\mathrm H}\Phi_j-P_r^{\mathrm H}\Theta_j.
$$


The original boundary values give


$$
\Psi_0^{(r;N)}=0,\qquad
\Psi_1^{(r;N)}=Q_r^{\mathrm H}-P_r^{\mathrm H},
$$


and both original forcing terms remain:


$$
\boxed{
\Psi_{j+1}^{(r;N)}+4j\Psi_j^{(r;N)}
-\Psi_{j-1}^{(r;N)}
=
2\bigl(Q_r^{\mathrm H}(-1)^j-P_r^{\mathrm H}\bigr).
}
\tag{4.2}
$$


Substitution into the complete centered columns yields


$$
\boxed{
\begin{aligned}
16\mathcal R_{r;N}
={}&d_K\Bigl(
P_r^{\mathrm H}\widetilde{\mathsf C}_U
+Q_r^{\mathrm H}\widetilde{\mathsf C}_E
+\widetilde{\mathsf A}\Psi_\ell^{(r;N)}
+\widetilde{\mathsf B}\Psi_{\ell-1}^{(r;N)}
\Bigr)\\
&-16Q_r^{\mathrm H}a_K.
\end{aligned}}
\tag{4.3}
$$



This is the new canonical return in the smaller centered coordinates. It retains:

- the source constant $\widetilde{\mathsf C}_U$;
- the different endpoint constant $\widetilde{\mathsf C}_E$;
- the full reduced arc term $-16Q_r^{\mathrm H}a_K$;
- the original constant and alternating forcings;
- the original boundaries at $j=0,1$.

Unlike the old coefficient Bézout identity, (4.1) already has numerical output generators. The next step supplies a nonzero, explicitly bounded right side for these actual generators.

### 4.2 Evaluating the sign and size of the return

Put


$$
I_K=\int_0^1e^tK(t)\,dt,
$$


and keep the complete endpoint contribution


$$
T_K=I_K+R_K
=\int_0^1K(t)\left(e^t+\frac4{1+t^2}\right)\,dt.
\tag{4.4}
$$


Since


$$
I_K=e\eta(K)-E_K=-eU-E_K,
$$


we have


$$
E_K=-eU-I_K.
$$


Using (3.8) in (4.1) gives the evaluated signed expression


$$
\boxed{
\mathcal R_{r;N}
=d_K\left(
(-1)^{r+1}U I_r^{\mathrm H}
-Q_r^{\mathrm H}T_K
\right).
}
\tag{4.5}
$$



This is not being used as an unevaluated sum. We now bound both terms explicitly and establish the required nonvanishing.

On $[0,1]$, $0\le C_m^2\le1$, so


$$
0<T_K<7\int_0^1\mathcal H(t)\,dt.
$$


A direct degree-six integration gives


$$
\int_0^1\mathcal H(t)\,dt=\frac{61}{210}.
$$


Hence


$$
\boxed{
0<T_K<\frac{61}{30},
\qquad
0<I_K<\frac{61}{70}<1.
}
\tag{4.6}
$$



We also need coarse explicit bounds for $U$. They are elementary and do not repeat the closed asymptotic analysis.

The alternating coefficient formula for shifted Chebyshev polynomials gives


$$
\|C_m(1-z)\|_1=T_m(3)<6^m.
$$


Moreover,


$$
\mathcal H(1-z)=4z-12z^2+16z^3-12z^4+5z^5-z^6,
$$


whose coefficient $1$-norm is $50$. The physical degree is $2N$. Positive factorial weighting therefore gives


$$
\boxed{
U<50\cdot36^{N-3}(2N)!.
}
\tag{4.7}
$$



For a lower bound, on $s\ge0$,


$$
|C_m(-s)|=T_m(1+2s)\ge2^{2m-1}s^m.
$$


Also


$$
s(1+s)(1+s^2)^2\ge s^6.
$$


Consequently,


$$
-E_K
=\int_0^\infty e^{-s}
s(1+s)(1+s^2)^2C_m(-s)^2\,ds
\ge2^{4N-14}(2N)!.
$$


Using $eU=-E_K-I_K$, (4.6), and $e<3$, one obtains, for $N\ge4$,


$$
\boxed{
U>2^{4N-16}(2N)!.
}
\tag{4.8}
$$



Every original $N$ is odd. Thus $N-1$ is even, and (4.5) immediately gives


$$
\mathcal R_{N-1;N}
=-d_K\left(UI_{N-1}^{\mathrm H}
+Q_{N-1}^{\mathrm H}T_K\right)<0.
\tag{4.9}
$$



For $r=N$, equations (3.9), (3.10), (4.6), and (4.8) give


$$
UI_N^{\mathrm H}
>2^{4N-16}\frac{N!}{2N+1},
$$


whereas


$$
Q_N^{\mathrm H}T_K
<\frac{61}{15}4^N N!.
$$


The first lower bound exceeds the second upper bound whenever


$$
4^N>\frac{61}{15}2^{16}(2N+1).
$$


This holds for $N\ge16$, hence on the full original domain. Therefore


$$
\mathcal R_{N;N}>0.
\tag{4.10}
$$



Finally,


$$
\begin{aligned}
\frac{|\mathcal R_{N-1;N}|}{d_K}
&<
150\cdot36^{N-3}(2N)!
\frac{(N-1)!}{(2N-1)!}
+\frac{61}{15}4^{N-1}(N-1)!\\
&=
N!\left(
300\cdot36^{N-3}
+\frac{61}{15N}4^{N-1}
\right)
<36^N N!.
\end{aligned}
\tag{4.11}
$$


Since $\mathcal R_{N;N}>0$, dropping its subtracted positive term gives


$$
\frac{\mathcal R_{N;N}}{d_K}
<UI_N^{\mathrm H}
<
\frac{150}{2N+1}36^{N-3}N!
<36^N N!.
\tag{4.12}
$$



This proves the new numerical return theorem:


$$
\boxed{
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
\qquad
|\mathcal R_{N-1;N}|,\ |\mathcal R_{N;N}|
<d_K36^N N!.
}
\tag{4.13}
$$



The sign proof depends on the actual canonical boundaries through


$$
E_K=-eU-I_K.
$$


It is not valid for arbitrary affine recurrence states.

---

## 5. Exact all-prime factorization and every paid division

### 5.1 Paying the determinant’s binary factor in the original objects

The determinant in (3.6) is $2$, not $1$. Its binary factor must therefore be handled rather than ignored.

On the original domain, $m=N-3$ is even. The coefficient congruence


$$
C_m^2\equiv1\pmod{16}
$$


gives


$$
E_K\equiv E(\mathcal H)=-903\equiv1\pmod8,
$$


and


$$
U\equiv-\eta(\mathcal H)=332\equiv12\pmod{16}.
$$


Thus


$$
v_2(U)=2.
\tag{5.1}
$$



The exact arc formula has $v_2(g_{\rm arc})=1$ and $d_K$ odd. Since $x\equiv0\pmod{16}$,


$$
\frac{A_K(x)}2\equiv-2925\equiv3\pmod8,
$$


while


$$
\frac{30L(x)}2=15L(x)\equiv1\pmod8.
$$


All remaining arc cancellation is by odd factors, so in the $2$-adic integers


$$
R_K=\frac{a_K}{d_K}\equiv3\pmod8.
$$


Therefore


$$
\frac{y_K}{d_K}=E_K-R_K\equiv1-3=6\pmod8,
$$


and


$$
\boxed{v_2(y_K)=1.}
\tag{5.2}
$$



This calculation is a payment of the factor $2$ in the new exact determinant. It is not an unrelated fixed-prime table.

### 5.2 Exact factorization of the endpoint gcd

Let


$$
H_N=\gcd(U_N,y_{K,N}).
$$


Because $\gcd(d_K,y_K)=1$,


$$
\gcd(d_KU,y_K)=H_N.
$$


Write


$$
a=\frac{d_KU}{H_N},\qquad b=\frac{y_K}{H_N},
\qquad \gcd(a,b)=1.
$$


Then


$$
\frac{\mathcal R_{r;N}}{H_N}
=P_r^{\mathrm H}a+Q_r^{\mathrm H}b.
$$


By (3.6), any common divisor of two adjacent normalized returns divides $2$.

Equations (5.1)–(5.2) give $v_2(H_N)=1$, so $a$ is even and $b$ is odd. Since all $P_r^{\mathrm H},Q_r^{\mathrm H}$ are odd, both normalized returns are odd. Their gcd is therefore $1$.

Hence, at every original $N$,


$$
\boxed{
\gcd(U_N,y_{K,N})
=
\gcd(\mathcal R_{N-1;N},\mathcal R_{N;N}).
}
\tag{5.3}
$$



Together with (4.13), this proves


$$
\boxed{
\gcd(U_N,y_{K,N})
<d_{K,N}36^N N!
<\frac{64}{3}N^6 36^N N!.
}
\tag{5.4}
$$



No prime dividing $d_K$ was discarded: its absence from the endpoint gcd followed from the actual reduced column. No prime dividing $g_B,\delta$, or $\Delta$ was inverted.

### 5.3 Exact factorization after the actual source content is removed

Now put


$$
s_{r;N}=\gcd(c_N,Q_r^{\mathrm H}),
\qquad
\mathcal T_{r;N}=\frac{\mathcal R_{r;N}}{s_{r;N}}.
$$


The division is integral because $s_{r;N}\mid c_N\mid U_N$ and $s_{r;N}\mid Q_r^{\mathrm H}$.

Indeed,


$$
\boxed{
\mathcal T_{r;N}
=
d_K\frac{c_N}{s_{r;N}}P_r^{\mathrm H}\tau_N
+\frac{Q_r^{\mathrm H}}{s_{r;N}}y_{K,N}.
}
\tag{5.5}
$$


The two adjacent quotients


$$
\frac{Q_{N-1}^{\mathrm H}}{s_{N-1;N}},
\qquad
\frac{Q_N^{\mathrm H}}{s_{N;N}}
$$


are coprime, because they divide the coprime integers
$Q_{N-1}^{\mathrm H},Q_N^{\mathrm H}$.

Reducing (5.5) modulo $\tau_N$, and using an integer Bézout combination of these two coprime quotients, proves


$$
\gcd(\tau_N,\mathcal T_{N-1;N},\mathcal T_{N;N})
=\gcd(\tau_N,y_{K,N}).
$$


Therefore


$$
\boxed{
\mathfrak J_N^0
=
c_N\gcd\!\left(
\tau_N,\mathcal T_{N-1;N},\mathcal T_{N;N}
\right).
}
\tag{5.6}
$$



This is an exact factorization in the original family, at all primes and all depths. In particular,


$$
\boxed{
\mathfrak J_N^0
<
d_{K,N}36^N N!\,
\frac{c_N}{\max(s_{N-1;N},s_{N;N})}.
}
\tag{5.7}
$$



### 5.4 A numerical Bézout identity with the requested generators

The factorization can also be written as a genuine integer identity in $U_N,V_Ny_{K,N}$.

Choose integers $a_0,b_0$ with


$$
a_0U+b_0V=c.
$$


For either $r=N-1$ or $r=N$, put $s=s_{r;N}$. Then


$$
\boxed{
\begin{aligned}
\frac cs\,\mathcal R_{r;N}
={}&
\left(
d_KP_r^{\mathrm H}\frac cs
+a_0\frac{Q_r^{\mathrm H}}s\,y_K
\right)U\\
&+
b_0\frac{Q_r^{\mathrm H}}s\,V y_K.
\end{aligned}}
\tag{5.8}
$$


Every coefficient is an integer. The right side uses the actual required numerical generators. The left side is nonzero, has a proved sign, and satisfies


$$
\left|\frac cs\,\mathcal R_{r;N}\right|
<
\frac cs\,d_K36^N N!.
\tag{5.9}
$$



This is a new numerical certificate, not the earlier coefficient-row certificate. Its precise deficiency is also visible: the factor $c/s$ has not been paid sufficiently.

---

## 6. Why the new return does not yet retire the producer

### 6.1 The new bound remains at a critical scale

From (5.4),


$$
\gcd(\tau,y_K)\le\gcd(U,y_K)\le N!e^{O(N)}.
$$


Combining this only with the accepted source-content bound gives


$$
\log\mathfrak J^0
\le \log c+\log(N!)+O(N)
\le2N\log N+O(N).
$$


This has the same leading scale as


$$
\log U=2N\log N+O(N).
$$


There is no fixed positive $\delta_0$ in


$$
\mathfrak J^0\le e^{CN}U^{1-\delta_0}
$$


from these estimates alone.

The exact factorization (5.6) is stronger information than that critical upper bound, but the common arithmetic of its actual return values remains unresolved.

### 6.2 A size bound is not a factorial-excess payment

It is essential not to confuse


$$
|\mathcal R_{r;N}|\le N!e^{O(N)}
$$


with


$$
\mathcal R_{r;N}=N!B_N,\qquad |B_N|\le e^{O(N)},
$$


or with a prime-by-prime bound on its excess over $N!$.

No such divisibility by $N!$ has been proved. A prime $p>N$ can divide an integer of size $N!e^{O(N)}$, while receiving zero allowance from $N!$.

Accordingly, neither (5.4) nor (5.7) proves (0.1).

### 6.3 The remaining obstruction is arithmetic synchronization

The old coefficient Bézout identity paid row collapse. The new return additionally pays a genuine numerical height reduction for the original endpoint.

What remains is synchronization between:

- the actual source content $c=\gcd(U,V)$;
- the two adjacent canonical integers $Q_{N-1}^{\mathrm H},Q_N^{\mathrm H}$;
- the common divisors of the reduced returns in (5.6).

The coprimality


$$
\gcd(Q_{N-1}^{\mathrm H},Q_N^{\mathrm H})=1
$$


does not force a large part of $c$ into either one. Both can be units at a prime dividing $c$.

Likewise, neither the centered coefficient-content theorem nor the independent boundary lift directions imply that the numerical affine intersections are empty. The established original prime-$5$ exception already rules out that inference.

The $83$-deduction removes $y_K$ on its collapsed branch, but leaves the source factor $c$ there. It supplies no source-depth estimate.

---

## 7. A concrete new follow-on lemma and its conditional effect

The new return identifies a specific sufficient source-arithmetic target.

### 7.1 Two-column Hermite capture — open lemma

For the actual original objects, seek a constant $C$ such that


$$
\boxed{
\frac{c_N}
{\gcd(c_N,Q_{N-1}^{\mathrm H}Q_N^{\mathrm H})}
\le e^{CN}.
}
\tag{HC}
$$



This is an all-prime, all-depth assertion about the actual divided Gaussian source column $V_N$. It is not asserted for arbitrary affine states, and it is not inferred from coefficient primitivity.

Because the two Hermite denominators are coprime,


$$
\gcd(c_N,Q_{N-1}^{\mathrm H}Q_N^{\mathrm H})
=s_{N-1;N}s_{N;N}.
$$


Thus (HC) would imply


$$
\max(s_{N-1;N},s_{N;N})
\ge \sqrt{c_N}\,e^{-CN/2}.
$$


Equation (5.7) would then give


$$
\mathfrak J_N^0
\le d_{K,N}36^N N!\sqrt{c_N}\,e^{CN/2}.
$$


Using the accepted bound for $c_N$,


$$
\log\mathfrak J_N^0
\le\frac32N\log N+O(N)
=\frac34\log U_N+O(N).
$$


Hence


$$
\boxed{
\text{(HC)}\quad\Longrightarrow\quad
\mathfrak J_N^0\le e^{O(N)}U_N^{3/4}.
}
\tag{7.1}
$$



This would be a sufficiently strict intrinsic bound even without proving the stronger exact factorial-excess target.

A concrete route to (HC) would be an evaluated original-source integer return


$$
a_NU_N+b_NV_N
=Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}B_N,
\qquad
0<|B_N|\le e^{CN}.
\tag{7.2}
$$


Indeed, $c_N$ would divide the right side, so the quotient in (HC) would divide $B_N$. The coefficients and $B_N$ in (7.2) would have to be derived from the original canonical $\Theta$-boundary and the changing, actually divided $\alpha,\beta,\delta$. Merely choosing a Bézout representation of $c_N$ and naming the resulting quotient would not establish the estimate.

No proof or original-family counterexample to (HC) is supplied here.

### 7.2 Conditional effect on the actual primitive denominator

If (HC), or any other strict intrinsic estimate


$$
\mathfrak J_N^0\le e^{CN}U_N^{1-\delta_0},
\qquad \delta_0>0,
$$


were proved, then the actual denominator satisfies


$$
q_N\ge\frac{U_N}{\mathfrak J_N}
\ge\frac{U_N}{\mu_N\mathfrak J_N^0}
\ge e^{-O(N)}U_N^{\delta_0}.
$$


Using the unchanged positive whole error,


$$
\log(q_N\epsilon_N)
\ge2\delta_0N\log N-O(N)\longrightarrow+\infty.
$$


For the particular conditional saving (7.1),


$$
\log(q_N\epsilon_N)\ge\frac12N\log N-O(N).
\tag{7.3}
$$



These deductions concern


$$
q_N=\frac{\lambda_NM_N}{G_N}
$$


after actual content removal, least aggregate clearing, and the final all-prime gcd. They would retire this signed producer only. They would not prove either rationality or irrationality of $e+\pi$.

### 7.3 Literature scope

No general gcd theorem is imported. The fixed-$S$ obstruction in the supplied literature gate remains: an unremoved factorial has outside-$S$ logarithmic height


$$
\log(N!)-O(N).
$$


Neither the original factorial evaluations nor the new return values have been shown to satisfy the almost-$S$-unit hypotheses and exceptional-set exclusions required by the cited literature.

The new return uses only explicit integer endpoint algebra, integration by parts, the beta integral, and the original canonical boundaries.

---

## 8. Retained finite source, endpoint, and arc returns

For clarity, the new auxiliary return does not alter any of the original finite data.

Put $n=2N$. The thirteen weights remain


$$
(1,8,58,168,399,-176,-916,-176,399,168,58,8,1).
$$


The original local evaluator retains


$$
r_{k+1}=r_{k-1}+4(n-k)r_k,\qquad
s_{k+1}=s_{k-1}+4(n-k)s_k,
$$


and the complete inhomogeneous columns


$$
\kappa_{k+1}=\kappa_{k-1}+4(n-k)\kappa_k-2,
$$




$$
\omega_{k+1}=\omega_{k-1}+4(n-k)\omega_k-2(-1)^k,
\qquad 1\le k\le11,
$$


with the original initial values. Thus


$$
4096U=\mathsf C_U-\mathsf A\Theta_n-\mathsf B\Theta_{n-1},
$$




$$
4096E_K=\mathsf A\Phi_n+\mathsf B\Phi_{n-1}+\mathsf C_E,
$$


where the complete constants are


$$
\mathsf C_U=679936-\sum_{k=0}^{12}w_k(n-k)\kappa_k,
$$




$$
\mathsf C_E=-1849344+\sum_{k=0}^{12}w_k(n-k)\omega_k.
$$



The square source and endpoint remain


$$
V=\mathsf C_V-\mathsf P\Theta_n-\mathsf Q\Theta_{n-1},
$$




$$
E_F=\mathsf C_F^E-\mathsf P\Phi_n-\mathsf Q\Phi_{n-1},
$$


with


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
\tag{8.1}
$$


In particular, neither $-\delta^2$ nor $4\alpha\beta$ has been dropped.

For


$$
\Delta=\mathsf A\mathsf Q-\mathsf B\mathsf P,
$$


the original source return is


$$
z_n=4096\mathsf Q U-\mathsf B V,\qquad
z_{n-1}=\mathsf A V-4096\mathsf P U,
$$




$$
z_j=-\Delta\Theta_j+r_j,
$$




$$
z_{j-1}=z_{j+1}+4jz_j,\qquad
r_{j-1}=r_{j+1}+4jr_j-2\Delta,
$$


with


$$
r_n=\mathsf Q\mathsf C_U-\mathsf B\mathsf C_V,\qquad
r_{n-1}=\mathsf A\mathsf C_V-\mathsf P\mathsf C_U.
$$



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
\sigma_n=\mathsf Qk_E+\mathsf Bf_E,\qquad
\sigma_{n-1}=-\mathsf Pk_E-\mathsf Af_E,
$$




$$
w_{j-1}=w_{j+1}+4jw_j,\qquad
\sigma_{j-1}=\sigma_{j+1}+4j\sigma_j+2D\Delta(-1)^j.
$$


Its determinant is still


$$
z_nw_{n-1}-z_{n-1}w_n
=-4096\Delta(UX+VY).
\tag{8.2}
$$


No division by $\Delta$ is made.

Finally, the square arc retains its complete return


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
(1-j^2)^{-1},&j\ \text{even},
\end{cases}
$$


and the initial values at $j=0,1$ are zero. Thus


$$
R_F=\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
                  -2\alpha\beta\xi_{n-1}}2.
\tag{8.3}
$$



The six-step centered reconciliation remains an integer unimodular coordinate change inside this same finite system. No closed polynomial comparison is requested again.

---

## 9. New bounded exact-arithmetic check

No calculation at an enormous original $N$ is proposed.

The following optional check concerns only the new fixed-size auxiliary identities. Its finite scope must not be confused with the uniform proofs above.

### Inputs

1. Integers $r=0,1,2,3,4$.
2. Factorials only through $8!$.
3. The rational polynomials
   

$$
f_r(t)=t^r(1-t)^r/r!,
$$


   of degree at most $8$.
4. The coefficient definition
   

$$
a_{r,j}=(r+j)!/[j!(r-j)!].
$$


5. Formal centered symbols
   

$$
\widetilde{\mathsf A},\widetilde{\mathsf B},
   \widetilde{\mathsf C}_U,\widetilde{\mathsf C}_E,
   \Theta_\ell,\Theta_{\ell-1},\Phi_\ell,\Phi_{\ell-1},
   d_K,a_K,P,Q,
$$


   for checking only the linear substitution in (4.3).

No old source arrays, prime-$5$ or prime-$17$ tables, closed centered polynomial eliminations, or original Gaussian recurrences are inputs.

### Expected verifiable outputs

The coefficient arrays of $b_r(z)$, in increasing degree, are


$$
\begin{array}{c|l}
r&b_r\\ \hline
0&(1)\\
1&(1,2)\\
2&(1,6,12)\\
3&(1,12,60,120)\\
4&(1,20,180,840,1680).
\end{array}
$$



The endpoint pairs are


$$
\boxed{
(P_r^{\mathrm H},Q_r^{\mathrm H})_{r=0}^4
=
(1,1),(3,1),(19,7),(193,71),(2721,1001).
}
$$



Exact factorial evaluation of $E(f_r)$ and $\eta(f_r)$ gives


$$
E(f_r)=(-1)^rP_r^{\mathrm H},\qquad
\eta(f_r)=(-1)^rQ_r^{\mathrm H}.
$$



The four adjacent determinant outputs are


$$
2,\quad-2,\quad2,\quad-2.
$$



Exact polynomial integration gives


$$
\int_0^1 f_r(t)\,dt=\frac{r!}{(2r+1)!}.
$$



Finally, substitution of


$$
16U=\widetilde{\mathsf C}_U
-\widetilde{\mathsf A}\Theta_\ell
-\widetilde{\mathsf B}\Theta_{\ell-1},
$$




$$
16y_K=d_K\bigl(
\widetilde{\mathsf C}_E+
\widetilde{\mathsf A}\Phi_\ell+
\widetilde{\mathsf B}\Phi_{\ell-1}
\bigr)-16a_K
$$


into


$$
16(d_KPU+Qy_K)
$$


must give exactly the right side of (4.3), with


$$
\Psi_j=Q\Phi_j-P\Theta_j.
$$



These finite outputs check the small arithmetic and the new substitution identity. Uniformity in $r$ and in the original $N$ comes from the proofs in Sections 3–5, not from extrapolation from these samples. This check would not prove (HC), (0.1), producer retirement, or any assertion about the rationality of $e+\pi$.

---

## 10. Final conclusions

### New proved statements

The original complete centered source and endpoint admit the canonical integer return


$$
\mathcal R_{r;N}
=d_KP_r^{\mathrm H}U_N+Q_r^{\mathrm H}y_{K,N},
$$


with the fully retained forced representation (4.3).

At the same original $N$, the two returns at $r=N-1,N$ satisfy


$$
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
\qquad
|\mathcal R_{N-1;N}|,\ |\mathcal R_{N;N}|
<d_K36^N N!.
$$


Their all-prime gcd is exactly the actual endpoint gcd:


$$
\gcd(\mathcal R_{N-1;N},\mathcal R_{N;N})
=\gcd(U_N,y_{K,N}).
$$



After the actual source content is removed, the exact factorization is


$$
\mathfrak J_N^0
=
c_N\gcd\!\left(
\frac{U_N}{c_N},
\frac{\mathcal R_{N-1;N}}{\gcd(c_N,Q_{N-1}^{\mathrm H})},
\frac{\mathcal R_{N;N}}{\gcd(c_N,Q_N^{\mathrm H})}
\right).
$$



The parent’s exceptional-$83$ deduction is correct:


$$
u\equiv27\pmod{41}\Longrightarrow83\nmid y_{K,N}.
$$


It leaves $v_{83}(c_N)$ unresolved.

### Exact remaining bottleneck

The new numerical return reaches the critical $N!e^{O(N)}$ scale, but does not yet pay the remaining source factor


$$
\frac{c_N}
{\max\{\gcd(c_N,Q_{N-1}^{\mathrm H}),
       \gcd(c_N,Q_N^{\mathrm H})\}}.
$$


Nor does its archimedean size bound establish the all-prime factorial excess. In particular, every $p>N$ still has zero $N!$-allowance.

A concrete follow-on is the two-column capture lemma (HC), to be proved or disproved using the original canonical source and the changing paid Gaussian data. If proved, it would yield a strict intrinsic bound of exponent $3/4$ and force the same actual $q_N\epsilon_N$ to diverge.

Throughout, the original domain, terminal $2N$, both forcings, complete centered constants, original square column, both arcs, all paid divisions, actual $h,\mu,D,\lambda$, final all-prime $G$, actual primitive denominator $q$, and nonzero whole error remain unchanged.

**The new result is a proved canonical numerical return and an exact original-family gcd factorization. The aggregate estimate, producer retirement, and the rationality or irrationality of $e+\pi$ remain unresolved.**
