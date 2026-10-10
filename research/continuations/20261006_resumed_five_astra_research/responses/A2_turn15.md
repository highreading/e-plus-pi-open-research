> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 15 — Exact factorial filtration, the first exceptional mixed channel, and a bounded actual-head interface

## Executive assessment

The all-row force identification remains closed. I do not introduce another version of $\mathbf{EF}_6$, repeat the accepted $\Xi=17$ computation, or reinterpret the accepted $29^3$-mixed zero as a primitive alignment theorem.

This turn obtains four further results.

1. **The exterior inverse preserves the exact factorial valuation, not only the weaker staircase filtration.** In particular,
   

$$
v_{29}(v_h)\ge v_{29}\!\left(\frac{(b+h)!}{b!}\right).
$$


   On the stated original family, the complete exterior solve modulo $29^6$ therefore needs only $0\le h\le117$, or **118 coordinates**. This also resolves an indexing issue: the previous interval $0\le h\le146$ has 147 coordinates, not 146.

2. **The four actual first-head scalars are not independent.** With
   

$$
m=n/29,\qquad q=\lfloor m/29\rfloor,
$$


   they satisfy
   

$$
\boxed{
   (A_m,B_m,C_m,D_m)
   \equiv(2,14,8,24)\,A_q\pmod{29}.
   }
$$


   This is an identity for the actual original head, valid for every compatible continuation. The remaining scalar is an actual high-index coefficient, not a free parameter.

3. **The eight-interface Gram matrix at the new quadratic correction has rank at most one modulo $29$.** Its only possible contribution comes from the exceptional residue
   

$$
J\equiv14\pmod{29}.
$$


   This gives an explicit reduction of the first-order-correction product in the unknown $29^3$-mixed coefficient. It does **not** annihilate the other new lifted terms.

4. **There is a bounded prime-power interface for all actual first-head digits sufficient for this fixed mixed layer.** A direct Cartier construction uses at most 371 polynomial coordinates at modulus $29^7$, with smaller modules at the lower precisions actually needed by later head entries. It preserves the original exponent dependence. It does not require a matrix solve of original size $b$.

The first unknown coefficient


$$
\boxed{
\kappa(u):=\frac{F^TQ}{29^3}\pmod{29},
\qquad u\equiv2\pmod{29^9},
}
$$


is **not numerically evaluated here**. Nor is its vanishing proved for every compatible continuation. The new rank-one relation identifies one previously uncontrolled contribution, but a complete lifted contraction still remains.

There is also a necessary restriction on any proposed result: $\kappa$ cannot be nonzero throughout a nonempty full original arithmetic cylinder. The accepted unbounded-content theorem forces zeros of $\kappa$ in every such cylinder. A nonzero value at an actual index would nevertheless obstruct the true alignment at that index, under the local integrality hypothesis on $\rho_n$ used in the preceding reports.

---

## 1. Preserved objects and proof scope

Throughout,


$$
p=29,\qquad D=p^3,
$$




$$
b=3^{249005515+574312172u}
  =410910916+p^6C,\qquad n=2001b,\qquad u\ge0.
$$



The original domains remain:

- contact coordinates $0\le j<b$;
- recurrence source rows $1\le i\le b-2$;
- reconstructed coordinates $0\le j\le b$.

The actual corrected columns are


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,
\qquad
W_j=\binom{n+2}{j},
$$


where


$$
(\mathcal Rx)_j=W_j(jx_{j-1}-x_j),\qquad x_{-1}=x_b=0.
$$


Thus


$$
(\mathcal Rx)_b=bW_bx_{b-1}.
$$



Retain


$$
Z_w=p^{c+2}x,\qquad x\ \text{primitive at }p,
$$




$$
\nu=v_p(x^Tx),\qquad d=2c+4+\nu,
$$


and


$$
F=Z_w/p^4,\qquad G=Y/p^4,\qquad Q=pG.
$$



The results reused at their stated scope are


$$
u\equiv2\pmod{p^3}
\Longrightarrow Z_w,Y\in p^4\mathbb Z_p^{b+1},
$$


and


$$
u\equiv2\pmod{p^9}
\Longrightarrow d\ge10,\qquad F^TQ\in p^3\mathbb Z_p.
$$



The recovered all-row source, its positive recurrence forcing, its homogeneous logarithmic part, and the finite $\mathsf P_-$ boundary conversion remain closed. The accepted finite value $\Xi=17$, including its complete path support, is reused without recalculation.

---

# Part I. Convergence and precision audit

## 2. A suitable space for the infinite operator identities

For a fixed original $b,n$, use


$$
c_0(\mathbb Z_p)=
\{a=(a_j)_{j\ge0}:a_j\to0\text{ \(p\)-adically}\}
$$


with the supremum norm.

This is important: integrality of matrix entries alone does not make an arbitrary infinite matrix product legitimate.

The upper-triangular matrices $T_n,R_n$ act continuously on this space.

- $T_n$ has finite bandwidth.
- For $R_n$, the $i$-th output is a convergent series because the input tends to zero and all coefficients are integral.
- Its output tends to zero because the $i$-th row uses only input indices $j\ge i$.

For


$$
(D_-)_{ij}=c_{i-j}(n)\binom ij,
\qquad
c_s(n)=s![z^s]\phi(z)^{-n},
$$


and the analogous $D_+$, the symbol coefficients tend to zero $p$-adically. Both lower operators are norm limits of finite-band operators. They are therefore continuous on $c_0$.

The inverse identities


$$
T_n^{-1}=R_n,\qquad D_+^{-1}=D_-
$$


hold there by finite-band approximation and the corresponding formal coefficient identities. Consequently


$$
\mathcal C_\infty=R_nD_-R_n
$$


is the inverse of


$$
B_{\rm ext}=T_nD_+T_n
$$


on this space.

This does **not** assert that the full $\mathsf P_-$ operator preserves $c_0$. It need not: its action on a finitely supported vector can have a nondecaying tail. The transfer from $B_{\rm ext}$ to the finite $A$ still uses only the already-audited finite lower-triangular identity


$$
(B_{\rm ext})_{II}=(\mathsf P_-)_{II}A_{II},
\qquad
(B_{\rm ext})_{IE}=(\mathsf P_-)_{II}A_{IE}.
$$



No additional infinite $\mathsf P_-$ inversion is required.

### Exterior Neumann convergence

On exterior indices,


$$
(\mathcal C_\infty)_{EE}=R_{2n}+E,
\qquad \|E\|\le p^{-1}.
$$


The upper-triangular exterior $R_{2n}$ block has inverse $T_{2n}$, of norm at most one. Hence


$$
(\mathcal C_\infty)_{EE}^{-1}
=
\sum_{r\ge0}(-T_{2n}E)^rT_{2n}
$$


converges in operator norm.

Thus the earlier exterior inverse argument has a valid convergence setting. Its use does not require an unproved convergence claim for arbitrary integral sequences.

---

## 3. Correct norm-relative budgets

Write


$$
z=v_p(Z_w)=c+2,\qquad \tau=v_p(Y)\ge4
$$


on the reviewed cylinder. Suppose


$$
\widehat Z-Z_w\in p^a\mathbb Z_p^{b+1},\qquad
\widehat Y-Y\in p^k\mathbb Z_p^{b+1},
$$


with $a\ge z$, $k\ge\tau$.

Then


$$
v_p(\widehat Z^T\widehat Y-Z_w^TY)
\ge \min(a+\tau,\ k+z),
\tag{3.1}
$$


and


$$
v_p(\widehat Z^T\widehat Z-Z_w^TZ_w)\ge a+z.
\tag{3.2}
$$



Therefore a sufficient budget for the mixed contraction modulo $p^{d+2}$ is


$$
\boxed{
a\ge d+2-\tau,\qquad k\ge d-c.
}
\tag{3.3}
$$



Using the proved $\tau\ge4$, this improves the previous conservative first-column mixed budget:


$$
\boxed{
K_Z^{\rm mixed}\ge d-2,\qquad K_Y^{\rm mixed}\ge d-c.
}
\tag{3.4}
$$



The earlier $d-1$ budget remains sufficient, but is no longer sharp after actual $Y$-saturation has been established.

To determine the norm through modulus $p^{d+1}$, a sufficient first-column budget remains


$$
\boxed{K_Z^{\rm norm}\ge d-c-1.}
\tag{3.5}
$$



For the term $p\rho_nZ_w^TZ_w$, write $r_\rho=v_p(\rho_n)$. Its error is paid modulo $p^{d+2}$ if


$$
a\ge d-c-1-r_\rho.
\tag{3.6}
$$


The standard budget in the sources uses $r_\rho\ge0$. The excerpts do not supply an independent formula from which to reevaluate $\rho_n$; when that hypothesis matters below, I state it explicitly.

None of these formulas turns $d\ge10$ into an actual final precision input.

### Fixed precision for the first unknown coefficient

To determine


$$
F^TQ\pmod{p^4},
$$


it is enough to know **both** $Z_w$ and $Y$ modulo $p^7$, because


$$
F^TQ=\frac{Z_w^TY}{p^7},
$$


and each other column is divisible by $p^4$. Thus an error in either column of order $p^7$ changes the numerator only by $p^{11}$.

This fixed calculation is distinct from evaluating the true-depth alignment.

---

# Part II. A stronger exact exterior filtration

## 4. Exact factorial weights

Define


$$
q_b(j)=v_p(j!)-v_p(b!),\qquad j\ge0.
$$


For exterior indices $j=b+h$, this is


$$
q_b(b+h)=v_p(z_h),\qquad
z_h=\frac{(b+h)!}{b!}.
$$



Consider the closed weighted space


$$
\mathscr X_b=
\{a\in c_0(\mathbb Q_p):
v_p(a_j)\ge q_b(j)\text{ for every }j\}.
$$


Only finitely many of its weights are negative.

### Lemma 4.1 — Exact factorial-filtration preservation

The operators $T_n,R_n,D_+,D_-$, and hence $\mathcal C_\infty$, preserve $\mathscr X_b$.

#### Proof

For an upper-triangular integral operator, an output at $i$ uses only indices $j\ge i$. Since $q_b$ is nondecreasing,


$$
v_p(a_j)\ge q_b(j)\ge q_b(i).
$$



For the lower operator $D_-$, put $s=i-j$. Its entry is


$$
c_s(n)\binom is
=
[z^s]\phi(z)^{-n}\frac{i!}{j!}.
$$


The coefficient of $\phi(z)^{-n}$ is $p$-integral. Therefore


$$
v_p((D_-)_{ij})\ge v_p(i!)-v_p(j!)
=q_b(i)-q_b(j).
$$


Every term in $(D_-a)_i$ has valuation at least $q_b(i)$.

The same argument applies to $D_+$, since $[z^s]\phi(z)^n$ is $p$-integral. Convergence follows from §2. ∎

Extend an exterior sequence by zero on $I$. Projection back to $E$ shows that $(\mathcal C_\infty)_{EE}$ preserves the exact exterior factorial lattice. So do $R_{2n}$, $T_{2n}$, and their difference $E$. The convergent Neumann inverse therefore preserves it as well.

### Theorem 4.2 — Exact factorial decay of the actual exterior solution

For the actual solution


$$
(\mathcal C_\infty)_{EE}v=z,
$$


one has


$$
\boxed{
v_p(v_h)\ge
v_p\!\left(\frac{(b+h)!}{b!}\right)
\qquad(h\ge0).
}
\tag{4.1}
$$



This strengthens Turn 14’s staircase bound. It also explains why finite exterior returns cannot erase the additional valuation at $b+2$.

---

## 5. The resulting finite sizes

At precision $p^K$, define


$$
r_b(K)=
\max\left\{h\ge0:
v_p\!\left(\frac{(b+h)!}{b!}\right)<K
\right\}.
\tag{5.1}
$$


Then the exact exterior solution is obtained modulo $p^K$ by solving only through $h=r_b(K)$. Omitted entries already belong to $p^K$, so their contribution to retained equations is paid.

The previous symbol cutoff


$$
s\le p(K-1)
\tag{5.2}
$$


remains valid.

For the actual original low residues,


$$
b\equiv-2\pmod{p^2},
\qquad
b+2\equiv6p^2\pmod{p^3}.
$$


Thus $v_p(b+2)=2$. For $0\le h<843$,


$$
v_p(z_h)
=
\left\lfloor\frac{h+27}{29}\right\rfloor
+\mathbf1_{h\ge2}.
\tag{5.3}
$$



In particular,


$$
\boxed{r_b(6)=117,\qquad r_b(7)=146.}
\tag{5.4}
$$



Therefore:

| Precision | Exterior indices | Number of coordinates |
|---|---:|---:|
| $p^6$ | $0,\ldots,117$ | $118$ |
| $p^7$ | $0,\ldots,146$ | $147$ |

These are symbolic consequences of the displayed residues, not a rerun of a finite solve.

The reconstructed support bound from Turn 14 remains a valid safe bound:


$$
0\le a\le p(K-1),\qquad
0\le v\le p(K-1)+2.
$$


The new result shrinks the exterior linear system; it does not silently shrink every reconstructed atom range.

At true depth $K=d-c$, the logarithmic contribution is still retained whenever its guard fails. In particular, the complete approximation remains


$$
Y^{[K]}
=
\mathcal R\theta^{(e,[K])}
+W_be_b
+\mathcal RA^{-1}r^{(F,[K])}.
$$


Neither the $b\times b$ contact boundary nor the physical terminal has changed.

---

# Part III. The actual four-head dependence

## 6. Reduction to one actual scalar modulo $29$

Put


$$
\mathscr P(z)=1+2z+2z^2,\qquad
R(z)=z^{-1}\mathscr P(z)=z^{-1}+2+2z.
$$


Define


$$
A_r=\operatorname{CT}_z R(z)^r,
\qquad
D_r=\operatorname{CT}_z zR(z)^r.
$$



The four scalars from Turn 13 are exactly


$$
A_m,\qquad B_m=A_{m-1},\qquad C_m=D_{m-1},\qquad D_m.
$$



On the original family,


$$
m=n/p\equiv7\pmod p.
$$


Write


$$
m=7+pq.
$$



By Frobenius,


$$
R(z)^m\equiv R(z)^7R(z^p)^q\pmod p.
$$


The support of $R^7$ is $[-7,7]$. In taking a constant term, the only exponent in this interval divisible by $p$ is zero. The same is true after multiplication by $z$. Hence


$$
A_m\equiv A_7A_q,\qquad D_m\equiv D_7A_q\pmod p.
$$


Similarly,


$$
B_m\equiv A_6A_q,\qquad C_m\equiv D_6A_q\pmod p.
\tag{6.1}
$$



For completeness, the small exact values follow from


$$
rA_r=(4r-2)A_{r-1}+4(r-1)A_{r-2},
$$


and


$$
D_r=\frac{A_{r+1}-2A_r}{4}.
$$


They give


$$
A_6=2624,\quad A_7=11776,\quad
D_6=1632,\quad D_7=7448.
$$


Reduction modulo $29$ yields


$$
\boxed{
(A_m,B_m,C_m,D_m)
\equiv(2,14,8,24)A_q\pmod{29}.
}
\tag{6.2}
$$



These are actual coefficient identities. No arbitrary assignment of the four scalars is admissible.

### Consequence for the leading first column

The accepted four-profile reduction therefore becomes


$$
\boxed{
F\bmod p=A_q\,\mathcal F_{\rm lead},
}
\tag{6.3}
$$


where $\mathcal F_{\rm lead}$ is the fixed complete leading profile obtained from the corresponding linear combination of the four retained profiles. It includes the finite returns used in that reduction.

In particular,


$$
A_q=0\pmod p\quad\Longrightarrow\quad c\ge3.
\tag{6.4}
$$



The converse requires a nonzero evaluation of the complete profile; it is not asserted.

### Actual continuation dependence

The scalar $A_q$ is not determined merely by the displayed low residue of $u$. Iterating the same support argument gives the classical constant-term Lucas product


$$
A_q\equiv\prod_{\text{base-}29\text{ digits }q_i}A_{q_i}\pmod{29}.
\tag{6.5}
$$


Thus it depends on the actual complete digit string of the original coefficient index $q$. Formula (6.5) is useful structure, but it is not a feasible full-digit evaluation at the enormous original index without further information about that digit string.

This is precisely why replacing the actual head by free low coefficients would be invalid.

---

# Part IV. The first new mixed layer

## 7. What must be evaluated

On $u\equiv2\pmod{p^9}$, put


$$
\kappa(u)=\frac{F^TQ}{p^3}\pmod p
=\frac{F^TG}{p^2}\pmod p.
\tag{7.1}
$$



Writing canonical coordinatewise digits


$$
F=F_0+pF_1+p^2F_2\pmod{p^3},
\qquad
G=G_0+pG_1+p^2G_2\pmod{p^3},
$$


the required whole numerator is


$$
\begin{aligned}
\kappa(u)=\frac1{p^2}\bigl[
&F_0^TG_0
+p(F_0^TG_1+F_1^TG_0)\\
&+p^2(F_0^TG_2+F_1^TG_1+F_2^TG_0)
\bigr]\pmod p.
\end{aligned}
\tag{7.2}
$$



The division belongs to the **whole sum**. The accepted $p^2\,17\,\mathscr L_{FG}\mathcal H(t)$ reduction proves that this whole numerator is divisible by $p^2$; it does not evaluate (7.2).

In particular, the following are genuinely new:

- the next lift of the leading contraction;
- the paid lift of the first-order cross terms;
- the product $F_1^TG_1$;
- the leading contractions involving $F_2,G_2$.

The ordinary $\mathcal H(t)$-zero is not a proof that these all vanish.

---

## 8. A rank-one relation for the new interface Gram matrix

Retain the exact upper kernels


$$
K_s(J)=H_s(J)/p^3,\qquad s=(w,k,c)\in\{0,1\}^3,
$$


with $K=K_{000}$.

The exact ratio identities from the source are


$$
\frac{H_{w0c}(J)}{U(J)}
=(W-J)^w(A+B-J+1)^c,
\tag{8.1}
$$


and


$$
\frac{H_{w1c}(J)}{U(J)}
=(W-J)^w(B-J)(A+B-J)^{c-1}.
\tag{8.2}
$$



Here


$$
W\equiv7,\qquad B\equiv28,\qquad A+B\equiv14\pmod p.
$$



### Off the exceptional residue

If $J\not\equiv14\pmod p$, all ratios in (8.1)–(8.2) are integral units or integral factors whose reductions depend only on $J_0$. Consequently


$$
K_s(J)\equiv r_s(J_0)K(J)\pmod p.
$$


The accepted weighted radical


$$
\sum_JR(J_0)K(J)^2=0\pmod p
$$


therefore eliminates every pairwise Gram contribution off $J_0=14$.

### On the exceptional residue

The leading support of $K\bmod p$ excludes $J_0=14$. Thus $K(J)=0\pmod p$ there.

Every $K_s$ is still zero there modulo $p$, except possibly the two kernels having


$$
k=1,\qquad c=0.
$$


Moreover,


$$
K_{110}(J)=(W-J)K_{010}(J)
\equiv22K_{010}(J)\pmod p
$$


on that residue.

Define the actual finite scalar


$$
\mathcal E_{\rm exc}
=
\sum_{\substack{0\le J\le B\\J\equiv14\;(\mathrm{mod}\ p)}}
K_{010}(J)^2\pmod p,
\tag{8.3}
$$


and


$$
\eta_{010}=1,\qquad \eta_{110}=22,\qquad
\eta_s=0\quad\text{otherwise}.
$$



### Theorem 8.1 — Rank-one exceptional Gram relation

For every compatible continuation,


$$
\boxed{
\sum_{J=0}^{B}K_s(J)K_t(J)
=
\eta_s\eta_t\,\mathcal E_{\rm exc}\pmod p.
}
\tag{8.4}
$$



#### Boundary check

The original interior ranges remain


$$
J\le B\quad(\ell<5044),\qquad
J\le B-1\quad(\ell\ge5044).
$$


At $J=B$, one has $B_0=28\ne14$, the relevant ratio denominator is a unit, and $K(B)\in p\mathbb Z_p$. Hence every endpoint product in (8.4) is zero modulo $p$.

Thus (8.4) is valid for both original cutoff branches. It has not been obtained by replacing the physical terminal by a continued contact value. ∎

---

## 9. Application to the actual first-order correction product

Use the complete coefficients in Turn 14:


$$
B_\ell(J)=Jb_\ell K(J)+\sum_s c_{\ell,s}K_s(J),
$$




$$
E_\ell(J)=Jd_\ell K(J)+\sum_s e_{\ell,s}K_s(J).
$$


The coefficients are the actual ones, including the solved finite returns.

The weighted radical removes the terms involving $JK$, while (8.4) gives


$$
\boxed{
\sum_{\ell,J}B_\ell(J)E_\ell(J)
=
\mathcal E_{\rm exc}
\sum_{\ell=0}^{D-1}
(c_{\ell,010}+22c_{\ell,110})
(e_{\ell,010}+22e_{\ell,110})
\pmod p.
}
\tag{9.1}
$$



This is a genuine all-continuation relation for one new contribution to $\kappa$. It replaces a potentially full eight-by-eight Gram calculation by a single exceptional channel.

It does **not** evaluate either factor in (9.1), and it does not remove the remaining terms of (7.2).

The precise obstruction to extending the old radical is now explicit: the ratio $H_{010}/U$ contains


$$
(A+B-J)^{-1},
$$


which ceases to be a unit exactly at $J_0=14$. That is the new support on which the previous $K$-radical has no authority.

---

# Part V. A bounded paid interface for the actual first head

## 10. Exact generating function

The actual first force is


$$
f_i^0=\frac{(n+i)!}{n!}J_i(n),
\qquad
J_i(n)=\operatorname{CT}_z R(z)^n(1+z)^i.
\tag{10.1}
$$


Hence


$$
J_i(n)
=[t^nz^0]\frac{(1+z)^i}{Q(t,z)},
\qquad
Q(t,z)=1-tR(z).
\tag{10.2}
$$



This is a rational generating function in $t$, with Laurent-polynomial coefficients in $z$. The established rational/diagonal prime-power machinery applies. The following construction gives explicit target-specific support bounds rather than importing an unspecified feasible automaton.

At precision $p^7$,


$$
f_i^0=0\pmod{p^7}\qquad(i\ge203).
$$


For $0\le i\le202$, the actual low residue $n\equiv203\pmod{841}$ gives


$$
v_p\!\left(\frac{(n+i)!}{n!}\right)=\lfloor i/29\rfloor.
\tag{10.3}
$$


Thus $J_i(n)$ is needed only modulo


$$
p^{r_i},\qquad r_i=7-\lfloor i/29\rfloor.
\tag{10.4}
$$



This specifies necessary head digits without constructing original-length factorials.

---

## 11. An explicit prime-power Cartier module

For $1\le r\le7$, use states of the form


$$
S(t,z)=
\sum_{h=1}^{r}
p^{h-1}\frac{P_h(t,z)}{Q(t,z)^h}
\pmod{p^r},
\tag{11.1}
$$


with


$$
\deg_tP_h\le h,\qquad
\operatorname{supp}_zP_h\subset[-h,h].
\tag{11.2}
$$



Define


$$
V(t,z)=\frac{Q(t,z)^p-Q(t^p,z^p)}p.
$$


This is an integral Laurent polynomial.

For a digit $d\in\{0,\ldots,p-1\}$, let


$$
\Lambda_{d,0}\!\left(\sum a_{a,b}t^az^b\right)
=
\sum a_{pa+d,pb}t^az^b.
$$



Since $h\le7<p$,


$$
\frac1{Q^h}
=
\frac{Q^{p-h}}{Q(t^p,z^p)+pV}.
$$


Expanding only through paid precision gives


$$
\begin{aligned}
\Lambda_{d,0}
\left(p^{h-1}\frac{P_h}{Q^h}\right)
\equiv
\sum_{k=0}^{r-h}
(-1)^kp^{h-1+k}
\frac{
\Lambda_{d,0}(P_hQ^{p-h}V^k)
}{Q^{k+1}}
\pmod{p^r}.
\end{aligned}
\tag{11.3}
$$



The numerator before Cartier has $t$-degree at most $p(k+1)$ and $z$-support inside $[-p(k+1),p(k+1)]$. Thus the output satisfies (11.2) for denominator $Q^{k+1}$. Its coefficient is divisible by the required $p^k$.

This proves closure.

### Dimension

The number of polynomial coordinates is


$$
N_r=\sum_{h=1}^{r}(h+1)(2h+1).
$$


Explicitly,


$$
\boxed{
(N_1,\ldots,N_7)=(6,21,49,94,160,251,371).
}
\tag{11.4}
$$



The initial numerator $(1+z)^i$ can exceed the support in (11.2). For $i\le202$, two initial Cartier steps suffice: the excess $z$-support is divided by $29$ at each step. The resulting state is in the displayed bounded module.

After the actual base-$29$ digits of $n$ have been read, the accepting functional is


$$
S\longmapsto
\sum_{h=1}^{r}p^{h-1}[z^0]P_h(0,z)\pmod{p^r}.
\tag{11.5}
$$



This construction uses only unit-free polynomial arithmetic and exact powers of $p$. It introduces no division by a possibly nonunit factorial.

---

## 12. What the bounded interface can and cannot evaluate

The module provides two legitimate outputs:

1. an actual coefficient value after a complete actual digit word has been supplied; or
2. after a fixed original prefix, a row functional on the unread suffix.

For the present huge original powers, the second is the feasible bounded output. A finite-state representation does not make a digit-by-digit traversal of an astronomically long original integer feasible.

The original exponent dependence is exact. With


$$
574312172=28p^5,
$$


the retained principal-unit parametrization gives


$$
b\bmod p^L
\quad\text{from}\quad
u\bmod p^{\max(L-6,0)}.
$$


Since $v_p(2001)=1$,


$$
n\bmod p^L
\quad\text{depends on}\quad
u\bmod p^{\max(L-7,0)}.
\tag{12.1}
$$



But an accepting state on the unread suffix is not determined by that low residue alone. This distinction is necessary when formulating an all-continuation claim.

### Resource bounds for a new head-interface certificate

No accepted scalar or original-prefix producer needs to be rerun.

A new bounded calculation can take:

- the already-recorded original low residue of $b$;
- $Q,V$ from §11;
- the head indices $0\le i\le202$;
- the per-entry precisions $r_i$ from (10.4).

It should construct the digit operators and return the actual prefix row functionals, not arbitrary head values.

Useful explicit bounds are:

- largest state dimension: $371$;
- total head-row coordinates after the two initialization digits:
  

$$
29\sum_{r=1}^{7}N_r=27\,608;
$$


- storing all 29 dense digit matrices separately at each precision requires at most
  

$$
29\sum_{r=1}^{7}N_r^2
  =6\,900\,724
$$


  modular entries;
- the largest raw polynomial box needed in (11.3) has
  

$$
0\le\deg_t\le203,\qquad -203\le\deg_z\le203,
$$


  hence at most $83\,028$ slots.

Polynomial products can use exact multimodular convolution with a CRT product exceeding the elementary coefficient bound. Dense transition storage is about 56 MB using eight-byte entries; working storage can be kept bounded independently of $b$.

The expected verifiable output is:

- the transition arrays;
- polynomial identities verifying (11.3);
- the actual head prefix rows at their paid precisions;
- the terminal functional (11.5);
- the exact original residue dependence (12.1).

This would be a **new head-interface certificate**, not a computation of $\kappa$. To turn it into the latter, the complete lifted mixed observation must still be connected to these actual rows.

---

# Part VI. Growing content and true-depth obstruction

## 13. A restriction on any proposed nonzero cylinder

Because


$$
F=p^{c-2}x,\qquad Q=pG,
$$


we have


$$
F^TQ=p^{c-1}x^TG.
\tag{13.1}
$$


Therefore


$$
\boxed{c\ge5\Longrightarrow\kappa(u)=0.}
\tag{13.2}
$$



Reuse the accepted theorem that $c$ is unbounded in every original arithmetic progression. Every nonempty original arithmetic progression contained in $u\equiv2\pmod{p^9}$ therefore contains indices with $c\ge5$.

Consequently:

### Proposition 13.1

The first unknown physical coefficient $\kappa$ cannot be nonzero on every original index of a nonempty full arithmetic cylinder.

This is not a finite computation and does not depend on an auxiliary digit word. It is an infinite original-domain consequence of actual column content.

Along an increasing original sequence with $c\to\infty$, every fixed physical mixed coefficient eventually vanishes. That fact is stronger than exterior omission alone, but it still does **not** control the primitive mixed value: division by the growing content removes precisely this automatic gain.

---

## 14. What an actual nonzero $\kappa$ would prove

Suppose an actual original index on the reviewed cylinder satisfies


$$
\kappa(u)\ne0.
$$


Then


$$
v_p(Z_w^TY)=10.
\tag{14.1}
$$


In particular $c\le4$, by $v_p(Z_w^TY)\ge c+6$.

If $v_p(\rho_n)\ge0$, then


$$
v_p(p\rho_nZ_w^TZ_w)\ge d+1\ge11.
$$


Hence


$$
\boxed{
v_p(Z_w^TY-p\rho_nZ_w^TZ_w)=10<d+2.
}
\tag{14.2}
$$


Thus the true alignment fails at that actual index.

No exact value of $d$ is required for this deduction once the actual fixed-layer nonzero value has been established. However, this is an obstruction at the evaluated index or at a proved restricted set of evaluated indices—not an exclusion of the entire original family.

Without the integrality hypothesis on $\rho_n$, the exact condition is


$$
d+1+v_p(\rho_n)>10.
$$



---

## 15. The primitive bottleneck in exact form

Write


$$
x^Tx=p^\nu\eta,\qquad \eta\in\mathbb Z_p^\times,
$$


and put


$$
K=d-c=c+4+\nu.
$$


The true target is


$$
\boxed{
x^TY\equiv p^{K-1}\rho_n\eta\pmod{p^K}.
}
\tag{15.1}
$$



Thus it has two different requirements:

1. the primitive mixed contraction must reach valuation at least $K-1$;
2. its last required digit must match the independently defined $\rho_n\eta$.

The automatic fixed-layer zeros supplied by $c\to\infty$ prove neither requirement.

The exact factorial theorem permits replacing $Y$ by the complete $Y^{[K]}$, with logarithmic retention whenever needed:


$$
x^TY^{[K]}\equiv p^{K-1}\rho_n\eta\pmod{p^K}.
\tag{15.2}
$$


This is a smaller, paid expression, but it remains an unevaluated primitive contraction.

---

# Part VII. Remaining finite task and global arithmetic

## 16. The next complete mixed certificate

The outstanding fixed-layer task is now more specific than “calculate another tail.”

It is to evaluate (7.2), using:

1. the actual first-head prefix rows, with (6.2) imposed;
2. the complete first-column normal form modulo $p^7$;
3. the complete second-column exterior solve modulo $p^7$, now requiring only $0\le h\le146$;
4. all new coefficient and row-unit lifts;
5. the exceptional scalar and actual coefficient contraction in (9.1);
6. both original cutoff branches;
7. the actual finite endpoint returns.

The physical terminal is separately harmless at this fixed coefficient:


$$
F_b,G_b\in p^2\mathbb Z_p
\Longrightarrow pF_bG_b\in p^5\mathbb Z_p.
$$


Its deletion here is therefore paid. That does not permit deleting its influence on the solved contact coefficients.

A satisfactory output would be either:

- an actual original value of $\kappa$, with completed terminal acceptance; or
- an exact zero observation on every admissible continuation state, with the actual head rows included.

Neither an arbitrary choice of the four scalars nor a nonzero intermediate paid row is such an output.

I do not provide a purported complete-$\kappa$ code specification with an unproved reachable-state bound. The bounded specification in §12 is justified; the full mixed observation connecting it to (7.2) remains to be derived and evaluated.

---

## 17. Preserved global denominator and error

No physical normalization above changes the original row contents, the falling row metric


$$
\omega_j=\frac{(n+2)!}{(n+2-j)!},
\qquad
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2),
$$


or the least simultaneous two-column clearer $d_B$.

Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),
\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
$$


The final gcd is over **all primes**, and the actual primitive multiplier remains


$$
d_B^2/g_B.
$$



For the same original index,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


and the whole evaluated error is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$



At the retained scope of the signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$


Nothing proved here supplies the necessary all-prime bound on the actual $q_n$.

---

## 18. Proof-status ledger

| Statement | Status |
|---|---|
| All-row complete force and finite $\mathsf P_-$ boundary conversion | Reused as closed |
| $\Xi=17$, complete support and paid divisions | Reused completed finite calculation |
| $Y\in p^4$, $F^TQ\in p^3$ on the stated cylinders | Reused at their established scope |
| Convergence on $c_0$ and exterior Neumann convergence | Audited explicitly |
| Exact factorial-filtration preservation | **Proved** |
| Exterior sizes 118 at $K=6$, 147 at $K=7$ | **Proved from actual low residues** |
| Improved mixed first-column budget $d-2$ using $v_p(Y)\ge4$ | **Proved** |
| Actual four-scalar relation $(2,14,8,24)A_q$ | **Proved** |
| Rank-one exceptional eight-interface Gram relation | **Proved for every compatible continuation** |
| Complete first unknown coefficient $\kappa$ | **Not evaluated** |
| Bounded 371-coordinate actual-head interface | **Derived; finite certificate not executed** |
| Nonzero $\kappa$ on a full original cylinder | **Excluded by unbounded actual content** |
| Actual nonzero $\kappa$ obstructs true alignment | **Conditional deduction, with stated $\rho_n$-valuation condition** |
| Primitive mixed alignment on an infinite growing-content subsequence | Open |
| All-prime $q_n$ versus whole same-index error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The new rigorous results are:



$$
\boxed{
v_p(v_h)\ge v_p((b+h)!/b!)
}
$$


for the complete exterior solution,



$$
\boxed{
(A_m,B_m,C_m,D_m)\equiv(2,14,8,24)A_{\lfloor m/29\rfloor}\pmod{29}
}
$$


for the actual first head, and



$$
\boxed{
\sum_JK_s(J)K_t(J)
=\eta_s\eta_t\mathcal E_{\rm exc}\pmod{29}
}
$$


for the first new interface Gram contribution.

These results reduce the exterior solve, remove fictitious freedom from the actual head, and isolate the precise exceptional support on which the old radical fails.

They do **not** evaluate


$$
\kappa(u)=29^{-3}F^TQ\pmod{29}.
$$


The exact remaining fixed-layer bottleneck is the whole lifted expression (7.2), including its new unit corrections and the actual exceptional contraction (9.1). The bounded new arithmetic justified here is the actual-head prime-power interface of §§10–12; it has explicit states, support, precision, original-residue dependence, and verifiable polynomial outputs. No accepted producer is proposed for repetition.

At true depth, the remaining bottleneck is still


$$
\boxed{
x^TY^{[d-c]}-29^{c+3}\rho_nx^Tx
\pmod{29^{d-c}},
}
$$


with the logarithmic head retained when its guard fails.

Finally, no selected-prime result here controls the all-prime final gcd and actual primitive denominator strongly enough to make the whole nonzero same-index error tend to zero. An unconditional proof or disproof of the irrationality of $e+\pi$ remains unresolved.
