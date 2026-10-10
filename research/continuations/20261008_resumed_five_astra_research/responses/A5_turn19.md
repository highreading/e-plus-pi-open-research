> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A paid Hermite-anchored lift of the remaining second collisions

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved. **The full exponential bound for the remaining non-arc interval is not proved in this report.**

The input to this turn is the already evaluated second collision


$$
d_{p,N}^{\mathrm{block}}=p^2,
$$


not an unevaluated first-block problem. Starting from that input, this report proves a new, exact, all-depth identity for the error in the second-precision block. The identity is anchored in the **actual** $p$-base states and actual Hermite integers. Its first reduction evaluates the complete next source and endpoint digits modulo $p^3$.

The resulting invariant has three useful properties.

1. At determinant-unit primes, its full valuation is exactly $c_p-2$. It preserves the original target
   

$$
\Theta_\ell^*=\frac{\mathscr I_2}{\Delta},
   \qquad
   \Theta_{\ell-1}^*=-\frac{\mathscr I_1}{\Delta}.
$$



2. At critical determinant primes, the difference between the invariant’s valuation and $c_p-2$ is nonnegative and at most $v_p(\Delta)$. The sum of these **conditioning losses**, with logarithmic weights, is $O(N)$. This does **not** pay the remaining state-proximity depth at those primes.

3. After the complete endpoint and Hermite credits, there is an exact paid reduction of the remaining mass: the first two source-depth layers cost at most
   

$$
4N\log 2,
$$


   and the error in replacing the remaining depth by the new contact invariant costs at most $\log|\Delta|=O(N)$.

What remains unproved is an $O(N)$ upper bound for the contact invariant’s surviving positive-part mass. Its third digit is evaluated below, but its universal nonvanishing is not established. Thus this is a **new proved lifting and payment identity**, not a solution of the requested interval noncollision problem.

No original-index counterexample is claimed. No original-sized computation or prime scan is proposed.

---

## 1. Original objects, exact scope, and reuse

Throughout,


$$
\boxed{N=9^{18+32u}=3^{36+64u},\qquad u\in\mathbb Z_{\ge0},}
$$


and


$$
n=2N,\qquad m=N-3,\qquad \ell=2N-6.
$$


The physical terminal is $n$.

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


with


$$
C_0=1,\quad C_1=2t-1,\quad
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
F=\alpha C_N-\beta C_{N-1},\qquad F(\pm i)=\delta,
\qquad \gcd(\alpha,\beta)=1.
$$



For integer polynomials,


$$
\eta(H)=\sum_j j![z^j]H(1-z),\qquad
E(H)=\sum_j(-1)^jj![t^j]H(t).
$$


Set


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad K=\mathcal H C_m^2,
$$




$$
U=-\eta(K),\qquad V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$


The supplied original-domain normalization remains


$$
\operatorname{cont}(W_{\rm raw})=g_B^2c,\qquad
\tau=\frac Uc,\quad \nu=\frac Vc,
$$




$$
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2,
$$


with $U,V,M>0$.

### 1.1 The exact multiplier depth

Put


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


Write


$$
E_K=E(K),\qquad y_K=d_KE_K-a_K.
$$


Then $\gcd(d_K,y_K)=1$.

The intrinsic factors remain


$$
\gamma=\gcd(\tau,y_K),\qquad
b^\circ=\gcd(\gamma,a_K),\qquad r^\circ=\gamma/b^\circ.
$$


For every prime,


$$
\boxed{
k_p=v_p(\kappa_N^{\rm prod})
=[c_p-h_p-2b_p-2(z_p-t_p)_+]_+,
}
\tag{1.1}
$$


where


$$
c_p=\min(v_p(U),v_p(V)),\qquad t_p=v_p(U)-c_p,
$$




$$
z_p=v_p(y_K),\qquad b_p=v_p(b^\circ),\qquad
h_p=v_p(Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}).
$$


For convenience, define the **actual complete credit**


$$
\boxed{H_p=h_p+2b_p+2(z_p-t_p)_+.}
\tag{1.2}
$$


No component of $H_p$ will be discarded or replaced by a residual-index analogue.

### 1.2 The complete original columns

The affine states have seeds


$$
\Theta_0=\Phi_0=0,\qquad \Theta_1=\Phi_1=1,
$$


and, for exactly $1\le j\le n-1$,


$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
\tag{1.3}
$$


Equivalently, their full finite affine matrices are


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
\tag{1.4}
$$


Both third coordinates are retained.

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


The corrected $K$-columns are


$$
16U=\mathscr C_U-\mathscr A\Theta_\ell-\mathscr B\Theta_{\ell-1},
$$




$$
16E_K=\mathscr C_E+\mathscr A\Phi_\ell+\mathscr B\Phi_{\ell-1}.
\tag{1.5}
$$



At the physical terminal,


$$
V=C_V-P\Theta_n-Q\Theta_{n-1},
$$




$$
E_F=C_F^E-P\Phi_n-Q\Phi_{n-1},
\tag{1.6}
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
\tag{1.7}
$$


In particular, neither $-\delta^2$ nor $4\alpha\beta$ is omitted.

### 1.3 What is reused, rather than recalculated

The completed turn18 proves the exact common-center columns


$$
V=C^{\rm s}-\Pi\Theta_\ell-\Omega\Theta_{\ell-1},
$$




$$
E_F=C^{\rm e}-\Pi\Phi_\ell-\Omega\Phi_{\ell-1}.
\tag{1.8}
$$


These are the actual six-step transports from $\ell$ to $n=\ell+6$.

For an unambiguous self-contained definition, let


$$
T_j=\begin{pmatrix}-4j&1\\1&0\end{pmatrix},
\qquad
T=T_{\ell+5}\cdots T_\ell.
$$


Let $f,g$ be the two forcing vectors supplied by the corresponding six affine steps in (1.4), starting at the even index $\ell$. Then


$$
(\Pi,\Omega)=(P,Q)T,\qquad
C^{\rm s}=C_V-(P,Q)f,\qquad
C^{\rm e}=C_F^E-(P,Q)g.
$$


The already evaluated quadratic forms and forcing scalars are reuse; their closed six-step calculation is not repeated here.

Retain


$$
\Delta=\mathscr A\Omega-\mathscr B\Pi<0,
$$




$$
\mathscr I_1=\Pi\mathscr C_U-\mathscr A C^{\rm s},\qquad
\mathscr I_2=\Omega\mathscr C_U-\mathscr B C^{\rm s},
$$


and


$$
J_N^{\rm aff}=\gcd(\mathscr I_1,\mathscr I_2)>0.
$$


The exact identities are


$$
16\Pi U-\mathscr A V=\mathscr I_1+\Delta\Theta_{\ell-1},
$$




$$
16\Omega U-\mathscr B V=\mathscr I_2-\Delta\Theta_\ell.
\tag{1.9}
$$


Their proved depth consequence is


$$
v_p(\Delta)>v_p(J_N^{\rm aff})
\quad\Longrightarrow\quad c_p\le v_p(J_N^{\rm aff}).
\tag{1.10}
$$


The numerical bill is


$$
J_N^{\rm aff}
<
10^{10}(2N)^{15}\frac{5^{4N}}{g_B^2}.
\tag{1.11}
$$



The completed non-arc $p^2$-block and its binomial payment are also reuse. The favorable source proof review does not supply the missing coverage theorem. The supplied $p=23,a=3$ receipt is a **PASS at its stated auxiliary finite scope**; its computation is closed and is neither rerun nor enlarged here.

---

## 2. The actual remaining branch and its finite boundaries

Let


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
\tag{2.1}
$$


Thus every $p\in\mathcal S_N$ satisfies


$$
p^2\mid U,\qquad p^2\mid V.
\tag{2.2}
$$


These are the actually remaining second collisions after removing the two already paid sets.

Write


$$
r=n-p,\qquad s=r-6,\qquad k=\frac{p+1}{2}.
\tag{2.3}
$$



### Lemma 2.1 — The non-arc residual is at least $13$

For every $p\in\mathcal S_N$,


$$
\boxed{13\le r<N,\qquad r\ \text{odd},\qquad s\ge7,\qquad k\le N-6.}
\tag{2.4}
$$



**Proof.**
Since $n$ is even and $p$ is odd, $r$ is odd. Also $p>N$ gives $r<N$.

The factors of $L(\ell^2)$ are


$$
n-7,\ n-5,\ n-9,\ n-3,\ n-11,\ n-1.
$$


Each is positive and smaller than $2p$. Consequently, a prime $p>N$ divides one of these factors precisely when it equals that factor. Thus the excluded non-arc residuals are exactly


$$
r=1,3,5,7,9,11.
$$


Hence $r\ge13$. Finally,


$$
k=N-\frac{r-1}{2}\le N-6.
$$


∎

This elementary observation matters for the new lift:

- $(\ell,\ell-1)=(p+s,p+s-1)$ always lies in the genuine residual block;
- no negative residual indices or exceptional $r=3,5$ formulas occur;
- all Hermite indices used below are at most $N$;
- all shifted recurrence steps end at $p+r-1=n-1$.

Also,


$$
p\nmid d_K,
\tag{2.5}
$$


because the only prime factors of $30g_{\rm arc}$ are much smaller than $N$, and $p\nmid L(\ell^2)$. This does **not** imply $p\nmid a_K$, and therefore does not remove the $b_p$-credit from (1.1).

---

## 3. Reuse notation for the evaluated block

For a residual sequence $Z_j$, write


$$
\mathcal L_j Z=Z_{j+1}+4jZ_j-Z_{j-1}.
$$



The already established block uses


$$
\mathcal L_j\mathcal A=\mathcal L_j\mathcal B=0,
$$


with


$$
(\mathcal A_0,\mathcal A_1)=(1,0),\qquad
(\mathcal B_0,\mathcal B_1)=(0,1),
$$


and


$$
\begin{aligned}
\mathcal L_j\mathcal D&=-4\mathcal A_j,&
\mathcal L_j\mathcal E&=-4\mathcal B_j,\\
\mathcal L_j\mathcal T&=-4\Theta_j,&
\mathcal L_j\mathcal W&=-4\Phi_j,
\end{aligned}
\tag{3.1}
$$


where


$$
(\mathcal D_0,\mathcal D_1)=(0,-4),
$$


and the other three pairs of initial values are zero. All recurrences here have $1\le j\le r-1$.

Put


$$
\begin{aligned}
H_j^+&=\mathcal A_j\Theta_p+
 \mathcal B_j(\Theta_{p-1}+1)+\Theta_j,\\
K_j^+&=\mathcal D_j\Theta_p+
 \mathcal E_j(\Theta_{p-1}+1)+\mathcal T_j,
\end{aligned}
$$




$$
\begin{aligned}
H_j^-&=\mathcal A_j\Phi_p+
 \mathcal B_j(\Phi_{p-1}-1)-\Phi_j,\\
K_j^-&=\mathcal D_j\Phi_p+
 \mathcal E_j(\Phi_{p-1}-1)-\mathcal W_j.
\end{aligned}
$$


Then the reused block is


$$
X_j^\pm=H_j^\pm+pK_j^\pm,
$$




$$
\Theta_{p+j}\equiv X_j^+\pmod{p^2},\qquad
\Phi_{p+j}\equiv X_j^-\pmod{p^2}.
\tag{3.2}
$$


No first-block calculation is being proposed or claimed as new.

---

# Part I. A new actual Hermite-anchored lifting identity

## 4. The $p$-base Hermite defects must be retained

The Hermite integers satisfy


$$
P_0^{\mathrm H}=Q_0^{\mathrm H}=1,\qquad
P_1^{\mathrm H}=3,\quad Q_1^{\mathrm H}=1,
$$




$$
Z_{a+1}=(4a+2)Z_a+Z_{a-1},\qquad 1\le a\le N-1.
\tag{4.1}
$$



Let


$$
\chi_p=2k!.
$$


The universal $p$-base identities proved in turn17 imply


$$
\Theta_p\equiv\chi_p Q_{k-1}^{\mathrm H},\qquad
\Theta_{p-1}+1\equiv-\chi_p Q_k^{\mathrm H}\pmod p,
$$




$$
\Phi_p\equiv\chi_p P_{k-1}^{\mathrm H},\qquad
\Phi_{p-1}-1\equiv-\chi_p P_k^{\mathrm H}\pmod p.
\tag{4.2}
$$



Here the scope requires care. The full Gaussian arc jet of turn17 is **not** being transferred to the present non-arc branch. Only its preceding universal $p$-base moment identities are used. Their proof requires an odd prime, the states through $p$, and Hermite indices through $k$. Those hypotheses hold here because


$$
p<n,\qquad k\le N-6.
$$


No condition $p\mid2N-1$ is used in (4.2).

Define the four exact integer defects


$$
\sigma_0^+
=\frac{\Theta_p-\chi_p Q_{k-1}^{\mathrm H}}p,\qquad
\sigma_1^+
=\frac{\Theta_{p-1}+1+\chi_p Q_k^{\mathrm H}}p,
$$




$$
\sigma_0^-
=\frac{\Phi_p-\chi_p P_{k-1}^{\mathrm H}}p,\qquad
\sigma_1^-
=\frac{\Phi_{p-1}-1+\chi_p P_k^{\mathrm H}}p.
\tag{4.3}
$$


These are integral by (4.2).

They are not free correction coordinates. They are determined by the actual $p$-base states. In particular, replacing the left sides of (4.2) by their Hermite reductions modulo $p^2$ or $p^3$ would improperly discard (4.3).

### 4.1 Two completely specified Hermite-anchored columns

Define


$$
Z_{0,j}^+
=\chi_p(\mathcal A_jQ_{k-1}^{\mathrm H}
        -\mathcal B_jQ_k^{\mathrm H})+\Theta_j,
$$




$$
Z_{1,j}^+
=\chi_p(\mathcal D_jQ_{k-1}^{\mathrm H}
        -\mathcal E_jQ_k^{\mathrm H})
 +\mathcal T_j
 +\mathcal A_j\sigma_0^+
 +\mathcal B_j\sigma_1^+,
\tag{4.4}
$$


and


$$
Z_{0,j}^-
=\chi_p(\mathcal A_jP_{k-1}^{\mathrm H}
        -\mathcal B_jP_k^{\mathrm H})-\Phi_j,
$$




$$
Z_{1,j}^-
=\chi_p(\mathcal D_jP_{k-1}^{\mathrm H}
        -\mathcal E_jP_k^{\mathrm H})
 -\mathcal W_j
 +\mathcal A_j\sigma_0^-
 +\mathcal B_j\sigma_1^-.
\tag{4.5}
$$


Put


$$
Z_j^\pm=Z_{0,j}^\pm+pZ_{1,j}^\pm.
$$



Substitution of (4.3) into the reused block gives the exact algebraic relation


$$
\boxed{
X_j^\pm
=
Z_j^\pm+
p^2(\mathcal D_j\sigma_0^\pm+
     \mathcal E_j\sigma_1^\pm).
}
\tag{4.6}
$$


Consequently, the following quotients are integers:


$$
\mathfrak e_j^+
=\frac{\Theta_{p+j}-Z_j^+}{p^2},\qquad
\mathfrak e_j^-
=\frac{\Phi_{p+j}-Z_j^-}{p^2}.
\tag{4.7}
$$



The purpose of the next theorem is to evaluate these quotients by an exact finite recurrence, rather than leave them as divided differences.

---

## 5. New theorem: the exact all-depth quotient recurrence

### Theorem 5.1 — Hermite-anchored second-collision transport

For every original $N$, every $p\in\mathcal S_N$, and $0\le j\le r$, the integers in (4.7) satisfy


$$
\boxed{
\mathfrak e_0^\pm=0,\qquad
\mathfrak e_1^\pm=-4\sigma_0^\pm,
}
\tag{5.1}
$$


and


$$
\boxed{
\mathfrak e_{j+1}^\pm
+4(p+j)\mathfrak e_j^\pm
-\mathfrak e_{j-1}^\pm
=-4Z_{1,j}^\pm,
\qquad 1\le j\le r-1.
}
\tag{5.2}
$$


In particular,


$$
\boxed{
\Theta_{p+j}=Z_j^++p^2\mathfrak e_j^+,\qquad
\Phi_{p+j}=Z_j^-+p^2\mathfrak e_j^-,
}
\tag{5.3}
$$


as exact integer identities, not merely modulo $p^3$.

**Proof.**
From (3.1), (4.4), and the original source forcing,


$$
\mathcal L_j Z_0^+=2,\qquad
\mathcal L_j Z_1^+=-4Z_{0,j}^+.
$$


Similarly, the endpoint’s residual forcing has the required opposite sign:


$$
\mathcal L_j Z_0^-=-2(-1)^j,\qquad
\mathcal L_j Z_1^-=-4Z_{0,j}^-.
$$


The first endpoint forcing is precisely


$$
-2(-1)^j=2(-1)^{p+j},
$$


since $p$ is odd.

It follows, by direct substitution, that


$$
Z_{j+1}^\pm+4(p+j)Z_j^\pm-Z_{j-1}^\pm
=f_j^\pm+4p^2Z_{1,j}^\pm,
$$


where


$$
f_j^+=2,\qquad f_j^-=2(-1)^{p+j}.
$$


Subtract this identity from the appropriate original recurrence at $p+j$, and divide by the already proved factor $p^2$. This gives (5.2).

At $j=0$, the definitions of $\sigma_0^\pm$ give exact equality between the original base state and $Z_0^\pm$. At $j=1$, the recurrence at $p$, together with (4.3), gives


$$
\Theta_{p+1}-Z_1^+=-4p^2\sigma_0^+,
$$




$$
\Phi_{p+1}-Z_1^-=-4p^2\sigma_0^-.
$$


Thus (5.1) holds.

All steps end at $p+r-1=n-1$, so no above-terminal recurrence is used. ∎

This is the new paid identity. Its forcing is fully specified by the actual Hermite integers, actual $p$-base defects, and actual residual $\Theta,\Phi$. It contains no unevaluated factorial moment.

---

## 6. Evaluation of the next digit

Define four new residual sequences, all with zero values at $0,1$, by


$$
\begin{aligned}
\mathcal L_j\mathcal D^{\langle2\rangle}
  &=-4\mathcal D_j,&
\mathcal L_j\mathcal E^{\langle2\rangle}
  &=-4\mathcal E_j,\\
\mathcal L_j\mathcal T^{\langle2\rangle}
  &=-4\mathcal T_j,&
\mathcal L_j\mathcal W^{\langle2\rangle}
  &=-4\mathcal W_j.
\end{aligned}
\tag{6.1}
$$


Again, $1\le j\le r-1$. These recurrences use integer operations only.

Set


$$
\begin{aligned}
Y_j^+={}&
\mathcal D_j\sigma_0^+
+\mathcal E_j\sigma_1^+\\
&+\chi_p\bigl(
\mathcal D_j^{\langle2\rangle}Q_{k-1}^{\mathrm H}
-\mathcal E_j^{\langle2\rangle}Q_k^{\mathrm H}
\bigr)
+\mathcal T_j^{\langle2\rangle},
\end{aligned}
\tag{6.2}
$$




$$
\begin{aligned}
Y_j^-={}&
\mathcal D_j\sigma_0^-
+\mathcal E_j\sigma_1^-\\
&+\chi_p\bigl(
\mathcal D_j^{\langle2\rangle}P_{k-1}^{\mathrm H}
-\mathcal E_j^{\langle2\rangle}P_k^{\mathrm H}
\bigr)
-\mathcal W_j^{\langle2\rangle}.
\end{aligned}
\tag{6.3}
$$



### Proposition 6.1 — Evaluated third precision

For $0\le j\le r$,


$$
\boxed{\mathfrak e_j^\pm\equiv Y_j^\pm\pmod p.}
\tag{6.4}
$$


Consequently,


$$
\boxed{
\Theta_{p+j}\equiv Z_j^++p^2Y_j^+\pmod{p^3},
\qquad
\Phi_{p+j}\equiv Z_j^-+p^2Y_j^-\pmod{p^3}.
}
\tag{6.5}
$$



**Proof.**
Equations (3.1) and (6.1) give, exactly,


$$
\mathcal L_jY^\pm=-4Z_{1,j}^\pm.
$$


Their initial values are


$$
Y_0^\pm=0,\qquad Y_1^\pm=-4\sigma_0^\pm.
$$


Modulo $p$, these are the recurrence and seeds of (5.1)–(5.2). Uniqueness of the finite recurrence gives (6.4), and (5.3) gives (6.5). ∎

This evaluation is source-specific in the required sense:

- $Q_{k-1}^{\mathrm H},Q_k^{\mathrm H},P_{k-1}^{\mathrm H},P_k^{\mathrm H}$ are the actual finite Hermite integers;
- $\sigma^\pm$ are the actual divided $p$-base defects;
- $\mathcal T,\mathcal W$ and their second corrections retain both affine forcings;
- Gaussian data enter the source tests through the actual divided $\alpha,\beta,\delta$, without replacing $N$ by $r$ or $s$.

---

# Part II. The actual next Gaussian–Hermite collision

## 7. All four complete columns at the new precision

Define the exact integers


$$
B_U=\mathscr C_U-\mathscr A Z_s^+-\mathscr B Z_{s-1}^+,
$$




$$
B_V=C_V-PZ_r^+-QZ_{r-1}^+.
\tag{7.1}
$$


By (5.3),


$$
16U=B_U-p^2(\mathscr A\mathfrak e_s^+
                    +\mathscr B\mathfrak e_{s-1}^+),
$$




$$
V=B_V-p^2(P\mathfrak e_r^+
                    +Q\mathfrak e_{r-1}^+).
\tag{7.2}
$$


Since $p^2\mid U,V$, both $B_U$ and $B_V$ are divisible by $p^2$.

The new source digit is therefore the completely specified pair


$$
\boxed{
\begin{aligned}
\mathscr L_U&=
\frac{B_U}{p^2}
-\mathscr A Y_s^+-\mathscr B Y_{s-1}^+,\\
\mathscr L_V&=
\frac{B_V}{p^2}
-PY_r^+-QY_{r-1}^+
\end{aligned}
\pmod p.
}
\tag{7.3}
$$


It evaluates


$$
\boxed{
\mathscr L_U\equiv\frac{16U}{p^2},\qquad
\mathscr L_V\equiv\frac V{p^2}\pmod p.
}
\tag{7.4}
$$



The two complete endpoint outputs are


$$
\boxed{
\begin{aligned}
16E_K\equiv{}&
\mathscr C_E+\mathscr A Z_s^-+\mathscr B Z_{s-1}^-\\
&+p^2(\mathscr A Y_s^-+\mathscr B Y_{s-1}^-)
\pmod{p^3},
\end{aligned}}
\tag{7.5}
$$




$$
\boxed{
\begin{aligned}
E_F\equiv{}&
C_F^E-PZ_r^--QZ_{r-1}^-\\
&-p^2(PY_r^-+QY_{r-1}^-)
\pmod{p^3}.
\end{aligned}}
\tag{7.6}
$$


Thus $y_K=d_KE_K-a_K$ is evaluated to the same precision using the actual reduced $a_K,d_K$.

These formulas retain all four constants


$$
\mathscr C_U,\quad \mathscr C_E,\quad
\alpha^2+(2n-3)\beta^2-\delta^2,\quad
\alpha^2+(5-2n)\beta^2+4\alpha\beta.
$$


No endpoint is replaced by its source counterpart.

### Corollary 7.1 — Exact effect of a nonzero third source digit

If


$$
(\mathscr L_U,\mathscr L_V)\ne(0,0)\pmod p,
$$


then


$$
\boxed{c_p=2,\qquad k_p=[2-H_p]_+.}
\tag{7.7}
$$



**Proof.**
The second-collision input gives $c_p\ge2$. Equation (7.4) shows that at least one source has valuation exactly $2$, so $c_p=2$. Apply (1.1). ∎

This is an all-depth conclusion at a prime where the new digit is nonzero: it excludes **every** common source depth above $2$, not merely the next displayed congruence.

The report does not prove that the pair in (7.3) is always nonzero.

---

## 8. The new contact invariant and the unchanged exact target

The common-center form makes the next obstruction especially precise.

Define


$$
\rho_\ell=\frac{\mathscr I_2-\Delta Z_s^+}{p^2},
\qquad
\rho_{\ell-1}=\frac{\mathscr I_1+\Delta Z_{s-1}^+}{p^2}.
\tag{8.1}
$$


Both are integers. Indeed, (1.9), (2.2), and (5.3) show that their numerators are divisible by $p^2$.

Define the exact contact vector


$$
\boxed{
\mathbf T_{p,N}=
\begin{pmatrix}
\rho_\ell-\Delta\mathfrak e_s^+\\
\rho_{\ell-1}+\Delta\mathfrak e_{s-1}^+
\end{pmatrix}.
}
\tag{8.2}
$$



### Theorem 8.1 — Actual Gaussian–Hermite contact identity

For every $p\in\mathcal S_N$,


$$
\boxed{
\mathbf T_{p,N}
=
\begin{pmatrix}
\Omega&-\mathscr B\\
\Pi&-\mathscr A
\end{pmatrix}
\begin{pmatrix}
16U/p^2\\
V/p^2
\end{pmatrix}.
}
\tag{8.3}
$$


Its reduction modulo $p$ is explicitly


$$
\boxed{
\mathbf T_{p,N}\equiv
\begin{pmatrix}
\rho_\ell-\Delta Y_s^+\\
\rho_{\ell-1}+\Delta Y_{s-1}^+
\end{pmatrix}
\pmod p.
}
\tag{8.4}
$$



**Proof.**
Using (5.3),


$$
\begin{aligned}
p^2(\rho_\ell-\Delta\mathfrak e_s^+)
&=\mathscr I_2-\Delta\Theta_\ell\\
&=16\Omega U-\mathscr B V.
\end{aligned}
$$


Similarly,


$$
\begin{aligned}
p^2(\rho_{\ell-1}+\Delta\mathfrak e_{s-1}^+)
&=\mathscr I_1+\Delta\Theta_{\ell-1}\\
&=16\Pi U-\mathscr A V.
\end{aligned}
$$


Divide by the proved factor $p^2$. Equation (8.4) follows from Proposition 6.1. ∎

This is not an arbitrary affine target. The numerators $\mathscr I_1,\mathscr I_2$, the determinant $\Delta$, the base defects, and the forced corrections are all fixed by the original objects.

### 8.1 Determinant-unit primes

Suppose $p\nmid\Delta$. The matrix in (8.3) has determinant $-\Delta$, a $p$-adic unit. Hence


$$
\boxed{
c_p-2
=
\min\bigl(
v_p(\rho_\ell-\Delta\mathfrak e_s^+),
v_p(\rho_{\ell-1}+\Delta\mathfrak e_{s-1}^+)
\bigr).
}
\tag{8.5}
$$



Moreover,


$$
\Theta_\ell-\frac{\mathscr I_2}{\Delta}
=
p^2\left(\mathfrak e_s^+-\frac{\rho_\ell}{\Delta}\right),
$$




$$
\Theta_{\ell-1}+\frac{\mathscr I_1}{\Delta}
=
p^2\left(\mathfrak e_{s-1}^+
              +\frac{\rho_{\ell-1}}{\Delta}\right).
\tag{8.6}
$$


Thus the target remains exactly


$$
\boxed{
\Theta_\ell^*=\frac{\mathscr I_2}{\Delta},
\qquad
\Theta_{\ell-1}^*=-\frac{\mathscr I_1}{\Delta}.
}
\tag{8.7}
$$


There is no replacement by a leading coefficient, a homogeneous target, or a target with the forcing constants removed.

In particular, a third common depth survives precisely when


$$
\boxed{
\rho_\ell\equiv\Delta Y_s^+,\qquad
\rho_{\ell-1}\equiv-\Delta Y_{s-1}^+\pmod p.
}
\tag{8.8}
$$


Equation (8.8) is the evaluated next collision, not a nonvanishing theorem.

### 8.2 Critical determinant primes

Put


$$
d_p=v_p(\Delta),\qquad
a_p=\min\bigl(v_p(T_{p,N,1}),v_p(T_{p,N,2})\bigr).
$$


Then


$$
\boxed{c_p-2\le a_p\le c_p-2+d_p.}
\tag{8.9}
$$



**Proof.**
The first inequality follows from (8.3), since its coefficients are integers.

For the second, multiply (8.3) by the integer adjugate matrix. The result is $-\Delta$ times the source vector. Every coordinate of that adjugate product has valuation at least $a_p$. Therefore


$$
d_p+(c_p-2)\ge a_p.
$$


∎

This proves an exact bound on determinant-conditioning loss. It does **not** prove $c_p\le d_p+2$. The latter would require an additional bound on $a_p$, which is precisely the remaining state-proximity problem.

The direct source test (7.3) remains valid at critical primes and uses no determinant inversion. The adjugate reduction (8.4), by contrast, can vanish because of determinant divisibility even when the direct source digit is nonzero.

---

# Part III. A quantified payment and its precise limitation

## 9. The first two depths and determinant losses are summably paid

The complete post-credit depth admits a simple exact decomposition.

### Lemma 9.1 — Exact post-second-collision payment

For $c_p\ge2$,


$$
\boxed{
k_p=[2-H_p]_+
+\bigl[c_p-2-(H_p-2)_+\bigr]_+.
}
\tag{9.1}
$$



**Proof.**
If $H_p\le2$, the right side is $2-H_p+c_p-2=c_p-H_p$.
If $H_p>2$, it is $[c_p-H_p]_+$.
Both equal (1.1). ∎

Since every $p\in\mathcal S_N$ lies in $N<p<2N$,


$$
v_p\binom{2N}{N}=1.
$$


Therefore


$$
\boxed{
\prod_{p\in\mathcal S_N}p^{[2-H_p]_+}
\mid \binom{2N}{N}^{\,2},
}
\tag{9.2}
$$


and


$$
\boxed{
\sum_{p\in\mathcal S_N}[2-H_p]_+\log p
\le4N\log2.
}
\tag{9.3}
$$



This payment covers the first two layers at **every** remaining second collision, with the actual credits already deducted.

### 9.1 A full-depth comparison with an exponentially paid error

Define


$$
\mathfrak C_N^{\rm lift}
=
\sum_{p\in\mathcal S_N}
\bigl[a_p-(H_p-2)_+\bigr]_+\log p.
\tag{9.4}
$$


Here $a_p$ is the valuation of the explicit actual vector (8.2), evaluated at its first surviving digit by (8.4).

The function $x\mapsto[x-B]_+$ is nondecreasing and $1$-Lipschitz. Hence (8.9) and (9.1) give


$$
\boxed{
\begin{aligned}
0\le{}&
\sum_{p\in\mathcal S_N}[2-H_p]_+\log p
+\mathfrak C_N^{\rm lift}
-\sum_{p\in\mathcal S_N}k_p\log p\\
\le{}&\sum_{p\in\mathcal S_N}d_p\log p
\le\log|\Delta|.
\end{aligned}}
\tag{9.5}
$$



The inherited coefficient bounds for $\mathscr A,\mathscr B,\Pi,\Omega$, together with the already paid Gaussian division, give the immediate bound


$$
|\Delta|
<
10^{10}(2N)^{15}\frac{5^{4N}}{g_B^2}.
\tag{9.6}
$$


Thus the error term in (9.5) is $O(N)$.

Equations (9.3) and (9.5) constitute a **new universal paid identity on the remaining second-collision branch**. They do not rely on an unproved coverage assertion for a newly selected set of primes.

Their limitation is equally exact:



$$
\boxed{\text{No upper bound }\mathfrak C_N^{\rm lift}=O(N)\text{ is proved.}}
\tag{9.7}
$$



At determinant-unit primes, (9.5) has no determinant loss at all. At critical determinant primes, only the conditioning loss is paid by (9.6); their surviving contact depth remains inside (9.4).

---

## 10. Why the evaluated invariant does not yet prove noncollision

There are three distinct obstructions.

### 10.1 A unit determinant does not exclude the next actual cancellation

At a determinant-unit prime, (8.8) is a pair of congruences between fixed, source-specific integers. The new derivation evaluates both sides. It does not show that they differ.

In particular, $\Delta$ being a unit only permits the exact equivalence (8.5). It supplies no nonvanishing of


$$
\rho_\ell-\Delta Y_s^+,\qquad
\rho_{\ell-1}+\Delta Y_{s-1}^+.
$$



The exponential heights of $\mathscr I_1,\mathscr I_2,\Delta$ do not repair this. The integers $\rho_\ell,\rho_{\ell-1}$ include the actual $p$-base states and the actual carries in the divisions by $p^2$. Their proximity to the forced corrections is not bounded by the heights of $\mathscr I_1,\mathscr I_2,\Delta$ alone.

### 10.2 A double-zero input does not determine the third digit

The hypothesis


$$
d_{p,N}^{\rm block}=p^2
$$


proves the integrality of every division by $p^2$ in Sections 7 and 8. It does not determine those quotients modulo $p$. Their evaluation requires the extra precision explicitly billed below.

Thus the new invariant genuinely identifies an additional arithmetic obligation. It is not already decided by the admitted second-precision block.

### 10.3 Fixed-prime index lifting does not cover this interval

The original indices satisfy


$$
\frac{N_{u+1}}{N_u}=3^{64}>2.
$$


Consequently, for a fixed prime $p$, **at most one** original index satisfies


$$
N<p<2N.
\tag{10.1}
$$



Therefore an argument that varies $u$ through a congruence class at a fixed $p$ cannot produce a family of admissible interval lifts. Such an argument may concern genuine original indices in another range, but it does not establish a pointwise bound for the present interval.

No generic zero of (8.8), and no auxiliary numerical choice of its inputs, would be an original-index counterexample.

---

## 11. A concrete repaired continuation lemma

The new formulas support the following precise next lemma.

> **Third-depth avoidance lemma — open.**  
> For every original $N$ and every $p\in\mathcal S_N$, the pair in (7.3), formed from the actual divided Gaussian coefficients, actual $p$-base defects, and the two complete forced systems, is nonzero modulo $p$.

This permits common source depth $2$; it only excludes common depth $3$. It is therefore weaker than universal mod-$p^2$ noncollision and still sufficient for the desired exponential interval bound.

At determinant-unit primes it is exactly the assertion that the evaluated pair in (8.8) does not collide. At critical determinant primes it must be tested through the direct pair (7.3), or through a fully paid saturated equivalent—not by pretending that $\Delta$ is a unit.

### Conditional consequence

If the third-depth avoidance lemma holds, then every prime in $\mathcal S_N$ has


$$
k_p=[2-H_p]_+\le2.
$$


Combining this with the already paid turn18 sets gives


$$
\boxed{
\prod_{\substack{N<p<2N\\p\nmid L(\ell^2)}}p^{k_p}
\mid
J_N^{\rm aff}\binom{2N}{N}^{\,2}.
}
\tag{11.1}
$$


Hence, conditionally,


$$
\boxed{
\prod_{\substack{N<p<2N\\p\nmid L(\ell^2)}}p^{k_p}
<
10^{10}(2N)^{15}\frac{10000^N}{g_B^2}.
}
\tag{11.2}
$$



This implication is rigorous. Its hypothesis is not proved.

A weaker, fully post-credit alternative would suffice: prove


$$
c_p\le H_p+2
$$


at every remaining prime, or prove a summable upper bound for the exceptions. The exact recurrence (5.2) is valid at the necessary higher precision. But merely writing that recurrence does not establish the required nonvanishing.

In particular, when a third collision survives, the present report does not assign it an unsupported depth cap.

---

# Part IV. Precision, divisions, and a bounded receipt

## 12. Exact precision and division bill

The following distinctions are essential.

### 12.1 Gaussian division

Let


$$
a=v_p(g_B),\qquad g_B=p^a g_0,\qquad p\nmid g_0.
$$


To obtain the actual $\alpha,\beta,\delta$ modulo $p^3$, one may use the raw linear Gaussian data modulo $p^{a+3}$, divide their proved $p^a$-factors, and then divide by the actual unit $g_0$ modulo $p^3$.

If instead a raw quadratic source or remainder is evaluated and divided afterwards, it must be known modulo


$$
p^{2a+3}.
$$


A raw test modulo $p^3$, or modulo $p^2$, is not a divided-source test when $a>0$.

The unit part of the changing $g_B$ is also retained when computing the actual coefficients and targets. It is not replaced by an unspecified normalization.

### 12.2 Hermite defects

To know $\sigma^\pm$ modulo $p^2$, the numerators in (4.3) must be known modulo $p^3$. Their division by $p$ is paid by (4.2).

The factorial $k!$ is a $p$-adic unit because $k<p$. No division by $k!$ is used.

The actual credit $h_p$ still uses


$$
Q_{N-1}^{\mathrm H}Q_N^{\mathrm H},
$$


not the pair at $k-1,k$.

### 12.3 Divided second-collision carries

To evaluate


$$
B_U/p^2,\quad B_V/p^2,\quad
\rho_\ell,\quad\rho_{\ell-1}\pmod p,
$$


their numerators must be known modulo $p^3$. The double collision and the exact identities prove the required divisibility.

For the state formulas:

- $Z_{0,j}^\pm$ is needed modulo $p^3$;
- $Z_{1,j}^\pm$ is needed modulo $p^2$;
- $Y_j^\pm$ is needed only modulo $p$.

All these requirements are finite and explicit.

### 12.4 Determinant precision

No determinant division occurs in (7.3), (8.2), or (8.3).

At a unit determinant, the target interpretation uses a legitimate $p$-adic unit division. At a critical determinant of depth $d_p$, recovering a source vector to precision $p^a$ from an adjugate vector generally requires precision $p^{a+d_p}$. That loss cannot be ignored.

### 12.5 Endpoint and full-credit precision

The third-precision endpoint formulas determine only the corresponding truncated valuations of $y_K$. They need not determine the exact $t_p,z_p,b_p,h_p$ when deeper zeros occur.

For a general post-credit certificate $c_p\le H_p+2$, one needs a validated value or sufficient certified information for the **actual** $H_p$, and source precision through $p^{H_p+3}$. Formula (5.2) remains valid there, but the required nonvanishing is open.

### 12.6 Summary

| Operation | Payment and scope |
|---|---|
| Gaussian normalization | Actual $g_B$, before the residue test |
| Raw quadratic evaluation | Extra precision $2v_p(g_B)$ before division |
| Hermite base defects | One paid division by $p$, using (4.2) |
| New second-collision carries | Two paid divisions by $p$, using the actual double zero |
| Factors $2,16$ | Units at the present primes $p>N$ |
| Determinant inversion | Used only when $p\nmid\Delta$; otherwise the loss is explicit |
| Residual states | Actual indices $0\le j\le r<N$ |
| Shifted states | Largest recurrence step $n-1$ |
| Hermite indices | At most $N$; credit remains at $N-1,N$ |
| Endpoint reduction | Actual $a_K,d_K$; no assumption that $a_K$ is a unit |
| Final clearing and cancellation | Actual $D,\lambda,G$, unchanged |

---

## 13. One optional constant-size algebraic receipt

No new numerical calculation is indispensable for the proofs above. The new statements follow from the displayed finite recurrences and exact algebra.

If an independent bounded audit is desired, the following receipt tests the new quadratic correction, not an original-family noncollision assertion.

### Fixed inputs

Work in the polynomial ring $\mathbb Z[z,S,B]$. Use only indices $0,1,2,3$.

For the source, take


$$
Y_0=S,\qquad Y_1=-4zS+B+1,
$$




$$
Y_{j+1}=-4(z+j)Y_j+Y_{j-1}+2.
$$



For the endpoint, take


$$
Y_0=S,\qquad Y_1=-4zS+B-1,
$$




$$
Y_{j+1}=-4(z+j)Y_j+Y_{j-1}-2(-1)^j.
$$



### Expected independently verifiable outputs

The source updates give


$$
\begin{aligned}
Y_2^+={}&(1+16z+16z^2)S-4(1+z)B-2-4z,\\
Y_3^+={}&(-8-136z-192z^2-64z^3)S\\
&+(33+48z+16z^2)B+19+40z+16z^2.
\end{aligned}
\tag{13.1}
$$


The endpoint updates give


$$
\begin{aligned}
Y_2^-={}&(1+16z+16z^2)S-4(1+z)B+6+4z,\\
Y_3^-={}&(-8-136z-192z^2-64z^3)S\\
&+(33+48z+16z^2)B-51-56z-16z^2.
\end{aligned}
\tag{13.2}
$$



The second-correction recurrences (6.1) must independently give


$$
\mathcal D_2^{\langle2\rangle}=16,\qquad
\mathcal E_2^{\langle2\rangle}
=\mathcal T_2^{\langle2\rangle}
=\mathcal W_2^{\langle2\rangle}=0,
$$


and


$$
\boxed{
\mathcal D_3^{\langle2\rangle}=-192,\quad
\mathcal E_3^{\langle2\rangle}=16,\quad
\mathcal T_3^{\langle2\rangle}
=\mathcal W_3^{\langle2\rangle}=16.
}
\tag{13.3}
$$



These are fixed, constant-size mathematical inputs and expected outputs. They check signs and the quadratic correction. They do not check any original $N$, do not constitute a counterexample, and cannot establish the infinite continuation lemma.

The closed $p=23,a=3$ receipt is not part of this proposed audit.

---

# Part V. Preservation of the complete producer

## 14. Complete forcing and returns remain unchanged

The new quotient system is auxiliary. It does not change the original source balance


$$
\begin{aligned}
&(\nu\mathscr A-16\tau\Pi)\Theta_\ell
 +(\nu\mathscr B-16\tau\Omega)\Theta_{\ell-1}\\
&\hspace{12mm}=\nu\mathscr C_U-16\tau C^{\rm s}.
\end{aligned}
\tag{14.1}
$$


For


$$
T=\tau(E_F-\delta^2)+\nu E_K,
$$


the complete endpoint remains


$$
\begin{aligned}
16T={}&16\tau(C^{\rm e}-\delta^2)+\nu\mathscr C_E\\
&+(\nu\mathscr A-16\tau\Pi)\Phi_\ell
 +(\nu\mathscr B-16\tau\Omega)\Phi_{\ell-1}.
\end{aligned}
\tag{14.2}
$$



### 14.1 Source and endpoint returns

The source return is


$$
z_\ell^{\rm ret}=16\Omega U-\mathscr B V,\qquad
z_{\ell-1}^{\rm ret}=\mathscr A V-16\Pi U,
$$




$$
z_j^{\rm ret}=-\Delta\Theta_j+\varrho_j,
$$


where


$$
\varrho_\ell=\mathscr I_2,\qquad
\varrho_{\ell-1}=-\mathscr I_1,
$$




$$
\varrho_{j-1}=\varrho_{j+1}+4j\varrho_j-2\Delta.
$$


Thus


$$
z_{j-1}^{\rm ret}=z_{j+1}^{\rm ret}+4jz_j^{\rm ret}.
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


with


$$
\sigma_\ell=\Omega k_E+\mathscr B f_E,\qquad
\sigma_{\ell-1}=-\Pi k_E-\mathscr A f_E,
$$




$$
\sigma_{j-1}
=\sigma_{j+1}+4j\sigma_j+2D\Delta(-1)^j.
$$


The return is homogeneous, and its determinant identity remains


$$
z_\ell^{\rm ret}w_{\ell-1}-z_{\ell-1}^{\rm ret}w_\ell
=-16\Delta(UX+VY).
\tag{14.3}
$$


There is no division by $\Delta$.

### 14.2 Canonical signed returns

For exactly $0\le a\le N$,


$$
\mathcal R_{a;N}=d_KP_a^{\mathrm H}U+Q_a^{\mathrm H}y_K.
$$


With


$$
\Psi_j^{(a)}=Q_a^{\mathrm H}\Phi_j-P_a^{\mathrm H}\Theta_j,
$$




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
\tag{14.4}
$$


Both affine forcings, both complete constants, and the reduced arc term remain.

The established determinant-$2$ payment and fixed-product theorem are reused at their original scope. No new signed-return height calculation is made.

The old rational recurrence interface also remains paid by its stated local and global clearers:


$$
Q_{\rm loc}(n)=\prod_{a=0}^{12}(n-a),\qquad
\mathcal L_n=\operatorname{lcm}(1,\ldots,n),
$$


with the nonsingular forcing


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}.
$$


Neither clearer replaces the least simultaneous arc clearer.

---

## 15. Both arcs, least clearers, final all-prime gcd, and primitive output

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


Its physical output remains


$$
R_F=
\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
      -2\alpha\beta\xi_{n-1}}2.
\tag{15.1}
$$



Reduce both arcs completely and use the actual least simultaneous clearer


$$
D=\operatorname{lcm}(\operatorname{den}R_F,\operatorname{den}R_K),
$$




$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$


Independently reduce


$$
\tau R_F+\nu R_K=\frac b\lambda,\qquad
\gcd(b,\lambda)=1,\quad \lambda>0.
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
p_N=\frac AG,\qquad q_N=\frac{\lambda M}{G}.
}
\tag{15.2}
$$



Because $\gcd(\lambda,A)=1$, this is the actual primitive numerator-denominator pair. Neither the binomial payments, $\Delta$, $J_N^{\rm aff}$, nor any local $p$-adic normalization replaces $D,\lambda$, or $G$.

---

## 16. The complete nonzero error at the same original indices

The original producer is


$$
P_N(t)=\frac{F(t)^2+(V/U)K(t)}{\delta^2}
      =\frac{W_{\rm prim}(t)}M.
$$


Its whole error remains


$$
\boxed{
\epsilon_N=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0.
}
\tag{16.1}
$$



For completeness, the exact rational relation follows directly from the retained balance. Since


$$
\eta(W_{\rm prim})
=\tau(\delta^2+V)-\nu U=M,
$$


finite integration by parts gives


$$
\int_0^1 e^tW_{\rm prim}(t)\,dt=eM-E.
$$


Also,


$$
4\int_0^1\frac{W_{\rm prim}(t)}{1+t^2}\,dt
=\pi M+\frac b\lambda.
$$


Therefore


$$
\epsilon_N=e+\pi-\frac{A}{\lambda M},
$$


and at these same original indices,


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0.
}
\tag{16.2}
$$



The complete rational enclosure is unchanged:


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


Thus


$$
\boxed{
q_NJ_N=\frac{\lambda_N}{G_N}
       \bigl(\tau_NJ_F+\nu_NJ_K\bigr).
}
\tag{16.3}
$$


Both positive summands remain.

Even a completed interval estimate such as (11.2) would not establish the remaining all-prime fixed-fraction factorial saving. The supplied implication from a future strict all-prime estimate would still have only its stated force: it would make $q_N\epsilon_N$ grow and retire this producer. It would not decide whether $e+\pi$ is rational or irrational.

---

## 17. Final ledger and conclusion

### New proved statements

1. On the present non-arc interval,
   

$$
r=2N-p\ge13,\qquad s=r-6\ge7,\qquad k=(p+1)/2\le N-6.
$$



2. The exact Hermite-anchored quotient recurrence (5.1)–(5.3) evaluates the error of the admitted $p^2$-block at **all further depths**, with both forcings and actual $p$-base defects retained.

3. Equations (6.2)–(7.6) evaluate the complete next source and endpoint digits modulo $p^3$.

4. The actual Gaussian–Hermite contact identity (8.3) preserves the full determinant-unit target. Its valuation is exactly $c_p-2$ at determinant-unit primes and differs from it by at most $v_p(\Delta)$ at critical primes.

5. The complete first two source-depth layers on the remaining branch cost at most $4N\log2$, and all determinant-conditioning losses cost at most $\log|\Delta|=O(N)$, as expressed in the full-depth comparison (9.5).

### Conditional implication

Universal nonvanishing of the direct third-digit pair (7.3) on $\mathcal S_N$ would give the full exponential non-arc interval bound (11.2). This is a rigorous implication, not an established theorem.

### Exact remaining bottleneck

The unresolved quantity is


$$
\boxed{
\mathfrak C_N^{\rm lift}
=
\sum_{p\in\mathcal S_N}
\left[
\min\!\left\{
v_p(\rho_\ell-\Delta\mathfrak e_s^+),
v_p(\rho_{\ell-1}+\Delta\mathfrak e_{s-1}^+)
\right\}
-(H_p-2)_+
\right]_+\log p.
}
\tag{17.1}
$$


The integers in this expression are specified by exact finite recurrences, and their next digit is evaluated in (8.4). Nevertheless, no $O(N)$ upper bound for (17.1) is proved.

At determinant-unit primes, the obstruction is the actual cancellation (8.8). At critical determinant primes, the remaining state contact is also open; paying the determinant-conditioning loss does not pay that contact.

The unchanged obligations for $p>2N$ and for the remaining smaller primes stay open and have not been expanded in this report.

### Computation status

No computation at an original enormous index has been performed or proposed. The optional receipt in Section 13 has fixed, constant-size inputs and explicit expected outputs. Its scope is only the new algebraic correction. The prior $p23/a3$ PASS receipt remains closed.

### Final conclusion

The new result is a **paid, actual Hermite-anchored lifting identity and a quantified full-depth comparison** for the remaining second-collision branch. It advances the next invariant beyond the admitted $p^2$-block and identifies exactly what a third-depth or post-credit continuation theorem must exclude.

It does **not** prove universal noncollision, a summable bound for surviving contact depths, a fixed all-prime factorial saving, retirement of the producer, or irrationality of $e+\pi$. The requested primary interval objective remains open at the explicitly evaluated contact cancellation in (8.8) and its higher-depth continuation.
