> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed differential elimination, a fully evaluated mixed-return certificate, and the remaining finite-tail obstruction

## 1. Executive conclusion

The supplied work does not establish whether $e+\pi$ is rational or irrational. This report also does not resolve that question.

Nor does it prove the requested uniform normality statements


$$
\operatorname{rank}_{\mathbb F_p} Z_k=2k-1,
\qquad
\operatorname{rank}_{\mathbb F_p} Y_k=2k-1
\qquad (p>6k-4).
$$


No actual mixed-family counterexample at such a prime is produced.

There are, however, two new rigorous results.

1. **A sharp obstruction to improving the fixed constant-coefficient differential method.**  
   The constant-coefficient operators used in Turn 3 are of minimal possible order among operators that rationalize the entire corresponding parameter family. Moreover, no larger operator in that class improves the degree-versus-physical-tail comparison. Thus replacing the Turn 3 operator by another fixed constant-coefficient operator cannot, using only universal pole orders and the retained tail length, close the projection gap.

2. **An evaluated arithmetic certificate using the complete mixed returns.**  
   For every $k\ge4$ and every matched pair of columns
   

$$
\bigl(\sigma_{m+j},\,\Lambda_k\tau_{m+j}\bigr),
   \qquad 0\le j<k,
$$


   two explicit integer linear combinations of the first six physical rows have determinant
   

$$
\boxed{2^{15}3^2\Lambda_k.}
$$


   This calculation retains both the factorial forcing and the $4/(2n+1)$ correction. It involves no division by an interpolation pivot.

   It yields a fully evaluated maximal-minor certificate for a precisely specified weighted stack of the actual $Y_k$:
   

$$
\boxed{
   \delta_{2k}(\mathbb Y_k)
   \mid
   (2^{15}3^2\Lambda_k)^k
   \left(\prod_{j=0}^{k-1}j!\right)^4.
   }
$$


   In particular, that stack has full column rank at every prime $p>6k-4$, including $p=6k-1$ when it is prime.

The second result is **not** a normality theorem for $Y_k$. The weighted stack contains additional equations not supplied by an original relation in $Y_k$. Indeed, the result proves that the original kernel cannot be invariant under multiplication of column coefficients by their shift indices. This gives an actual-family obstruction to the otherwise tempting weighted-column closure shortcut.

The remaining obligation is still to control the original, unaugmented finite projection—or its actual all-prime maximal-minor contents.

---

## 2. Original objects, physical boundaries, and normalization

### 2.1 The complete compact construction

Throughout the compact construction,


$$
k\ge2,\qquad 0\le m<2k,\qquad 0\le j<k.
$$


The sequences remain


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad w_n=(-1)^n,
$$




$$
c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-f_n+4\rho_n.
$$



Their complete returns are


$$
\sigma_n=c_{n+1}+c_n=u_{n+1}+u_n,
$$




$$
\boxed{
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{2.1}
$$



Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$


The original affine determinant is


$$
H_k(s)=
\det\left[
(c_{m+j})\ \middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s.
\tag{2.2}
$$



Its physical terminal remains


$$
\boxed{
m+j=3k-2,\qquad (6k-4)!,\qquad 6k-5.
}
\tag{2.3}
$$



The two rectangles under investigation are exactly


$$
Z_k=
\left[
(c_{m+j})_{\substack{m<2k\\j<k}}
\ \middle|\
(\Lambda_k\tau_{m+j})_{\substack{m<2k\\j<k-1}}
\right],
\tag{2.4}
$$


and


$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{m<2k-1\\j<k}}
\ \middle|\
(\Lambda_k\tau_{m+j})_{\substack{m<2k-1\\j<k}}
\right].
\tag{2.5}
$$


Their actual maximal-minor contents are


$$
\mathscr R_k=\delta_{2k-1}(Z_k),
\qquad
\mathscr L_k=\delta_{2k-1}(Y_k).
$$



Whenever $H_{1,k}\ne0$, retain the **all-prime final gcd**


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$


and the actual primitive pair


$$
q_k=\frac{|H_{1,k}|}{G_k},
\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
\tag{2.6}
$$



At every original index


$$
\boxed{
k=K_u=9^{18+32u},\qquad u\ge0,
}
\tag{2.7}
$$


the supplied nonvanishing and positive-error results give


$$
\boxed{
0<\ell_{K_u}
=q_{K_u}(e+\pi)-p_{K_u}
=\frac{|H_{K_u}(e+\pi)|}{G_{K_u}}.
}
\tag{2.8}
$$


Outside the stated positive-error scope, the universally valid identity is the corresponding absolute-value identity; positivity is not inferred merely from $H_{1,k}\ne0$.

### 2.2 Established results reused, not recomputed

The following established results are used only at their proved scope.

- The positive-contact rank theorem applies to $U_k$, not automatically to the complete mixed arrays.
- The bordered-content theorem gives
  

$$
\operatorname{lcm}(\mathscr R_k,\mathscr L_k)
  \mid G_k
  \mid \Lambda_k\mathscr R_k\mathscr L_k
  \tag{2.9}
$$


  when $H_{1,k}\ne0$.
- Turn 3's paid finite-jet transformations identify the requested coefficient-map normality with the original ranks at $p>6k-4$. Their physical factorial payments are units throughout that range, including $p=6k-1$.
- The exact Turn 3 content transfers remain unchanged. In particular, the actual cofactor clearer $\zeta_{Z,k}$ and actual correction $\chi_{Y,k}$ remain paid. Neither is assigned the value $1$.
- The actual individual right-column clearers
  

$$
\Lambda_{k,j}
  =\operatorname{lcm}(1,3,\ldots,4k+2j-3)
$$


  and the actual return-array clearer $\Lambda_k$ are retained.
- The established contact-column contents, divided-contact factorial clearers, and product lower divisor of $G_k$ are not substitutes for $G_k$.

For completeness, the rational polynomial $H_k/\Lambda_k^k$ still has actual least simultaneous coefficient clearer


$$
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}),
$$


and remaining coefficient content $G_k/d_{H,k}$.

No determinant, Smith table, adjacent-transfer calculation, or closed $32/33$ calculation is repeated below.

---

## 3. A new no-go theorem for fixed constant-coefficient rationalization

This section does **not** repeat the Laurent construction or its mixed pole-injectivity proof. It establishes a new minimality property of that construction.

### 3.1 The operator class being tested

Consider a nonzero operator $P(D)\in\mathbb Q[D]$, independent of the coefficient parameters $X,V$, with the following property:

> Applying $P(D)$ to every member of the relevant Turn 3 generating family produces a rational function.

The word “every” is essential. Parameter-dependent differential elimination is not covered by the theorem below.

The local data already established in Turn 3 suffice for the proof:

- at $x=1$, the positive-contact logarithmic coefficient is a nonzero constant multiple of $e^x$;
- at $x=-1$, it is a nonzero constant multiple of $e^{-x}$;
- the arctangent term has a nonzero constant logarithmic coefficient at $x=1$;
- the contact atom remains a rational simple pole at the roots of $x^2+1$;
- the factorial term has a nonzero $x\log x$ leading logarithmic term at $x=0$.

These are characteristic-zero local statements. No infinite characteristic-$p$ arctangent series is used.

### 3.2 Minimality theorem

**Theorem 3.1.**  
For the full $Z_k$ family, every such $P(D)$ is divisible by


$$
\boxed{
D^{2k-3}(D-1)^{2k-1}(D+1)^{2k-1}.
}
\tag{3.1}
$$


For the full $Y_k$ family, every such $P(D)$ is divisible by


$$
\boxed{
D^{2k-1}(D-1)^{2k+1}(D+1)^{2k+1}.
}
\tag{3.2}
$$



Thus the respective minimal orders are $6k-5$ and $6k+1$.

#### Proof

Suppose first that $P(D)$ rationalizes the full $Z_k$ family.

Choose $V=0$ and choose the highest-degree contact coefficient polynomial. The logarithmic monodromy at $x=1$ is a nonzero constant multiple of


$$
x^{2k-2}e^x.
$$


A rational function has zero logarithmic monodromy, so


$$
P(D)(x^{2k-2}e^x)=0.
$$


Equivalently,


$$
P(D+1)x^{2k-2}=0.
$$



If $P(T)$ has a root of multiplicity $s$ at $T=1$, write


$$
P(T+1)=T^sU(T),\qquad U(0)\ne0.
$$


The polynomial $U(D)x^{2k-2}$ still has degree $2k-2$, with nonzero leading coefficient. It cannot be annihilated by $D^s$ unless


$$
s\ge2k-1.
$$


Hence $(D-1)^{2k-1}\mid P(D)$.

The corresponding logarithmic monodromy at $x=-1$ gives


$$
(D+1)^{2k-1}\mid P(D).
$$



Now set $X=0$ and choose $V(x^2)=x^{2k-4}$. At $x=1$, the factorial part is locally analytic; the arctangent monodromy is a nonzero constant multiple of $x^{2k-4}$. Therefore


$$
P(D)x^{2k-4}=0,
$$


which forces


$$
D^{2k-3}\mid P(D).
$$


The three factors are relatively prime in $\mathbb Q[D]$, proving (3.1).

For $Y_k$, the coefficient multiplying the positive-contact function is


$$
(x^2+1)X(x^2),
$$


whose maximal degree is $2k$. The same arguments at $1$ and $-1$ force multiplicities $2k+1$ at $D=1,-1$. The maximal degree of the arctangent coefficient is $2k-2$, forcing multiplicity $2k-1$ at $D=0$. This proves (3.2). ∎

The operators already supplied in Turn 3 attain these orders. The theorem therefore proves minimality, rather than merely a lower estimate for one attempted construction.

### 3.3 Larger fixed operators do not improve the projection comparison

The minimality theorem also gives a precise limitation on the degree-counting method.

Let


$$
n=\deg P,\qquad l=\operatorname{ord}_{T=0}P(T).
$$



For $Z_k$, write


$$
n=(6k-5)+s,\qquad s\ge0.
$$


Divisibility (3.1) implies


$$
l\le(2k-3)+s.
\tag{3.3}
$$



The universal maximal pole orders after applying $P(D)$ are exactly

- $n-1$ at $0$;
- $n$ at each of $1,-1$;
- $n+1$ at each root of $x^2+1$.

They are exact universal orders: the constant return coefficient detects the first, and suitable contact coefficients detect the others. The highest derivative produces each highest pole; lower derivatives cannot cancel it universally.

Consequently, the minimal common pole divisor for the whole family has degree


$$
(n-1)+2n+2(n+1)=5n+1.
$$



The original $2k$ zero coefficients force the retained negative tail to start no earlier than $x^{-(4k+1)}$. After applying $P(D)$, the permitted numerator-degree ceiling is therefore


$$
5n+1-(4k+l+1)=5n-4k-l.
$$


Using (3.3),


$$
\boxed{
5n-4k-l\ge24k-22+4s.
}
\tag{3.4}
$$



For $Y_k$, similarly write


$$
n=(6k+1)+s,\qquad l\le(2k-1)+s.
$$


There is no contact atom in this returned family. The universal pole divisor has degree


$$
(n-1)+2n=3n-1.
$$


The original $2k-1$ zero coefficients give the numerator-degree ceiling


$$
3n-4k-l,
$$


and hence


$$
\boxed{
3n-4k-l\ge12k+4+2s.
}
\tag{3.5}
$$



For an operator of one parity, the numerator is a polynomial in $x^2$, and division of these ceilings by two recovers the minimal permitted degrees $12k-11$ and $6k+2$. A mixed-parity operator can be separated into its parity components, each of which rationalizes the family, so it provides no escape.

These are bounds on the **degree ceiling permitted by the argument**, not lower bounds on the degree of every actual numerator.

**Corollary 3.2 — precise no-go statement.**  
An argument using only

1. a fixed constant-coefficient rationalizing operator;
2. universal pole orders;
3. the original finite-tail vanishing; and
4. nonvanishing of the resulting rational function,

cannot force the numerator to vanish by degree comparison. Increasing the operator order makes the permitted ceiling no smaller.

This does not rule out exploiting the constrained coefficient image. It establishes that such exploitation must contribute genuinely new information beyond the preceding four ingredients.

---

## 4. A lower-order identity for the complete returned columns

We now work directly with the original moment indices. This avoids high-order differentiation entirely.

Put


$$
q=2n+1,\qquad
P_n=q(q+1),\qquad
A_n=P_n+1=q^2+q+1.
\tag{4.1}
$$


Also,


$$
A_{n+1}=q^2+5q+7.
$$



The original recurrence gives


$$
u_{n+1}=P_nu_n-q,\qquad f_{n+1}=P_nf_n.
$$


Therefore the complete returns satisfy


$$
\boxed{
\sigma_n=A_nu_n-q,
\qquad
\tau_n=-A_nf_n+\frac4q.
}
\tag{4.2}
$$



The multiplier $A_n$ must not be treated as a unit merely because the physical factorials are units. The following calculation never divides by it.

### 4.1 Exact coupled forcing

Define, for any sequence $y$,


$$
\mathcal D_n y
=(q+2)\bigl(A_ny_{n+1}-P_nA_{n+1}y_n\bigr).
\tag{4.3}
$$



For the contact return, substitution of (4.2) gives


$$
A_n\sigma_{n+1}-P_nA_{n+1}\sigma_n
=-qA_{n+1}-(q+2)A_n.
$$


Consequently,


$$
\boxed{
\mathcal D_n\sigma
=-F_\sigma(q),
}
\tag{4.4}
$$


where


$$
\boxed{
F_\sigma(q)=2q^4+12q^3+26q^2+22q+4.
}
\tag{4.5}
$$



For the complete right return,


$$
A_n\tau_{n+1}-P_nA_{n+1}\tau_n
=
\frac{4A_n}{q+2}
-\frac{4P_nA_{n+1}}q.
$$


Since $P_n=q(q+1)$,


$$
\boxed{
\mathcal D_n\tau
=-F_\tau(q),
}
\tag{4.6}
$$


with


$$
\boxed{
F_\tau(q)=4q^4+32q^3+92q^2+120q+52.
}
\tag{4.7}
$$



For verification,


$$
(q+2)\bigl(qA_{n+1}+(q+2)A_n\bigr)
=F_\sigma(q),
$$


and


$$
4\bigl((q+2)(q+1)A_{n+1}-A_n\bigr)
=F_\tau(q).
$$



Thus every forcing contribution has been evaluated. In particular, the second polynomial would disappear if one incorrectly replaced $\tau_n$ by its factorial part.

No shift commutator has been suppressed: in a shifted column, $n=m+j$ everywhere in (4.3).

---

## 5. An evaluated two-column certificate inside the actual $Y_k$

### 5.1 Integer row functionals

Fix $k\ge4$ and $0\le j<k$. Consider the actual six-row, two-column subarray


$$
M_{k,j}
=
\left(
\begin{array}{cc}
\sigma_j&\Lambda_k\tau_j\\
\sigma_{j+1}&\Lambda_k\tau_{j+1}\\
\vdots&\vdots\\
\sigma_{j+5}&\Lambda_k\tau_{j+5}
\end{array}
\right).
\tag{5.1}
$$



Let $q_0=2j+1$, and for a six-entry column $y_m=y_{j+m}$ put


$$
d_m(y)=
(q_0+2m+2)
\left(
A_{j+m}y_{m+1}
-P_{j+m}A_{j+m+1}y_m
\right),
\quad 0\le m\le4.
\tag{5.2}
$$



Define the two integer row functionals


$$
E_j^{(4)}y=\Delta^4d_0(y),
\qquad
E_j^{(3)}y=\Delta^3d_0(y),
\tag{5.3}
$$


where


$$
\Delta^r d_0
=\sum_{m=0}^r(-1)^{r-m}\binom rm d_m.
$$


These are integer linear combinations of the original six rows. There is no division.

### 5.2 Evaluation of the resulting $2\times2$ matrix

By (4.4)–(4.7),


$$
d_m(\sigma)=-F_\sigma(q_0+2m),
$$




$$
d_m(\Lambda_k\tau)=-\Lambda_kF_\tau(q_0+2m).
$$



The needed differences follow from


$$
\Delta^4m^4=24,\qquad
\Delta^3m^4\big|_{m=0}=36,\qquad
\Delta^3m^3=6.
$$



For $F_\sigma(q_0+2m)$, the coefficients of $m^4,m^3$ are


$$
32,\qquad 64q_0+96.
$$


For $F_\tau(q_0+2m)$, they are


$$
64,\qquad 128q_0+256.
$$


Hence


$$
\Delta^4F_\sigma(q_0+2m)=768,
$$




$$
\Delta^3F_\sigma(q_0+2m)\big|_{m=0}
=384q_0+1728,
$$


and


$$
\Delta^4F_\tau(q_0+2m)=1536,
$$




$$
\Delta^3F_\tau(q_0+2m)\big|_{m=0}
=768q_0+3840.
$$



Therefore


$$
\begin{pmatrix}
E_j^{(4)}\\ E_j^{(3)}
\end{pmatrix}
M_{k,j}
=
-
\begin{pmatrix}
768&1536\Lambda_k\\
384q_0+1728&\Lambda_k(768q_0+3840)
\end{pmatrix}.
\tag{5.4}
$$



Its determinant is


$$
\begin{aligned}
&\Lambda_k\left[
768(768q_0+3840)
-1536(384q_0+1728)
\right]\\
&\qquad=768\cdot384\,\Lambda_k
=2^{15}3^2\Lambda_k.
\end{aligned}
$$



We have proved the following.

**Theorem 5.1 — actual mixed-return pair certificate.**  
For every $k\ge4$ and $0\le j<k$,


$$
\boxed{
\delta_2(M_{k,j})\mid 2^{15}3^2\Lambda_k.
}
\tag{5.5}
$$


In particular, the two actual columns in (5.1) are independent modulo every prime $p>6k-4$.

#### Why the content divisibility is valid

The matrix on the left of (5.4) is obtained by an integer $2\times6$ row-combination matrix. Cauchy–Binet expresses its determinant as an integer linear combination of the $2\times2$ minors of $M_{k,j}$. Thus their gcd divides the displayed determinant.

No claim is made that these rectangular row combinations are unimodular, or that they preserve content exactly.

### 5.3 Original-boundary check

The proof uses rows $m=0,\ldots,5$ of $Y_k$, which exist for $k\ge4$.

The largest return index used is


$$
j+5\le k+4\le3k-3.
$$


The largest underlying moment is


$$
j+6\le k+5\le3k-2.
$$


Thus every entry lies inside the original physical boundary. No terminal row or moment has been added.

The right columns retain their original $\Lambda_k$ scaling. In particular, the factor $\Lambda_k$ in (5.4)–(5.5) has not been canceled.

The prime $p=6k-1$, when prime, causes no exception: neither $2$, $3$, nor $\Lambda_k$ is divisible by it. No high derivative factorial occurs in this certificate.

Finally, the disappearance of the contact atom from this calculation is legitimate: the calculation concerns $\sigma_n=c_{n+1}+c_n$, where the atom cancels exactly. It does not replace $c_n$ by $u_n$ in $Z_k$ or in $H_k$.

---

## 6. A fully evaluated certificate for the weighted stack—and its exact limitation

### 6.1 The augmented matrix

Let


$$
\mathcal J_k
=\operatorname{diag}(0,1,\ldots,k-1,\;0,1,\ldots,k-1)
$$


in the original contact-then-return column ordering of $Y_k$. Define


$$
\boxed{
\mathbb Y_k=
\begin{pmatrix}
Y_k\\
Y_k\mathcal J_k\\
\vdots\\
Y_k\mathcal J_k^{\,k-1}
\end{pmatrix}.
}
\tag{6.1}
$$



This stack uses only existing physical moments. Nevertheless, it is an **augmentation**, not a replacement for $Y_k$. An original relation $Y_kz=0$ does not supply the other block equations.

### 6.2 Explicit integer column selectors

For $0\le j<k$, put


$$
L_j(T)=\prod_{\substack{0\le i<k\\i\ne j}}(T-i)\in\mathbb Z[T].
$$


Then


$$
L_j(j)=d_j=(-1)^{k-1-j}j!(k-1-j)!,
\tag{6.2}
$$


while $L_j(i)=0$ for $i\ne j$.

Therefore


$$
Y_kL_j(\mathcal J_k)
$$


has only two possibly nonzero columns: the contact and return columns with shift $j$. Those columns equal $d_j$ times the corresponding columns of $Y_k$.

Because $\deg L_j=k-1$, every row of $Y_kL_j(\mathcal J_k)$ is an explicit integer linear combination of rows of $\mathbb Y_k$.

Apply the two row functionals of Section 5 to this selected pair, for each $j$, and stack the resulting $2k$ rows. After interleaving the two columns for each $j$, the resulting square matrix is block diagonal, with blocks $d_j$ times (5.4). Its determinant, up to the harmless column-permutation sign, is


$$
\prod_{j=0}^{k-1}
d_j^2(2^{15}3^2\Lambda_k).
$$



Since


$$
\prod_{j=0}^{k-1}d_j^2
=
\left(\prod_{j=0}^{k-1}j!\right)^4,
$$


Cauchy–Binet proves the next theorem.

**Theorem 6.1 — evaluated weighted-stack content bound.**  
For every $k\ge4$, $\mathbb Y_k$ has full column rank over $\mathbb Q$, and


$$
\boxed{
\delta_{2k}(\mathbb Y_k)
\mid
\mathcal W_k,
\qquad
\mathcal W_k=
(2^{15}3^2\Lambda_k)^k
\left(\prod_{j=0}^{k-1}j!\right)^4.
}
\tag{6.3}
$$



Every prime divisor of the evaluated certificate $\mathcal W_k$ is at most $6k-5$. Hence


$$
\boxed{
\operatorname{rank}_{\mathbb F_p}\mathbb Y_k=2k
\qquad(p>6k-4).
}
\tag{6.4}
$$



This is a uniform theorem involving the complete actual mixed columns. It is not an unevaluated observability condition.

### 6.3 Evaluated height and prime-depth bounds

The exact certificate gives


$$
\begin{aligned}
v_p\!\left(\delta_{2k}(\mathbb Y_k)\right)
\le{}&
k\left(15\,\mathbf1_{p=2}
+2\,\mathbf1_{p=3}
+v_p(\Lambda_k)\right)\\
&+4\sum_{j=0}^{k-1}v_p(j!).
\end{aligned}
\tag{6.5}
$$



The factorial term is explicitly computable by Legendre's formula. In particular,


$$
4\sum_{j=0}^{k-1}\log(j!)
=
4\sum_{r=1}^{k-1}(k-r)\log r
=
2k^2\log k+O(k^2).
$$


Together with $\log\Lambda_k=O(k)$, this yields


$$
\boxed{
\log\delta_{2k}(\mathbb Y_k)
\le 2k^2\log k+O(k^2).
}
\tag{6.6}
$$



The content in (6.6) is the actual content of $\mathbb Y_k$. It is **not**
$\mathscr L_k$, $\mathscr C_{Y,k}$, or a substitute for either.

### 6.4 A new actual-family obstruction to weighted-column closure

The full-rank statement has an immediate consequence.

**Corollary 6.2.**  
For $k\ge4$ and $p>6k-4$, the kernel of $Y_k$ contains no nonzero $\mathcal J_k$-invariant subspace.

Equivalently, for every nonzero $z\in\ker Y_k$, at least one of


$$
Y_k\mathcal J_kz,\ldots,Y_k\mathcal J_k^{\,k-1}z
$$


is nonzero.

#### Proof

If a nonzero vector $z$ belonged to such an invariant subspace, all $k$ block equations in (6.1) would vanish on $z$. This contradicts (6.4). ∎

Since $Y_k$ has $2k$ columns but only $2k-1$ rows, its right kernel is necessarily nonzero. Thus the entire kernel is never $\mathcal J_k$-invariant in this range.

This makes the obstruction particularly concrete:

> A proposed proof that treats every original mixed relation as automatically closed under multiplication of its coefficients by $j$ is false in the actual $Y_k$, not merely unsupported by a general argument.

The corollary does not say that the first weighted discrepancy is nonzero for every relation. It says that a nonzero relation cannot survive all the explicitly listed weights.

---

## 7. Why this still does not prove finite-tail normality

### 7.1 Where the extra information entered

The row functional $E_j$ in Section 5 depends on the column shift $j$. It cannot be applied independently to each matched pair by one common row operation on $Y_k$.

Section 6 achieves that separation using $L_j(\mathcal J_k)$. But this requires the weighted block equations


$$
Y_k\mathcal J_k^r z=0,
\qquad 0\le r<k,
$$


whereas an original relation supplies only the equation for $r=0$.

All interpolation payments in this construction are explicit:


$$
L_j(j)=(-1)^{k-1-j}j!(k-1-j)!.
$$


They are units in the required prime range. The problem is therefore no longer an unpaid pivot in this particular construction. It is the absence of the additional weighted relations.

This is precisely the kind of distinction the original finite projection requires.

### 7.2 Full stacked rank cannot be descended by linear algebra alone

The limitation is not cosmetic. For example, over a field with distinct $0,\ldots,k-1$, consider a matrix with all contact columns equal to a vector $e_1$, all return columns equal to $e_2$, and all other rows zero. Each matched pair is independent, and its weighted stack has rank $2k$ by Vandermonde interpolation. The original matrix has rank only $2$.

This example is **not** a counterexample in the compact mixed family. It proves only that pairwise independence and full weighted-stack rank do not, by themselves, imply the desired original rank.

Accordingly, neither (6.3) nor (6.6) may be transferred to $\mathscr L_k$ without an additional arithmetic identity specific to the actual coupled moments.

### 7.3 One concrete follow-on arithmetic lemma

The evaluated integer $\mathcal W_k$ supplies a specific possible descent target.

**Proposed certificate-descent lemma — open.**  
At the original indices $k=K_u$, prove


$$
\boxed{
\mathcal W_k
\in
I_{2k-1}(Y_k),
}
\tag{7.1}
$$


where $I_{2k-1}(Y_k)\subset\mathbb Z$ is the ideal generated by the actual maximal minors of the original $Y_k$.

Equivalently, construct integers $\beta_I$ satisfying


$$
\sum_{\substack{I\subset\{0,\ldots,2k-1\}\\|I|=2k-1}}
\beta_I\det Y_k[:,I]
=
(2^{15}3^2\Lambda_k)^k
\left(\prod_{j=0}^{k-1}j!\right)^4.
\tag{7.2}
$$



This is a concrete arithmetic claim with an already evaluated right-hand side. It would prove large-prime normality for $Y_k$ on those indices and an explicit all-prime bound for $\mathscr L_k$.

It is not proved here. In particular, Cauchy–Binet in Section 6 constructs a combination of maximal minors of the **stack**, not the coefficients $\beta_I$ in (7.2). Constructing those coefficients requires controlling the actual weighted commutators rather than asserting their disappearance.

Even a proof of this $Y$-descent would leave the corresponding $Z_k$ obligation. It would also not automatically yield the requested strictly subcritical sum of the two Turn 3 contents.

### 7.4 The $149$ obstruction remains in force

Nothing above rehabilitates the false interpolation shortcut from Turn 3. Its evaluated determinant


$$
7152=2^4\cdot3\cdot149
$$


still shows that the selected even-factorial interpolation pivot need not be a unit merely because all physical factorials are units.

At the same auxiliary pair $k=3,p=149$, the supplied actual mixed minors remain


$$
132,\qquad95\pmod{149},
$$


both units. Thus $149$ is not an actual mixed-family counterexample.

The new six-row theorem begins at $k=4$; it is not being used retrospectively as a proof of the $k=3$ receipt.

---

## 8. Consequences for the actual primitive whole errors

The new results do not change $H_k$, $G_k$, $q_k$, or $\ell_k$.

The accepted analytic estimate, at its supplied scope, remains


$$
\log|H_k(e+\pi)|=4k^2\log k+O(k^2).
\tag{8.1}
$$



Turn 3's exact content-payment theorem is reused without rederivation. It says that the requested bound


$$
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
\le(12-\eta)k^2\log k+O(k^2),
\qquad \eta>0,
\tag{8.2}
$$


on the original indices would imply the corresponding strictly-below-$4$ bound for
$\log\mathscr R_k+\log\mathscr L_k$.

Together with (2.9), that would give


$$
\log\ell_{K_u}
\ge
\eta K_u^2\log K_u-O(K_u^2),
$$


so the primitive whole errors would diverge.

Neither (6.6) nor any other result of this report proves (8.2). The matrix in (6.6) is different, and no valid content descent has been established.

Furthermore:

- large-prime normality alone would not bound small-prime depths;
- the closed $32/33$ failures of the older content envelope remain failures;
- whole-error divergence would retire this producer as a source of primitive whole-error decay, not prove $e+\pi$ rational.

Conversely, a proof that


$$
0<\ell_{K_u}\longrightarrow0
$$


on the same infinite original indices would prove irrationality: if $e+\pi=a/b$, every nonzero $q_{K_u}(e+\pi)-p_{K_u}$ has absolute value at least $1/b$. No such decay is established here.

### Separate binary producer

No compact conclusion is transferred to the separate binary producer. Its domain and physical endpoint remain


$$
b=9^{18+32u},\qquad n=4002b,
\qquad j=0,\ldots,b-1,\qquad z_b=0.
$$


Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0.
$$


Its return remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
$$


with only the supplied paid estimate


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$



Its norm $Q=x_0^Tx_0$, corrected-column contents, actual least simultaneous clearer, and final all-prime gcd are not replaced by compact quantities. Its stated $3$-adic primitive-denominator valuation is not transferred to $q_k$.

---

## 9. Proof-status ledger and bounded verification

### 9.1 Status ledger

| Statement | Status and exact scope |
|---|---|
| Turn 3 finite-jet equivalence and content payments | Reused at their stated scope; no clearer or correction dropped |
| Minimality of the fixed constant-coefficient rationalizing operators | **New proof**, over $\mathbb Q$, for the full parameter families |
| Impossibility of improving the pole/tail degree comparison within that operator class | **New proof**; does not rule out parameter-dependent elimination or additional image constraints |
| Complete first-order return identities (4.4) and (4.6) | **New proof**, with both forcings fully evaluated |
| Six-row mixed-pair determinant $2^{15}3^2\Lambda_k$ | **New proof**, every $k\ge4$, every $0\le j<k$, inside the original physical prefix |
| Weighted-stack maximal-minor certificate (6.3) | **New proof**, all-prime integer divisibility for the explicitly augmented matrix |
| Full weighted-stack rank at $p>6k-4$, including $p=6k-1$ | **New proof**, $k\ge4$ |
| Absence of a nonzero shift-weight-invariant subspace in $\ker Y_k$ | **New proof**, same field and index scope |
| Original $Z_k$ finite-tail injectivity | **Open** |
| Original $Y_k$ kernel dimension exactly one | **Open** |
| An actual mixed-family counterexample at $p>6k-4$ | **Not produced** |
| Certificate descent (7.1)–(7.2) | **Concrete open follow-on lemma**, not inferred from the stack |
| Required bound for the actual $\mathscr C_{Z,k},\mathscr C_{Y,k}$ | **Open** |
| Primitive whole-error decay or divergence at the original $K_u$ | **Open** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

### 9.2 Bounded arithmetic requiring coordinator inspection

No new large determinant or Smith computation is requested.

The only outstanding small receipt remains the supplied $k=3,p=149$ check.

**Bounded inputs**

- $k=3$, $p=149$;
- the original recurrences through moment $7$;
- factorials through $14!$;
- odd denominators through $13$;
- $\Lambda_3=45045\equiv47\pmod{149}$;
- the actual $Z_3,Y_3$ defined by (2.4)–(2.5);
- the $3\times3$ interpolation matrix
  

$$
\left(\frac{(2m+2j)!}{(2m)!}\right)_{0\le m,j\le2}.
$$



**Expected verifiable outputs**


$$
7152=2^4\cdot3\cdot149,
$$




$$
\det Z_3[\text{rows }0,\ldots,4]\equiv132\pmod{149},
$$




$$
\det Y_3[\text{columns }0,\ldots,4]\equiv95\pmod{149}.
$$



These outputs verify exactly one interpolation obstruction and two actual mixed unit minors. They establish no growing-index theorem.

The new polynomial identities and the constant determinant in Sections 4–6 have been derived explicitly above; they do not depend on an unexecuted numerical experiment.

---

## Final conclusion

The new result is a **sharp limitation theorem for fixed differential rationalization**, together with a **fully evaluated arithmetic certificate for complete mixed-return pairs and their weighted stack**.

The latter certificate also proves that the weighted-column closure shortcut fails in the actual $Y_k$: the mandatory original kernel cannot be invariant under the shift-index operator. Thus invertible state transport and paid interpolation do not supply the missing weighted relations.

The exact remaining bottleneck is the descent from such coupled, weighted identities to the **original finite coefficient projection**, or an adequate bound for its **actual all-prime contents**. No original boundary, forcing term, clearer, final gcd, primitive denominator, or whole error has been replaced.

The rationality or irrationality of $e+\pi$ remains unresolved.
