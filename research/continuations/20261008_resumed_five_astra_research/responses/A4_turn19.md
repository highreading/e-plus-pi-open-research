> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the paid Newton pair theorem in A2turn11

## 1. Verdict and scope

**Verdict: PASS for the new mathematical assertions in A2turn11, Sections 4–8, at their stated scope.**

The following conclusions withstand an independent derivation:

1. The additional Newton column divisors are the **full integers**
   

$$
D_r=2^r r!,\qquad 0\le r<d,
$$


   not merely their powers of $2$.

2. For the two specified, completely corrected columns, the actual two-column determinantal content has
   

$$
v_2(\mathscr C_k^{(2)})=5.
$$


   The minor in the residual rows labelled by the original indices $m=d,d+1$ attains this valuation.

3. Every Cramer numerator used in the subsequent interpolation is an integer multiple of $32$. After that division, the retained denominator
   

$$
\mu_k=\frac{x_0y_1-x_1y_0}{32}
$$


   is odd, but is **not** assumed to be $\pm1$.

4. The interpolation residues justify all $d$ subsequent row divisions by $2$, including the complete constant and linear affine borders.

5. The sign and all scalars in the final all-prime transfer are correct:
   

$$
\boxed{
   |\delta_k|^{d+2}\Omega_k|\mu_k|^{d-1}G_k
   =
   |f_k|\,2^{\lambda_d+d+5}\mathfrak D_d\,g_k^{\mathrm{new}}.
   }
$$



6. Consequently,
   

$$
\boxed{
   v_2(G_k)=
   d^2+4d+29+(d+4)s_2(d)
   -3\sum_{n=0}^{d-1}s_2(n)+\nu_k.
   }
$$



No mathematical change to the claimed depth $5$, the exponent $d-1$ of $\mu_k$, or the displayed digit-sum formula is required.

There are two important scope qualifications.

- This report does **not** declare the separate full audit of A2turn10’s dyadic construction passed. That earlier audit remains A3’s distinct pending assignment. Below I identify the older facts checked as dependencies of the new theorem.
- This fixed-rank evaluation supplies **no upper bound** for the remaining complete coefficient content
  

$$
\nu_k=v_2\gcd(|P_{0,k}|,|P_{1,k}|).
$$


  In particular, neither the target $\nu_k\le 15k^2/4+O(k\log k)$ nor the corresponding final-$G_k$ upper bound has been proved.

The rationality or irrationality of $e+\pi$ remains unresolved.

---

## 2. Original objects, normalization, and dependency boundary

### 2.1 The domain is unchanged

Throughout this audit,


$$
\mathcal K=\{9^{18+32u}:u\ge0\},\qquad d=k-1.
$$



Since


$$
k=81^{9+16u}=(1+80)^{9+16u}
$$


and $9+16u$ is odd, the first nonconstant binomial term has valuation $4$, whereas every subsequent term has valuation at least $8$. Thus


$$
v_2(d)=4.
$$


Also $3\mid k$, so


$$
d\equiv2\pmod3.
$$


Every original $d$ is larger than $32$.

Write


$$
\alpha=\alpha_d=v_2((2d)!),\qquad
\beta=\beta_d=v_2((2d-2)!).
$$


Two identities repeatedly used below are


$$
\alpha=d+v_2(d!),\qquad
\alpha-\beta=v_2((2d)(2d-1))=5.
\tag{2.1}
$$


In particular,


$$
2\beta-\alpha-2=\alpha-12\ge20.
\tag{2.2}
$$



These are original-domain statements. No auxiliary compact index set replaces $\mathcal K$.

### 2.2 Complete sequences and forcing

Retain the original recurrence and sequences:


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad
w_n=(-1)^n,\qquad c_n=u_n-w_n,
$$




$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-f_n+4\rho_n.
$$



The complete returns are


$$
\sigma_n=c_{n+1}+c_n=u_{n+1}+u_n
$$


and


$$
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
$$



With


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),
$$


the integer forcing remains


$$
\boxed{
T_n=-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1}.
}
\tag{2.3}
$$


Both factorial terms are essential. In particular,


$$
(2n+2)!+(2n)!
=(4n^2+6n+3)(2n)!,
$$


and the polynomial


$$
b(n)=4n^2+6n+3
$$


is odd. Dropping the second factorial would destroy the odd normalized factorial multiplier used in the Pascal congruence.

The original determinant is


$$
H_k(s)=
\det\left[
(c_{m+j})\ \middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s,
$$


where


$$
0\le m<2k,\qquad 0\le j<k.
$$



Its physical terminal is still


$$
\boxed{
\text{moment }3k-2,\qquad
\text{factorial }(6k-4)!,\qquad
\text{last odd denominator }6k-5.
}
\tag{2.4}
$$



### 2.3 Actual clearers, contents, and primitive normalization

The established least original right-column entry clearers are retained:


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3),
\qquad 0\le j<k.
$$


The least common entry clearer is $\Lambda_k$.

The final gcd is always


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$


over **all primes**.

For the rational coefficient pair $H_k/\Lambda_k^k$, let


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


Its actual least simultaneous coefficient clearer and subsequent content are


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
}
\tag{2.5}
$$


Indeed, prime by prime the least clearer has valuation


$$
\max\!\left(0,v_p(\Lambda_k^k)
-\min(v_p(H_{0,k}),v_p(H_{1,k}))\right).
$$



The original rectangles remain


$$
Z_k=
\left[
(c_{m+j})_{\substack{m<2k\\j<k}}
\ \middle|\
(T_{m+j})_{\substack{m<2k\\j<k-1}}
\right],
$$




$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{m<2k-1\\j<k}}
\ \middle|\
(T_{m+j})_{\substack{m<2k-1\\j<k}}
\right].
$$


Writing


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k),
$$


the established interface is reused exactly:


$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k\mid \Lambda_k\mathscr L_k\mathscr R_k.
\tag{2.6}
$$



The accepted sign and nonvanishing results give, at every original index,


$$
q_k=\frac{|H_{1,k}|}{G_k}>0,\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k},
$$


and


$$
\boxed{
0<\ell_k=q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}.
}
\tag{2.7}
$$



No lower divisor of $G_k$ is substituted for $G_k$, and $\ell_k/q_k$ is not substituted for the whole error $\ell_k$.

### 2.4 The exact older interface used here

The new proof begins with the turn10 block reduction. Its relevant objects are


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),
$$




$$
(\mathcal A_d y)_n
=\sum_{i=0}^d(-1)^i\binom di P_d(n+i)y_{n+i}.
$$


Because $d$ is even,


$$
\mathcal A_d y=\Delta^d(P_dy).
$$



The row operator acts only on the first $d$ rows, with


$$
\det\mathcal S_d=\Omega_k
=\prod_{n=0}^{d-1}P_d(n)>0,
$$


an odd integer, not an integer-unimodular payment.

The complete common-column form is


$$
H_k(s)=\det[\mathcal T\mid\mathcal M(s)],
$$


where


$$
\mathcal T=(T_{m+j})_{\substack{m<2d+2\\j<d}},
$$




$$
\mathcal M(s)
=[c_m\mid(\sigma_{m+j})_{j<d}\mid\Lambda_k(r_m+sw_m)]_{m<2d+2}.
$$


The earlier column permutation has sign


$$
(-1)^{d(d+2)}=1.
$$



Partition


$$
\mathcal S_d[\mathcal T\mid\mathcal M(s)]
=
\begin{pmatrix}
F_k&A_0+sA_1\\
B&C_0+sC_1
\end{pmatrix}.
\tag{2.8}
$$


The bottom rows are exactly those labelled by


$$
m=d,\ldots,2d+1.
$$



The complete factorial pivot is


$$
F_k=-\Lambda_kD_fK_dD_f,\qquad
D_f=\operatorname{diag}((2n)!)_{n<d},
$$


with


$$
K_d(n,j)=
\sum_{i=0}^d(-1)^i\binom di
P_d(n+i)b(n+i+j)
\frac{(2(n+i+j))!}{(2n)!(2j)!}.
\tag{2.9}
$$


Put


$$
\eta_d=\det K_d,\qquad h_d=(2d-2)!,
$$




$$
\widehat D_f=h_dD_f^{-1},\qquad
N_d=\widehat D_f\,\operatorname{adj}(K_d)\,\widehat D_f,
$$




$$
\delta_k=\Lambda_k\eta_dh_d^2.
$$


Then


$$
F_k^{-1}=-\frac{N_d}{\delta_k}.
\tag{2.10}
$$


This follows directly by substituting the definitions and using
$\operatorname{adj}(K_d)=\eta_dK_d^{-1}$.

The old Schur numerators are


$$
E_i=\delta_k C_i+BN_dA_i.
$$


The earlier column divisions are


$$
2^{d+2},\qquad
\underbrace{2^{\alpha+3},\ldots,2^{\alpha+3}}_{d\text{ contact-return columns}},
\qquad 4.
$$


Their total is


$$
\lambda_d=d\alpha+4d+4.
$$


For the resulting integer pencil $\widehat E_k(s)$,


$$
\det\widehat E_k(s)=J_{0,k}+J_{1,k}s,
$$


the older exact transfer is


$$
\boxed{
\delta_k^{d+2}\Omega_kH_{i,k}
=f_k\,2^{\lambda_d}J_{i,k},
\qquad i=0,1,
}
\tag{2.11}
$$


where


$$
f_k=(-\Lambda_k)^d\eta_d
\left(\prod_{n=0}^{d-1}(2n)!\right)^2.
$$



**Dependency checks made in this audit.** I checked the original-domain identities, the sequence divisibilities needed by the new Newton divisions, the finite-difference and atom formulas, the Pascal congruence and its leading-block consequences, the inverse formula (2.10), and the scalar algebra needed from (2.11).

**Separate audit still pending.** I do not reissue a full audit verdict for the entire turn10 dyadic construction. Nor do I rerun its closed analytic spread work, exact ternary theorem, or finite diagnostics.

---

## 3. Audit of the full Newton integer payments

### 3.1 A direct check of the required sequence divisibility

The moment representation


$$
u_n=\int_0^\infty e^{-t}(t-1)^{2n}\,dt
$$


agrees with the original recurrence. In fact, if


$$
M_j=\int_0^\infty e^{-t}(t-1)^j\,dt,
$$


integration by parts gives $M_j=(-1)^j+jM_{j-1}$, so
$(-1)^jM_j$ satisfies the recurrence for $a_j$.

Define


$$
\theta_t=\frac{\Delta^tu_0}{2^tt!}.
$$


Expanding the integral for $\Delta^tu_0$ gives the exact finite formula


$$
\boxed{
\theta_t
=
\sum_{h=0}^t
(-1)^{t-h}\binom{t+h}{2h}(2h-1)!!,
}
\tag{3.1}
$$


with $(-1)!!=1$. Hence $\theta_t\in\mathbb Z$.

For every $n\ge0$, the finite Newton shift gives


$$
\frac{\Delta^tu_n}{2^tt!}
=
\sum_{h=0}^n
\binom nh\,2^h(t+1)_h\,\theta_{t+h}\in\mathbb Z.
$$


Thus


$$
2^tt!\mid\Delta^tu_n.
$$


Since


$$
\sigma=2u+\Delta u,
$$


it follows that


$$
\boxed{
2^{t+1}t!\mid\Delta^t\sigma_n
\qquad(n,t\ge0).
}
\tag{3.2}
$$



This verifies the full factorial divisibility at the scope required by the new theorem, rather than only its dyadic part.

### 3.2 Product rule and shifted arguments

The finite-difference product rule used in the source is


$$
\boxed{
\Delta^d(fg)(n)
=
\sum_{h=0}^d
\binom dh\,\Delta^hf(n)\,
\Delta^{d-h}g(n+h).
}
\tag{3.3}
$$


The shift $n+h$ on the second factor is correct.

Also,


$$
\Delta^hP_d(n)
=
2^h\frac{d!}{(d-h)!}Q_h(n),
\qquad
Q_h(n)=\prod_{a=h}^{d-1}(2n+2a+1).
\tag{3.4}
$$



Apply (3.3) to $P_d\Delta^r\sigma$. A summand is


$$
\binom dh
2^h\frac{d!}{(d-h)!}Q_h(n)
\Delta^{d-h+r}\sigma_{n+h}.
$$


By (3.2), it is divisible by


$$
2^{d+r+1}d!\,
\frac{(d-h+r)!}{(d-h)!}.
$$


Because


$$
\frac{(d-h+r)!}{(d-h)!}
=r!\binom{d-h+r}{r},
$$


every summand is divisible by


$$
2^{d+1}d!(2^rr!).
$$


Therefore


$$
\boxed{
2^{d+1}d!D_r
\mid\mathcal A_d(\Delta^r\sigma)_n,
\qquad D_r=2^rr!.
}
\tag{3.5}
$$



The bottom source satisfies


$$
2D_r\mid\Delta^r\sigma_m.
\tag{3.6}
$$



### 3.3 Integrality in the complete corrected columns

The Newton column transformation is upper triangular with diagonal entries $1$:


$$
\Delta^r\sigma_m
=\sum_{j=0}^r(-1)^{r-j}\binom rj\sigma_{m+j}.
$$


It is therefore determinant one. Since the Schur correction is linear in each contact-return source column, this transformation acts on the **complete corrected columns**, not just on their uncorrected parts.

Put $R=B/4$. The weighted corrected column is exactly


$$
\frac{\delta_k\Delta^r\sigma_{\mathrm{bot}}}
     {2^{\alpha+3}D_r}
+
RN_d
\frac{\mathcal A_d\Delta^r\sigma}
     {2^{\alpha+1}D_r}.
\tag{3.7}
$$



The top vector is integral by (3.5), since


$$
\frac{2^{d+1}d!}{2^{\alpha+1}}
=\operatorname{odd}(d!).
$$


The bottom term is integral by (3.6) and


$$
2\beta-\alpha-2\ge0.
$$



Thus every full $D_r$, including its odd part, is paid integrally.

If $\mathcal Q_k(s)$ denotes the resulting pencil, then


$$
\det\mathcal Q_k(s)=I_{0,k}+I_{1,k}s,
$$


and


$$
\boxed{
J_{i,k}=\mathfrak D_d I_{i,k},
\qquad
\mathfrak D_d=\prod_{r=0}^{d-1}2^rr!.
}
\tag{3.8}
$$


This is an all-prime identity. Its binary valuation is


$$
\boxed{
v_2(\mathfrak D_d)
=d(d-1)-\sum_{r=0}^{d-1}s_2(r).
}
\tag{3.9}
$$



**Section 4 verdict: PASS.**

---

## 4. Audit of the normalized source pair

To avoid confusing the original recurrence $a_n$ with local source notation, write


$$
a_n^*=\frac{(\mathcal A_dc)_n}{2^d},
\qquad
b_n^*=\frac{(\mathcal A_d\Delta\sigma)_n}{2^{\alpha+2}},
\qquad n<d.
$$


These are the source’s local vectors $a,b$.

The exact corrected pair is


$$
\boxed{
x=RN_da^*+\frac{\delta_k}{2^{d+2}}c_{\mathrm{bot}},
}
\tag{4.1}
$$




$$
\boxed{
y=RN_db^*+
\frac{\delta_k}{2^{\alpha+4}}(\Delta\sigma)_{\mathrm{bot}}.
}
\tag{4.2}
$$


The $y$-normalization includes both the old contact-return payment and the additional $D_1=2$.

### 4.1 The literal atom modulo $4$

For $w_n=(-1)^n$,


$$
(\mathcal A_dw)_n
=(-1)^n(1+E)^dP_d(n)
=(-1)^n(2+\Delta)^dP_d(n),
$$


where $E$ is the shift operator. Substituting (3.4),


$$
(\mathcal A_dw)_n=(-1)^n2^dU_d(n),
$$


with


$$
U_d(n)=
\sum_{h=0}^d
\binom dh\frac{d!}{(d-h)!}Q_h(n).
$$



For $h\ge1$, the factor $d!/(d-h)!$ contains $d$, hence is divisible by $16$. The $h=0$ term is a product of $d$ consecutive odd numbers. Modulo $4$, it is


$$
(-1)^{d/2}=1,
$$


because $4\mid d$. Thus


$$
U_d(n)\equiv1\pmod4.
$$



The same product-rule argument, using the divisibility for $u$, gives


$$
2^dd!\mid(\mathcal A_du)_n.
$$


Since $4\mid d!$, the decomposition $c=u-w$ yields


$$
\boxed{
a_n^*\equiv-(-1)^n\pmod4.
}
\tag{4.3}
$$



This calculation genuinely uses the literal atom. Replacing $c$ by $u$ would erase the alternating residue needed later.

### 4.2 The contact parity generating function

For clarity, use $\zeta$ for the contact normalization called $\eta$ in the source:


$$
\zeta_t^{(m)}
=\frac{\Delta^t\sigma_m}{2^{t+1}t!},
\qquad
\zeta_t=\zeta_t^{(0)}.
$$


Then


$$
\zeta_t=\theta_t+(t+1)\theta_{t+1}.
\tag{4.4}
$$



Reducing (3.1) modulo $2$,


$$
\theta_t\equiv\sum_{h=0}^t\binom{t+h}{2h}\pmod2.
$$


The formal generating function is


$$
\begin{aligned}
\sum_{t\ge0}\sum_{h=0}^t\binom{t+h}{2h}z^t
&=\sum_{h\ge0}\frac{z^h}{(1-z)^{2h+1}}\\
&=\frac{1-z}{1-3z+z^2}.
\end{aligned}
$$


Over $\mathbb F_2$, this is


$$
\frac{1+z}{1+z+z^2}.
$$


Consequently,


$$
\boxed{
\theta_{t+2}=\theta_{t+1}+\theta_t
\quad\text{in }\mathbb F_2,
\qquad
(\theta_0,\theta_1,\theta_2)=(1,0,1).
}
\tag{4.5}
$$


The recurrence proves period $3$; the conclusion does not rest on a finite table.

The finite Newton shift gives


$$
\zeta_t^{(m)}
=
\sum_{h=0}^m
\binom mh\,2^h(t+1)_h\,\zeta_{t+h},
$$


and hence


$$
\boxed{\zeta_t^{(m)}\equiv\zeta_t\pmod2.}
\tag{4.6}
$$



### 4.3 Oddness of the divided $\Delta\sigma$ source

Define


$$
\widetilde b_n
=\frac{(\mathcal A_d\Delta\sigma)_n}{2^{d+2}d!}.
$$


The correctly shifted product rule gives


$$
\widetilde b_n
=
\sum_{h=0}^d
\binom dh Q_h(n)(d-h+1)
\zeta_{d-h+1}^{(n+h)}.
\tag{4.7}
$$



Set $t=d-h$. Since $d$ is even, $\binom dt$ is even for odd $t$. Using (4.6), and noting that all $Q_h(n)$ are odd,


$$
\widetilde b_n
\equiv
\sum_{t=0}^d\binom dt\zeta_{t+1}\pmod2.
$$


Writing $d=2D$, Lucas reduction gives


$$
\widetilde b_n
\equiv
\sum_{h=0}^{D}\binom Dh\theta_{2h+1}.
$$



The period-three table implies


$$
\theta_{2h+1}=\theta_{h+1}\quad\text{in }\mathbb F_2.
$$


On this sequence $E^2=E+1$, so


$$
\sum_{h=0}^{D}\binom Dh\theta_{h+1}
=((1+E)^D\theta)_1
=(E^{2D}\theta)_1
=\theta_{d+1}.
$$


Since $3\mid d+1$, this value is $1$.

Finally,


$$
b_n^*=\operatorname{odd}(d!)\,\widetilde b_n,
$$


so


$$
\boxed{b_n^*\equiv1\pmod2.}
\tag{4.8}
$$



The relevant source sum has therefore been evaluated, not merely assigned a name.

### 4.4 Constancy modulo $4$: the expanded calculation

This is one of the compressed steps in the source for which an explicit expansion is useful.

Because $d$ is even,


$$
\Delta_n(\mathcal A_d\Delta\sigma)_n
=\Delta^{d+1}(P_d\Delta\sigma)_n.
$$


The product rule here uses $\binom{d+1}{h}$, and the term $h=d+1$ vanishes because $P_d$ has degree $d$. Thus


$$
\boxed{
\begin{aligned}
\Delta_n(\mathcal A_d\Delta\sigma)_n
={}&2^{d+3}d!
\sum_{h=0}^{d}
\binom{d+1}{h}Q_h(n)\\
&\quad\cdot(d-h+1)(d-h+2)
\zeta_{d-h+2}^{(n+h)}.
\end{aligned}
}
\tag{4.9}
$$


The product $(d-h+1)(d-h+2)$ is always even. Therefore


$$
2^{d+4}d!\mid
\Delta_n(\mathcal A_d\Delta\sigma)_n.
$$


After division by the actual normalizer $2^{\alpha+2}$,


$$
\boxed{
b_{n+1}^*-b_n^*\equiv0\pmod4.
}
\tag{4.10}
$$



There is no lost shift or missing factorial in this step.

### 4.5 The last-two-top-row minor

Let


$$
A^{(2)}=[a^*\mid b^*],\qquad
I_*=\{d-2,d-1\}.
$$


Every entry in both columns is odd, so every two-row minor is even.

Because $d$ is even,


$$
a_{d-2}^*\equiv-1,\qquad
a_{d-1}^*\equiv1\pmod4.
$$


The two corresponding $b^*$-entries have the same odd residue, say $c$, modulo $4$. Hence


$$
\det A^{(2)}[I_*,:]
\equiv -c-c=-2c\equiv2\pmod4.
$$


Therefore


$$
\boxed{
v_2\bigl(\det A^{(2)}[I_*,:]\bigr)=1.
}
\tag{4.11}
$$



**Section 5 verdict: PASS.**

---

## 5. Audit of the complete paired-cofactor evaluation

### 5.1 Complete bottom forcing minors

The residual row $i$ is labelled by the original row $m=d+i$. Thus


$$
R(i,j)
=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}
b(d+i+j)(2(d+i+j))!.
\tag{5.1}
$$



All these entries are integers. Indeed,


$$
d+i+j\le3d,
$$


so every displayed odd denominator is at most


$$
6d+1=6k-5
$$


and divides $\Lambda_k$.

The factorial correction has valuation at least


$$
\alpha-2\ge30.
$$


It follows that the complete $R$ agrees modulo $8$ with its rational Cauchy part.

For rows $i<i'$ and columns $j<j'$, direct cross multiplication gives


$$
\det\left[
\frac{\Lambda_k}{2(d+a+b)+1}
\right]_{\substack{a\in\{i,i'\}\\b\in\{j,j'\}}}
=
\frac{
4\Lambda_k^2(i'-i)(j'-j)
}{
\prod_{a,b}(2(d+a+b)+1)
}.
\tag{5.2}
$$


Every denominator is odd. Hence


$$
4\mid \det R[\{i,i'\},\{j,j'\}],
$$


and


$$
\boxed{
\frac{\det R[\{i,i'\},\{j,j'\}]}4
\equiv(i'-i)(j'-j)\pmod2.
}
\tag{5.3}
$$



For $I_*=\{d-2,d-1\}$, the column gap is $1$, so


$$
\boxed{
\frac{\det R[\{i,i'\},I_*]}4
\equiv i'-i\pmod2.
}
\tag{5.4}
$$



The rational expression is used only for a justified congruence. The exact matrix $R$ still contains both factorial terms.

### 5.2 Pascal leading blocks: the precise dependency

In (2.9), every summand with $i\ge1$ is even because


$$
\frac{(2(n+i+j))!}{(2n)!(2j)!}
=
\frac{(2(n+i))!}{(2n)!}
\binom{2(n+i+j)}{2j},
$$


and the first factor is even.

The $i=0$ term therefore gives


$$
K_d(n,j)\equiv
\binom{2(n+j)}{2j}
\equiv\binom{n+j}{j}\pmod2.
\tag{5.5}
$$


For every leading block of size $L$,


$$
\binom{n+j}{j}
=\sum_{h=0}^{L-1}\binom nh\binom jh
\qquad(n,j<L).
$$


Thus that block is $L_LL_L^T$, where $L_L$ is unit lower triangular. Its determinant is $1$.

Accordingly, **every leading principal block of $K_d$ has odd determinant**. This includes:

- the full block, giving $\eta_d$ odd;
- the leading $(d-2)\times(d-2)$ block needed for the distinguished two-row adjugate minor;
- the leading $(d-1)\times(d-1)$ block needed for the rank-one residue of $N_d$.

The last item is a separate necessary use of the leading-block statement; invertibility of $K_d$ alone would not suffice.

### 5.3 Actual factorial diagonal gaps in the adjugate

Let


$$
e_n=v_2\!\left(\frac{h_d}{(2n)!}\right).
$$


Then


$$
e_{d-1}=0.
$$


Moreover,


$$
\frac{h_d}{(2d-4)!}=(2d-3)(2d-2),
$$


so $e_{d-2}=1$, since $d-1$ is odd.

For $n=d-3$, the additional factor $2d-4=2(d-2)$ has valuation $2$, because $v_2(d-2)=1$. Therefore


$$
\boxed{
e_{d-1}=0,\qquad e_{d-2}=1,\qquad
e_n\ge3\quad(n\le d-3).
}
\tag{5.6}
$$



Since


$$
N_d=\widehat D_f\,\operatorname{adj}(K_d)\,\widehat D_f,
$$


every two-row, two-column minor satisfies


$$
v_2(\det N_d[I,J])
\ge \sum_{i\in I}e_i+\sum_{j\in J}e_j.
\tag{5.7}
$$


The unique two-element set with weight sum $1$ is $I_*$. Every other two-element set has weight sum at least $3$.

For the principal pair, Jacobi’s complementary-minor identity gives


$$
\det\operatorname{adj}(K_d)[I_*,I_*]
=
\eta_d
\det K_d[0,\ldots,d-3;\,0,\ldots,d-3].
$$


Both factors are odd. Hence


$$
\boxed{
v_2(\det N_d[I_*,I_*])=2.
}
\tag{5.8}
$$


For every other pair $(I,J)$,


$$
\boxed{
v_2(\det N_d[I,J])\ge4.
}
\tag{5.9}
$$



Also, all entries of $\widehat D_f$ except the last are even, while


$$
\operatorname{adj}(K_d)_{d-1,d-1}
$$


is the odd leading $(d-1)\times(d-1)$ determinant. Consequently,


$$
\boxed{
N_d\equiv e_{\mathrm{last}}e_{\mathrm{last}}^T\pmod2.
}
\tag{5.10}
$$



These conclusions explicitly use the factorial diagonal weights.

### 5.4 Both literal bottom source corrections

The correction in $x$ has valuation at least


$$
2\beta-(d+2)+1
=2\beta-d-1,
$$


because $c_m$ is even.

The correction in $y$ has valuation at least


$$
2\beta-(\alpha+4)+2
=2\beta-\alpha-2
=\alpha-12,
$$


because $4\mid\Delta\sigma_m$.

Using $\beta=\alpha-5$, $\alpha\ge d$, and $d\ge32$,


$$
2\beta-d-1\ge d-11\ge21,
\qquad
\alpha-12\ge20.
$$


Thus both corrections are, in particular, divisible entrywise by $64$:


$$
\boxed{
[x\mid y]\equiv RN_dA^{(2)}\pmod{64}.
}
\tag{5.11}
$$



This is a congruence for the exact corrected columns. Neither correction has been deleted from the integer construction.

### 5.5 Complete compound-product valuation

For a fixed bottom-row pair $M=\{i,i'\}$, Cauchy–Binet gives


$$
\det(RN_dA^{(2)})[M,:]
=
\sum_{\substack{|I|=2\\|J|=2}}
\det R[M,I]\,
\det N_d[I,J]\,
\det A^{(2)}[J,:].
\tag{5.12}
$$



Every factor has the required audited valuation:

| Factor | Universal lower valuation | Distinguished value |
|---|---:|---:|
| $\det R[M,I]$ | $2$ | quotient by $4$ has residue $i'-i$ for $I=I_*$ |
| $\det N_d[I,J]$ | $2$ | exactly $2$ for $I=J=I_*$ |
| $\det A^{(2)}[J,:]$ | $1$ | exactly $1$ for $J=I_*$ |

For every $(I,J)\ne(I_*,I_*)$, the total valuation is at least


$$
2+4+1=7.
$$


The distinguished term, divided by $32$, has residue $i'-i$ modulo $2$.

The corrections in (5.11) change two-column minors only by multiples of $64$, because all remaining factors are integers. Therefore


$$
\boxed{
32\mid x_i y_{i'}-x_{i'}y_i,\qquad
\frac{x_i y_{i'}-x_{i'}y_i}{32}
\equiv i'-i\pmod2.
}
\tag{5.13}
$$



Finally, $R$ is entrywise odd, (5.10) holds, and $a_{d-1}^*$ is odd. Hence


$$
x_i\equiv1\pmod2.
$$


The same argument also gives $y_i\equiv1\pmod2$.

### 5.6 Actual content and attaining original-row minor

Define the actual all-prime content


$$
\mathscr C_k^{(2)}
=
\gcd_{0\le i<i'<d+2}
|x_i y_{i'}-x_{i'}y_i|.
$$


Every minor is divisible by $32$, and the pair $i=0,i'=1$ has valuation exactly $5$. Hence


$$
\boxed{v_2(\mathscr C_k^{(2)})=5.}
\tag{5.14}
$$



The attaining rows are labelled by the original indices


$$
m=d,\qquad m=d+1.
$$


This is an attaining minor of the **actual corrected pair in original physical rows**. It is not a claim that an unscaled minor of the original $2k\times2k$ matrix itself equals $32$ times a unit.

The odd part of $\mathscr C_k^{(2)}$ remains unevaluated.

**Section 6 verdict: PASS.**

---

## 6. Cramer divisions, interpolation, and every corrected column

### 6.1 Integral division by $32$ and the retained odd denominator

Set


$$
\Pi_k=
\begin{pmatrix}
x_0&y_0\\
x_1&y_1
\end{pmatrix},
\qquad
\det\Pi_k=32\mu_k.
$$


Equation (5.13) proves that $\mu_k$ is odd and nonzero.

For a residual row $i$,


$$
(x_i,y_i)\operatorname{adj}(\Pi_k)
=
\bigl(x_i y_1-x_1y_i,\ x_0y_i-x_i y_0\bigr).
$$


Both components are integer multiples of $32$. Their quotients have residues


$$
1-i,\qquad i\pmod2.
$$


Therefore


$$
\boxed{
(x_i,y_i)\Pi_k^{-1}\in\mathbb Z_{(2)}^2,
\qquad
(x_i,y_i)\Pi_k^{-1}
\equiv(1-i,i)\pmod2.
}
\tag{6.1}
$$



The payment is exact:

- first divide the integer Cramer numerators by $32$;
- retain the remaining denominator $\mu_k$;
- use only its proved oddness for binary congruences.

The first two rows form a basis of the row lattice over $\mathbb Z_{(2)}$. Before payment, that lattice has index $2^5$ in the ambient rank-two module. Thus “saturation after payment” must not be read as saying that the unpaid row lattice was already saturated.

### 6.2 Row parity of every weighted contact-return column

For every $0\le r<d$, set


$$
z_n^{(r)}
=
\frac{(\mathcal A_d\Delta^r\sigma)_n}
     {2^{\alpha+1}D_r}\in\mathbb Z.
$$


The exact corrected column is


$$
\frac{\delta_k\Delta^r\sigma_{\mathrm{bot}}}
     {2^{\alpha+3}D_r}
+RN_dz^{(r)}.
\tag{6.2}
$$


Its first term has valuation at least $\alpha-12$, uniformly in $r$, and is therefore even.

By (5.10), $RN_dz^{(r)}$ has the same residue $z_{d-1}^{(r)}$ in every bottom row. This proves the source’s assertion for **every** corrected return column, without assuming that all those residues are $1$.

For completeness, the common parity can itself be evaluated symbolically. The product rule gives


$$
z_n^{(r)}
\equiv
\sum_{t=0}^d
\binom dt\binom{t+r}{r}\zeta_{t+r}\pmod2.
\tag{6.3}
$$


Let


$$
\gamma(d,r)=
\sum_{\substack{\ell\ge0\\
\text{bit }\ell\text{ of }d=1\\
\text{bit }\ell\text{ of }r=0}}2^\ell,
\qquad
c_r=r+2\mathbf1_{\{r\text{ even}\}}.
$$


Lucas’s criterion says that the nonzero terms in (6.3) are exactly those with $t$ a binary submask of $\gamma(d,r)$. Since $d$ is even, all such $t$ are even. Equation (4.4) then gives


$$
\zeta_{t+r}=\theta_{t+c_r}\quad\text{in }\mathbb F_2.
$$


Using $1+E=E^2$ on $\theta$,


$$
\boxed{
z_n^{(r)}
\equiv
\theta_{\,2\gamma(d,r)+c_r}\pmod2.
}
\tag{6.4}
$$


Thus the common residue is $0$ precisely when the displayed index is $1\pmod3$, and is $1$ otherwise.

This optional refinement is not needed for the transfer, but it independently evaluates the parity of every weighted return column. It supplies no bound for the remaining coefficient gcd.

### 6.3 First contact column and both affine-border coefficients

For the first contact column, (4.1), (5.10), and the evenness of the correction give the constant row residue $1$.

For the affine border, the exact column is


$$
\frac{\delta_k(C_{0,\mathrm{border}}+sC_{1,\mathrm{border}})}4
+
RN_d(A_{0,\mathrm{border}}+sA_{1,\mathrm{border}}).
\tag{6.5}
$$


Both coefficients of the first term are even: $v_2(\delta_k/4)=2\beta-2\ge1$.

The second term is row-constant modulo $2$ by (5.10). In fact, both border coefficients have residue $0$:

- $A_{1,\mathrm{border}}=\Lambda_k\mathcal A_dw$ is divisible by $2^d$;
- the last top entry of $A_{0,\mathrm{border}}$ is an integer combination of $\Lambda_kr_n$ with $n\ge d-1\ge1$, and these entries are even.

Thus the complete constant border and the literal linear border both satisfy the required parity assertion. Neither $\Lambda_kr$ nor $\Lambda_kw$ has been omitted.

### 6.4 All $d$ new row divisions

After swapping return columns $r=0$ and $r=1$, write the matrix as


$$
\begin{pmatrix}
\Pi_k&U_k(s)\\
V_k&C_k(s)
\end{pmatrix}.
$$


The top rows are $m=d,d+1$, and the remaining rows are


$$
m=d+2,\ldots,2d+1.
$$



Define


$$
M_k^{(2)}=\frac{V_k\operatorname{adj}(\Pi_k)}{32}.
$$


This is an integer matrix by the Cramer divisibility just proved, and


$$
V_k\Pi_k^{-1}=\frac{M_k^{(2)}}{\mu_k}.
$$



Set


$$
\mathcal V_k(s)=\mu_kC_k(s)-M_k^{(2)}U_k(s).
\tag{6.6}
$$


For the row corresponding to residual index $i$, the two interpolation coefficients have sum


$$
(1-i)+i=1\pmod2.
$$


Each corrected column has the same parity in its two pivot rows and in that bottom row. Since $\mu_k$ is odd, (6.6) is therefore even coefficientwise.

Hence


$$
\boxed{
\mathcal P_k(s)=\frac{\mathcal V_k(s)}2
\in\mathbb Z[s]^{d\times d}.
}
\tag{6.7}
$$


Dividing all $d$ rows contributes exactly the determinant factor $2^d$.

Only the last column depends on $s$, so


$$
\det\mathcal P_k(s)=P_{0,k}+P_{1,k}s.
$$



These divisions are proved integral; they are not claimed to exhaust the remaining content.

---

## 7. Audit of the sign and every scalar in the transfer

### 7.1 The single column transposition

Before the swap, the relevant column order is


$$
[x,\ r=0,\ r=1,\ r=2,\ldots,\text{border}].
$$


Interchanging $r=0$ and $r=1$ is exactly one column transposition. Thus the block determinant above equals


$$
-\det\mathcal Q_k(s).
$$



Using $\det\Pi_k=32\mu_k$,


$$
\begin{aligned}
-\det\mathcal Q_k(s)
&=\det\Pi_k\,
\det\!\left(C_k(s)-V_k\Pi_k^{-1}U_k(s)\right)\\
&=32\mu_k^{1-d}\det\mathcal V_k(s)\\
&=2^{d+5}\mu_k^{1-d}\det\mathcal P_k(s).
\end{aligned}
$$


Together with $J_i=\mathfrak D_d I_i$, this gives


$$
\boxed{
\mu_k^{d-1}J_{i,k}
=
-2^{d+5}\mathfrak D_dP_{i,k},
\qquad i=0,1.
}
\tag{7.1}
$$



The exponent $d-1$ of $\mu_k$, rather than $d$, is correct: the Schur denominator contributes $\mu_k^{-d}$, while the pivot determinant contributes one factor $\mu_k$.

### 7.2 All-prime gcd identity

Let


$$
g_k^\sharp=\gcd(|J_{0,k}|,|J_{1,k}|),
\qquad
g_k^{\mathrm{new}}=\gcd(|P_{0,k}|,|P_{1,k}|).
$$


Taking actual all-prime gcds in (7.1),


$$
|\mu_k|^{d-1}g_k^\sharp
=
2^{d+5}\mathfrak D_dg_k^{\mathrm{new}}.
\tag{7.2}
$$



Combining with (2.11), the signed coefficient identity is


$$
\delta_k^{d+2}\Omega_k\mu_k^{d-1}H_{i,k}
=
-f_k\,2^{\lambda_d+d+5}\mathfrak D_dP_{i,k}.
\tag{7.3}
$$


Therefore


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_k|^{d-1}G_k
=
|f_k|\,2^{\lambda_d+d+5}\mathfrak D_dg_k^{\mathrm{new}}.
}
\tag{7.4}
$$



Every required factor is present:

- $\Omega_k$;
- the full $\delta_k=\Lambda_k\eta_dh_d^2$;
- the full forcing determinant $f_k$;
- all old column payments $2^{\lambda_d}$;
- the full Newton product $\mathfrak D_d$;
- the paired payment $32$;
- the $d$ row payments $2^d$;
- the odd, potentially nontrivial $\mu_k$;
- the actual final all-prime gcd $g_k^{\mathrm{new}}$.

Neither $\delta_k$ nor $\mu_k$ is being represented as an established *least* all-prime clearer. They are exact retained payments. The original least coefficient clearer remains (2.5).

### 7.3 Independent check of the digit-sum formula

Let


$$
S_d=\sum_{n=0}^{d-1}s_2(n),\qquad s=s_2(d).
$$


Legendre’s formula gives


$$
V_d=v_2(f_k)=2d(d-1)-2S_d,
$$




$$
\alpha=2d-s.
$$


Since $v_2(d)=4$,


$$
s_2(d-1)=s+3,
\qquad
\beta=2d-5-s.
$$


Thus the old offset is


$$
\begin{aligned}
V_d+\lambda_d-2(d+2)\beta
&=4d+24+(d+4)s-2S_d\\
&=\kappa_k.
\end{aligned}
$$



Because $\mu_k$ is odd, (7.2) gives


$$
v_2(g_k^\sharp)
=v_2(\mathfrak D_d)+d+5+\nu_k,
$$


where


$$
\nu_k=v_2(g_k^{\mathrm{new}})
=\min(v_2(P_{0,k}),v_2(P_{1,k})).
$$


Using (3.9),


$$
\boxed{
v_2(G_k)
=
d^2+4d+29+(d+4)s_2(d)
-3\sum_{n=0}^{d-1}s_2(n)+\nu_k.
}
\tag{7.5}
$$


Since $d=k-1$ and digit sums are $O(\log d)$,


$$
\boxed{\chi_k=k^2+O(k\log k).}
\tag{7.6}
$$



The formula is exact. It is not an asymptotic guess based on finite data.

### 7.4 Preservation of the actual primitive denominator and whole error

Equation (7.3) makes the pairs $(H_{0,k},H_{1,k})$ and
$(P_{0,k},P_{1,k})$ nonzero common rational scalar multiples. Equation (7.4) accounts for the absolute value of that scalar in their full gcds.

Consequently,


$$
\boxed{
\frac{|P_{1,k}|}{g_k^{\mathrm{new}}}
=\frac{|H_{1,k}|}{G_k}=q_k.
}
\tag{7.7}
$$


Likewise,


$$
\boxed{
\frac{|P_{0,k}+P_{1,k}(e+\pi)|}{g_k^{\mathrm{new}}}
=
\frac{|H_k(e+\pi)|}{G_k}
=\ell_k>0.
}
\tag{7.8}
$$



These are exact normalization identities, not numerical evaluations of $q_k$, $G_k$, or $g_k^{\mathrm{new}}$.

**Section 7 verdict: PASS, including signs, odd factors, and primitive normalization.**

---

## 8. Finite-boundary audit

Every new operation remains inside the original finite arrays.

- The annihilator acts only on the first $d$ rows.
- A transformed top row uses original rows through
  

$$
(d-1)+d=2d-1.
$$


- The Newton transformation uses only the existing contact-return shifts $0,\ldots,d-1$.
- Its largest top return index is at most
  

$$
(d-1)+d+(d-1)=3d-2.
$$


- Its largest bottom return index is
  

$$
(2d+1)+(d-1)=3d.
$$


- The corresponding successor moment is $3d+1=3k-2$.
- The paired pivot uses the original row labels $m=d,d+1$.
- The reduced pencil still includes the original last row $m=2d+1=2k-1$.
- The full bottom rational forcing remains in $R$; only the previously specified top rational channel was annihilated.
- The terminal factorial remains $(6k-4)!$.

No conclusion is transferred to the distinct binary producer. In that separate construction, the data


$$
b=9^{18+32u},\qquad n=4002b,
$$


the contact indices $0,\ldots,b-1$, reconstruction indices $0,\ldots,b$, and terminal $z_b=0$ remain unchanged. Its complete corrected columns


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0,
$$


and complete return


$$
\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f
$$


are not identified with the present compact pencil. Its actual contents, least simultaneous clearer, primitive denominator, norm $x_0^Tx_0$, and all-prime final gcd remain separate.

---

## 9. Why the theorem does not bound the remaining coefficient gcd

Section 8 of A2turn11 states the limitation correctly.

The evaluated pair proves that a particular rank-two cofactor can be eliminated with a known binary payment. It does not control the determinant content of the remaining $d\times d$ pencil.

A simple abstract example makes the logical obstruction explicit. Take


$$
x_i=1,\qquad y_i=1+32i,\qquad 0\le i<d+2.
$$


Then


$$
x_iy_j-x_jy_i=32(j-i),\qquad \mu=1,
$$


and the interpolation coefficients are exactly $(1-i,i)$.

Let all remaining columns have zero entries in the first two rows and bottom block


$$
2^{M+1}\operatorname{diag}(1,\ldots,1,1+s).
$$


Every remaining column is row-constant modulo $2$. The same paid elimination produces


$$
\mathcal P(s)=2^M\operatorname{diag}(1,\ldots,1,1+s),
$$


so


$$
\det\mathcal P(s)=2^{Md}(1+s)
$$


and the residual coefficient gcd has valuation $Md$, arbitrarily large.

This is **not** a counterexample to a proposed bound for the original source pencil. It is a counterexample to inferring such a bound from the fixed-rank cofactor and parity facts alone. Additional original-source information about the remaining complete columns is indispensable.

### Exact follow-on lemma

The concrete remaining binary target is:

> **Residual original-domain upper-bound lemma — open.**  
> There exist constants $C$ and $k_0$ such that, for every
> 

$$
> k\in\mathcal K,\qquad k\ge k_0,
>
$$


> the actual complete pencil constructed in (6.7) satisfies
> 

$$
> \boxed{
> \min(v_2(P_{0,k}),v_2(P_{1,k}))
> \le \frac{15}{4}k^2+Ck\log k.
> }
>
$$



Combined with (7.5)–(7.6), this would give


$$
v_2(G_k)\le\frac{19}{4}k^2+O(k\log k).
$$



A useful next proof must evaluate an additional common-column elimination or otherwise bound this actual coefficient pair. Merely renaming its determinant, exhibiting another invertible forcing pivot, or providing a lower divisor of its content would not prove the lemma.

**Section 8 verdict: PASS as a statement of quantified progress and remaining limitation.**

---

## 10. Reused analytic and odd-prime consequences

The closed same-$H$ spread estimate is reused, not recalculated:


$$
\log|H_k(e+\pi)|
\ge
4k^2\log k+
\left(15\log2-\frac92\log3+\frac4{85}\right)k^2
+o(k^2).
\tag{10.1}
$$



Likewise, for $k=3^s\in\mathcal K$, reuse


$$
v_3(\mathscr L_k)=v_3(\mathscr R_k)
=E_k=\frac{(k-2)(k-1-2s)}2.
$$


This gives only


$$
E_k\le v_3(G_k)\le2E_k+s+1,
$$


not an equality for $v_3(G_k)$.

The other odd-prime hypotheses remain independent and open:


$$
v_p(\mathscr L_k),v_p(\mathscr R_k)\le B_p(k)
\qquad(5\le p\le6k-5),
$$


and


$$
v_p(\mathscr L_k)=v_p(\mathscr R_k)=0
\qquad(p>6k-5),
$$


where


$$
B_p(k)=
k\bigl(2\mathbf1_{p=3}+v_p(\Lambda_k)\bigr)
+4\sum_{j=0}^{k-1}v_p(j!).
$$



Neither the oddness of $\eta_d$ and $\mu_k$ nor their appearance in an exact scalar transfer proves these global odd-prime statements.

Conditionally on those odd-prime hypotheses and on the residual binary lemma, the already audited sharp odd payment gives


$$
\log\ell_k
\ge
\left(
\frac{57}{4}\log2-\frac72\log3-\frac{506}{85}
\right)k^2+o(k^2).
$$


The coefficient is positive by the existing certified logarithm bounds. Thus those hypotheses would imply


$$
\ell_k\longrightarrow+\infty
\qquad(k\in\mathcal K).
$$



That would retire this producer as a source of primitive whole-error decay. It would **not** prove $e+\pi$ rational, and it would not decide the global rationality question.

---

## 11. Bounded exact arithmetic and proof-status ledger

No code execution or new matrix calculation is needed for this audit. In particular, no original-size solve, factorial determinant scan, adjacent scan, capped Smith calculation, or new content scan is proposed.

The existing $k=32,33$ diagnostics are not rerun or extrapolated. They are outside the original index set and establish only their stated finite values.

The only optional small arithmetic checksum is:

- **Inputs:** arithmetic in $\mathbb F_2$,
  

$$
\theta_0=1,\quad\theta_1=0,\quad
  \theta_{n+2}=\theta_{n+1}+\theta_n,
$$


  and
  

$$
\zeta_n=\theta_n+(n+1)\theta_{n+1}.
$$


- **Bound:** indices $0,\ldots,5$.
- **Expected output:**
  

$$
(\theta_0,\ldots,\theta_5)=(1,0,1,1,0,1),
$$


  

$$
(\zeta_0,\ldots,\zeta_5)=(1,0,0,1,1,1).
$$


- **Scope:** a checksum of the local parity calculation only. The uniform recurrence proof, not this finite table, establishes the infinite parity statements. It supplies no bound for $\nu_k$.

| Statement | Audit status |
|---|---|
| Full Newton payments $2^rr!$, including odd parts | **PASS** |
| Finite-difference product rule and shifted arguments | **PASS**, explicitly expanded |
| Contact parity generating function | **PASS** |
| Normalized atom modulo $4$ | **PASS** |
| Divided $\Delta\sigma$ source oddness and row constancy modulo $4$ | **PASS** |
| Distinguished last-two-top-row source minor | **PASS**, valuation exactly $1$ |
| Complete bottom forcing Cauchy minors | **PASS**, with both factorial terms retained |
| Factorial adjugate gaps and complementary leading Pascal blocks | **PASS** |
| Valuation of every other compound term | **PASS**, at least $7$ |
| Both literal bottom source corrections | **PASS**, divisible by $64$ |
| Actual two-column content | **PASS**, binary valuation exactly $5$ |
| Attaining original-row minor | **PASS**, rows $m=d,d+1$ |
| Integral Cramer division by $32$, odd $\mu_k$, interpolation residues | **PASS** |
| Every corrected column and both affine-border coefficients | **PASS** |
| All $d$ row divisions by $2$ | **PASS** |
| Column-transposition sign and all-prime scalar transfer | **PASS** |
| Exact $\chi_k$, actual $q_k$, and nonzero whole error | **PASS** |
| Separate full turn10 dyadic-construction audit | **Still pending with A3** |
| Residual bound $\nu_k\le15k^2/4+O(k\log k)$ | **OPEN** |
| Other odd-prime descents and large-prime exclusion | **OPEN** |
| Primitive whole-error divergence | **CONDITIONAL** |
| Rationality or irrationality of $e+\pi$ | **UNRESOLVED** |

## Final conclusion

The new source-specific theorem passes the independent audit. Its substantive proved advance is the exact depth-five evaluation of the **complete corrected pair**, with an attaining original-row minor, integral Cramer payments, and an explicitly retained odd interpolation denominator. The subsequent parity argument correctly removes one factor $2$ from each of the $d$ remaining rows, including the whole affine border.

The resulting exact identities are


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_k|^{d-1}G_k
=
|f_k|\,2^{\lambda_d+d+5}\mathfrak D_dg_k^{\mathrm{new}},
}
$$


and


$$
\boxed{
v_2(G_k)=
d^2+4d+29+(d+4)s_2(d)
-3\sum_{n<d}s_2(n)+\nu_k.
}
$$



The exact remaining binary bottleneck is the upper bound for the actual complete coefficient pair


$$
\boxed{
\nu_k=v_2\gcd(|P_{0,k}|,|P_{1,k}|).
}
$$


Its target $15k^2/4+O(k\log k)$ remains unproved. The other odd-prime descents, including exclusion of primes above $6k-5$, remain separate open obligations.

No further bounded matrix computation is necessary to verify this new theorem, and no finite scan can replace those uniform obligations. The original index set, physical terminal, complete forcing, all-prime gcd, actual primitive denominator, and nonzero whole evaluated error have all been preserved.
