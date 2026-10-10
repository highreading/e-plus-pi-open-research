> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 7 — A short adjoint for the actual norm acceptance, an infinite content-two subfamily, and an all-prime saturation theorem

## Abstract

The rationality or irrationality of $e+\pi$ remains unresolved. In particular, neither the supplied finite certificates nor the results below give a same-index comparison between the actual primitive denominator and the nonzero whole approximation error.

This report makes three advances.

1. **A short adjoint for the complete linear norm acceptance.** At every admissible paid precision, the full inverse symbol disappears from the adjoint observation except through its first three coefficients. The resulting acceptance is expressed by at most six binomial products per force coefficient, together with the actual finite return vector. This is a reduction of the actual scalar calculation, not another inverse digit.

2. **An evaluated infinite original subfamily with $a\ge2$.** On
   

$$
\boxed{u\equiv1\pmod4,\qquad u\ge0,}
$$


   a direct eight-bit Kummer argument excludes content one. The period and transfer to the original power-$9$ family are proved. This is a lower bound, not an evaluation of the actual higher content.

3. **An all-prime theorem for the actual least clearer and column contents.** After the actual least simultaneous clearing, the two complete integer producer columns have coprime contents:
   

$$
\boxed{\gcd(c_U,c_V)=1.}
$$


   More precisely, their contents are determined by the two factorial-contact denominator clearers. The primitive-column minor content divides the complete second contact denominator. These identities rule out a common-column-content mechanism and isolate the relative scalar cofactors that can actually reduce $q_n$.

The outstanding local obligation is still an evaluated norm acceptance at sufficient precision for the actual content on an infinite original subfamily, or a paid higher-depth source relation. A bounded new calculation of the linear acceptance at $u=0$, modulo $2^{12}$, is specified at the end. It uses a $44\times44$ return matrix, not the original matrix.

---

## 1. Original objects and assessment of the supplied evidence

Throughout,


$$
\boxed{b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.}
$$


Contact indices are exactly $0\le i,j<b$. Physical reconstruction has exactly $0\le j\le b$.

Set


$$
h=\frac n2,\qquad d=\frac{b-1}{4},\qquad
g=\frac{h+1}{2}.
$$


The exact global relations are


$$
\boxed{h=8004d+2001,\qquad g=4002d+1001,\qquad h=2g-1.}
$$



Retain


$$
R=2^h\binom nh,\qquad
\Lambda=\frac{(n!)^2}{2^n},\qquad
\phi(z)=1-z+\frac{z^2}{2},
$$




$$
\lambda_s=s![z^s]\phi(z)^n,\qquad W_j=\binom{n+2}{j},
$$


and


$$
A_{ij}=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j}.
$$


The normalized force is


$$
\mathfrak f_i=
\frac{(n+i)!}{n!R}
[t^n](1+2t+2t^2)^n(1+t)^i.
$$



For a contact vector $z$,


$$
\Delta_jz=jz_{j-1}-z_j,\qquad z_{-1}=z_b=0,
\qquad
(\mathcal Rz)_j=W_j\Delta_jz.
$$


The complete corrected columns remain


$$
x=\frac12\mathcal RA^{-1}\mathfrak f,
\qquad
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$


The logarithmic force $h^F$ is retained.

Write


$$
z^f=A^{-1}\mathfrak f,\qquad x=2^ax_0,
\qquad a=\min_{0\le j\le b}v_2(x_j),
$$


and


$$
z^k=A^{-1}k,\qquad
k=\frac{h^e-A(j!)_{0\le j<b}}{b!}.
$$



The complete raw forms are


$$
\mathcal U=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)^2
+b^2W_b^2(z^f_{b-1})^2,
\tag{1.1}
$$




$$
\mathcal V=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)(\Delta_jz^k)
+W_b^2bz^f_{b-1}(bz^k_{b-1}+1).
\tag{1.2}
$$


Thus


$$
Q=2^{-2a-2}\mathcal U=x_0^Tx_0,\qquad
E=2^{-a-3}\mathcal V.
\tag{1.3}
$$



Both mixed terminal summands, the norm terminal, and the physical conditions $z_b^f=z_b^k=0$ remain in force.

### 1.1 What is reused

The following are reused at their stated scope:

- the reviewed modulo-$4$ calculation and $a\ge1$;
- the actual endpoint valuation
  

$$
v_2(x_{b-1})=v_2\binom gd;
$$


- the complete modulo-$8$ formulas and the content-one criterion from Turn 6;
- the complete-source conclusion $\tau\in8\mathbb Z_2^{b+1}$, hence $E\in2\mathbb Z_2$;
- the corrected finite-completion and boundary-cancellation theorem;
- the corrected Cartier evaluator only under its bounded-precision hypotheses;
- the original-family ternary denominator law at its already established scope.

No modulo-$8$ inverse is derived again here.

For clarity about the dependency on Turn 6, the implication used below is exactly


$$
\boxed{
a=1
\iff
\exists\,s\in[0,d],\ s\ {\rm even}:
v_2\binom gs+
v_2\binom{h+d-s}{d-s}=1.
}
\tag{1.4}
$$


Its reconstruction test is $v_2(W_j)+v_2(\Delta_jz^f)=2$. The supplied residue-class formulas cover every physical row, including $j=b$; no higher-content conclusion follows from (1.4).

### 1.2 What the new receipts establish

The two-valuation receipt establishes the reported minima at precisely $u=0,\ldots,20$. In conjunction with (1.4), these give


$$
\boxed{a(u)\ge2\qquad(0\le u\le20).}
$$


They do not give exact higher contents.

At $u=0$, the new witness has valuation pair $(1,7)$. Its total cost $8$ is not an assertion that the corresponding reconstructed coordinate has valuation $8$. Turn 6 only uses that two-cost statistic to decide whether the total is $1$.

The earlier, separately proved row witness still gives the useful upper bound


$$
\boxed{2\le a(0)\le10.}
\tag{1.5}
$$



The low-prefix receipt does not show that all original words have prefix cost at least two. Indeed it explicitly shows otherwise. Nor does a cost-one prefix prove that it extends to a full cost-one word.

---

## 2. An infinite original subfamily with $a\ge2$

This section proves a genuine infinite consequence without extrapolating the finite list.

### 2.1 Exact period of the original low words

Let


$$
B_0=9^{18},\qquad G_0=9^{32}.
$$


By the elementary $2$-adic lifting formula,


$$
v_2(G_0-1)=8,
$$


and, for every positive integer $t$,


$$
v_2(G_0^t-1)=8+v_2(t).
\tag{2.1}
$$


Hence the exact period of $b=B_0G_0^u$ modulo $2^{k+2}$, for $k\ge6$, is


$$
\boxed{2^{\max(0,k-6)}.}
\tag{2.2}
$$


Knowing $b\bmod2^{k+2}$ determines all of


$$
d\bmod2^k,\qquad h\bmod2^k,\qquad g\bmod2^k:
$$


the divisions by $4$ and $2$ have therefore been paid in the parameter modulus.

At eight bits,


$$
9^{18}\equiv721\pmod{1024},\qquad
9^{32}\equiv257\pmod{1024}.
$$


Consequently


$$
b\equiv721+256u\pmod{1024}.
$$


In particular,


$$
u\equiv1\pmod4
\Longrightarrow
b\equiv977\pmod{1024}.
\tag{2.3}
$$


The corresponding low words are


$$
\boxed{d\equiv244,\qquad g\equiv81,\qquad h\equiv161\pmod{256}.}
\tag{2.4}
$$



### 2.2 Direct exclusion of total Kummer cost at most one

Suppose $s$ is even, $0\le s\le d$, and put $R_1=d-s$.

In the low eight bits:

- let $\beta$ count the borrows in subtracting $s$ from $g$;
- let $\gamma$ count the carries in adding $h$ and $R_1$.

Kummer’s theorem identifies their full-word totals with the two valuations in (1.4). Their prefix counts are nonnegative lower bounds for those totals.

We prove


$$
\beta+\gamma\ge2
\tag{2.5}
$$


already in the first eight bits of (2.4).

#### Case 1: $\beta=0$

The low word of $s$ is an even submask of $81=64+16+1$. Thus


$$
s\bmod256\in\{0,16,64,80\}.
$$


Because these values are at most $244$,


$$
R_1\bmod256\in\{244,228,180,164\}.
$$


Each of these four residues has bits $5$ and $7$ set. So does


$$
161=128+32+1.
$$


The addition $h+R_1$ therefore produces carries at both bit $5$ and bit $7$. Hence $\gamma\ge2$.

#### Case 2: $\beta=1$ and $\gamma=0$

Zero carries in $h+R_1$ require the low word of $R_1$ to have bits $0,5,7$ unset. Thus


$$
0\le R_1\bmod256\le94.
$$


Since the low word of $s$ is even and at most $254$, the equation


$$
s+R_1=d
$$


cannot have low-word sum $244+256=500$. Therefore its low-word sum is $244$, and


$$
s\bmod256=244-(R_1\bmod256)\ge150.
$$


This is larger than $g\bmod256=81$, so the subtraction has an outgoing borrow at bit $7$. If that is its only borrow, the lower seven bits of $s$ must be a submask of $81$. As $s$ is even,


$$
s\bmod256\in\{128,144,192,208\}.
$$


The corresponding residues $244-s$ are


$$
116,\ 100,\ 52,\ 36,
$$


all of which have bit $5$ set. This contradicts $\gamma=0$.

These exhaust total prefix cost at most one.

The lower bound is sharp as a prefix statement: $s=80$, $R_1=164$ gives no subtraction borrow and exactly the two addition carries at bits $5$ and $7$. Its exit carry is unrestricted, as required by the prefix convention.

### Theorem 2.1 — Infinite original content lower bound

For every original index satisfying $u\equiv1\pmod4$,


$$
\boxed{a(u)\ge2.}
\tag{2.6}
$$



**Proof.** Every actual full-word choice $s$ projects to an admissible low-eight-bit calculation. Full Kummer cost is at least prefix cost, which is at least two by the preceding argument. Equation (1.4) excludes $a=1$, while the already proved universal theorem excludes $a=0$. ∎

This proves an infinite original statement. It does **not** prove:

- universal $a\ge2$;
- an exact value of $a$ on this progression;
- that the prefix minimum controls higher inverse content.

Its arithmetic gain is a fixed lower content factor $4$, not an asymptotic denominator saving.

---

## 3. A short adjoint for the actual linear norm acceptance

The accepted summed-reconstruction identity is


$$
S=\sum_{j=0}^{b-1}(n+1-j)W_jz^f_j,
\qquad
\sum_{j=0}^{b}x_j=S/2.
\tag{3.1}
$$


Consequently


$$
\boxed{Q\equiv 2^{-a-1}S\pmod2.}
\tag{3.2}
$$


To use this, one needs $S$ modulo at least $2^{a+2}$.

The next theorem considerably shortens the calculation of $S$, while retaining the finite return.

### 3.1 Paid completion hypotheses

Fix $L\ge2$, and put


$$
I=\min(b-1,8L-2),\qquad m=4(L-1),
$$




$$
T=\min(2L-1,2n-1),\qquad V=T+m.
$$


Retain the scope condition


$$
\boxed{n>4(I+2m+T+4)+2.}
\tag{3.3}
$$



Let


$$
c_s=s![z^s]\phi(z)^{-n},
\qquad
c_0=1,\qquad
c_s=-\sum_{r=1}^s\binom sr\lambda_rc_{s-r}.
$$


In divided powers define


$$
\mathcal J_L=U_{-n}H_{c,\le m}U_{-n},
\qquad U_\alpha=(1+\partial_z)^\alpha.
$$


The complete transformed force is


$$
q^f_j=
\begin{cases}
(P_b^{-1}\mathfrak f_{\le I})_j,&0\le j<b,\\
(\eta_f)_{j-b},&b\le j<b+m,\\
0,&j\ge b+m,
\end{cases}
\tag{3.4}
$$


with the actual finite return


$$
\eta_f=U_n^{(m)}K\Sigma^{-1}D_f.
\tag{3.5}
$$


Here $\Sigma$ denotes the finite Schur matrix, to distinguish it from the scalar $S$.

The reused completion theorem states, as a whole finite coefficient vector,


$$
\boxed{\mathcal J_Lq^f\equiv\overline z^f\pmod{2^L}.}
\tag{3.6}
$$


The exterior entries on the right are zero. Equation (3.6), rather than an infinite-matrix inverse substitution, is what justifies the following adjoint calculation.

### 3.2 The adjoint collapse

Extend


$$
\ell_j=(n+1-j)\binom{n+2}{j}
$$


to $j\ge0$, with $\ell_j=0$ for $j>n+2$. Its ordinary generating polynomial is


$$
\sum_{j\ge0}\ell_jt^j=(n+1-t)(1+t)^{n+1}.
\tag{3.7}
$$



For a row functional, right multiplication by $U_{-n}$ multiplies its ordinary generating series by $(1+t)^{-n}$. Hence


$$
\ell^TU_{-n}
\quad\text{has generating polynomial}\quad
(n+1-t)(1+t)
=(n+1)+nt-t^2.
\tag{3.8}
$$



Only three symbol coefficients can now contribute:


$$
c_0=1,\qquad c_1=n,\qquad c_2=n^2.
\tag{3.9}
$$


Indeed, multiplying the row in (3.8) by the divided-power multiplication matrix gives


$$
\begin{aligned}
k=0 &: (n+1)+nc_1-c_2=n+1,\\
k=1 &: n-2c_1=-n,\\
k=2 &: -1,
\end{aligned}
$$


and zero at every $k>2$.

After the second $U_{-n}$, the complete adjoint therefore has generating series


$$
\boxed{
\sum_{k\ge0}\mu_kt^k
=\bigl((n+1)-nt-t^2\bigr)(1+t)^{-n}.
}
\tag{3.10}
$$



Equivalently, with negative lower indices interpreted as zero,


$$
\boxed{
\mu_k=(-1)^k\left[
(n+1)\binom{n+k-1}{k}
+n\binom{n+k-2}{k-1}
-\binom{n+k-3}{k-2}
\right].
}
\tag{3.11}
$$



The argument is finite: each column involved acts on a finite polynomial. No differentiation of an uncontrolled infinite series is required.

### Theorem 3.1 — Complete short-adjoint norm acceptance

Under (3.3),


$$
\boxed{
S\equiv
\sum_{j=0}^{b-1}\mu_j(P_b^{-1}\mathfrak f_{\le I})_j
+\sum_{v=0}^{m-1}\mu_{b+v}(\eta_f)_v
\pmod{2^L}.
}
\tag{3.12}
$$



**Proof.** By (3.6), the full functional $\ell$ applied to $\mathcal J_Lq^f$ equals its contact value $S$ modulo $2^L$. Equations (3.8)–(3.10) evaluate $\ell^T\mathcal J_L$ exactly. ∎

The symbol’s higher coefficients have disappeared from the observation itself. They have **not** disappeared from the finite return $\eta_f$.

### 3.3 Eliminating the remaining original-length contact sum

For $i\ge0$, $B\ge0$, define the explicitly evaluated binomial product


$$
\mathcal F_i(B)=
\binom{n+i-1}{i}\binom{n+B}{B-i},
\tag{3.13}
$$


and set $\mathcal F_i(B)=0$ for $i<0$ or $B<0$.

The elementary identity


$$
\sum_{j=0}^{B}
\binom ji\binom{n+j-1}{j}
=
\binom{n+i-1}{i}\binom{n+B}{B-i}
\tag{3.14}
$$


follows by absorbing $\binom ji$ into the rising factorial and then applying finite hockey-stick summation.

Put $B=b-1$. Since


$$
(P_b^{-1}\mathfrak f_{\le I})_j
=\sum_{i=0}^{I}(-1)^{j-i}\binom ji\mathfrak f_i,
$$


equations (3.11)–(3.14) give


$$
S\equiv
\sum_{i=0}^{I}(-1)^i\mathfrak f_i\,\mathcal H_i(B)
+\sum_{v=0}^{m-1}\mu_{b+v}(\eta_f)_v
\pmod{2^L},
\tag{3.15}
$$


where


$$
\begin{aligned}
\mathcal H_i(B)={}&(n+1)\mathcal F_i(B)\\
&+n\bigl(\mathcal F_i(B-1)+\mathcal F_{i-1}(B-1)\bigr)\\
&-\bigl(\mathcal F_i(B-2)+2\mathcal F_{i-1}(B-2)
+\mathcal F_{i-2}(B-2)\bigr).
\end{aligned}
\tag{3.16}
$$



Thus the actual $b$-term contact sum has been evaluated into at most six binomial products per retained force coefficient and $m$ actual return terms.

This is not yet a primitive norm theorem: the finite return and these binomial values must still be evaluated at the required paid precision. It is, however, a concrete scalar reduction substantially smaller than assembling the quadratic kernel family.

---

## 4. What the same adjoint does—and does not do—for the source

Retain the complete source return data


$$
\xi_v=
\sum_{t=0}^{T}a_t
\sum_{\substack{0\le r\le t\\0\le v-r\le m}}
\binom n{t-r}\lambda_{v-r}\binom{b+v}{v-r},
\qquad a_t=\frac{(b+t)!}{b!},
$$




$$
\delta=K\Sigma^{-1}G^{[V]}\xi-\xi,
\qquad
\theta_v=\sum_{w=v}^{V}\binom n{w-v}\delta_w.
\tag{4.1}
$$


The completion theorem gives


$$
\mathcal J_L\sum_{v=0}^{V}\theta_ve_{b+v}
\equiv\overline z^k-\sum_{t=0}^{T}a_te_{b+t}
\pmod{2^L}.
\tag{4.2}
$$



Define the complete physical source


$$
\tau_j=W_j\Delta_jz^k\quad(j<b),\qquad
\tau_b=W_b(bz^k_{b-1}+1).
$$


Summed reconstruction yields


$$
\sum_{j=0}^{b}\tau_j=\ell^Tz^k+W_b.
\tag{4.3}
$$



The exterior factorial contribution telescopes exactly:


$$
a_t\ell_{b+t}
=a_{t+1}W_{b+t+1}-a_tW_{b+t}.
$$


Therefore


$$
\sum_{t=0}^{T}a_t\ell_{b+t}+W_b
=a_{T+1}W_{b+T+1}.
\tag{4.4}
$$


Using (3.10) in (4.2), we obtain


$$
\boxed{
\sum_{j=0}^{b}\tau_j
\equiv
\sum_{v=0}^{V}\mu_{b+v}\theta_v
+a_{T+1}W_{b+T+1}
\pmod{2^L}.
}
\tag{4.5}
$$


Under the present scope condition $T=2L-1$, the last factorial coefficient is divisible by $2^L$, so it vanishes at this modulus—but only after being retained and paid.

Equation (4.5) is a linear source acceptance. It is **not**


$$
x_0^T(\tau/4)=E.
$$


The adjoint collapse therefore does not itself prove a higher-depth law $E-r(u)Q$.

The existing paid conclusion remains


$$
E\in2\mathbb Z_2.
$$


For an independently specified integral $r(u)$,


$$
E-r(u)Q
=
2^{-2a-2}\left(2^{a-1}\mathcal V-r(u)\mathcal U\right).
\tag{4.6}
$$


A depth-$K$ assertion must protect this division using the actual $a$, or a proved sufficient upper bound.

The logarithmic contribution is still governed by


$$
B_\star=n-v_2(b!)-1-2s_2(n)-\ell.
\tag{4.7}
$$


It may be suppressed only when the original bound protects the requested observation **after payment**. No source statement here extends that guard.

---

## 5. An all-prime saturation theorem from factorial reconstruction

This section is exact over $\mathbb Q$, not merely $2$-adic.

Set


$$
\omega_j=j!W_j,
\qquad
u_j=\frac{2\Lambda R\,x_j}{\omega_j},
\qquad
v_j=\frac{4b!\,y_j}{\omega_j}.
$$


The actual least simultaneous clearer is


$$
d_B=\operatorname{lcm}_{0\le j\le b}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\}.
\tag{5.1}
$$


Let


$$
U=d_Bu,\qquad V=d_Bv
$$


be the complete integer columns, and let


$$
c_U=\gcd_j|U_j|,\qquad c_V=\gcd_j|V_j|
\tag{5.2}
$$


be their **actual** contents.

No column is being replaced in the producer. Primitive columns introduced below are only devices for analyzing its final gcd.

### 5.1 The finite factorial-coordinate transformation

Define the actual factorial-contact vectors


$$
\zeta_j=\frac{\Lambda R\,z^f_j}{j!},
\qquad
\rho_j=\frac{[A^{-1}(h^e+h^F)]_j}{j!},
\qquad 0\le j<b.
\tag{5.3}
$$


Let $\mathsf D$ be the finite difference map


$$
(\mathsf Dt)_0=-t_0,\qquad
(\mathsf Dt)_j=t_{j-1}-t_j\ (1\le j<b),\qquad
(\mathsf Dt)_b=t_{b-1}.
$$


The original reconstruction gives exactly


$$
\boxed{u=\mathsf D\zeta,\qquad v=e_0+\mathsf D\rho.}
\tag{5.4}
$$


In particular,


$$
\boxed{\sum_{j=0}^{b}u_j=0,\qquad \sum_{j=0}^{b}v_j=1.}
\tag{5.5}
$$



This is where both the physical endpoint and the complete $+e_0$ correction matter. Deleting the terminal row would invalidate (5.5).

Let


$$
D_\zeta=\operatorname{lcm}_{j<b}\operatorname{den}(\zeta_j),
\qquad
D_\rho=\operatorname{lcm}_{j<b}\operatorname{den}(\rho_j).
\tag{5.6}
$$


Partial sums invert (5.4):


$$
\zeta_i=-\sum_{j=0}^{i}u_j,\qquad
\rho_i=1-\sum_{j=0}^{i}v_j.
$$


Thus


$$
\boxed{d_B=\operatorname{lcm}(D_\zeta,D_\rho).}
\tag{5.7}
$$



This is a content/clearer identity for the actual finite inverse, including the complete logarithmic force.

### 5.2 Exact contents

Let


$$
c_\zeta=\gcd_{j<b}|D_\zeta\zeta_j|.
$$


Minimality of $D_\zeta$ gives


$$
\gcd(c_\zeta,D_\zeta)=1.
\tag{5.8}
$$


The finite difference map and its integral partial-sum inverse preserve coordinate gcd. Hence


$$
\boxed{c_U=\frac{d_B}{D_\zeta}\,c_\zeta.}
\tag{5.9}
$$



For the second column, $D_\rho e_0+\mathsf D(D_\rho\rho)$ has content one. Indeed, a prime dividing all its coordinates divides their sum $D_\rho$; its partial sums then show that it divides every coordinate of $D_\rho\rho$, contradicting minimality of $D_\rho$. Therefore


$$
\boxed{c_V=\frac{d_B}{D_\rho}.}
\tag{5.10}
$$



### Theorem 5.1 — Actual all-prime column saturation

For every original index,


$$
\boxed{\gcd(c_U,c_V)=1.}
\tag{5.11}
$$



**Proof.** Write $D_\zeta=gr$, $D_\rho=gs$, where $\gcd(r,s)=1$. Then


$$
d_B=grs,\qquad c_U=sc_\zeta,\qquad c_V=r.
$$


Equation (5.8) implies $\gcd(c_\zeta,r)=1$, proving (5.11). ∎

This is an evaluated all-prime assertion: the common column content is exactly one. It is not an uncomputed primewise definition.

It refutes the candidate mechanism in which the least simultaneous clearer is followed by a large **shared** content of the two complete integer columns. Such a shared factor cannot occur in these original objects.

### 5.3 A relative-minor consequence

Put


$$
U^\circ=U/c_U,\qquad V^\circ=V/c_V,
$$


and let $M$ be the gcd of all their $2\times2$ minors. Since


$$
\sum_jU^\circ_j=0,\qquad
\sum_jV^\circ_j=\frac{d_B}{c_V}=D_\rho,
$$


we have, for every $i$,


$$
\sum_j\left(U^\circ_iV^\circ_j-U^\circ_jV^\circ_i\right)
=D_\rho U^\circ_i.
$$


Primitivity of $U^\circ$ gives


$$
\boxed{M\mid D_\rho.}
\tag{5.12}
$$



Thus, after paying actual column contents, a common relative-minor factor can arise only from the complete second factorial-contact denominator.

For the weighted columns $\omega_jU^\circ_j$ and $\omega_jV^\circ_j$, every prime $p>n+2$ is a unit in every $\omega_j$. Consequently


$$
\boxed{
p>n+2,\quad p\nmid D_\rho
\Longrightarrow
\text{the weighted columns are independent modulo }p.
}
\tag{5.13}
$$



This is useful support information for an all-prime mechanism. It is not yet a scalar gcd theorem: independent vectors over a finite field can have a common isotropic norm/orthogonality observation.

For example, the primitive integer vectors


$$
X=(1,2,-1,-2),\qquad Y=(6,0,1,0)
$$


have primitive minor content $1$, but


$$
X^TX=10,\qquad X^TY=5.
$$


Thus a scalar common factor $5$ can survive even though the vectors remain independent modulo $5$. This small example illustrates the precise obstruction to replacing scalar analysis by minor saturation.

---

## 6. The resulting exact relative-cofactor formula for $q_n$

Retain


$$
\mathcal N=x^Tx,\qquad \mathcal H=x^Ty,
$$




$$
A_B=d_B^2\,4\Lambda^2R^2\mathcal N,\qquad
H_B=d_B^2\,8\Lambda Rb!\mathcal H,
$$


and the all-prime final gcd


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
\tag{6.1}
$$



In terms of the actual integer columns,


$$
A_B=\sum_j\omega_j^2U_j^2,\qquad
H_B=\sum_j\omega_j^2U_jV_j.
$$


Define


$$
N^\circ=\sum_j\omega_j^2(U^\circ_j)^2,\qquad
H^\circ=\sum_j\omega_j^2U^\circ_jV^\circ_j.
$$


Then


$$
A_B=c_U^2N^\circ,\qquad H_B=c_Uc_VH^\circ.
\tag{6.2}
$$



Because $\gcd(c_U,c_V)=1$, put


$$
\delta=\gcd(c_U,|H^\circ|).
$$


The elementary identity


$$
\gcd(ab,c)=\gcd(a,c)\,
\gcd\!\left(b,\frac{c}{\gcd(a,c)}\right)
$$


now yields


$$
\boxed{
q_n=
\frac{c_U}{\delta}\,
\frac{N^\circ}
{\gcd\!\left(N^\circ,\left|c_VH^\circ/\delta\right|\right)}.
}
\tag{6.3}
$$



This formula separates two genuinely different requirements:

1. the first-column content $c_U$ cancels only to the extent that it divides the actual relative scalar $H^\circ$;
2. the remaining primitive norm cancels only through its actual scalar gcd with $c_VH^\circ/\delta$.

In particular, a large first-column content can increase, rather than decrease, the primitive denominator when the corresponding relative scalar factor is absent.

Equivalently,


$$
\begin{aligned}
\log q_n
={}&\log(c_U/\delta)+\log N^\circ\\
&-\sum_p
\min\left\{
v_p(N^\circ),
v_p(c_VH^\circ/\delta)
\right\}\log p.
\end{aligned}
\tag{6.4}
$$


This is an exact all-prime decomposition of the denominator contribution, not a binary surrogate.

No asymptotic estimate for the final sum is proved here. The saturation theorem eliminates one proposed mechanism; it does not eliminate scalar cancellation.

The already closed original-family law is retained unchanged:


$$
\boxed{v_3(q_n)=n-\frac{b+15}{2}.}
\tag{6.5}
$$


It already places an exponentially large factor in $q_n$. A fixed binary gain, or even a polynomial-size binary content factor, cannot by itself settle the necessary denominator/error comparison.

---

## 7. A bounded new scalar calculation at the actual original index $u=0$

No tools were used. The following calculation is proposed for coordinator inspection; it is not claimed to have been performed.

Its purpose is to evaluate the new short-adjoint norm acceptance at enough precision to pay every possible actual $a(0)$ in the proved interval $2\le a(0)\le10$.

### 7.1 Inputs and size

Use


$$
b=150094635296999121,\qquad n=4002b,
\qquad L=12.
$$


Then


$$
I=94,\qquad m=44,\qquad T=23,\qquad V=67.
$$


The scope inequality is overwhelmingly satisfied:


$$
n>4(94+88+23+4)+2=838.
$$



Only the force return is needed for $S$. The Schur matrix has size $44$, and the force head has $95$ entries. No $b\times b$ matrix is constructed.

### 7.2 A short paid seed calculation at this new precision

The force seeds can be obtained from bounded factorial sums.

Expanding the central coefficient with $n=2h$ gives exactly


$$
\mathfrak f_0
=
\sum_{r=0}^{h}
\frac{2^r(h^{\underline r})^2}{(2r)!},
\tag{7.1}
$$


where $h^{\underline r}=h(h-1)\cdots(h-r+1)$.

Similarly, if $C_-$ is the coefficient of $t^{n-1}$ divided by $R$,


$$
C_-=
\sum_{r=0}^{h-1}
\frac{2^r(h^{\underline r})^2(h-r)}{(2r+1)!},
\qquad
\mathfrak f_1=(n+1)(\mathfrak f_0+C_-).
\tag{7.2}
$$



The valuation of the $r$-th term in (7.1) is


$$
v_2(r!)+2v_2\binom hr.
\tag{7.3}
$$


The extra denominator in (7.2) is $2r+1$, which is odd, and the extra numerator cannot reduce valuation. Since


$$
v_2(r!)\ge12\qquad(r\ge16),
$$


both sums truncate at $r=15$ modulo $2^{12}$.

For these sixteen terms, the largest binary division to be paid is


$$
v_2(15!)=11.
$$


Thus $h\bmod2^{23}$ is sufficient for a falling-factorial implementation. Odd denominator parts are inverted modulo $2^{12}$.

This is a new depth-$12$, sixteen-term seed calculation. It does not repeat the old lower-precision force receipt.

The integral recurrence


$$
\begin{aligned}
\mathfrak f_{i+2}={}&(2n+2i+3)\mathfrak f_{i+1}\\
&-\frac{(3i+n+2)(n+i+1)}2\mathfrak f_i\\
&+\frac{i(n+i)(n+i+1)}2\mathfrak f_{i-1}
\end{aligned}
\tag{7.4}
$$


then supplies the required head through $i=94$. The coefficient divisions are exact integer divisions; they do not incur a bit loss at every recurrence step.

### 7.3 Forming the return without an original-length vector

The required near-terminal entries of $U_{-n}P_b^{-1}\mathfrak f_{\le I}$ can be formed using the finite identity


$$
\begin{aligned}
&\sum_{k=j}^{b-1}
\binom{n+k-j-1}{k-j}\binom ki\\
&\qquad=
\sum_{q=0}^{i}
\binom{n+q-1}{q}\binom j{i-q}
\binom{n+b-1-j}{b-1-j-q}.
\end{aligned}
\tag{7.5}
$$


Only the $O(m)$ near-terminal positions used by $D_f$ are needed. Applying $H^{-1}$, constructing $K,\Sigma$, and solving for $\eta_f$ therefore use the stated $44$-dimensional finite return system.

The exterior return must be formed in full. Setting it to zero would not evaluate (3.15).

Finally evaluate (3.15)–(3.16) modulo $4096$.

Large-index binomials do not require large factorial integers. Their valuations follow from binary digit sums. Their odd factorial parts can be evaluated modulo $4096$ from a table of products of odd integers through one block of length $4096$, followed by the usual binary factorial recursion. All relevant arguments have fewer than $72$ bits.

### 7.4 Expected verifiable outputs

The proposed certificate should contain:

1. the sixteen paid residues in each seed sum (7.1)–(7.2);
2. $\mathfrak f_0,\ldots,\mathfrak f_{94}\pmod{4096}$;
3. the $44\times44$ Schur system and a verified solution for its actual force return;
4. the $44$ entries of $\eta_f$;
5. the separate head and return contributions in (3.15);
6. the final residue
   

$$
\boxed{S(0)\pmod{4096}.}
$$



A result


$$
S(0)\equiv0\pmod{4096}
$$


would imply, without guessing the actual content,


$$
\boxed{Q(0)\equiv0\pmod2.}
$$


Indeed $a(0)\le10$, so division by $2^{a(0)+1}$ leaves at least one factor of $2$.

This would be an actual paid primitive norm conclusion at one original index. It would still not prove an infinite-family norm law.

If the residue is nonzero, it gives the exact valuation of $S(0)$ below $12$. In that case primitive norm parity may still depend on the unresolved actual $a(0)$. That possibility must be reported, not hidden by choosing a convenient normalization.

---

## 8. The precise remaining obligations

### 8.1 Local binary obligation

The new adjoint theorem makes the following a concrete target:

> On a specified infinite original subfamily, evaluate the right side of (3.15) at depth at least $a(u)+2$, with either the actual $a(u)$ certified or a sufficient original-family upper bound paid.

A useful sufficient version would be


$$
S(u)\equiv0\pmod{2^{A(u)+2}},
\qquad
a(u)\le A(u),
$$


on that same infinite subfamily. This would prove $Q(u)$ even without requiring equality $a(u)=A(u)$.

No such infinite evaluation is proved here. The binomial products and the finite return depend on the full original words; the period of a fixed low prefix does not settle their higher acceptances.

For the mixed scalar, the corresponding concrete obligation remains a source-derived, independently specified $r(u)$ and a paid evaluation of


$$
2^{a(u)-1}\mathcal V-r(u)\mathcal U.
$$


The linear source sum in §4 does not supply that relation.

### 8.2 All-prime obligation

The new saturation theorem proves that shared column content is not the missing saving. The remaining all-prime question is now localized to the actual scalar cofactors in (6.3):


$$
\delta=\gcd(c_U,|H^\circ|),
\qquad
\gcd\!\left(N^\circ,\left|c_VH^\circ/\delta\right|\right).
$$



A concrete follow-on lemma is:

> Derive, from the complete finite inverse and complete forcing, a bound or an exact divisor for these two scalar cofactors whose primewise logarithmic contribution can be summed on an infinite original subfamily.

Minor saturation alone is insufficient, as the explicit isotropic example shows. A common determinant depth alone is likewise insufficient.

### 8.3 Whole error at the same indices

The producer’s error remains


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


and the relevant whole error is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{8.1}
$$



An irrationality proof through this producer would require, on the **same infinitely many original indices**, nonvanishing and a favorable estimate involving the actual primitive denominator. For example,


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0
$$


would suffice.

No binary content result, finite acceptance certificate, or all-prime saturation identity in this report proves that assertion.

---

## 9. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Reported two-cost minima at $u=0,\ldots,20$ | Finite supplied computation |
| $a(u)\ge2$ at those 21 indices | Consequence at that finite scope of the Turn 6 criterion |
| Exact higher contents at those indices | Not established |
| Period $2^{\max(0,k-6)}$ for the original $k$-bit parameter words | Proved |
| $a(u)\ge2$ for every $u\equiv1\pmod4$ | **New infinite original-family theorem** |
| Universal $a\ge2$ | Open |
| Short adjoint (3.10) and finite binomial acceptance (3.15) | **New proved scalar reduction at paid precision** |
| Actual primitive norm parity on an infinite subfamily | Open |
| New higher-depth $E-r(u)Q$ law | Not obtained |
| Exact least-clearer/contact-clearer identity | **Newly proved** |
| Actual complete column contents satisfy $\gcd(c_U,c_V)=1$ | **New evaluated all-prime theorem** |
| Primitive minor content divides $D_\rho$ | **Newly proved** |
| Relative-cofactor formula (6.3) for actual $q_n$ | **Newly proved** |
| All-prime asymptotic denominator saving | Open |
| Same-index nonzero whole-error comparison | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

The principal new scalar result is the explicit adjoint


$$
\boxed{
\ell^T\mathcal J_L
\longleftrightarrow
\bigl((n+1)-nt-t^2\bigr)(1+t)^{-n},
}
$$


together with its finite head-plus-return evaluation. It removes the quadratic kernel assembly from the primitive norm-parity task, but does not remove the actual return or the actual content payment.

The principal new all-prime result is


$$
\boxed{
d_B=\operatorname{lcm}(D_\zeta,D_\rho),\qquad
c_U=\frac{d_B}{D_\zeta}c_\zeta,\qquad
c_V=\frac{d_B}{D_\rho},\qquad
\gcd(c_U,c_V)=1.
}
$$


Thus any substantial denominator reduction must come from the actual relative scalar cofactors, not from a common content created by clearing the two columns.

The bounded next calculation is the depth-$12$ linear acceptance at $u=0$, with the inputs and expected outputs in §7. It can establish a paid primitive norm fact at that original index. It cannot establish an infinite theorem by itself.

**The global objective remains open: the exact remaining bottleneck is an infinite, same-index control of the actual scalar cofactors and primitive denominator together with the nonzero whole evaluated error.**
