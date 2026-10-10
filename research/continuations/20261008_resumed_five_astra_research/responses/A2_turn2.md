> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the complete compact arithmetic, with a new paid-transfer splitting theorem

## 1. Executive conclusion

The attached work does **not** prove that $e+\pi$ is rational or irrational. The unconditional rationality question remains unresolved.

The principal arithmetic theorems of A5 Turn 2 survive this independent audit, with their stated hypotheses retained:

1. The positive-contact matrix has full column rank modulo every prime $p>k$.
2. The complete contact matrix, with its atom retained, has rank at least $k-1$ at those primes.
3. The complete right forcing has the stated, evaluated Cauchy determinant certificate.
4. The two actual rectangular contents satisfy
   

$$
\operatorname{lcm}(\mathscr R_k,\mathscr L_k)
   \mid G_k\mid
   \Lambda_k\mathscr R_k\mathscr L_k
$$


   whenever $H_{1,k}\ne0$.
5. The $(k+1)$-square local reduction is valid at $p>6k-4$, and it retains both the contact atom and the complete right correction.

Several restrictions are indispensable:

- The exact formula
  

$$
v_p(G_k)=\min\bigl(v_p(D),v_p(\mathscr R_k)+v_p(\mathscr L_k)\bigr)
$$


  requires the additional hypothesis that the period-isolated block $B$ has at most one nonunit Smith invariant. The positive-contact theorem does **not** establish that hypothesis.
- The Cauchy certificate concerns the augmented return/factorial-return arrays. It is not already a certificate for $Y_k$ or $Z_k$.
- The homogeneous Bessel recurrence applies to a normalized positive part, not to the complete contact or right columns.
- The complete divided-difference recurrences involving $\mathcal B_n$ must be used for $n\ge1$; their displayed initial conditions must not be replaced by an erroneous $n=0$ recurrence.
- Five-consecutive scalar primitivity is not matrix primitivity.

This report adds two rigorous refinements.

### New proved refinement I: separated Smith depth

In the bordered-content setting, put


$$
S=v_p(\det B),\qquad
r=v_p(\mathscr R_k),\qquad c=v_p(\mathscr L_k),
$$


and


$$
t_B=v_p\bigl(\delta_{N-1}(B)\bigr),\qquad N=2k-1.
$$


If


$$
r+c<S,
$$


then, without assuming that $B$ has only one nonunit invariant,


$$
\boxed{v_p(G_k)=r+c-t_B.}
\tag{1.1}
$$


This conclusion remains valid even when $p\mid\Lambda_k$.

### New proved refinement II: exact splitting of the paid Schur primes

For the complete paid adjacent transfer


$$
\chi_kF^+=\alpha_kF+\beta_k,
$$


one necessarily has


$$
\boxed{\gcd(|\alpha_k|,\chi_k)=1.}
\tag{1.2}
$$


Moreover,


$$
\boxed{
\gcd(\chi_k,t^kG_k)=\gcd(\chi_k,|\beta_k|),
\qquad
\gcd(|\alpha_k|,G_{k+1})
=\gcd(|\alpha_k|,|\beta_k|).
}
\tag{1.3}
$$


Consequently,


$$
\boxed{
\frac{\chi_k}{\gcd(\chi_k,|\beta_k|)}\mid q_k,
\qquad
\frac{|\alpha_k|}{\gcd(|\alpha_k|,|\beta_k|)}\mid q_{k+1}.
}
\tag{1.4}
$$



These are statements about the **actual primitive denominators**, not denominators obtained by substituting a known lower divisor for $G_k$.

They yield a new, fully paid lower bound for the whole error at an original index $K_u$:


$$
\boxed{
\ell_{K_u}\ge
\frac{3}{4K_u^2A^{K_u-1}}\,
\frac{\chi_{K_u}}
{\gcd(\chi_{K_u},|\beta_{K_u}|)},
\qquad A=17+12\sqrt2.
}
\tag{1.5}
$$


No useful infinite lower or upper asymptotic estimate for the new quotient has yet been proved.

The splitting theorem also gives a genuinely new bounded follow-on check using the **already completed** $11\to12$ transfer certificate: only two additional scalar gcds are needed. No determinant, Smith table, $32/33$ calculation, or $k=5$ rectangular diagnostic needs to be repeated.

---

## 2. Objects, normalization, and scope

For the compact construction,


$$
k\ge2,\qquad 0\le m<2k,\qquad 0\le j<k.
$$


Retain


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad w_n=(-1)^n,
$$




$$
c_n=u_n-w_n,
$$




$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad
r_n=-f_n+4\rho_n.
$$



The complete returns are


$$
\sigma_n=c_{n+1}+c_n=u_{n+1}+u_n,
$$


and


$$
\boxed{
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{2.1}
$$



Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5)
$$


and


$$
H_k(s)=
\det\left[
(c_{m+j})\ \middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s.
\tag{2.2}
$$



The original finite boundary is


$$
\max(m+j)=3k-2,
$$


so the largest factorial is $(6k-4)!$, and the last odd denominator is $6k-5$.

Whenever $H_{1,k}\ne0$, the actual normalization is


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$




$$
q_k=\frac{|H_{1,k}|}{G_k},
\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
\tag{2.3}
$$



The closed analytic results are reused at their supplied scope. In particular, for $k\ge64$,


$$
0<\varepsilon_k=e+\pi-\frac{p_k}{q_k},
\qquad
0<\varepsilon_{k+1}\le\frac14\varepsilon_k,
$$


and


$$
\frac{3}{4k^2A^{k-1}}
\le\varepsilon_k
\le\frac{63}{2A^{k-1}}.
\tag{2.4}
$$


The whole error is exactly


$$
\boxed{
\ell_k=q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}>0.
}
\tag{2.5}
$$



The accepted leading scales are


$$
\log|H_k(e+\pi)|=4k^2\log k+O(k^2),
\qquad
\log|H_{1,k}|=4k^2\log k+O(k^2).
\tag{2.6}
$$


The older leading-$2$ lower estimate is not substituted for these accepted leading-$4$ scales.

---

## 3. Independent check of the arithmetic payments from A5 Turn 1

### 3.1 Actual right-column clearers

For column $j$, put


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$



Sufficiency follows directly from the recurrence for $\rho_n$. For necessity, if an integer $L$ clears


$$
r_j,\ldots,r_{2k-1+j},
$$


then, using only adjacent entries already in that column, (2.1) gives


$$
2n+1\mid L
\qquad(j\le n\le2k-2+j).
$$



Every odd prime power below $4k+2j-3$ divides an odd integer in this interval. Indeed, if $q<2j+1$, choose the least odd multiple of $q$ not below $2j+1$. It is less than


$$
2j+1+2q\le6j-1\le4k+2j-3.
$$


Thus $\Lambda_{k,j}$ is the actual least clearer.

Therefore


$$
H_k(s)=E_k\widehat H_k(s),
\qquad
E_k=\frac{\Lambda_k^k}{\prod_{j=0}^{k-1}\Lambda_{k,j}}\in\mathbb Z_{>0}.
\tag{3.1}
$$


For odd $p$,


$$
v_p(E_k)=
\sum_{\substack{a\ge1\\4k-3<p^a\le6k-5}}
\frac{p^a-4k+3}{2},
\qquad v_2(E_k)=0.
\tag{3.2}
$$



After clearing a right coefficient-column by its actual $\Lambda_{k,j}$, its coefficient content is $1$. Its period coefficients have gcd $\Lambda_{k,j}$; if a prime dividing this number divided every cleared constant entry as well, a smaller clearer would exist. Primes outside $\Lambda_{k,j}$ cannot divide all period coefficients.

This is a statement about individual coefficient-columns, not the final determinant content.

### 3.2 Divided contact moments, including the atom

The integral identity


$$
u_n=\int_0^\infty(t-1)^{2n}e^{-t}\,dt
$$


gives


$$
\Delta^nu_0=\int_0^\infty[t(t-2)]^ne^{-t}\,dt.
$$


Two integrations by parts give, for $n\ge1$,


$$
d_{n+1}
=2(n+1)(2n+1)d_n+4n(n+1)d_{n-1},
$$


where $d_n=\Delta^nu_0$, $d_0=1$, $d_1=0$.

Hence


$$
d_n=2^nn!g_n,
$$


with


$$
g_0=1,\quad g_1=0,\quad
g_{n+1}=(2n+1)g_n+g_{n-1}\quad(n\ge1).
$$



Since the atom contributes $\Delta^nw_0=(-2)^n$,


$$
\boxed{
\Delta^nc_0=2^nb_n,\qquad
b_n=n!g_n-(-1)^n.
}
\tag{3.3}
$$


In particular,


$$
b_0=0,\qquad b_1=1,
$$


and, for $n\ge1$,


$$
\boxed{
b_{n+1}
=(n+1)(2n+1)b_n+n(n+1)b_{n-1}
+\bigl((n+1)^2+1\bigr)(-1)^n.
}
\tag{3.4}
$$



The restriction $n\ge1$ matters: applying this displayed recurrence at $n=0$ would incorrectly give $b_1=2$.

A common divisor of $b_n,\ldots,b_{n+4}$ divides


$$
(n+2)^2+1,\quad(n+3)^2+1,\quad(n+4)^2+1.
$$


The gcd of these three integers divides $2$, while at least one of the first two is odd. Thus


$$
\gcd(b_n,\ldots,b_{n+4})=1.
\tag{3.5}
$$


Also,


$$
\gcd(b_n,n!)=1.
\tag{3.6}
$$



These statements are correct, but remain scalar statements.

### 3.3 Exact transformed column contents and factorial payments

The integral binomial row and contact-column transformations have determinant $1$ and send the contact matrix to


$$
C'_{mj}=\Delta^{m+j}c_0=2^{m+j}b_{m+j}.
\tag{3.7}
$$



Every $b_n$ with $n\ge1$ is odd. Together with (3.5), this proves that the actual content of contact column $j$ is


$$
\boxed{2^{\max(1,j)}.}
\tag{3.8}
$$



The tempting normalized entry is


$$
\frac{\Delta^nc_0}{2^nn!}=\frac{b_n}{n!}.
$$


Its actual denominator is $n!$, by (3.6). Thus column $j$, whose final index is $N_j=2k-1+j$, has actual simultaneous clearer


$$
\boxed{N_j!}
\tag{3.9}
$$


and content $1$ after that clearing.

The entrywise division by $(m+j)!$ is not a row or column scaling of the original determinant. It cannot be treated as a free unimodular normalization.

### 3.4 Product contact divisor, including shared powers of $2$

Take an $h$-minor of $C'$, with row set $I$ and column set $J$. Factoring powers of $2$ gives


$$
2^{\sum_{m\in I}m+\sum_{j\in J}j}
\det(b_{m+j})_{I,J},
$$


and


$$
\sum_{m\in I}m+\sum_{j\in J}j\ge h(h-1).
$$



Write


$$
b_{m+j}=A_{mj}-(-1)^m(-1)^j,
\qquad
A_{mj}=(m+j)!g_{m+j}.
$$


An $h$-minor of this rank-one perturbation is an $h$-minor of $A$ plus an integer linear combination of $(h-1)$-minors of $A$.

Moreover,


$$
A_{mj}
=m!j!\binom{m+j}{m}g_{m+j}.
$$


Every relevant $(h-1)$-minor is therefore divisible by


$$
\prod_{r=0}^{h-2}(r!)^2.
$$


This factorial divisibility has been proved **after** the displayed binary factor was removed. Consequently,


$$
\boxed{
2^{h(h-1)}
\prod_{r=0}^{h-2}(r!)^2
\mid\delta_h(C_k).
}
\tag{3.10}
$$



This validates the product, not merely its least common multiple.

Expanding $\widehat H_k$ along its $k$ contact columns and then restoring $E_k$ yields


$$
\boxed{
\mathcal P_k:=
E_k\,2^{k(k-1)}
\prod_{r=0}^{k-2}(r!)^2
\mid H_{0,k},H_{1,k}.
}
\tag{3.11}
$$


Thus $\mathcal P_k\mid G_k$ on the nonvanishing domain.

### 3.5 Complete divided right forcing

For completeness, let


$$
F_n=\Delta^nf_0,\qquad V_n=\Delta^n\rho_0,
$$


and


$$
\mathcal B_n y
=y_{n+1}-2(n+1)(2n+1)y_n-4n(n+1)y_{n-1}.
$$


For $n\ge1$, direct integration by parts and the $\rho$-recurrence give


$$
\mathcal B_nF=(-1)^{n+1},
$$




$$
V_{n+1}+2V_n=\beta_n,
\qquad
\beta_n=(-1)^n\frac{4^n(n!)^2}{(2n+1)!}.
\tag{3.12}
$$



The actual denominator of $\beta_n$ is the odd part of


$$
(2n+1)\binom{2n}{n}.
$$


Its finite-sum representation shows that this denominator divides the lcm of the odd integers through $2n+1$.

For


$$
R_n(s)=-F_n+4V_n+s(-2)^n,
$$


one obtains


$$
\mathcal B_nR
=(-1)^n
-2\bigl((n+1)^2+1\bigr)(R_n+F_n)
+4(2n^2+3n+2)\beta_n.
\tag{3.13}
$$



Thus the contact atom, factorial endpoint forcing, and full beta-integral correction all survive. The homogeneous recurrence cannot replace (3.4) or (3.13).

---

## 4. Audit of the positive-contact rank theorem

Let


$$
U_k=(u_{m+j})_{0\le m<2k,\ 0\le j<k}.
$$



### Theorem 4.1

For every $k\ge2$ and prime $p>k$,


$$
\operatorname{rank}_{\mathbb F_p}U_k=k.
$$



### Proof

Work over characteristic zero or characteristic $p>k$. From


$$
u_{n+1}=(4n^2+6n+2)u_n-(2n+1),
$$


the formal series


$$
\mathcal U(z)=\sum_{n\ge0}u_nz^n
$$


satisfies


$$
\mathcal L\mathcal U=\frac{1-3z}{(1-z)^2},
$$


where


$$
\mathcal L
=1-2z-10z^2\frac{d}{dz}-4z^3\frac{d^2}{dz^2}.
\tag{4.1}
$$



Suppose


$$
\sum_{j=0}^{r}x_ju_{m+j}=0
\qquad(0\le m<2k),
$$


where $r\le k-1$ and $x_r\ne0$. The case $r=0$ is impossible already at $m=0$, since $u_0=1$.

Put


$$
B(z)=\sum_{j=0}^{r}x_jz^{r-j}.
$$


Then $B(0)\ne0$, and for a polynomial $A$ of degree $<r$,


$$
B\mathcal U-A=O(z^{2k+r}).
$$


Thus $R=A/B$ satisfies


$$
\mathcal U-R=O(z^{2k+r}).
$$



The operator $\mathcal L$ preserves this order of vanishing: multiplication by $z^2$ or $z^3$ compensates for every differentiation. Therefore


$$
\mathcal L(\mathcal U-R)=O(z^{2k+r}).
$$



Set


$$
N_B=B^3\mathcal L(A/B).
$$


Differentiation gives


$$
\begin{aligned}
N_B={}&(1-2z)AB^2
-10z^2(A'B-AB')B\\
&-4z^3\left(
A''B^2-AB''B-2A'B'B+2A(B')^2
\right).
\end{aligned}
\tag{4.2}
$$



The potentially largest degree is $3r$. It can occur only when
$\deg B=r$ and $\deg A=r-1$. Its scalar coefficient is


$$
-2-10(-1)-4(-1)(-2)=0.
$$


In every other degree case the bound is already smaller. Hence


$$
\deg N_B\le3r-1.
$$



It follows that


$$
Q=(1-z)^2N_B-(1-3z)B^3
$$


has degree at most $3r+1$, while


$$
Q=O(z^{2k+r}).
$$


Since


$$
2k+r-(3r+1)=2(k-r)-1\ge1,
$$


we have $Q=0$. Thus


$$
\mathcal LR=\frac{1-3z}{(1-z)^2}.
\tag{4.3}
$$



This is impossible at $z=1$. The right side has a nonzero double pole because its numerator there is $-2$, nonzero in the stated characteristics.

If $R$ is regular at $1$, so is $\mathcal LR$, a contradiction. If $R$ has pole order $m$, then


$$
1\le m\le r\le k-1.
$$


The term $-4z^3R''$ has pole order $m+2$, with nonzero leading coefficient proportional to $4m(m+1)$. Since $m+1\le k<p$, this coefficient cannot vanish. The remaining terms have smaller pole order. Hence $\mathcal LR$ has pole order at least $3$, again contradicting (4.3). ∎

### Finite-boundary verification

The highest moment used in the assumed relation is


$$
u_{2k+r-1}\le u_{3k-2}.
$$


The forced ODE is required only through that same coefficient order. The formal-series notation therefore introduces no $u_{3k-1}$, no extra row, and no factorial beyond $(6k-4)!$.

### Atom-retaining corollary

Let


$$
w=(( -1)^m)_{m<2k},\qquad v=(( -1)^j)_{j<k}.
$$


The exact identity is


$$
U_k=C_k+w v^T.
$$


If $C_kx=0$ and $v^Tx=0$, then $U_kx=0$, hence $x=0$. Therefore


$$
\boxed{
\operatorname{rank}
\begin{pmatrix}C_k\\v^T\end{pmatrix}=k,
\qquad
\operatorname{rank}C_k\ge k-1
\quad(p>k).
}
\tag{4.4}
$$



If $C_k$ has rank $k-1$, its kernel is transverse to $v^T$, and


$$
w\notin\operatorname{im}C_k.
$$


Otherwise $U_k=C_k(I+yv^T)$ for some $y$, contradicting its rank.

Consequently,


$$
\operatorname{rad}\bigl(\delta_{k-1}(C_k)\bigr)
\mid\operatorname{rad}(k!).
\tag{4.5}
$$


This proves that at most one contact Smith invariant is nonunit at $p>k$. It does not bound the depth of that last invariant, and does not prove full rank of $C_k$.

---

## 5. Forced displacement and the Cauchy certificate

### 5.1 Every shift commutator is present

Put


$$
P_n=(2n+1)(2n+2).
$$


The exact shift difference is


$$
\boxed{P_{m+j}-P_m=8mj+4j^2+6j.}
\tag{5.1}
$$



With


$$
M=\operatorname{diag}(0,\ldots,2k-2),\quad
J=\operatorname{diag}(0,\ldots,k-1),\quad
B_J=4J^2+6J,
$$


the positive and factorial blocks satisfy


$$
U_+
=P(M)U_-+8MU_-J+U_-B_J
-(2M+I)\mathbf1\mathbf1^T-2\mathbf1\mathbf1^TJ,
\tag{5.2}
$$




$$
F_+
=P(M)F_-+8MF_-J+F_-B_J.
\tag{5.3}
$$



Since $C=U-W$ and $W_+=-W_-$,


$$
\begin{aligned}
C_+={}&P(M)C_-+8MC_-J+C_-B_J\\
&+(P(M)+I)W_-+8MW_-J+W_-B_J\\
&-(2M+I)\mathbf1\mathbf1^T-2\mathbf1\mathbf1^TJ.
\end{aligned}
\tag{5.4}
$$



For the complete paid right block,


$$
\boxed{
\mathcal R(s)_++\mathcal R(s)_-
=
-\Lambda_k\bigl((P(M)+I)F_-+8MF_-J+F_-B_J\bigr)
+4\Lambda_k\mathcal D,
}
\tag{5.5}
$$


where


$$
\mathcal D_{mj}=\frac1{2m+2j+1}.
$$



All successors remain at most $3k-2$.

There is also an elementary, evaluated check that the commutator cannot be ignored. Replacing $P_{m+j}$ by $P_m$ in the complete contact recurrence omits


$$
(P_{m+j}-P_m)u_{m+j}-2j.
$$


At the physical entry $(m,j)=(0,1)$, this is


$$
(12-2)\cdot1-2=8\ne0.
\tag{5.6}
$$


Thus even the first shifted column already exhibits the failure.

### 5.2 State transport does not imply pencil primitivity

The five-state matrix has determinant $P_n^2$, entry content $1$, and actual inverse clearer $P_n$: an inverse entry $1/P_n$ occurs, and multiplication by $P_n$ clears the entire inverse.

For $0\le n\le3k-3$, all its rational forcing has already been cleared by $\Lambda_k$. Therefore the state transport is invertible at $p>6k-4$.

This proves regularity of the state transport only. A relation among columns does not imply the same relation after replacing its coefficient vector by $Jx$ or $J^2x$.

### 5.3 Exact Cauchy forcing

On the $(2k-1)\times k$ return array,


$$
T_{mj}=\Lambda_k\tau_{m+j},
\qquad
V_{mj}=\Lambda_k\bigl((2m+2j+2)!+(2m+2j)!\bigr),
$$


we have


$$
\boxed{T+V=4\Lambda_k\mathcal D.}
\tag{5.7}
$$



The actual denominator of $\tau_n$ is $2n+1$: its numerator modulo that odd denominator is $4$. Thus the whole return array has actual least clearer $\Lambda_k$.

Its cleared entry content is $1$. The entry $n=0$ is $\Lambda_k$, excluding all primes outside $\Lambda_k$. For a maximal prime power $p^a\mid\Lambda_k$, the entry with $2n+1=p^a$ is a $p$-adic unit after multiplication by $\Lambda_k$.

For the first $k$ rows, the forcing array has actual raw clearer


$$
L_k^{\rm force}=\operatorname{lcm}(1,3,\ldots,4k-3),
$$


and its content after multiplication by $\Lambda_k$ is


$$
\frac{4\Lambda_k}{L_k^{\rm force}}.
$$


No division by this content is made in the determinant certificate.

The Cauchy determinant is


$$
\det\mathcal D_0
=
\frac{
2^{k(k-1)}\prod_{r=1}^{k-1}(r!)^2
}{
\prod_{i,j=0}^{k-1}(2i+2j+1)
}.
$$


Hence


$$
\boxed{
\Theta_k=\det(T_0+V_0)
=(4\Lambda_k)^k
\frac{
2^{k(k-1)}\prod_{r=1}^{k-1}(r!)^2
}{
\prod_{i,j=0}^{k-1}(2i+2j+1)
}.
}
\tag{5.8}
$$



This is a positive integer. Every prime divisor is at most $6k-5$, and


$$
\begin{aligned}
v_p(\Theta_k)
={}&k\,v_p(4\Lambda_k)+k(k-1)v_p(2)
+2\sum_{r=1}^{k-1}v_p(r!)\\
&-\sum_{i,j=0}^{k-1}v_p(2i+2j+1).
\end{aligned}
\tag{5.9}
$$


Hadamard's inequality and $\log\Lambda_k=O(k)$ give


$$
\log\Theta_k=O(k^2).
$$



Column and row expansion give


$$
\delta_k([T_0\mid V_0])\mid\Theta_k,
\qquad
\delta_k\begin{pmatrix}T_0\\V_0\end{pmatrix}\mid\Theta_k.
\tag{5.10}
$$



Thus the augmented horizontal and vertical arrays are primitive at $p>6k-4$. This is a genuine evaluated matrix certificate. It is not yet a certificate for the mixed arrays in the next section.

---

## 6. Period isolation and the two actual rectangles

Define


$$
Z_k=
\left[
(c_{m+j})_{\substack{m<2k\\j<k}}
\ \middle|\
(\Lambda_k\tau_{m+j})_{\substack{m<2k\\j<k-1}}
\right],
$$




$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{m<2k-1\\j<k}}
\ \middle|\
(\Lambda_k\tau_{m+j})_{\substack{m<2k-1\\j<k}}
\right].
$$


Put


$$
\mathscr R_k=\delta_{2k-1}(Z_k),
\qquad
\mathscr L_k=\delta_{2k-1}(Y_k).
$$



### 6.1 Simultaneous unimodular operations and their sign

In the right block, replace each column $j\ge1$ by


$$
\text{old column }j+\text{old column }j-1,
$$


simultaneously. This is a unit-triangular integer column operation. It leaves right column $0$ unchanged and turns every other right column into a complete return column.

Move right column $0$ past the $k$ contact columns. This contributes the sign $(-1)^k$.

Now apply the simultaneous row operation


$$
\text{new row }0=\text{old row }0,\qquad
\text{new row }r=\text{old row }r+\text{old row }r-1.
$$


Its matrix is unit lower-bidiagonal. The period vector becomes $e_0$.

Thus, with no unspecified sign,


$$
F_k(s):=(-1)^kH_k(s)
=
\det\begin{pmatrix}
\Lambda_k(s-1)&b\\
d&B
\end{pmatrix}.
\tag{6.1}
$$


Here $N=2k-1$, and


$$
b=(c_0,\ldots,c_{k-1},\Lambda_k\tau_0,\ldots,\Lambda_k\tau_{k-2}),
$$




$$
d_m=\Lambda_k\tau_m,
$$


while $B$ has contact columns $\sigma_{m+j}$ and return columns


$$
\Lambda_k(\tau_{m+j}+\tau_{m+j-1}),
\qquad 1\le j<k.
$$



Writing


$$
D=\det B,\qquad L=b\operatorname{adj}(B)d,
$$


gives


$$
F_k(s)=\Lambda_k(s-1)D-L,
$$


and therefore


$$
\boxed{G_k=\gcd(|\Lambda_kD|,|L|).}
\tag{6.2}
$$



Deleting the period column gives a unimodular row transform of $Z_k$. Deleting the period row, then undoing the triangular return-column operation and reordering columns, gives $Y_k$. Hence


$$
\mathscr R_k
=\gcd\bigl(|D|,\text{entries of }b\operatorname{adj}(B)\bigr),
\tag{6.3}
$$




$$
\mathscr L_k
=\gcd\bigl(|D|,\text{entries of }\operatorname{adj}(B)d\bigr).
\tag{6.4}
$$



The largest return index is $3k-3$, ending at the original moment $3k-2$. No terminal row has been added.

### 6.2 Bordered-content lemma, including cancellation

For an integral nonsingular $N$-square $B$, define


$$
g=\gcd(|D|,|b\operatorname{adj}(B)d|),
$$


and $R,C$ by the analogues of (6.3)–(6.4). Then


$$
\boxed{\operatorname{lcm}(R,C)\mid g\mid RC.}
\tag{6.5}
$$



The lower divisibility is immediate.

For the upper divisibility, work over $\mathbb Z_p$, transform $B$ to Smith form, and absorb unit factors into the borders. Let the diagonal entries be $p^{s_i}$, and put


$$
S=\sum_i s_i,\quad b_i^*=v_p(b_i),\quad d_i^*=v_p(d_i).
$$


Then


$$
r=v_p(R)=\min\left(S,\min_i(S-s_i+b_i^*)\right),
$$




$$
c=v_p(C)=\min\left(S,\min_i(S-s_i+d_i^*)\right).
$$



If $r+c\ge S$, then $v_p(g)\le S\le r+c$. This step permits arbitrary balanced cancellation.

If $r+c<S$, indices attaining $r$ and $c$ must coincide. Distinct indices $i,j$ would give


$$
r+c\ge2S-s_i-s_j\ge S.
$$


At the common index $i$, the corresponding summand of


$$
b\operatorname{adj}(B)d=\sum_l b_ld_l p^{S-s_l}
$$


has valuation


$$
r+c-(S-s_i)<s_i.
$$


Every other summand has valuation at least $s_i$. Thus the least term cannot cancel, and


$$
v_p(g)=r+c-(S-s_i)\le r+c.
$$


This proves (6.5).

### 6.3 New separated-depth refinement

In the last case, $s_i>S/2$, so $s_i$ is the unique largest Smith exponent. Therefore


$$
S-s_i=v_p(\delta_{N-1}(B))=t_B.
$$


The same least-term calculation proves


$$
v_p(L)=r+c-t_B<S.
$$


Since


$$
v_p(\Lambda_kD)\ge S,
$$


we obtain (1.1):


$$
\boxed{
r+c<S\quad\Longrightarrow\quad
v_p(G_k)=r+c-t_B.
}
\tag{6.6}
$$



This is stronger than the upper divisibility in this separated range, but does not evaluate $t_B$ uniformly.

### 6.4 Application to $G_k$

For integers $D,L,\Lambda$,


$$
\frac{\gcd(\Lambda D,L)}{\gcd(D,L)}\mid\Lambda.
$$


Applying this to (6.2) and using (6.5) proves


$$
\boxed{
\operatorname{lcm}(\mathscr R_k,\mathscr L_k)
\mid G_k
\mid\Lambda_k\mathscr R_k\mathscr L_k.
}
\tag{6.7}
$$



The hypothesis $D\ne0$ is equivalent to $H_{1,k}\ne0$. It is validated on the supplied nonvanishing domain, hence at every original index.

For $p>6k-4$, $\Lambda_k$ is a unit, so


$$
p\nmid G_k
\iff
\operatorname{rank}_{\mathbb F_p}Z_k=2k-1
\ \text{and}\
\operatorname{rank}_{\mathbb F_p}Y_k=2k-1.
\tag{6.8}
$$



If $B$ has at most one nonunit Smith invariant, the Smith calculation gives


$$
\boxed{
v_p(G_k)=\min(S,r+c).
}
\tag{6.9}
$$


When $r+c<S$, this follows from $t_B=0$. When $r+c\ge S$, every summand of the bordered scalar has valuation at least $S$, so the gcd depth is exactly $S$.

The extra rank hypothesis is therefore real. Without it, even matrices with the same $D,R,C$ can have different gcd depths because their least terms can cancel.

Finally, Laplace expansion and (3.10) give


$$
2^{k(k-1)}\prod_{r=0}^{k-2}(r!)^2\mid\mathscr R_k,
$$




$$
2^{(k-1)(k-2)}\prod_{r=0}^{k-3}(r!)^2\mid\mathscr L_k.
\tag{6.10}
$$


For $Y_k$, its contact block is an integral row transform of the original contact matrix, so Cauchy–Binet validates the contact-minor payment.

---

## 7. A finite original-object check of the extra Smith hypothesis

The following small exact example checks the algebraic distinction in the actual compact objects. It is an auxiliary $k=2$ calculation, not an original-index result, and not a proposed repetition of the coordinator’s $k=5$ diagnostic.

Here $\Lambda_2=105$, and


$$
(c_0,\ldots,c_4)=(0,2,8,266,14832),
$$




$$
(\Lambda_2\tau_0,\ldots,\Lambda_2\tau_3)
=(105,-2590,-78036,-4309140).
$$


Thus


$$
Z_2=
\begin{pmatrix}
0&2&105\\
2&8&-2590\\
8&266&-78036\\
266&14832&-4309140
\end{pmatrix},
$$




$$
Y_2=
\begin{pmatrix}
2&10&105&-2590\\
10&274&-2590&-78036\\
274&15098&-78036&-4309140
\end{pmatrix}.
$$



Two maximal minors of $Z_2$ are


$$
319844,\qquad18749960,
$$


and


$$
-896099(319844)+15286(18749960)=4.
$$


All maximal minors are divisible by $4$, by the proved contact-minor theorem. Hence


$$
\mathscr R_2=4.
$$



The four maximal minors of $Y_2$, in column order, are


$$
44120832,\quad15470336,\quad12604724888,\quad5074954360.
$$


Their gcd is $56$. For example, the first two have gcd $1792$, and the third reduces that gcd to $56$; the fourth is also a multiple of $56$. Therefore


$$
\mathscr L_2=56.
$$



The period-isolated block and borders are


$$
B=
\begin{pmatrix}
2&10&-2485\\
10&274&-80626\\
274&15098&-4387176
\end{pmatrix},
\quad
b=(0,2,105),
\quad
d=(105,-2590,-78036)^T.
$$


Direct arithmetic gives


$$
D=59591168,\qquad
b\operatorname{adj}(B)d=29842137136,
$$




$$
H_{1,2}=6257072640,\qquad
H_{0,2}=-36099209776,
\qquad
G_2=112.
$$



At $p=2$,


$$
S=9,\quad r=2,\quad c=3,\quad v_2(G_2)=4.
$$


The matrix $B\bmod2$ has rank $1=N-2$, and


$$
v_2(\delta_2(B))=1.
$$


Thus the new separated formula gives


$$
r+c-t_B=2+3-1=4,
$$


whereas the unjustified formula $\min(S,r+c)$ would give $5$.

This is not a large-prime counterexample to A5 Turn 2. It is a finite example, inside the actual producer and with $\Lambda_2$ a $2$-adic unit, showing exactly why the additional Smith-rank condition cannot simply be omitted.

---

## 8. Audit of the $(k+1)$-square local reduction

Fix $p>6k-4$. Define the integral unit matrix $V$ by


$$
V_0=e_0,\qquad V_j=e_j-(-1)^je_0\quad(j\ge1).
$$


Then


$$
v^TV=e_0^T,\qquad\det V=1.
$$



The positive-contact theorem supplies a unit $k$-minor of $U_kV$. Consequently, ordinary elimination using only $p$-adic units produces


$$
S\in\mathrm{GL}_{2k}(\mathbb Z_p),
\qquad
SU_kV=\binom{I_k}{0}.
\tag{8.1}
$$


No global integer clearer for $S$ is being asserted.

Write


$$
Sw=\binom{a}{b},
\qquad
S(r_{m+j})V=\binom{\mathsf A}{\mathsf B},
$$


and set


$$
h=1-a_0,\qquad r=e_0^T\mathsf A,\qquad\eta=\det S.
$$


The atom is exactly


$$
SC_kV=
\binom{I_k-ae_0^T}{-be_0^T}.
$$



Apply $V$ to both column blocks. Then add $s\Lambda_k$ times each contact column to its corresponding right column. The identity used is


$$
r_n+s w_n+s c_n=r_n+s u_n.
$$


In particular, $r_n=-f_n+4\rho_n$ remains complete.

Expanding along contact columns $1,\ldots,k-1$ has positive sign: the deleted row and column index sums agree. It gives


$$
\boxed{
\frac{\eta H_k(s)}{\Lambda_k^k}
=
\det\begin{pmatrix}
h&r+s e_0^T\\
-b&\mathsf B
\end{pmatrix}.
}
\tag{8.2}
$$



If $c=\operatorname{adj}(\mathsf B)b$, then


$$
\boxed{
\frac{\eta H_{0,k}}{\Lambda_k^k}
=h\det\mathsf B+rc,
\qquad
\frac{\eta H_{1,k}}{\Lambda_k^k}=c_0.
}
\tag{8.3}
$$


Every division here is by a $p$-adic unit.

The contact determinantal divisor satisfies


$$
v_p(\delta_k(C_k))
=\min\bigl(v_p(h),v_p(b_0),\ldots,v_p(b_{k-1})\bigr),
\tag{8.4}
$$


because after eliminating the other top entries of contact column $0$, its only nonunit-coordinate candidates are $h,-b_0,\ldots,-b_{k-1}$.

The three cofactor cases in A5 Turn 2 follow:

- If $\mathsf B$ is invertible, the coefficient pair is nonzero precisely when
  

$$
\left(e_0^T\mathsf B^{-1}b,\ h+r\mathsf B^{-1}b\right)\ne(0,0).
$$


- If $\operatorname{rank}\mathsf B=k-1$, writing
  

$$
\operatorname{adj}(\mathsf B)=\gamma xy^T,\qquad\gamma\ne0,
$$


  the pair is nonzero precisely when
  

$$
y^Tb\ne0,\qquad (x_0,rx)\ne(0,0).
$$


- If $\operatorname{rank}\mathsf B\le k-2$, both coefficients vanish.

This is a valid reduction, but not an evaluated solution of the mixed rank/cofactor problem.

### Why the forcing certificate still does not transfer

A mixed right relation in $Z_k$ has the form


$$
C_kx+Ty=0.
$$


The complete forcing identity gives


$$
4\Lambda_k\mathcal D\,y=Vy-C_kx.
\tag{8.5}
$$


Neither term on the right is separately zero. Thus invertibility of a Cauchy forcing minor cannot be applied as though $\mathcal D y=0$.

Applying a moment recurrence introduces precisely the $J$- and $J^2$-weighted combinations displayed in Section 5. Their elimination requires genuine interpolation information. No supplied proof pays that information with an evaluated unit or a sufficiently small content bound.

---

## 9. New paid-transfer splitting theorem

### 9.1 The complete adjacent construction is unchanged

Use the nested ordering


$$
T_0,C_0,T_1,C_1,\ldots
$$


with entries


$$
\mathscr M_{0,T_0}=s-1,\qquad
\mathscr M_{r,T_0}=\tau_{r-1},
$$




$$
\mathscr M_{0,C_j}=c_j,\qquad
\mathscr M_{r,C_j}=\sigma_{r+j-1},
$$




$$
\mathscr M_{0,T_j}=\tau_{j-1}\quad(j\ge1),
$$




$$
\mathscr M_{r,T_j}
=\tau_{r+j-1}+\tau_{r+j-2}\quad(r,j\ge1).
$$



For the adjacent pair put


$$
\lambda=\Lambda_{k+1},\qquad t=\lambda/\Lambda_k,
\qquad
\omega_k=(-1)^{k(k+1)/2}.
$$


After multiplying every $T$-column by $\lambda$,


$$
F=\omega_k t^kH_k,\qquad
F^+=\omega_{k+1}H_{k+1}.
$$


Their actual contents are


$$
\operatorname{cont}(F)=t^kG_k,\qquad
\operatorname{cont}(F^+)=G_{k+1}.
\tag{9.1}
$$



The complete new corner is


$$
\begin{pmatrix}
\lambda(\tau_{3k-1}+\tau_{3k-2})&\sigma_{3k-1}\\
\lambda(\tau_{3k}+\tau_{3k-1})&\sigma_{3k}
\end{pmatrix}.
$$


Its physical terminal is moment $3k+1$, factorial $(6k+2)!$, and odd denominator $6k+1$.

Using the complete Schur blocks, write


$$
D_{\rm tr}^{\,2}F^+=\mathcal K F-\mathcal T.
\tag{9.2}
$$


The established nonvanishing domain validates $D_{\rm tr}\mathcal K\ne0$.

Set


$$
g_{\rm tr}=\gcd(D_{\rm tr}^2,|\mathcal K|,|\mathcal T|),
$$




$$
\alpha=\mathcal K/g_{\rm tr},\quad
\beta=-\mathcal T/g_{\rm tr},\quad
\chi=D_{\rm tr}^2/g_{\rm tr}.
$$


Then


$$
\chi F^+=\alpha F+\beta,
\qquad
\gcd(|\alpha|,|\beta|,\chi)=1.
\tag{9.3}
$$



### 9.2 The primitive forward and inverse clearers are coprime

Taking constant coefficients in (9.2) shows that


$$
\gcd(D_{\rm tr}^2,|\mathcal K|)\mid\mathcal T.
$$


Therefore


$$
\boxed{
g_{\rm tr}=\gcd(D_{\rm tr}^2,|\mathcal K|),
\qquad
\gcd(|\alpha|,\chi)=1.
}
\tag{9.4}
$$



Equivalently, any common divisor of $\alpha,\chi$ would divide $\beta$ by (9.3), contradicting primitive triple content.

Thus $\chi$ is already the reduced denominator of the slope ratio, and $|\alpha|$ is the reduced denominator of the inverse slope ratio. The complete intercept remains present through $\beta$.

This also means that the paid triple can be recovered from the two integral affine coefficient pairs without recomputing Schur determinants. If


$$
F=F_0+F_1s,\qquad F^+=F_0^++F_1^+s,
$$


and


$$
d_s=\gcd(|F_1|,|F_1^+|),
$$


then


$$
\chi=\frac{|F_1|}{d_s},\qquad
\alpha=\frac{\operatorname{sgn}(F_1)F_1^+}{d_s},
\qquad
\beta=\chi F_0^+-\alpha F_0.
\tag{9.5}
$$



### 9.3 Exact truncated content identities

Put


$$
g=t^kG_k,\qquad g^+=G_{k+1}.
$$



The slope relation is


$$
\chi F_1^+=\alpha F_1.
$$


Because $\gcd(\alpha,\chi)=1$,


$$
\chi\mid F_1,\qquad \alpha\mid F_1^+.
$$



Modulo $\chi$, the constant relation gives


$$
\alpha F_0\equiv-\beta\pmod\chi.
$$


Multiplication by $\alpha$ is invertible modulo $\chi$, so


$$
\gcd(\chi,g)
=\gcd(\chi,F_0,F_1)
=\gcd(\chi,\beta).
$$


Similarly, reduction modulo $\alpha$ gives


$$
\gcd(|\alpha|,g^+)=\gcd(|\alpha|,\beta).
$$



This proves (1.3). Prime by prime,


$$
\min(v_p(\chi),v_p(g))
=\min(v_p(\chi),v_p(\beta)),
$$




$$
\min(v_p(\alpha),v_p(g^+))
=\min(v_p(\alpha),v_p(\beta)).
\tag{9.6}
$$



These are exact even in the balanced-cancellation case. They determine content depth up to the corresponding paid clearer, but do not bound additional depth beyond it.

### 9.4 Actual primitive-denominator divisors

Since $|F_1|/g=q_k$ and $|F_1^+|/g^+=q_{k+1}$,


$$
\boxed{
\frac{\chi}{\gcd(\chi,|\beta|)}\mid q_k,
\qquad
\frac{|\alpha|}{\gcd(|\alpha|,|\beta|)}\mid q_{k+1}.
}
\tag{9.7}
$$



There are also paid content divisors:


$$
\boxed{
\frac{\gcd(\chi,|\beta|)}
{\gcd(\gcd(\chi,|\beta|),t^k)}
\mid G_k,
\qquad
\gcd(|\alpha|,|\beta|)\mid G_{k+1}.
}
\tag{9.8}
$$


When combining the first of these with $\mathcal P_k\mid G_k$, only their **lcm** is immediately justified; their product must not be presumed.

At an original index $K_u$, (9.7) and the accepted ordinary-error lower bound yield (1.5). The error is still the whole error at $K_u$, not at the auxiliary adjacent index $K_u+1$.

### 9.5 Balanced cancellation has not disappeared

Writing


$$
F=g(f_0+f_1s),\qquad \gcd(f_0,f_1)=1,
$$


and


$$
a=v_p(\alpha),\quad b=v_p(\beta),\quad
c=v_p(\chi),\quad m=v_p(g),
$$


one has, if $a+m\ne b$,


$$
c+v_p(G_{k+1})=\min(a+m,b).
$$


At equal depth,


$$
c+v_p(G_{k+1})
=a+m+\min\bigl(v_p(f_1),v_p(uf_0+v)\bigr),
$$


where $u=\alpha g/p^{a+m}$ and $v=\beta/p^b$ are units.

The new splitting theorem does not license deletion of this balanced constant-term cancellation.

---

## 10. A bounded follow-on check using only closed arithmetic

The completed $11\to12$ certificate supplies


$$
|\alpha_{11}|=2^{73}3^65^411^2A_{11},
$$




$$
\chi_{11}=47^253^259^261^2C_{11},
$$


where $A_{11},C_{11}>1$, and both residuals are coprime to every prime at most $67$.

Their nonunit values refute the unrestricted paid Schur $S$-unit assertion. They do not by themselves say whether these primes occur in final content or primitive denominators.

The new theorem resolves that distinction by two scalar gcds.

### Inputs

Use the already certified exact integers


$$
A_{11},\qquad C_{11},\qquad\beta_{11}.
$$


No determinant or Smith computation is required.

These are bounded mathematical inputs: they arise from the already specified $24$-square complete construction through moment $34$, factorial $68!$, and odd denominator $67$. If an explicit size bound is desired, one may bound every coefficient-entry of the paid nested matrix by


$$
M=16(68!)^2.
$$


The usual Leibniz bounds then give finite explicit bounds for $D_{\rm tr},\mathcal K,\mathcal T$, hence for all three primitive transfer integers.

### Requested outputs

Compute only


$$
d_C=\gcd(C_{11},|\beta_{11}|),
\qquad
d_A=\gcd(A_{11},|\beta_{11}|),
\tag{10.1}
$$


with Bézout certificates.

The expected verifiable conclusions are


$$
\boxed{
\gcd(C_{11},G_{11})=d_C,
\qquad
\gcd(A_{11},G_{12})=d_A,
}
\tag{10.2}
$$


and


$$
\boxed{
C_{11}/d_C\mid q_{11},
\qquad
A_{11}/d_A\mid q_{12}.
}
\tag{10.3}
$$


Here $C_{11}$ is coprime to $t^{11}$, because all primes in $t$ are at most $67$.

No unrestricted factorization is needed.

- If $d_C>1$, there is an auxiliary large-prime divisor of $G_{11}$.
- If $d_A>1$, there is an auxiliary large-prime divisor of $G_{12}$.
- If both gcds equal $1$, all primes in these two particular residuals are excluded from the corresponding final contents and are forced into the corresponding primitive denominators.

A nonunit output would locate a genuine failure of one of the corresponding actual rectangular saturation conditions through (6.8). It would still be only an auxiliary $k=11$ or $12$ result: it would not establish a failure on $k\ge32$, an eventual failure, or an original-index failure.

This is different from the coordinator’s new $k=5$ rectangular diagnostic and does not repeat the closed $11\to12$ determinant calculation.

---

## 11. Whole errors and the same infinite original indices

The original compact index set remains


$$
\mathcal O=\{K_u=9^{18+32u}:u\ge0\},
\qquad K_{u+1}=9^{32}K_u.
$$



At those indices,


$$
0<\ell_{K_u}
=\frac{|H_{K_u}(e+\pi)|}{G_{K_u}}.
$$



The two-border theorem gives


$$
\frac{|H_{K_u}(e+\pi)|}
{\Lambda_{K_u}\mathscr R_{K_u}\mathscr L_{K_u}}
\le\ell_{K_u}
\le
\frac{|H_{K_u}(e+\pi)|}
{\operatorname{lcm}(\mathscr R_{K_u},\mathscr L_{K_u})}.
\tag{11.1}
$$


These are bounds for the original whole error, not alternative normalizations.

For adjacent compact indices, the fully paid identities remain


$$
\Delta_k
=\frac{\lambda|\mathcal T|}
{|D_{\rm tr}|\,t^kG_kG_{k+1}},
$$




$$
\frac{\Delta_k}{q_{k+1}}
=\frac{|\mathcal T|}{t^kG_k|\mathcal K|},
$$


and, for $k\ge64$,


$$
\frac{\Delta_k}{q_{k+1}}<\ell_k
\le\frac43\frac{\Delta_k}{q_{k+1}}.
\tag{11.2}
$$


Both final gcds occur before division by the actual $q_{k+1}$.

For two consecutive original indices,


$$
\Delta_u^{\mathcal O}
=
\frac{
H_{0,K_u}H_{1,K_{u+1}}
-H_{0,K_{u+1}}H_{1,K_u}
}{
G_{K_u}G_{K_{u+1}}
}>0.
\tag{11.3}
$$


Selecting the endpoint with smaller actual denominator gives


$$
0<\ell_{i_{\mathcal O}(u)}
\le
\sqrt{\frac{42\Delta_u^{\mathcal O}}{A^{K_u-1}}},
\qquad
i_{\mathcal O}(u)\in\{K_u,K_{u+1}\}.
\tag{11.4}
$$


Thus


$$
\Delta_u^{\mathcal O}=o(A^{K_u-1})
$$


on a specified infinite set would prove irrationality.

Conversely, an upper bound


$$
\log\mathscr R_k+\log\mathscr L_k
\le(4-\eta)k^2\log k+O(k^2)
$$


on the required original indices would force whole-error divergence there. That would diagnose failure of this family’s primitive decay, not prove rationality.

Neither conclusion has been established.

---

## 12. Normalization and separate-producer ledger

For the rational polynomial $H_k/\Lambda_k^k$, define


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


Its actual least simultaneous coefficient clearer remains


$$
\frac{\Lambda_k^k}{d_{H,k}},
$$


and its remaining content is


$$
\frac{G_k}{d_{H,k}}.
$$



No nonsaturated contact frame has been substituted. The separate saturation payment involving the leading contact determinant and the rectangular contact determinantal divisor has not been assigned a guessed value.

The separate binary producer also remains unchanged:


$$
b=9^{18+32u},\qquad n=4002b.
$$


Its contact indices are $0,\ldots,b-1$; its physical reconstruction includes $0,\ldots,b$, with


$$
z_b=0.
$$



Its complete columns remain


$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0.
$$


The return is


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
$$


and the retained paid estimate is only


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$



The norm $Q=x_0^Tx_0$, corrected-column contents, least simultaneous clearer, and final all-prime scalar gcd of that producer remain unevaluated here. Its known valuation


$$
v_3(q^{\rm bin})=n-\frac{b+15}{2}
$$


is not transferred to $q_k$.

---

## 13. Final status ledger

| Item | Status |
|---|---|
| Positive-contact rank for every $p>k$ | **Proved; independently checked**, including degree cancellation, characteristic-$p$ pole order, and the finite boundary |
| Atom-retaining complete-contact corollary | **Proved**, but only rank $\ge k-1$, not full rank |
| Cauchy forcing determinant, clearers, contents, support and valuation formula | **Proved and evaluated** |
| Product contact divisor, including shared powers of $2$ | **Proved; independently checked** |
| Period-isolating operations and signs | **Verified**; $F_k=(-1)^kH_k$ in the stated ordering |
| Two actual rectangles and $\operatorname{lcm}(\mathscr R_k,\mathscr L_k)\mid G_k\mid\Lambda_k\mathscr R_k\mathscr L_k$ | **Proved** when $H_{1,k}\ne0$ |
| Exact depth formula under one nonunit Smith invariant of $B$ | **Proved conditionally on that extra rank hypothesis** |
| New separated-depth formula (1.1) | **Proved** |
| Unit-local $(k+1)$-square reduction | **Proved**, with atom and complete right correction retained |
| Uniform unit/saturation certificate for $Y_k,Z_k$ | **Open** |
| Unrestricted paid Schur $S$-unit conjecture | **Finitely false**, by the closed $11\to12$ certificate |
| Old content envelope | **Finitely false**, by the closed $32/33$ certificates; not restored here |
| New paid-transfer splitting and actual denominator divisors | **Proved** |
| Two new scalar gcds in Section 10 | **Bounded auxiliary check, not executed here** |
| Primitive whole-error decay or divergence on the original infinite indices | **Open** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

### Exact remaining bottleneck

The missing uniform theorem is still an evaluated all-prime control of the actual maximal-minor contents of $Y_k$ and $Z_k$, or an equivalent evaluated control of the local projected right block and its cofactor pair.

The positive-contact ODE proof does not supply the missing weighted-column relations. The Cauchy forcing determinant does not eliminate the factorial-return term in a mixed relation. The paid affine recurrence does not eliminate $\beta_k$, balanced cancellation, or the actual final contents.

The new splitting theorem provides a concrete advance: it separates paid Schur primes, to an exact truncated depth, between **actual final content** and **unavoidable actual primitive denominator factors**. The two-gcd diagnostic can exploit that advance without repeating any closed expensive calculation. It does not yet provide the infinite arithmetic estimate needed to decide the whole errors at the original indices, and it does not decide the rationality of $e+\pi$.
