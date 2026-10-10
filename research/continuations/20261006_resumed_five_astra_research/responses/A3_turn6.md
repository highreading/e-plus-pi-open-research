> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 6 — An inhomogeneous terminal Wronskian and a polynomial bound for structural residual intersection

## Executive conclusion

The irrationality or rationality of $e+\pi$ remains unresolved.

There is a new unconditional arithmetic result for the original endpoint construction. Write, as in Turn 5,


$$
R_j=r_j\mathbf H,\qquad C_j=r_j\mathbf C,\qquad
G_j=\gcd(r_jv',r_jw'),
$$


where $r_j$ is the **actual primitive contact row**, and $\mathbf C$ includes the zero-seeded exponential residual, the exterior subtraction, and the complete logarithmic force.

For every retained original index,


$$
\boxed{
\gcd(G_3,C_3)\mid 4(n+1)^2(n+2)^2,
}
\tag{E1}
$$


and


$$
\boxed{
\gcd(G_0,C_0)\mid
4(n+1)^2(n+2)^2(n+3).
}
\tag{E2}
$$



These are integer divisibility theorems, not support-only statements. In particular, because the original indices are odd, every prime factor of the right sides is at most $n+2$. Therefore


$$
\boxed{
\gcd(G_j,C_j)_{>n+2}=1,\qquad j=0,3.
}
\tag{E3}
$$



This eliminates one of the unknown terminal intersections in Turn 5. At large primes, the structural reference-pair content cannot be canceled by the complete residual:


$$
\boxed{
(\gamma_j)_{>n+2}=(G_j)_{>n+2}.
}
\tag{E4}
$$


Any remaining large-prime cancellation in $\gcd(R_j,C_j)$ occurs where $G_j$ is a unit.

The proof comes from the actual inhomogeneous coefficient recurrence. At its singular terminal step, the complete residual satisfies


$$
\boxed{
q_\partial\mathbf C
=
2(n+1)(n+2)\bigl(2a_{n+1}-(n+1)a_n\bigr),
}
\tag{E5}
$$


with


$$
q_\partial=(n+2,-2(2n+3),2(n+2)).
$$


The complete logarithmic contribution is annihilated here because it lies in the reference plane. The exterior correction is essential to the right side of (E5).

I also derive an integral, inhomogeneous discrete Wronskian and use the established Legendre companion identity to reduce the remaining endpoint gcd to explicit projected integers. The common residual integer is


$$
\boxed{
\mathscr K_n
=
h_n b_{n+1}-h_{n+1}b_n
+2(-1)^n(n!)^3,
\qquad b_k=g_k-a_k.
}
\tag{E6}
$$


It is produced by a stated integral recurrence, not an unevaluated resultant. On all original indices,


$$
\boxed{
(n!)^3<|\mathscr K_n|<3(n!)^3,
\qquad
\operatorname{sgn}\mathscr K_n=(-1)^n=-1.
}
\tag{E7}
$$



The remaining endpoint-specific projected gcd is **not** proved small. Its precise reduction is given below. The real bound (E7) does not supply the missing primewise or infinite-family cancellation estimate.

No producer or bounded computation was executed for this report. No accepted computation is proposed for repetition.

---

## 1. Scope, retained evidence, and source assessment

The index domain is unchanged:


$$
n=15^r,\quad r\ge2,
\qquad\text{or}\qquad
n=105^r,\quad r\ge2.
$$



I retain without alteration:

- the original $3\times3$ contact matrix;
- both corrected reconstructed columns, with all four coordinates in each;
- the original complete forcing range through exactly $2n+2$;
- the complete logarithmic force at its established three-contact-row scope;
- the terminal return;
- the exterior $+1$;
- the least clearer over all eight corrected reconstruction entries;
- all actual reconstruction row contents and primitive endpoint triples;
- every prime in the final gcd;
- the actual primitive denominator;
- the whole error at the same original index.

The coefficient recurrences below reorganize the retained terminal data. They do not define a shortened forcing producer.

### 1.1 What the new selected-prime receipt establishes

The new receipt directly reports:



$$
\begin{array}{c|cc|cc}
p&
v_p(\gamma_0)&v_p(d_0)&
v_p(\gamma_3)&v_p(d_3)\\ \hline
3&3365&3365&3368&3368\\
5&1682&1682&1686&1686\\
7&1120&1121&1120&1120
\end{array}
$$


at $n=3375$, and


$$
\eta_7(3375)=1.
$$



Thus the corresponding Turn 5 denominator predictions are now finite corroboration, rather than pending predictions.

The receipt does not separately print $r_0\mathbf U$ or the dual contents. Their values deduced in Turn 5 remain theorem-derived consequences of the exact normalization laws, not additional fields purportedly extracted by this receipt.

### 1.2 Some denominator checks are already in the complete receipt

The attached complete receipt already contains


$$
\boxed{
v_{241}(d_0)=v_{241}(d_3)=28,
}
$$




$$
\boxed{
v_{211}(d_0)=v_{211}(d_3)=30,
}
$$


and


$$
\boxed{
v_2(d_0)=v_2(d_3)=5053.
}
$$



These denominator values need not be requested again. The additional Turn 5 predictions concerning $\gamma_j,G_j,r_j\mathbf U,X_j,V_j$, where not printed in a receipt, remain distinct postprocessing checks.

### 1.3 Closed results reused at their actual scope

I use:

1. the all-prime primitivity of the retained consecutive factorial-normalized moment triple;
2. the selected-prime endpoint laws and the stronger selected-part law $5n$;
3. the established common-$W_n$ results, including the stated restriction on $(W_n)_{>n+2}$;
4. the Turn 5 theorems at $p\ge5\mid n-1$;
5. the Turn 5 reductions at odd $p\mid n+1$, retaining their explicit reference-unit hypotheses;
6. the classical Legendre companion Wronskian in the actual $(\tau,\rho)$ normalization.

The A4 Turn 7 Jacobi and binary-observable theorems concern different normalized constructions. Their projective-scope cautions are pertinent, but their valuation conclusions are not imported into this endpoint problem.

---

## 2. The actual zero-seeded residual recurrence

Keep


$$
M_n(z)=e^zq(z)^n,\qquad
q(z)=1-z+\frac{z^2}{2},
$$


and


$$
\mathscr H_n(z)=\frac{q(z)^n}{(1-z)^{n+1}}.
$$



Turn 5 proved


$$
\Omega_n(z)=\mathscr H_n(z)\bigl(E_n+I_n(z)\bigr),
\qquad
I_n(z)=\int_0^z e^t(1-t)^n\,dt.
$$


Thus


$$
u_k=E_nh_k+g_k,
$$


where


$$
h_k=k![z^k]\mathscr H_n(z),\qquad
g_k=k![z^k]\mathscr H_n(z)I_n(z).
$$



For the exterior-corrected residual, define


$$
\boxed{b_k=g_k-a_k.}
\tag{2.1}
$$


Here $g_0=0$, but $b_0=-1$. That nonzero initial value is the retained exterior subtraction, not an arbitrary new seed.

### 2.1 Differential equation with the exterior correction included

Set


$$
\mathcal L_n
=(1-z)q(z)\frac{d}{dz}
-\bigl((n+1)q(z)+n(1-z)q'(z)\bigr).
$$


Then


$$
\mathcal L_n\mathscr H_n=0,
\qquad
\mathcal L_n(\mathscr H_n I_n)=qM_n.
$$


Also,


$$
\mathcal L_nM_n=-(n+z)qM_n.
$$


Consequently,


$$
\boxed{
\mathcal L_n\bigl(\mathscr H_n I_n-M_n\bigr)
=(n+1+z)qM_n.
}
\tag{2.2}
$$



The right side is not merely $qM_n$. Replacing it by $qM_n$ would discard the exterior correction.

### 2.2 Integral coefficient recurrence

Define


$$
A_k=2k+1,
$$




$$
B_k=\frac{k(2n+1-3k)}2,
\qquad
D_k=\frac{k(k-1)(k-n-1)}2.
$$


These are integers for integer $k,n$.

Coefficient extraction gives


$$
\boxed{
h_{k+1}=A_kh_k+B_kh_{k-1}+D_kh_{k-2},
}
\tag{2.3}
$$


and


$$
\boxed{
b_{k+1}=A_kb_k+B_kb_{k-1}+D_kb_{k-2}+F_k,
}
\tag{2.4}
$$


where the complete inhomogeneous term is


$$
\boxed{
\begin{aligned}
F_k={}&(n+1)a_k-nk\,a_{k-1}\\
&+\frac{(n-1)k(k-1)}2a_{k-2}
+\frac{k(k-1)(k-2)}2a_{k-3}.
\end{aligned}}
\tag{2.5}
$$



Terms with negative coefficient index are omitted in the initial coefficient equations. For $k\ge2$, the displayed recurrence is used directly, with the last term zero at $k=2$.

The initial data are


$$
(h_0,h_1,h_2)=(1,1,n+2),
$$




$$
\boxed{
(b_0,b_1,b_2)=(-1,n,n+2-n^2).
}
\tag{2.6}
$$



There is no coefficient-denominator cost in this factorial-normalized recurrence. The halves in (2.3)–(2.5) always multiply even integer products.

---

## 3. The terminal singular step evaluates the normal residual

Put


$$
m=n+1,\qquad N=n+2,
$$


and abbreviate


$$
A=a_n,\quad B=a_{n-1},\quad D=a_{n+1},\quad E=a_{n+2}.
$$


Define the moment scalar


$$
\boxed{Z_n=2D-mA.}
\tag{3.1}
$$



At $k=n+1$, the coefficient $D_k$ in (2.4) vanishes. The moment recurrence gives


$$
a_{n+1}
=a_n+\frac{n(n-1)}2(a_{n-1}+a_{n-2}).
$$


Substitution into the **complete** $F_{n+1}$ yields


$$
\boxed{F_{n+1}=m(2D-mA)=mZ_n.}
\tag{3.2}
$$


Therefore


$$
\boxed{
b_{n+2}-(2n+3)b_{n+1}+\frac{mN}{2}b_n=mZ_n.
}
\tag{3.3}
$$



Now retain the terminal columns


$$
\mathbf H=(n+2)!\,t,
$$




$$
\mathbf B=
\begin{pmatrix}
mN b_n\\
N b_{n+1}\\
b_{n+2}
\end{pmatrix},
$$




$$
\mathbf Q=
4n!(n+2)!(\rho_nv+\rho_{n+1}w),
\qquad
\mathbf C=\mathbf B+\mathbf Q.
$$



The integral reference vectors are


$$
v'=(2N,N,m)^T,\qquad
w'=(0,N,2n+3)^T.
$$


Their primitive normal is


$$
\boxed{
q_\partial=(N,-2(2n+3),2N).
}
\tag{3.4}
$$


Since $q_\partial v'=q_\partial w'=0$,


$$
q_\partial\mathbf H=q_\partial\mathbf Q=0.
$$



Multiplying (3.3) by $2N$ proves


$$
\boxed{
q_\partial\mathbf C=2mN Z_n.
}
\tag{3.5}
$$



This identity is evaluated solely in terms of actual moment coefficients. It includes the complete logarithmic force through its exact reference-plane cancellation.

Importantly, no assertion is made that the logarithmic terminal vector satisfies (2.4) at earlier coefficient indices. Its established three-row identity is all that is used.

---

## 4. A polynomial all-prime bound for $\gcd(G_j,C_j)$

This is the main new arithmetic theorem.

Let


$$
r_j=(x_j,y_j,z_j)\in\mathbb Z^3
$$


be the actual primitive row proportional to
$\ell_j\operatorname{adj}(T)$. Set


$$
\alpha_j=r_jv',\qquad
\beta_j=r_jw',
$$




$$
G_j=\gcd(\alpha_j,\beta_j),
\qquad C_j=r_j\mathbf C.
$$



The following exact row identity is useful:


$$
\boxed{
2N r_j=(\alpha_j-\beta_j,\,2\beta_j,\,0)+z_jq_\partial.
}
\tag{4.1}
$$



No contact determinant is inverted in what follows.

### 4.1 Exact endpoint kernel equations

Let $J=(n+2)!T$, and let $J_i$ be its columns, numbered $0,1,2$.

The actual endpoint rows satisfy


$$
\boxed{r_3J_0=r_3J_1=0,}
\tag{4.2}
$$


and


$$
\boxed{
r_0(nJ_0+J_1)=0,\qquad
r_0(-nmJ_0+J_2)=0.
}
\tag{4.3}
$$


These follow from


$$
\ell_3=(0,0,1),\qquad
\ell_0=(-1,n,-nm).
$$


They remain valid even when $J$ becomes singular modulo a prime.

Define


$$
q_\partial J_i=Nf_i.
$$


Using the actual moment recurrence to remove $a_{n-2}$ and $a_{n+2}$, direct calculation gives


$$
\boxed{
f_0=m(nB-A)-(2n+1)Z_n,
}
\tag{4.4}
$$




$$
\boxed{
f_1=m\bigl(nNB-(3n+4)A\bigr)+NZ_n,
}
\tag{4.5}
$$




$$
\boxed{
f_2=m^2\bigl(NA-n(n+4)B\bigr)+mNZ_n.
}
\tag{4.6}
$$



The needed combinations are


$$
\boxed{
f_1-Nf_0=2mNZ_n-2m^2A,
}
\tag{4.7}
$$




$$
\boxed{
nf_0+f_1
=
2m^2(nB-2A)-2m(n-1)Z_n,
}
\tag{4.8}
$$


and


$$
\boxed{
-nmf_0+f_2
=
2m^2(mA-nNB)+2m(n^2+n+1)Z_n.
}
\tag{4.9}
$$



These explicit identities replace a determinant-only saturation argument.

### 4.2 Odd-prime denominator costs

Fix an odd prime $p$, and write


$$
e=\min\{v_p(G_j),v_p(C_j)\},
\quad s=v_p(m),\quad t=v_p(N).
$$



If $e>t$, primitivity of $r_j$, primitivity of $q_\partial$, and (4.1) imply


$$
v_p(z_j)=t.
$$


Taking the scalar product of (4.1) with $\mathbf C$, and using (3.5), gives


$$
\boxed{v_p(mZ_n)\ge e-2t.}
\tag{4.10}
$$



Likewise, applying (4.1) to the exact endpoint kernels gives:

- at endpoint $3$,
  

$$
v_p(f_0),v_p(f_1)\ge e-2t;
$$


- at endpoint $0$,
  

$$
v_p(nf_0+f_1),\,
  v_p(-nmf_0+f_2)\ge e-2t.
$$



Thus the total loss at $p\mid N$ is explicitly at most $2v_p(N)$. No normalization-unit hypothesis has silently been extended across those primes.

#### Endpoint $3$

Put $e'=e-2t$. Equations (4.7), (4.10), and (4.4) show


$$
v_p(m^2A)\ge e',
\qquad
v_p(m^2nB)\ge e'.
$$


Since


$$
2mD=mZ_n+m^2A,
$$


and


$$
2E=4D+m(n-2)A+nmB,
$$


we obtain


$$
v_p(A)\ge e'-2s,\qquad
v_p(D),v_p(E)\ge e'-s.
$$


If $e'>2s$, the consecutive moment triple $(A,D,E)$ would have common $p$-content, contrary to the closed moment-primitivity theorem.

Therefore


$$
\boxed{
\min\{v_p(G_3),v_p(C_3)\}
\le2v_p(mN).
}
\tag{4.11}
$$



#### Endpoint $0$

Let $u=v_p(n+3)$. Equations (4.8)–(4.10) imply


$$
v_p\bigl(m^2(nB-2A)\bigr)\ge e',
$$




$$
v_p\bigl(m^2(mA-nNB)\bigr)\ge e'.
$$


Taking the second expression plus $N$ times the first gives


$$
-m^2(n+3)A.
$$


Hence


$$
v_p(A)\ge e'-2s-u,
$$


and then


$$
v_p(nB)\ge e'-2s-u,\qquad
v_p(D),v_p(E)\ge e'-s-u.
$$


Moment primitivity now gives


$$
\boxed{
\min\{v_p(G_0),v_p(C_0)\}
\le2v_p(mN)+v_p(n+3).
}
\tag{4.12}
$$



### 4.3 Binary cost, with the actual primitive row retained

Here $N$ is odd and $s=v_2(m)\ge1$.

If $e=\min(v_2(G_j),v_2(C_j))>1$, equation (4.1) and row primitivity give


$$
v_2(z_j)=1.
$$


Consequently,


$$
v_2(mZ_n)\ge e-2.
$$


The endpoint kernel equations give the relevant $f$-combination valuations at least $e-1$.

For endpoint $3$, (4.7) and (4.4) imply


$$
v_2(m^2A),v_2(m^2nB)\ge e-2.
$$


The two divisions by $2$ in recovering $D,E$ give


$$
v_2(A)\ge e-2-2s,\qquad
v_2(D),v_2(E)\ge e-3-s.
$$


Because $s\ge1$, $e>2s+2$ would make all three moments even. Therefore


$$
\boxed{
\min\{v_2(G_3),v_2(C_3)\}\le2s+2.
}
\tag{4.13}
$$



For endpoint $0$, the same calculation using (4.8)–(4.9), with
$u=v_2(n+3)$, gives


$$
\boxed{
\min\{v_2(G_0),v_2(C_0)\}\le2s+u+2.
}
\tag{4.14}
$$



The extra factor $4$ in the resulting integer bounds records these binary losses. It is a proved sufficient cost, not a claim that the bound is sharp.

### Theorem 4.1 — Complete structural residual-intersection bound

Combining all primes,


$$
\boxed{
\gcd(G_3,C_3)\mid4m^2N^2,
}
\tag{4.15}
$$




$$
\boxed{
\gcd(G_0,C_0)\mid4m^2N^2(n+3).
}
\tag{4.16}
$$



This proof uses primitive endpoint rows, exact endpoint kernel equations, the actual inhomogeneous terminal source, and actual moment primitivity. It does not infer projected primitivity from a full-system determinant.

---

## 5. Consequences at primes above $n+2$

For odd $n$, every prime divisor of $n+3$ is at most $(n+3)/2<n+2$. Thus Theorem 4.1 gives


$$
\boxed{\gcd(G_j,C_j)_{>n+2}=1.}
\tag{5.1}
$$



Recall Turn 5’s exact large-prime identities. For


$$
g=v_p(G_j),\quad x=v_p(\xi_j),\quad c=v_p(C_j),
$$


they are


$$
v_p(\gamma_j)=(g-c)_+,
$$




$$
v_p(\mathcal C_j^\sharp)=\min\{x,(c-g)_+\},
$$




$$
v_p(d_j)=(g+x-c)_+.
$$



The new theorem gives the following sharper dichotomy.

### If $p>n+2$ divides $G_j$

Then $c=0$, so


$$
\boxed{
v_p(\gamma_j)=g,\qquad
v_p(\mathcal C_j^\sharp)=0,\qquad
v_p(d_j)=g+x.
}
\tag{5.2}
$$


No factor of the large-prime reference projection is canceled at such a prime.

### If $p>n+2$ does not divide $G_j$

Then


$$
\boxed{
v_p(\gamma_j)=0,\qquad
v_p(\mathcal C_j^\sharp)=\min\{x,c\},\qquad
v_p(d_j)=(x-c)_+.
}
\tag{5.3}
$$



Thus


$$
\boxed{
(\gamma_j)_{>n+2}=(G_j)_{>n+2},
}
$$


and


$$
\boxed{
\gcd\!\left(
\gcd(R_j,C_j)_{>n+2},
(G_j)_{>n+2}
\right)=1.
}
\tag{5.4}
$$



This removes the structural/residual threshold ambiguity in Turn 5. It does **not** exclude the remaining intersection between $\xi_j$ and $C_j$ where $G_j$ is a unit.

The already controlled common $W_n$ is retained separately. Nothing here identifies it with the still-unknown endpoint-specific reference/residual gcd.

---

## 6. An integral inhomogeneous discrete Wronskian

The coefficient recurrence also provides an explicit residual evaluator.

For $k\ge2$, define


$$
w_{1,k}=h_{k-1}b_k-h_kb_{k-1},
$$




$$
w_{2,k}=h_{k-2}b_k-h_kb_{k-2},
$$




$$
w_{3,k}=h_{k-2}b_{k-1}-h_{k-1}b_{k-2}.
$$


Equations (2.3)–(2.4) give


$$
\boxed{
\begin{pmatrix}
w_{1,k+1}\\
w_{2,k+1}\\
w_{3,k+1}
\end{pmatrix}
=
\begin{pmatrix}
-B_k&-D_k&0\\
A_k&0&-D_k\\
1&0&0
\end{pmatrix}
\begin{pmatrix}
w_{1,k}\\
w_{2,k}\\
w_{3,k}
\end{pmatrix}
+
F_k
\begin{pmatrix}
h_k\\
h_{k-1}\\
0
\end{pmatrix}.
}
\tag{6.1}
$$



The initial values are


$$
\boxed{
\begin{aligned}
w_{1,2}&=2-n-2n^2,\\
w_{2,2}&=2n+4-n^2,\\
w_{3,2}&=n+1.
\end{aligned}}
\tag{6.2}
$$



This is an integral inhomogeneous recurrence for the actual zero-seeded/exterior-corrected coefficient pair. It is not the earlier fifteen-state mixed moment–force system.

At the terminal position,


$$
w_{1,n+1}=h_nb_{n+1}-h_{n+1}b_n.
$$



---

## 7. Incorporating the complete logarithmic force: an evaluated residual integer

At the three retained rows,


$$
h_n=n!\tau_n,
\qquad
h_{n+1}=\frac{(n+1)!}{2}(\tau_n+\tau_{n+1}).
\tag{7.1}
$$



Reuse the established companion Wronskian


$$
\boxed{
\tau_n\rho_{n+1}-\tau_{n+1}\rho_n
=\frac{(-1)^n}{n+1}.
}
\tag{7.2}
$$



Define


$$
\boxed{
\mathscr K_n
=
w_{1,n+1}+2(-1)^n(n!)^3.
}
\tag{7.3}
$$



The second term is the complete logarithmic contribution to this scalar. Dropping it would replace the actual complete residual by an exponential-only quantity.

### 7.1 Exact decomposition of the terminal residual

Equation (3.3) gives


$$
\mathbf B
=
\frac{mb_n}{2}v'
+
\left(b_{n+1}-\frac{mb_n}{2}\right)w'
+
mZ_ne_2,
$$


where $e_2=(0,0,1)^T$.

Since


$$
\mathbf Q
=
2n!(n+1)!(\rho_nv'+\rho_{n+1}w'),
$$


put


$$
S_n=\frac{mb_n}{2}+2n!(n+1)!\rho_n,
$$




$$
T_n=b_{n+1}-\frac{mb_n}{2}
+2n!(n+1)!\rho_{n+1}.
$$


Then


$$
\boxed{
\mathbf C=S_nv'+T_nw'+mZ_ne_2.
}
\tag{7.4}
$$


Because $m$ is even and the factorial companion clearers are retained, these coefficients are integral.

By (7.1)–(7.2),


$$
\boxed{
n!\bigl(\tau_nT_n-\tau_{n+1}S_n\bigr)=\mathscr K_n.
}
\tag{7.5}
$$



Thus $\mathscr K_n$ is the explicitly evaluated two-coordinate Wronskian of the complete terminal residual against the reference pair.

### 7.2 A rigorous size and nonvanishing bound

On $|z|=1/2$,


$$
|\mathscr H_n(z)|\le2(13/4)^n,
$$




$$
|I_n(z)|\le \frac12e^{1/2}(3/2)^n.
$$


Consequently,


$$
|h_k|\le2k!2^k(13/4)^n,
$$


and


$$
|b_k|
\le2e^{1/2}k!2^k(39/8)^n.
$$


It follows that


$$
\boxed{
|w_{1,n+1}|
\le16e^{1/2}(n+1)(n!)^2(507/8)^n.
}
\tag{7.6}
$$



For $n\ge225$, the elementary lower bound


$$
n!>(n/3)^n
$$


shows that the right side of (7.6) is less than $(n!)^3$. For example,


$$
\frac{8n}{1521}\ge\frac{1800}{1521}>\frac76,
$$


and


$$
32(n+1)(6/7)^n<1\qquad(n\ge225).
$$



Therefore


$$
\boxed{
(n!)^3<|\mathscr K_n|<3(n!)^3,
\qquad
\operatorname{sgn}\mathscr K_n=(-1)^n.
}
\tag{7.7}
$$



All original indices are odd and at least $225$, so $\mathscr K_n<0$.

This is a proved bound for a specified integer generated by the actual recurrence. It is not a claimed prime-factor bound.

---

## 8. Exact projection scope: reduction of $\gcd(R_j,C_j)$

Continue to write


$$
\alpha_j=r_jv',\qquad \beta_j=r_jw',\qquad z_j=r_{j,2}.
$$


Define the explicit integers


$$
\boxed{
I_j=\beta_j\mathscr K_n+mh_nZ_nz_j,
}
\tag{8.1}
$$




$$
\boxed{
J_j=-\alpha_j\mathscr K_n
+(2h_{n+1}-mh_n)Z_nz_j.
}
\tag{8.2}
$$



These contain:

- the actual primitive contact row;
- the actual moment scalar $Z_n$;
- the integral inhomogeneous Wronskian;
- the complete logarithmic correction inside $\mathscr K_n$.

There is no factorial seed $E_n$.

### 8.1 Integral Bézout-type identities and their denominator costs

Put


$$
L_0=b_n+4(n!)^2\rho_n,
$$




$$
L_1=2b_{n+1}-mb_n+4m(n!)^2\rho_{n+1}.
$$


Both are integers by the established factorial companion-denominator bounds.

Directly from (7.4)–(7.5),


$$
\boxed{
I_j=h_nC_j-L_0R_j,
}
\tag{8.3}
$$


and


$$
\boxed{
mJ_j=(2h_{n+1}-mh_n)C_j-L_1R_j.
}
\tag{8.4}
$$



Thus, at every prime,


$$
\boxed{
\gcd(R_j,C_j)\mid\gcd(I_j,mJ_j).
}
\tag{8.5}
$$



The factor $m=n+1$ in (8.4) is retained. Removing it globally would be an unjustified denominator cancellation.

There is also the exact integer identity


$$
\boxed{
(2h_{n+1}-mh_n)I_j-h_n(mJ_j)
=2R_j\mathscr K_n.
}
\tag{8.6}
$$


Since $R_j\ne0$ in the retained endpoint construction and $\mathscr K_n\ne0$, the pair $(I_j,mJ_j)$ cannot be identically zero.

### 8.2 Exact equality of local ideals above the cutoff

At $p>n+2$, the scalars $m,n!$, and $2$ are units. The Legendre companion Wronskian implies that $\tau_n,\tau_{n+1}$ are not both divisible by $p$. Hence


$$
h_n,\quad 2h_{n+1}-mh_n=mn!\tau_{n+1}
$$


generate the unit ideal over $\mathbb Z_p$.

Equations (8.3)–(8.4) therefore prove


$$
\boxed{
(R_j,C_j)=(R_j,I_j,J_j)
\quad\text{as ideals in }\mathbb Z_p,
\qquad p>n+2.
}
\tag{8.7}
$$



In particular,


$$
\boxed{
v_p\gcd(R_j,C_j)
=
\min\{v_p(R_j),v_p(I_j),v_p(J_j)\}.
}
\tag{8.8}
$$



This is the projection scope of the recurrence reduction. It does **not** say that $(I_j,J_j)$ is primitive merely because a larger coefficient state is primitive.

If additionally $p\nmid\mathscr K_n$, then (8.6) also yields


$$
\boxed{
(R_j,C_j)=(I_j,J_j)
\quad\text{over }\mathbb Z_p.
}
\tag{8.9}
$$



The exceptional cost in this last elimination is explicitly supported on $\mathscr K_n$, whose recurrence and size have been proved.

### 8.3 What remains unbounded

Theorem 4.1 excludes cancellation where $p\mid G_j$. Where $G_j$ is a unit, however, the two affine expressions


$$
\beta_j\mathscr K_n+mh_nZ_nz_j,
$$




$$
-\alpha_j\mathscr K_n
+(2h_{n+1}-mh_n)Z_nz_j
$$


can both vanish modulo a prime while the full coefficient state remains primitive.

That is the precise remaining obstruction.

The bound


$$
|\mathscr K_n|\asymp(n!)^3
$$


does not exclude such congruences. Nor does it imply that their accumulated prime-power depth is $O(n)$, $o(n\log n)$, or any other sufficiently small quantity.

Thus the new recurrence gives an evaluated residual and eliminates the structural projected gcd, but it does not yet prove a useful infinite-family bound for the full endpoint-specific $\gcd(R_j,C_j)$.

---

## 9. Binary status and retained small-prime theorems

Theorem 4.1 supplies a new binary bound for the **complete structural residual intersection at both endpoints**:


$$
\boxed{
v_2\gcd(G_3,C_3)\le2v_2(n+1)+2,
}
$$




$$
\boxed{
v_2\gcd(G_0,C_0)
\le2v_2(n+1)+v_2(n+3)+2.
}
\tag{9.1}
$$



This is substantive all-prime bookkeeping: the structural intersection costs only $O(\log n)$, including endpoint $0$, and its proof uses the actual primitive row without assuming a binary normalization unit.

It is not a replacement for the separate binary quantities


$$
v_2(\gamma_j),\quad v_2(\xi_j),\quad v_2(\zeta_j).
$$


The complete endpoint-$0$ primitive-row/reference/force valuation classification requested in the assignment is not finished here. In particular, I do not turn (9.1) into an unproved formula for $v_2(d_0)$.

The previously proved endpoint-$3$ inequalities remain:


$$
v_2(\gamma_3)\le
\begin{cases}
2v_2(n!)-1,&n\equiv1\pmod4,\\
2v_2(n!),&n\equiv3\pmod4.
\end{cases}
$$



Likewise, the closed odd-prime results remain unchanged:

- for $p\ge5\mid n-1$,
  

$$
v_p(\gamma_j)=2v_p(n!),\qquad
  v_p(\zeta_j)=0,
$$


  without a reference-unit assumption;

- for odd $p\mid n+1$,
  

$$
v_p(\gamma_j)\le2v_p(n!),\qquad
  v_p(d_j)\le2v_p(n!)+v_p(\xi_j),
$$


  with the sharper $2v_p(n!)$ denominator bound only at the proved reference-unit scope.

No new all-prime unit claim for the Legendre reference sequence is used.

---

## 10. Actual denominators, all eight entries, and the whole error

The two corrected four-coordinate reconstruction columns are retained in full. No endpoint calculation below changes the least clearer over their eight entries or any row content.

At $n=3375$, the accepted actual row contents remain


$$
\boxed{
(113940000,\ 9780750,\ 10125,\ 1).
}
$$



The exact endpoint ratio and denominator remain


$$
\frac{v_j^{\rm rec}}{u_j^{\rm rec}}
=
\frac{E_nR_j+C_j}{n!R_j},
$$




$$
\boxed{
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,\ |E_nR_j+C_j|)}
=
\frac{|\gamma_jX_j|}
{\gcd(|\gamma_jX_j|,|V_j|)}.
}
\tag{10.1}
$$



At large primes only,


$$
(d_j)_{>n+2}
=
\frac{|R_j|_{>n+2}}
{\gcd(R_j,C_j)_{>n+2}}.
\tag{10.2}
$$


The all-prime formula is still (10.1), not (10.2).

For a reduced weight $\lambda=a/k$, retain


$$
J_{\rm wt}=B\widetilde v_0-A\widetilde v_3,
$$




$$
T_{\rm wt}=aJ_{\rm wt}+kA\widetilde v_3,
$$




$$
F_{\rm gcd}
=\gcd(|A|,|a|)\gcd(|B|,|a-k|),
$$




$$
G=\gcd(k,|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=
\gcd\!\left(h,\frac{|T_{\rm wt}|}{F_{\rm gcd}G}\right).
$$


Then the actual primitive pair is still


$$
\boxed{
q_\lambda=
\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda=
\operatorname{sgn}(AB)
\frac{T_{\rm wt}}{F_{\rm gcd}GH_{\rm gcd}}.
}
\tag{10.3}
$$



Every prime remains in this final gcd.

The complete same-index error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{10.4}
$$



### Retained finite whole-form evidence

The Turn 5 report records the accepted separate whole-form enclosures at $3375$:



$$
\begin{array}{c|c|r}
\text{Probe}&\text{sign}&
\lfloor\log_{10}|q(e+\pi)-p|\rfloor\\ \hline
3&-&43069\\
0&-&43068\\
1/2&-&68342\\
n^2/2&+&68338\\
\text{reference-canceling}&-&31327
\end{array}
$$



The attached complete-producer receipt itself explicitly says it did not compute those enclosures. I retain the accepted Turn 5 enclosure conclusions at their stated finite scope; I do not attribute them to a receipt that says otherwise.

All five whole forms are nonzero and larger than $1$ in absolute value. They prove neither an infinite exclusion nor irrationality.

---

## 11. The sharpened follow-on lemma

The structural intersection is now closed:


$$
\gcd(G_j,C_j)\mid\text{an explicit polynomial in }n.
$$



For $p>n+2$, all remaining endpoint-specific cancellation is therefore concentrated on $p\nmid G_j$, with exact depth


$$
\boxed{
\kappa_{j,p}
=
\min\{v_p(R_j),v_p(I_j),v_p(J_j)\}.
}
\tag{11.1}
$$


On this scope $v_p(R_j)=v_p(\xi_j)$.

A concrete next target is:

> **Projected inhomogeneous-Wronskian content lemma.**  
> On an infinite subsequence of $n=15^r$ or $105^r$, bound
> 

$$
> \sum_{\substack{p>n+2\\p\nmid G_0}}
> \min\{v_p(R_0),v_p(I_0),v_p(J_0)\}\log p
> +
> \sum_{\substack{p>n+2\\p\nmid G_3}}
> \min\{v_p(R_3),v_p(I_3),v_p(J_3)\}\log p,
>
$$


> using the actual recurrence (6.1), the evaluated residual
> 

$$
> \mathscr K_n=2(-1)^n(n!)^3+w_{1,n+1},
>
$$


> and the actual contact-row coefficients.

An $O(n)$ or $o(n\log n)$ estimate would be a meaningful arithmetic advance. It is not established here, and even such an estimate would still have to be combined with:

- the remaining small-prime reference and complete-force valuations;
- the actual denominator imbalance;
- all weight-dependent gcd factors in (10.3);
- the whole same-index analytic error.

The precise mathematical obstacle is no longer cancellation at the $G_j$-threshold. It is the simultaneous congruence of the two explicit affine projected expressions (8.1)–(8.2) with the actual reference projection.

---

## 12. Bounded exact arithmetic and proof status

### 12.1 No computation is needed for the new theorems

Theorem 4.1, the discrete recurrence, the projection identities, and the bound for $\mathscr K_n$ are proved symbolically.

There is no need to rerun:

- $n=225$;
- the $n=17$ direct validation;
- the $n=3375$ producer;
- the accepted $3/5/7$ selected-valuation extraction;
- any accepted whole-form enclosure.

### 12.2 Optional new certificate from the existing artifact

If a bounded check of the new identities is desired, it uses only archived exact data.

**Inputs**

- the actual primitive rows $r_0,r_3$;
- archived moment coefficients;
- archived force coefficients and reference values;
- the complete terminal columns.

Recover, by exact subtraction,


$$
b_k=u_k-E_nh_k-a_k,\qquad k=n,n+1,
$$


without regenerating any force.

**Expected verifiable outputs**

1. Zero residual in
   

$$
q_\partial\mathbf C-2mNZ_n=0.
$$



2. Zero residuals in
   

$$
I_j-h_nC_j+L_0R_j=0,
$$


   

$$
mJ_j-(2h_{n+1}-mh_n)C_j+L_1R_j=0.
$$



3. Zero residual in
   

$$
(2h_{n+1}-mh_n)I_j-h_n(mJ_j)-2R_j\mathscr K_n=0.
$$



4. Exact divisibility
   

$$
\gcd(G_3,C_3)\mid4m^2N^2,
$$


   

$$
\gcd(G_0,C_0)\mid4m^2N^2(n+3).
$$



5. The certified inequalities
   

$$
-(3(n!)^3)<\mathscr K_n<-(n!)^3
$$


   at the original odd index.

These are new identity checks on an existing artifact, not requests to repeat accepted producer work. No execution is claimed.

### 12.3 Status ledger

| Statement | Status |
|---|---|
| $3375$ selected $3/5/7$ endpoint valuations and $\eta_7=1$ | New receipt; finite corroboration |
| $241,211,2$ endpoint denominator values printed in complete receipt | Retained finite data |
| Inhomogeneous recurrence for $b_k=g_k-a_k$ | **New proof** |
| Complete terminal normal source $q_\partial\mathbf C=2mNZ_n$ | **New proof** |
| Polynomial all-prime bounds for $\gcd(G_j,C_j)$ | **New theorem** |
| $\gcd(G_j,C_j)_{>n+2}=1$ | **New theorem** |
| $(\gamma_j)_{>n+2}=(G_j)_{>n+2}$ | **New exact consequence** |
| Integral three-coordinate Wronskian recurrence | **New proof** |
| Complete residual integer $\mathscr K_n$ | **Explicitly evaluated by recurrence and identity** |
| Sign and factorial-scale bound for $\mathscr K_n$ | **New proof on all original indices** |
| Projection ideal equality (8.7) | **New proof at its stated unit scope** |
| Useful infinite-family bound for the remaining $\gcd(R_j,C_j)$ | Open |
| Full endpoint-$0$ binary reference/complete-force valuation classification | Open |
| Infinite actual-denominator versus whole-error comparison | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The zero-seeded reduction now yields more than an unevaluated terminal scalar.

The actual coefficient recurrence, with the exterior correction retained, evaluates the complete normal residual:


$$
\boxed{
q_\partial\mathbf C
=
2(n+1)(n+2)\bigl(2a_{n+1}-(n+1)a_n\bigr).
}
$$


Combined with the exact endpoint kernels and actual moment primitivity, it proves


$$
\boxed{
\gcd(G_3,C_3)\mid4(n+1)^2(n+2)^2,
}
$$




$$
\boxed{
\gcd(G_0,C_0)\mid4(n+1)^2(n+2)^2(n+3).
}
$$



Thus the structural large-prime residual intersection is eliminated at both endpoints. The remaining intersection is reduced, with exact denominator costs, to the actual projected integers $I_j,J_j$, built from an integral inhomogeneous Wronskian and the complete logarithmic correction.

The residual integer is nonzero and rigorously bounded:


$$
\boxed{
\mathscr K_n
=
2(-1)^n(n!)^3+h_nb_{n+1}-h_{n+1}b_n,
\qquad
(n!)^3<|\mathscr K_n|<3(n!)^3.
}
$$



What is still missing is a strong arithmetic bound for the simultaneous projected congruences involving $R_j,I_j,J_j$, not a seed-unit argument and not a full-state determinant. That bound must then be combined with the remaining small-prime costs and the actual all-prime primitive denominator in the whole same-index error.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ has been obtained.}}
$$


