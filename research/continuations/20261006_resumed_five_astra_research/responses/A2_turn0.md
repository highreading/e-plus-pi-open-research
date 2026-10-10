> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — A finite-binomial reduction of the complete weighted defect

## Executive assessment

The supplied work does not settle whether $e+\pi$ is rational or irrational. The original-family $29$-adic alignment law also remains open.

This report advances the latter problem by reducing the complete contact-inverted output calculation to a **polynomial-sized family of one-dimensional, finitely truncated hypergeometric kernels**. The reduction retains:

- the original indices
  

$$
b=3^{249005515+574312172u},\qquad n=2001b,\qquad u\ge0;
$$


- all source rows $1,\ldots,b-2$;
- the complete first force;
- both complete initial charges of the second force;
- the finite contact-inverse correction;
- the squared-binomial reconstruction metric;
- the separate reconstructed coordinate $j=b$.

The main new result is the following.

> **Complete finite-binomial kernel reduction.**  
> At precision $29^K$, each of the four actual contact solutions
> 

$$
> A^{-1}f^0,\quad A^{-1}h^{(0)},\quad A^{-1}h^{(1)},\quad A^{-1}\tau
>
$$


> has a finite representation by atoms
> 

$$
> \binom jr\binom{-\sigma n-a}{b+v-j},
> \qquad \sigma\in\{0,1,2\},
>
$$


> with $a,r,|v|=O(K)$. The representation is obtained with explicit finite-boundary identities and without nonunit modular division. Its actual weighted pairings reduce to a table of $O(K^5)$ scalar finite sums.

This is not another unrestricted characteristic-zero closure result. It applies to the **specific finite operator path** in the accepted contact inverse and to the **complete particular input**. Nor is it yet a feasible original-index algorithm: the remaining scalar kernels have their true upper endpoint $b-1$, and their high-index evaluation is unresolved.

The exact local bottleneck is now a complete, one-dimensional kernel problem rather than a multivariate rational-coefficient problem. No vanishing at the true norm depth is claimed.

No tools were executed.

---

## 1. Domain, complete data, and reused results

Set $p=29$. The original family is


$$
a=432827+682892t,\qquad t=364+841u,\qquad u\ge0,
$$


so that


$$
b=3^{249005515+574312172u},\qquad n=2001b.
$$



The domains remain:



$$
0\le i,j<b \quad\text{for contact coordinates},
$$




$$
1\le i\le b-2 \quad\text{for recurrence rows},
$$




$$
0\le j\le b \quad\text{for reconstructed coordinates}.
$$



Write


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
W_j=\binom{n+2}{j}.
$$


The reconstruction is


$$
(\mathcal Rx)_j=W_j(jx_{j-1}-x_j),
$$


with $x_{-1}=x_b=0$ used only for reconstruction. Thus


$$
(\mathcal Rx)_0=-x_0,\qquad
(\mathcal Rx)_b=bW_bx_{b-1}.
$$



The actual columns are


$$
A\theta=f^0,\qquad A\psi=\mathbf r,
$$




$$
Z_w=\mathcal R\theta,\qquad
Y=\mathcal R\psi+W_be_b.
$$


Consequently


$$
\mathcal N=Z_w^TZ_w,\qquad
\mathcal C=Z_w^TY.
$$



The metric is the actual finite matrix


$$
L=\mathcal R^T\mathcal R,
$$


and


$$
\Gamma=A^{-T}LA^{-1}.
$$


In particular,


$$
L_{b-1,b-1}=W_{b-1}^2+b^2W_b^2.
$$



### 1.1 Complete first force

The first force is not replaced by a reference column:


$$
\boxed{
f_i^0=\frac{(n+i)!}{n!}J_i,\qquad
J_i=[t^n](1+2t+2t^2)^n(1+t)^i.
}
\tag{1.1}
$$



Its homogeneous recurrence and its support bound are reused at their established scopes:


$$
\mathcal Df^0=0,\qquad
f_i^0\equiv0\pmod{p^K}\quad(i\ge pK).
$$



Thus its input head has length


$$
L_f=\min(b,29K).
$$


This is a precision truncation of the actual force, not a substitution of a simpler force.

### 1.2 Complete second force

The recurrence decomposition remains


$$
\mathbf r=r_0h^{(0)}+r_1h^{(1)}+\tau,
$$


where


$$
(h^{(0)}_0,h^{(0)}_1)=(1,0),\qquad
(h^{(1)}_0,h^{(1)}_1)=(0,1),
$$


and


$$
\tau_0=\tau_1=0,\qquad \mathcal D\tau=\mathcal H.
$$



The complete initial values are


$$
\boxed{
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}\right),
\qquad i=0,1,
}
\tag{1.2}
$$


where


$$
a_s(n)=[z^s]\phi(z)^n,
$$




$$
T_m=\frac1{b!}\sum_{q=b}^{m}(m)_{\underline q},
$$




$$
L_0=0,\qquad
L_m=mL_{m-1}+2(m-1)!u_{m-1},
\qquad
u_r=[z^r]\phi(z)^{-1}.
$$



These formulas retain the factorial subtraction and the logarithmic initial contribution.

The complete source is


$$
\boxed{
\mathcal H_i=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b},
\qquad 1\le i\le b-2.
}
\tag{1.3}
$$



### 1.3 Reused inverse and memory

The accepted $58K+1$ memory law is reused, not reproved. Put


$$
H=58K+1,\qquad M=29K-1.
$$


Then


$$
\tau_j\equiv
\sum_{d=0}^{H-1}
\mathbf1_{j\ge d+2}\,
q_d(j)\mathcal H_{j-d-1}
\pmod{p^K},
\qquad 0\le j<b,
\tag{1.4}
$$


where


$$
q_d(j)\in\mathbb Z[1/2][n,j],\qquad \deg_jq_d\le d.
$$



The complete finite inverse is also reused. With the notation of Turn 10,


$$
A^{-1}\equiv
\mathsf B-\mathsf U\mathsf S_{\rm end}^{-1}\mathsf V
\pmod{p^K},
\tag{1.5}
$$


where


$$
\mathsf B=\mathsf R\mathsf D\mathsf R\mathsf P_-,
\qquad
\mathsf U=\mathsf R\mathsf D F\overline K,
\qquad
\mathsf V=E\mathsf D\mathsf R\mathsf P_-.
$$


Here


$$
\mathsf R_{jk}=\binom{-n}{k-j},
\qquad
(\mathsf P_-)_{ji}=(-1)^{j-i}\binom ji,
$$


in their finite triangular ranges, and


$$
\mathsf D_{jk}
=
c_{j-k}(n)\binom jk,\qquad
c_s(n)=s![z^s]\phi(z)^{-n},
$$


with $0\le j-k\le M$.

The endpoint matrix satisfies


$$
\mathsf S_{\rm end}\equiv I\pmod p.
$$


Its previously established geometric inverse is retained in the same factor order.

---

## 2. Finite-binomial atoms

For integers $A,B$ and $r\ge0$, define a contact vector


$$
\boxed{
E(A,B;r)_j=\binom jr\binom A{B-j},
\qquad 0\le j<b.
}
\tag{2.1}
$$



Throughout, generalized binomial coefficients have the convention


$$
\binom Ak=0\quad(k<0),
$$


and, for $k\ge0$,


$$
\binom Ak=\frac{A(A-1)\cdots(A-k+1)}{k!}.
$$


For integral $A$, these are integers.

The following two identities are the finite-boundary mechanism of the new reduction.

### Proposition 2.1 — Exact finite upper-transform identity

For every integral $A,B$ and $r\ge0$,


$$
\boxed{
\begin{aligned}
\mathsf R E(A,B;r)
={}&
\sum_{h=0}^{r}\binom{-n}{h}
\Bigg[
E(A-n-h,B-h;r-h)\\
&\qquad-
\sum_{\ell=0}^{B-b}
\binom A{B-b-\ell}
E(-n-h,b+\ell-h;r-h)
\Bigg].
\end{aligned}
}
\tag{2.2}
$$


The inner sum is empty when $B<b$.

In particular, this is not an infinite-convolution identity with its boundary discarded.

#### Proof

For $0\le j<b$,


$$
(\mathsf R E)_j
=
\sum_{t=0}^{b-1-j}
\binom{-n}{t}\binom{j+t}{r}\binom A{B-j-t}.
$$


Use


$$
\binom{j+t}{r}
=
\sum_{h=0}^{r}\binom j{r-h}\binom th,
$$


and


$$
\binom{-n}{t}\binom th
=
\binom{-n}{h}\binom{-n-h}{t-h}.
$$



For a fixed $h$, the unrestricted coefficient convolution gives


$$
\sum_{t\ge0}
\binom{-n}{t}\binom th\binom A{B-j-t}
=
\binom{-n}{h}\binom{A-n-h}{B-j-h}.
$$


This follows from the formal identity


$$
(1+x)^{-n-h}(1+x)^A=(1+x)^{A-n-h};
$$


only finitely many terms can contribute to a fixed nonnegative coefficient.

The actual sum stops at $t=b-1-j$. Its omitted terms have


$$
t=b-j+\ell,\qquad 0\le\ell\le B-b.
$$


They contribute


$$
\binom{-n}{h}
\binom{-n-h}{b+\ell-j-h}
\binom A{B-b-\ell}.
$$


Multiplication by $\binom j{r-h}$, followed by summation over $h$, gives (2.2).

Negative lower indices vanish under the declared convention, including when $h>b-j+\ell$. Thus no supplementary boundary case is hidden in the formula. ∎

### Proposition 2.2 — Divided-power action on an atom

Modulo $p^K$,


$$
\boxed{
\mathsf D E(A,B;r)
=
\sum_{s=0}^{M}
c_s(n)\binom{r+s}{s}
E(A,B+s;r+s).
}
\tag{2.3}
$$



#### Proof

The $j$-th coordinate of the left side is


$$
\sum_{s=0}^{\min(M,j)}
c_s(n)\binom js\binom{j-s}{r}
\binom A{B-j+s}.
$$


Now


$$
\binom js\binom{j-s}{r}
=
\binom{r+s}{s}\binom j{r+s}.
$$


The right side of (2.3) therefore agrees term by term. If $s>j$, its binomial factor is zero, so extending the displayed $s$-sum to $M$ adds nothing. ∎

Both identities use integer binomial coefficients. Neither requires division by $h!$, $r!$, or $s!$ inside $\mathbb Z/p^K\mathbb Z$.

---

## 3. The complete particular input before contact inversion

The source truncates modulo $p^K$ at


$$
S=\min(2n+2,M).
$$


Substituting (1.3) into the complete impulse formula gives


$$
\tau_j\equiv
\sum_{d=0}^{H-1}\sum_{s=0}^{S}
\mathbf1_{j\ge d+2}\,
P_{d,s}(j)\binom{2n+j-d-s}{b},
\tag{3.1}
$$


where


$$
\boxed{
P_{d,s}(j)
=
a_s(n+1)q_d(j)(n+j-d-1)_{\underline s}.
}
\tag{3.2}
$$


Its degree is at most


$$
d+s\le G:=87K-1.
$$



This formula contains every source row that can affect a contact coordinate. Indeed, $j<b$ and $j\ge d+2$ imply


$$
1\le j-d-1\le b-2.
$$



### 3.1 Removing indicators with an explicit head correction

Define an algebraic extension


$$
g_j=
\sum_{d=0}^{H-1}\sum_{s=0}^{S}
P_{d,s}(j)\binom{2n+j-d-s}{b},
$$


and define


$$
\boxed{
\eta_j=
\sum_{\substack{0\le d<H\\j\le d+1}}
\sum_{s=0}^{S}
P_{d,s}(j)\binom{2n+j-d-s}{b}.
}
\tag{3.3}
$$


Then


$$
\boxed{\tau=g-\eta\pmod{p^K},}
\tag{3.4}
$$


and


$$
\eta_j=0\qquad(j\ge H+1).
$$



The extension is only a polynomial/binomial device. Equation (3.3) subtracts every term that would otherwise correspond to a nonexistent source row. No negative source row or additional recurrence row has been introduced.

For generating this correction, the high binomials required are contained in the explicit table


$$
\boxed{
\beta_\delta=\binom{2n+\delta}{b},
\qquad -G\le\delta\le1.
}
\tag{3.5}
$$


There are only $G+2$ such entries. Their evaluation is nevertheless a genuine high-index task; it is not charged as a small-lower-index calculation.

### 3.2 Newton coefficients introduce no nonunit loss

Expand


$$
P_{d,s}(j)=
\sum_{r=0}^{d+s}p_{d,s,r}\binom jr.
\tag{3.6}
$$


The coefficients are


$$
p_{d,s,r}=\Delta^rP_{d,s}(0)\in\mathbb Z_{29}.
$$


Finite differences compute them using addition and subtraction only. No modular division by $r!$ is needed.

For integral $N$,


$$
\boxed{
\mathsf P_-
\left(\binom ir\binom{N+i}{b}\right)
=
E(N+r,b+r;r).
}
\tag{3.7}
$$



#### Proof

Extract $[x^b]$ from


$$
\begin{aligned}
&\sum_{i=0}^{j}
(-1)^{j-i}\binom ji\binom ir(1+x)^{N+i}\\
&\qquad=
\binom jr(1+x)^{N+r}x^{j-r}.
\end{aligned}
$$


This proves (3.7). The argument is formal and valid for negative integral $N$ as well. ∎

Thus the non-head part of $\mathsf P_-\tau$ is an explicit sum of atoms


$$
E(2n-d-s+r,b+r;r).
$$


The head correction $\eta$ remains separately present.

---

## 4. Head inputs and contact-end columns in the same representation

### 4.1 Head inputs

For a head input $h$, supported in $0\le i<L$, the accepted finite formula for $\mathsf R\mathsf P_-h$ can be rewritten as


$$
\boxed{
\mathsf R\mathsf P_-h
=
\sum_{i=0}^{L-1}\sum_{t=0}^{i}
(-1)^{b-1-i-t}
h_i\binom{n+t-1}{t}
E(-n-t-1,b-1-t;i-t).
}
\tag{4.1}
$$



This is the finite formula of Turn 10, expressed with a constant upper binomial parameter. The rewriting uses


$$
\binom{n+b-1-j}{b-1-j-t}
=
(-1)^{b-1-j-t}
\binom{-n-t-1}{b-1-j-t}.
$$



The formula applies to:

- the actual first-force head, of length $L_f$;
- the two homogeneous heads, each of length at most $58K+2$;
- the correction $\eta$, of length at most $58K+2$.

The values in the first-force head are still those of (1.1). Alternatively, they may be generated from the exact $f_0^0,f_1^0$ by their established homogeneous recurrence.

### 4.2 Complete contact-end columns

The accepted endpoint columns are


$$
F_{jr}
=
-\sum_{u=0}^{r}
\binom n{r-u}\binom{-n}{b+u-j}.
$$


Therefore


$$
\boxed{
F_r=
-\sum_{u=0}^{r}\binom n{r-u}E(-n,b+u;0).
}
\tag{4.2}
$$



Applying (2.3) and then (2.2) evaluates $\mathsf R\mathsf D F_r$ in the same atom system. The multiplication by $\overline K$, the endpoint restrictions, and the unit solve $\mathsf S_{\rm end}^{-1}$ are unchanged.

In particular, nothing in this representation permits replacing the endpoint correction by zero.

---

## 5. A bounded atom factorization for the actual four columns

Let


$$
R_*=120K+4.
$$


Consider the finite atom list


$$
\boxed{
\mathcal E_{\sigma,a,v,r}
=
E(-\sigma n-a,b+v;r),
}
\tag{5.1}
$$


where


$$
\sigma\in\{0,1,2\},\qquad
0\le a,r\le R_*,
\qquad
-R_*\le v\le R_*.
$$



Its size is


$$
\boxed{
N_{\rm at}=3(R_*+1)^2(2R_*+1).
}
\tag{5.2}
$$


The list can be redundant; no claim of linear independence is needed.

### Theorem 5.1 — Complete atom factorization

For each


$$
h\in\{f^0,h^{(0)},h^{(1)},\tau\},
$$


there is an explicitly constructible coefficient vector $z_h$ over
$\mathbb Z/p^K\mathbb Z$ such that


$$
\boxed{
A^{-1}h
\equiv
\sum_{\alpha}z_{h,\alpha}\mathcal E_\alpha
\pmod{p^K}.
}
\tag{5.3}
$$



The construction retains the complete finite-end correction in (1.5).

#### Proof

For head inputs, start from (4.1), apply $\mathsf D$, and then apply the final $\mathsf R$.

For the extended particular input, start with (3.6)–(3.7), apply the first $\mathsf R$, then $\mathsf D$, then the final $\mathsf R$, and subtract the transformed head correction $\eta$.

For the contact-end correction, start from (4.2), apply $\mathsf D$ and $\mathsf R$, combine with $\overline K$, and retain the actual coefficients


$$
\mathsf S_{\rm end}^{-1}E\mathsf D\mathsf R\mathsf P_-h.
$$



It remains to verify the parameter bounds.

For a particular-input term, let


$$
0\le d\le58K,\qquad 0\le s\le29K-1,\qquad
0\le r\le d+s.
$$


The first upper transform has a main atom with upper parameter


$$
n-d-s+r-h.
$$


After a divided-power shift $z$, $0\le z\le M$, and the final upper transform, its main upper parameter becomes


$$
-d-s+r-h-h'.
$$


Because


$$
h+h'\le r+z,
$$


this parameter lies between $-G-M$ and $0$.

A boundary atom from the first upper transform has upper parameter $-n-h$. After the final upper transform it has upper parameter either


$$
-2n-h-h'
\quad\text{or}\quad
-n-h'.
$$


Their nonnegative offsets are at most $G+M$.

The polynomial index and the absolute lower-index offset are also at most $G+M$. Since


$$
G+M=116K-2<R_*,
$$


all these terms are in (5.1).

For a head input of length $L\le58K+2$, the largest upper-parameter offset after both remaining operations is at most


$$
L+M\le87K+1.
$$


The polynomial indices and lower-index offsets obey the same bound.

For the endpoint columns, $u\le M-1$, so their lower-index offsets after the two operations are at most $2M$, and their upper-parameter offsets and polynomial indices are at most $M$. Again all bounds are below $R_*$.

Finally, the endpoint solve forms scalar linear combinations of these vectors; it creates no new atom labels. This proves (5.3). ∎

### Scope of the theorem

This is a factorization for the required finite operator path. It is not an assertion that this atom space is invariant under arbitrary repetitions of the operators, weight multiplication, or Cartier sections.

In particular, it does not contradict the characteristic-zero obstructions discussed in the sources, and it does not claim a small reachable prime-power digit module.

---

## 6. The actual weighted metric becomes a one-dimensional kernel table

For an atom


$$
\alpha=(A,v,r),\qquad
E_\alpha(j)=\binom jr\binom A{b+v-j},
$$


define its terminal contact value


$$
\boxed{
e_\alpha=E_\alpha(b-1)
=\binom{b-1}{r}\binom A{v+1}.
}
\tag{6.1}
$$



For $0\le j<b$,


$$
jE_\alpha(j-1)-E_\alpha(j)
=
(r+1)E(A,b+v+1;r+1)_j-E_\alpha(j).
\tag{6.2}
$$


At $j=b$, however, the reconstruction is only


$$
bE_\alpha(b-1).
$$


The term $-E_\alpha(b)$ must not be inserted.

Define the scalar kernels


$$
\boxed{
\begin{aligned}
S_t(A,v;A',v')
={}&
\sum_{j=0}^{b-1}
\binom{n+2}{j}^{\!2}
\binom jt\\
&\qquad\times
\binom A{b+v-j}
\binom{A'}{b+v'-j}.
\end{aligned}
}
\tag{6.3}
$$



These are the remaining high-index contractions.

### 6.1 Integral linearization of the polynomial factors

The product identity


$$
\boxed{
\binom jr\binom js
=
\sum_{h=0}^{\min(r,s)}
\frac{(r+s-h)!}{h!(r-h)!(s-h)!}
\binom j{r+s-h}
}
\tag{6.4}
$$


has integer coefficients. It follows by counting two subsets of sizes $r,s$ according to the size $h$ of their intersection.

Let


$$
P_{r,s}(A,v;A',v')
=
\sum_{j=0}^{b-1}
W_j^2E(A,b+v;r)_jE(A',b+v';s)_j.
$$


Then (6.4) expresses $P_{r,s}$ as an integral linear combination of the kernels (6.3).

### Proposition 6.1 — Complete Gram kernel

The actual reconstructed pairing of two atoms is


$$
\boxed{
\begin{aligned}
G_{\alpha\beta}
={}&(r+1)(r'+1)
 P_{r+1,r'+1}(A,v+1;A',v'+1)\\
&-(r+1)P_{r+1,r'}(A,v+1;A',v')\\
&-(r'+1)P_{r,r'+1}(A,v;A',v'+1)\\
&+P_{r,r'}(A,v;A',v')\\
&+b^2W_b^2e_\alpha e_\beta .
\end{aligned}
}
\tag{6.5}
$$



#### Proof

For rows $0,\ldots,b-1$, substitute (6.2) into


$$
\sum_{j=0}^{b-1}W_j^2
\bigl(jE_\alpha(j-1)-E_\alpha(j)\bigr)
\bigl(jE_\beta(j-1)-E_\beta(j)\bigr).
$$


The four products give the first four lines of (6.5).

The actual row $j=b$ contributes


$$
W_b^2\,bE_\alpha(b-1)\,bE_\beta(b-1),
$$


which is exactly the final line. ∎

This establishes


$$
G_{\alpha\beta}
=(\mathcal R\mathcal E_\alpha)^T
 (\mathcal R\mathcal E_\beta).
$$


It therefore retains the full matrix $L$, including its last diagonal entry.

### 6.2 Size of the complete scalar table

The required parameters can be taken in


$$
A=-\sigma n-a,\qquad
A'=-\sigma'n-a',
$$




$$
0\le a,a'\le R_*,
\quad
-R_*\le v,v'\le R_*+1,
\quad
0\le t\le2R_*+2.
$$


Thus a sufficient number of scalar kernels is


$$
\boxed{
N_{\rm ker}
=
9(R_*+1)^2(2R_*+2)^2(2R_*+3)
=O(K^5).
}
\tag{6.6}
$$



Many of these kernels are unnecessary or identical. The stated count is a uniform upper bound, not a claim that the dense table should be stored.

---

## 7. The complete normalized defect in the new factorization

Let


$$
z_f,\quad z_0,\quad z_1,\quad z_\tau
$$


be the coefficient vectors from Theorem 5.1, and put


$$
z_r=r_0z_0+r_1z_1+z_\tau.
$$


Then


$$
\boxed{
\mathcal N\equiv z_f^TGz_f\pmod{p^K},
}
\tag{7.1}
$$


and


$$
\boxed{
\mathcal C
\equiv
z_f^TGz_r+
bW_b^2\sum_\alpha z_{f,\alpha}e_\alpha
\pmod{p^K}.
}
\tag{7.2}
$$



The second term in (7.2) is the exterior $+1$. It is not included in the contact Gram matrix.

The homogeneous relation for the actual first force gives


$$
A^{-1}f^0
=
f_0^0A^{-1}h^{(0)}+f_1^0A^{-1}h^{(1)}.
$$


The coefficient vectors themselves need not be identical under this relation, because the atom list is redundant. Their evaluated contact vectors, and hence their pairings, are identical.

Therefore the exact local numerator is


$$
\boxed{
\begin{aligned}
\mathcal C-p\rho_n\mathcal N
\equiv{}&
z_f^TG\Bigl(
(r_0-p\rho_nf_0^0)z_0
+(r_1-p\rho_nf_1^0)z_1
+z_\tau
\Bigr)\\
&+bW_b^2\sum_\alpha z_{f,\alpha}e_\alpha
\pmod{p^K}.
\end{aligned}
}
\tag{7.3}
$$



This is a factorization of the actual source-plus-end defect with


$$
\Gamma=A^{-T}LA^{-1}.
$$


It includes all source impulses through the explicitly constructed $z_\tau$.

No block-end vanishing has been used to delete interior impulses.

---

## 8. Resource and division budgets

### 8.1 Relation to Turn 10’s estimates

The previous estimates


$$
V\le32,\qquad D_K=256K+16,\qquad
T_K\le100(29K+2)^4
$$


do not enter this proof.

The accepted rational representation remains valid at its established algebraic scope. Its aggregate task and degree estimates remain author estimates unless separately audited. The present argument instead uses the explicit finite-binomial expansion rules (2.2), (2.3), and (3.7).

### 8.2 Arithmetic construction, separated from high-index evaluation

The following inputs must be distinguished.

**Small-index arithmetic data:**

- $n,b$ to the necessary guarded $29$-adic precision;
- symbol coefficients $a_s(n+1)$, $c_s(n)$;
- recurrence polynomials $q_d$;
- the actual finite endpoint matrices;
- binomial coefficients with lower index $O(K)$.

**Genuine high-index inputs:**

1. the complete $f_0^0,f_1^0$ from (1.1);
2. the complete $r_0,r_1$ from (1.2), unless separately protected;
3. the source-head table (3.5);
4. $W_b=\binom{n+2}{b}$;
5. the kernel values (6.3);
6. the independent $\rho_n$.

A complexity claim that treats the latter as already evaluated is conditional on those inputs. It is not a complete original-index algorithm.

### 8.3 Explicit polynomial construction bound

Put $X=R_*+2$.

For the parameter ranges in the proof:

- one upper-transform application emits fewer than $X^2$ atoms;
- one divided-power application emits fewer than $X$ atoms;
- a source polynomial has fewer than $X$ Newton terms;
- there are fewer than $X^2$ pairs $(d,s)$.

Thus a streamed expansion of the particular input through both upper transforms and the divided-power operator has fewer than $X^8$ elementary emitted terms.

Head transformations, endpoint-column construction, endpoint restrictions, and the finite unit solve have smaller polynomial bounds. Pairing two final coefficient vectors and applying (6.4) requires at most $O(X^7)$ coefficient-accumulation steps, without storing the full atom Gram matrix.

A deliberately loose construction budget is therefore


$$
\boxed{
10^4X^{10}
}
\tag{8.1}
$$


scalar arithmetic operations, including naive generation of the small-index binomial data, once the genuine high-index inputs have been supplied.

A sufficient storage budget for collected coefficient arrays is


$$
\boxed{200X^5}
\tag{8.2}
$$


residue slots. Streaming can reduce it substantially.

These bounds follow from the displayed loop ranges. They are not estimates of the missing kernel evaluation cost, and they are not presented as practical at the original input.

### 8.4 Division budget

The atom identities and Newton conversion use no nonunit modular division.

For a small-index binomial $\binom{x}{k}$, compute


$$
(x)_{\underline k}
$$


at precision


$$
p^{K+v_p(k!)}.
$$


Then remove the demonstrated factor $p^{v_p(k!)}$ and invert only the unit part of $k!$. All small-index binomials needed here can be covered by the guard


$$
\boxed{
v_p((3R_*+3)!).
}
\tag{8.3}
$$


This guard is paid independently for scalar generation; it does not accumulate through the subsequent atom transformations.

The endpoint inverse remains the established finite geometric sum. It does not divide by a contact minor or by part of the primitive norm.

No nonunit division is needed to assemble (7.1)–(7.3).

---

## 9. The remaining scalar kernels are explicit finite hypergeometric sums

The reduction has replaced high-dimensional coefficient extraction by the kernels (6.3). Their summands are now completely specified.

Suppose first


$$
A=-\alpha,\qquad A'=-\alpha',
\qquad \alpha,\alpha'\ge1,
$$


and put


$$
B=b+v,\qquad B'=b+v'.
$$


The summand is zero outside


$$
j_0=t,\qquad
j_0\le j\le J:=\min(b-1,B,B').
$$


If $J<j_0$, the sum is zero.

Within this interval, write the summand as $U_j$. Then


$$
\boxed{
\frac{U_{j+1}}{U_j}
=
\frac{(n+2-j)^2(B-j)(B'-j)}
{(j+1)(j+1-t)(A-B+j+1)(A'-B'+j+1)}.
}
\tag{9.1}
$$


Equivalently, the denominator-cleared identity


$$
\boxed{
\begin{aligned}
&(j+1)(j+1-t)(A-B+j+1)(A'-B'+j+1)U_{j+1}\\
&\qquad=(n+2-j)^2(B-j)(B'-j)U_j
\end{aligned}
}
\tag{9.2}
$$


is exact.

For $A=0$, the factor $\binom0{B-j}$ restricts the sum to $j=B$. Such kernels are single-term evaluations, subject to the actual bounds $0\le B<b$. The same applies if $A'=0$.

### 9.1 The original truncation is not a full Hahn measure

Even though (9.1) is hypergeometric, the upper endpoint is the actual


$$
b-1,
$$


or a smaller support endpoint caused by $v$ or $v'$. It is not generally a standard full orthogonality range.

Consequently, the standard Hahn-class results do not by themselves diagonalize this metric. Identifying a standard measure would require checking both the weights and the complete finite support; that identification has not been proved.

### 9.2 Why direct hypergeometric iteration is not a feasible answer

At many steps, the denominator in (9.1) is divisible by $29$. Its factors cannot simply be inverted modulo $29^K$.

There is an explicit conservative guard for literal forward iteration. Write $F_m=v_p(m!)$. For $j=j_0,\ldots,J-1$, the total denominator valuation is


$$
\boxed{
\begin{aligned}
E_{\rm rat}={}&F_J-F_{j_0}
+F_{J-t}-F_{j_0-t}\\
&+F_{\alpha+B-j_0-1}-F_{\alpha+B-J-1}\\
&+F_{\alpha'+B'-j_0-1}-F_{\alpha'+B'-J-1}.
\end{aligned}
}
\tag{9.3}
$$


Computing the initial value to precision $p^{K+E_{\rm rat}}$, followed by exact removal of each demonstrated nonunit factor, is sufficient for this literal scheme.

That budget can be of original-index size. Numerator cancellation may improve it, but no uniform cancellation theorem has been established here.

Thus:

> The first-order hypergeometric ratio supplies an exact certificate for the summand, but it does not supply a feasible modular summation algorithm.

Classical creative telescoping may be applied to this now-explicit finite summand. A successful application must still provide:

- the actual boundary certificate at $j=t$ and $j=J$;
- specialization rules at singular parameter values;
- every $29$-adic denominator loss;
- original-index cost bounds.

An existence theorem for a telescoper does not establish any of these automatically.

---

## 10. A concrete complete kernel lemma

The following is the reduced open obligation.

> **Complete truncated-binomial kernel lemma — open.**  
> For the actual
> 

$$
> b=3^{249005515+574312172u},\qquad n=2001b,
>
$$


> evaluate modulo $29^K$, or establish suitable exact relations among, the complete family
> 

$$
> S_t(-\sigma n-a,v;-\sigma'n-a',v')
>
$$


> in (6.3), over the parameter box of §6.2, together with the boundary binomials in (3.5) and $W_b$.
>
> The evaluation or relations must preserve the endpoint $b-1$ and have an explicit nonunit-division budget. They must be strong enough to determine the complete scalar combination (7.3), rather than an isolated source or reference term.

This materially reduces the earlier target:

- there are no unevaluated original-length matrix products;
- no adjoint solve remains;
- all contact-end corrections have already entered the coefficient vectors;
- the remaining summation variable is a single original contact index;
- the squared weights and exterior reconstruction are explicit;
- the number of offset parameters is polynomial in $K$.

What remains unproved is a feasible evaluation or an identity forcing the required complete combination to vanish.

A smaller observable table for these kernels would suffice. It must, however, give actual reduction identities for the full scalar combination; merely naming a new state for every shifted sum would not complete the task.

---

## 11. True norm depth and logarithmic protection

The local target is still


$$
\boxed{
\mathcal C-p\rho_n\mathcal N
\equiv0\pmod{p^{d+2}},
\qquad d=v_p(\mathcal N).
}
\tag{11.1}
$$



The norm is positive over the reals and therefore nonzero. This proves $d<\infty$, not a useful upper bound on $d$.

Retain


$$
P=\frac{Z_w}{p^2}=p^cx,
\qquad x\ \text{primitive},
\qquad
\nu=v_p(x^Tx).
$$


Then


$$
d=2c+4+\nu.
$$


The atom factorization does not remove any row content and supplies no bound on $\nu$.

Once a nonzero norm digit is known, the actual normalized certificate is


$$
\delta_{\rm act}
=
\left(\frac{\mathcal C}{p^{d+1}}\right)
\left(\frac{\mathcal N}{p^d}\right)^{-1}
-\rho_n
\pmod p,
\tag{11.2}
$$


provided $v_p(\mathcal C)\ge d+1$. If that inequality fails, alignment already fails.

Only the demonstrated unit $\mathcal N/p^d$ is inverted.

The independent $\rho_n=(6C_n)^{-1}$ must still be supplied from its original definition. The packet does not provide a complete evaluator for $C_n$, and it is not permissible to define $\rho_n$ from the mixed/norm ratio.

### 11.1 Complete logarithmic budget

Retain


$$
N_{\log}
=
2v_p(n!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor.
$$


The established relative protection estimate is


$$
v_p\!\left(\frac MD-\frac{M^{(e)}}D\right)
\ge N_{\log}-c-3-\nu.
$$


Therefore logarithmic omission from the normalized ratio modulo $p$ requires


$$
\boxed{N_{\log}\ge c+4+\nu.}
\tag{11.3}
$$



Until this inequality is certified for the actual norm valuation, the complete $r_0,r_1$ in (1.2) must be used.

---

## 12. Bounded exact arithmetic proposed for inspection

No calculation is required to establish the symbolic identities above. A bounded calculation would audit their implementation.

### Auxiliary complete-kernel test

Use


$$
\boxed{n=203,\qquad b=143,\qquad K=2.}
$$


This is not an original-family index.

The actual auxiliary ranges are:

- contact coordinates $0,\ldots,142$;
- source rows $1,\ldots,141$;
- reconstruction rows $0,\ldots,143$.

#### Inputs

1. The exact contact matrix
   

$$
A_{ij}
   =
   \sum_s a_s(n)(n+i)_{\underline s}
   \binom{2n+i-s}{j}.
$$


2. The complete first force (1.1).
3. The complete source (1.3), without residue-class deletion.
4. The exact $r_0,r_1$ from (1.2).
5. $W_j=\binom{205}{j}$.
6. The accepted finite endpoint data.

Generate the factorial/logarithmic data exactly through


$$
2n+b-1=548.
$$


No original-family logarithmic omission estimate should be substituted for this exact auxiliary generation.

#### New identities to inspect

**A. Finite upper-transform atoms.**

For


$$
r\in\{0,1,2,28,29,57\},
$$




$$
v\in\{-58,-1,0,1,57\},
$$




$$
A\in\{-2n-3,-n,-2,-1,0,n-5,2n+1\},
$$


compare the direct finite transform of $E(A,b+v;r)$ with (2.2), for every contact coordinate.

This includes negative lower-index ranges and nonunit factorial indices.

**Expected output:** zero discrepancies modulo $841$, with the finite tail in (2.2) reported separately.

**B. Complete source decomposition.**

Compare:

- the actual $\tau_j$ generated from rows $1,\ldots,141$;
- the indicator formula (3.1);
- the extended formula $g_j-\eta_j$.

**Expected output:** zero discrepancies for every $0\le j<143$, including $\tau_0=\tau_1=0$.

**C. Complete atom columns.**

Construct all four coefficient vectors in Theorem 5.1 and compare their evaluated contact vectors with the four direct finite solutions.

**Expected output:** zero discrepancies modulo $841$.

This check must retain the complete endpoint correction; it is not another test that replaces it by the identity.

**D. Weighted kernel contraction.**

Compute the norm and mixed contraction in two ways:

1. directly from all reconstructed rows $0,\ldots,143$;
2. from (6.3)–(7.2).

Report separately:

- the sum over $j<143$;
- the contact-column terminal product $b^2W_b^2\theta_{b-1}\psi_{b-1}$;
- the exterior term $bW_b^2\theta_{b-1}$.

**Expected output:** zero discrepancies. No numerical value of a normalized defect is predicted.

These are finite implementation audits only. They establish no original-family norm-relative law.

### What an original certificate would additionally require

An original calculation must supply an actual $u$, all genuine high-index inputs, the independent $\rho_n$, and a precision reaching a nonzero norm digit.

If a bounded computation finds only


$$
\mathcal N\equiv0\pmod{p^{K_{\max}}},
$$


its conclusion is only $d\ge K_{\max}$. It has not tested (11.1).

---

## 13. Source and literature evaluation

The supplied review supports reuse of:

- the finite contact inverse and its factor order;
- the terminal-zero adjoint telescope;
- the actual squared-weight kernel;
- the finite gluing identities;
- the $58K+1$ memory law and complete impulse formulas.

The supplied recurrence receipt is consistent with those scopes. It reports auxiliary complete-source and recurrence-output checks, and no original Gram pair. It is not evidence for norm alignment.

The prime-power rational/diagonal literature is relevant background, but does not by itself furnish a feasible reachable or observable module for the complete kernels here.

The standard Legendre logarithmic companion is not a new result and does not eliminate the initial logarithmic charges.

The Hahn and creative-telescoping literature is relevant to (6.3) and (9.1), but no standard full-measure identification or endpoint-complete, denominator-controlled telescoper is asserted.

No claim of exhaustive global novelty is made. The advance is the explicit application of elementary finite-binomial identities to the complete, boundary-corrected target.

---

## 14. Final gcd, actual primitive denominator, and whole error

The atom representation makes no row-content normalization or lattice saturation change.

Retain the least actual two-column clearer $d_B$, the original weighted integer Gram pair


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


and the final reduction


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
}
\tag{14.1}
$$


The primitive multiplier remains $d_B^2/g_B$.

With


$$
F_m=v_{29}(m!),\qquad
\delta=v_{29}(D),\qquad
\mu=v_{29}(M),
$$


the retained local interface is


$$
v_{29}(g_B)
=
\min\{4F_n+4+\delta,\ 2F_n+F_b+5+\mu\},
$$




$$
\boxed{
v_{29}(q_n)
=
\max\{0,\ 2F_n-F_b-1+\delta-\mu\}.
}
\tag{14.2}
$$



Even a proof of the local alignment law would settle only this selected-prime contribution.

The actual primitive denominator still requires


$$
\boxed{
\log q_n
=
\sum_{\ell}
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{14.3}
$$



For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the relevant evaluated form is the whole same-index quantity


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{14.4}
$$



At the retained scope of the complete signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$


and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$


No componentwise error has been substituted for (14.4).

The present reduction gives no all-prime bound on $q_n$ sufficient to make that whole nonzero form tend to zero.

---

## Proof-status ledger

| Statement | Status |
|---|---|
| Original domain and finite endpoints | Retained exactly |
| Complete first force and complete initial second force | Retained |
| $58K+1$ memory and impulse polynomials | Reused at established scope |
| Complete finite inverse and endpoint unit solve | Reused; not rederived |
| Finite upper-transform atom identity, including its tail | Proved here |
| Divided-power action on atoms | Proved here |
| Complete particular input as an algebraic extension minus an explicit head | Proved here |
| No nonexistent source rows introduced | Verified by the explicit subtraction |
| Four actual contact columns factor through $O(K^3)$ atoms | Proved here |
| Actual reconstructed metric reduces to $O(K^5)$ scalar kernels | Proved here |
| Contact terminal product and exterior $+1$ | Explicitly retained |
| Construction arithmetic and division budgets | Explicit, conditional on genuine high-index inputs |
| Feasible evaluation of the complete scalar kernel table | Open |
| Structural cancellation at the true primitive norm depth | Not proved |
| Original normalized defect | Not computed |
| Logarithmic omission at actual norm-relative precision | Conditional on (11.3) |
| Final all-prime gcd and actual primitive-denominator bound | Open |
| Whole nonzero evaluated form tends to zero | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The new result is a **complete finite-binomial factorization of the actual contact-inverted columns and their weighted source-plus-end defect**.

Its central improvement is the exact finite identity


$$
\mathsf R E(A,B;r)
=
\text{explicit main atoms}
-
\text{explicit finite endpoint atoms},
$$


which, together with the divided-power inverse and the complete impulse formula, reduces the actual $\Gamma$-contractions to one-dimensional truncated hypergeometric kernels.

The exact remaining local bottleneck is to evaluate or relate those complete kernels strongly enough to determine (7.3) at


$$
K=v_{29}(\mathcal N)+2.
$$


Their first-order hypergeometric ratios do not yet provide a feasible modular summation method: nonunit denominator losses and the true finite endpoints remain consequential.

The proposed bounded auxiliary calculation can audit this new reduction. It cannot prove the original-family law.

Even an affirmative local resolution would leave the final all-prime gcd, actual primitive denominator, and whole same-index nonzero error to be compared.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


