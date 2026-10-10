> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All-order source ranks and a paid mixed-compound window for the complete Newton–Cauchy pencil

## 1. Results and limitations

The rationality or irrationality of $e+\pi$ remains unresolved. In particular, this report does **not** prove the required upper bound


$$
\nu_k^{[5]}\le \frac{15}{4}k^2-64+O(k\log k),
\qquad k=9^{18+32u}.
$$



It does establish four new, source-specific results.

1. **The parent finite-field filter is correct.**  
   Its derivative term is necessary, and the two-carry algorithm evaluates the stated normalized contact-jet parity at every admissible order. No extension of the old $r+j<16$ formula is used.

2. **The old growing source-unit hypothesis is obstructed.**  
   After the row normalization relevant to the old source-minor divisor, the contact-jet matrix has an explicitly evaluated binary rank. In particular, every row whose index shares a binary $1$-digit with $d$ vanishes. Consequently, the old source-minor payment $b_q$ is unattainable for every
   

$$
18\le q\le d,
$$


   regardless of which actual Newton return columns are chosen.

   A stronger, fully paid source divisor is proved, and an explicit family of binary-unit contact-jet minors is constructed using the actual binary digits of $d$. These are source-jet minors, not substitutes for the complete corrected physical cofactors.

3. **The entrywise correction barrier is crossed on a linear-rank interval.**  
   A mixed-compound argument proves a comparison between complete corrected common-column minors and their pure Cauchy-product terms for
   

$$
1\le q\le \left\lfloor\frac d8\right\rfloor.
$$


   The comparison is valid through an explicitly defined depth
   

$$
\Theta_q(d)=5q^2+O(q\log d),
$$


   even when $\Theta_q(d)$ is much larger than the entrywise correction threshold $L_d=\alpha_d-12$.

   Thus the former $O(\sqrt d)$-rank precision limitation is replaced by an unconditional $\Omega(d)$-rank mixed-compound window. This does not finish the $d+1$-common-column elimination.

4. **The first direct weighted-return correction layer in the actual $\mathcal P_k^{[5]}$ is evaluated.**  
   After the already paid five-column elimination, the normalized weighted-return bottom corrections are divisible by $2^7$, with a fully evaluated residue for every remaining return order. At the first remaining physical row and return order $3$, the correction has exact depth
   

$$
\boxed{L_d+7.}
$$


   This is an evaluation of an actual correction summand, not a new common-column pivot and not a valuation of the whole entry or either terminal determinant coefficient.

All original scalar transfers, odd Cramer denominators, factorial payments, coefficient borders, finite boundaries, actual contents, final all-prime gcd, primitive denominator, and nonzero whole error are retained.

---

## 2. Original objects and established payments retained

### 2.1 Domain, sequences, returns, and terminal

Throughout,


$$
\boxed{k=9^{18+32u},\qquad u\ge0,\qquad d=k-1.}
$$


Thus


$$
v_2(d)=4,\qquad d\equiv2\pmod3,\qquad d\equiv2\pmod6.
$$



The original sequences are


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad w_n=(-1)^n,\qquad c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-f_n+4\rho_n.
$$



The complete returns remain


$$
\sigma_n=u_{n+1}+u_n=c_{n+1}+c_n
$$


and


$$
\boxed{\tau_n=-(2n+2)!-(2n)!+\frac4{2n+1}.}
$$


Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),\qquad T_n=\Lambda_k\tau_n.
$$


In particular,


$$
T_n=-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)+\frac{4\Lambda_k}{2n+1}.
$$



The original affine determinant is


$$
H_k(s)=
\det\left[
(c_{m+j})\
\middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s,
$$


with $0\le m<2k$, $0\le j<k$.

The physical last row remains $2k-1=2d+1$. The terminal data remain


$$
\boxed{\text{moment }3k-2,\qquad (6k-4)!,\qquad 6k-5.}
$$



### 2.2 Actual clearers, contents, gcd, and primitive error

The individual least original right-column entry clearers are


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3),
\qquad 0\le j<k.
$$


The common least entry clearer is $\Lambda_k$.

Retain


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
\qquad
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


The rational coefficient pair $H_k/\Lambda_k^k$ has actual least simultaneous coefficient clearer and subsequent content


$$
\boxed{\frac{\Lambda_k^k}{d_{H,k}},\qquad \frac{G_k}{d_{H,k}}.}
$$



The original rectangles are


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


Their actual maximal-minor contents


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k)
$$


satisfy the established interface


$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k\mid \Lambda_k\mathscr L_k\mathscr R_k.
$$



The established sign and nonvanishing results apply at every original index, giving


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
$$


No lower divisor of $G_k$ is substituted for this normalization.

### 2.3 The exact corrected pencil

Write


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),\qquad
\mathcal A_d y=\Delta^d(P_dy),
$$


where the equality uses that $d$ is even. This operator is applied only to the original first $d$ rows. Its determinant payment is


$$
\Omega_k=\prod_{n=0}^{d-1}P_d(n),
$$


an odd integer retained in full.

Put


$$
\mathfrak b(t)=4t^2+6t+3.
$$


The complete forcing block is


$$
F_k(n,j)=
-\Lambda_k\sum_{i=0}^d(-1)^i\binom di
P_d(n+i)\mathfrak b(n+i+j)(2(n+i+j))!,
\qquad n,j<d.
$$


Thus $\mathfrak b(t)(2t)!=(2t+2)!+(2t)!$, and both factorial terms remain.

With $D_f=\operatorname{diag}((2n)!)_{n<d}$, write


$$
F_k=-\Lambda_kD_fK_dD_f.
$$


To distinguish the forcing determinant from the contact sequence below, denote


$$
\eta_d^F=\det K_d.
$$


The established Pascal congruence makes $\eta_d^F$, and every leading principal determinant of $K_d$, odd.

Retain


$$
f_k=(-\Lambda_k)^d\eta_d^F
       \left(\prod_{n<d}(2n)!\right)^2,
$$




$$
h_d=(2d-2)!,\quad \beta_d=v_2(h_d),\quad
\alpha_d=v_2((2d)!),\quad \alpha_d=\beta_d+5,
$$




$$
N_d=(h_dD_f^{-1})\operatorname{adj}(K_d)(h_dD_f^{-1}),
\qquad
\delta_k=\Lambda_k\eta_d^Fh_d^2.
$$


Then


$$
F_k^{-1}=-N_d/\delta_k.
$$



Residual row $i$, $0\le i<d+2$, is physical row $m=d+i$. The complete bottom forcing matrix is


$$
\boxed{
R(i,j)=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}\mathfrak b(d+i+j)(2(d+i+j))!,
\quad j<d.
}
$$



Every full Newton divisor


$$
D_r=2^rr!,\qquad 0\le r<d,
$$


including its odd part, is retained. Put


$$
\mathfrak D_d=\prod_{r<d}D_r,\qquad o_d=\operatorname{odd}(d!),
$$


and define the actual top sources


$$
\mathsf a_n=\frac{(\mathcal A_dc)_n}{2^d},
\qquad
t_n^{(r)}
=\frac{(\mathcal A_d\Delta^r\sigma)_n}
       {2^{\alpha_d+1}D_r},
\quad n,r<d.
$$



The complete corrected columns are


$$
x=RN_d\mathsf a+\frac{\delta_k}{2^{d+2}}c_{\rm bot},
$$




$$
z^{(r)}
=RN_dt^{(r)}
+\frac{\delta_k}{2^{\alpha_d+3}D_r}
       (\Delta^r\sigma)_{\rm bot},
$$


and, with $\psi_0=r,\ \psi_1=w$,


$$
\mathfrak b_j
=RN_d\Lambda_k(\mathcal A_d\psi_j)_{\rm top}
+\frac{\delta_k\Lambda_k}{4}(\psi_j)_{\rm bot},
\quad j=0,1.
$$


Thus


$$
\mathcal Q_k(s)
=[x,z^{(0)},z^{(1)},\ldots,z^{(d-1)},\mathfrak b_0+s\mathfrak b_1].
$$



### 2.4 Fixed cofactor payments are reused, not recalculated

The already evaluated selected columns are


$$
[x,z^{(1)},z^{(0)},z^{(5)},z^{(4)}].
$$


Their nested complete contents have binary depths $5,19,39,72$, and their actual attaining cofactors satisfy


$$
\det\Pi_{q,k}=2^{t_q}\mu_{q,k},
\quad
(t_2,t_3,t_4,t_5)=(5,19,39,72),
$$


with every $\mu_{q,k}$ odd.

The fixed residual payments are $13,19,32$. Their all-prime identities retain all four odd Cramer factors:


$$
|\mu_{3,k}|^{d-2}g_k^{[2]}
=2^{13}|\mu_{2,k}|^{d-1}g_k^{[3]},
$$




$$
|\mu_{4,k}|^{d-3}g_k^{[3]}
=2^{19}|\mu_{3,k}|^{d-2}g_k^{[4]},
$$




$$
|\mu_{5,k}|^{d-4}g_k^{[4]}
=2^{32}|\mu_{4,k}|^{d-3}g_k^{[5]}.
$$



In particular,


$$
\boxed{\nu_k=64+\nu_k^{[5]}.}
$$


With $\lambda_d=d\alpha_d+4d+4$, the complete all-prime transfer remains


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_d+d+69}\mathfrak D_d\,g_k^{[5]}.
}
\tag{2.1}
$$


Consequently,


$$
\boxed{
v_2(G_k)=\chi_k+64+\nu_k^{[5]},
}
$$


where


$$
\chi_k=d^2+4d+29+(d+4)s_2(d)-3\sum_{n<d}s_2(n).
$$


None of these established payments is an upper bound for $\nu_k^{[5]}$.

---

## 3. Independent verification of the all-order filter

### 3.1 Exact product-rule identity in the original sources

Define


$$
Q_h(n)=\prod_{a=h}^{d-1}(2n+2a+1),
\qquad
\eta_t^{(m)}=\frac{\Delta^t\sigma_m}{2^{t+1}t!}.
$$


The established sequence divisibility makes every $\eta_t^{(m)}$ integral, and


$$
\Delta^hP_d(n)=2^h\frac{d!}{(d-h)!}Q_h(n).
$$



Applying the finite-difference product rule to
$\Delta^{d+j}(P_d\Delta^r\sigma)$, with every product-rule term retained, gives


$$
\boxed{
\frac{\Delta^jt_n^{(r)}}{2^j(r+1)_j}
=
o_d\sum_{h=0}^d
\binom{d+j}{h}Q_h(n)
\binom{d-h+r+j}{r+j}
\eta_{d-h+r+j}^{(n+h)}.
}
\tag{3.1}
$$


This calculation does not commute $\mathcal A_d$ with $\Delta^r$.

The contact premises give


$$
\theta_t=\frac{\Delta^tu_0}{2^tt!},\qquad
\eta_t=\theta_t+(t+1)\theta_{t+1},
$$


with


$$
\theta_{t+2}=\theta_{t+1}+\theta_t\pmod2,
\qquad (\theta_0,\theta_1)=(1,0)\pmod2.
$$


Also,


$$
\eta_t^{(m+1)}-\eta_t^{(m)}
=2(t+1)\eta_{t+1}^{(m)},
$$


so $\eta_t^{(m)}\equiv\eta_t\pmod2$.

Reducing (3.1) and setting $t=d-h$ proves, without a low-order restriction,


$$
J(d,r,j):=
\frac{\Delta^jt_n^{(r)}}{2^j(r+1)_j}\pmod2
=
\sum_{t=0}^d
\binom{d+j}{t+j}
\binom{t+j+r}{j+r}\eta_{t+j+r}\pmod2.
\tag{3.2}
$$



### 3.2 The root formula and its derivative term

Work in


$$
\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1),
\qquad \operatorname{Tr}(z)=z+z^2.
$$


The contact parities are exactly


$$
\theta_m=\operatorname{Tr}(\omega^{m+2}),
$$




$$
\eta_m
=\operatorname{Tr}\!\left(
\omega^{m+2}[1+(m+1)\omega]
\right).
\tag{3.3}
$$



Put $n_0=d+j$, $K=j+r$, and


$$
C(a,b,K)=[z^K](1+z)^a[1+\omega(1+z)]^b.
$$


Writing $\ell=t+j$, terms with $\ell<j$ vanish because
$\binom{\ell+r}{K}=0$. Hence the binomial sum may run over $0\le\ell\le n_0$.

The part containing $\ell$ uses


$$
\sum_\ell \ell\binom{n_0}{\ell}X^\ell
=(n_0\bmod2)X(1+X)^{n_0-1}.
$$


Substitution of $X=\omega(1+z)$ therefore gives


$$
\boxed{
J(d,r,j)=
\operatorname{Tr}\!\left(
\omega^{r+2}
\left\{
[1+(r+1)\omega]C(r,n_0,K)
+(n_0\bmod2)\omega^2C(r+1,n_0-1,K)
\right\}
\right).
}
\tag{3.4}
$$



This verifies the parent formula. The derivative term is present whenever its coefficient is nonzero; it has not been suppressed by the fact that the original $d$ is even.

### 3.3 Two-carry evaluation and complexity

Since $1+\omega=\omega^2$,


$$
C(a,b,K)
=\omega^{2b}
\sum_{\substack{u+v=K\\u\subseteq_{\rm bit}a\\v\subseteq_{\rm bit}b}}
\omega^{-v}.
\tag{3.5}
$$



At binary position $i$, choose $u_i\le a_i$, $v_i\le b_i$, and retain precisely the transitions


$$
u_i+v_i+c_i=K_i+2c_{i+1},
\qquad c_i,c_{i+1}\in\{0,1\}.
$$


The transition weight is


$$
\omega^{-v_i2^i\bmod3}.
$$


Starting with carry $0$, and ending with carry $0$ after sufficiently many zero leading digits, evaluates (3.5). A zero input bit supplies one zero choice, not two duplicate choices.

Thus, given the binary inputs, one entry takes $O(\log(a+b+K+1))$ fixed-field operations.

This is **not** an $O(\log d)$ algorithm for a growing determinant. Filling a $q\times q$ parity matrix generally costs $O(q^2\log d)$, followed by, for example, $O(q^3)$ field operations for elimination. Computing the full integer entries or their odd cofactors is a different, much larger problem.

---

## 4. A structurally evaluated all-order source-rank law

The determinant normalization uses not $J(d,r,j)$ alone, but


$$
\mathcal J_{jr}
:=
\frac{\Delta^jt_0^{(r)}}{2^jj!}\pmod2
=
\binom{r+j}{j}J(d,r,j)\pmod2.
\tag{4.1}
$$



This distinction matters: when the binomial prefactor is even, $\mathcal J_{jr}=0$ need not imply $J(d,r,j)=0$.

### 4.1 An additional exact row divisor

A factorial identity in (3.1) gives


$$
\binom{d+j}{h}
\binom{d-h+r+j}{r+j}
\binom{r+j}{j}
=
\binom{d+j}{j}\binom dh
\binom{d-h+r+j}{r}.
$$


Consequently,


$$
\boxed{
\frac{\Delta^jt_n^{(r)}}{2^j(d+1)_j}
=
o_d\sum_{h=0}^d
\binom dh Q_h(n)
\binom{d-h+r+j}{r}
\eta_{d-h+r+j}^{(n+h)}
\in\mathbb Z.
}
\tag{4.2}
$$



The full integer $(d+1)_j$, not merely its binary part, divides as stated. This is a source-row divisibility assertion; it is not an unproved simultaneous row division of the whole corrected pencil, whose atom column has a different normalization.

### 4.2 Closed bitwise values

For nonnegative $r,j$ in the finite source range,


$$
\boxed{
\mathcal J_{jr}
=
\begin{cases}
\eta_{\,j+r+2d+(r\mathbin{\&}d)},&
j\mathbin{\&}(d\mathbin{|}r)=0,\\[2mm]
0,&j\mathbin{\&}(d\mathbin{|}r)\ne0,
\end{cases}
\quad\text{in }\mathbb F_2.
}
\tag{4.3}
$$



Here $\eta_m$ means the evaluated parity in (3.3).

#### Proof

If $r\mathbin{\&}j\ne0$, Lucas’ theorem makes the prefactor in (4.1) zero. If $d\mathbin{\&}j\ne0$, the exact factor $\binom{d+j}{j}$ in (4.2) is even. Thus only the no-carry case


$$
r\mathbin{\&}j=d\mathbin{\&}j=0
$$


requires evaluation.

Vandermonde’s identity gives


$$
\binom{d+j}{t+j}\binom{t+j+r}{j+r}
=
\sum_a
\binom ra\binom{d+j}{j+a}\binom{d-a}{t-a}.
\tag{4.4}
$$


In the no-carry case, the surviving $a$'s are precisely the binary subsets of


$$
e=r\mathbin{\&}d.
$$


Every such $a$, and $d-a$, is even.

For a surviving $a$, set $t=a+h$. The inner contact filter is


$$
\sum_h\binom{d-a}{h}\eta_{h+a+j+r}.
$$


Using (3.3), its derivative contribution vanishes because $d-a$ is even. Its value is


$$
\operatorname{Tr}\!\left(
\omega^{j+r+2+2d-a}[1+(j+r+1)\omega]
\right).
$$


Finally,


$$
\sum_{a\subseteq_{\rm bit}e}\omega^{-a}
=(1+\omega^{-1})^e=\omega^e.
$$


Because $e$ is even, the resulting trace is exactly
$\eta_{j+r+2d+e}$. This proves (4.3). ∎

The simplification is legitimate only after the no-carry restrictions and the reorganization (4.4). It does not justify deleting the derivative term from the general formula (3.4).

For example,


$$
J(d,0,j)=
\mathbf1_{d\mathbin{\&}j=0}\,\eta_{j+2d}.
$$


Hence


$$
J(d,0,17)=0
$$


at every original index, whereas extrapolating the former low-order period would give $\varepsilon_{17}=1$. This is a concrete failure of that extrapolation.

### 4.3 Exact rank and an explicit unit family

Let


$$
m_d=1+\lfloor\log_2d\rfloor,\qquad
F_d=2^{m_d}-1-d.
$$


Thus $F_d$ is the bitwise complement of $d$ within its actual binary length.

For $1\le q\le d$, define


$$
C_d(q)=\#\{0\le j<q:j\mathbin{\&}d=0\}.
$$



#### Theorem 4.1 — exact normalized contact rank

For the matrix with rows $0\le j<q$ and all actual columns $0\le r<d$,


$$
\boxed{\operatorname{rank}_{\mathbb F_2}(\mathcal J_{jr})=C_d(q).}
\tag{4.5}
$$



#### Proof

Rows with $j\mathbin{\&}d\ne0$ vanish by (4.3), proving the upper bound.

List the remaining row indices increasingly:


$$
j_0<\cdots<j_{C_d(q)-1}.
$$


Choose actual return columns


$$
r_\ell=F_d-j_\ell.
$$


These are nonnegative and less than $d$, because $F_d<2^{m_d-1}\le d$.

The entry in row $j_a$, column $r_\ell$, can be nonzero only if


$$
j_a\subseteq_{\rm bit}j_\ell.
$$


It therefore vanishes when $a>\ell$. On the diagonal,


$$
j_\ell+r_\ell=F_d,\qquad r_\ell\mathbin{\&}d=0,
$$


so the diagonal value is


$$
\eta_{F_d+2d}
=\eta_{2^{m_d}-1+d}.
$$


Since $d\equiv2\pmod6$, this index is $3$ or $5\pmod6$; both contact parities are $1$. The selected matrix is upper triangular with diagonal $1$. ∎

In particular,


$$
\boxed{C_d(d)=2^{m_d-s_2(d)}.}
\tag{4.6}
$$


The binary rank is evaluated without computing a growing determinant.

More generally, any set of return indices $R_0$ consisting of binary subsets of $F_d$ has a unit minor on jet rows


$$
J_0=\{F_d-r:r\in R_0\}.
$$


After ordering by inclusion-compatible numerical order, the same triangular argument applies.

The actual return indices $1,0,5,4$ are binary subsets of $F_d$, because the lowest four digits of $d$ vanish. Hence this contact-jet unit family can be nested so that its return-column order begins


$$
1,0,5,4.
$$


For such a minor,


$$
\det[\Delta^jt_0^{(r)}]_{j\in J_0,r\in R_0}
=
\left(\prod_{j\in J_0}2^jj!\right)\xi_{J_0,R_0},
\qquad \xi_{J_0,R_0}\ \text{odd}.
\tag{4.7}
$$


The odd integer $\xi_{J_0,R_0}$ is not assigned the value $1$.

These are evaluated **jet-minor** payments. They do not replace the original physical attaining cofactor $\Pi_{5,k}$, nor do they yet attain the optimal atom-containing source-minor budget below.

### 4.4 Genuinely growing flags at proved original indices

No unproved assertion about the distribution of digits of powers of $9$ is needed to obtain arbitrarily large members of this unit family.

First,


$$
9^{18+32u}=81^{9+16u}\equiv209\pmod{256},
$$


so $d\equiv208\pmod{256}$.

For every $H\ge8$, there is a residue class $u_H\pmod{2^{H-8}}$ such that


$$
9^{18+32u}\equiv209\pmod{2^H}.
\tag{4.8}
$$


This follows by explicit lifting. Start with $u_8=0$. At the next step, either retain $u_H$ or add $2^{H-8}$. Indeed,


$$
81^{2^{H-4}}\equiv1+2^H\pmod{2^{H+1}},
$$


so that addition toggles precisely the required next bit.

Every resulting residue class contains infinitely many original indices. On it,


$$
d\equiv208\pmod{2^H},
$$


whose lowest $H$ digits have only the three $1$-digits $4,6,7$. For sufficiently large members of that class,


$$
C_d(d)\ge2^{H-3}.
$$


Thus the explicit contact-jet unit flags have unbounded length at rigorously specified original indices.

This is not a replacement of the global index domain, and it is not a proof of the remaining complete-cofactor unit hypothesis.

---

## 5. A stronger source divisor and a definitive obstruction to the old flag

Define


$$
v_j(d)=v_2((d+1)_j)
=j+s_2(d)-s_2(d+j).
$$


These valuations are nondecreasing in $j$.

For $q\ge1$, put


$$
\boxed{
B_q(d)=\binom q2+\sum_{j=0}^{q-2}v_j(d).
}
\tag{5.1}
$$


Equivalently,


$$
B_q(d)
=(q-1)^2+(q-1)s_2(d)-\sum_{j=0}^{q-2}s_2(d+j).
\tag{5.2}
$$



### Theorem 5.1 — stronger actual source-minor divisor

Every $q$-minor of a top source matrix consisting of one atom-contact column and $q-1$ actual weighted return sources is divisible by $2^{B_q(d)}$.

The same lower divisor is valid if all $q$ selected columns are return sources.

#### Proof

Use the finite, determinant-one Newton row transformation on the $d$ actual top rows.

For a selected set of jet orders $j_0<\cdots<j_{q-1}$, extract $2^{j_0+\cdots+j_{q-1}}$. The atom source has integral normalized jets; each return source has the additional full divisor $(d+1)_{j_a}$ by (4.2).

Expanding in the atom column, the smallest possible additional binary payment omits the largest $v_{j_a}(d)$. Monotonicity therefore gives


$$
\sum_a j_a+\sum_{a=0}^{q-2}v_{j_a}(d)
\ge
\binom q2+\sum_{j=0}^{q-2}v_j(d).
$$


If every column is a return source, there is an additional nonnegative payment. ∎

The former divisor was


$$
b_q=\binom q2+\sum_{j=0}^{q-2}v_2(j!).
$$


Their exact difference is


$$
\boxed{
B_q(d)-b_q
=\sum_{j=0}^{q-2}v_2\binom{d+j}{j}.
}
\tag{5.3}
$$



Because the $2^4$-digit of $d$ is $1$, the term $j=16$ is positive. Hence:

### Corollary 5.2 — the old attaining-source hypothesis fails

For every original index and every $18\le q\le d$,


$$
\boxed{
v_2\det A[J,:]\ge b_q+1
}
$$


for every actual $q$-row source minor and every choice of the actual return columns.

In particular, the former hypothesis


$$
v_2\det A[T_q,:]=b_q
$$


cannot hold for a growing flag.

This is not merely a fixed-rank anomaly. From (5.3),


$$
B_q(d)-b_q
\ge (q-1)-C_d(q-1).
$$


Since the $2^4$-digit excludes half of each complete block of $32$,


$$
C_d(q-1)\le \frac{q-1}{2}+8.
$$


Thus


$$
\boxed{
B_q(d)-b_q\ge \frac{q-1}{2}-8.
}
\tag{5.4}
$$



The old source-unit obligation is therefore answered negatively at its stated scale.

### 5.3 The repaired source parity problem is explicit

The stronger normalized entries


$$
\widetilde{\mathcal J}_{jr}
=
\frac{\Delta^jt_n^{(r)}}{2^j(d+1)_j}\pmod2
$$


also have an evaluated finite-field formula:


$$
\boxed{
\widetilde{\mathcal J}_{jr}
=
\operatorname{Tr}\!\left(
\omega^{j+r+2}[1+(j+r+1)\omega]\,
C(j+r,d,r)
\right).
}
\tag{5.5}
$$



To check it, reduce (4.2), set $t=d-h$, and use


$$
\binom{t+j+r}{r}=[z^r](1+z)^{t+j+r}.
$$


Only even $t$'s survive because $d$ is even. The trace factor involving $t\bmod2$ is therefore constant, and the remaining binomial theorem is exactly the coefficient $C(j+r,d,r)$. Its two-carry evaluation has already been proved.

For a consecutive $q$-row source minor containing the atom, the parity after division by $2^{B_q(d)}$ is consequently an explicit contact-row determinant:

- if $q$ is odd, use rows $0,\ldots,q-2$ of $\widetilde{\mathcal J}$;
- if $q$ is even, use rows $0,\ldots,q-3$, followed by
  

$$
\widetilde{\mathcal J}_{q-2,\bullet}
  +\widetilde{\mathcal J}_{q-1,\bullet}.
$$



Indeed, the atom can contribute at minimal valuation only in the row or rows where $v_j(d)$ is maximal. Since $d$ is even, those are exactly the last row for odd $q$, and the last two rows for even $q$.

This repairs the source-unit criterion. Its growing original-domain solution for the **optimal atom-containing physical flag** is still open.

---

## 6. A uniform exact form of every bottom correction

Set


$$
L_d=\alpha_d-12,\qquad
M_d=\alpha_d-d+1,
$$


and retain the actual odd integer


$$
\gamma_k=\frac{\delta_k}{2^{2\beta_d}}
=\Lambda_k\eta_d^F\operatorname{odd}(h_d)^2.
$$



Because


$$
\Delta^r\sigma_m=2D_r\eta_r^{(m)},
$$


all corrected columns can be written simultaneously as


$$
\boxed{
\mathcal Q_k(s)
=RN_d\mathcal A_k(s)+2^{L_d}\gamma_k\mathcal W_k(s),
}
\tag{6.1}
$$


where


$$
\mathcal A_k(s)=
[\mathsf a,t^{(0)},\ldots,t^{(d-1)},
 \Lambda_k(\mathcal A_d(r+sw))_{\rm top}]
$$


and


$$
\boxed{
\mathcal W_k(s)=
\left[
2^{M_d}\frac{c_{\rm bot}}2,\
(\eta_r^{(d+i)})_{r<d},\
2^{\alpha_d}\Lambda_k(r+sw)_{\rm bot}
\right].
}
\tag{6.2}
$$



Every entry is integral. In particular:

- the atom correction has its full extra factor $2^{M_d}$;
- every weighted return correction uses the actual $\eta_r^{(m)}$, whose denominator includes the full $r!$;
- both border corrections retain their complete factor $2^{\alpha_d}\Lambda_k$;
- the full odd factor $\gamma_k$ remains.

The factorial correction inside $R$ also has an exact uniform form. Define


$$
R^{\rm C}(i,j)=\frac{\Lambda_k}{2(d+i+j)+1},
$$




$$
V(i,j)=
\frac{\Lambda_k\mathfrak b(d+i+j)(2(d+i+j))!}{2^{\alpha_d}}.
$$


Then $V$ is integral and


$$
\boxed{R=R^{\rm C}-2^{\alpha_d-2}V.}
\tag{6.3}
$$


This retains both factorial terms, since $\mathfrak b(n)(2n)!=(2n+2)!+(2n)!$.

Equations (6.1)–(6.3) are exact at all depths.

---

## 7. A paid mixed Cauchy identity

Let $M$ be $q$ increasing residual row indices, and let $I$ be $a$ increasing forcing-column indices, with $a\le q$. Put


$$
Q_I(i)=\prod_{j\in I}(2(d+i+j)+1),
\qquad
\Phi_a=\prod_{j=0}^{a-1}j!.
$$



For any additional integer columns $Z$ making a square $q$-column matrix,


$$
\boxed{
\begin{aligned}
&\det[R^{\rm C}[M,I],Z[M,:]]\\
&\quad=
\frac{\Lambda_k^a\,2^{a(a-1)}\Phi_a V(I)}
     {\prod_{i\in M}Q_I(i)}
\det\left[
\left(\binom{i}{j}\right)_{\substack{i\in M\\0\le j<a}},
\ (Q_I(i)Z_i)_{i\in M}
\right].
\end{aligned}
}
\tag{7.1}
$$



Every odd denominator in this identity is displayed. It is not replaced by $1$ over $\mathbb Z$.

#### Proof

Multiply row $i$ by $Q_I(i)$. The first $a$ columns become


$$
\Lambda_k\prod_{\substack{j'\in I\\j'\ne j}}
(2(d+i+j')+1),
$$


polynomials in $i$ of degree at most $a-1$.

Their coefficient determinant in the binomial basis
$1,\binom i1,\ldots,\binom i{a-1}$ is


$$
\Lambda_k^a2^{a(a-1)}\Phi_aV(I).
$$


One factor $2^{\binom a2}V(I)$ comes from the pole differences, and the second factor $2^{\binom a2}\Phi_a$ from passing from powers of $2i$ to the binomial basis. Factoring that coefficient matrix proves (7.1). ∎

Define


$$
c_a=a(a-1)+2v_2(\Phi_a).
$$


Since $V(I)/\Phi_a$ is integral, (7.1) proves:

> Any square mixed determinant containing $a$ actual rational Cauchy columns and otherwise arbitrary integer columns is divisible by $2^{c_a}$.

This payment persists when the other columns are bottom corrections. It is the key improvement over an entrywise error estimate.

### 7.1 One normalized weighted-return column: evaluated residue

For $p$ Cauchy columns and one normalized return column


$$
W_r(i)=\eta_r^{(d+i)},
$$


put


$$
H_p=c_p+p+v_2(p!).
$$


Then


$$
2^{H_p}\mid
\det[R^{\rm C}[M,I],W_r[M]],
\qquad |M|=p+1,\ |I|=p,
$$


and


$$
\boxed{
\frac{\det[R^{\rm C}[M,I],W_r[M]]}{2^{H_p}}
\equiv
\mathcal N_{p+1}(M)\mathcal N_p(I)S_p(r)
\pmod2,
}
\tag{7.2}
$$


where


$$
\mathcal N_q(M)=\frac{V(M)}{\Phi_q}.
$$



The scalar $S_p(r)$ is explicitly evaluated. Set


$$
b=p-(p\mathbin{\&}r)=p\mathbin{\&}\neg r.
$$


Then


$$
\boxed{
S_p(r)=
\operatorname{Tr}\!\left(
\omega^{r+2+2b}
[1+(r+1)\omega+(b\bmod2)]
\right).
}
\tag{7.3}
$$



#### Derivation

The exact bottom jets are


$$
\Delta^jW_r(i)
=2^j(r+1)_j\eta_{r+j}^{(d+i)}.
\tag{7.4}
$$


Thus $2^jj!\mid\Delta^jW_r(i)$.

The product $Q_IW_r$ has the same divisibility. In (7.1), its Newton rows below degree $p$ are eliminated by the first $p$ polynomial columns. The first possible contribution is degree $p$, with payment $2^pp!$. Higher degrees contribute one additional power of $2$.

Moreover,


$$
\frac{\Delta^hQ_I(i)}{2^hh!}\equiv\binom ph\pmod2.
$$


The normalized degree-$p$ coefficient is therefore


$$
S_p(r)
=\sum_{t=0}^p
\binom pt\binom{r+t}{t}\eta_{r+t}\pmod2.
\tag{7.5}
$$


Lucas’ theorem restricts the surviving $t$'s precisely to binary subsets of $b=p\mathbin{\&}\neg r$. Applying (3.3) to that binomial filter gives (7.3), including its derivative contribution $b\bmod2$.

Thus (7.5) is not left as an unevaluated sum.

---

## 8. A linear-rank comparison theorem for complete corrected minors

Let


$$
e_n=v_2\!\left(\frac{h_d}{(2n)!}\right),
\qquad
E_q=\sum_{n=d-q}^{d-1}e_n,
$$


with $E_0=0$. Define


$$
\boxed{\Theta_q(d)=c_q+2E_q+B_q(d).}
\tag{8.1}
$$



The factorial-diagonal and adjugate facts already established imply


$$
v_2\det N_d[I,J]\ge2E_q
\quad (|I|=|J|=q),
$$


with equality for $I=J=\{d-q,\ldots,d-1\}$, and strictly larger valuation for every other pair. The equality uses the odd leading complementary determinant of $K_d$, not merely the oddness of $\det K_d$.

### Theorem 8.1 — growing corrected-compound window

Choose $q$ actual common columns, including the atom-contact column, and let $A_S$ be their top source matrix. Suppose


$$
L_d>10q+3m_d,
\qquad
\alpha_d-2>4q.
\tag{8.2}
$$


Then every corresponding complete corrected minor satisfies


$$
\boxed{
\det\mathcal C_S[M,:]
\equiv
\det(R^{\rm C}N_dA_S)[M,:]
\pmod{2^{\Theta_q(d)+1}}.
}
\tag{8.3}
$$


Both sides are divisible by $2^{\Theta_q(d)}$.

At every original index, (8.2) holds for all


$$
\boxed{1\le q\le\lfloor d/8\rfloor.}
\tag{8.4}
$$



#### Proof: every correction term is paid

Expand the determinant using (6.1). Suppose $h$ of its $q$ columns are taken from $\mathcal W_k$, leaving


$$
p=q-h
$$


product columns. Cauchy–Binet pays a $p$-minor of $N_d$ and a $p$-minor of the top source matrix.

Next expand those $p$ columns using (6.3). Suppose $v$ are factorial correction columns, leaving


$$
a=p-v
$$


rational Cauchy columns.

Every such term has the scalar payment


$$
2^{hL_d+v(\alpha_d-2)}\gamma_k^h.
$$


Its mixed bottom determinant contains $a$ Cauchy columns and otherwise integer columns, so (7.1) pays $2^{c_a}$. The $N_d$-minor pays $2^{2E_p}$, and Theorem 5.1 pays $2^{B_p(d)}$ from the source minor. If the atom was one of the bottom correction columns, all remaining source columns are returns, for which the same lower divisor is still valid.

Thus every term has valuation at least


$$
\boxed{
hL_d+v(\alpha_d-2)+c_a+2E_p+B_p(d).
}
\tag{8.5}
$$


The extra atom and border weights in $\mathcal W_k$ have not been discarded from the exact expansion; ignoring their nonnegative valuations only weakens this lower bound.

Now


$$
c_r-c_{r-1}\le4q\qquad(r\le q),
$$




$$
E_r-E_{r-1}
=e_{d-r}
=2r-2+s_2(d-r)-s_2(d-1)
\le2q+m_d,
$$


and


$$
B_r(d)-B_{r-1}(d)\le2q+m_d.
$$


Consequently,


$$
\Theta_q-\Theta_p\le h(10q+3m_d),
\qquad
c_p-c_a\le4qv.
$$


Subtracting $\Theta_q$ from (8.5) leaves at least


$$
h(L_d-10q-3m_d)+v(\alpha_d-2-4q).
\tag{8.6}
$$


Under (8.2), this is at least $1$ whenever $h+v>0$. Every term containing any correction therefore vanishes modulo $2^{\Theta_q+1}$.

The uncorrected term is divisible by $2^{\Theta_q}$, proving (8.3).

For the original indices, $d$ is far larger than $128$, and


$$
m_d\le d/16,\qquad \alpha_d=2d-s_2(d)\ge2d-m_d.
$$


If $q\le d/8$, then


$$
L_d-10q-3m_d
\ge \frac34d-4m_d-12
\ge\frac12d-12>0,
$$


and $\alpha_d-2-4q>0$. This proves (8.4). ∎

### 8.1 The resulting cofactor criterion

Put $T_q=\{d-q,\ldots,d-1\}$, and define the actual source residue


$$
u_q(S)=\frac{\det A_S[T_q,:]}{2^{B_q(d)}}\pmod2.
$$


Inside the proved window,


$$
\boxed{
\frac{\det\mathcal C_S[M,:]}{2^{\Theta_q(d)}}
\equiv u_q(S)\mathcal N_q(M)\pmod2.
}
\tag{8.7}
$$



This follows from the uniquely minimal principal $N_d$-minor and the exact Cauchy determinant. Therefore, if the repaired source criterion of Section 5.3 yields $u_q(S)=1$, the first $q$ residual physical rows attain the complete content depth $\Theta_q(d)$.

No growing assertion $u_q(S)=1$ is assumed here.

### 8.2 Why this changes the growing obligation

For $q\asymp d$,


$$
c_q=2q^2+O(q\log d),\quad
E_q=q^2+O(q\log d),\quad
B_q(d)=q^2+O(q\log d).
$$


Hence


$$
\Theta_q(d)=5q^2+O(q\log d).
$$



At $q=\lfloor d/8\rfloor$, the comparison depth is quadratic in $d$, while $L_d$ is only linear. Thus (8.3) is not an entrywise congruence disguised by new notation: the mixed Cauchy payments prove that every omitted determinant term has the required additional valuation.

The theorem does **not** say that corrections are harmless through $q=d+1$. Indeed, the pure product has rank at most $d$. Every complete $(d+1)$-common-column minor must use at least one bottom correction. For the full $(d+2)$-column coefficient determinant, at least two correction columns are required in the rank expansion.

That rank obstruction remains exact.

---

## 9. The first direct return-correction layer in the actual $\mathcal P_k^{[5]}$

This section does not introduce a sixth common-column pivot.

Let


$$
\mathcal C^{[5]}=[x,z^{(1)},z^{(0)},z^{(5)},z^{(4)}],
$$


and retain the actual complete pivot $\Pi_{5,k}$. Write


$$
M_{5,k}=\frac{V_{5,k}\operatorname{adj}(\Pi_{5,k})}{2^{72}},
$$


which is integral by the established cofactor theorem.

Define the exact row numerator


$$
\mathcal E_5=[-M_{5,k}\mid \mu_{5,k}I].
$$


Then


$$
\mathcal E_5\mathcal C^{[5]}=0,
$$


and the actual residual pencil is


$$
\mathcal P_k^{[5]}(s)
=\frac12\mathcal E_5\mathcal Q_{k,\rm remaining}(s).
\tag{9.1}
$$



The remaining return orders are exactly


$$
2,3,6,7,\ldots,d-1,
$$


followed by the complete affine border.

### 9.1 An all-depth corrected Schur form

Set


$$
R_5=\frac12\mathcal E_5R,\qquad
W_5(s)=\frac12\mathcal E_5\mathcal W_k(s).
$$


Both are integral:

- $R$ is entrywise odd, and the interpolation coefficient sum is $1\pmod2$;
- every column of $\mathcal W_k(s)$ is row-constant modulo $2$, coefficientwise in $s$.

Therefore


$$
\boxed{
\mathcal P_k^{[5]}(s)
=
R_5N_d\mathcal A_{k,\rm remaining}(s)
+2^{L_d}\gamma_kW_{5,\rm remaining}(s).
}
\tag{9.2}
$$



This identity retains the full constant and linear borders. It also retains the atom correction through the actual complete $M_{5,k}$, and through the exact relation
$\mathcal E_5\mathcal C^{[5]}=0$. The odd denominator $\mu_{5,k}$ has not been replaced by $1$.

Importantly, $R_5$ depends on the complete corrected pivot. Formula (9.2) does not pretend that all correction-dependence lies only in its second summand.

### 9.2 Evaluation of every weighted-return correction residue

For return order $r$, write


$$
W_{5,r}(i)=
\frac12\left(
\mu_{5,k}\eta_r^{(d+i)}
-\sum_{\ell=0}^4M_{5,k}(i,\ell)\eta_r^{(d+\ell)}
\right),
\quad 5\le i\le d+1.
$$



The bordered-determinant identity is exact:


$$
W_{5,r}(i)
=
\frac{
\det[\mathcal C^{[5]},\eta_r^{\rm bot}]
[\{0,1,2,3,4,i\},:]
}{2^{73}}.
\tag{9.3}
$$



Use the already established five-column source payment $12$, factorial-adjugate payment $30$, and the new mixed Cauchy payment


$$
H_5=c_5+5+v_2(5!)=30+5+3=38.
$$


The uniquely minimal term therefore has depth


$$
12+30+38=80.
$$


All other factorial-adjugate terms have at least one further power of $2$. The complete-column corrections and the factorial part of $R$ do not change this residue, since $L_d\ge100$ on the original domain.

Equation (7.2) now gives


$$
\boxed{
2^7\mid W_{5,r}(i),\qquad
\frac{W_{5,r}(i)}{2^7}
\equiv \binom i5 S_5(r)\pmod2.
}
\tag{9.4}
$$



The scalar is completely evaluated:


$$
\boxed{
S_5(r)=
\begin{cases}
\operatorname{Tr}(\omega^{r+1}),&r\mathbin{\&}4=0,\\
\operatorname{Tr}(\omega^{r+2}),&r\mathbin{\&}4\ne0.
\end{cases}
}
\tag{9.5}
$$


Equivalently, $S_5(r)=0$ precisely when

- $r\mathbin{\&}4=0$ and $r\equiv2\pmod3$, or
- $r\mathbin{\&}4\ne0$ and $r\equiv1\pmod3$.

In particular,


$$
S_5(3)=1,\qquad \binom55=1.
$$


Return order $3$ is an actual uneliminated column. Hence


$$
v_2(W_{5,3}(5))=7,
$$


and its direct bottom-correction summand in the actual residual pencil has exact valuation


$$
\boxed{
v_2\!\left(2^{L_d}\gamma_kW_{5,3}(5)\right)=L_d+7.
}
\tag{9.6}
$$



This is the first nonzero direct weighted-return correction layer after the paid five-column projector. It is not the valuation of the whole entry
$(\mathcal P_k^{[5]})_{0,z^{(3)}}$: cancellation with the complete product part is not excluded.

### 9.3 Higher layers and finite boundaries

There is also an exact finite expression retaining every higher return jet. Put


$$
h_{i,t}=
\mu_{5,k}\binom it
-\sum_{\ell=0}^4M_{5,k}(i,\ell)\binom\ell t.
$$


Then


$$
\boxed{
W_{5,r}(i)=
\frac12\sum_{t=0}^{i}
h_{i,t}\,2^t(r+1)_t\,\eta_{r+t}^{(d)}.
}
\tag{9.7}
$$


All factorial ratios $(r+1)_t$, including their odd parts, remain.

The largest source index in (9.7) is


$$
d+r+t\le d+(d-1)+(d+1)=3d.
$$


It is a return index, whose successor moment is $3d+1=3k-2$. Thus the last factorial remains $(6k-4)!$, and the physical last row is still $2d+1$.

The atom and both border corrections in (9.2) retain their respective additional powers $2^{M_d}$ and $2^{\alpha_d}$. Their direct contributions cannot precede the layer in (9.6), but they remain in the exact pencil and in the complete interpolation coefficients at every depth.

---

## 10. What is now proved, and the exact remaining bottleneck

The old growing source-unit hypothesis has not merely been left unchecked: it is false at the old budget $b_q$ for every $q\ge18$.

The repaired route has two concrete ingredients:

1. the source normalization $B_q(d)$, with explicit entries (5.5) and the atom-cofactor criterion of Section 5.3;
2. the complete mixed-compound comparison (8.3), valid throughout a linear-rank interval.

The remaining source obligation is to construct an attaining nested **physical** source flag at the repaired budget, or to quantify its excess valuation sufficiently sharply. The explicit contact-jet flags in Section 4 do not by themselves solve that optimal physical-minor problem: their jet orders need not be the minimizing consecutive orders.

After that, the final stages must still:

- retain the mixed terms when the inequalities (8.2) no longer certify their disappearance;
- use bottom corrections to supply the missing $(d+1)$-st common direction;
- propagate both complete coefficient borders through the same paid elimination;
- control the joint terminal coefficient depth rather than assuming a border unit.

The actual numerical target remains


$$
\boxed{
\nu_k^{[5]}
\le \frac{15}{4}k^2-64+O(k\log k).
}
\tag{10.1}
$$


No theorem above implies this upper bound.

All coefficient transfers remain unchanged. In particular,


$$
\boxed{
\frac{|P_{1,k}^{[5]}|}{g_k^{[5]}}
=\frac{|H_{1,k}|}{G_k}=q_k,
}
$$


and


$$
\boxed{
\frac{|P_{0,k}^{[5]}+P_{1,k}^{[5]}(e+\pi)|}{g_k^{[5]}}
=\frac{|H_k(e+\pi)|}{G_k}
=\ell_k>0.
}
\tag{10.2}
$$


An evaluated correction summand is not substituted for this nonzero whole error.

---

## 11. Independent odd-prime obligations and the global objective

The established ternary contents are retained only at their proved scope:


$$
v_3(\mathscr L_k)=v_3(\mathscr R_k)=E_k,
\qquad
E_k=\frac{(k-2)(k-1-2s)}2
\quad(k=3^s),
$$


and hence


$$
E_k\le v_3(G_k)\le2E_k+s+1.
$$


No equality for $v_3(G_k)$ is inferred.

The other odd-prime descents remain separate open obligations:


$$
v_p(\mathscr L_k),v_p(\mathscr R_k)\le B_p(k)
\quad(5\le p\le6k-5),
$$


where


$$
B_p(k)=
k\bigl(2\mathbf1_{p=3}+v_p(\Lambda_k)\bigr)
+4\sum_{j<k}v_p(j!),
$$


and


$$
v_p(\mathscr L_k)=v_p(\mathscr R_k)=0
\quad(p>6k-5).
$$



The closed same-$H$ analytic estimate is reused, not recalculated:


$$
\log|H_k(e+\pi)|
\ge
4k^2\log k+
\left(15\log2-\frac92\log3+\frac4{85}\right)k^2
+o(k^2).
$$


Together with the independent odd descents, a final binary bound with coefficient $19/4$ would give the already certified positive primitive-error divergence margin


$$
\frac{57}{4}\log2-\frac72\log3-\frac{506}{85}>0.
$$



That would retire this producer as a source of primitive whole-error decay. It would not prove $e+\pi$ rational, and it would not by itself prove $e+\pi$ irrational.

---

## 12. Bounded exact arithmetic for independent inspection

No tools have been used. No original-length determinant calculation, adjacent scan, Smith scan, or closed analytic computation is proposed.

No computation is indispensable to the proofs above. The following bounded checks would independently authenticate arithmetic details.

### Check A: finite root-filter comparison

**Inputs**


$$
d=80,\qquad 0\le r,j\le47.
$$


Compare:

1. the direct finite sum (3.2), with $0\le t\le80$;
2. the trace formula (3.4), including the derivative term;
3. the two-carry evaluation of its coefficients.

All binomial upper arguments are at most $174$.

**Expected output:** zero discrepancies over the $48^2$ pairs.

This is an auxiliary finite check, not an original-domain theorem.

### Check B: original-index digit authentication

**Inputs**


$$
d=9^{18}-1,
$$




$$
r\in\{0,1,4,5,16,17,31,32\},
$$




$$
j\in\{0,1,2,3,4,15,16,17,31,32\}.
$$


Compare the two-carry coefficient rule with direct arithmetic in


$$
\mathbb F_4[z]/(z^{65}),
$$


using repeated squaring for the exponents in (3.4). Then multiply by
$\binom{r+j}{j}\bmod2$ and compare with (4.3).

**Expected outputs:**

- zero discrepancies in all $80$ root-filter comparisons;
- zero discrepancies in all $80$ normalized source-entry comparisons;
- every tested row $j=16,17,31$ is zero in the matrix $\mathcal J$.

Only degrees at most $64$ are built. No original-length source array is needed.

### Check C: first correction layer

**Inputs**


$$
p=5,\qquad 0\le r<24.
$$


Compare the finite sum (7.5) with (9.5).

**Expected output:** zeros exactly at


$$
\boxed{\{2,4,7,8,11,13,17,22\}\pmod{24}.}
$$


In particular $S_5(3)=1$.

The uniform period and formula follow from the proof, not from this finite check.

The coordinator may author any implementation. These checks would establish only their stated finite arithmetic scope; none would establish (10.1).

---

## 13. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Parent all-order trace/filter law, including derivative term | **Independently proved** |
| Two-carry entry algorithm | **Proved**, linear in input bit length |
| $O(\log d)$ computation of a growing determinant | **Rejected** |
| Closed bitwise law (4.3) for normalized contact jets | **New proved evaluation** |
| Exact binary rank $C_d(q)$ | **New proved growing-rank theorem** |
| Explicit contact-jet unit flags at original indices | **New proved statement** |
| Old atom-source budget $b_q$ attainable for growing $q$ | **Disproved for every $q\ge18$** |
| Stronger source payment $B_q(d)$ | **New proved integer-divisibility theorem** |
| Optimal growing physical source flag at $B_q(d)$ | **Open** |
| Complete mixed-compound window through $q\le d/8$ | **New proved theorem** |
| Direct weighted-return correction layer $L_d+7$ in actual $\mathcal P_k^{[5]}$ | **New evaluated theorem** |
| Missing common direction supplied and terminal pair bounded | **Open** |
| Actual all-prime transfers, primitive denominator, and whole error | **Preserved exactly** |
| Required upper bound for $\nu_k^{[5]}$ | **Open** |
| Other odd-prime descents and large-prime exclusion | **Independent open obligations** |
| Primitive whole-error divergence | **Conditional** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

### Final conclusion

The new unconditional arithmetic advance is not another fixed common-column pivot. It is a structural evaluation of the all-order normalized contact ranks, a proof that the former growing source-unit hypothesis cannot hold at its old payment, and a mixed-compound argument that extends complete corrected-minor control from an entrywise $O(\sqrt d)$-rank window to a proved linear-rank window.

The complete weighted-return corrections are also evaluated at their first direct nonzero layer after the existing five-column elimination:


$$
\boxed{
2^{-7}W_{5,r}(i)\equiv\binom i5S_5(r)\pmod2,
}
$$


with $S_5(r)$ explicitly given and the actual remaining column $r=3$ attaining depth $L_d+7$.

The exact remaining bottleneck is now the repaired growing physical source-unit problem, followed by the genuinely mixed final common-column elimination and the joint depth of the two complete terminal coefficient borders. The final all-prime gcd and the primitive whole error remain the original ones at the same infinite original indices. No unconditional conclusion about the rationality of $e+\pi$ has been obtained.
