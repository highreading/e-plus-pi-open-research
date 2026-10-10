> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A paid high-depth $3$-adic factorization of the original contact–forcing cofactors

## 1. Main outcome

The rationality or irrationality of $e+\pi$ remains unresolved.

The primary cofactor obligation in this assignment, however, has an affirmative answer. In fact, both specified cofactors have the same explicitly evaluated $3$-adic valuation.

Let


$$
k=3^s,\qquad d=k-1,
$$


and define


$$
E_k=2\sum_{j=0}^{k-2}v_3(j!).
$$


For the two original maximal minors of $Y_k$ obtained by omitting the first or last contact-return column, while retaining **all $k$ original scaled forcing columns**, the result is


$$
\boxed{
v_3\!\left(M_k^{(0)}\right)
=
v_3\!\left(M_k^{(k-1)}\right)
=
E_k
=
\frac{(k-2)(k-1-2s)}2.
}
\tag{1.1}
$$



Consequently, at every unchanged original index


$$
k=K_u=9^{18+32u}=3^{36+64u},
$$




$$
\boxed{
\min\!\left(v_3(M_k^{(0)}),v_3(M_k^{(k-1)})\right)
\le k^2+(2-s)k.
}
\tag{1.2}
$$


The exact margin is


$$
\boxed{
k^2+(2-s)k-E_k
=
\frac{k^2+7k-2-4s}{2}>0.
}
\tag{1.3}
$$



The proof does **not** extend the earlier row-scalar periodic Schur reduction beyond its valid depth. Instead, it establishes a saturated contact-row basis after paying the full factorial-square divisor. That basis permits a different Schur elimination whose remaining forcing determinant is a unit at $3$. The complete factorial forcing and all cross-residue terms remain in that determinant.

There are two further consequences.

1. For the actual original contents,
   

$$
\boxed{
   v_3(\mathscr L_k)=v_3(\mathscr R_k)=E_k
   }
   \tag{1.4}
$$


   at all original indices. For $Z_k$, an explicit original maximal minor—its first $2k-1$ rows—attains this valuation.

2. A secondary, rigorous improvement of the **actual binary upper bound** follows from the established all-prime contact divisors and original-content size bound. It gives
   

$$
\boxed{
   v_2(\mathscr L_k),\,v_2(\mathscr R_k)
   \le
   \left\lfloor
   \log_2\frac{\mathcal U_k}
   {\left(\prod_{j=0}^{k-2}\operatorname{odd}(j!)\right)^2}
   \right\rfloor.
   }
   \tag{1.5}
$$


   Its leading coefficient improves the previously stated size-derived binary bound from $4/\log2$ to $3/\log2$. It is still of order $k^2\log k$, not the useful $O(k^2)$ bound.

No simultaneous odd-prime Bézout certificate is constructed. The final all-prime gcd, actual primitive denominator, and complete nonzero whole error remain essential.

---

## 2. Original objects and source scope

### 2.1 The unchanged arrays

Retain


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad w_n=(-1)^n,
\qquad c_n=u_n-w_n,
$$


and


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
\boxed{
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{2.1}
$$



Put


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),
\qquad T_n=\Lambda_k\tau_n.
$$


Thus


$$
\boxed{
T_n
=
-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1}
}
\tag{2.2}
$$


is an integer at every original return index.

The rectangles are exactly


$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{0\le m<2k-1\\0\le j<k}}
\ \middle|\
(T_{m+j})_{\substack{0\le m<2k-1\\0\le j<k}}
\right],
\tag{2.3}
$$


and


$$
Z_k=
\left[
(c_{m+j})_{\substack{0\le m<2k\\0\le j<k}}
\ \middle|\
(T_{m+j})_{\substack{0\le m<2k\\0\le j<k-1}}
\right].
\tag{2.4}
$$



Their actual maximal-minor contents are


$$
\mathscr L_k=\delta_{2k-1}(Y_k),
\qquad
\mathscr R_k=\delta_{2k-1}(Z_k).
$$



The physical terminal is unchanged:


$$
\boxed{
\text{moment }3k-2,\qquad
(6k-4)!,\qquad
\text{last odd denominator }6k-5.
}
\tag{2.5}
$$


The largest return index remains $3k-3$.

For definiteness, the two $Y_k$ minors below are ordinary determinants in inherited column order. A conventional signed-cofactor orientation does not affect any valuation statement.

### 2.2 What is reused

The following established results are reused at their stated scope.

* Every $d$-minor of a finite contact-return block $(\sigma_{m+j})$ is divisible by
  

$$
\mathcal A_d
  =
  2^{d^2}\left(\prod_{j=0}^{d-1}j!\right)^2.
  \tag{2.6}
$$


* Every $d$-minor of a finite contact block $(c_{m+j})$, with the atom retained, is divisible by
  

$$
\mathcal B_d
  =
  2^{d(d-1)}
  \left(\prod_{j=0}^{d-2}j!\right)^2.
  \tag{2.7}
$$


* The integral weighted certificate
  

$$
\mathcal W_k
  =
  (2^{15}3^2\Lambda_k)^k
  \left(\prod_{j=0}^{k-1}j!\right)^4
$$


  does **not** belong to $I_{2k-1}(Y_k)$ for $k\ge18$. That disproof is not reattempted.
* The original-content size bound $\mathscr R_k,\mathscr L_k\le\mathcal U_k$, the exact finite-jet transfers, and the bordered-content relations are retained with their original hypotheses.

The supplied $k=81$, modulo-$27$ receipt is a completed finite audit of the capped local theorem. It is not a computation of full content. It is neither repeated nor used as a premise for the new high-depth proof.

The earlier capped theorem remains scoped by $2h\le s+2$. Nothing below asserts that its row-scalar reduction remains valid at larger depths.

---

## 3. A normalized contact calculation at $3$

The crucial new input is an evaluated congruence **after** the factorial payments, not a deeper congruence of the raw rows.

Let $\Delta y_n=y_{n+1}-y_n$, and set


$$
D_r=2^r r!.
$$



### 3.1 Integral normalized differences

The finite polynomial-moment identity


$$
a_n=\int_0^\infty e^{-t}(1-t)^n\,dt
\tag{3.1}
$$


follows by integration by parts from the original recurrence. Thus


$$
u_n=\int_0^\infty e^{-t}(t-1)^{2n}\,dt.
$$


Taking $r$ finite differences multiplies the integrand by


$$
\bigl((t-1)^2-1\bigr)^r=t^r(t-2)^r.
$$



The established divisibilities are


$$
2^r r!\mid \Delta^r u_n,
\qquad
2^{r+1}r!\mid \Delta^r\sigma_n.
\tag{3.2}
$$


For completeness, their factorial payment is explicit: expansion of $t^r(t-2)^r$ gives terms whose required quotient contains


$$
\frac{\binom rh 2^{r-h}(r+h)!}{2^r r!}
=
\binom{r+h}{2h}(2h-1)!!\in\mathbb Z.
\tag{3.3}
$$


The second assertion follows from $\sigma_n=2u_n+\Delta u_n$.

Define the integers


$$
\eta_n^{(\alpha)}
=
\frac{\Delta^n\sigma_\alpha}{2^{n+1}n!},
\qquad \alpha=0,1.
\tag{3.4}
$$



### 3.2 Evaluation of $\eta_n^{(0)}\pmod3$

Put


$$
d_n=\frac{\Delta^n u_0}{2^n n!}.
$$


Direct expansion gives the finite integer formula


$$
d_n
=
\sum_{h=0}^n
(-1)^{n-h}
\binom{n+h}{2h}(2h-1)!!.
\tag{3.5}
$$


For $h\ge2$, the odd double factorial contains a factor $3$. Consequently


$$
d_n
\equiv
(-1)^n\left(1-\binom{n+1}{2}\right)
\pmod3.
\tag{3.6}
$$



Since


$$
\eta_n^{(0)}=d_n+(n+1)d_{n+1},
$$


substitution yields


$$
\begin{aligned}
\eta_n^{(0)}
&\equiv
(-1)^n
\left[
1-\binom{n+1}{2}
-(n+1)\left(1-\binom{n+2}{2}\right)
\right]\\
&=
(-1)^n
\left[1+\frac{n(n+1)(n+2)}2\right]
\pmod3.
\end{aligned}
$$


The product of three consecutive integers, divided by $2$, is a multiple of $3$. Therefore


$$
\boxed{
\eta_n^{(0)}\equiv(-1)^n\pmod3
\qquad(n\ge0).
}
\tag{3.7}
$$



For the shifted contact-return sequence,


$$
\Delta^n\sigma_1
=
\Delta^n\sigma_0+\Delta^{n+1}\sigma_0.
$$


Hence


$$
\eta_n^{(1)}
=
\eta_n^{(0)}+2(n+1)\eta_{n+1}^{(0)},
$$


and so


$$
\boxed{
\eta_n^{(1)}
\equiv(-1)^n(n-1)\pmod3.
}
\tag{3.8}
$$



These congruences are the new evaluated normalized contact input.

---

## 4. The two normalized contact determinants are units

For $\alpha=0,1$, define the finite integral matrix


$$
B^{(\alpha)}_{rc}
=
\binom{r+c}{r}\eta_{r+c}^{(\alpha)}.
\tag{4.1}
$$



The finite double-Newton identity gives


$$
(\sigma_{m+j+\alpha})
=
2P_{\rm row}D_{\rm row}
B^{(\alpha)}
D_{\rm col}P_{\rm col}^{\,T},
\tag{4.2}
$$


where $P$ is the appropriate finite Pascal matrix and $D_{rr}=2^r r!$.

This identity also explains the all-minor divisor $\mathcal A_d$: Cauchy–Binet supplies $d$ distinct entries of each diagonal $D$, and


$$
D_i\mid D_{i+1}.
$$


Thus every $d$-minor contains


$$
2^d\left(\prod_{i=0}^{d-1}D_i\right)^2
=
\mathcal A_d.
$$



### 4.1 Unshifted contact return

Let $B_d^{(0)}$ be the leading $d\times d$ block. By (3.7),


$$
B_d^{(0)}
\equiv
\left((-1)^{r+c}\binom{r+c}{r}\right)_{r,c<d}
\pmod3.
$$


The elementary identity


$$
\binom{r+c}{r}
=
\sum_h\binom rh\binom ch
$$


gives a factorization $PP^T$, with $P$ unit lower triangular. The row and column signs have total determinant $1$. Therefore


$$
\boxed{
\det B_d^{(0)}\equiv1\pmod3
\qquad(d\ge1).
}
\tag{4.3}
$$



### 4.2 Once-shifted contact return

By (3.8), after removing row and column signs,


$$
B_d^{(1)}
\equiv
N_d
:=
\left((r+c-1)\binom{r+c}{r}\right)_{r,c<d}
\pmod3.
\tag{4.4}
$$



Let


$$
J=\operatorname{diag}(0,1,\ldots,d-1),
$$


and let $S$ have subdiagonal entries $S_{i,i-1}=i$. The finite Pascal identity


$$
P^{-1}JP=J+S
$$


implies


$$
N_d=P(2J-I+S+S^T)P^T.
\tag{4.5}
$$


Thus its determinant is the determinant of a fully evaluated tridiagonal matrix with diagonal $2i-1$ and adjacent off-diagonal entries $i+1$.

Write that determinant as $D_d^\ast$. Its exact recurrence is


$$
D_0^\ast=1,\qquad D_1^\ast=-1,
$$




$$
D_{n+1}^\ast=(2n-1)D_n^\ast-n^2D_{n-1}^\ast.
\tag{4.6}
$$


Reduction of this recurrence modulo $3$ gives


$$
D_{3q}^\ast=1,\qquad
D_{3q+1}^\ast=-1,\qquad
D_{3q+2}^\ast=1
\pmod3.
\tag{4.7}
$$


Indeed, a block of three recurrence steps sends


$$
D_{3q}^\ast
\longmapsto -D_{3q}^\ast
\longmapsto D_{3q}^\ast
\longmapsto D_{3q}^\ast.
$$



In particular, when $d=k-1$ and $3\mid k$,


$$
\boxed{
\det B_d^{(1)}\equiv1\pmod3.
}
\tag{4.8}
$$



No determinant has been left as an unevaluated nonvanishing assumption: the two necessary normalized determinants have been evaluated modulo $3$.

---

## 5. A saturated contact-row basis at the full factorial depth

This is the step that replaces the capped row-scalar argument.

### Lemma 5.1 — normalized minor residue dependence

Let


$$
k=3^s,\qquad s\ge1,\qquad d=k-1,
$$


and let $\alpha=0$ or $1$. For any $d$ nonnegative row indices $m_0,\ldots,m_{d-1}$, the integer


$$
\frac{
\det(\sigma_{m_i+c+\alpha})_{i,c<d}
}{\mathcal A_d}
\tag{5.1}
$$


has a residue modulo $3$ depending only on the ordered residues $m_i\bmod k$.

If those residues, in order, are $0,1,\ldots,k-2$, then


$$
\boxed{
\frac{
\det(\sigma_{m_i+c+\alpha})_{i,c<d}
}{\mathcal A_d}
\equiv1\pmod3.
}
\tag{5.2}
$$



#### Proof

Use a finite row range containing all $m_i$, and apply (4.2). Since the contact columns are consecutive, the column Pascal determinant is $1$. Cauchy–Binet gives the exact finite identity


$$
\frac{\det(\sigma_{m_i+c+\alpha})}{\mathcal A_d}
=
\sum_{\substack{R=\{r_0<\cdots<r_{d-1}\}}}
\det\!\left(\binom{m_i}{r_j}\right)
\frac{\prod_{r\in R}D_r}{\prod_{j=0}^{d-1}D_j}
\det B^{(\alpha)}[R,0,\ldots,d-1].
\tag{5.3}
$$


Every displayed diagonal quotient is an integer because $r_j\ge j$ and $D_j\mid D_{r_j}$.

If $R$ contains an index at least $k$, then its largest index is at least $k$, whereas the largest denominator index is $k-2$. Thus that quotient has $3$-adic valuation at least


$$
v_3(k!)-v_3((k-2)!)=s\ge1.
\tag{5.4}
$$


Such terms vanish modulo $3$.

For every remaining term, all $r_j<k$. The freshman’s-dream identity


$$
(1+x)^k\equiv1+x^k\pmod3
$$


shows that, for $r<k$,


$$
\binom{m+k}{r}\equiv\binom mr\pmod3.
\tag{5.5}
$$


This proves the asserted residue dependence.

Now suppose $m_i\equiv i\pmod k$, $0\le i\le k-2$. Any surviving row-index set other than


$$
R_0=\{0,1,\ldots,k-2\}
$$


contains $k-1$. Its Pascal determinant is zero modulo $3$, because


$$
\binom{m_i}{k-1}\equiv\binom{i}{k-1}=0.
$$


For $R_0$, the Pascal determinant is $1$, the diagonal quotient is $1$, and the final determinant is $1$ by (4.3) or (4.8). This proves (5.2). ∎

### Corollary 5.2 — all contact interpolation divisions are paid at $3$

Let


$$
C_F=(\sigma_{m+c+\alpha})_{\substack{m\in F\\0\le c<d}},
$$


where $F$ has ordered residues $0,\ldots,k-2$ modulo $k$. Then


$$
\det C_F=\mathcal A_d\,b,\qquad b\in\mathbb Z,\quad b\equiv1\pmod3.
\tag{5.6}
$$


For any other physical contact row $C(m)$,


$$
C(m)C_F^{-1}\in\mathbb Z_{(3)}^d.
\tag{5.7}
$$



To check the division, each Cramer numerator is a contact $d$-minor and therefore is divisible by $\mathcal A_d$. After canceling that proved integer divisor, the only remaining denominator is $b$, a unit at $3$.

Moreover, if $m\equiv m_i\pmod k$ for one of the chosen rows, then


$$
\boxed{
C(m)C_F^{-1}\equiv e_i^T\pmod3.
}
\tag{5.8}
$$


This follows from Lemma 5.1 applied to the row-replacement determinants.

The denominator $b$ can have other prime divisors. This is a $3$-local interpolation statement, not a dyadic one.

---

## 6. Paid unit Schur evaluation of both original $Y_k$ cofactors

### 6.1 Physical row sets and complete forcing

Let


$$
k=3^s,\qquad
t=\frac{k-1}{2},\qquad
n_0=\frac{3k-1}{2}=3t+1.
$$


Use the $k$ original pivot rows, in the indicated order,


$$
P=(n_0,n_0-1,\ldots,n_0-k+1).
\tag{6.1}
$$


The remaining $d=k-1$ rows of $Y_k$, in increasing order, are


$$
F=
\{0,\ldots,t\}
\;\cup\;
\{3t+2,\ldots,4t\}.
\tag{6.2}
$$


Their residues modulo $k=2t+1$, in this order, are exactly


$$
0,1,\ldots,k-2.
\tag{6.3}
$$



The physical denominator range gives


$$
v_3(\Lambda_k)=s+1.
\tag{6.4}
$$


Set


$$
\gamma=\frac{4\Lambda_k}{3k}\in\mathbb Z,
\qquad 3\nmid\gamma.
\tag{6.5}
$$



Reduction of the **complete integer** entry (2.2) modulo $3$ gives


$$
T_n\equiv
\gamma\,\mathbf1_{n=n_0}\pmod3.
\tag{6.6}
$$


Here:

* the factorial term is a multiple of $\Lambda_k$, hence of $3$;
* among the physical odd denominators $1,\ldots,6k-5$, the only one with $3$-adic valuation $s+1$ is $3k$;
* the quotient $4\Lambda_k/(2n+1)$ is formed as an integer before reduction.

Consequently the actual $k\times k$ forcing block


$$
M=(T_{n_0-i+j})_{0\le i,j<k}
\tag{6.7}
$$


and its free-row block satisfy


$$
\boxed{
M\equiv\gamma I_k\pmod3,\qquad T_F\equiv0\pmod3.
}
\tag{6.8}
$$



Only these modulo-$3$ statements are used. The full entries of $M$ and $T_F$ remain in the subsequent exact identity.

### 6.2 The two contact blocks

For $\alpha=0,1$, put


$$
C_F^{(\alpha)}
=
(\sigma_{m+c+\alpha})_{\substack{m\in F\\0\le c<d}},
\qquad
C_P^{(\alpha)}
=
(\sigma_{m+c+\alpha})_{\substack{m\in P\\0\le c<d}}.
$$



The choice $\alpha=0$ corresponds to omitting the last contact-return column. The choice $\alpha=1$ corresponds to omitting the first.

By Lemma 5.1,


$$
\det C_F^{(\alpha)}
=
\mathcal A_d b_\alpha,
\qquad
b_\alpha\equiv1\pmod3.
\tag{6.9}
$$



Define an integer $k\times d$ matrix $N_\alpha$ by Cramer’s rule:
its $(i,j)$-entry is the determinant obtained by replacing row $j$ of $C_F^{(\alpha)}$ by row $i$ of $C_P^{(\alpha)}$, divided by $\mathcal A_d$. The division is integral by (2.6). Therefore


$$
C_P^{(\alpha)}(C_F^{(\alpha)})^{-1}
=
\frac{N_\alpha}{b_\alpha}.
\tag{6.10}
$$



This displays every local denominator explicitly.

### 6.3 The evaluated integer Schur determinant

After arranging rows as $F,P$, the selected original cofactor has block form


$$
\begin{pmatrix}
C_F^{(\alpha)}&T_F\\
C_P^{(\alpha)}&M
\end{pmatrix}.
$$


Subtracting


$$
\frac{N_\alpha}{b_\alpha}
$$


times the free rows from the pivot rows is legitimate over $\mathbb Z_{(3)}$. Its exact lower-right block is


$$
M-\frac{N_\alpha}{b_\alpha}T_F.
$$



Introduce the **integer** matrix


$$
\boxed{
K_\alpha=b_\alpha M-N_\alpha T_F.
}
\tag{6.11}
$$


It contains the complete forcing entries, including all factorial and cross-residue contributions. Equations (6.8)–(6.9) give the evaluated congruence


$$
\boxed{
K_\alpha\equiv\gamma I_k\pmod3,
\qquad
\det K_\alpha\equiv\gamma^k\not\equiv0\pmod3.
}
\tag{6.12}
$$



This is the required paid unit Schur determinant.

The row permutation from the original row order to $F,P$ has sign $-1$: its inversion count is


$$
k(t-1)+\frac{k(k-1)}2=k(k-2),
$$


which is odd. Hence the exact integer identities are


$$
\boxed{
b_\alpha^{\,k-1}M_k^{(\mathrm{omit})}
=
-\mathcal A_d\det K_\alpha,
}
\tag{6.13}
$$


with “omit” equal to $k-1$ for $\alpha=0$, and $0$ for $\alpha=1$.

Both $b_\alpha$ and $\det K_\alpha$ are units at $3$. Thus


$$
\boxed{
v_3(M_k^{(0)})
=
v_3(M_k^{(k-1)})
=
v_3(\mathcal A_d)
=
2\sum_{j=0}^{k-2}v_3(j!).
}
\tag{6.14}
$$



There is also an evaluated leading residue. Since $d$ is even,


$$
3^{-E_k}\mathcal A_d\equiv1\pmod3.
$$


Therefore, for the inherited determinant orientation,


$$
\boxed{
3^{-E_k}M_k^{(0)}
\equiv
3^{-E_k}M_k^{(k-1)}
\equiv
-\frac{\Lambda_k}{3k}
\pmod3.
}
\tag{6.15}
$$



### 6.4 Why this reaches high depth without the invalid extension

The earlier row-scalar argument tried to control a Schur complement entrywise modulo $3^h$. That required preservation of contact residue classes and failed beyond $2h\le s+2$.

The present proof does something different:

1. it pays the full divisor $\mathcal A_d$;
2. it proves that the selected free contact rows form a saturated row basis at $3$;
3. it uses the integrality of the **whole** interpolation matrix $N_\alpha/b_\alpha$;
4. it proves the remaining complete forcing determinant is a unit modulo $3$.

Thus no high-depth contact-period assertion is made. No cross-residue term is set to zero in the exact matrix $K_\alpha$. No factorial forcing is dropped from that matrix. Its unit determinant prevents any further $3$-adic valuation.

---

## 7. Exact $3$-parts of the original contents

### 7.1 Evaluation and the requested allowance

For $k=3^s$,


$$
\sum_{j=0}^{k-1}v_3(j!)
=
\frac{k(k-1-2s)}4,
\qquad
v_3((k-1)!)=\frac{k-1-2s}{2}.
$$


Subtracting the last term gives


$$
\boxed{
E_k
=
\frac{(k-2)(k-1-2s)}2.
}
\tag{7.1}
$$



The odd-certificate allowance at $3$ is


$$
v_3(\mathcal W_k^{\rm odd})=k^2+(2-s)k.
$$


Its difference from (7.1) is precisely (1.3), proving the requested inequality.

Every maximal minor of $Y_k$ contains at least $k-1$ contact-return columns. Laplace expansion and (2.6) therefore show that every such minor has $3$-adic valuation at least $E_k$. Since the two evaluated cofactors attain $E_k$,


$$
\boxed{v_3(\mathscr L_k)=E_k.}
\tag{7.2}
$$



### 7.2 An explicit original $Z_k$ maximal minor

The $Z_k$ result retains the atom and uses an actual maximal minor: take the first $2k-1$ rows of $Z_k$. This selects a minor; it does not change the original $2k$-row producer.

Assume $k=3^s\ge9$, which includes every original index. With $k=2t+1$, choose the $k-1$ forcing pivot rows


$$
P_Z=(3t+1,3t,\ldots,t+2).
\tag{7.3}
$$


The free rows in the selected maximal minor are


$$
F_Z=\{0,\ldots,t+1\}\cup\{3t+2,\ldots,4t\}.
\tag{7.4}
$$



Make the integer unit-triangular contact-column transformation


$$
(c_0,\ldots,c_{k-1})
\longmapsto
(c_0,\sigma_0,\ldots,\sigma_{k-2}).
\tag{7.5}
$$



Put


$$
m_0=t+1,\qquad h=3t+2=m_0+k,
$$


and remove $h$ temporarily from the free rows:


$$
F_\sigma=F_Z\setminus\{h\}.
$$


The $k-1$ rows in $F_\sigma$ have ordered residues $0,\ldots,k-2$ modulo $k$. Hence the square $\sigma$-block on those rows has determinant valuation $E_k$.

By Corollary 5.2, the row $\sigma(h)$ is an integral $3$-local combination $x$ of those rows, and


$$
x\equiv e_{m_0}^T\pmod3.
$$


Eliminate its $\sigma$-entries. The remaining entry in the retained atom column is


$$
c_h-xc_{F_\sigma}.
$$


Modulo $3$, this equals


$$
c_h-c_{m_0}.
$$


The original recurrence gives $u_{n+3}\equiv u_n\pmod3$, while $k$ is odd. Consequently


$$
c_h-c_{m_0}
\equiv
-\bigl((-1)^h-(-1)^{m_0}\bigr)
=
2(-1)^{m_0}\not\equiv0\pmod3.
\tag{7.6}
$$



Thus the $k\times k$ contact block on $F_Z$, **with its atom**, has determinant valuation $E_k$.

Every $k$-minor of the original contact block is divisible by $\mathcal B_k$, and


$$
v_3(\mathcal B_k)=E_k.
$$


Its pivot-row contact interpolation is therefore integral over $\mathbb Z_{(3)}$, by the same paid Cramer argument.

The $k-1$ forcing columns have a unit block on $P_Z$, and their free-row entries vanish modulo $3$. The same saturated-contact Schur elimination consequently proves


$$
\boxed{
v_3\!\left(\det Z_k[0,\ldots,2k-2;\,:]\right)=E_k.
}
\tag{7.7}
$$


All original $Z_k$ maximal minors have valuation at least $E_k$, by (2.7) and Laplace expansion. Therefore


$$
\boxed{v_3(\mathscr R_k)=E_k.}
\tag{7.8}
$$



### 7.3 Physical-boundary and division audit

All applications above stay inside the original finite arrays.

* The $Y_k$ contact shifts are exactly $0,\ldots,k-2$ or $1,\ldots,k-1$.
* All $k$ scaled forcing columns are retained in both requested cofactors.
* Every forcing entry is the complete integer (2.2).
* The largest $Y_k$ return index remains $3k-3$, using $u_{3k-2}$ and $(6k-4)!$.
* The $Z_k$ proof selects an original maximal minor; its unused last row remains part of $Z_k$ and of the producer.
* Finite-difference formulas require no contact value beyond the corresponding physical terminal.
* Divisions by $\mathcal A_d$ or $\mathcal B_k$ are proved integer divisions.
* The remaining denominators are actual integers prime to $3$, not presumed powers of $2$.

The high-depth $3$-part is therefore closed for both original contents. This does not close their other prime parts.

---

## 8. A secondary advance: an upper bound for the actual binary exponents

Write


$$
\mathfrak a_Y=v_2(\mathscr L_k),
\qquad
\mathfrak a_Z=v_2(\mathscr R_k).
$$


These are the actual exponents. They are not replaced by the established lower bounds $\nu_k^Y,\nu_k^Z$.

Define the odd integer


$$
\mathcal D_k^{\rm odd}
=
\left(\prod_{j=0}^{k-2}\operatorname{odd}(j!)\right)^2.
\tag{8.1}
$$


The contact-minor divisibilities (2.6)–(2.7), followed by Laplace expansion in the original mixed minors, give the all-prime integer divisibilities


$$
\mathcal D_k^{\rm odd}\mid\mathscr L_k,
\qquad
\mathcal D_k^{\rm odd}\mid\mathscr R_k.
\tag{8.2}
$$



Reuse the established original-content bound


$$
\mathscr L_k,\mathscr R_k\le\mathcal U_k,
$$


where


$$
\mathcal U_k
=
(2k-1)!\,4^k10^{k-1}\Lambda_k^{k-1}
\prod_{i=0}^{k-1}(2k+4i)!.
\tag{8.3}
$$


Its original nonvanishing hypothesis holds on the supplied original domain.

Because $\mathcal D_k^{\rm odd}$ is odd,


$$
2^{\mathfrak a_Y}\mathcal D_k^{\rm odd}\le\mathscr L_k,
\qquad
2^{\mathfrak a_Z}\mathcal D_k^{\rm odd}\le\mathscr R_k.
$$


This proves the exact upper bound


$$
\boxed{
\mathfrak a_Y,\mathfrak a_Z
\le
\left\lfloor
\log_2\frac{\mathcal U_k}{\mathcal D_k^{\rm odd}}
\right\rfloor.
}
\tag{8.4}
$$



### 8.1 Evaluation of its size

The previously unevaluated next constant in $\log\mathcal U_k$ is straightforward to obtain. Stirling summation gives


$$
\begin{aligned}
\log\prod_{i=0}^{k-1}(2k+4i)!
={}&4k^2\log k\\
&+\left(4\log2+\frac92\log3-6\right)k^2
+O(k\log k).
\end{aligned}
\tag{8.5}
$$


Indeed, the constant is


$$
\int_0^1(2+4x)\bigl(\log(2+4x)-1\bigr)\,dx
=
4\log2+\frac92\log3-6.
$$


Using $\log\Lambda_k=6k+o(k)$, the other factors in (8.3) give


$$
\boxed{
\log\mathcal U_k
=
4k^2\log k+
\left(4\log2+\frac92\log3\right)k^2+o(k^2).
}
\tag{8.6}
$$



Similarly,


$$
\boxed{
\log\mathcal D_k^{\rm odd}
=
k^2\log k-\left(\frac32+\log2\right)k^2
+O(k\log k).
}
\tag{8.7}
$$


Thus


$$
\boxed{
\mathfrak a_Y\log2,\ \mathfrak a_Z\log2
\le
3k^2\log k+
\left(\frac32+5\log2+\frac92\log3\right)k^2
+o(k^2).
}
\tag{8.8}
$$



This is a genuine upper bound for the actual binary depths. It is also explicitly insufficient: it does not establish $\mathfrak a_Y,\mathfrak a_Z=O(k^2)$.

### 8.2 A concrete remaining binary lemma

The paid factorization supplies a more specific next target than an unspecified binary content estimate. From (6.13),


$$
\boxed{
v_2(M_k^{(\mathrm{omit})})
=
v_2(\mathcal A_d)
+v_2(\det K_\alpha)
-(k-1)v_2(b_\alpha).
}
\tag{8.9}
$$


All quantities here are the explicit original integer objects defined in Section 6.

A sufficient next binary lemma is to prove, for at least one of $\alpha=0,1$,


$$
v_2(\det K_\alpha)-(k-1)v_2(b_\alpha)=O(k^2)
\tag{8.10}
$$


uniformly at the original indices, with an analogous paid statement for the explicit $Z_k$ minor.

This is an **open obligation**, not an evaluation claimed here. The precise obstruction to transferring the $3$-adic proof is that $b_\alpha$, and the Schur pivot itself, need not be units at $2$. Their actual binary valuations in (8.9) must be paid.

---

## 9. What is now settled in odd descent—and what is not

Define


$$
\mathcal W_k^{\rm odd}
=
3^{2k}\Lambda_k^k
\left(\prod_{j=0}^{k-1}\operatorname{odd}(j!)\right)^4.
\tag{9.1}
$$


For an odd prime $p$, its exact allowance is


$$
B_p(k)
=
k\bigl(2\mathbf1_{p=3}+v_p(\Lambda_k)\bigr)
+4\sum_{j=0}^{k-1}v_p(j!).
\tag{9.2}
$$



The new theorem proves


$$
v_3(\mathscr L_k),v_3(\mathscr R_k)\le B_3(k)
$$


at every original index. Thus the $3$-part is no longer an open part of these odd-divisibility targets.

Still unproved are


$$
v_p(\mathscr L_k)\le B_p(k),
\qquad
v_p(\mathscr R_k)\le B_p(k)
\tag{9.3}
$$


for all other odd primes. In particular, $B_p(k)=0$ for $p>6k-5$, so the corresponding good-prime normality obligation remains.

The $3$-local integers $b_\alpha$ and the other contact interpolation denominators can contain other odd primes. The proof therefore does **not** produce dyadic Bézout coefficients.

Conditionally, if


$$
\operatorname{odd}(\mathscr L_k)\mid\mathcal W_k^{\rm odd},
$$


then the least exponent in an integer identity


$$
\sum_j\beta_jM_{k,j}
=
2^a\mathcal W_k^{\rm odd}
$$


is exactly


$$
\boxed{a=\mathfrak a_Y=v_2(\mathscr L_k),}
\tag{9.4}
$$


not $\nu_k^Y$. The analogous assertion holds for $Z_k$.

No such simultaneous odd-prime identity, with its full integer coefficients, is asserted here.

---

## 10. Exact normalization and all-prime payments remain unchanged

### 10.1 Final determinant and primitive pair

The original affine determinant remains


$$
H_k(z)=
\det\left[
(c_{m+j})_{\substack{m<2k\\j<k}}
\ \middle|\
\bigl(\Lambda_k(r_{m+j}+z(-1)^{m+j})\bigr)_{\substack{m<2k\\j<k}}
\right]
=H_{0,k}+H_{1,k}z.
\tag{10.1}
$$



Whenever $H_{1,k}\ne0$,


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$




$$
q_k=\frac{|H_{1,k}|}{G_k},
\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
\tag{10.2}
$$


The universally valid signed identity is


$$
q_k(e+\pi)-p_k
=
\frac{\operatorname{sgn}(H_{1,k})H_k(e+\pi)}{G_k}.
\tag{10.3}
$$



On the supplied original nonvanishing and positivity domain,


$$
\boxed{
0<\ell_{K_u}
=q_{K_u}(e+\pi)-p_{K_u}
=\frac{|H_{K_u}(e+\pi)|}{G_{K_u}}.
}
\tag{10.4}
$$



The bordered-content relations remain


$$
\boxed{
\operatorname{lcm}(\mathscr R_k,\mathscr L_k)
\mid G_k
\mid\Lambda_k\mathscr R_k\mathscr L_k.
}
\tag{10.5}
$$


The new $3$-part result gives only the range


$$
\boxed{
E_k\le v_3(G_k)\le 2E_k+s+1.
}
\tag{10.6}
$$


It does not determine $G_k$, or even its exact $3$-part.

The least simultaneous coefficient clearer of $H_k/\Lambda_k^k$ is still


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}),
}
\tag{10.7}
$$


with remaining coefficient content $G_k/d_{H,k}$. No lower divisor replaces these actual quantities.

### 10.2 Finite-jet arrays and their actual corrections

For completeness, the finite jet transformations remain


$$
(T_\star y)_m
=
\sum_{r=0}^m
(-1)^r\binom{b_\star}{r}
(2m-2r+1)_{h_\star+2r}\,y_{m-r},
\tag{10.8}
$$


where


$$
h_Z=2k-3,\quad b_Z=2k-1,
\qquad
h_Y=2k-1,\quad b_Y=2k+1.
$$


Their row ranges are the original $m<2k$ and $m<2k-1$.

They factor as $T_\star=D_\star S_\star$, with $S_\star$ integer unit lower triangular and diagonal payments


$$
(D_Z)_{mm}=(2m+1)_{2k-3},
\qquad
(D_Y)_{mm}=(2m+1)_{2k-1}.
$$


The integral arrays use the complete $\tau$:


$$
\mathbf J_{Z,k}=T_Z[c_{m+j}\mid\tau_{m+j}],
\qquad
\mathbf J_{Y,k}=T_Y[\sigma_{m+j}\mid\tau_{m+j}].
$$



Retain their actual contents $\mathscr C_{Z,k},\mathscr C_{Y,k}$, and


$$
t_Z=\prod_{m=0}^{2k-1}(2m+1)_{2k-3},
\qquad
t_Y=\prod_{m=0}^{2k-2}(2m+1)_{2k-1}.
\tag{10.9}
$$



If $v$ is the actual primitive signed cofactor vector after the stated $Z$-row transformation, retain


$$
\zeta_{Z,k}
=
\operatorname{lcm}_m
\frac{(2m+1)_{2k-3}}
{\gcd((2m+1)_{2k-3},|v_m|)}.
\tag{10.10}
$$


For the actual two $Y$-jet minor-type gcds $\alpha_Y,\beta_Y$, retain


$$
\chi_{Y,k}
=
\frac{\gcd(\Lambda_k\alpha_Y,\beta_Y)}
{\gcd(\alpha_Y,\beta_Y)},
\qquad
\chi_{Y,k}\mid\Lambda_k.
\tag{10.11}
$$



The exact transfers are unchanged:


$$
\boxed{
\mathscr R_k
=
\frac{\Lambda_k^{k-1}\mathscr C_{Z,k}\zeta_{Z,k}}{t_Z},
\qquad
\mathscr L_k
=
\frac{\Lambda_k^{k-1}\mathscr C_{Y,k}\chi_{Y,k}}{t_Y}.
}
\tag{10.12}
$$


Neither $\zeta_{Z,k}$ nor $\chi_{Y,k}$ is assigned the value $1$.

The individual original right-column clearers also remain


$$
\Lambda_{k,j}
=
\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$


No previously paid contact-column or divided-contact factorial normalization is removed by the new local argument.

---

## 11. Whole-error comparisons, including both required constants

The already evaluated transfer constant is reused:


$$
\boxed{
\log\mathscr R_k+\log\mathscr L_k
=
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
-8k^2\log k
+(24-18\log3)k^2+o(k^2).
}
\tag{11.1}
$$


Before taking asymptotics, the exact logarithmic identity is


$$
\begin{aligned}
\log\mathscr R_k+\log\mathscr L_k
={}&
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
+2(k-1)\log\Lambda_k\\
&+\log\zeta_{Z,k}+\log\chi_{Y,k}
-\log t_Z-\log t_Y.
\end{aligned}
\tag{11.2}
$$



The odd-certificate height is likewise retained:


$$
\boxed{
\log\mathcal W_k^{\rm odd}
=
2k^2\log k+(3-2\log2)k^2+o(k^2).
}
\tag{11.3}
$$



Conditionally, if odd descent were proved for both contents, then


$$
\log\mathscr R_k+\log\mathscr L_k
\le
(\mathfrak a_Z+\mathfrak a_Y)\log2
+2\log\mathcal W_k^{\rm odd}.
\tag{11.4}
$$


If one also proved the useful actual binary upper bound


$$
\mathfrak a_Z+\mathfrak a_Y\le Ak^2+o(k^2),
$$


then


$$
\log G_k
\le
4k^2\log k+
\bigl(A\log2+6-4\log2\bigr)k^2+o(k^2).
\tag{11.5}
$$


The new bound (8.8) does not establish this additional hypothesis.

The supplied analytic estimate remains


$$
\log|H_k(e+\pi)|=4k^2\log k+O(k^2)
\tag{11.6}
$$


on its original-index scope. The new arithmetic proof needs no analytic nonvanishing premise; the whole-error discussion uses the supplied analytic and positivity results only at that stated scope.

A strict content estimate


$$
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
\le(12-\eta)k^2\log k+O(k^2),
\qquad \eta>0,
$$


would imply divergence of the primitive whole errors at the same original indices. It would retire this compact producer as a source of primitive whole-error decay; it would not prove $e+\pi$ rational.

At the critical leading coefficient, estimates


$$
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
\le12k^2\log k+C_Jk^2+o(k^2)
$$


and


$$
\log|H_k(e+\pi)|
\ge4k^2\log k+C_Hk^2+o(k^2)
$$


would force divergence if


$$
\boxed{C_H>C_J+24-18\log3.}
\tag{11.7}
$$



Conversely, a proof of


$$
0<\ell_{K_u}\longrightarrow0
$$


would prove irrationality: if $e+\pi=a/b$, every nonzero $q_{K_u}(e+\pi)-p_{K_u}$ has absolute value at least $1/b$.

Neither decay nor divergence is established here.

### Separate binary producer

No compact result is transferred to the separate binary producer. Its domain and terminal remain


$$
b=9^{18+32u},\qquad n=4002b,\qquad
j=0,\ldots,b-1,\qquad z_b=0.
$$


Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0,
$$


and its complete return remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


Only the supplied paid estimate


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1},
$$


is retained. Its $Q=x_0^Tx_0$, corrected-column contents, actual least simultaneous clearer, actual primitive denominator, and final all-prime gcd remain separate and unchanged.

---

## 12. A new bounded auxiliary check

No computation is needed for the proofs above. No tool execution has been performed.

If the coordinator confirms that this scale is not already closed, a new finite audit can check the **full cofactor valuation**, rather than another capped spectrum.

### Inputs

Take


$$
k=27,\qquad s=3,\qquad \text{modulus }3^{251}.
$$


Use exactly


$$
\Lambda_{27}=\operatorname{lcm}(1,3,\ldots,157)
$$


and the original recurrences.

The bounded physical data are:

* moments through $79$;
* factorials through $158!$;
* last odd denominator $157$;
* $Y_{27}$ of shape $53\times54$;
* the two $53\times53$ minors omitting contact column $0$ or $26$;
* all $27$ original scaled forcing columns in each minor.

The pivot rows are $40,39,\ldots,14$, and the free rows are


$$
0,\ldots,13,\quad 41,\ldots,52.
$$



### Expected verifiable outputs

Here


$$
E_{27}=\frac{25(26-6)}2=250.
$$


Also


$$
\frac{\Lambda_{27}}{81}\equiv2\pmod3.
$$


For example, the odd-exponent prime-power contributions congruent to $-1\pmod3$ are represented by


$$
5,17,23,29,41,47,53,59,71,83,89,101,107,113,131,137,149,
$$


a list of odd cardinality; the $11^2$ contribution has even exponent.

Thus, in inherited determinant orientation, the predicted outputs are


$$
\boxed{
M_{27}^{(0)}\equiv3^{250}\pmod{3^{251}},
\qquad
M_{27}^{(26)}\equiv3^{250}\pmod{3^{251}}.
}
\tag{12.1}
$$


Equivalently, both valuations are exactly $250$, and both normalized units are $1\pmod3$.

A receipt should retain the complete scaled forcing entries and verify determinant residues with all nonunit divisions, if any, explicitly paid. These bounded inputs do not require an enormous original-index factorial matrix or third-party code.

This would establish exactly one finite auxiliary check of the new theorem. It would not be an all-prime content audit, a simultaneous odd-descent certificate, or an irrationality proof.

---

## 13. Proof-status ledger

| Statement | Status |
|---|---|
| High-depth inequality (6.4) for the two specified original $Y_k$ cofactors | **Proved**, with equality to the smaller value $E_k$ |
| Exact valuations of both cofactors | **New evaluated theorem** |
| $v_3(\mathscr L_k)=E_k$ | **Proved** at every original index |
| $v_3(\mathscr R_k)=E_k$, retaining the atom | **Proved**, using an explicit original maximal minor |
| Complete forcing and cross-residue terms in the high-depth elimination | **Retained in the exact integer Schur matrix** |
| Extension of the old row-scalar reduction beyond $2h\le s+2$ | **Not used or asserted** |
| Improved actual binary upper bound (8.4)–(8.8) | **Proved**, but still $O(k^2\log k)$ |
| Useful actual binary upper bound $O(k^2)$ | **Open** |
| Integral weighted-certificate descent | **Previously disproved** for $k\ge18$; not reattempted |
| Simultaneous odd descent at primes other than $3$ | **Open** |
| Full integer/dyadic Bézout certificate for odd descent | **Not constructed** |
| Exact final all-prime gcd $G_k$ | **Not determined** |
| Critical jet-content/whole-error comparison | **Open**, with both required constants retained |
| Proposed $k=27$ full-cofactor audit | **New bounded auxiliary check, not executed** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

## Final conclusion

The primary high-depth gate is closed. Both specified original $Y_k$ cofactors satisfy the requested inequality, and more precisely


$$
\boxed{
v_3(M_k^{(0)})
=
v_3(M_k^{(k-1)})
=
v_3(\mathscr L_k)
=
v_3(\mathscr R_k)
=
\frac{(k-2)(k-1-2s)}2
}
$$


at every unchanged original index $k=3^s=9^{18+32u}$.

The new mechanism is a fully paid factorial-normalized contact-row basis followed by an evaluated unit Schur determinant. It retains every original forcing column and does not invoke invalid high-depth row-scalar periodicity.

The remaining arithmetic bottleneck is now genuinely outside this $3$-part: simultaneous control at the other odd primes, a useful upper bound paying the actual binary exponents, and then control of the final **all-prime** gcd $G_k$ in the complete primitive whole error. The primitive denominator remains $|H_{1,k}|/G_k$, and the nonzero evaluated whole error remains $|H_k(e+\pi)|/G_k$ on the same infinite original indices. No conclusion about the rationality of $e+\pi$ follows yet.
