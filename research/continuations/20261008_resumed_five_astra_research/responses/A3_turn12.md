> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the all-depth ternary content theorem and the canonical Hermite numerical return

## Executive conclusions

The original infinite domain is retained throughout:


$$
k=N=N_u=9^{18+32u}=3^{36+64u},
\qquad u\in\mathbb Z_{\ge 0}.
$$


The compact determinant producer and the signed polynomial producer remain distinct objects, even though their numerical indices coincide.

### Referee verdict 1 — A2 turn 8: **PASS at the stated original-family scope**

The proof establishes


$$
\boxed{
v_3(\mathscr L_k)=v_3(\mathscr R_k)
=\frac{(k-2)(k-1-2s)}2,
\qquad k=3^s,\quad s=36+64u.
}
$$


More specifically, both designated $Y_k$ cofactors, each retaining all $k$ original scaled forcing columns, attain this valuation.

The decisive argument is valid: after paying the complete factorial-square contact divisor, the prescribed free contact rows give a $3$-integral interpolation basis, and the remaining **complete** forcing Schur matrix has unit determinant modulo $3$. This is not an extension of the old capped-depth row-scalar argument.

The corresponding conclusion for the final compact gcd is only


$$
\boxed{
E_k\le v_3(G_k)\le 2E_k+s+1,
\qquad
E_k=\frac{(k-2)(k-1-2s)}2.
}
$$


No equality for $v_3(G_k)$ follows.

### Referee verdict 2 — A5 turn 11: **PASS for the unconditional numerical return and exact gcd factorizations**

For the actual integer $U_N$, actual reduced $K$-arc denominator $d_{K,N}$, and actual integer $y_{K,N}$, the canonical returns satisfy


$$
\boxed{
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
\qquad
|\mathcal R_{N-1;N}|,\ |\mathcal R_{N;N}|
<d_{K,N}36^N N!.
}
$$


All exceptional divisions are correctly paid, including primes dividing $d_K$ and the determinant factor $2$. Consequently,


$$
\boxed{
\gcd(U_N,y_{K,N})
=\gcd(\mathcal R_{N-1;N},\mathcal R_{N;N}).
}
$$


The exact intrinsic factorization with


$$
s_{r;N}=\gcd(c_N,Q_r^{\mathrm H})
$$


is also correct.

The Hermite source-capture assertion **HC remains open**. Its stated implication


$$
\mathrm{HC}\Longrightarrow
\mathfrak J_N^0\le e^{O(N)}U_N^{3/4}
$$


is correct, and its effect on the **actual** primitive whole error is correctly a conditional divergence result. Neither the critical $N!e^{O(N)}$ endpoint bound nor the coefficient-content work proves HC.

### Global status

These are completed proof audits, not an irrationality proof. The rationality or irrationality of $e+\pi$ remains unresolved.

The deferred A3 $b/\mathrm{first4}$ finite-return obligation remains **open and unevaluated**. Nothing in this report counts its deferral as progress on that obligation.

---

## 1. Scope, conventions, and reused results

A valuation $v_p$ is applied to a nonzero integer or rational number in the usual way. Gcds are positive gcds of absolute values. A “unit at $3$” means an element of $\mathbb Z_{(3)}^\times$; it need not be a unit at another prime.

The following established results are reused at their proved scopes:

1. the integral contact-minor divisors from A3 turn 10;
2. the disproof of the old integral weighted certificate for $k\ge18$;
3. the original-content size bound and exact finite-jet transfer identities;
4. the exact reduced $K$-arc formula, including its original-index cancellation branches;
5. the original signed normalization, content identity, positivity, and already established analytic estimates.

The old capped ternary theorem remains restricted by


$$
2h\le s+2.
$$


It is not used as an all-depth theorem.

The pending centered coefficient-content theorem is not used as an unconditional premise for the direct Hermite numerical return. The already checked centered **polynomial identities** and their two boundary constants are a different matter from an aggregate coefficient-content or numerical gcd bound.

No computation was executed for this report.

---

# Part I. Audit of the exact original $3$-primary rectangle contents

## 2. Original finite arrays and complete forcing

Retain


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad w_n=(-1)^n,
\qquad c_n=u_n-w_n.
$$


Also retain


$$
\rho_0=0,\qquad
\rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad
r_n=-f_n+4\rho_n.
$$


The complete returns are


$$
\sigma_n=c_{n+1}+c_n=u_{n+1}+u_n
$$


and


$$
\boxed{
\tau_n=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
$$



For


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),
$$


write


$$
\boxed{
T_n=\Lambda_k\tau_n
=-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1}.
}
\tag{2.1}
$$


Every displayed quotient in (2.1) is formed as an integer before any modular reduction.

The original arrays are


$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{0\le m<2k-1\\0\le j<k}}
\ \middle|\
(T_{m+j})_{\substack{0\le m<2k-1\\0\le j<k}}
\right]
$$


and


$$
Z_k=
\left[
(c_{m+j})_{\substack{0\le m<2k\\0\le j<k}}
\ \middle|\
(T_{m+j})_{\substack{0\le m<2k\\0\le j<k-1}}
\right].
$$


Their actual maximal-minor contents are


$$
\mathscr L_k=\delta_{2k-1}(Y_k),
\qquad
\mathscr R_k=\delta_{2k-1}(Z_k).
$$



The finite boundary is unchanged:


$$
\boxed{
\text{largest moment }3k-2,\qquad
\text{largest factorial }(6k-4)!,\qquad
\text{last odd denominator }6k-5.
}
\tag{2.2}
$$



---

## 3. Factorial-normalized contact moments

### 3.1 Integral payment of the finite differences

Integration by parts gives


$$
a_n=\int_0^\infty e^{-t}(1-t)^n\,dt.
$$


Hence


$$
u_n=\int_0^\infty e^{-t}(t-1)^{2n}\,dt
$$


and


$$
\Delta^r u_n
=\int_0^\infty e^{-t}(t-1)^{2n}t^r(t-2)^r\,dt.
$$



Expanding $t^r(t-2)^r$, the term indexed by $h$ has a factor


$$
\binom rh 2^{r-h}(r+h)!.
$$


The remaining integral after expanding $(t-1)^{2n}$ is an integer multiple of $(r+h)!$. Moreover,


$$
\frac{\binom rh2^{r-h}(r+h)!}{2^rr!}
=
\binom{r+h}{2h}(2h-1)!!\in\mathbb Z.
$$


Therefore


$$
2^rr!\mid\Delta^r u_n.
$$


Since $\sigma_n=2u_n+\Delta u_n$,


$$
\boxed{
2^{r+1}r!\mid\Delta^r\sigma_n.
}
\tag{3.1}
$$



These are integral divisibilities. No factorial is being inverted as a local unit.

Put


$$
D_r=2^rr!,
\qquad
d_n=\frac{\Delta^n u_0}{2^nn!},
\qquad
\eta_n^{(\alpha)}
=\frac{\Delta^n\sigma_\alpha}{2^{n+1}n!},
\quad \alpha=0,1.
$$



### 3.2 Exact normalized congruences

Direct expansion at $u_0$ gives


$$
d_n
=
\sum_{h=0}^n
(-1)^{n-h}
\binom{n+h}{2h}(2h-1)!!.
$$


For $h\ge2$, the double factorial contains $3$. Thus


$$
d_n\equiv
(-1)^n\left(1-\binom{n+1}{2}\right)\pmod3.
$$



Now


$$
\eta_n^{(0)}=d_n+(n+1)d_{n+1}.
$$


The bracket resulting from substitution is exactly


$$
1-\binom{n+1}{2}
-(n+1)\left(1-\binom{n+2}{2}\right)
=
1+\frac{n(n+1)(n+2)}2.
$$


The second term is divisible by $3$, so


$$
\boxed{\eta_n^{(0)}\equiv(-1)^n\pmod3.}
\tag{3.2}
$$



For the once-shifted sequence,


$$
\eta_n^{(1)}
=\eta_n^{(0)}+2(n+1)\eta_{n+1}^{(0)},
$$


whence


$$
\boxed{\eta_n^{(1)}\equiv(-1)^n(n-1)\pmod3.}
\tag{3.3}
$$



The normalizations in these identities are exact, including the factor $2^{n+1}n!$.

---

## 4. Both normalized contact determinants are evaluated units

Define


$$
B_{rc}^{(\alpha)}
=
\binom{r+c}{r}\eta_{r+c}^{(\alpha)}.
$$


The finite double-Newton identity gives


$$
(\sigma_{m+j+\alpha})
=
2P_{\rm row}D_{\rm row}
B^{(\alpha)}
D_{\rm col}P_{\rm col}^{T},
\tag{4.1}
$$


where $P$ is the relevant finite Pascal matrix.

Indeed,


$$
2D_rB_{rc}^{(\alpha)}D_c
=2^{r+c+1}(r+c)!\eta_{r+c}^{(\alpha)}
=\Delta^{r+c}\sigma_\alpha.
$$



For later use, the established contact-return divisor is


$$
\mathcal A_d
=
2^{d^2}\left(\prod_{j=0}^{d-1}j!\right)^2
=
2^d\left(\prod_{j=0}^{d-1}D_j\right)^2.
\tag{4.2}
$$


Cauchy–Binet proves that it divides every $d$-minor: the selected diagonal indices are distinct, and $D_i\mid D_{i+1}$.

### 4.1 Unshifted determinant

By (3.2),


$$
B_d^{(0)}
\equiv
\left((-1)^{r+c}\binom{r+c}{r}\right)_{r,c<d}
\pmod3.
$$


The identity


$$
\binom{r+c}{r}
=\sum_h\binom rh\binom ch
$$


factors the unsigned matrix as $PP^T$, with $P$ unit lower triangular. The row and column signs have combined determinant $1$. Hence


$$
\boxed{\det B_d^{(0)}\equiv1\pmod3.}
\tag{4.3}
$$



### 4.2 Once-shifted determinant

After removing the same row and column signs, (3.3) gives


$$
N_d=\left((r+c-1)\binom{r+c}{r}\right)_{r,c<d}.
$$


Let


$$
J=\operatorname{diag}(0,\ldots,d-1),
\qquad S_{i,i-1}=i.
$$


The finite identity


$$
P^{-1}JP=J+S
$$


follows entrywise from


$$
r\binom rh
=h\binom rh+(h+1)\binom r{h+1}.
$$


Consequently


$$
N_d=P(2J-I+S+S^T)P^T.
$$



If $D_n^\ast$ denotes the tridiagonal determinant, then


$$
D_0^\ast=1,\qquad D_1^\ast=-1,
$$




$$
D_{n+1}^\ast=(2n-1)D_n^\ast-n^2D_{n-1}^\ast.
\tag{4.4}
$$


Modulo $3$, three consecutive steps give


$$
D_{3q+1}^\ast=-D_{3q}^\ast,\qquad
D_{3q+2}^\ast=D_{3q}^\ast,\qquad
D_{3q+3}^\ast=D_{3q}^\ast.
$$


Thus


$$
D_{3q}^\ast=1,\quad
D_{3q+1}^\ast=-1,\quad
D_{3q+2}^\ast=1\pmod3.
$$


In particular, for $d=k-1$ and $3\mid k$,


$$
\boxed{\det B_d^{(1)}\equiv1\pmod3.}
\tag{4.5}
$$



Both required normalized determinants have therefore been evaluated. No nonvanishing determinant remains as an assumption.

---

## 5. The factorial row weights and the saturated contact basis

Let


$$
k=3^s,\qquad d=k-1,
$$


and let $m_0,\ldots,m_{d-1}$ be any nonnegative row indices. Use a finite row range $0,\ldots,M$, where $M=\max m_i$. Cauchy–Binet in (4.1) gives the exact finite identity


$$
\frac{\det(\sigma_{m_i+c+\alpha})_{i,c<d}}{\mathcal A_d}
=
\sum_{\substack{R=\{r_0<\cdots<r_{d-1}\}\\R\subseteq\{0,\ldots,M\}}}
\det\left(\binom{m_i}{r_j}\right)
\frac{\prod_{r\in R}D_r}{\prod_{j=0}^{d-1}D_j}
\det B^{(\alpha)}[R,0,\ldots,d-1].
\tag{5.1}
$$



Every diagonal quotient is integral because $r_j\ge j$.

If $R$ contains an index at least $k$, its last diagonal quotient alone contributes at least


$$
v_3(k!)-v_3((k-2)!)=s.
$$


All other contributions are nonnegative. Such a term vanishes modulo $3$.

This is the correct factorial-weight argument. It does **not** assert that the leading index set is the unique minimum-weight set: sets containing $k-1$ can have the same $3$-weight. They must be handled separately.

For every surviving $r<k$,


$$
\binom{m+k}{r}\equiv\binom mr\pmod3,
$$


because


$$
(1+x)^k\equiv1+x^k\pmod3.
$$


Thus the normalized determinant in (5.1), modulo $3$, depends only on the ordered residues $m_i\bmod k$.

If these ordered residues are $0,1,\ldots,k-2$, every surviving set other than


$$
R_0=\{0,\ldots,k-2\}
$$


contains $k-1$, and its Pascal determinant vanishes because


$$
\binom{i}{k-1}=0,\qquad 0\le i\le k-2.
$$


The $R_0$ term equals $1$, by (4.3) or (4.5). Therefore


$$
\boxed{
\frac{\det(\sigma_{m_i+c+\alpha})_{i,c<d}}{\mathcal A_d}
\equiv1\pmod3
}
\tag{5.2}
$$


for the prescribed residue order.

Let $C_F$ be such a square contact block. Then


$$
\det C_F=\mathcal A_d b,\qquad b\equiv1\pmod3.
$$


Every row-replacement Cramer numerator is divisible by $\mathcal A_d$. Hence


$$
C(m)C_F^{-1}\in\mathbb Z_{(3)}^d.
\tag{5.3}
$$


If $m\equiv m_i\pmod k$, the normalized replacement determinants are $1$ in position $i$ and $0$ in all other positions, so


$$
\boxed{C(m)C_F^{-1}\equiv e_i^T\pmod3.}
\tag{5.4}
$$



This pays the entire interpolation denominator at $3$. The remaining integer $b$ may have other prime factors.

---

## 6. The two original $Y_k$ cofactors

### 6.1 Prescribed rows and complete forcing support

Write


$$
k=2t+1,\qquad n_0=3t+1=\frac{3k-1}{2}.
$$


The forcing pivot rows, in the prescribed order, are


$$
P=(n_0,n_0-1,\ldots,t+1).
$$


The remaining rows, in increasing order, are


$$
F=\{0,\ldots,t\}\cup\{3t+2,\ldots,4t\}.
$$


Their ordered residues modulo $k$ are exactly $0,\ldots,k-2$.

Since


$$
3k\le6k-5<9k,
$$




$$
v_3(\Lambda_k)=s+1.
$$


Define


$$
\gamma=\frac{4\Lambda_k}{3k}\in\mathbb Z,\qquad 3\nmid\gamma.
$$


Among the physical odd denominators, the only one of valuation $s+1$ is $3k$. The factorial portion of (2.1) is divisible by $3$. Therefore


$$
T_n\equiv\gamma\,\mathbf1_{n=n_0}\pmod3.
\tag{6.1}
$$



For the actual forcing blocks


$$
M=(T_{n_0-i+j})_{0\le i,j<k},
\qquad
T_F=(T_{f_a+j})_{\substack{0\le a<d\\0\le j<k}},
$$


this yields


$$
\boxed{M\equiv\gamma I_k,\qquad T_F\equiv0\pmod3.}
\tag{6.2}
$$



Only these reductions are used. The exact matrices retain every factorial and rational-forcing contribution.

### 6.2 Paid Schur matrix

For $\alpha=0,1$, let $C_F^{(\alpha)}$ and $C_P^{(\alpha)}$ be the contact blocks with shifts $c+\alpha$, $0\le c<d$. Here:

- $\alpha=0$ omits contact-return column $k-1$;
- $\alpha=1$ omits contact-return column $0$.

By Section 5,


$$
\det C_F^{(\alpha)}=\mathcal A_d b_\alpha,
\qquad b_\alpha\equiv1\pmod3.
$$


Define the integer Cramer matrix $N_\alpha$ by dividing each corresponding row-replacement determinant by $\mathcal A_d$. Then


$$
C_P^{(\alpha)}(C_F^{(\alpha)})^{-1}
=\frac{N_\alpha}{b_\alpha}.
$$



The exact integer Schur numerator is


$$
\boxed{K_\alpha=b_\alpha M-N_\alpha T_F.}
\tag{6.3}
$$


Entrywise, this is


$$
\begin{aligned}
(K_\alpha)_{ij}
={}&b_\alpha\left[
-\Lambda_k\bigl((2(n_0-i+j)+2)!+(2(n_0-i+j))!\bigr)
+\frac{4\Lambda_k}{2(n_0-i+j)+1}
\right]\\
&-\sum_{a=0}^{d-1}(N_\alpha)_{ia}\left[
-\Lambda_k\bigl((2(f_a+j)+2)!+(2(f_a+j))!\bigr)
+\frac{4\Lambda_k}{2(f_a+j)+1}
\right].
\end{aligned}
\tag{6.4}
$$


Thus all forcing and cross terms are present.

Equations (6.2) and $b_\alpha\equiv1$ give


$$
K_\alpha\equiv\gamma I_k\pmod3,
\qquad
\det K_\alpha\equiv\gamma^k\ne0\pmod3.
\tag{6.5}
$$



### 6.3 Permutation sign and exact determinant identity

The permutation from the original row order to $F,P$ has


$$
k(t-1)+\frac{k(k-1)}2=k(k-2)
$$


inversions, an odd number. Its sign is $-1$.

The block determinant formula therefore gives, in inherited determinant orientation,


$$
\boxed{
b_\alpha^{k-1}M_k^{(\mathrm{omit})}
=-\mathcal A_d\det K_\alpha.
}
\tag{6.6}
$$


Both factors outside $\mathcal A_d$ are $3$-units. Hence


$$
\boxed{
v_3(M_k^{(0)})
=v_3(M_k^{(k-1)})
=2\sum_{j=0}^{k-2}v_3(j!).
}
\tag{6.7}
$$



Since $d$ is even, the $3$-unit part of $\mathcal A_d$ is $1$ modulo $3$. Also $\gamma^k\equiv\gamma\pmod3$. Thus


$$
\boxed{
3^{-E_k}M_k^{(0)}
\equiv
3^{-E_k}M_k^{(k-1)}
\equiv-\frac{\Lambda_k}{3k}\pmod3.
}
\tag{6.8}
$$



Every finite-difference input used here lies within (2.2).

---

## 7. The original $Z_k$ minor and its literal contact atom

Select the first $2k-1$ rows of the original $Z_k$. This is a maximal minor of $Z_k$, not a replacement producer.

For $k=3^s\ge9$, use


$$
P_Z=(3t+1,3t,\ldots,t+2),
$$


and


$$
F_Z=\{0,\ldots,t+1\}\cup\{3t+2,\ldots,4t\}.
$$


Make the integer determinant-one contact-column transformation


$$
(c_0,\ldots,c_{k-1})
\longmapsto
(c_0,\sigma_0,\ldots,\sigma_{k-2}).
\tag{7.1}
$$



Let


$$
m_0=t+1,\qquad h=3t+2=m_0+k,
\qquad
F_\sigma=F_Z\setminus\{h\}.
$$


The rows of $F_\sigma$ have ordered residues $0,\ldots,k-2$, so their square $\sigma$-block has determinant valuation $E_k$.

By (5.3)–(5.4), the $\sigma$-row at $h$ is a $3$-integral combination $x$ of the rows of $F_\sigma$, with


$$
x\equiv e_{m_0}^T\pmod3.
$$


After eliminating that row’s $\sigma$-entries, the retained first-column entry is


$$
c_h-xc_{F_\sigma}\equiv c_h-c_{m_0}\pmod3.
$$



The recurrence gives $u_{n+3}\equiv u_n\pmod3$. Since $3\mid k$ and $k$ is odd,


$$
u_h\equiv u_{m_0}\pmod3,\qquad
(-1)^h=-(-1)^{m_0}.
$$


Therefore


$$
\boxed{
c_h-c_{m_0}\equiv2(-1)^{m_0}\ne0\pmod3.
}
\tag{7.2}
$$



This is the essential atom payment. Deleting $(-1)^n$ would delete the unit in (7.2).

The reused all-minor contact divisor is


$$
\mathcal B_k
=
2^{k(k-1)}
\left(\prod_{j=0}^{k-2}j!\right)^2,
\qquad
v_3(\mathcal B_k)=E_k.
$$


Its proof retains the rank-one atom: after double differences and extraction of row and column powers of $2$, the matrix is a factorial-divisible matrix minus a rank-one matrix. A $k$-minor therefore contains at least the factorial payments for a $(k-1)$-minor of the first matrix.

The contact block on $F_Z$ has determinant valuation $E_k$, by (7.2). Dividing its Cramer numerators by $\mathcal B_k$ again pays the contact interpolation at $3$.

The $k-1$ forcing columns have a unit pivot block on $P_Z$, while their entries on $F_Z$ vanish modulo $3$. Thus the same complete Schur argument proves


$$
\boxed{
v_3\!\left(\det Z_k[0,\ldots,2k-2;\,:]\right)=E_k.
}
\tag{7.3}
$$



The unused last row remains part of the original $Z_k$, its actual content, and the producer.

---

## 8. Evaluation of the contents, allowance, and final $G_3$ range

Legendre’s formula and the base-$3$ digit sum over $0,\ldots,3^s-1$ give


$$
\sum_{j=0}^{k-1}v_3(j!)
=\frac{k(k-1-2s)}4,
\qquad
v_3((k-1)!)=\frac{k-1-2s}{2}.
$$


Therefore


$$
\boxed{
E_k=2\sum_{j=0}^{k-2}v_3(j!)
=\frac{(k-2)(k-1-2s)}2.
}
\tag{8.1}
$$



Every maximal minor of $Y_k$ has at least $k-1$ contact-return columns. Laplace expansion and $\mathcal A_{k-1}$ give the lower valuation $E_k$; the two evaluated cofactors attain it.

Every maximal minor of $Z_k$ contains all $k$ contact columns. The divisor $\mathcal B_k$ gives the same lower valuation, and (7.3) attains it. Hence


$$
\boxed{v_3(\mathscr L_k)=v_3(\mathscr R_k)=E_k.}
\tag{8.2}
$$



The odd-certificate allowance is


$$
B_3(k)=k^2+(2-s)k.
$$


Its exact excess over $E_k$ is


$$
\boxed{
B_3(k)-E_k=\frac{k^2+7k-2-4s}{2}>0.
}
\tag{8.3}
$$



For the final affine determinant


$$
H_k(z)=H_{0,k}+H_{1,k}z
=\det[c_{m+j}\mid
\Lambda_k(r_{m+j}+z(-1)^{m+j})],
$$


retain


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|).
$$


The established bordered-content relations are


$$
\operatorname{lcm}(\mathscr R_k,\mathscr L_k)
\mid G_k\mid\Lambda_k\mathscr R_k\mathscr L_k.
$$


Consequently,


$$
\boxed{E_k\le v_3(G_k)\le2E_k+s+1.}
\tag{8.4}
$$



The lower and upper bounds come from different divisibilities. Neither establishes equality, and neither controls the other prime parts of $G_k$.

---

## 9. The completed $Y_{27}$ receipt: correct finite scope

The supplied receipt retains the correct data:

- $Y_{27}$ has shape $53\times54$;
- moments stop at $79$;
- factorials stop at $158!$;
- the last odd denominator is $157$;
- both cofactors retain all $27$ original forcing columns.

The theorem predicts


$$
E_{27}=\frac{25(26-6)}2=250.
$$


Moreover,


$$
\Lambda_{27}/81\equiv2\pmod3,
$$


so (6.8) predicts normalized unit $1$ in both inherited determinant orientations.

The nonzero depth payments in each supplied ternary ledger are


$$
\begin{array}{c|rrrrrrrr}
\text{active size}&23&20&17&14&11&8&5&2\\
\text{entry division depth}&2&2&4&2&2&4&2&2\\
\text{determinant payment}&46&40&68&28&22&32&10&4
\end{array}
$$


and their sum is


$$
46+40+68+28+22+32+10+4=250.
$$


The sum of the entry-precision losses is $20$, leaving precision $251-20=231$, consistent with the receipt.

For omitted column $0$, the listed unit-pivot product has $39$ factors congruent to $-1$, and the total swap parity is odd. For omitted column $26$, there are $43$ such pivot factors, again with odd total swap parity. Both normalized determinant units are therefore $1$.

The Bareiss division count is also internally consistent:


$$
\sum_{j=1}^{52}j^2=48230.
$$



This audits the mathematical accounting of the supplied finite receipt. It does not reproduce its hashes or large exact determinants. The two expected residues also follow independently by specializing the uniform proof above:


$$
\boxed{
M_{27}^{(0)}\equiv M_{27}^{(26)}
\equiv3^{250}\pmod{3^{251}}.
}
$$


The receipt remains one auxiliary finite check, not an original-index experiment or an all-prime theorem. It must not be regenerated as another capped-spectrum calculation.

---

## 10. Remaining compact payments and limits of the result

### 10.1 Actual binary upper bound

Let


$$
\mathcal D_k^{\rm odd}
=
\left(\prod_{j=0}^{k-2}\operatorname{odd}(j!)\right)^2.
$$


The integral contact divisors imply


$$
\mathcal D_k^{\rm odd}\mid\mathscr L_k,\mathscr R_k.
$$


Using the established size bound


$$
\mathscr L_k,\mathscr R_k\le\mathcal U_k,
$$




$$
\mathcal U_k
=(2k-1)!\,4^k10^{k-1}\Lambda_k^{k-1}
\prod_{i=0}^{k-1}(2k+4i)!,
$$


gives


$$
\boxed{
v_2(\mathscr L_k),v_2(\mathscr R_k)
\le
\left\lfloor
\log_2\frac{\mathcal U_k}{\mathcal D_k^{\rm odd}}
\right\rfloor.
}
\tag{10.1}
$$


This uses a size bound, not the false assertion that a content divides $\mathcal U_k$.

The stated asymptotic constants check:


$$
\log\mathcal U_k
=
4k^2\log k+
\left(4\log2+\frac92\log3\right)k^2+o(k^2),
$$




$$
\log\mathcal D_k^{\rm odd}
=
k^2\log k-\left(\frac32+\log2\right)k^2
+O(k\log k).
$$


Thus the resulting binary bound is still $O(k^2\log k)$, not the useful $O(k^2)$ estimate.

The exact paid identity


$$
v_2(M_k^{(\mathrm{omit})})
=
v_2(\mathcal A_{k-1})
+v_2(\det K_\alpha)
-(k-1)v_2(b_\alpha)
$$


is valid, but it does not evaluate its last two terms. In particular, $b_\alpha$ was proved to be a unit only at $3$.

Other odd-prime descent, including good-prime normality above $6k-5$, and a useful direct upper bound for the actual $v_2(G_k)$, remain open.

### 10.2 Actual finite-jet corrections and coefficient clearer

The finite transformations remain


$$
(T_\star y)_m
=
\sum_{r=0}^m
(-1)^r\binom{b_\star}{r}
(2m-2r+1)_{h_\star+2r}y_{m-r},
$$


with


$$
(h_Z,b_Z)=(2k-3,2k-1),\qquad
(h_Y,b_Y)=(2k-1,2k+1),
$$


on the original row ranges. The integral jet arrays retain the complete $\tau$:


$$
\mathbf J_{Z,k}=T_Z[c\mid\tau],
\qquad
\mathbf J_{Y,k}=T_Y[\sigma\mid\tau].
$$



Retain their actual contents $\mathscr C_{Z,k},\mathscr C_{Y,k}$, and


$$
t_Z=\prod_{m=0}^{2k-1}(2m+1)_{2k-3},
\qquad
t_Y=\prod_{m=0}^{2k-2}(2m+1)_{2k-1}.
$$


For the actual primitive transformed $Z$-cofactor vector $v$,


$$
\zeta_{Z,k}
=
\operatorname{lcm}_m
\frac{(2m+1)_{2k-3}}
{\gcd((2m+1)_{2k-3},|v_m|)}.
$$


For the two actual $Y$-jet minor-type gcds $\alpha_Y,\beta_Y$,


$$
\chi_{Y,k}
=
\frac{\gcd(\Lambda_k\alpha_Y,\beta_Y)}
{\gcd(\alpha_Y,\beta_Y)}.
$$


The exact transfers are


$$
\boxed{
\mathscr R_k=
\frac{\Lambda_k^{k-1}\mathscr C_{Z,k}\zeta_{Z,k}}{t_Z},
\qquad
\mathscr L_k=
\frac{\Lambda_k^{k-1}\mathscr C_{Y,k}\chi_{Y,k}}{t_Y}.
}
\tag{10.2}
$$


Neither correction is assigned the value $1$.

The original individual affine right-column clearers remain


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$


The least simultaneous coefficient clearer of $H_k/\Lambda_k^k$ is


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}),
}
$$


and the remaining coefficient content is $G_k/d_{H,k}$.

### 10.3 Actual primitive compact error

Whenever $H_{1,k}\ne0$,


$$
q_k=\frac{|H_{1,k}|}{G_k},
\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
$$


On the established original positivity domain,


$$
\boxed{
0<q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}.
}
\tag{10.3}
$$



The reused transfer constant remains


$$
\log\mathscr R_k+\log\mathscr L_k
=
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
-8k^2\log k+(24-18\log3)k^2+o(k^2).
$$


The exact identity preceding this asymptotic must retain $\zeta_{Z,k}$, $\chi_{Y,k}$, and $2(k-1)\log\Lambda_k$.

At the critical leading coefficient, the proposed divergence comparison remains


$$
C_H>C_J+24-18\log3.
$$


The all-depth $3$-part theorem does not settle that comparison or establish primitive whole-error decay.

---

# Part II. Audit of the canonical numerical Hermite return

## 11. Actual signed source, content, arcs, and clearers

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j.
$$


At an original $N$, retain the actual Gaussian divisions


$$
g_B=\gcd(b_{N-1},b_N)>0,
\quad
\alpha=\frac{b_{N-1}}{g_B},
\quad
\beta=\frac{b_N}{g_B},
$$




$$
\delta=\frac{a_Nb_{N-1}-a_{N-1}b_N}{g_B}.
$$


Then


$$
F=\alpha C_N-\beta C_{N-1},
\qquad F(\pm i)=\delta,
\qquad \gcd(\alpha,\beta)=1.
$$



Set


$$
\mathcal H(t)=t(1-t)(1+t^2)^2,
\qquad m=N-3,\qquad K=\mathcal H C_m^2.
$$


The physical degree is


$$
\deg K=2m+6=2N.
$$



For an integer polynomial $H$, retain


$$
\eta(H)=\int_{-\infty}^1e^{t-1}H(t)\,dt
=\sum_r[z^r]H(1-z)\,r!,
$$


and


$$
E(H)=\sum_r(-1)^rr![t^r]H.
$$


There is no extra alternating sign in the coefficient formula for $\eta$.

The actual numerical source data are


$$
U=-\eta(K),\qquad
V=\eta(F^2)-\delta^2,\qquad
c=\gcd(U,V).
$$


The established content identity is


$$
h=\operatorname{cont}(W_{\rm raw})=g_B^2c.
$$


Thus


$$
\tau=\frac Uc,\qquad \nu=\frac Vc,\qquad
W_{\rm prim}=\tau F^2+\nu K,\qquad
M=\tau\delta^2.
\tag{11.1}
$$



The two complete arcs are


$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,
\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


Monic division proves that both quotients are integer polynomials of degree at most $2N-2$. Their reduced denominators therefore divide


$$
L_{\rm aff}=\operatorname{lcm}(1,\ldots,2N-1).
$$



The actual least simultaneous clearer is


$$
D=\operatorname{lcm}(\operatorname{den}R_F,\operatorname{den}R_K),
$$


and


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$



Independently reduce the aggregate arc:


$$
\tau R_F+\nu R_K=\frac b\lambda,
\qquad \gcd(b,\lambda)=1,\quad\lambda>0.
$$


Then


$$
E=\tau E_F+\nu E_K,\quad A=\lambda E-b,\quad G=\gcd(M,A),
$$


and the actual primitive pair is


$$
\boxed{p=\frac AG,\qquad q=\frac{\lambda M}{G}.}
\tag{11.2}
$$


Because $\gcd(A,\lambda)=1$, this is the full reduction over all primes.

The exact reconciliation is


$$
\tau X+\nu Y=\frac D\lambda A,
$$




$$
\boxed{
\gcd(D\tau\delta^2,\tau X+\nu Y)=\frac D\lambda G.
}
\tag{11.3}
$$


Also,


$$
\lambda=\frac D{\gcd(D,\tau DR_F+\nu DR_K)}.
$$


Thus $D$ and $\lambda$ are not interchangeable.

---

## 12. The actual reduced $K$-arc denominator

Write


$$
\ell=2N-6,\qquad x=\ell^2,
$$




$$
L(x)=(x-1)(x-9)(x-25),
$$




$$
A_K(x)=13x^3-455x^2+3502x-5850.
$$


The reused exact arc identity is


$$
R_K=\frac{A_K(x)}{30L(x)}.
$$



The previous all-prime cancellation proof uses


$$
A_K=13L+45(3x-65),
$$




$$
27L=(3x-65)(9x^2-120x-269)-23560.
$$


It then evaluates the possible cancellation primes on the original exponent domain. Retaining that result,


$$
g_{\rm arc}
=90\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}},
$$


where


$$
\varepsilon_5=\mathbf1_{u\equiv1\pmod5},
\quad
\varepsilon_{19}=\mathbf1_{u\equiv3\pmod9},
$$




$$
\varepsilon_{31}
=\mathbf1_{u\equiv5\text{ or }7\pmod{15}}.
$$


Hence the actual reduced fraction is


$$
\boxed{
a_K=\frac{A_K(x)}{g_{\rm arc}},
\qquad
d_K=\frac{30L(x)}{g_{\rm arc}}
=\frac{L(x)}
 {3\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}}}.
}
\tag{12.1}
$$


In particular,


$$
\gcd(a_K,d_K)=1,
\qquad
\frac{L(x)}{285}\le d_K\le\frac{L(x)}3
<\frac{64}{3}N^6.
\tag{12.2}
$$



Define


$$
\boxed{y_K=d_KE_K-a_K,\qquad \mu=D/d_K.}
$$


Then


$$
Y=\mu y_K,\qquad
\boxed{\gcd(d_K,y_K)=1.}
\tag{12.3}
$$


This last equality is a property of the actual reduced fraction. It is not a statement about a coefficient-row gcd.

The coarse exponential clearer bound is safe:


$$
D\le L_{\rm aff}<256^N.
\tag{12.4}
$$


For example, an elementary dyadic proof uses


$$
\frac{\operatorname{lcm}(1,\ldots,2r)}
{\operatorname{lcm}(1,\ldots,r)}
\mid\binom{2r}{r},
$$


followed by $\binom{2r}{r}<4^r$ and a containing power of $2$. This yields
$\operatorname{lcm}(1,\ldots,m)<16^m$, more than enough for (12.4) with $m=2N-1$.

---

## 13. Paid Hermite endpoint sequences

For $r\ge0$, put


$$
f_r(t)=\frac{t^r(1-t)^r}{r!},
\qquad
a_{r,j}=\frac{(r+j)!}{j!(r-j)!}.
$$


The latter is an integer, for example because


$$
a_{r,j}
=\binom{r+j}{j}\frac{r!}{(r-j)!}.
$$



Define


$$
P_r^{\mathrm H}=\sum_{j=0}^r a_{r,j},
\qquad
Q_r^{\mathrm H}=\sum_{j=0}^r(-1)^{r+j}a_{r,j}.
$$



### 13.1 Endpoint normalization and the $r!$ payment

For a polynomial $H$, let


$$
\mathcal A(H)=\sum_{k=0}^{\deg H}(-1)^kH^{(k)}.
$$


Then


$$
\mathcal A(H)'+\mathcal A(H)=H,
$$


and


$$
\mathcal A(H)(0)=E(H),\qquad
\mathcal A(H)(1)=\eta(H).
$$



At $0$,


$$
f_r^{(r+j)}(0)=(-1)^j a_{r,j}.
$$


Symmetry $f_r(1-t)=f_r(t)$ supplies the derivatives at $1$. Therefore


$$
\boxed{
E(f_r)=(-1)^rP_r^{\mathrm H},
\qquad
\eta(f_r)=(-1)^rQ_r^{\mathrm H}.
}
\tag{13.1}
$$


Thus the rational coefficient divisor $r!$ is completely paid in the endpoint integers.

### 13.2 Recurrence, parity, and determinant

With out-of-range coefficients interpreted as zero,


$$
a_{r+1,j}=(4r+2)a_{r,j-1}+a_{r-1,j}.
$$


After extracting the common factorial factor, this reduces to


$$
(r+j)(r+j+1)-(r+1-j)(r-j)=j(4r+2).
$$


Consequently


$$
P_{r+1}^{\mathrm H}=(4r+2)P_r^{\mathrm H}+P_{r-1}^{\mathrm H},
$$




$$
Q_{r+1}^{\mathrm H}=(4r+2)Q_r^{\mathrm H}+Q_{r-1}^{\mathrm H},
$$


with


$$
(P_0^{\mathrm H},Q_0^{\mathrm H})=(1,1),
\qquad
(P_1^{\mathrm H},Q_1^{\mathrm H})=(3,1).
$$



All these integers are positive and odd. Their determinant satisfies


$$
\boxed{
P_{r+1}^{\mathrm H}Q_r^{\mathrm H}
-P_r^{\mathrm H}Q_{r+1}^{\mathrm H}
=2(-1)^r.
}
\tag{13.2}
$$


The Euclidean recurrence also gives


$$
\boxed{\gcd(Q_r^{\mathrm H},Q_{r+1}^{\mathrm H})=1.}
\tag{13.3}
$$



The determinant is $2$, not $1$. Its binary payment is supplied in Section 17 below.

### 13.3 Signed Hermite error and heights

Let


$$
I_r^{\mathrm H}=\int_0^1e^tf_r(t)\,dt.
$$


Equation (13.1) gives


$$
\boxed{
P_r^{\mathrm H}-eQ_r^{\mathrm H}
=(-1)^{r+1}I_r^{\mathrm H}.
}
\tag{13.4}
$$


The beta integral yields


$$
\int_0^1f_r(t)\,dt=\frac{r!}{(2r+1)!}.
$$


Since $1<e^t<3$ on the interior,


$$
\boxed{
\frac{r!}{(2r+1)!}
<I_r^{\mathrm H}
<\frac{3r!}{(2r+1)!}.
}
\tag{13.5}
$$



Relative to the last coefficient,


$$
\frac{a_{r,r-j}}{a_{r,r}}
=\frac1{j!}\prod_{k=0}^{j-1}\frac{r-k}{2r-k}
\le\frac{2^{-j}}{j!}.
$$


Hence


$$
\boxed{
0<Q_r^{\mathrm H}\le P_r^{\mathrm H}
<2\frac{(2r)!}{r!}
\le2\cdot4^rr!.
}
\tag{13.6}
$$



No external approximation theorem is needed for these identities or constants.

---

## 14. The complete centered force and both boundary constants

The canonical original coordinates satisfy


$$
\Theta_0=\Phi_0=0,\qquad \Theta_1=\Phi_1=1,
$$




$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
\tag{14.1}
$$



Retain the already checked centered polynomials


$$
\begin{aligned}
\mathcal P(x)&=-8x^3-1116x^2-8150x+151,\\
\mathcal Q(x)&=76x^2+2408x+5637,\\
\mathcal F(x)&=4x^2+492x+5463,\\
\mathcal G(x)&=4x^2+556x-3325.
\end{aligned}
$$


At $x=\ell^2$, set


$$
\widetilde{\mathsf A}
=2\ell((2\ell+1)\mathcal Q-\mathcal P),
\quad
\widetilde{\mathsf B}=-2\ell\mathcal Q,
$$




$$
\widetilde{\mathsf C}_U
=\mathcal F-\mathcal P+2\ell\mathcal Q,
\quad
\widetilde{\mathsf C}_E
=\mathcal G+\mathcal P-2(\ell+1)\mathcal Q.
$$


The complete identities are


$$
16U=\widetilde{\mathsf C}_U
-\widetilde{\mathsf A}\Theta_\ell
-\widetilde{\mathsf B}\Theta_{\ell-1},
$$




$$
16E_K=\widetilde{\mathsf C}_E
+\widetilde{\mathsf A}\Phi_\ell
+\widetilde{\mathsf B}\Phi_{\ell-1}.
\tag{14.2}
$$



The two constants check independently:


$$
\widetilde{\mathsf C}_U(0)=5463-151=5312,
$$




$$
\widetilde{\mathsf C}_E(0)=-3325+151-2(5637)=-14448.
$$


They also agree with the direct degree-six evaluations


$$
\eta(\mathcal H)=-332,\qquad E(\mathcal H)=-903.
$$



For fixed original $N$, define the actual integer return


$$
\boxed{
\mathcal R_{r;N}=d_KP_r^{\mathrm H}U+Q_r^{\mathrm H}y_K,
\qquad 0\le r\le N.
}
\tag{14.3}
$$


Put


$$
\Psi_j=Q_r^{\mathrm H}\Phi_j-P_r^{\mathrm H}\Theta_j.
$$


Then the actual boundaries and both forcings give


$$
\Psi_0=0,\qquad \Psi_1=Q_r^{\mathrm H}-P_r^{\mathrm H},
$$




$$
\boxed{
\Psi_{j+1}+4j\Psi_j-\Psi_{j-1}
=2\bigl(Q_r^{\mathrm H}(-1)^j-P_r^{\mathrm H}\bigr).
}
\tag{14.4}
$$


Substituting (14.2) into (14.3) proves


$$
\boxed{
\begin{aligned}
16\mathcal R_{r;N}
={}&d_K\Bigl(
P_r^{\mathrm H}\widetilde{\mathsf C}_U
+Q_r^{\mathrm H}\widetilde{\mathsf C}_E
+\widetilde{\mathsf A}\Psi_\ell
+\widetilde{\mathsf B}\Psi_{\ell-1}
\Bigr)\\
&-16Q_r^{\mathrm H}a_K.
\end{aligned}
}
\tag{14.5}
$$



Thus neither boundary constant, neither forcing, nor the reduced arc term has been omitted.

The direct proof of the numerical return below uses the original integral definitions, not an unproved coefficient-content theorem or arbitrary recurrence states.

---

## 15. Evaluation of the actual return: signs and all height constants

### 15.1 Complete $K$-endpoint contribution

Let


$$
I_K=\int_0^1e^tK(t)\,dt,
$$


and retain the whole contribution


$$
T_K=I_K+R_K
=\int_0^1K(t)\left(e^t+\frac4{1+t^2}\right)\,dt.
\tag{15.1}
$$


The antiderivative identity gives


$$
I_K=e\eta(K)-E_K=-eU-E_K,
$$


so


$$
E_K=-eU-I_K.
$$


Using (13.4) in (14.3),


$$
\boxed{
\mathcal R_{r;N}
=d_K\left(
(-1)^{r+1}UI_r^{\mathrm H}
-Q_r^{\mathrm H}T_K
\right).
}
\tag{15.2}
$$



On $[0,1]$, $0\le C_m^2\le1$, and


$$
\int_0^1\mathcal H(t)\,dt=\frac{61}{210}.
$$


Therefore


$$
\boxed{
0<T_K<\frac{61}{30},
\qquad
0<I_K<\frac{61}{70}<1.
}
\tag{15.3}
$$



### 15.2 Explicit upper and lower bounds for $U$

The coefficients of $C_m(1-z)=T_m(1-2z)$ alternate in sign, so


$$
\|C_m(1-z)\|_1=T_m(3)<6^m
$$


for $m\ge1$. Also


$$
\mathcal H(1-z)
=4z-12z^2+16z^3-12z^4+5z^5-z^6
$$


has coefficient $1$-norm $50$. Since $\deg K=2N$,


$$
\boxed{
U<50\cdot36^{N-3}(2N)!.
}
\tag{15.4}
$$



For $s\ge0$,


$$
|C_m(-s)|=T_m(1+2s)\ge2^{2m-1}s^m.
$$


One justification is that the shifted roots are negative, so the expansion in $s$ has positive coefficients and the leading term is the displayed one. Also


$$
s(1+s)(1+s^2)^2\ge s^6.
$$


Thus


$$
-E_K
=\int_0^\infty e^{-s}
s(1+s)(1+s^2)^2C_m(-s)^2\,ds
\ge2^{4N-14}(2N)!.
$$


Using $eU=-E_K-I_K$, $I_K<1$, and $e<3$, gives for $N\ge4$


$$
\boxed{
U>2^{4N-16}(2N)!.
}
\tag{15.5}
$$



These inequalities also independently confirm the required leading size


$$
\log U=2N\log N+O(N).
$$



### 15.3 Nonzero signs at the same original $N$

Every original $N$ is odd. Hence $N-1$ is even, and (15.2) immediately gives


$$
\boxed{
\mathcal R_{N-1;N}
=-d_K\left(UI_{N-1}^{\mathrm H}
+Q_{N-1}^{\mathrm H}T_K\right)<0.
}
\tag{15.6}
$$



For $r=N$,


$$
UI_N^{\mathrm H}
>2^{4N-16}\frac{N!}{2N+1},
$$


whereas


$$
Q_N^{\mathrm H}T_K
<\frac{61}{15}4^NN!.
$$


The former exceeds the latter when


$$
4^N>\frac{61}{15}2^{16}(2N+1).
$$


This holds at $N=16$, and $4^N/(2N+1)$ is increasing. It therefore holds throughout the original domain. Consequently,


$$
\boxed{\mathcal R_{N;N}>0.}
\tag{15.7}
$$



These signs use the canonical relation $E_K=-eU-I_K$. They do not hold merely because a pair of arbitrary affine recurrence states satisfies the same recurrence.

### 15.4 Return-height bounds

For $r=N-1$,


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
<36^NN!.
\end{aligned}
$$


For $r=N$, its positivity permits dropping the subtracted positive term:


$$
\frac{\mathcal R_{N;N}}{d_K}
<UI_N^{\mathrm H}
<
\frac{150}{2N+1}36^{N-3}N!
<36^NN!.
$$



Thus


$$
\boxed{
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
\qquad
|\mathcal R_{N-1;N}|,\ |\mathcal R_{N;N}|
<d_K36^NN!.
}
\tag{15.8}
$$


Both Hermite polynomials have degree at most $2N$. No terminal is enlarged.

---

## 16. The $83$-branch: endpoint removal only

The modular powers


$$
9^2\equiv-2,\quad 9^4\equiv4,\quad
9^8\equiv16,\quad9^{16}\equiv7,\quad9^{32}\equiv49
\pmod{83}
$$


give


$$
9^{21}\equiv3,\qquad9^{41}\equiv1.
$$


The order is $41$. Therefore


$$
83\mid\ell
\iff18+32u\equiv21\pmod{41}
\iff u\equiv27\pmod{41}.
$$



On this branch, the two centered row coefficients vanish modulo $83$, and


$$
16E_K\equiv-14448\equiv-6\pmod{83},
$$


so $E_K\equiv10\pmod{83}$.

At $x\equiv0\pmod{83}$, the raw arc denominator is a unit, and


$$
R_K\equiv\frac{13}{15}\equiv23\pmod{83}.
$$


Thus


$$
y_K/d_K=E_K-R_K\equiv-13\ne0\pmod{83}.
$$


Hence


$$
\boxed{
u\equiv27\pmod{41}\Longrightarrow83\nmid y_K.
}
\tag{16.1}
$$



In fact, the source constant satisfies $5312=64\cdot83$, so the same collapsed centered row gives $83\mid U$, not a source unit. This reinforces the limitation:


$$
\boxed{v_{83}(\mathfrak J^0)=v_{83}(c)}
$$


on this branch, with no upper bound here on that remaining source/Gaussian common depth.

---

## 17. Every exceptional division and the exact numerical gcd

### 17.1 Binary payment in the original objects

Since $m=N-3$ is even, $C_m^2\equiv1\pmod{16}$ coefficientwise. To check this, write $m=2h$. The recurrence gives $C_h\equiv1\pmod2$, so


$$
C_h^2\equiv1\pmod4,
\qquad
C_{2h}=2C_h^2-1\equiv1\pmod8,
$$


and squaring gives the assertion.

Therefore


$$
E_K\equiv E(\mathcal H)=-903\equiv1\pmod8,
$$




$$
U\equiv-\eta(\mathcal H)=332\equiv12\pmod{16}.
$$


Thus


$$
\boxed{v_2(U)=2.}
\tag{17.1}
$$



Here $\ell$ is divisible by $4$, so $x\equiv0\pmod{16}$. The raw arc numerator and denominator both have binary valuation $1$, and


$$
A_K(x)/2\equiv-2925\equiv3\pmod8,
$$




$$
30L(x)/2=15L(x)\equiv1\pmod8.
$$


The reduced $d_K$ is odd and


$$
R_K\equiv3\pmod8.
$$


Consequently,


$$
y_K/d_K=E_K-R_K\equiv6\pmod8,
$$


and


$$
\boxed{v_2(y_K)=1.}
\tag{17.2}
$$



As a direct local consequence, for every $0\le r\le N$,


$$
\boxed{v_2(\mathcal R_{r;N})=1,}
\tag{17.3}
$$


because its two summands have binary valuations $2$ and $1$, respectively.

This is a useful exact local consequence, not an all-prime source-capture result.

### 17.2 Paying all primes dividing $d_K$

Let


$$
H_N=\gcd(U,y_K).
$$


Because $\gcd(d_K,y_K)=1$,


$$
\gcd(d_KU,y_K)=H_N.
$$


Set


$$
a=\frac{d_KU}{H_N},\qquad
b=\frac{y_K}{H_N}.
$$


Then $\gcd(a,b)=1$, and


$$
\frac{\mathcal R_{r;N}}{H_N}
=P_r^{\mathrm H}a+Q_r^{\mathrm H}b.
$$


By the adjacent determinant (13.2), any common divisor of two adjacent normalized returns divides $2a$ and $2b$, hence divides $2$.

But (17.1)–(17.2) give $v_2(H_N)=1$, so $a$ is even and $b$ odd. All $P_r^{\mathrm H},Q_r^{\mathrm H}$ are odd. Both normalized returns are therefore odd, and their gcd is $1$.

Thus


$$
\boxed{
\gcd(U,y_K)
=\gcd(\mathcal R_{N-1;N},\mathcal R_{N;N}).
}
\tag{17.4}
$$


In particular,


$$
\boxed{
\gcd(U,y_K)
<d_K36^NN!
<\frac{64}{3}N^6\,36^NN!.
}
\tag{17.5}
$$



No denominator prime was silently inverted: its removal followed from the actual reduced arc. No prime dividing $g_B$, $\delta$, or a source determinant was inverted.

---

## 18. Exact intrinsic factorization after actual source-content removal

Define


$$
\mathfrak J^0=\gcd(U,Vy_K).
$$


Because $U=c\tau$, $V=c\nu$, and $\gcd(\tau,\nu)=1$,


$$
\boxed{\mathfrak J^0=c\gcd(\tau,y_K).}
\tag{18.1}
$$



For either adjacent Hermite index, put


$$
s_r=\gcd(c,Q_r^{\mathrm H}),
\qquad
\mathcal T_r=\frac{\mathcal R_{r;N}}{s_r}.
$$


The division is integral: $s_r\mid c\mid U$ and $s_r\mid Q_r^{\mathrm H}$. Explicitly,


$$
\boxed{
\mathcal T_r
=d_K\frac c{s_r}P_r^{\mathrm H}\tau
+\frac{Q_r^{\mathrm H}}{s_r}y_K.
}
\tag{18.2}
$$



The two integers


$$
Q_{N-1}^{\mathrm H}/s_{N-1},
\qquad Q_N^{\mathrm H}/s_N
$$


are coprime because they divide coprime adjacent Hermite denominators. Reducing (18.2) modulo $\tau$ and taking an integer Bézout combination proves


$$
\gcd(\tau,\mathcal T_{N-1},\mathcal T_N)
=\gcd(\tau,y_K).
$$


Therefore


$$
\boxed{
\mathfrak J^0
=c\gcd\!\left(
\frac Uc,
\frac{\mathcal R_{N-1;N}}{\gcd(c,Q_{N-1}^{\mathrm H})},
\frac{\mathcal R_{N;N}}{\gcd(c,Q_N^{\mathrm H})}
\right).
}
\tag{18.3}
$$



Since both returns are nonzero,


$$
\boxed{
\mathfrak J^0
<
d_K36^NN!\,
\frac c{\max(s_{N-1},s_N)}.
}
\tag{18.4}
$$



There is also a genuine numerical certificate in the required generators. If


$$
a_0U+b_0V=c,
$$


then for $s=s_r$,


$$
\boxed{
\frac cs\mathcal R_{r;N}
=
\left(d_KP_r^{\mathrm H}\frac cs
+a_0\frac{Q_r^{\mathrm H}}s\,y_K\right)U
+b_0\frac{Q_r^{\mathrm H}}s\,Vy_K.
}
\tag{18.5}
$$


All coefficients are integers, and the left side is a nonzero, explicitly bounded integer. Its unremoved factor $c/s$ is exactly the outstanding payment.

---

## 19. Preservation of the complete original source and endpoint interface

The new return does not replace the old finite columns.

Put $n=2N$. Retain the thirteen weights


$$
(w_0,\ldots,w_{12})
=(1,8,58,168,399,-176,-916,-176,399,168,58,8,1).
$$


The local backward evaluator has initial data


$$
r_0=1,\ r_1=0,\qquad
s_0=0,\ s_1=1,\qquad
\kappa_0=\kappa_1=\omega_0=\omega_1=0,
$$


and


$$
r_{k+1}=r_{k-1}+4(n-k)r_k,\qquad
s_{k+1}=s_{k-1}+4(n-k)s_k,
$$




$$
\kappa_{k+1}=\kappa_{k-1}+4(n-k)\kappa_k-2,
$$




$$
\omega_{k+1}=\omega_{k-1}+4(n-k)\omega_k-2(-1)^k,
\qquad1\le k\le11.
$$


Thus the complete constants remain


$$
\mathsf C_U=679936-\sum_{k=0}^{12}w_k(n-k)\kappa_k,
$$




$$
\mathsf C_E=-1849344+\sum_{k=0}^{12}w_k(n-k)\omega_k,
$$


with


$$
4096U=\mathsf C_U-\mathsf A\Theta_n-\mathsf B\Theta_{n-1},
$$




$$
4096E_K=\mathsf A\Phi_n+\mathsf B\Phi_{n-1}+\mathsf C_E.
$$



The divided square columns remain


$$
V=\mathsf C_V-\mathsf P\Theta_n-\mathsf Q\Theta_{n-1},
$$




$$
E_F=\mathsf C_F^E-\mathsf P\Phi_n-\mathsf Q\Phi_{n-1},
$$


where


$$
\mathsf P=n\alpha^2+(n-2)\beta^2,
$$




$$
\mathsf Q=4(n-1)(n-2)\beta^2-2(n-1)\alpha\beta,
$$




$$
\boxed{
\mathsf C_V=\alpha^2+(2n-3)\beta^2-\delta^2,
\quad
\mathsf C_F^E=\alpha^2+(5-2n)\beta^2+4\alpha\beta.
}
\tag{19.1}
$$



These constants can be checked directly from


$$
F^2
=\frac{\alpha^2}{2}(C_n+1)
+\frac{\beta^2}{2}(C_{n-2}+1)
-\alpha\beta(C_{n-1}+C_1),
$$


using the two different forcings in (14.1). In particular, the terms $-\delta^2$ and $4\alpha\beta$ are necessary.

For


$$
\Delta=\mathsf A\mathsf Q-\mathsf B\mathsf P,
$$


the retained source return is


$$
z_n=4096\mathsf Q U-\mathsf B V,\qquad
z_{n-1}=\mathsf A V-4096\mathsf P U,
$$




$$
z_j=-\Delta\Theta_j+r_j,\qquad
z_{j-1}=z_{j+1}+4jz_j,
$$




$$
r_{j-1}=r_{j+1}+4jr_j-2\Delta,
$$


with terminal forcing values


$$
r_n=\mathsf Q\mathsf C_U-\mathsf B\mathsf C_V,
\quad
r_{n-1}=\mathsf A\mathsf C_V-\mathsf P\mathsf C_U.
$$



The endpoint return retains


$$
k_E=D\mathsf C_E-4096DR_K,\qquad
f_E=D\mathsf C_F^E-DR_F,
$$




$$
w_n=4096\mathsf QY+\mathsf B X,
\quad
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
w_{j-1}=w_{j+1}+4jw_j,
$$




$$
\sigma_{j-1}=\sigma_{j+1}+4j\sigma_j+2D\Delta(-1)^j.
$$


Its exact determinant is


$$
\boxed{
z_nw_{n-1}-z_{n-1}w_n
=-4096\Delta(UX+VY).
}
\tag{19.2}
$$


No division by $\Delta$ is made.

Finally, the complete square arc remains


$$
R_F=\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
-2\alpha\beta\xi_{n-1}}2,
$$


where


$$
\xi_{j+1}=4\upsilon_j-2\xi_j-\xi_{j-1}+16b_j,
$$




$$
\upsilon_{j+1}
=-4\xi_j-2\upsilon_j-\upsilon_{j-1}+16(\ell_j-a_j),
$$




$$
\ell_j=
\begin{cases}
0,&j\ \text{odd},\\
(1-j^2)^{-1},&j\ \text{even},
\end{cases}
$$


and the values at $j=0,1$ are zero. The piecewise definition avoids an invalid substitution at $j=1$.

These identities are retained, not regenerated as closed macro calculations.

---

## 20. Why the endpoint theorem does not prove source capture

The numerical endpoint theorem gives


$$
\gcd(\tau,y_K)\le\gcd(U,y_K)\le N!e^{O(N)}.
$$


Combining this only with the established bound


$$
\log c\le N\log N+O(N)
$$


yields


$$
\log\mathfrak J^0\le2N\log N+O(N),
$$


the same leading scale as $\log U$.

There is no strict saving from this argument.

Moreover,


$$
|\mathcal R_{r;N}|\le N!e^{O(N)}
$$


does not imply that $N!$ divides the return, or that its excess prime powers over $N!$ have exponential size. In particular, a prime $p>N$ has zero $N!$-allowance.

Thus the factorial-excess target


$$
\frac{\mathfrak J^0}{\gcd(\mathfrak J^0,N!)}\le e^{CN}
$$


remains unproved.

The exact obstruction in (18.4) is


$$
\frac c{\max\{\gcd(c,Q_{N-1}^{\mathrm H}),
                 \gcd(c,Q_N^{\mathrm H})\}}.
$$


Coprimality of the two Hermite denominators does not force a prime dividing the actual $c$ to divide either denominator.

---

## 21. HC: open lemma and fully checked conditional consequence

The concrete source-capture target is


$$
\boxed{
\frac{c_N}
{\gcd(c_N,Q_{N-1}^{\mathrm H}Q_N^{\mathrm H})}
\le e^{CN}.
}
\tag{HC}
$$


This is an assertion about the actual divided Gaussian source column $V_N$, all primes, and all depths on the unchanged original indices.

Since adjacent $Q^{\mathrm H}$'s are coprime,


$$
\gcd(c,Q_{N-1}^{\mathrm H}Q_N^{\mathrm H})=s_{N-1}s_N.
$$


If HC holds, then


$$
\max(s_{N-1},s_N)\ge\sqrt c\,e^{-CN/2}.
$$


Substitution in (18.4) gives


$$
\mathfrak J^0
\le d_K36^NN!\sqrt c\,e^{CN/2}.
$$


Using the established source-content bound,


$$
\log\mathfrak J^0
\le\frac32N\log N+O(N)
=\frac34\log U+O(N).
$$


Therefore


$$
\boxed{
\mathrm{HC}\Longrightarrow
\mathfrak J^0\le e^{O(N)}U^{3/4}.
}
\tag{21.1}
$$



A concrete sufficient follow-on lemma is an evaluated original-source identity


$$
a_NU_N+b_NV_N
=Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}B_N,
\qquad
0<|B_N|\le e^{CN}.
\tag{21.2}
$$


Indeed, $c_N$ divides its right side, so prime by prime


$$
\frac{c_N}
{\gcd(c_N,Q_{N-1}^{\mathrm H}Q_N^{\mathrm H})}
\mid B_N.
$$


The coefficients and the bounded nonzero $B_N$ must be obtained from the canonical boundary data and the actual paid $\alpha,\beta,\delta$. Merely naming a Bézout quotient does not establish (21.2).

No proof or original-family disproof of HC is supplied here.

---

## 22. Conditional effect on the actual denominator and whole error

Define


$$
\mathfrak J=\gcd(U,VY).
$$


Since $Y=\mu y_K$,


$$
\boxed{\mathfrak J^0\mid\mathfrak J\mid\mu\mathfrak J^0,}
\qquad
\mathfrak J=c\gcd(\tau,Y).
\tag{22.1}
$$



The actual denominator satisfies


$$
\boxed{\frac U{\mathfrak J}\mid q.}
\tag{22.2}
$$


For verification, at a prime with $v_p(\tau)>v_p(Y)$, coprimality of $\tau,\nu$ gives


$$
v_p(\tau X+\nu Y)=v_p(Y).
$$


Reduction of the actual fraction with denominator $D\tau\delta^2$ leaves at least


$$
v_p(\tau)-v_p(Y)
$$


powers of $p$ in $q$. This proves (22.2), including primes dividing $D,\delta$, or the previously paid Gaussian data.

The original normalized polynomial is


$$
P_N(t)=\frac{F(t)^2+(V/U)K(t)}{\delta^2}
=\frac{W_{\rm prim}(t)}M.
$$


It satisfies $\eta(P_N)=1$ and $P_N(\pm i)=1$. Consequently,


$$
\epsilon_N
=\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0,
$$


and


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0.
}
\tag{22.3}
$$



The complete rational enclosure remains


$$
3J_N<\epsilon_N<7J_N,
$$




$$
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
q_NJ_N=\frac{\lambda_N}{G_N}
(\tau_NJ_F+\nu_NJ_K).
\tag{22.4}
$$


Neither positive contribution is discarded.

If HC holds, (21.1), (22.1), (22.2), and $\mu\le D<256^N$ give


$$
q_N\ge e^{-O(N)}U_N^{1/4}.
$$


Using the established


$$
\epsilon_N\asymp R^{-2N},
\qquad
R=1+\sqrt2+\sqrt{2+2\sqrt2},
$$


one obtains


$$
\boxed{
\log(q_N\epsilon_N)
\ge\frac12N\log N-O(N)\longrightarrow+\infty.
}
\tag{22.5}
$$



This is a correct conditional conclusion about


$$
q_N=\frac{\lambda_NM_N}{G_N}
$$


after actual content removal, least aggregate clearing, and the final all-prime gcd. It would retire this signed producer as a source of primitive whole-error decay. It would not prove $e+\pi$ rational.

Because HC is open, this producer is not retired by the present report.

---

## 23. Separate binary producer and deferred task

No compact or signed conclusion is transferred to the separate binary producer. Its retained data are


$$
b=9^{18+32u},\qquad n=4002b,\qquad
0\le j<b,\qquad z_b=0,
$$




$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0,
$$


and the complete return


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


Only the established paid estimate


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1},
$$


is retained.

Its $Q=x_0^Tx_0$, actual corrected-column contents, least simultaneous clearer, final all-prime gcd, and actual primitive denominator remain separate and unchanged. The actual $b/\mathrm{first4}$ return evaluation remains open.

---

## 24. Bounded exact arithmetic: what is and is not needed

No new finite computation is required for either proof verdict.

The completed $Y_{27}$ full-cofactor check is not to be rerun. No original-size factorial matrix, Gaussian recurrence, capped spectrum, old source sample, or closed macro table is requested.

If an additional short implementation receipt for the new Hermite normalization is desired, the following is sufficient and bounded.

### Inputs

- $r=0,1,2,3,4$;
- factorials only through $8!$;
- $f_r(t)=t^r(1-t)^r/r!$;
- $a_{r,j}=(r+j)!/[j!(r-j)!]$;
- the formal symbols in the two linear identities (14.2).

### Expected verifiable outputs

The coefficient arrays of $\sum_j a_{r,j}z^j$ are


$$
(1),\quad
(1,2),\quad
(1,6,12),\quad
(1,12,60,120),\quad
(1,20,180,840,1680).
$$


The endpoint pairs are


$$
\boxed{
(1,1),\ (3,1),\ (19,7),\ (193,71),\ (2721,1001).
}
$$


The adjacent determinant outputs are


$$
2,-2,2,-2.
$$


Exact polynomial evaluation must give


$$
E(f_r)=(-1)^rP_r^{\mathrm H},
\qquad
\eta(f_r)=(-1)^rQ_r^{\mathrm H},
$$




$$
\int_0^1f_r(t)\,dt=\frac{r!}{(2r+1)!}.
$$


Formal substitution in $16(d_KPU+Qy_K)$ must give exactly (14.5), with zero residual.

This optional check would establish only those finite arithmetic identities. It would not test HC, the changing actual source content, all-prime factorial excess, producer retirement, or irrationality.

---

## 25. Final proof-status ledger and remaining mathematical bottlenecks

| Statement | Status after this audit |
|---|---|
| Both designated original $Y_k$ cofactor valuations equal $E_k$ | **Proved and independently audited** |
| $v_3(\mathscr L_k)=v_3(\mathscr R_k)=E_k$ on all original indices | **Proved and independently audited** |
| Complete forcing and cross terms in the all-depth Schur matrix | **Retained and checked** |
| Literal $Z_k$ contact atom | **Retained; supplies an essential unit** |
| Exact final compact $v_3(G_k)$ | **Not determined; only the range (8.4)** |
| Other odd-prime compact descent | **Open** |
| Useful direct actual $v_2(G_k)$ upper bound | **Open** |
| Two canonical numerical Hermite returns, signs, and heights | **Proved and independently audited** |
| Exact numerical endpoint gcd equality | **Proved at all primes** |
| Exact intrinsic $s_r$-factorization | **Proved at all primes and depths** |
| Centered coefficient-content theorem’s external audit | **Still pending; not a premise for the direct numerical return** |
| HC source capture | **Open** |
| All-prime factorial-excess estimate | **Open** |
| HC $\Rightarrow U^{3/4}e^{O(N)}$ intrinsic bound | **Correct conditional implication** |
| HC $\Rightarrow$ divergence of the actual signed whole error | **Correct conditional implication** |
| Deferred A3 $b/\mathrm{first4}$ evaluation | **Open and unevaluated** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

### Final conclusion

The completed new work is a full independent verification of two uniform original-family results:



$$
\boxed{
v_3(M_k^{(0)})
=v_3(M_k^{(k-1)})
=v_3(\mathscr L_k)
=v_3(\mathscr R_k)
=\frac{(k-2)(k-1-2s)}2,
}
$$


and


$$
\boxed{
\gcd(U_N,y_{K,N})
=\gcd(\mathcal R_{N-1;N},\mathcal R_{N;N}),
\quad
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
}
$$


with the fully paid height and intrinsic-factorization formulas above.

The compact bottleneck is now outside the rectangle $3$-part: other odd primes, useful actual binary control, and the final all-prime gcd in the whole error.

The signed bottleneck is the arithmetic synchronization of the actual source content $c_N$ with the adjacent Hermite denominators and the reduced numerical returns. The return theorem reaches the critical factorial scale; it does not by itself provide a strict saving. HC is a precise sufficient follow-on lemma, not a proved conclusion.

Finally, an irrationality proof would require, for some rigorously controlled integer approximants at infinitely many unchanged original indices,


$$
0<|q_N(e+\pi)-p_N|\longrightarrow0.
$$


If $e+\pi=a/b$ were rational, every such nonzero integer linear form would have absolute value at least $1/b$. Neither audited producer has yet been shown to meet this decay condition after its actual least clearers, actual contents, final all-prime gcd, and actual primitive denominator have all been paid.
