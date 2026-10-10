> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 8 — Exact endpoint-factor reduction and the obstruction to importing the $b=0$ primitive-growth theorem

## Executive conclusion

The irrationality or rationality of


$$
S=e+\pi
$$


remains unresolved.

This report addresses the proposed **all-prime endpoint-factor route**. It obtains an exact reduction of the actual $d=2$ endpoints to five exponential coefficient moments, two adjacent classical Legendre values, and the complete companion force. It also identifies an important normalization issue:

> The original endpoints $u_0,u_3$ depend only on the contact matrix and first force. The coprime factors $A,B$ in the final denominator formula generally do not: they are formed **after separately reducing the two complete endpoint rows**.

Consequently, a lower bound for the primitive numerator and denominator of $u_0/u_3$ is not automatically a lower bound for the actual $|AB|_{\mathcal P^c}$.

The principal results established here are:

1. **A five-moment formula for both actual endpoint rows.**  
   It uses precisely the original $3\times3$ contact matrix, retains the exterior $+1$, and permits exact evaluation of the actual endpoint factor after all row contents.

2. **An adjacent-Legendre representation of the first and complete logarithmic endpoint responses.**  
   The logarithmic sequence is the classical second-kind polynomial sequence specified in the assignment. No novelty claim is made for that sequence, its convolution, or its classical Wronskian.

3. **An explicit determinant controlling the two endpoint transformations.**  
   It reduces to a linear combination of only three of the five exponential moments.

4. **An infinite noncollapse theorem.**  
   On both original smooth families, for all sufficiently large indices, the two complete logarithmic endpoint corrections to the $b=0$ reference approximant are distinct. Thus the complete logarithmic contribution is not a common reference term that can simply be subtracted from both endpoints.

5. **An exact all-prime evaluation formula for $|AB|_{\mathcal P^c}$, including complete row reduction.**  
   On the original families,
   

$$
\boxed{(|AB|)_{\mathcal P}=5n.}
$$


   The remaining target is therefore the fully reduced denominator imbalance outside $\mathcal P$, not a raw factorial or an unreduced first-column ratio.

This turn **does not prove** superexponential growth of that remaining factor, an infinite subexponential-weight exclusion, or an explicit favorable short-weight family. The exact obstruction is the unbounded, force-dependent cancellation in the two endpoint rows. The accepted $b=0$ primitive-growth theorem cannot presently be transferred across that obstruction.

No tools were executed.

---

## 1. Scope and status of the supplied results

The original infinite families remain


$$
n=15^r,\qquad r\ge2,\qquad \mathcal P=\{3,5\},
\tag{1.1}
$$


and


$$
n=105^r,\qquad r\ge2,\qquad \mathcal P=\{3,5,7\}.
\tag{1.2}
$$



Throughout,


$$
d=2,\qquad b=3.
$$


Contact indices are $0,1,2$; reconstructed coordinates are $0,1,2,3$. The complete force for an individual producer has maximum index exactly $2n+2$.

The following are reused at their accepted scope:

- the complete finite force and contact construction;
- the first-force formula in three consecutive $\tau$-values;
- the local invertibility and endpoint valuation theorems at eligible primes;
- the full endpoint-gcd formula;
- the homogeneous/flat decomposition, including the entire $F(n)$;
- the fixed-$d$ whole-error identity;
- the classical monic Legendre reference and its complete second-kind error;
- the all-degree $b=0$ primitive-growth obstruction.

The supplied homogeneous-budget receipt now certifies the stated homogeneous splitting, terminal identities, invariant determinant, middle-depth outputs, and 80 finite budget probes at


$$
n=15,30,105,210.
$$


It does not certify an infinite endpoint-factor growth theorem. Nor does it constitute the pending independent audit of every Turn 7 exponential-Wronskian assertion.

The derivation below does not use Turn 7’s exponential Wronskian $\omega_n$.

---

## 2. The complete finite producer

Set


$$
Q(z)=1-z+\frac{z^2}{2},\qquad q_j=[z^j]Q(z)^n.
$$


Let


$$
\alpha_0=\alpha_1=1,\qquad
\alpha_j=\alpha_{j-1}-\frac12\alpha_{j-2},
$$


and


$$
\eta_L=\sum_{r=0}^{L}\frac1{r!}
+\sum_{r=1}^{L}\frac{2\alpha_{r-1}}r,
\qquad
\mathcal W_L=L!\eta_L.
$$



The complete contact force is


$$
w_i=
\sum_{j=0}^{\min(2n,n+i)}
q_j(n+i)^{\underline j}\mathcal W_{2n+i-j},
\qquad 0\le i\le2.
\tag{2.1}
$$


Both the exponential and logarithmic contributions remain present.

Write


$$
\mathcal B_N=N![z^N](e^zQ(z)^n).
$$


The contact matrix is


$$
C_{ij}=(n+i)^{\underline j}\mathcal B_{n+i-j}.
\tag{2.2}
$$



For


$$
s_n=(1,-n,n(n+1))^T,\qquad
x=C^{-1}z,\qquad y=C^{-1}w,
$$


the actual endpoints are


$$
u_0=-s_n^Tx,\qquad u_3=x_2,
\tag{2.3}
$$




$$
\boxed{v_0=1-s_n^Ty,\qquad v_3=y_2.}
\tag{2.4}
$$



The exterior $+1$ in $v_0$ will remain explicit.

---

## 3. Exact five-moment reduction of the endpoints

### 3.1 The row-factorial normalization is Toeplitz

Define ordinary coefficients


$$
c_j=[z^j](e^zQ(z)^n)
$$


and the five moments


$$
a=c_{n-2},\quad b=c_{n-1},\quad c=c_n,\quad
d=c_{n+1},\quad e_*=c_{n+2}.
\tag{3.1}
$$


The symbol $e_*$ here is a rational coefficient, not Euler’s number.

Then


$$
C=
\operatorname{diag}(n!,(n+1)!,(n+2)!)\,T_n,
$$


where


$$
\boxed{
T_n=
\begin{pmatrix}
c&b&a\\
d&c&b\\
e_*&d&c
\end{pmatrix}.
}
\tag{3.2}
$$



This is an exact normalization of the original finite matrix. No row or column is added.

Put


$$
\Delta_T=\det T_n
=c^3-2bcd+b^2e_*+ad^2-ace_*.
\tag{3.3}
$$


At the original smooth indices, $\Delta_T\ne0$, since the accepted local theorem gives $\det C\ne0$.

For later use,


$$
\operatorname{adj}(T_n)=
\begin{pmatrix}
c^2-bd&ad-bc&b^2-ac\\
be_*-cd&c^2-ae_*&ad-bc\\
d^2-ce_*&be_*-cd&c^2-bd
\end{pmatrix}.
\tag{3.4}
$$



### 3.2 Two adjacent $\tau$-values suffice

Use the accepted recurrence


$$
(n+2)\tau_{n+2}=(2n+3)\tau_{n+1}+(n+1)\tau_n.
\tag{3.5}
$$


Define


$$
\mathbf v_n=
\begin{pmatrix}
1\\[1mm]1/2\\[1mm](n+1)/(2(n+2))
\end{pmatrix},
\qquad
\mathbf w_n=
\begin{pmatrix}
0\\[1mm]1/2\\[1mm](2n+3)/(2(n+2))
\end{pmatrix}.
\tag{3.6}
$$


Then


$$
\mathbf t_n=
\begin{pmatrix}
\tau_n\\[1mm]
(\tau_n+\tau_{n+1})/2\\[1mm]
\tau_{n+2}/2
\end{pmatrix}
=\tau_n\mathbf v_n+\tau_{n+1}\mathbf w_n.
\tag{3.7}
$$



Dividing the first force by the three row factorials gives exactly


$$
\operatorname{diag}(n!,(n+1)!,(n+2)!)^{-1}z
=n!\mathbf t_n.
$$


Thus


$$
x=n!T_n^{-1}\mathbf t_n.
\tag{3.8}
$$



Let


$$
\ell_0^T=-s_n^T,\qquad \ell_3^T=e_2^T,
\qquad
R_j=\ell_j^T\operatorname{adj}(T_n),\quad j=0,3.
$$


Define


$$
\alpha_j=R_j\mathbf v_n,\qquad
\beta_j=R_j\mathbf w_n,\qquad
\xi_j=\alpha_j\tau_n+\beta_j\tau_{n+1}.
\tag{3.9}
$$



We obtain the exact first-column endpoint formula


$$
\boxed{
u_j=\frac{n!\xi_j}{\Delta_T},\qquad j=0,3.
}
\tag{3.10}
$$



The coefficients $\alpha_j,\beta_j$ are explicit quadratic expressions in the five rational moments (3.1), with rational polynomial factors in $n$.

### 3.3 The complete second row is equally explicit

Normalize the complete force by


$$
\widehat w_i=\frac{w_i}{(n+i)!}.
\tag{3.11}
$$


Equivalently, directly from the complete finite sum,


$$
\widehat w_i
=
\sum_{j=0}^{\min(2n,n+i)}
q_j\frac{\mathcal W_{2n+i-j}}{(n+i-j)!}.
\tag{3.12}
$$



Set


$$
N_0=\Delta_T+R_0\widehat w,\qquad
N_3=R_3\widehat w.
\tag{3.13}
$$


Then


$$
\boxed{
v_0=\frac{N_0}{\Delta_T},\qquad
v_3=\frac{N_3}{\Delta_T}.
}
\tag{3.14}
$$



In particular, the two actual rational centers are


$$
\boxed{
c_0:=\frac{v_0}{u_0}=\frac{N_0}{n!\xi_0},
\qquad
c_3:=\frac{v_3}{u_3}=\frac{N_3}{n!\xi_3}.
}
\tag{3.15}
$$



The $+\Delta_T$ in $N_0$ is the exterior $+1$. Dropping it would change both the complete center and its row content.

Equations (3.1)–(3.15) are an exact endpoint evaluation. They do not yet estimate the reduced heights of these rational quantities.

---

## 4. Classical Legendre overlap and the complete logarithmic normalization

### 4.1 The reference sequences

As specified in the assignment,


$$
\tau_n=i^nP_n(-i),
\qquad
\rho_n=i^{n-1}W_{n-1}(-i).
\tag{4.1}
$$


The sequence $\rho_n$ is classical. In the present normalization,


$$
\rho_0=0,\qquad \rho_1=1,
$$




$$
(n+2)\rho_{n+2}=(2n+3)\rho_{n+1}+(n+1)\rho_n.
\tag{4.2}
$$


Its convolution and Wronskian are


$$
\rho_n=\sum_{j=0}^{n-1}\frac{\tau_j\tau_{n-1-j}}{j+1},
\tag{4.3}
$$




$$
\boxed{
\tau_n\rho_{n+1}-\tau_{n+1}\rho_n
=\frac{(-1)^n}{n+1}.
}
\tag{4.4}
$$



These are not new results of this report.

### 4.2 Normalization against the original complete force

The specialized issue is whether the complete logarithmic contact force has exactly this normalization.

Let


$$
f(0)=0,\qquad f'(z)=\frac2{Q(z)},\qquad
A_n^{\log}(z)=Q(z)^n\left(\frac{f(z)}{1-z}\right)^{(n)}.
$$


Its contact coefficients are the logarithmic part of the original finite force.

The identity


$$
A_{n+1}^{\log}=Q(A_n^{\log})'-nQ'A_n^{\log}
\tag{4.5}
$$


and the accepted terminal recurrence give, with


$$
D_n=n![z^n]A_n^{\log},
$$




$$
D_{n+1}=2(n+1)w_1^{\log}(n)-(n+1)^2D_n,
\tag{4.6}
$$




$$
w_1^{\log}(n+1)
=(n+1)(3n+5)w_1^{\log}(n)
-(n+1)^2(n+2)D_n.
\tag{4.7}
$$


Eliminating $w_1^{\log}(n)$ yields


$$
D_{n+2}
=(n+2)(2n+3)D_{n+1}
+(n+2)(n+1)^3D_n.
$$


Therefore $D_n/(n!)^2$ satisfies (4.2). Directly,


$$
D_0=0,\qquad D_1=4.
$$


Consequently,


$$
D_n=4(n!)^2\rho_n.
$$



Recovering the other two contacts from (4.6) and the terminal relation proves


$$
w^{\log}
=4(n!)^2
\begin{pmatrix}
\rho_n\\[1mm]
\dfrac{n+1}{2}(\rho_n+\rho_{n+1})\\[2mm]
\dfrac{(n+1)(n+2)}2\rho_{n+2}
\end{pmatrix}.
\tag{4.8}
$$



This identifies the complete original logarithmic force with the classical sequence. The coefficient manipulations may use neighboring original producers; they do not extend any finite inverse.

Dividing by the row factorials,


$$
\boxed{
\widehat w^{\log}
=4n!\bigl(\rho_n\mathbf v_n+\rho_{n+1}\mathbf w_n\bigr).
}
\tag{4.9}
$$



Hence the logarithmic endpoint response is


$$
\boxed{
v_j^{\log}
=\frac{4n!}{\Delta_T}
\bigl(\alpha_j\rho_n+\beta_j\rho_{n+1}\bigr),
\qquad j=0,3.
}
\tag{4.10}
$$


Here the exterior $+1$ belongs to the exponential-only companion, not to $v^{\log}$.

### 4.3 Exact relation to the accepted $b=0$ reference

The classical reference approximant in the attached reconstruction is


$$
\boxed{f_n^{\mathrm{ref}}=\frac{4\rho_n}{\tau_n}.}
\tag{4.11}
$$



To check the normalization, let $B_n=\binom{2n}{n}$, and let $v_n^{\mathrm{ref}}$ be the accepted monic second-kind integral. The sequence $B_nv_n^{\mathrm{ref}}$ obeys the same recurrence as $\tau_n,\rho_n$, with initial values


$$
\pi,\qquad \pi-4.
$$


Thus


$$
B_nv_n^{\mathrm{ref}}=\pi\tau_n-4\rho_n,
$$


which proves (4.11) and its exact complete reference error.

Applying (4.4) to (4.10) gives


$$
\boxed{
\frac{v_j^{\log}}{u_j}
=f_n^{\mathrm{ref}}+\kappa_j,
\qquad
\kappa_j=
\frac{4(-1)^n\beta_j}
{(n+1)\tau_n\xi_j}.
}
\tag{4.12}
$$



The correction $\kappa_j$ is the precise extra term that a proposed $b=0$ bridge must handle. It cannot be omitted because $f_n^{\mathrm{ref}}$ has a familiar classical interpretation.

---

## 5. An explicit contiguous determinant and an infinite noncollapse theorem

### 5.1 The determinant reduces to one linear moment

Define


$$
\mathcal H_n=
\frac{b+nc}{4}
-\frac{(2n+3)(c+nd)}{2(n+2)}
+\frac{d+ne_*}{2}.
\tag{5.1}
$$



### Theorem 5.1 — Endpoint transformation determinant



$$
\boxed{
\alpha_0\beta_3-\beta_0\alpha_3
=\Delta_T\mathcal H_n.
}
\tag{5.2}
$$



#### Proof

The cross-product identity for the rows of an adjugate gives


$$
R_0\times R_3
=\Delta_T\bigl(\operatorname{col}_1(T_n)
+n\operatorname{col}_0(T_n)\bigr).
$$


Also,


$$
\mathbf v_n\times\mathbf w_n
=
\begin{pmatrix}
1/4\\[1mm]
-(2n+3)/(2(n+2))\\[1mm]
1/2
\end{pmatrix}.
$$


Taking the scalar product proves (5.2). ∎

There is a further exact simplification. From


$$
Q(e^zQ^n)'=(Q+nQ')e^zQ^n
$$


one obtains


$$
(j+1)c_{j+1}
=(j+1-n)c_j+
\left(n-\frac{j+1}{2}\right)c_{j-1}
+\frac12c_{j-2}.
\tag{5.3}
$$


At $j=n,n+1$, this reduces (5.1) to


$$
\boxed{
\mathcal H_n
=\frac{n+1}{2(n+2)}
\bigl(b+(n-3)c-2(n-1)d\bigr),
}
\tag{5.4}
$$


and then to


$$
\boxed{
\mathcal H_n
=
\frac{-(n-1)a+n(3-n)b+(n^2-4n-1)c}
{2(n+2)}.
}
\tag{5.5}
$$



Thus the contiguous determinant is controlled by only three exponential moments. It has not reduced to a determinant of $\tau$-values alone.

### 5.2 Nonvanishing on the original infinite families

Put


$$
R=\sqrt2,\qquad M=1+\sqrt2.
$$



For each fixed integer $s\in\{-2,-1,0,1,2\}$,


$$
\boxed{
c_{n+s}
=(-1)^{n+s}e^{-R}R^{-s}\tau_n
\bigl(1+O(n^{-1})\bigr).
}
\tag{5.6}
$$



Here is a direct justification. Let


$$
A(z)=1+z+\frac{z^2}{2}.
$$


Then


$$
\tau_n=[z^n]A(z)^n,
\qquad
c_{n+s}=(-1)^{n+s}[z^{n+s}]A(z)^ne^{-z}.
$$


The positive saddle is $z=R$. On the circle $z=Re^{i\theta}$, the normalized central characteristic factor is


$$
\phi(\theta)
=\frac{Re^{0i\theta}+2\cos\theta}{2+R}
=\frac{R+2\cos\theta}{2+R}.
$$


It satisfies


$$
\phi(0)=1,\qquad
\phi(\theta)=1-\frac{2-R}{2}\theta^2+O(\theta^4),
$$


and $|\phi(\theta)|<1$ away from $0$. The extra analytic factor is


$$
e^{-Re^{i\theta}}e^{-is\theta}.
$$


The Gaussian contribution gives $e^{-R}$; odd first-order terms integrate to zero, and the next contribution is $O(n^{-1})$. The complementary arcs are exponentially smaller. This proves (5.6), and also the familiar estimate


$$
\tau_n\sim\frac{M^n}{\sqrt{2\pi n(2-R)}}.
$$



Substituting (5.6) into (5.4) gives


$$
\boxed{
\mathcal H_n
=(-1)^n\frac{M}{2}\,n e^{-R}\tau_n
\bigl(1+O(n^{-1})\bigr).
}
\tag{5.7}
$$


Therefore $\mathcal H_n\ne0$ for every sufficiently large $n$.

The accepted local theorem guarantees $\Delta_T,\xi_0,\xi_3\ne0$ on the original smooth families. Equations (4.12) and (5.2) consequently give


$$
\boxed{
\kappa_0-\kappa_3
=
-\frac{4(-1)^n\Delta_T\mathcal H_n}
{(n+1)\xi_0\xi_3}
\ne0
}
\tag{5.8}
$$


for all sufficiently large indices in either family.

### Meaning of the theorem

This proves an infinite obstruction to a specific proposed simplification:

> The complete logarithmic endpoint contributions are not both the same $b=0$ reference approximant.

For a rational weight $\lambda=a/k$,


$$
\kappa_\lambda=\lambda\kappa_0+(1-\lambda)\kappa_3
$$


vanishes for exactly one rational weight, namely


$$
\boxed{
\lambda_n^{\mathrm{ref}}
=\frac{\beta_3\xi_0}
{\tau_n\Delta_T\mathcal H_n},
}
\tag{5.9}
$$


once (5.8) holds.

This is an explicit family of reference-canceling weights. No subexponential bound for its **reduced** height is proved, and no favorable whole primitive form is asserted for it. In particular, (5.9) is not a solution to the requested short-reconstruction problem.

---

## 6. The actual coprime endpoint factor after complete row reduction

This is the arithmetic distinction needed before any growth estimate.

### 6.1 Reduced endpoint denominators

Let


$$
d_0=\operatorname{den}(c_0),\qquad
d_3=\operatorname{den}(c_3),
\tag{6.1}
$$


where denominators are positive and fractions are fully reduced.

The original procedure takes the least clearer of both complete columns and then separately reduces the two endpoint rows. That procedure gives


$$
|\widetilde u_0|=d_0,\qquad
|\widetilde u_3|=d_3.
$$


This follows because a primitive integer pair representing $v_j/u_j$ has first coordinate of absolute value $\operatorname{den}(v_j/u_j)$. Thus it is independent of which common clearer was used before the row reduction.

Consequently, with


$$
h=\gcd(d_0,d_3),
$$


the actual coprime endpoint factor is


$$
\boxed{
|AB|=\frac{d_0d_3}{h^2}.
}
\tag{6.2}
$$



This is not in general the primitive numerator-denominator product of $u_0/u_3$.

### 6.2 Exact all-prime evaluation

From (3.15), for every prime $p$, define


$$
E_j(p)
=
\max\left\{
0,\,
v_p(n!\xi_j)-v_p(N_j)
\right\},
\qquad j=0,3.
\tag{6.3}
$$


The convention $v_p(0)=+\infty$ covers a zero companion endpoint.

Then


$$
v_p(d_j)=E_j(p)
$$


and therefore


$$
\boxed{
v_p(|AB|)
=
|E_0(p)-E_3(p)|.
}
\tag{6.4}
$$



In particular,


$$
\boxed{
|AB|_{\mathcal P^c}
=
\prod_{p\notin\mathcal P}
p^{\left|
[v_p(n!\xi_0)-v_p(N_0)]_+
-
[v_p(n!\xi_3)-v_p(N_3)]_+
\right|}.
}
\tag{6.5}
$$



Equation (6.5) is the exact endpoint-factor evaluation in terms of the specialized five-moment data and the complete force. It pays:

- cancellation inside the contiguous expressions $\xi_j$;
- cancellation against the complete numerators $N_j$;
- both endpoint row contents;
- the common endpoint factor $h$.

It makes no use of a nonminimal clearer as a denominator estimate.

### 6.3 An integer implementation without ambiguity

For an exact calculation, take a common denominator of the four rational numbers


$$
n!\xi_0,\quad n!\xi_3,\quad N_0,\quad N_3
$$


and obtain integers


$$
M_0,M_3,V_0^*,V_3^*.
$$


This is only a bookkeeping representation. Reduce


$$
g_j=\gcd(|M_j|,|V_j^*|),\qquad d_j=|M_j|/g_j,
$$


then use (6.2). Every factor of the bookkeeping denominator disappears through the indicated gcds.

This is exactly equivalent to the original complete-column normalization, not a replacement for its arithmetic.

### 6.4 An exact infinite selected-prime law

On the original smooth families, put


$$
m_p=2v_p(n!),\qquad w_p=v_p(v_0).
$$


The accepted endpoint theorem gives


$$
v_p(u_0)=v_p(u_3)=m_p,\qquad
v_p(v_3)=0,
$$


and


$$
w_3=r,\qquad w_5=r+1,\qquad w_7=r
$$


when the prime is selected. Since $w_p<m_p$,


$$
E_0(p)=m_p-w_p,\qquad E_3(p)=m_p.
$$


Thus


$$
v_p(|AB|)=w_p.
$$



Therefore, on **both** original families,


$$
\boxed{
(|AB|)_{\mathcal P}=5n,
\qquad
|AB|_{\mathcal P^c}=\frac{|AB|}{5n}.
}
\tag{6.6}
$$



This is an exact infinite-family statement. It is not a growth theorem for the complementary part.

For comparison, $u_0/u_3$ is a unit at every selected prime. Its primitive numerator-denominator product therefore has selected part $1$, whereas the actual $|AB|$ has selected part $5n$. This already disproves a literal identification of the two full factors. It does not, by itself, decide whether their complementary parts might satisfy some further relation.

---

## 7. Why the accepted $b=0$ growth theorem does not yet transfer

The accepted $b=0$ theorem is a theorem about a particular fully reduced endpoint approximant. Its proof has two essential ingredients:

1. an exponentially bounded-height rational logarithmic reference;
2. a rational approximant to $e$ with factorially small error, whose denominator is bounded by the actual endpoint denominator times an exponential factor.

The reference in the present construction is indeed the same classical quantity


$$
f_n^{\mathrm{ref}}=\frac{4\rho_n}{\tau_n}.
$$


That part of the bridge is proved.

The rest is not the same.

From (4.12), the complete weighted center has the exact decomposition


$$
c_\lambda
=
c_\lambda^{\exp}
+f_n^{\mathrm{ref}}
+\kappa_\lambda,
\tag{7.1}
$$


where


$$
\boxed{
\kappa_\lambda
=
\frac{4(-1)^n
\left(a\beta_0\xi_3+(k-a)\beta_3\xi_0\right)}
{k(n+1)\tau_n\xi_0\xi_3}.
}
\tag{7.2}
$$



The denominator in (7.2) is not to be read before reduction. Its reduced denominator can be affected by substantial cancellation in the quadratic exponential moments and in the displayed numerator.

The accepted reference-height estimate does **not** bound this additional rational correction by $\exp(O(n))$. Nor does the accepted $b=0$ theorem bound the complete row contents in (6.5).

The infinite noncollapse theorem shows that $\kappa_\lambda$ is not an identically absent term. The remaining issue is its **reduced arithmetic height**, not merely its real size.

### 7.1 What raw growth fails to establish

The following quantities can be large without proving that $|AB|_{\mathcal P^c}$ is large:

- $n!$;
- the denominators of the moments $c_{n-2},\ldots,c_{n+2}$;
- cleared numerators of $\xi_0,\xi_3$;
- a denominator of $\kappa_\lambda$ before its gcd;
- the denominator of $\omega_n$;
- the least clearer of the full reconstructed columns.

The exact obstruction is visible in (6.5): large valuations in $n!\xi_j$ can be removed by $N_j$, and comparable surviving valuations at the two endpoints disappear again from the coprime factor through $h^2$.

No supplied theorem bounds these two cancellation mechanisms outside the selected primes.

### 7.2 Concrete next arithmetic object

The next content calculation is now explicitly specified, rather than being an unrestricted search for a lattice theorem:



$$
\boxed{
\left(
n!(\alpha_0\tau_n+\beta_0\tau_{n+1}),\
\Delta_T+R_0\widehat w;\
n!(\alpha_3\tau_n+\beta_3\tau_{n+1}),\
R_3\widehat w
\right).
}
\tag{7.3}
$$



A successful follow-on result must control the **difference of the two reduced endpoint denominator valuations** in (6.5). A bound for only one raw numerator or one raw content is insufficient.

Equivalently, a bridge to the accepted $b=0$ theorem must prove a reduced-height estimate for the extra correction (7.2), together with the required complete exponential approximation estimate. Neither follows from the classical second-kind identity alone.

This is the remaining lemma to prove, not a lemma claimed here.

---

## 8. Consequences for weights, with the full gcd retained

Let the original complete endpoint normalization be


$$
\widetilde u_0=hA,\qquad
\widetilde u_3=hB,\qquad \gcd(A,B)=1,
$$


and define


$$
J=B\widetilde v_0-A\widetilde v_3,\qquad
\mathcal V=A\widetilde v_3,\qquad
T=aJ+k\mathcal V.
$$


For reduced $a/k$, $k>0$,


$$
F_{\mathrm{gcd}}
=\gcd(|A|,|a|)\gcd(|B|,|a-k|),
$$




$$
G=\gcd(k,|J|),\qquad
H_{\mathrm{gcd}}
=\gcd\!\left(h,\frac{|T|}{F_{\mathrm{gcd}}G}\right).
$$


The actual primitive pair remains


$$
\boxed{
q_\lambda=
\frac{kh|AB|}{F_{\mathrm{gcd}}GH_{\mathrm{gcd}}},
\qquad
p_\lambda=
\operatorname{sgn}(AB)
\frac{T}{F_{\mathrm{gcd}}GH_{\mathrm{gcd}}}.
}
\tag{8.1}
$$



For $a(a-k)\ne0$,


$$
q_\lambda\ge\frac{|AB|}{|a|\,|a-k|},
$$


and


$$
\boxed{
(q_\lambda)_{\mathcal P^c}
\ge
\frac{|AB|_{\mathcal P^c}}{|a|\,|a-k|}.
}
\tag{8.2}
$$



Thus, for weights of subexponential height,


$$
\log\max(|a|,k)=o(n),
$$


the endpoint factor can lose only $\exp(o(n))$ through these weight factors.

On the original smooth families, (6.6) makes this


$$
\boxed{
(q_\lambda)_{\mathcal P^c}
\ge
\frac{|AB|}{5n\,|a|\,|a-k|}.
}
\tag{8.3}
$$



However, no lower bound of the form


$$
\log|AB|_{\mathcal P^c}\ge cn
\quad\text{or}\quad
\log|AB|_{\mathcal P^c}\ge c n\log n
$$


has been proved here. Therefore (8.3) is not being promoted to an infinite subexponential-weight exclusion.

For an independent exact check, the integer representation in Section 6 gives


$$
c_\lambda
=
\frac{aV_0^*M_3+(k-a)V_3^*M_0}
{kM_0M_3}.
$$


Direct reduction of this fraction must agree with (8.1), including its full gcd.

---

## 9. The complete moving residue and whole error are unchanged

The endpoint-factor calculation does not simplify the actual moving residue.

The accepted homogeneous decomposition remains


$$
\boxed{
\Theta
=
\Theta^{\mathrm{flat}}
+n!\mathfrak u_n\bigl(F(n)+n!\ell_n\bigr),
}
\tag{9.1}
$$


where


$$
F(n)=\sum_{t=0}^{n}n^{\underline t},
\qquad
\ell_n=\sum_{r=1}^{n}\frac{2\alpha_{r-1}}r.
$$


For the exponential-only companion,


$$
\boxed{
\Theta^{\exp}
=
\Theta^{\exp,\mathrm{flat}}
+n!\mathfrak u_n^{\exp}F(n).
}
\tag{9.2}
$$



Neither $F(n)$ nor the complete logarithmic restoration has been deleted. Nothing in the endpoint determinant calculation proves a continued-fraction gap for the residue in (9.2).

The whole evaluated error remains


$$
\boxed{
q_\lambda S-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}),
}
\tag{9.3}
$$


with


$$
e_3=(-1)^{n+1}4\pi M^{-2n-3}(1+O(n^{-1})),
$$




$$
\alpha_{n,2}=\frac2{n^2}(1+O(n^{-1})),
$$




$$
\Lambda_{n,2}
=\frac{n^2}{2}+\frac{1-3\sqrt2}{2}n+O(1).
$$



An irrationality construction still requires


$$
\boxed{
0<
q_\lambda|e_3\alpha_{n,2}|
\,|\lambda-\Lambda_{n,2}|
\longrightarrow0.
}
\tag{9.4}
$$



Even a future large-denominator theorem must be interpreted correctly. It obstructs a favorable denominator budget; by itself it does not rule out an exceptionally small distance to the actual threshold. Conversely, a favorable denominator bound alone does not certify nonvanishing of the whole form.

The nonvanishing of $\mathcal H_n$, of $\kappa_0-\kappa_3$, or of Turn 7’s $\omega_n$ is not the nonvanishing required in (9.4).

---

## 10. Bounded exact arithmetic for personal inspection

No further weight-window enumeration is proposed.

### 10.1 Inputs

Use


$$
n=15,30,105,210,225.
\tag{10.1}
$$


The first four reuse existing complete producers. The additional index


$$
225=15^2
$$


lies in the original infinite family with $r\ge2$.

For each input, retain the original complete force through $2n+2$. The largest required force index is therefore $452$.

### 10.2 Exact identities to verify

Compute the five moments (3.1), $T_n$, its adjugate, and the scalars in Sections 3–5. Verify exact zero residuals for:

1. The matrix normalization
   

$$
C-\operatorname{diag}(n!,(n+1)!,(n+2)!)T_n.
$$



2. Both first endpoints
   

$$
u_j-\frac{n!\xi_j}{\Delta_T},\qquad j=0,3.
$$



3. Both complete second endpoints
   

$$
v_0-\frac{\Delta_T+R_0\widehat w}{\Delta_T},
   \qquad
   v_3-\frac{R_3\widehat w}{\Delta_T}.
$$



4. The complete logarithmic endpoint identities (4.10).

5. The transformation determinant
   

$$
\alpha_0\beta_3-\beta_0\alpha_3-\Delta_T\mathcal H_n.
$$



6. Equality of the three formulas (5.1), (5.4), and (5.5).

7. The correction difference (5.8).

8. Equality of the endpoint factor computed:
   - from the original full-column normalization;
   - from the reduced denominators $d_0,d_3$;
   - from the integer-pair calculation in Section 6.3.

Every listed residual should be exactly zero over $\mathbb Q$.

### 10.3 Predicted output at the first original smooth index

At $n=225$,


$$
v_3(225!)=110,\qquad v_5(225!)=55.
$$


The accepted local theorem therefore predicts


$$
\begin{array}{c|r|r|r}
p&v_p(d_0)&v_p(d_3)&v_p(|AB|)\\ \hline
3&218&220&2\\
5&107&110&3
\end{array}
$$


and hence


$$
\boxed{(|AB|)_{\{3,5\}}=3^2\,5^3=1125=5n.}
\tag{10.2}
$$



The requested new arithmetic output is the **actual integer**


$$
|AB|_{\{3,5\}^c}
$$


after complete row reduction, together with the full row gcds that produced it. Its value is not predicted here.

### 10.4 Non-vacuous primitive-reduction probes

At these inputs, use only the fixed normalization probes


$$
\lambda=0,\qquad 1,\qquad \frac12,\qquad \frac{n^2}{2},
$$


reducing the last weight when necessary. These are not a threshold-window search.

For each probe, return:

- the original least two-column clearer;
- both endpoint row contents;
- $A,B,h$;
- $F_{\mathrm{gcd}},G,H_{\mathrm{gcd}}$;
- the actual primitive $p_\lambda,q_\lambda$;
- agreement with direct reduction of the rational center.

If whole-error intervals are included, they must use the complete center and complete $e+\pi$. Fixed rational factorial-series and Machin-series bounds are suitable; an interval containing zero must be reported as inconclusive, not as nonvanishing.

These checks would certify only their stated finite inputs.

---

## 11. Final proof ledger and exact remaining bottleneck

### Results established in this report

- An exact five-moment representation of the original finite contact matrix.
- Exact adjacent-$\tau$ formulas for both first-column endpoints.
- Exact formulas for both complete endpoint numerators, including the exterior $+1$.
- Normalization of the complete original logarithmic force against the classical Legendre second-kind sequence.
- Identification of the accepted $b=0$ reference term inside each logarithmic endpoint ratio.
- An explicit contiguous determinant
  

$$
\alpha_0\beta_3-\beta_0\alpha_3=\Delta_T\mathcal H_n,
$$


  with $\mathcal H_n$ reduced to three exponential moments.
- A rigorous asymptotic proving $\mathcal H_n\ne0$ eventually.
- An infinite noncollapse theorem for the two logarithmic endpoint corrections.
- An explicit reference-canceling rational weight, without a claimed reduced-height bound.
- An exact all-prime formula for the actual coprime endpoint factor after complete row reduction.
- The exact original-family law
  

$$
(|AB|)_{\mathcal P}=5n.
$$



### What is not established

There is still no proof of:

- superexponential or sufficiently large exponential growth of $|AB|_{\mathcal P^c}$;
- an infinite subexponential-weight exclusion for the correct moving residue;
- a favorable explicit subexponential-height family;
- a bridge transferring the accepted $b=0$ primitive-growth theorem to these actual $d=2$ endpoint rows;
- a new sequence of nonzero whole primitive forms tending to zero.

### Exact bottleneck

The unresolved endpoint-factor problem is now


$$
\boxed{
\text{Estimate }
\sum_{p\notin\mathcal P}
\left|
[v_p(n!\xi_0)-v_p(N_0)]_+
-
[v_p(n!\xi_3)-v_p(N_3)]_+
\right|\log p
}
$$


on one of the original smooth families.

All quantities in this expression have been explicitly reduced to the five actual exponential moments, the adjacent classical Legendre values, and the complete finite force. The missing theorem is a bound **after those cancellations**, not a bound for the unreduced determinants.

The classical reference supplies an exact part of the logarithmic response, but the additional rational corrections are genuinely present on the infinite families. Their reduced arithmetic height, and the force-dependent endpoint contents, are the precise obstruction to applying the closed $b=0$ result.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


