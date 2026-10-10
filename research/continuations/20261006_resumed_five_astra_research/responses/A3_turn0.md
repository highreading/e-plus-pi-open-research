> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 — Reduced correction heights and a complete-row denominator factor theorem

## Executive summary

The rationality or irrationality of


$$
S=e+\pi
$$


remains unresolved.

This report addresses the complementary-prime arithmetic **after both complete endpoint rows have been made primitive**. It reuses the accepted five-moment endpoint reduction, the eventual noncollapse theorem, the complete row-denominator formula, and


$$
(|AB|)_{\mathcal P}=5n
$$


on the original families


$$
n=15^r,\quad r\ge2,\quad \mathcal P=\{3,5\},
$$


and


$$
n=105^r,\quad r\ge2,\quad \mathcal P=\{3,5,7\}.
$$



The new results are:

1. **An exact primitive-coordinate description of the reduced corrections.**  
   Each correction $\kappa_j$ is obtained from a primitive integer pair by an integer linear transformation whose coefficients and determinant have height $\exp(O(n))$. Consequently,
   

$$
\log H(\kappa_j)
   =
   \log H(\text{primitive moment pair at }j)+O(n).
$$


   This identifies precisely what an exponential correction-height theorem would have to prove. The available direct moment bounds give only
   

$$
\log H(\kappa_j)\le 2n\log n+O(n),
$$


   which is not the desired reference-height bound.

2. **An exact denominator formula for $\kappa_0-\kappa_3$.**  
   It includes the gcd of the complete evaluated numerator and denominator. Its transformation determinant is exactly the accepted $\Delta_T\mathcal H_n$, after the appropriate primitive scaling.

3. **A complete-row denominator factor theorem with only exponential distortion.**  
   Two explicitly defined integers $K_0,K_3$, formed from the specialized moment data and the **complete exponential force**, satisfy
   

$$
\left|
   v_p(|AB|)
   -
   v_p\!\left(\frac{K_0K_3}{\gcd(K_0,K_3)^2}\right)
   \right|
   \le v_p(Lt_0)
$$


   at every prime. Here $Lt_0=\exp(O(n))$. The logarithmic force has not been discarded: its entire contribution is eliminated from the row-content calculation by an exact Wronskian identity, with every resulting gcd and reference-denominator factor retained.

4. **A precise additional arithmetic obstruction.**  
   The remaining cancellation is an explicit congruence involving the complete exponential endpoint numerator, including the exterior $+1$. Transformation noncollapse does not prevent that congruence from holding to the full denominator depth.

No tools were executed. A new bounded calculation at the original index $n=225$ is specified below.

---

## 1. Scope and retained inputs

### 1.1 Original finite construction

Throughout,


$$
d=2,\qquad b=3.
$$


The contact matrix has rows and columns $0,1,2$. Reconstruction retains coordinates $0,1,2,3$. An individual producer uses the complete force through index exactly $2n+2$.

Set


$$
Q(z)=1-z+\frac{z^2}{2},\qquad q_j=[z^j]Q(z)^n.
$$


To avoid confusing the logarithmic coefficient sequence with the endpoint coefficients, write


$$
a^{\log}_0=a^{\log}_1=1,\qquad
a^{\log}_j=a^{\log}_{j-1}-\frac12a^{\log}_{j-2}.
$$


Then


$$
\eta_L
=
\sum_{r=0}^{L}\frac1{r!}
+
\sum_{r=1}^{L}\frac{2a^{\log}_{r-1}}r,
\qquad
\mathcal W_L=L!\eta_L,
$$


and


$$
w_i
=
\sum_{j=0}^{\min(2n,n+i)}
q_j(n+i)^{\underline j}\mathcal W_{2n+i-j},
\qquad 0\le i\le2.
\tag{1.1}
$$



The complete force is decomposed only as the exact sum


$$
w=w^{\exp}+w^{\log}.
$$


In particular,


$$
w_i^{\exp}
=
\sum_{j=0}^{\min(2n,n+i)}
q_j(n+i)^{\underline j}
(2n+i-j)!
\sum_{r=0}^{2n+i-j}\frac1{r!}.
\tag{1.2}
$$


No factorial tail is removed.

The contact matrix is


$$
C_{ij}=(n+i)^{\underline j}\mathcal B_{n+i-j},
\qquad
\mathcal B_N=N![z^N](e^zQ(z)^n).
$$



With $x=C^{-1}z$, $y=C^{-1}w$, the full reconstructed columns remain


$$
u=\mathsf I\mathcal Sx,\qquad
v=\mathsf I\mathcal Sy+e_0,
$$


where


$$
\mathcal S=
\begin{pmatrix}
1&-n&n(n+1)\\
0&1&-2n\\
0&0&1
\end{pmatrix},
\qquad
\mathsf I=
\begin{pmatrix}
-1&0&0\\
1&-1&0\\
0&1&-1\\
0&0&1
\end{pmatrix}.
\tag{1.3}
$$


The least clearer $d_B$ is taken over **all eight entries** of these two columns.

### 1.2 What is reused

The coordinator’s final review accepts A3 turn 8’s:

- five-moment endpoint reduction;
- exact normalization of the logarithmic companion;
- endpoint transformation determinant;
- fixed-shift saddle estimate and eventual noncollapse;
- complete row-primitive denominator formula;
- selected-prime law.

Those results are inputs here, not reproved.

The retained receipts cover the finite indices $15,30,105,210$. They do not cover the new primitive correction coordinates or the new content factorization below. Their reported row gcds remain finite facts, not asymptotic estimates.

The classical Legendre companion and Wronskian are established background. Prime-power state methods and creative telescoping do not, without an additional target-specific argument, bound the gcds appearing in this report. No exhaustive novelty claim is made.

---

## 2. The accepted endpoint formulas, with complete numerators

Write


$$
c_k=[z^k](e^zQ(z)^n),
$$


and retain the five moments


$$
a=c_{n-2},\quad b=c_{n-1},\quad c=c_n,\quad
d=c_{n+1},\quad e_*=c_{n+2}.
$$


Then


$$
T_n=
\begin{pmatrix}
c&b&a\\
d&c&b\\
e_*&d&c
\end{pmatrix},
\qquad
C=\operatorname{diag}(n!,(n+1)!,(n+2)!)T_n.
$$


Put


$$
\Delta_T=\det T_n.
$$



Let


$$
\ell_0^T=(-1,n,-n(n+1)),\qquad
\ell_3^T=(0,0,1),
\qquad
R_j=\ell_j^T\operatorname{adj}(T_n).
$$


Define


$$
\mathbf v_n=
\begin{pmatrix}
1\\1/2\\(n+1)/(2(n+2))
\end{pmatrix},
\qquad
\mathbf w_n=
\begin{pmatrix}
0\\1/2\\(2n+3)/(2(n+2))
\end{pmatrix},
$$


and


$$
\alpha_j=R_j\mathbf v_n,\qquad
\beta_j=R_j\mathbf w_n,\qquad
\xi_j=\alpha_j\tau_n+\beta_j\tau_{n+1}.
\tag{2.1}
$$



For $\widehat w_i=w_i/(n+i)!$, the complete endpoint numerators are


$$
N_0=\Delta_T+R_0\widehat w,\qquad
N_3=R_3\widehat w.
\tag{2.2}
$$


Thus


$$
u_j=\frac{n!\xi_j}{\Delta_T},
\qquad
v_j=\frac{N_j}{\Delta_T},
\qquad
c_j:=\frac{v_j}{u_j}=\frac{N_j}{n!\xi_j}.
\tag{2.3}
$$



Define, importantly,


$$
N_0^{\exp}=\Delta_T+R_0\widehat w^{\exp},
\qquad
N_3^{\exp}=R_3\widehat w^{\exp}.
\tag{2.4}
$$


The exterior $+1$ is the term $\Delta_T$ in $N_0^{\exp}$.

The accepted complete logarithmic formula gives


$$
N_j
=
N_j^{\exp}
+
4n!\bigl(\alpha_j\rho_n+\beta_j\rho_{n+1}\bigr).
\tag{2.5}
$$



Here


$$
\tau_0=\tau_1=1,\qquad \rho_0=0,\quad\rho_1=1,
$$


and both sequences satisfy


$$
(n+2)y_{n+2}=(2n+3)y_{n+1}+(n+1)y_n.
$$


Their exact Wronskian is


$$
\tau_n\rho_{n+1}-\tau_{n+1}\rho_n
=\frac{(-1)^n}{n+1}.
\tag{2.6}
$$



The reference and corrections are therefore


$$
f_n^{\rm ref}=\frac{4\rho_n}{\tau_n},
\qquad
\kappa_j
=
\frac{4(-1)^n\beta_j}{(n+1)\tau_n\xi_j}.
\tag{2.7}
$$



---

## 3. Primitive coefficient triples for the complete endpoint rows

The following normalization is an auxiliary exact coordinate system. It does **not** replace the actual row primitivization.

### 3.1 A common reference clearer

Set


$$
L=2^{n+1}\operatorname{lcm}(1,\ldots,n+1)
$$


and define integers


$$
t_0=L\tau_n,\qquad t_1=L\tau_{n+1},
$$




$$
r_0=4L\rho_n,\qquad r_1=4L\rho_{n+1}.
\tag{3.1}
$$


The stated integrality follows from the accepted dyadic formula for $\tau_n$ and the finite convolution denominator bound for $\rho_n$.

Their determinant is the nonzero integer


$$
\boxed{
\Omega:=t_0r_1-t_1r_0
=\frac{4(-1)^nL^2}{n+1}.
}
\tag{3.2}
$$



All five integers $L,t_0,t_1,r_0,r_1$, and also $\Omega$, have height $\exp(O(n))$. Indeed:

- $\log\operatorname{lcm}(1,\ldots,n+1)=O(n)$, by the elementary binomial-coefficient proof of Chebyshev’s bound;
- $\tau_m\le(1+\sqrt2)^m$;
- the convolution gives
  

$$
|\rho_m|
  \le(1+\sqrt2)^{m-1}\sum_{j=1}^{m}\frac1j.
$$



In particular,


$$
\log(Lt_0)=O(n),\qquad
\log(|\Omega|t_0)=O(n).
\tag{3.3}
$$



### 3.2 Primitive triples

For each $j\in\{0,3\}$, choose the positive rational scale $\sigma_j$ such that


$$
\mathsf A_j=\sigma_j\alpha_j,\qquad
\mathsf B_j=\sigma_j\beta_j,\qquad
\mathsf E_j=\sigma_j\frac{N_j^{\exp}}{n!}
\tag{3.4}
$$


are integers with


$$
\gcd(|\mathsf A_j|,|\mathsf B_j|,|\mathsf E_j|)=1.
$$


This is obtained by clearing the three rational denominators and dividing by the common integer content.

Put


$$
\gamma_j=\gcd(|\mathsf A_j|,|\mathsf B_j|),
\qquad
\mathfrak a_j=\frac{\mathsf A_j}{\gamma_j},
\qquad
\mathfrak b_j=\frac{\mathsf B_j}{\gamma_j}.
\tag{3.5}
$$


Then


$$
\gcd(|\mathfrak a_j|,|\mathfrak b_j|)=1,
\qquad
\gcd(\gamma_j,|\mathsf E_j|)=1.
\tag{3.6}
$$



Define the evaluated integers


$$
X_j=\mathfrak a_jt_0+\mathfrak b_jt_1,
\qquad
Y_j=\mathfrak a_jr_0+\mathfrak b_jr_1,
\tag{3.7}
$$


and the complete integer row


$$
M_j=\gamma_jX_j,
\qquad
V_j=\gamma_jY_j+L\mathsf E_j.
\tag{3.8}
$$



### Proposition 3.1 — Exact complete-row representation

For $j=0,3$,


$$
\boxed{
c_j=\frac{V_j}{M_j}.
}
\tag{3.9}
$$


Moreover,


$$
\boxed{
(u_j,v_j)
=
\frac{n!}{\sigma_jL\Delta_T}(M_j,V_j).
}
\tag{3.10}
$$



#### Proof

From the definitions,


$$
M_j
=
L(\mathsf A_j\tau_n+\mathsf B_j\tau_{n+1})
=
\sigma_jL\xi_j.
$$


Using (2.5),


$$
\begin{aligned}
V_j
&=L\mathsf E_j+\mathsf A_jr_0+\mathsf B_jr_1\\
&=\frac{\sigma_jL}{n!}N_j^{\exp}
+4\sigma_jL(\alpha_j\rho_n+\beta_j\rho_{n+1})\\
&=\frac{\sigma_jL}{n!}N_j.
\end{aligned}
$$


Equations (2.3) now give both conclusions. ∎

Thus, if


$$
g_j^*=\gcd(|M_j|,|V_j|),
$$


the actual reduced endpoint denominator is exactly


$$
\boxed{
d_j=\frac{|M_j|}{g_j^*}.
}
\tag{3.11}
$$



To connect this to the original least clearer, let


$$
(U_j^{\rm orig},V_j^{\rm orig})=d_B(u_j,v_j).
$$


Then


$$
\gcd(|U_j^{\rm orig}|,|V_j^{\rm orig}|)
=
\left|\frac{d_Bn!}{\sigma_jL\Delta_T}\right|g_j^*.
\tag{3.12}
$$


The right side is an integer. This identity preserves the original full-column normalization and its actual row contents.

---

## 4. Reduced heights of the corrections

### 4.1 Exact primitive correction formula

The logarithmic endpoint response is $Y_j/X_j$. Hence


$$
\boxed{
\kappa_j
=
\frac{Y_j}{X_j}-\frac{r_0}{t_0}
=
\frac{\Omega\mathfrak b_j}{t_0X_j}.
}
\tag{4.1}
$$



This formula is evaluated at the same original index $n$.

Let


$$
Q_j^\kappa=\operatorname{den}(\kappa_j),
$$


with $\operatorname{den}(0)=1$. Then, without any omitted gcd,


$$
\boxed{
Q_j^\kappa
=
\frac{|t_0X_j|}
{\gcd(|t_0X_j|,|\Omega\mathfrak b_j|)}.
}
\tag{4.2}
$$



### Theorem 4.1 — Correction height is primitive moment-pair height up to $\exp(O(n))$

For a reduced rational $x=P/Q$, $Q>0$, put


$$
H(x)=\max(|P|,Q).
$$


Then


$$
\boxed{
\log H(\kappa_j)
=
\log\max(|\mathfrak a_j|,|\mathfrak b_j|)+O(n).
}
\tag{4.3}
$$


The implied constants are independent of the original smooth index.

Also,


$$
\boxed{
|X_j|\mid |\Omega|t_0Q_j^\kappa,
\qquad
Q_j^\kappa\mid t_0|X_j|.
}
\tag{4.4}
$$


Consequently,


$$
\boxed{
\frac{|X_j|}{|\Omega|t_0}
\le Q_j^\kappa\le t_0|X_j|.
}
\tag{4.5}
$$



#### Proof

The numerator-denominator vector before reduction in (4.1) is


$$
F
\begin{pmatrix}\mathfrak a_j\\ \mathfrak b_j\end{pmatrix},
\qquad
F=
\begin{pmatrix}
0&\Omega\\
t_0^2&t_0t_1
\end{pmatrix}.
$$


Its determinant is


$$
\det F=-\Omega t_0^2\ne0.
$$



For any integer matrix $F$ and primitive integer vector $v$, the content of $Fv$ divides $|\det F|$. Indeed, if $g$ divides both entries of $Fv$, then


$$
g\mid\det(F)v_1,\qquad g\mid\det(F)v_2,
$$


and $\gcd(v_1,v_2)=1$.

Thus


$$
\gcd(|\Omega\mathfrak b_j|,|t_0X_j|)
\mid |\Omega|t_0^2.
\tag{4.6}
$$


This proves (4.4) and (4.5).

For heights, use the maximum row-sum norm. The forward inequality is


$$
H(\kappa_j)
\le \|F\|_\infty
\max(|\mathfrak a_j|,|\mathfrak b_j|).
$$


If $w$ is the primitive output vector and $Fv=gw$, then


$$
v=\frac{g}{\det F}\operatorname{adj}(F)w.
$$


Since $g\mid|\det F|$,


$$
\max(|\mathfrak a_j|,|\mathfrak b_j|)
\le
\|\operatorname{adj}(F)\|_\infty H(\kappa_j).
$$


Both matrix norms are $\exp(O(n))$ by (3.3). This proves (4.3). ∎

### 4.2 What the theorem does and does not establish

The theorem proves the exact equivalence


$$
H(\kappa_j)\le\exp(O(n))
\quad\Longleftrightarrow\quad
\max(|\mathfrak a_j|,|\mathfrak b_j|)\le\exp(O(n)).
\tag{4.7}
$$


It does **not** prove either side.

A direct bound from the five moments is weaker. The integer


$$
D_{\rm mom}=2^n(n+2)!
$$


clears all five moments, and


$$
|c_{n+s}|\le e(5/2)^n,\qquad -2\le s\le2.
$$


After multiplying $(\alpha_j,\beta_j)$ by


$$
2(n+2)D_{\rm mom}^2,
$$


one obtains an integer pair of size at most


$$
\exp(2n\log n+O(n)).
$$


Its primitive pair is $(\mathfrak a_j,\mathfrak b_j)$, up to sign. Therefore


$$
\boxed{
\log H(\kappa_j)\le2n\log n+O(n).
}
\tag{4.8}
$$



This factorial-scale bound is rigorous but insufficient for importing a theorem requiring an exponentially bounded-height correction.

---

## 5. The reduced correction difference

Define


$$
\mathscr D
=
\mathfrak a_0\mathfrak b_3
-
\mathfrak b_0\mathfrak a_3.
\tag{5.1}
$$


Then


$$
\boxed{
\kappa_0-\kappa_3
=
-\frac{\Omega\mathscr D}{X_0X_3}.
}
\tag{5.2}
$$



Indeed,


$$
\mathfrak b_0X_3-\mathfrak b_3X_0=-t_0\mathscr D.
$$



The accepted moment determinant gives


$$
\boxed{
\mathscr D
=
\frac{\sigma_0\sigma_3}{\gamma_0\gamma_3}
\Delta_T\mathcal H_n.
}
\tag{5.3}
$$


Thus $\mathscr D\ne0$ eventually on each original family. This is exactly transformation noncollapse, in primitive coordinates.

The **reduced** difference denominator is


$$
\boxed{
Q^\Delta
=
\frac{|X_0X_3|}
{\gcd(|X_0X_3|,|\Omega\mathscr D|)}.
}
\tag{5.4}
$$



No numerator in this formula may be replaced by its leading asymptotic term.

A useful divisibility consequence is obtained by setting


$$
Z_X=\frac{|X_0X_3|}{\gcd(|X_0|,|X_3|)^2}.
$$


Then


$$
\boxed{
Z_X\mid |\Omega|Q^\Delta.
}
\tag{5.5}
$$



To prove this, observe first that


$$
\gcd(|X_j|,|Y_j|)\mid|\Omega|,
$$


because the matrix with rows $(t_0,t_1)$, $(r_0,r_1)$ has determinant $\Omega$ and acts on a primitive pair. The coprime denominator imbalance of two reduced rationals divides the denominator of their difference. Applying this to $Y_0/X_0$ and $Y_3/X_3$, and paying their two contents primewise, gives (5.5).

The unique reference-canceling weight, when $\mathscr D\ne0$, is


$$
\boxed{
\lambda_n^{\rm ref}
=
\frac{\mathfrak b_3X_0}{t_0\mathscr D}.
}
\tag{5.6}
$$


Its denominator must therefore be reduced by the actual gcd


$$
\gcd(|\mathfrak b_3X_0|,|t_0\mathscr D|).
$$


No short-height estimate for this weight follows from noncollapse.

---

## 6. A denominator factor theorem for the complete primitive rows

This is the principal new complete-row consequence.

### 6.1 The exact cancellation integer

Define


$$
\boxed{
\mathcal R_j
=
t_0L\mathsf E_j+\Omega\gamma_j\mathfrak b_j,
}
\tag{6.1}
$$


and


$$
\boxed{
\mathcal C_j
=
\gcd(|X_j|,|\mathcal R_j|).
}
\tag{6.2}
$$



Although $\mathcal R_j$ contains no $\rho$-value, it is an exact elimination of the **complete** logarithmic response, not an omission of it. Indeed,


$$
\boxed{
t_0V_j=r_0M_j+\mathcal R_j.
}
\tag{6.3}
$$



The term $t_0L\mathsf E_0$ contains $N_0^{\exp}$, and hence contains the exterior $+\Delta_T$.

### Theorem 6.1 — Complete row-content bounds

For the exact content


$$
g_j^*=\gcd(|M_j|,|V_j|),
$$


one has


$$
\boxed{
g_j^*\mid L\mathcal C_j,
\qquad
\mathcal C_j\mid t_0g_j^*.
}
\tag{6.4}
$$



Define the positive integer


$$
\boxed{
K_j=\frac{\gamma_j|X_j|}{\mathcal C_j}.
}
\tag{6.5}
$$


Then the actual reduced endpoint denominator $d_j$ satisfies, at every prime,


$$
\boxed{
-v_p(L)
\le v_p(d_j)-v_p(K_j)
\le v_p(t_0).
}
\tag{6.6}
$$



#### Proof

Suppress $j$. Put


$$
e=\gcd(|X|,|V|).
$$


Equation (6.3) gives


$$
\mathcal C=\gcd(|X|,|t_0V|).
$$


Therefore


$$
e\mid\mathcal C,\qquad \mathcal C\mid t_0e.
\tag{6.7}
$$



Also,


$$
g^*=\gcd(\gamma|X|,|V|)
=e\,\gcd\!\left(\gamma,\frac{|V|}{e}\right).
\tag{6.8}
$$


By primitivity of the coefficient triple,


$$
\gcd(\gamma,|\mathsf E|)=1.
$$


Since $V=\gamma Y+L\mathsf E$,


$$
\gcd(\gamma,|V|)=\gcd(\gamma,L).
$$


Consequently the second factor in (6.8) divides $L$, and


$$
e\mid g^*\mid Le.
\tag{6.9}
$$


Combining (6.7) and (6.9) proves (6.4).

Finally,


$$
d=\frac{\gamma|X|}{g^*},
\qquad
K=\frac{\gamma|X|}{\mathcal C},
$$


so


$$
v_p(d)-v_p(K)=v_p(\mathcal C)-v_p(g^*).
$$


The bounds follow directly from (6.4). ∎

### Theorem 6.2 — Complete coprime endpoint factor, up to an explicit exponential factor

Put


$$
Z_K=\frac{K_0K_3}{\gcd(K_0,K_3)^2}.
\tag{6.10}
$$


Then


$$
\boxed{
\left|v_p(|AB|)-v_p(Z_K)\right|
\le v_p(Lt_0)
}
\tag{6.11}
$$


for every prime $p$. Equivalently,


$$
\boxed{
Z_K\mid Lt_0|AB|,
\qquad
|AB|\mid Lt_0Z_K.
}
\tag{6.12}
$$



For either selected set,


$$
\boxed{
\left|
\log|AB|_{\mathcal P^c}
-
\log(Z_K)_{\mathcal P^c}
\right|
\le\log(Lt_0)=O(n).
}
\tag{6.13}
$$



#### Proof

The actual complete-row formula is


$$
v_p(|AB|)=|v_p(d_0)-v_p(d_3)|.
$$


Write


$$
v_p(d_j)=v_p(K_j)+\varepsilon_j.
$$


Theorem 6.1 gives


$$
-v_p(L)\le\varepsilon_j\le v_p(t_0).
$$


Hence


$$
|\varepsilon_0-\varepsilon_3|\le v_p(Lt_0).
$$


Apply the reverse triangle inequality to the two denominator imbalances. This proves (6.11); the other statements follow. ∎

### Significance

This theorem provides an exponential-cost reduction of the **actual row-primitive endpoint factor** to a new, explicit arithmetic quantity:


$$
\boxed{
K_j
=
\frac{
\gamma_j|\mathfrak a_jt_0+\mathfrak b_jt_1|
}{
\gcd\!\left(
|\mathfrak a_jt_0+\mathfrak b_jt_1|,
|t_0L\mathsf E_j+\Omega\gamma_j\mathfrak b_j|
\right)
}.
}
\tag{6.14}
$$



Unlike the raw first-column ratio, this quantity pays for:

- the complete exponential endpoint numerator;
- the entire logarithmic response through the exact Wronskian;
- the exterior $+1$;
- coefficient-triple content;
- endpoint row content;
- the common denominator factor between the two endpoints.

The actual denominators $d_j$ have not been replaced silently: their discrepancy from $K_j$ is explicitly bounded at every prime.

---

## 7. The precise extra arithmetic obstruction

### 7.1 Good-prime interpretation

At a prime $p\nmid Lt_0$, Theorem 6.1 is exact:


$$
\boxed{
v_p(d_j)
=
v_p(\gamma_j)+v_p(X_j)-v_p(\mathcal C_j).
}
\tag{7.1}
$$



If in addition $p\nmid\Omega$, then


$$
v_p(Q_j^\kappa)=v_p(X_j).
\tag{7.2}
$$


Indeed, if $p\mid X_j$, primitivity of $(\mathfrak a_j,\mathfrak b_j)$ and the unit $t_0$ force $\mathfrak b_j$ to be a unit.

There are two distinct cases.

**Structural content survives.** If $p\mid\gamma_j$, then $\mathsf E_j$ is a unit and


$$
\mathcal R_j\equiv t_0L\mathsf E_j\not\equiv0\pmod p.
$$


Thus $\mathcal C_j$ is a unit and


$$
v_p(d_j)=v_p(\gamma_j)+v_p(X_j).
$$



**Complete-force cancellation is possible.** If $p\nmid\gamma_j$, a denominator factor of the correction is canceled from the complete center precisely to the depth


$$
\min\!\left(v_p(X_j),v_p(\mathcal R_j)\right).
$$



The exact congruence responsible is


$$
\boxed{
t_0L\mathsf E_j
\equiv-\Omega\gamma_j\mathfrak b_j
\pmod{p^a},
\qquad p^a\mid X_j.
}
\tag{7.3}
$$



This is the additional arithmetic obstruction.

### 7.2 Why noncollapse does not remove it

Noncollapse states $\mathscr D\ne0$. It concerns the two coefficient pairs


$$
(\mathfrak a_0,\mathfrak b_0),\qquad
(\mathfrak a_3,\mathfrak b_3).
$$


The cancellation congruence (7.3) additionally involves $\mathsf E_j$, hence the complete exponential force and the exterior endpoint term.

As an algebraic demonstration of the logical gap, suppose $p\nmid Lt_0\gamma_j$. For fixed coefficient pair and $X_j$, one can choose an auxiliary integer $\mathsf E_j$ satisfying (7.3) to any prescribed depth dividing $X_j$. This does not change the transformation determinant.

That observation is **not** a counterexample on the original families: their $\mathsf E_j$ are fixed specialized values. It proves that a noncollapse theorem alone cannot exclude complete-row cancellation. A successful original-family argument must use additional arithmetic of those fixed values.

### 7.3 A quantitative bridge isolating the two missing contents

Define


$$
R_\gamma
=
\frac{\gamma_0\gamma_3}{\gcd(\gamma_0,\gamma_3)^2},
\qquad
R_{\mathcal C}
=
\frac{\mathcal C_0\mathcal C_3}
{\gcd(\mathcal C_0,\mathcal C_3)^2}.
$$


Then the reverse triangle inequality gives


$$
\boxed{
\log|AB|_{\mathcal P^c}
\ge
\log(Z_X)_{\mathcal P^c}
-\log(R_\gamma)_{\mathcal P^c}
-\log(R_{\mathcal C})_{\mathcal P^c}
-O(n).
}
\tag{7.4}
$$



This is a correction-based bridge, not a raw first-column bridge. Its missing ingredients are now explicit.

A useful next lemma is:

> **Specialized contact-content lemma sought.**  
> On one specified original smooth family, prove
> 

$$
> \log(R_\gamma)_{\mathcal P^c}
> +
> \log(R_{\mathcal C})_{\mathcal P^c}
> =O(n),
>
$$


> or obtain a comparably useful bound directly for the evaluated integers $K_0,K_3$.

Together with a superexponential lower bound for $Z_X$, this would give one for the actual $|AB|_{\mathcal P^c}$. Alternatively, Theorem 6.2 permits a direct growth proof for $Z_K$.

Neither content bound is proved here.

---

## 8. Consequences for the reference-growth route

The new height theorem makes one outstanding obligation especially concrete:


$$
H(\kappa_j)\le\exp(O(n))
$$


is equivalent to an exponential height bound for the primitive pair obtained from the two specialized quadratic moment expressions $(\alpha_j,\beta_j)$.

The available direct clearing argument gives factorial-scale height instead. Thus the reference-growth transfer still lacks a sufficiently strong correction-height theorem.

There is a second, independent issue. Even a satisfactory correction-height estimate would not automatically establish complementary-prime growth of the complete endpoint factor. The contents $\mathcal C_j$ measure cancellation against the complete exponential companion. They must be controlled, or the complete rational approximation argument must otherwise pay for them.

Accordingly:

- the classical reference identity is valid;
- the corrections are genuine and eventually distinct;
- their actual reduced heights are now related to explicit primitive moment pairs;
- their cancellation inside the complete endpoint rows remains an additional arithmetic problem.

This report neither proves the desired transfer nor disproves its possibility.

---

## 9. Actual primitive denominator and whole error

Let the original endpoint rows, reduced using their actual contents, have first components


$$
\widetilde u_0=hA,\qquad
\widetilde u_3=hB,\qquad
\gcd(A,B)=1.
$$


For a reduced weight $\lambda=a/k$, $k>0$, retain


$$
J=B\widetilde v_0-A\widetilde v_3,\qquad
\mathcal V=A\widetilde v_3,\qquad
T=aJ+k\mathcal V,
$$


and


$$
F_{\rm gcd}
=
\gcd(|A|,|a|)\gcd(|B|,|a-k|),
$$




$$
G=\gcd(k,|J|),
\qquad
H_{\rm gcd}
=
\gcd\!\left(h,\frac{|T|}{F_{\rm gcd}G}\right).
$$


The actual primitive pair remains


$$
\boxed{
q_\lambda
=
\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda
=
\operatorname{sgn}(AB)
\frac{T}{F_{\rm gcd}GH_{\rm gcd}}.
}
\tag{9.1}
$$



For $a(a-k)\ne0$,


$$
(q_\lambda)_{\mathcal P^c}
\ge
\frac{|AB|_{\mathcal P^c}}{|a|\,|a-k|}.
$$


The new theorem consequently gives the rigorous, but presently unestimated, bound


$$
\boxed{
(q_\lambda)_{\mathcal P^c}
\ge
\frac{(Z_K)_{\mathcal P^c}}
{(Lt_0)_{\mathcal P^c}|a|\,|a-k|}.
}
\tag{9.2}
$$



The selected-prime law remains exactly


$$
(|AB|)_{\mathcal P}=5n.
$$


It is not extended to unselected primes.

No moving-residue shortcut is used here. If the homogeneous decomposition is invoked later, its complete scalar remains


$$
\Theta
=
\Theta^{\rm flat}
+n!\mathfrak u_n\bigl(F(n)+n!\ell_n\bigr),
\qquad
F(n)=\sum_{t=0}^{n}n^{\underline t}.
$$



Finally, the same-index whole-error identity is unchanged:


$$
\boxed{
q_\lambda S-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{9.3}
$$


A valid irrationality construction requires


$$
\boxed{
0<
q_\lambda|e_3\alpha_{n,2}|
\,|\lambda-\Lambda_{n,2}|
\longrightarrow0.
}
\tag{9.4}
$$



Neither $\mathscr D\ne0$ nor $\kappa_0-\kappa_3\ne0$ proves the nonvanishing in (9.4).

---

## 10. New bounded exact calculation

### 10.1 What is not covered by the retained receipts

The retained receipts do not certify:

- primitive triples $(\mathsf A_j,\mathsf B_j,\mathsf E_j)$;
- the actual reduced corrections and their difference;
- the content integers $\mathcal C_j$;
- the divisibilities in Theorem 6.1;
- the complete-factor comparison in Theorem 6.2.

These are the new implementation targets.

### 10.2 Input and finite limits

Use the single original-family input


$$
\boxed{n=225=15^2.}
$$


Retain:

- contact rows and columns $0,1,2$;
- reconstructed coordinates $0,1,2,3$;
- complete force through $2n+2=452$;
- five exponential moments through index $n+2=227$;
- $\tau,\rho$ through $n+1=226$.

No adjacent producer and no extended inverse is needed.

### 10.3 Required exact outputs

Return the following integers and rational numbers, not merely floating-point logarithms:

1. The full reconstructed $u,v$, the least clearer $d_B$, and all four integer row pairs.
2. All four row contents, with the two endpoint contents explicitly identified.
3. For $j=0,3$:
   

$$
\sigma_j,\ \mathsf A_j,\mathsf B_j,\mathsf E_j,\
   \gamma_j,\mathfrak a_j,\mathfrak b_j,\
   X_j,Y_j,M_j,V_j,g_j^*.
$$


4. The exact reduced $\kappa_0,\kappa_3,\kappa_0-\kappa_3$, their heights and denominators.
5. The integers
   

$$
\mathcal R_j,\mathcal C_j,K_j,Z_X,Z_K.
$$


6. The actual $d_0,d_3,h,A,B$ and
   

$$
|AB|_{\{3,5\}^c}.
$$



The expected exact zero residuals are those of (3.10), (4.1), (5.2), and (6.3). Verify the integer divisibilities (4.4), (6.4), and (6.12) by exact division; complete factorization of large integers is unnecessary.

The accepted local theorem predicts


$$
\begin{array}{c|r|r|r}
p&v_p(d_0)&v_p(d_3)&v_p(|AB|)\\ \hline
3&218&220&2\\
5&107&110&3
\end{array}
$$


and hence


$$
(|AB|)_{\{3,5\}}=1125.
$$



If $\mathscr D\ne0$, additionally form the new, data-dependent weight (5.6). Return its reduced numerator and denominator, and evaluate its complete primitive pair using every factor in (9.1). Direct reduction of


$$
\lambda_n^{\rm ref}c_0+(1-\lambda_n^{\rm ref})c_3
$$


must agree.

No favorable height or whole-error sign is predicted. Any error enclosure must evaluate the complete $e+\pi$ form; an interval containing zero is inconclusive.

This calculation would certify only $n=225$.

---

## 11. Proof-status ledger

| Statement | Status |
|---|---|
| Original families, finite matrix boundaries, complete force | Retained unchanged |
| Five-moment endpoint reduction and complete $N_0,N_3$ | Reused at accepted scope |
| Classical reference and complete logarithmic normalization | Reused at accepted scope |
| Eventual transformation noncollapse | Reused; not whole-error nonvanishing |
| Primitive coefficient-triple representation of the complete rows | Proved here |
| Exact connection to the original least clearer and row contents | Proved here |
| Reduced correction formula and complete gcd | Proved here |
| $H(\kappa_j)$ versus primitive moment-pair height, within $\exp(O(n))$ | Proved here |
| Direct bound $H(\kappa_j)\le\exp(2n\log n+O(n))$ | Proved; insufficient for the intended transfer |
| Exact reduced denominator of $\kappa_0-\kappa_3$ | Proved here |
| Complete logarithmic elimination from the content calculation | Proved as an exact identity |
| Complete row-content divisibilities | Proved here |
| Actual $|AB|$ versus $Z_K$, within the explicit factor $Lt_0$ primewise | Proved here |
| Exponential bound for primitive moment-pair height | Open |
| Specialized contact-content bound for $\mathcal C_0,\mathcal C_3$ | Open |
| Complementary-prime growth of actual $|AB|$ | Open |
| Favorable full primitive denominator and same-index nonzero whole error | Open |
| New computation at $n=225$ | Proposed, not executed |

## Conclusion

The new rigorous result is an explicit arithmetic reduction of the **complete, row-primitive endpoint factor**:


$$
\boxed{
\log|AB|_{\mathcal P^c}
=
\log(Z_K)_{\mathcal P^c}+O(n),
}
$$


with a primewise error bounded by $v_p(Lt_0)$, and with $K_j$ given by the complete specialized formula (6.14).

The correction-height problem has also been sharpened:


$$
\boxed{
\log H(\kappa_j)
=
\log H(\mathfrak a_j,\mathfrak b_j)+O(n).
}
$$


Thus the missing exponential height estimate is genuinely a primitive moment-content problem, not a consequence of the classical logarithmic reference.

The exact remaining denominator obstruction is the evaluated congruence


$$
t_0L\mathsf E_j+\Omega\gamma_j\mathfrak b_j
\equiv0\pmod{p^a},
\qquad p^a\mid X_j,
$$


together with the relative sizes of the two surviving endpoint denominators. Its analysis must retain the complete exponential force and the exterior $+1$.

No infinite bound for these contents, no successful reference-growth transfer, and no sequence satisfying the whole nonzero-error criterion have been established.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


