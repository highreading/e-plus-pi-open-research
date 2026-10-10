> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit and an integral arithmetic refinement of the signed Chebyshev source

## 1. Conclusions and scope

The original domain is retained throughout:


$$
\mathcal N=\{N_u=9^{18+32u}:u\in\mathbb Z_{\ge0}\}.
$$


No auxiliary subsequence replaces it.

The principal conclusions are these.

1. **A5 turn 5’s exact content formula and primitive-denominator obstruction are valid.** In particular, after the actual polynomial content, least aggregate clearer, and final ALL-prime gcd are retained,
   

$$
h_N=g_{B,N}^{\,2}c_N
$$


   and
   

$$
q_N\epsilon_N>
   \frac{N^N}
   {512\,2400^N\,c_N\sqrt{119N\log_2N}}
   \qquad(N\ge256).
$$



2. **A5 turn 6’s critical content estimate is valid.** Its thirteen source weights, constant column, fixed twelve-step affine evaluator, determinant sign, integer terminal pair, complete forced return, and midpoint estimate withstand independent proof audit:
   

$$
c_N<2^{15N}N^{N+15}\qquad(N\ge256).
$$


   This reaches, but does not cross, the critical coefficient $1$ of $N\log N$.

3. **There is a new, exact integral refinement of the source arithmetic.** The normalized source moments can be written
   

$$
\frac{S_j}{j}=\frac1j-2\Theta_j,
   \qquad \Theta_j\in\mathbb Z,
$$


   where
   

$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2.
$$


   Consequently, the complete affine source plane admits an integer constant-forcing evaluator. This proves cancellations in its rational constant columns and gives a sharper exact description of the determinantal part of the actual midpoint gcd.

4. **This integral refinement does not prove a strict content saving.** It identifies a precise obstruction: bounded forcing, bounded terminal coefficients, nonzero determinant, and full-state primitivity do not themselves exclude the required modular returns. The original boundary values and actual Gaussian terminal coefficients must be used quantitatively.

5. **The parent half-line cone bound is correct, including its constants.** Its hypotheses do not apply to the signed producer. In fact, combining that bound with the audited exponential upper bound proves the stronger statement that the signed polynomial is negative somewhere on $t<0$ for every $N\ge2^{16}$, hence at every original index.

No computation has been performed here. The corrected finite receipts are used only at their stated scope. In particular, the withdrawn source-jet tables are not used.

The global question whether $e+\pi$ is rational or irrational remains unresolved.

---

## 2. The corrected source and the unchanged producer

For an integer polynomial $Q$, define


$$
\eta(Q)=\int_{-\infty}^1 e^{t-1}Q(t)\,dt.
$$


There are two equivalent, correctly signed formulas:


$$
\eta(Q)=\sum_{r=0}^{\deg Q}(-1)^rQ^{(r)}(1),
$$


and, after $x=1-t$,


$$
\boxed{\eta(Q)=\sum_{r=0}^{\deg Q}[x^r]Q(1-x)\,r!.}
\tag{2.1}
$$


The weights in the second formula are positive. Introducing another $(-1)^r$ there changes the functional.

The integer moments satisfy


$$
\eta(t^j)=1-j\eta(t^{j-1})=(-1)^j\,!j.
$$


Thus


$$
\eta(\mathbb Z[t])\subseteq\mathbb Z.
$$



Write


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


with


$$
C_0=1,\quad C_1=2t-1,\quad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$


Retain the original quantities


$$
d=a_Nb_{N-1}-a_{N-1}b_N,
\qquad
B=b_{N-1}C_N-b_NC_{N-1},
$$




$$
K=t(1-t)(1+t^2)^2C_{N-3}^2,
\qquad
U=-\eta(K),\qquad I=\eta(B^2).
$$


The physical polynomial terminal is $2N$:


$$
\deg K=2N,\qquad
W_{\rm raw}=UB^2+(I-d^2)K,\qquad Z=Ud^2.
\tag{2.2}
$$



Let


$$
g_B=\gcd(b_{N-1},b_N)>0,
$$




$$
\alpha=\frac{b_{N-1}}{g_B},\qquad
\beta=\frac{b_N}{g_B},\qquad
F=\alpha C_N-\beta C_{N-1},\qquad
\delta=\frac d{g_B}.
$$


Then


$$
F(i)=F(-i)=\delta,\qquad \gcd(\alpha,\beta)=1.
$$


The paid scalar source gcd is


$$
V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
\tag{2.3}
$$


It is essential that


$$
I-d^2=g_B^2V.
$$


An assertion about $\gcd(U,I-d^2)$ is not automatically an assertion about $c$.

### Corrected finite evidence

The correction changes the status of the old original-domain claim $c_N=4$. The corrected residue certificates, combined with the stated period argument, give


$$
\boxed{
7\mid c_{N_u}
\quad\Longleftrightarrow\quad
u\equiv13\text{ or }17\pmod{21}.
}
\tag{2.4}
$$


Only divisibility is uniform in this statement. Uniform higher valuations have not been established.

The period-lifting mechanism is sound. Modulo $7$, the characteristic roots of the Gaussian transfer are $1+i$ and its inverse; $(1+i)^{24}=1$. Hence


$$
T^{24}=I\pmod7,\qquad T^{168}=I\pmod{49}.
$$


Together with the corrected coefficient periods modulo $7$, this propagates the corrected base residues. It does not turn a finite valuation calculation into a uniform higher-depth theorem.

The twenty-four corrected $u=0,\ldots,7$, $p=7,11,13$ receipts retain their finite scope. The direct-$t$-moment normalization computations and the auxiliary $N=13,\ldots,80$ contents are unaffected by the sign error. None is a substitute for an ALL-prime asymptotic bound.

---

## 3. Audit of the analytic normalization

### 3.1 Nonzero determinant and normalization at $i$

Put $c_j=C_j(i)$. The recurrence gives


$$
\operatorname{Im}(c_{j+1}\overline{c_j})
=4|c_j|^2+\operatorname{Im}(c_j\overline{c_{j-1}}).
$$


Since the initial imaginary part is $2$,


$$
\boxed{
d=-2-4\sum_{j=1}^{N-1}|c_j|^2<0.
}
\tag{3.1}
$$


Thus


$$
B(i)=B(-i)=d.
$$


This proves nonvanishing directly; no phase-separation hypothesis is needed.

### 3.2 The signs of $U$ and $V$

On $[0,1]$,


$$
0\le K\le1.
$$


On $[-3,-2]$,


$$
-K\ge150,
$$


because $|C_{N-3}(t)|\ge1$ there. Therefore


$$
U\ge150e^{-4}-1>0.
\tag{3.2}
$$



For $f=B/d$, the degree is at least $N-1$, and its nonzero leading coefficient has magnitude at least $1/|d|$. The classical monic Laguerre minimum gives


$$
\eta(f^2)\ge\frac{((N-1)!)^2}{d^2}.
$$


Also


$$
|d|\le |C_N(i)|\,|C_{N-1}(i)|\le6^{2N-1}.
$$


The supplied elementary factorial comparison at $N=256$, followed by multiplication by $N>36$, proves


$$
(N-1)!>6^{2N-1}\qquad(N\ge256).
$$


Hence


$$
I>d^2,\qquad V>0.
$$



Consequently, for every required index,


$$
P=\frac{F^2+(V/U)K}{\delta^2}
\tag{3.3}
$$


is nonnegative and nonzero on $[0,1]$, and


$$
\boxed{\eta(P)=P(i)=P(-i)=1.}
\tag{3.4}
$$



This argument establishes interval positivity only.

### 3.3 Factorial lower bound for the actual $U$

For $N\ge4$, $T_{N-3}(1+2x)$ has nonnegative coefficients and leading coefficient


$$
2^{2N-7}.
$$


Thus, for $x\ge0$,


$$
-K(-x)\ge2^{4N-14}x^{2N}.
$$


The positive contribution from $[0,1]$ is at most $1$, so


$$
U\ge e^{-1}2^{4N-14}(2N)!-1
\ge2^{4N-16}(2N)!.
\tag{3.5}
$$


This is a lower bound for the actual signed Chebyshev source, not for a retired factorial source.

### 3.4 Two-sided ordinary-error scale

Let


$$
R=1+\sqrt2+\sqrt{2+2\sqrt2},
\qquad 4<R<5.
$$


The exterior Chebyshev representation gives


$$
C_j(i)=\frac{\zeta^j+\zeta^{-j}}2,\qquad |\zeta|=R.
$$


With


$$
K_R=
\frac{R^2(1+R^{-2})(1+R^{-1})}
     {2(1-R^{-2})^2},
$$


the supplied upper-bound argument is valid:


$$
0<\epsilon_N:=
\int_0^1P(t)\left(e^t+\frac4{1+t^2}\right)dt
\le7(1+2^{17})K_R^2R^{-2N}.
\tag{3.6}
$$



The two summands of $P$ are both included. In particular, if


$$
s=\frac{|b_{N-1}|+|b_N|}{|d|},
$$


then $s\le K_RR^{-N}$, and


$$
\eta(f^2)\le s^2\{1+4^{2N}(2N)!\}.
$$


Combining this with (3.5) bounds the coefficient of $K$ by $2^{17}s^2$.

The lower bound is also correct. Opposite parity about $t=1/2$ gives


$$
\int_0^1C_NC_{N-1}=0,
$$


while


$$
\int_0^1C_j^2
=\frac{2j^2-1}{4j^2-1}\ge\frac13.
$$


Therefore


$$
\int_0^1 f^2
\ge\frac{b_{N-1}^2+b_N^2}{3d^2}.
$$


Since the kernel is strictly greater than $3$, and


$$
d^2\le
(b_{N-1}^2+b_N^2)(|c_N|^2+|c_{N-1}|^2),
$$


we obtain


$$
\boxed{
\epsilon_N>
\frac{R^{-2N}}{1+R^{-2}}.
}
\tag{3.7}
$$


Thus


$$
\boxed{\epsilon_N\asymp R^{-2N}}
\tag{3.8}
$$


with constants independent of $N$. In particular, at the same original indices,


$$
q_N\epsilon_N\to0
\quad\Longleftrightarrow\quad
q_N=o(R^{2N}).
\tag{3.9}
$$



---

## 4. Audit of the exact content and complete columns

### 4.1 The ALL-prime polynomial content

The recurrence modulo $8$ gives


$$
C_{2j}\equiv1,\qquad C_{2j+1}\equiv2t-1\pmod8.
$$


Thus $v_2(g_B)=1$, and exactly one of $\alpha,\beta$ is odd. Since $\gcd(\alpha,\beta)=1$,


$$
F(0)=(-1)^N(\alpha+\beta),\qquad F(1)=\alpha-\beta
$$


are coprime. Hence $F$ is primitive.

Now


$$
W_{\rm raw}=g_B^2(UF^2+VK).
$$


If $h_0=\operatorname{cont}(UF^2+VK)$, evaluation at $0$ and $1$ gives


$$
h_0\mid U.
$$


Subtracting $UF^2$ then gives $h_0\mid VK$. The coefficient of $t$ in $K$ is $1$, so $K$ is primitive and $h_0\mid V$. The converse divisibility is immediate. Therefore


$$
\boxed{
\operatorname{cont}(B)=g_B,\qquad
h=\operatorname{cont}(W_{\rm raw})=g_B^2c.
}
\tag{4.1}
$$



Put


$$
\tau=U/c,\qquad \nu=V/c.
$$


Then the actual primitive polynomial and target are


$$
\boxed{
W_{\rm prim}=\tau F^2+\nu K,\qquad
M=\tau\delta^2,\qquad \gcd(\tau,\nu)=1.
}
\tag{4.2}
$$



This proof treats every prime simultaneously.

The local deductions in A5 turn 5 are compatible with the corrected source:


$$
v_2(c)=2,\qquad v_2(h)=4,\qquad \gcd(h,15)=1.
$$


The proof of oddness of the actual aggregate clearer is coefficientwise and valid; hence the actual $q_N$ is odd. These local facts provide no asymptotic content saving. No completed prime-jet table is repeated here.

### 4.2 Complete source and exponential endpoint evaluators

Define


$$
S_j=\eta(C_j),\qquad
\mathcal E_j=\sum_{r=0}^j(-1)^rC_j^{(r)}(0).
$$


Their initial values are


$$
(S_0,S_1,S_2)=(1,-1,9),\qquad
(\mathcal E_0,\mathcal E_1,\mathcal E_2)=(1,-3,25).
$$



Using


$$
4C_j=\frac{C_{j+1}'}{j+1}-\frac{C_{j-1}'}{j-1},
$$


together with


$$
\eta(C_j')=1-S_j,\qquad
E(C_j')=(-1)^j-\mathcal E_j,
$$


gives, for $j\ge2$,


$$
(j-1)S_{j+1}+4(j^2-1)S_j-(j+1)S_{j-1}=-2,
\tag{4.3}
$$




$$
(j-1)\mathcal E_{j+1}
+4(j^2-1)\mathcal E_j-(j+1)\mathcal E_{j-1}=2(-1)^j.
\tag{4.4}
$$


Both forcing terms are necessary. Neither recurrence is used by illegally dividing by $j-1$ at a singular index.

For either $\mathcal L=\eta$ or $\mathcal L=E$,


$$
\begin{aligned}
\mathcal L(F^2)
={}&\frac{\alpha^2+\beta^2}{2}
+\frac{\alpha^2}{2}\mathcal L(C_{2N})
+\frac{\beta^2}{2}\mathcal L(C_{2N-2})\\
&-\alpha\beta\{\mathcal L(C_{2N-1})+\mathcal L(C_1)\}.
\end{aligned}
\tag{4.5}
$$



Let


$$
H=t(1-t)(1+t^2)^2.
$$


Its exact Chebyshev expansion is


$$
2048H=
458C_0+176C_1-399C_2-168C_3-58C_4-8C_5-C_6.
\tag{4.6}
$$


Also


$$
\eta(H)=-332.
$$


For $m=N-3$ and


$$
(\gamma_0,\ldots,\gamma_6)
=(458,176,-399,-168,-58,-8,-1),
$$


the complete $K$-column is


$$
\mathcal L(K)=\frac1{8192}\sum_{r=0}^6\gamma_r
\left(
2\mathcal L(C_r)+
\mathcal L(C_{2m+r})+
\mathcal L(C_{|2m-r|})
\right).
\tag{4.7}
$$


All terms terminate at their actual finite indices, at most $2N$.

### 4.3 Complete rational arcs

Define the integer monic quotients


$$
R_j(t)=\frac{C_j(t)-a_j-b_jt}{1+t^2},
$$


and


$$
\xi_j=4\int_0^1R_j,\qquad
\upsilon_j=4\int_0^1tR_j.
$$


Starting with zero values at $j=0,1$, their complete recurrence is


$$
\xi_{j+1}=4\upsilon_j-2\xi_j-\xi_{j-1}+16b_j,
\tag{4.8}
$$




$$
\upsilon_{j+1}
=-4\xi_j-2\upsilon_j-\upsilon_{j-1}
+16(\ell_j-a_j),
\tag{4.9}
$$


where


$$
\ell_j=
\begin{cases}
0,&j\text{ odd},\\
(1-j^2)^{-1},&j\text{ even}.
\end{cases}
$$


The $b_j$-terms cancel in (4.9) only after the full return
$t^2R_j=C_j-a_j-b_jt-R_j$ is included.

The complete arc columns are


$$
R_F=
\frac{\alpha^2\xi_{2N}+\beta^2\xi_{2N-2}
-2\alpha\beta\xi_{2N-1}}2,
\tag{4.10}
$$


and, with $j_r=(1-4r^2)^{-1}=j_{-r}$,


$$
R_K=\frac{13}{30}
+\frac{42j_m-20(j_{m+1}+j_{m-1})
-(j_{m+2}+j_{m-2})}{128}.
\tag{4.11}
$$


These formulas include the complete rational returns.

The monic arc quotients have degree at most $2N-2$. Their integration denominators therefore stop at $2N-1$, not at an artificially extended boundary.

### 4.4 The whole rational error enclosure

The exact unweighted integrals are


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
}{8192}.
$$


Thus


$$
J_N=\frac{J_F+(V/U)J_K}{\delta^2}
$$


satisfies


$$
\boxed{3J_N<\epsilon_N<7J_N.}
\tag{4.12}
$$


Neither positive summand of $P$ has been omitted.

---

## 5. Least clearers, final gcd, and the effective-$e$ obstruction

Let


$$
E_F=E(F^2),\qquad E_K=E(K),\qquad
E=\tau E_F+\nu E_K.
$$


Reduce the complete aggregate rational arc:


$$
\tau R_F+\nu R_K=\frac b\lambda,
\qquad \gcd(b,\lambda)=1,\quad \lambda>0.
\tag{5.1}
$$


This is the actual least aggregate clearer.

Set


$$
A=\lambda E-b,\qquad G=\gcd(M,A).
$$


Since $\gcd(A,\lambda)=1$,


$$
\boxed{
q=\frac{\lambda M}{G},\qquad p=\frac A G.
}
\tag{5.2}
$$


Integration by parts and monic division give


$$
\int_0^1W_{\rm prim}e^t=eM-E,
$$




$$
4\int_0^1\frac{W_{\rm prim}}{1+t^2}
=M\pi+\frac b\lambda.
$$


Consequently,


$$
\boxed{q(e+\pi)-p=q\epsilon_N>0.}
\tag{5.3}
$$


The exact rational enclosure after primitive normalization is


$$
qJ_N=\frac{\lambda}{G}(\tau J_F+\nu J_K).
\tag{5.4}
$$



### 5.1 The least simultaneous column clearer is only auxiliary

Let


$$
D=\operatorname{lcm}\bigl(\operatorname{den}(R_F),
                         \operatorname{den}(R_K)\bigr),
$$


where both denominators are taken after complete rational reduction. Define


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$


Then


$$
\frac pq=\frac{\tau X+\nu Y}{D\tau\delta^2}.
$$


Because $\lambda\mid D$,


$$
\tau X+\nu Y=\frac D\lambda A,
$$


and


$$
\boxed{
\gcd(D\tau\delta^2,\tau X+\nu Y)=\frac D\lambda G.
}
\tag{5.5}
$$


Thus the excess auxiliary clearing returns inside the final gcd. It is not silently substituted for $\lambda$.

The corresponding raw-interface identity is


$$
\gcd(B_{\rm raw},A_{\rm raw})
=\frac{L_{\rm aff}h}{\lambda}G,
\qquad L_{\rm aff}=\operatorname{lcm}(1,\ldots,2N-1).
\tag{5.6}
$$



### 5.2 The surviving divisor reaches the actual $q$

Since $\gcd(\tau,\nu)=1$,


$$
\gcd(\tau,\tau X+\nu Y)=\gcd(\tau,Y).
$$


Prime-power comparison in the reduced rational number therefore proves


$$
\boxed{\frac{\tau}{\gcd(\tau,Y)}\mid q.}
\tag{5.7}
$$


This remains valid at primes dividing $D$, $\delta$, or recurrence coefficients.

The $K$-column is a pure-$e$ column. Put


$$
L_K=\int_0^1K(t)\left(e^t+\frac4{1+t^2}\right)dt.
$$


Then


$$
0<L_K<7J_K\le7
$$


and


$$
\boxed{Y+DUe=-DL_K.}
\tag{5.8}
$$



The classical effective Euler estimate used in A5 is sufficient:


$$
|Qe-P|>\frac1{Q(4\log_2Q+8)}
\qquad(P\in\mathbb Z,\ Q\ge1).
\tag{5.9}
$$


Its applicability to unreduced pairs is legitimate. For reduced convergents, Euler’s partial quotients and $q_k\ge2^{(k-1)/2}$ give the stated constant; nonconvergents satisfy the stronger Legendre alternative. Multiplying a reduced pair by an integer does not weaken (5.9).

Let $a=\gcd(\tau,Y)$. Since $a\mid U$, the inputs


$$
Q=DU/a,\qquad P=-Y/a
$$


are integers with $Q\ge1$. Applying (5.9) to (5.8) yields


$$
a^2<7D^2U(4\log_2(DU)+8).
$$


Together with (5.7),


$$
q>
\frac{\sqrt U}
{cD\sqrt{7(4\log_2(DU)+8)}}.
\tag{5.10}
$$



Finally,


$$
D\mid\operatorname{lcm}(1,\ldots,2N-1),\qquad D<256^N,
$$




$$
U\le8\,36^{N-3}(2N)!,
$$


and, for $N\ge256$,


$$
4\log_2(DU)+8\le17N\log_2N.
$$


Equation (3.5) gives


$$
\sqrt U>\frac1{256}\left(\frac{8N}{e}\right)^N.
$$


Combining these bounds with (3.7), $e<3$, and $R<5$, proves


$$
\boxed{
q_N\epsilon_N>
\frac{N^N}
{512\,2400^N\,c_N\sqrt{119N\log_2N}}.
}
\tag{5.11}
$$



This is an unconditional lower bound for the actual nonzero whole error after the ALL-prime final gcd.

---

## 6. Audit of the critical-scale source-content proof

Put $n=2N$, so $n\ge512$, and define


$$
\mathscr S_j=S_j/j\qquad(j\ge1).
$$


Equation (4.3) becomes


$$
\mathscr S_{j-1}
=\mathscr S_{j+1}+4j\mathscr S_j+\frac2{j^2-1}.
\tag{6.1}
$$


This is initially an equality over $\mathbb Q$. The integer


$$
\mathcal L_n=\operatorname{lcm}(1,\ldots,n)
$$


pays every division because


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}\in\mathbb Z.
\tag{6.2}
$$



### 6.1 The thirteen weights and complete constant

From (4.6)–(4.7),


$$
8192U=1359872+\sum_{k=0}^{12}w_kS_{n-k},
\tag{6.3}
$$


where


$$
\boxed{
(w_0,\ldots,w_{12})
=(1,8,58,168,399,-176,-916,-176,399,168,58,8,1).
}
\tag{6.4}
$$


The middle weight is $-2\gamma_0=-916$; the other weights occur symmetrically as $-\gamma_r$. The constant is


$$
-2\sum_{r=0}^6\gamma_rS_r
=-2\cdot2048\,\eta(H)=1359872.
$$


Thus the complete constant has the correct sign and value.

Use the fixed evaluator


$$
(r_0,s_0,e_0)=(1,0,0),\qquad
(r_1,s_1,e_1)=(0,1,0),
$$




$$
\begin{aligned}
r_{k+1}&=r_{k-1}+4(n-k)r_k,\\
s_{k+1}&=s_{k-1}+4(n-k)s_k,\\
e_{k+1}&=e_{k-1}+4(n-k)e_k+\frac2{(n-k)^2-1},
\end{aligned}
\qquad1\le k\le11.
\tag{6.5}
$$


Then


$$
\mathscr S_{n-k}
=r_k\mathscr S_n+s_k\mathscr S_{n-1}+e_k.
$$


Set


$$
\mathsf A=\sum w_k(n-k)r_k,\qquad
\mathsf B=\sum w_k(n-k)s_k,
$$




$$
\mathsf E=1359872+\sum w_k(n-k)e_k.
$$


The complete source direction is


$$
8192U=\mathsf A\mathscr S_n+\mathsf B\mathscr S_{n-1}+\mathsf E.
\tag{6.6}
$$


Here $\deg\mathsf A\le11$, $\deg\mathsf B\le12$, with leading coefficients $4^{10}$ and $4^{11}$.

The actual paid square direction is


$$
2V=\mathsf P\mathscr S_n+\mathsf Q\mathscr S_{n-1}+\mathsf T,
\tag{6.7}
$$


where


$$
\mathsf P=n\alpha^2+(n-2)\beta^2,
$$




$$
\mathsf Q=4(n-1)(n-2)\beta^2-2(n-1)\alpha\beta,
$$




$$
\mathsf T=(\alpha+\beta)^2-2\delta^2+\frac{2\beta^2}{n}.
\tag{6.8}
$$


The $\delta^2$-term and the rational constant are indispensable.

### 6.2 Independent determinant-sign proof

Let


$$
\Delta=\mathsf A\mathsf Q-\mathsf B\mathsf P.
$$


The bounded symbolic certificate verifies this algebraic expression, but not its sign. The following estimates establish the sign independently.

Put


$$
s=\frac1{4n-7},\qquad r_*=4(n-1)+s,\qquad h=4(n-12)\ge2n.
$$


Since $r_2=1$ and the subsequent positive values grow by at least $h$,


$$
\mathsf A
\ge\left(n-12-\frac{1268n}{h^5}\right)r_{12}>0.
\tag{6.9}
$$



For $f_k=s_k-r_*r_k$, direct evaluation gives


$$
f_0=-r_*,\quad f_1=1,\quad f_2=-s,\quad
f_3=s,\quad f_4=(4n-13)s.
$$


For $k\ge3$, the positive values grow by at least $h$, and


$$
f_{12}\ge h^9s>128n^8.
$$


The only negative weights are $w_5,w_6,w_7$, whose absolute values sum to $1268$. Consequently,


$$
\mathsf B-r_*\mathsf A
\ge(n-13)f_{12}-nr_*-58(n-2)s>0.
$$


Hence


$$
\frac{\mathsf B}{\mathsf A}>
4(n-1)+\frac1{4n-7}.
\tag{6.10}
$$



For every real $(\alpha,\beta)\ne(0,0)$, $\mathsf P>0$, and


$$
\begin{aligned}
\mathsf Q-4(n-1)\mathsf P
&=-4n(n-1)\left(\alpha+\frac{\beta}{4n}\right)^2
+\frac{n-1}{4n}\beta^2\\
&\le\frac{n-1}{4n(n-2)}\mathsf P.
\end{aligned}
$$


But


$$
\frac1{4n-7}-\frac{n-1}{4n(n-2)}
=\frac{3n-7}{4n(n-2)(4n-7)}>0.
$$


Therefore


$$
\boxed{\Delta<0.}
\tag{6.11}
$$


This validates the determinant hypothesis for the actual Gaussian coefficients, including every possible exceptional phase.

### 6.3 Integer terminal pair and complete forced return

Define


$$
Z_n=8192\mathsf Q\,U-2\mathsf B\,V,
\qquad
Z_{n-1}=2\mathsf A\,V-8192\mathsf P\,U.
\tag{6.12}
$$


These are integers divisible by $c$. They satisfy


$$
Z_j=\Delta\frac{S_j}{j}+\rho_j
$$


at $j=n,n-1$, where


$$
\rho_n=\mathsf Q\mathsf E-\mathsf B\mathsf T,\qquad
\rho_{n-1}=\mathsf A\mathsf T-\mathsf P\mathsf E.
$$


Propagate


$$
Z_{j-1}=Z_{j+1}+4jZ_j
\tag{6.13}
$$


and


$$
\rho_{j-1}
=\rho_{j+1}+4j\rho_j-\frac{2\Delta}{j^2-1}.
\tag{6.14}
$$


Equation (6.1) proves the identity at every retained index. The source forcing is canceled by the explicitly retained opposite forcing, not discarded.

The propagation matrix


$$
\begin{pmatrix}0&1\\1&4j\end{pmatrix}
$$


is unimodular. The terminal transformation has determinant $2^{14}\Delta\ne0$. Thus every adjacent pair is nonzero, and


$$
\boxed{
\gcd(Z_N,Z_{N+1})=c\,e_N,\qquad
e_N\mid2^{14}|\Delta|.
}
\tag{6.15}
$$


No modular division is used.

### 6.4 Midpoint height

The bounds used by A5 are deliberately coarse but valid:


$$
|\mathsf A|,|\mathsf B|,|\mathsf E|
\le H:=2^{22}(5n)^{13},
$$




$$
|\mathsf P|,|\mathsf Q|,|\mathsf T|
\le H_V:=16n^2\,36^n.
$$


Thus


$$
|\Delta|,|\rho_n|,|\rho_{n-1}|
\le B_*:=2HH_V
=2^{27}5^{13}n^{15}36^n.
\tag{6.16}
$$



Including every forcing term in (6.14) gives


$$
\max(|\rho_N|,|\rho_{N+1}|)
\le B_*5^{N-1}\frac{(2N-1)!}{N!}.
\tag{6.17}
$$


The coefficient-norm recurrence gives $\|C_j\|_1\le7^j$, hence


$$
\left|\frac{S_j}{j}\right|\le7^j(j-1)!.
$$


Therefore


$$
c\le
B_*\left(
7^{N+1}N!+
5^{N-1}\frac{(2N-1)!}{N!}
\right).
\tag{6.18}
$$


Using $N!\le N^N$ and $(2N-1)!/N!\le(2N)^{N-1}$,


$$
c\le2^{45}5^{13}12960^N N^{N+15}
<2^{15N}N^{N+15}.
\tag{6.19}
$$



The critical theorem is therefore proved independently of the finite symbolic certificate and all source-jet tables.

---

## 7. New arithmetic result: an integral constant-forcing source plane

The rational forcing in (6.1) has more integral structure than the original presentation exposes.

### Theorem 7.1 — Integral source normalization

For $j\ge1$, define


$$
\Theta_j=\eta\!\left(U_{j-1}(2t-1)\right),
\qquad \Theta_0=0,
$$


where $U_{j-1}$ is the Chebyshev polynomial of the second kind. Then


$$
\boxed{S_j=1-2j\Theta_j,\qquad \Theta_j\in\mathbb Z,}
\tag{7.1}
$$


and


$$
\boxed{
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2
\qquad(j\ge1),
}
\tag{7.2}
$$


with


$$
\Theta_0=0,\qquad \Theta_1=1,\qquad \Theta_2=-2.
$$



#### Proof

The exact polynomial derivative identity is


$$
C_j'=2j\,U_{j-1}(2t-1).
$$


Thus division by $2j$ is paid at the polynomial level:


$$
C_j'/(2j)\in\mathbb Z[t].
$$


Integration by parts gives


$$
\eta(C_j')=C_j(1)-\eta(C_j)=1-S_j.
$$


This proves (7.1), including integrality.

Substituting


$$
\mathscr S_j=\frac1j-2\Theta_j
$$


into the normalized source recurrence gives (7.2) for $j\ge2$. At $j=1$, it is separately verified from the displayed initial values. No singular instance of the old recurrence has been inverted. ∎

This is an auxiliary coordinate change in the same source. It does not change the producer, the physical terminal $2N$, or any affine integration denominator.

### 7.1 An integer twelve-step evaluator

Retain $r_k,s_k$ from (6.5), and define integer polynomials


$$
\kappa_0=\kappa_1=0,
$$




$$
\kappa_{k+1}
=\kappa_{k-1}+4(n-k)\kappa_k-2,
\qquad1\le k\le11.
\tag{7.3}
$$


Then


$$
\Theta_{n-k}=r_k\Theta_n+s_k\Theta_{n-1}+\kappa_k.
\tag{7.4}
$$


All forcing is now integral and constant.

The thirteen weights satisfy $\sum w_k=0$. Define


$$
\mathsf C_U
=679936-\sum_{k=0}^{12}w_k(n-k)\kappa_k,
\tag{7.5}
$$




$$
\mathsf C_V=\alpha^2+(2n-3)\beta^2-\delta^2.
\tag{7.6}
$$


Both are integers at the actual inputs; $\mathsf C_U\in\mathbb Z[n]$ has degree at most $11$.

Substitution into the original two source columns gives the exact identities


$$
\boxed{
4096U=\mathsf C_U-\mathsf A\Theta_n-\mathsf B\Theta_{n-1},
}
\tag{7.7}
$$




$$
\boxed{
V=\mathsf C_V-\mathsf P\Theta_n-\mathsf Q\Theta_{n-1}.
}
\tag{7.8}
$$



For (7.8), the constant calculation is worth recording:


$$
\begin{aligned}
2V
={}&\alpha^2S_n+\beta^2S_{n-2}
-2\alpha\beta S_{n-1}
+(\alpha+\beta)^2-2\delta^2,\\
\Theta_{n-2}
={}&\Theta_n+4(n-1)\Theta_{n-1}-2.
\end{aligned}
$$


These give precisely


$$
V=-\mathsf P\Theta_n-\mathsf Q\Theta_{n-1}
+\alpha^2+(2n-3)\beta^2-\delta^2.
$$


The actual $\delta$, including the paid Gaussian division, remains present.

### Corollary 7.2 — Cancellation in the rational constant columns

Comparison with (6.6)–(6.7) proves


$$
\boxed{
\mathsf E
=2\mathsf C_U-\frac{\mathsf A}{n}-\frac{\mathsf B}{n-1},
}
\tag{7.9}
$$




$$
\boxed{
\mathsf T
=2\mathsf C_V-\frac{\mathsf P}{n}-\frac{\mathsf Q}{n-1}.
}
\tag{7.10}
$$


In particular,


$$
\boxed{n(n-1)\mathsf E\in\mathbb Z[n].}
\tag{7.11}
$$


The larger polynomial $Q_{\rm loc}(n)=\prod_{r=0}^{12}(n-r)$ is a valid clearer, but all factors $n-2,\ldots,n-12$ cancel from this complete constant column.

This is not a change to the actual arc clearer $\lambda$.

### 7.2 An integral return and a refined ALL-prime midpoint-content identity

Define


$$
z_n=4096\mathsf Q\,U-\mathsf B V,
\qquad
z_{n-1}=\mathsf A V-4096\mathsf P U,
\tag{7.12}
$$


and


$$
r_n=\mathsf Q\mathsf C_U-\mathsf B\mathsf C_V,
\qquad
r_{n-1}=\mathsf A\mathsf C_V-\mathsf P\mathsf C_U.
\tag{7.13}
$$


Then


$$
z_j=-\Delta\Theta_j+r_j
$$


at the terminal pair. Propagate


$$
z_{j-1}=z_{j+1}+4jz_j,
\tag{7.14}
$$




$$
\boxed{r_{j-1}=r_{j+1}+4jr_j-2\Delta.}
\tag{7.15}
$$


Every quantity here is an integer.

These are exactly the old objects with their common factor exposed:


$$
\boxed{
Z_j=2z_j,\qquad
\rho_j=2r_j-\frac{\Delta}{j}.
}
\tag{7.16}
$$


Thus the complete rational return has not been suppressed. Its rational part has been evaluated explicitly.

Let


$$
\mathfrak g_N=\gcd(z_N,z_{N+1})>0.
$$


The terminal determinant is $4096\Delta$, so


$$
\boxed{
\mathfrak g_N=c_N e_N',\qquad
e_N'\mid2^{12}|\Delta|.
}
\tag{7.17}
$$


The primitive midpoint height is unchanged:


$$
H_N^{\rm ret}
=\frac{\max(|z_N|,|z_{N+1}|)}{\mathfrak g_N}.
$$



Now define the exponentially bounded terminal integer


$$
\mathfrak d_N
=\gcd\bigl(|\Delta|,r_n,r_{n-1}\bigr).
\tag{7.18}
$$


Because the forcing in (7.15) is a multiple of $\Delta$, unimodular propagation gives


$$
\gcd(\Delta,r_j,r_{j+1})
=\gcd(\Delta,r_n,r_{n-1}).
$$


Since $z_j\equiv r_j\pmod\Delta$, this proves the new exact identity


$$
\boxed{
\gcd(\mathfrak g_N,|\Delta|)=\mathfrak d_N.
}
\tag{7.19}
$$


Furthermore,


$$
\boxed{e_N'\mid2^{12}\mathfrak d_N.}
\tag{7.20}
$$


Indeed, at every odd prime the exponent in $e_N'$ is bounded by both its exponent in $\mathfrak g_N$ and its exponent in $\Delta$; the prime $2$ costs at most the displayed additional twelve powers.

Equations (7.17)–(7.20) are ALL-prime statements for the actual midpoint pair. They improve the description of the determinantal excess without asserting that the selected content itself is small.

---

## 8. What the forcing does—and does not—control

The preceding theorem proves that rational denominator accumulation is not the missing source-content mechanism. The complete return is an integer constant-forcing return plus the explicit term $-\Delta/j$.

It does **not** homogenize the source by a rational particular solution. Indeed,


$$
\left(\frac1{x+1}+4x\frac1x-\frac1{x-1}\right)
=4-\frac2{x^2-1}.
$$


The extra constant $4$ is exactly why $\Theta_j$ still has forcing $2$. A5’s “no rational particular solution” proposition remains valid.

### 8.1 Exact good-modulus return condition

For any $m$ coprime to $2\Delta$, equations (7.7)–(7.8) show


$$
m\mid c
$$


if and only if


$$
\boxed{
\Theta_n\equiv r_n\Delta^{-1}\pmod m,\qquad
\Theta_{n-1}\equiv r_{n-1}\Delta^{-1}\pmod m.
}
\tag{8.1}
$$


This retains the actual $\alpha,\beta,\delta$, the entire constant columns, and the original source boundary $(\Theta_0,\Theta_1)=(0,1)$.

At primes dividing $2\Delta$, (8.1) must not be used by inversion. The integral formulas (7.7)–(7.8), or the integer midpoint pair, remain valid there.

### 8.2 A precise bounded-forcing obstruction

The augmented backward transfer for $\Theta$ is


$$
\begin{pmatrix}
0&1&0\\
1&4j&-2\\
0&0&1
\end{pmatrix},
$$


whose determinant is $-1$. It is therefore a bijection on augmented states modulo every modulus.

Fix $n$ and even fix the actual terminal coefficients


$$
\mathsf A,\mathsf B,\mathsf P,\mathsf Q,
\mathsf C_U,\mathsf C_V.
$$


For every arbitrarily large $m$ coprime to $2\Delta$, the congruence target in (8.1) has a unique preimage modulo $m$ under the affine transfer. One can lift that preimage to integer initial data. By additionally matching the actual terminal state modulo $4096$, the first selected output in (7.7) remains integrally divisible by $4096$. The resulting auxiliary sequence obeys the same forcing $2$, the same transfer matrices, and the same bounded terminal coefficient rows, while its two selected outputs are both divisible by $m$.

This proves the following limited but exact obstruction:

> A selected-content bound cannot follow from the displayed forcing bound, terminal coefficient heights, nonzero determinant, and full-state primitivity alone. It must quantitatively use the original boundary values and their synchronization with the actual Gaussian terminal data.

These auxiliary initial states are not substituted into the producer. The argument identifies a missing hypothesis in a possible shortcut; it does not claim large content for the original source.

Even the actual source already shows why pairwise coprimality is not automatic:


$$
\Theta_3=19,\qquad \Theta_4=-228,
\qquad \gcd(\Theta_3,\Theta_4)=19,
$$


although the augmented state containing the coordinate $1$ is primitive.

### 8.3 A concrete complementary arithmetic obligation

The new integral formulation permits an arithmetic target separate from a stable/dominant-solution proof.

> **Arithmetic return-content lemma.** Prove that there exist $\sigma>0$ and $C\ge0$ such that, for every sufficiently large original index,
> 

$$
> \boxed{
> \frac{\gcd(z_N,z_{N+1})}{\mathfrak d_N}
> \le e^{CN}N^{(1-\sigma)N}.
> }
> \tag{8.2}
>
$$


> Here $z_j,r_j,\mathfrak d_N$ are the explicit integer objects in
> (7.12)–(7.18), with the original boundary
> $(\Theta_0,\Theta_1)=(0,1)$ and actual paid Gaussian coefficients.

Since $\mathfrak d_N\le|\Delta|\le e^{O(N)}$, this would imply


$$
c_N\le e^{O(N)}N^{(1-\sigma)N}.
$$


Then (5.11) would force $q_N\epsilon_N\to\infty$.

Lemma (8.2) is **open**. The integral identities and gcd refinement above are proved; the quantitative return exclusion is not.

---

## 9. Independent audit of the source-half-line cone bound

Assume now, for a different scoped statement, that $P$ is a real polynomial of degree at most $2N$ satisfying


$$
P(t)\ge0\quad\text{for all }t\le1,\qquad
\eta(P)=1,\qquad P(i)=1.
\tag{9.1}
$$


Put


$$
M_0=\min(N,\lceil32\sqrt N\rceil).
$$



### 9.1 Representation and Laguerre normalization

The classical half-line representation gives


$$
P=F^2+(1-t)G^2,\qquad
\deg F\le N,\quad\deg G\le N-1.
$$


Only a real representation is used; no rational or integral coefficient normalization is asserted.

After $x=1-t$,


$$
\eta(F^2)+\eta((1-t)G^2)=1.
$$


The Laguerre norms are


$$
\int_0^\infty e^{-x}L_j(x)^2\,dx=1,
$$




$$
\int_0^\infty xe^{-x}(L_j^{(1)}(x))^2\,dx=j+1.
$$


Thus the coefficient-vector norms of the expansions in


$$
L_j(1-t),\qquad L_j^{(1)}(1-t)/\sqrt{j+1}
$$


are each at most $1$.

At $i$,


$$
1\le |F(i)|^2+\sqrt2\,|G(i)|^2.
$$


Therefore one of $H=F,G$ satisfies $|H(i)|>1/2$.

### 9.2 Entire-polynomial bound and Taylor cutoff

The finite Laguerre expansions imply


$$
|L_j(z)|\le e^{2\sqrt{j|z|}},
$$




$$
|L_j^{(1)}(z)|\le(j+1)e^{2\sqrt{j|z|}}.
$$


The exponential domination follows from


$$
\frac1{(r!)^2}\le\frac{4^r}{(2r)!}.
$$


Cauchy–Schwarz therefore gives


$$
|H(t)|\le (N+1)e^{2\sqrt{101N}}
\qquad(|t|\le100).
\tag{9.2}
$$



If $H_{M_0}$ is the Taylor polynomial through degree $M_0$, then either the tail is zero or


$$
|H-H_{M_0}|
\le\delta:=
\frac{(N+1)e^{2\sqrt{101N}}100^{-M_0}}{99}
\qquad(|t|\le1).
\tag{9.3}
$$


For


$$
K_{M_0}=\sqrt2(M_0+1)10^{M_0},
$$


the stated estimates yield


$$
\delta K_{M_0}
<2N^{3/2}e^{-43\sqrt N}<\frac18.
\tag{9.4}
$$


The cutoff and constants are valid.

### 9.3 Legendre evaluation constant

On $[0,1/2]$,


$$
\int_0^{1/2}P_j(4t-1)^2\,dt=\frac1{2(2j+1)}.
$$


The finite coefficient formula gives


$$
|P_j(4i-1)|
\le
2^j\sum_{r=0}^j\binom jr4^r=10^j.
$$


Hence the evaluation-kernel norm for degree at most $M_0$ is at most


$$
\left(2\sum_{j=0}^{M_0}(2j+1)100^j\right)^{1/2}
\le\sqrt2(M_0+1)10^{M_0}=K_{M_0}.
$$


Thus


$$
\|A\|_{L^2[0,1/2]}\ge\frac{|A(i)|}{K_{M_0}}.
$$



Combining this with the Taylor tail and the reverse triangle inequality gives


$$
\|H\|_{L^2[0,1/2]}\ge\frac1{4K_{M_0}}.
$$


Since $P\ge F^2$ and $P\ge\frac12G^2$ on $[0,1/2]$,


$$
\boxed{
\int_0^1P(t)\,dt
\ge\frac1{64(M_0+1)^2\,10^{2M_0}}.
}
\tag{9.5}
$$



No correction to the parent constant is needed.

If a producer satisfying these hypotheses also has an independently proved actual primitive-denominator floor $q_N\ge e^{cN}$, then its whole error diverges. The denominator hypothesis remains separate.

### 9.4 New consequence: actual failure of half-line positivity for the signed family

The audited constants satisfy $K_R<20$. Hence


$$
\epsilon_N<2^{30-4N}.
\tag{9.6}
$$


If the signed $P_N$ were nonnegative on the whole source half-line, (9.5) would apply.

For $N\ge2^{16}$,


$$
M_0+1\le34\sqrt N,
$$


and


$$
64(M_0+1)^2\,10^{2M_0}
<2^{23}N\,2^{256\sqrt N}.
$$


Thus half-line positivity would imply


$$
J_N>2^{-23}N^{-1}2^{-256\sqrt N}.
$$


But


$$
4N>53+\log_2N+256\sqrt N
\qquad(N\ge2^{16}),
$$


so (9.6) is smaller even than this lower bound for $J_N$, contradicting $\epsilon_N>3J_N$.

Therefore


$$
\boxed{
\text{For every }N\ge2^{16},\ P_N(t)<0
\text{ for some }t<0.
}
\tag{9.7}
$$


Every original index lies in this range. The cone theorem is therefore not merely unavailable without proof of a hypothesis: its half-line positivity hypothesis actually fails for the signed family.

---

## 10. What the audited estimates imply

The two uniform estimates are


$$
q_N\epsilon_N>
\frac{N^N}
{512\,2400^N\,c_N\sqrt{119N\log_2N}},
$$


and


$$
c_N<2^{15N}N^{N+15}.
$$


Their combination gives only an exponentially decaying lower bound for $q_N\epsilon_N$. Such a lower bound proves neither decay nor divergence.

If this producer were successful in the sense


$$
q_N\epsilon_N\to0,
$$


then necessarily


$$
\log c_N\ge N\log N-O(N).
$$


The critical upper bound therefore narrows hypothetical success to


$$
\boxed{\log c_N=N\log N+O(N).}
\tag{10.1}
$$



Conversely, any strict saving


$$
\log c_N\le(1-\sigma)N\log N+O(N),
\qquad \sigma>0,
$$


would force the actual whole errors to diverge.

Neither conclusion determines $e+\pi$. A no-go for this producer would retire only this producer. A proof of irrationality through it would still require


$$
0<q_N(e+\pi)-p_N=q_N\epsilon_N\to0
$$


for the actual primitive pairs at the retained infinite indices.

The integer target also genuinely grows. Since $\tau\ge1$,


$$
M=\tau\delta^2\ge\delta^2\to\infty.
$$


Thus the rational normalization $P(i)=1$ does not authorize applying a fixed-integer-target theorem with target $1$.

---

## 11. Bounded exact-arithmetic certificate for the new result

No new numerical normalization, prime-jet table, or huge original-index calculation is needed for the proofs above.

A small optional certificate can check the **new integral cancellation**, without repeating the already completed affine algebra certificate.

### Bounded inputs

Use:

- the thirteen fixed weights $w_0,\ldots,w_{12}$;
- the indeterminate $n$;
- the already supplied coefficient arrays for
  $\mathsf A,\mathsf B,Q_{\rm loc}\mathsf E$;
- the new recurrence
  

$$
\kappa_0=\kappa_1=0,\qquad
  \kappa_{k+1}=\kappa_{k-1}+4(n-k)\kappa_k-2,
  \quad1\le k\le11.
$$



### Expected verifiable outputs

1. An integer coefficient array for
   

$$
\mathsf C_U
   =679936-\sum_{k=0}^{12}w_k(n-k)\kappa_k,
$$


   of degree $11$, with leading coefficient
   

$$
[n^{11}]\mathsf C_U=2^{21}.
$$



2. Exact division, with zero remainder, of the supplied polynomial
   $Q_{\rm loc}\mathsf E$ by
   

$$
\prod_{r=2}^{12}(n-r).
$$


   The quotient is $n(n-1)\mathsf E$, of degree $11$.

3. A zero coefficient array for
   

$$
n(n-1)\mathsf E
   -2n(n-1)\mathsf C_U
   +(n-1)\mathsf A+n\mathsf B.
$$



4. A zero formal residual for
   

$$
\mathsf T
   =2\bigl(\alpha^2+(2n-3)\beta^2-\delta^2\bigr)
   -\frac{\mathsf P}{n}-\frac{\mathsf Q}{n-1}.
$$



5. Zero residuals for the two terminal identities
   

$$
\rho_n=2r_n-\Delta/n,\qquad
   \rho_{n-1}=2r_{n-1}-\Delta/(n-1).
$$



These are bounded polynomial calculations of degree at most $24$. Their outputs would certify the new algebra only. They would not establish the open return-content lemma, a strict $N\log N$ saving, primitive-error decay, or irrationality.

---

## 12. Final proof status

### Proved and independently audited

- Correct source normalization uses positive $r!$ after $x=1-t$.
- The signed producer is valid at every original index.
- Its whole ordinary error is positive and satisfies
  

$$
\epsilon_N\asymp R^{-2N}.
$$


- Its exact ALL-prime polynomial content is $g_B^2c$.
- The least aggregate clearer, final ALL-prime gcd, and actual primitive $q$ are retained.
- The pure-$e$ column yields the actual-whole-error lower bound (5.11).
- The complete affine midpoint argument proves
  

$$
c_N<2^{15N}N^{N+15}.
$$



### New proved statements in this report

- The source has an integer constant-forcing normalization
  

$$
S_j=1-2j\Theta_j,\qquad
  \Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2.
$$


- The complete source-plane constants satisfy the exact cancellations
  

$$
\mathsf E=2\mathsf C_U-\mathsf A/n-\mathsf B/(n-1),
$$


  and the analogous formula for $\mathsf T$.
- The actual midpoint pair admits an integral return with
  

$$
\gcd(\gcd(z_N,z_{N+1}),|\Delta|)
  =\gcd(|\Delta|,r_n,r_{n-1}),
$$


  and its determinantal excess divides $2^{12}\mathfrak d_N$.
- Bounded forcing and full-state primitivity alone cannot bound the selected content; the exact modular obstruction has been identified.
- The half-line cone theorem is valid, and the signed family actually fails half-line positivity at every original index.

### Open obligation

The unresolved arithmetic is a **strict ALL-prime saving for the actual selected return content**, or an equivalent source-specific lower bound for its primitive projective height, using the original boundary values and actual Gaussian coefficients.

The critical estimate does not supply that saving. Corrected fixed-prime information, including infinitely many original $7$-divisibilities, does not supply it either.

Accordingly, the signed producer is not proved successful or unsuccessful, and the unconditional rationality or irrationality of $e+\pi$ remains open.
