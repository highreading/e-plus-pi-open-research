> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 3 — Corrected integral evaluation and cancellation of the complete boundary channel

## Executive summary

The rationality or irrationality of $e+\pi$ remains unresolved.

The denominator identity displayed in A5 Turn 2 was false:


$$
(1-t)^2\ne (1-t^2)-2t.
$$


The correct identity is


$$
\boxed{(1-t)^2=(1-t^2)-2t(1-t).}
$$


The parent’s replacement of the denominator multiplier is correct. Its proof is given below independently of the seven reported finite checks.

The corrected evaluator retains the following properties:

* exact treatment of each finite offset tail;
* preservation of the raw modulus $2^L$, with no additional whole-pair clearing loss;
* cubic polynomial support;
* at most $32$ exponent/target classes after the specified initial stage.

The last assertion requires a separate support argument. Coincident exponent tuples do **not** imply coincident support-box centers. An absolute-coordinate bound proves a safe union bound without making that assumption.

The principal new result concerns the **actual completed source assembly**, rather than arbitrary kernels:

> **Complete boundary-channel cancellation.**  
> For the complete type-$2$ assembly, the sum of the offset tails is exactly the physical terminal contribution, modulo the paid raw modulus. For the exponential pairing this includes both terminal terms:
> 

$$
> W_b^2\,b z^f_{b-1}(bz^k_{b-1}+1).
>
$$


> Consequently, the complete raw norm and exponential response can be evaluated by the uncorrected coefficient acceptances alone—**not because the individual tails vanish, but because their assembled subtraction cancels the separately retained physical terminal**.

This is a source-dependent cancellation. Its proof uses the full finite completion


$$
\widehat z^f=\overline z^f,\qquad
\widehat z^k=\overline z^k-s
\pmod{2^L},
$$


where bars denote zero-padded physical contact vectors and


$$
s=\sum_{t=0}^{T}\frac{(b+t)!}{b!}e_{b+t}.
$$


In particular, the auxiliary value $\widehat z^k_b=-1$ is used only to prove the cancellation; it is never substituted for the physical contact value $z^k_b=0$.

After this cancellation, the at-most-$32$ classes can be placed in one common integral observation module using only bounded-degree multipliers. I give explicit integral differential operators whose images are annihilated by its acceptance functional. These supply a concrete, division-free sufficient certificate for a future relative law.

They do **not** establish that the actual relative polynomial belongs to that annihilator. No new infinite-original nonzero digit of $E$, and no nontrivial infinite-family law $E-r(u)Q$, is proved here.

---

## 1. Original objects, boundaries, and proof scope

Throughout the original problem,


$$
\boxed{b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.}
$$


The contact matrix has exactly the indices $0\le i,j<b$. Physical reconstruction has exactly the rows $0\le j\le b$.

Set


$$
h=\frac n2,\qquad
R=2^h\binom nh,\qquad
\Lambda=\frac{(n!)^2}{2^n},
$$




$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
\lambda_s=s![z^s]\phi(z)^n,\qquad
W_j=\binom{n+2}{j}.
$$


The finite matrix and normalized force are


$$
A_{ij}
=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j},
$$




$$
f_i^0=
\frac{(n+i)!}{n!}
[t^n](1+2t+2t^2)^n(1+t)^i,
\qquad
\mathfrak f=f^0/R.
$$



For a contact vector $z$, physical reconstruction is


$$
(\mathcal Rz)_j=W_j(jz_{j-1}-z_j),
\qquad z_{-1}=z_b=0.
$$


The corrected columns remain


$$
x=\frac12\mathcal RA^{-1}\mathfrak f,
\qquad
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$


No component of $h^e+h^F$ is being deleted.

Write


$$
x=2^ax_0,\qquad
z^f=A^{-1}\mathfrak f,\qquad
z^k=A^{-1}k,
\qquad
k=\frac{h^e-A(j!)_{0\le j<b}}{b!}.
$$


The actual content $a$ is retained symbolically.

Define


$$
\mathcal U=\mathfrak f^T\mathcal B\mathfrak f,
\qquad
\mathcal V=\mathfrak f^T(\mathcal Bk+v_{\rm term}),
$$


where


$$
\mathcal B=A^{-T}\mathcal R^T\mathcal RA^{-1},
\qquad
v_{\rm term}=bW_b^2A^{-T}e_{b-1}.
$$


Thus


$$
\boxed{Q=2^{-2a-2}\mathcal U,\qquad E=2^{-a-3}\mathcal V.}
\tag{1.1}
$$



Writing $\Delta_jz=jz_{j-1}-z_j$, the complete raw forms are


$$
\mathcal U=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)^2
+b^2W_b^2(z^f_{b-1})^2,
\tag{1.2}
$$


and


$$
\boxed{
\mathcal V=
\sum_{j=0}^{b-1}W_j^2
(\Delta_jz^f)(\Delta_jz^k)
+W_b^2\,b z^f_{b-1}(bz^k_{b-1}+1).
}
\tag{1.3}
$$



### Reused results

The Turn 1 normal-ordering and finite-completion results are reused at their stated scope. Their expensive audits and the earlier loss calculations are not repeated.

At raw precision $2^L$, $L\ge1$, put


$$
I=\min(b-1,8L-2),\qquad m=4(L-1),
$$




$$
d_{\rm tail}=\min(m,b),\qquad
T=\min(2L-1,2n-1),\qquad V=T+m.
\tag{1.4}
$$


The reused filtrations are


$$
\mathfrak f_i\equiv0\pmod{2^L}\quad(i>I),
\qquad
\lambda_s\equiv c_s\equiv0\pmod{2^L}\quad(s>m),
$$


with


$$
c_0=1,\qquad
c_s=-\sum_{r=1}^s\binom sr\lambda_rc_{s-r}.
$$


The complete source has the paid prefix


$$
k\equiv
\sum_{t=0}^{T}a_t\mathbf a_{b+t}\pmod{2^L},
\qquad
a_t=\frac{(b+t)!}{b!}.
\tag{1.5}
$$



For the kernel representation below, impose the bounded-precision hypothesis


$$
\boxed{n>4D+2,\qquad D=I+2m+T+4.}
\tag{1.6}
$$


This is not a half-length precision theorem.

The seven supplied repaired-Cartier checks establish only their seven listed finite cases. They neither prove the merging bound nor determine an original-family primitive observation. In particular, every reported offset-tail residue in that receipt is zero at its reported modulus; the receipt is not evidence of nontrivial assembled tail cancellation.

---

## 2. Corrected full kernel-evaluation theorem

### 2.1 Exact coefficient identity and finite tail

Consider


$$
\begin{aligned}
\mathcal K(d;\eta_1,\varepsilon_1;\eta_2,\varepsilon_2)
={}&\sum_{j=0}^{b-1}
\binom{n+2}{j}^{2}\binom jd\\
&\quad\cdot
\binom{2n+b+\eta_1-j}{b+\varepsilon_1-j}
\binom{2n+b+\eta_2-j}{b+\varepsilon_2-j}.
\end{aligned}
\tag{2.1}
$$


Use the zero convention for a negative lower binomial index.

Order the two factors so that $\varepsilon_1\le\varepsilon_2$, and set


$$
\delta=\varepsilon_2-\varepsilon_1,\qquad
a_i=\eta_i-\varepsilon_i,
$$




$$
N=n+2,\qquad A=2n+a_1,\qquad B=2n+a_2.
$$


For this identity assume


$$
0\le d\le N,\qquad
\delta\ge0,\qquad A-\delta\ge0,\qquad B\ge0,\qquad
b+\varepsilon_1\ge0.
\tag{2.2}
$$



The integral Euler identity is


$$
\sum_{k\ge0}
\binom{A+k}{k}\binom{B+k+\delta}{k+\delta}t^k
=
\frac{
\sum_{\ell\ge0}
\binom{A-\delta}{\ell}
\binom{B+\delta}{\ell+\delta}t^\ell}
{(1-t)^{A+B+1}}.
\tag{2.3}
$$


Its exact scope is important: the numerator is a polynomial under (2.2). One verification uses the coefficient recurrences


$$
(k+1)(k+\delta+1)h_{k+1}
=(k+A+1)(k+B+\delta+1)h_k
$$


and


$$
(\ell+1)(\ell+\delta+1)p_{\ell+1}
=(A-\delta-\ell)(B-\ell)p_\ell.
$$


Substitution of $H=(1-t)^{-A-B-1}P$ into the associated differential equation gives the first recurrence and the same constant coefficient. This proves (2.3) over $\mathbb Q[[t]]$; all its displayed coefficients are integers.

Also,


$$
\sum_{\ell\ge0}
\binom{A-\delta}{\ell}
\binom{B+\delta}{\ell+\delta}t^\ell
=
\operatorname{CT}_Y
Y^\delta(1+tY)^{A-\delta}(1+1/Y)^{B+\delta},
\tag{2.4}
$$


and


$$
\sum_{j\ge0}\binom Nj^2\binom jd\,t^j
=
\binom Nd\operatorname{CT}_X
X^d(1+X)^{N-d}(1+t/X)^N.
\tag{2.5}
$$



Define


$$
\begin{aligned}
N_1&=n+2-d,&N_2&=n+2,\\
N_3&=2n+a_1-\delta,&N_4&=2n+a_2+\delta,\\
M&=4n+a_1+a_2+1,&B_{\rm tar}&=b+\varepsilon_1.
\end{aligned}
\tag{2.6}
$$


If $\varepsilon_1\ge0$, define the exact offset tail


$$
\begin{aligned}
\mathcal T_{\rm off}
={}&\sum_{k=0}^{\varepsilon_1}
\binom{N}{b+\varepsilon_1-k}^{2}
\binom{b+\varepsilon_1-k}{d}\\
&\quad\cdot
\binom{A+k}{k}
\binom{B+k+\delta}{k+\delta};
\end{aligned}
\tag{2.7}
$$


otherwise set $\mathcal T_{\rm off}=0$.

Then


$$
\boxed{
\mathcal K=
\binom{n+2}{d}
[t^{B_{\rm tar}}X^0Y^0]
\frac{
X^dY^\delta\prod_{i=1}^4(1+v_i)^{N_i}}
{(1-t)^M}
-\mathcal T_{\rm off},
}
\tag{2.8}
$$


where


$$
v_1=X,\qquad v_2=t/X,\qquad v_3=tY,\qquad v_4=1/Y.
$$



Indeed, the substitution $b=j+r$ makes the original endpoint $r\ge1$. Setting $k=r+\varepsilon_1$, the Euler series starts at $k=0$. For $\varepsilon_1\ge0$, its extra terms are exactly $r=-\varepsilon_1,\ldots,0$, which give (2.7). For $\varepsilon_1<0$, the omitted lower-index terms are already zero.

Thus the finite boundary has not been replaced by an uncorrected infinite sum.

### 2.2 The corrected denominator transition

Work in the $t$-adic ring


$$
(\mathbb Z/2^L\mathbb Z)[X^{\pm1},Y^{\pm1}][[t]].
$$


Write


$$
M=2h_0+\epsilon_0,\qquad \epsilon_0\in\{0,1\},
\qquad
M'=h_0+\epsilon_0+L-1.
$$


The corrected multiplier is


$$
\boxed{
K_0(t)=
\sum_{s=0}^{L-1}
2^s\binom{h_0+s-1}{s}
t^s(1-t)^s(1-t^2)^{L-1-s}.
}
\tag{2.9}
$$


For $h_0=0$, the negative-binomial coefficient is $1$ at $s=0$ and $0$ for $s>0$.

Then


$$
\boxed{
(1-t)^{-M}\equiv
\frac{(1+t)^{\epsilon_0}K_0(t)}
{(1-t^2)^{M'}}
\pmod{2^L}.
}
\tag{2.10}
$$



**Proof.** The correct integer identity gives


$$
(1-t)^2
=(1-t^2)\left(1-\frac{2t(1-t)}{1-t^2}\right).
$$


Therefore


$$
(1-t)^{-2h_0}
=
(1-t^2)^{-h_0}
\sum_{s\ge0}
2^s\binom{h_0+s-1}{s}
\frac{t^s(1-t)^s}{(1-t^2)^s}.
$$


Every term with $s\ge L$ is zero modulo $2^L$. Putting the surviving terms over the common denominator
$(1-t^2)^{h_0+L-1}$, and using


$$
(1-t)^{-1}=\frac{1+t}{1-t^2},
$$


proves (2.10). All expansions have integral coefficients. ∎

The omitted factor in Turn 2 was therefore essential, not cosmetic.

Each summand of $K_0$ has degree at most


$$
s+s+2(L-1-s)=2L-2.
$$


Consequently


$$
\deg\bigl((1+t)^{\epsilon_0}K_0(t)\bigr)\le2L-1.
\tag{2.11}
$$



### 2.3 Numerator transition and acceptance

For $i=1,\ldots,4$, write


$$
N_i=2h_i+\epsilon_i,\qquad
H_i=\min(h_i,L-1),\qquad N_i'=h_i-H_i,
$$


and define


$$
K_i(v)=
\sum_{r=0}^{H_i}
2^r\binom{h_i}{r}v^r(1+v^2)^{H_i-r}.
\tag{2.12}
$$


The binomial expansion of $((1+v^2)+2v)^{h_i}$ gives


$$
(1+v)^{N_i}
\equiv
(1+v)^{\epsilon_i}K_i(v)(1+v^2)^{N_i'}
\pmod{2^L}.
\tag{2.13}
$$



A state means


$$
\mathcal A(P;\mathbf N,M,B_{\rm tar})
=
[t^{B_{\rm tar}}X^0Y^0]
P\,\frac{\prod_i(1+v_i)^{N_i}}{(1-t)^M}.
$$


Initially $P=X^dY^\delta$.

For $e=B_{\rm tar}\bmod2$, use


$$
\boxed{
P'=\mathcal C_{(e,0,0)}
\left(
P(1+t)^{\epsilon_0}K_0(t)
\prod_{i=1}^4(1+v_i)^{\epsilon_i}K_i(v_i)
\right),
}
\tag{2.14}
$$


where


$$
\mathcal C_{\boldsymbol e}
\left(\sum c_{a,b,c}t^aX^bY^c\right)
=
\sum c_{2a+e_t,\,2b+e_X,\,2c+e_Y}t^aX^bY^c.
$$


Update


$$
N_i\leftarrow N_i',\qquad
M\leftarrow M',\qquad
B_{\rm tar}\leftarrow\lfloor B_{\rm tar}/2\rfloor.
\tag{2.15}
$$



Equations (2.10) and (2.13) leave all unexpanded factors as functions of
$t^2,X^2,Y^2$. Cartier extraction therefore proves that every transition preserves the state’s acceptance modulo $2^L$.

When $B_{\rm tar}=0$ and every $N_i=0$, acceptance is


$$
\boxed{[t^0X^0Y^0]P.}
\tag{2.16}
$$


There are no negative $t$-powers, and the remaining denominator has constant coefficient $1$.

The number of shifts is $O(\log(n+b+D))$. No division by $2$ occurs in the state action.

---

## 3. Support, merging, and initial assembly cost

Put


$$
J=2L-1,\qquad
r_f=m+I+1,\qquad
\rho=T+2m+1,\qquad
\Delta_\varepsilon=\rho+I+1.
$$


The actual reconstructed atoms satisfy


$$
0\le d\le2r_f,\qquad
-I-1\le\varepsilon_i\le\rho,\qquad
-1\le a_i\le r_f-1.
\tag{3.1}
$$


In particular,


$$
0\le\delta\le\Delta_\varepsilon.
$$


These inequalities, together with (1.6), imply all the hypotheses (2.2), including $b+\varepsilon_1\ge b-I-1\ge0$.

### 3.1 Single-state support

Each multiplier in (2.14) has degree at most $J$ in its indicated monomial. Thus one transition adds $X$- and $Y$-exponents only in $[-J,J]$, and adds $t$-degree at most $3J$.

For a single state,


$$
w_X'\le\lfloor w_X/2\rfloor+J,\qquad
w_Y'\le\lfloor w_Y/2\rfloor+J.
$$


Starting from one monomial gives


$$
w_X,w_Y\le2J,\qquad \deg_tP\le3J.
$$


A safe single-state bound is consequently


$$
\boxed{(3J+1)(2J+1)^2=(6L-2)(4L-1)^2.}
\tag{3.2}
$$



### 3.2 Why coincident tuples are not enough

An exponent/target tuple does not record the location of the Laurent support. Two states with the same tuple may have arrived from different $d,\delta$, and may have different support centers.

The required union estimate follows instead from absolute coordinates.

After $s$ shifts, every descendant of an initial monomial $X^dY^\delta$ has


$$
-J(1-2^{-s})+\frac d{2^s}
\ \le x\le\
J(1-2^{-s})+\frac d{2^s},
\tag{3.3}
$$


and the analogous bound with $y,\delta$. This follows directly by iterating


$$
x'=(x+\mu)/2,\qquad -J\le\mu\le J.
$$


It does not require the multiplier polynomials to be identical.

Taking the union over the actual initial offsets yields the safe bounds


$$
x\in\left[-J,\ J+\left\lceil\frac{2r_f}{2^s}\right\rceil\right],
$$




$$
y\in\left[-J,\ J+\left\lceil\frac{\Delta_\varepsilon}{2^s}\right\rceil\right],
\qquad 0\le\deg_tP\le3J.
\tag{3.4}
$$



### 3.3 The at-most-$32$ assertion

The initial spreads of


$$
N_1,N_3,N_4,M,B_{\rm tar}
$$


are bounded respectively by


$$
2r_f,\quad r_f+\Delta_\varepsilon,\quad
r_f+\Delta_\varepsilon,\quad2r_f,\quad\Delta_\varepsilon.
$$


The exponent $N_2$ is common to all kernels.

The update maps


$$
N\longmapsto\max(\lfloor N/2\rfloor-(L-1),0),
$$




$$
M\longmapsto\lceil M/2\rceil+L-1,
\qquad
B\longmapsto\lfloor B/2\rfloor
$$


send an interval of integer width $w$ to one of width at most
$\lceil w/2\rceil$.

Hence, after


$$
\boxed{
t_0=\left\lceil
\log_2\max(2r_f,r_f+\Delta_\varepsilon)
\right\rceil,
}
\tag{3.5}
$$


each of the five varying entries has at most two values. There are at most $2^5=32$ tuples.

At this same stage, (3.4) gives a safe union bound per tuple:


$$
\boxed{(3J+1)(2J+2)^2=(6L-2)(4L)^2.}
\tag{3.6}
$$


Thus the numerical bound stated in Turn 2 can be retained, but its justification must be the absolute-coordinate argument—not an inference from coincident tuples.

### 3.4 Initial assembly is not free

Let


$$
C_m=\frac{(m+1)(m+2)}2.
$$


Before collecting duplicate atoms, valid bounds for the contact-profile atom occurrences are


$$
A_f\le C_m\left(\frac{(I+1)(I+2)}2+m\right),
\qquad
A_k\le C_m(V+1).
\tag{3.7}
$$


Reconstruction at most doubles each count.

The product identity


$$
\binom jd\binom je
=
\sum_{r=\max(d,e)}^{d+e}
\frac{r!}{(r-d)!(r-e)!(d+e-r)!}\binom jr
\tag{3.8}
$$


has integral multinomial coefficients and at most $\min(d,e)+1$ terms. Conservative emission bounds are therefore


$$
4A_f^2(r_f+1)
$$


for the norm and


$$
4A_fA_k(\min(r_f,m+1)+1)
$$


for the exponential product.

These are polynomial but potentially substantial. The number of distinct offset kernels is bounded by


$$
(2r_f+1)(\Delta_\varepsilon+1)^2(r_f+1)^2,
\tag{3.9}
$$


before exploiting further symmetry.

The finite Schur assembly, the paid scalar source coefficients, and especially the normalized-force computation must also be supplied. The support theorem alone is not a practical runtime certificate for a primitive original-family calculation.

---

## 4. Complete type-$2$ assembly retained

This section records the inputs needed for the new cancellation.

Let $P,U,H$ be the finite Pascal, upper-binomial, and symbol matrices:


$$
P_{ij}=\binom ij,\qquad
U_{ij}=\binom n{j-i},\qquad
H_{ij}=\lambda_{i-j}\binom ij
$$


on their appropriate triangular ranges. Then


$$
(H^{-1})_{ij}=c_{i-j}\binom ij.
$$



Retain


$$
F_{jv}=
-\sum_{q=0}^v
\binom{-n}{b+q-j}\binom n{v-q},
$$




$$
K_{rt}=
\lambda_{d_{\rm tail}+r-t}
\binom{b+r}{d_{\rm tail}+r-t},
$$




$$
G_v=E_{\rm tail}^TH^{-1}F_{\cdot v},
\qquad
S=I+E_{\rm tail}^TH^{-1}F^{(m)}K.
$$


The matrix $S$ is a $2$-adic unit matrix.

For the first force,


$$
D_f=E_{\rm tail}^TH^{-1}U^{-1}P^{-1}\mathfrak f_{\le I},
\qquad
\eta_f=U_n^{(m)}KS^{-1}D_f.
\tag{4.1}
$$


For the complete source,


$$
\xi_v=
\sum_{t=0}^{T}a_t
\sum_{\substack{0\le r\le t\\0\le v-r\le m}}
\binom n{t-r}\lambda_{v-r}\binom{b+v}{v-r},
$$




$$
\delta_v=(KS^{-1}G^{[V]}\xi)_v-\xi_v,
\qquad
\theta_v=\sum_{w=v}^{V}\binom n{w-v}\delta_w.
\tag{4.2}
$$


The $K$-term is padded by zeros beyond its $m$ coordinates. No returned-source term is removed from these formulas.

The profiles are


$$
\begin{aligned}
\Psi_{jv}
={}&(-1)^{b+v-j}
\sum_{s=0}^m(-1)^sc_s
\sum_{r=0}^s
\binom{n+r-1}{r}\binom j{s-r}\\
&\quad\cdot
\binom{2n+b+v+s-1-j}{b+v+s-r-j},
\end{aligned}
\tag{4.3}
$$


and


$$
\begin{aligned}
B_{ji}
={}&(-1)^{j-i}
\sum_{s=0}^m(-1)^sc_s
\sum_{r=0}^s\binom{n+r-1}{r}
\sum_{q=0}^i\binom{2n+r+q-1}{q}\\
&\quad\cdot
\binom{s-r+i-q}{s-r}
\binom j{s-r+i-q}
\binom{2n+b+s-1-j}{b+s-r-q-1-j}.
\end{aligned}
\tag{4.4}
$$


Thus, on $0\le j<b$,


$$
z^f_j\equiv
\sum_{i=0}^{I}\mathfrak f_iB_{ji}
+\sum_{v=0}^{m-1}(\eta_f)_v\Psi_{jv},
\qquad
z^k_j\equiv\sum_{v=0}^{V}\theta_v\Psi_{jv}.
\tag{4.5}
$$



The complete differential source remains


$$
\mathscr L_n
\left(
\frac{\phi^ng_n-e^z\phi^nU_b}{b!}
\right)
=
e^z\phi^{n+1}(C_{b-1}+C_b),
\tag{4.6}
$$


where


$$
C_j(z)=\sum_{r=0}^j\binom n{j-r}\frac{z^r}{r!},
\qquad
U_b(z)=\sum_{j=0}^{b-1}j!C_j(z).
$$


Both differential boundaries remain present.

---

## 5. New result: the assembled offset tails cancel the physical terminal

### 5.1 Extending the finite formulas without inventing contact equations

In divided-power coordinates, write


$$
\mathcal J=\mathcal U_{-n}\mathcal H_c\mathcal U_{-n},
\qquad
\mathcal U_\gamma=(1+\partial_z)^\gamma.
$$


The reused normal-order formula is


$$
\mathcal J
=
\sum_{s=0}^m c_s
\sum_{r=0}^s
(-1)^r\binom{n+r-1}{r}
M_{z^{[s-r]}}\mathcal U_{-(2n+r)}.
\tag{5.1}
$$



Let $q^f$ be the completed transformed force vector: its contact part is
$P^{-1}\mathfrak f_{\le I}$, and its exterior part is $\eta_f$.
Let


$$
q^\theta=\sum_{v=0}^{V}\theta_ve_{b+v},
\qquad
s=\sum_{t=0}^{T}a_te_{b+t}.
$$


The finite-completion proofs give, as **whole finite polynomial coefficient vectors**,


$$
\boxed{
\mathcal Jq^f\equiv\overline z^f,\qquad
\mathcal Jq^\theta\equiv\overline z^k-s
\pmod{2^L}.
}
\tag{5.2}
$$


Here $\overline z^f,\overline z^k$ are the physical contact solutions padded by zero. Equation (5.2) is stronger than equality only on $j<b$, but introduces no new contact equation.

For clarity, the closed formulas (4.3)–(4.4) also represent these polynomial vectors beyond the contact range.

For $\Psi$, this follows directly from (5.1). For the head profile, the only point needing verification is the finite hockey-stick identity


$$
\begin{aligned}
&\sum_{k=\max(\ell,i)}^{b-1}
\binom{\alpha+k-\ell-1}{k-\ell}\binom ki\\
&\qquad=
\sum_{q=0}^{i}
\binom{\alpha+q-1}{q}
\binom{\ell}{i-q}
\binom{\alpha+b-1-\ell}{b-1-\ell-q}.
\end{aligned}
\tag{5.3}
$$


For $0\le\ell\le b-1$, expand


$$
\binom ki=\sum_q\binom\ell{i-q}\binom{k-\ell}{q}
$$


and use


$$
\binom{\alpha+v-1}{v}\binom vq
=
\binom{\alpha+q-1}{q}
\binom{\alpha+v-1}{v-q},
$$


followed by hockey-stick summation. For $\ell>b-1$, both sides are zero by the negative-lower-index convention.

Taking $\ell=j-(s-r)$ and using


$$
\binom j{s-r}\binom{j-(s-r)}{i-q}
=
\binom{s-r+i-q}{s-r}\binom j{s-r+i-q}
$$


gives (4.4) for every relevant $j\ge0$. When $j<s-r$, all terms vanish.

Denote these extended profile formulas by $\widehat z^f,\widehat z^k$. Thus (5.2) says


$$
\widehat z^f\equiv\overline z^f,\qquad
\widehat z^k\equiv\overline z^k-s.
\tag{5.4}
$$



### 5.2 Reconstruction of the complete exterior source

For $j\ge0$, let


$$
\widehat F_j=j\widehat z^f_{j-1}-\widehat z^f_j,
\qquad
\widehat G_j=j\widehat z^k_{j-1}-\widehat z^k_j.
$$


The factorial coefficients obey


$$
a_t=(b+t)a_{t-1}\qquad(t\ge1).
$$


Consequently,


$$
\Delta_js=
\begin{cases}
-1,&j=b,\\
0,&b<j\le b+T,\\
a_{T+1},&j=b+T+1,\\
0,&\text{otherwise}.
\end{cases}
\tag{5.5}
$$


The last term is retained here; it need not be deleted to prove the pairing result.

From (5.4),


$$
\widehat F_j\equiv
\begin{cases}
\Delta_jz^f,&j<b,\\
bz^f_{b-1},&j=b,\\
0,&j>b,
\end{cases}
\tag{5.6}
$$


and


$$
\widehat G_j\equiv
\begin{cases}
\Delta_jz^k,&j<b,\\
bz^k_{b-1}+1,&j=b,\\
-a_{T+1},&j=b+T+1,\\
0,&\text{other }j>b.
\end{cases}
\tag{5.7}
$$


These are congruences modulo $2^L$.

The high endpoint in (5.7) contributes nothing to the paired observation, because $\widehat F_j\equiv0$ for every $j>b$.

This identifies the exact role of the auxiliary value $\widehat z_b^k=-1$: it produces the required $+1$ in the reconstructed observation at $b$, while the physical value remains $z_b^k=0$.

### 5.3 Offset tails are exactly exterior observations

Let $\gamma_\kappa^Q,\gamma_\kappa^E$ be the integral kernel coefficients obtained from


$$
\widehat F_j^2,\qquad \widehat F_j\widehat G_j,
$$


using the atom formulas and (3.8).

For each individual kernel, its offset tail is exactly its finite contribution from $j\ge b$. This is just (2.7) rewritten with


$$
j=b+\varepsilon_1-k.
$$


Therefore linearity gives


$$
\sum_\kappa\gamma_\kappa^Q\mathcal T_{{\rm off},\kappa}
=
\sum_{j\ge b}W_j^2\widehat F_j^2,
$$




$$
\sum_\kappa\gamma_\kappa^E\mathcal T_{{\rm off},\kappa}
=
\sum_{j\ge b}W_j^2\widehat F_j\widehat G_j.
\tag{5.8}
$$


These are finite sums: the profile vectors are polynomials, and $W_j=0$ for $j>n+2$.

Substituting (5.6)–(5.7) proves the new cancellation.

### Theorem 5.1 — Complete boundary-channel cancellation

For the complete first-force and complete source/type-$2$ assembly at raw precision $2^L$,


$$
\boxed{
\sum_\kappa\gamma_\kappa^Q\mathcal T_{{\rm off},\kappa}
\equiv
b^2W_b^2(z^f_{b-1})^2
\pmod{2^L},
}
\tag{5.9}
$$


and


$$
\boxed{
\sum_\kappa\gamma_\kappa^E\mathcal T_{{\rm off},\kappa}
\equiv
W_b^2\,bz^f_{b-1}(bz^k_{b-1}+1)
\pmod{2^L}.
}
\tag{5.10}
$$



This is not a statement that individual tails vanish. It is an identity for the complete, source-dependent assembly.

Let $\operatorname{Acc}_L(\kappa)$ denote the corrected terminating acceptance, including $\binom{n+2}{d}$, but before tail subtraction. Equations (1.2)–(1.3), (2.8), and (5.9)–(5.10) now give


$$
\boxed{
\mathcal U\equiv\sum_\kappa\gamma_\kappa^Q
\operatorname{Acc}_L(\kappa),\qquad
\mathcal V\equiv\sum_\kappa\gamma_\kappa^E
\operatorname{Acc}_L(\kappa)
\pmod{2^L}.
}
\tag{5.11}
$$



The offset tails and physical terminal have been **proved to cancel after assembly**. They have not been silently omitted.

### What this annihilates

The entire exterior boundary observation


$$
-\sum_\kappa\gamma_\kappa^\bullet\mathcal T_{{\rm off},\kappa}
+\tau_\bullet
$$


is zero for the actual completed assembly, for both channels. Corrected Cartier transitions preserve this zero observation.

This does not assert that the corresponding polynomial state is identically zero. It is cancellation in the observation, and it leaves the interior source-dependent observation unresolved.

---

## 6. An integral common observation module

The new boundary cancellation removes the need to retain a separate tail/terminal output channel for the completed pair.

There is also a useful exact consolidation of the at-most-$32$ classes.

After $t_0$ shifts, let the surviving tuples be indexed by $\tau$. Each varying entry has spread at most one. Define


$$
\bar N_i=\min_\tau N_{i,\tau},\qquad
\bar M=\max_\tau M_\tau,\qquad
\bar B=\max_\tau B_\tau.
$$


For either output channel, replace its class polynomials by


$$
\boxed{
\bar P=
\sum_\tau
t^{\bar B-B_\tau}P_\tau
\prod_{i=1}^4(1+v_i)^{N_{i,\tau}-\bar N_i}
(1-t)^{\bar M-M_\tau}.
}
\tag{6.1}
$$


All exponents introduced here are $0$ or $1$; $N_2$ is already common.

Direct multiplication proves


$$
\sum_\tau\mathcal A(P_\tau;\mathbf N_\tau,M_\tau,B_\tau)
=
\mathcal A(\bar P;\bar{\mathbf N},\bar M,\bar B).
\tag{6.2}
$$


No division is involved.

Thus the actual raw pair has one common tuple and two coefficient polynomials:


$$
\boxed{
\mathcal U\equiv\mathcal A(\bar P_Q),\qquad
\mathcal V\equiv\mathcal A(\bar P_E)\pmod{2^L}.
}
\tag{6.3}
$$



The bounded-degree multipliers preserve polynomial support. From the safe box in §3, one obtains, for example,


$$
0\le\deg_t\bar P\le3J+3,
$$




$$
-J\le x\le J+2,\qquad
-J-1\le y\le J+2.
$$


Hence a safe common-module support bound is


$$
\boxed{(3J+4)(2J+3)(2J+4).}
\tag{6.4}
$$



This is a genuine integral consolidation, but not a computation of the full observable quotient.

---

## 7. Explicit annihilators and a concrete remaining lemma

A named unevaluated pairing would not advance the remaining obligation. The following operators instead give explicit, checkable sufficient certificates for zero acceptance.

Fix the common tuple and write


$$
\mathscr R=
\frac{(1+X)^{N_1}(1+t/X)^{N_2}
(1+tY)^{N_3}(1+1/Y)^{N_4}}
{(1-t)^M}.
$$


Let


$$
D_X=X\partial_X,\qquad D_Y=Y\partial_Y,\qquad D_t=t\partial_t.
$$



### 7.1 Integral constant-term annihilators

Define


$$
\begin{aligned}
\mathscr D_X(H)
={}&(1+X)(1+t/X)D_XH\\
&+H\left((N_1+1)X(1+t/X)
-(N_2+1)(t/X)(1+X)\right),
\end{aligned}
\tag{7.1}
$$


and


$$
\begin{aligned}
\mathscr D_Y(H)
={}&(1+tY)(1+1/Y)D_YH\\
&+H\left((N_3+1)tY(1+1/Y)
-(N_4+1)(1/Y)(1+tY)\right).
\end{aligned}
\tag{7.2}
$$


Then


$$
\mathscr D_X(H)\mathscr R
=
D_X\!\left(H(1+X)(1+t/X)\mathscr R\right),
$$


and similarly for $Y$. Since the constant term of a Laurent derivative $D_XF$ or $D_YF$ is zero,


$$
\boxed{\mathcal A(\mathscr D_XH)=\mathcal A(\mathscr D_YH)=0.}
\tag{7.3}
$$



For the target coefficient, put


$$
F=(1+t/X)(1+tY)(1-t).
$$


Define


$$
\begin{aligned}
\mathscr D_t(H)
={}&F(D_t-B_{\rm tar})H\\
&+H\bigl(
(N_2+1)(t/X)(1+tY)(1-t)\\
&\hspace{17mm}
+(N_3+1)tY(1+t/X)(1-t)\\
&\hspace{17mm}
+(M-1)t(1+t/X)(1+tY)
\bigr).
\end{aligned}
\tag{7.4}
$$


Product differentiation gives


$$
\mathscr D_t(H)\mathscr R
=
(D_t-B_{\rm tar})(HF\mathscr R).
$$


Because


$$
[t^{B_{\rm tar}}](D_t-B_{\rm tar})G=0,
$$


we also have


$$
\boxed{\mathcal A(\mathscr D_tH)=0.}
\tag{7.5}
$$



These statements hold integrally and modulo every $2^L$. There is no factorial division or nonunit pivot.

### 7.2 What is, and is not, now known about the quotient

The proved submodule


$$
\operatorname{im}\mathscr D_X+
\operatorname{im}\mathscr D_Y+
\operatorname{im}\mathscr D_t
$$


lies in the acceptance kernel. It is not proved to be the entire kernel.

The actual relative law still requires a source-dependent membership statement. For an integral candidate $r$, the source normalization gives


$$
E-rQ
=
2^{-2a-3}(2^a\mathcal V-2r\mathcal U).
\tag{7.6}
$$


Under the conventional nonnegative-content case $a\ge0$, a sufficient certificate at primitive depth $K$ is therefore


$$
\boxed{
2^a\bar P_E-2r\bar P_Q
\equiv
\mathscr D_XH_X+\mathscr D_YH_Y+\mathscr D_tH_t
\pmod{2^{K+2a+3}}.
}
\tag{7.7}
$$


All initial data and transitions in (7.7) must be formed at that raw precision.

If nonnegativity of $a$ has not independently been established, one should instead use the always-integral common scaling


$$
c=\max(2a+2,a+3)
$$


and the numerator


$$
2^{c-a-3}\mathcal V-r\,2^{c-2a-2}\mathcal U,
$$


evaluated modulo $2^{K+c}$. This avoids inserting an unproved integrality hypothesis into a relative certificate.

### Concrete follow-on lemma

A substantive next target is:

> On an explicitly specified infinite original subdomain, with the actual content $a$ certified or bounded at the required depth, derive $r(u)$ and bounded-support Laurent polynomials $H_X,H_Y,H_t$ satisfying (7.7), using the actual $\eta_f,\theta$ and the corrected original parameter word.

A successful certificate would be an explicit polynomial identity over the paid residue ring, rather than a renamed long sum. A bounded-support search can test a proposed certificate, but failure in a chosen support box would not disprove the relative law.

### Precise obstruction to claiming a relative law now

The completion identities control the exterior support and prove the boundary cancellation. They do not relate the two interior functions


$$
\widehat F_j^2,\qquad \widehat F_j\widehat G_j
\quad(0\le j<b).
$$


No membership of the actual relative polynomial in the explicit annihilator has been derived. No nonzero acceptance residue of $\bar P_E$ on an infinite original subdomain has been proved either.

That is the remaining local mathematical obligation. The seven finite kernel checks do not address it.

---

## 8. Paid arithmetic and true primitive depth

Every corrected Cartier transition is integral modulo $2^L$. The new additional whole-combination clearing loss is therefore


$$
\boxed{e_{\rm sum}=0.}
\tag{8.1}
$$



This does not erase local exact divisions. For example, evaluating


$$
2^r\binom hr\pmod{2^L}
$$


by a falling-factorial computation requires the appropriate parameter precision, such as


$$
h\pmod{2^{L-r+v_2(r!)}}.
$$


Likewise, computing $\binom{n+2}{d}\pmod{2^L}$ by that method requires


$$
n+2\pmod{2^{L+v_2(d!)}}.
$$


The repaired factor $(1-t)^s$ introduces no new division. The previously paid source-coefficient requirements remain compulsory.

For primitive output modulo $2^K$, retain


$$
\boxed{L_Q=K+2a+2,\qquad L_E=K+a+3.}
\tag{8.2}
$$


The entire raw result must be obtained before the corresponding whole division in (1.1).

The boundary cancellation is valid at these depths whenever the evaluator’s scope hypotheses hold: first prove it modulo the appropriate raw modulus, then perform the same whole primitive division. There is no separate, unpaid division of a tail or terminal term.

No constant value of $a$ is assumed. Accordingly, no original-size primitive calculation is proposed.

### Logarithmic guard

The logarithmic source remains


$$
\mathcal L_s=s![z^s]\frac{F(z)}{1-z},
$$


with the retained guard


$$
\boxed{B_*=n-v_2(b!)-1-2s_2(n)-\ell.}
\tag{8.3}
$$


The parameter $\ell$ and the logarithmic normalization are those of the original bound. Omitting the logarithmic contribution is justified only where that bound protects the requested normalized observation after all divisions.

The exponential boundary cancellation does not extend that guard. Outside the protected range the complete original logarithmic contribution must be included.

---

## 9. Actual clearer, all-prime gcd, primitive denominator, and whole error

The producer normalization remains


$$
\omega_j=j!W_j,\qquad
u_j=\frac{2\Lambda R\,x_j}{\omega_j},
\qquad
v_j=\frac{4b!\,y_j}{\omega_j}.
$$


Its actual least simultaneous clearer is


$$
\boxed{
d_B=
\operatorname{lcm}_{0\le j\le b}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\}.
}
\tag{9.1}
$$


No reconstructed row content is divided out.

Let


$$
\mathcal N=x^Tx,\qquad \mathcal H=x^Ty.
$$


Then


$$
A_B=d_B^2\,4\Lambda^2R^2\mathcal N,
\qquad
H_B=d_B^2\,8\Lambda Rb!\mathcal H,
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
\tag{9.2}
$$


This is the **all-prime** final gcd.

For every prime $p$,


$$
v_p(q_n)=
\max\{v_p(\mathscr D_n)+v_p(\mathcal N)-v_p(\mathcal H),0\},
\qquad
\mathscr D_n=\frac{\Lambda R}{2b!}.
\tag{9.3}
$$


The previously established ternary law is retained at its stated original-family scope:


$$
v_3(q_n)=n-\frac{b+15}{2}.
$$


It is not recalculated here.

Finally,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


and the whole evaluated error remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{9.4}
$$



An irrationality proof through this producer would require, on the **same infinitely many original indices**, a nonzero whole error and a favorable estimate involving the actual $q_n$. For example,


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0
$$


would contradict rationality: if $e+\pi=A/C$, every nonzero value on the left is at least $1/C$.

Neither a nonzero exponential pairing nor the boundary-channel cancellation supplies that whole-error theorem.

---

## 10. Optional bounded audit of the new cancellation

No new computation is needed for the proofs above, and none was performed.

The following optional audit tests the new exterior-support and assembled-tail identities. It does **not** repeat a direct-kernel/Cartier comparison, a Schur identity audit, or the old loss computation.

### Mathematical inputs

Use the auxiliary finite model


$$
b=2,\qquad n=8004,\qquad L=3,
$$


so


$$
I=1,\qquad m=8,\qquad T=5,\qquad V=13.
$$


Use a symbolic contact force


$$
\mathfrak f=(F_0,F_1)
$$


over


$$
(\mathbb Z/8\mathbb Z)[F_0,F_1],
$$


and the complete factorial prefix


$$
s=\sum_{t=0}^{5}\frac{(2+t)!}{2!}e_{2+t}.
$$



Form the finite completed coefficient data and the accepted type-$2$ formulas. Evaluate their extensions only through degree


$$
b+V+m+1=24.
$$


Thus all polynomial vectors have at most $25$ positions. The Schur matrix has size $2$; the short binomial and symbol indices are bounded by $24$. There is no force coefficient of order $n$ to compute because the force is symbolic.

This finite model is an auxiliary test of the universal boundary lemma, not an original index.

### Expected verifiable outputs

The calculation should output:

1. The exterior coefficients
   

$$
\widehat F_j=0\quad(j>2),
   \qquad
   \widehat F_2=2z^f_1.
$$



2. The complete source endpoint
   

$$
\widehat G_2=2z^k_1+1,
$$


   together with the retained high endpoint from (5.7).

3. The two zero polynomial differences
   

$$
\sum_{j\ge2}W_j^2\widehat F_j^2
   -4W_2^2(z^f_1)^2=0,
$$


   

$$
\sum_{j\ge2}W_j^2\widehat F_j\widehat G_j
   -2W_2^2z^f_1(2z^k_1+1)=0
$$


   modulo $8$.

4. Nontrivial terminal residues, not merely zero tails. Here
   

$$
W_2=\binom{8006}{2}\equiv7\pmod8,\qquad W_2^2\equiv1\pmod8.
$$


   Also $A\equiv P\pmod2$, so
   

$$
z^f_1\equiv F_0+F_1\pmod2.
$$


   Consequently the norm exterior observation must be
   

$$
\boxed{4(F_0^2+F_1^2)\pmod8,}
$$


   and the exponential exterior observation must reduce modulo $4$ to
   

$$
\boxed{2(F_0+F_1)\pmod4.}
$$



The pairwise kernel list need not be emitted: distributivity permits the finite exterior observations to be formed from the reconstructed polynomial vectors. This keeps the audit bounded by the stated $25$-position model.

Passing it would establish only this auxiliary finite case. It would not establish (7.7), an actual content bound, an infinite-original digit, or a whole-error estimate.

---

## 11. Proof-status ledger

| Statement | Status |
|---|---|
| Turn 2 denominator identity | **False; explicitly corrected** |
| Parent’s repaired denominator multiplier | **Proved independently here** |
| Exact individual kernel coefficient identity and finite tail | **Proved at the stated hypotheses** |
| Corrected Cartier acceptance with no additional whole-pair clearing loss | **Proved** |
| Cubic single-state support | **Proved** |
| At most $32$ tuples | **Proved** |
| Union support bound for arbitrary actual initial offsets | **Proved without identifying support centers** |
| Complete source, finite returns, and both differential boundaries | Retained |
| Complete assembled tail equals physical terminal | **Newly proved modulo the paid raw modulus** |
| Both exponential terminal terms included in that cancellation | **Proved** |
| One common integral observation module | **Proved** |
| Explicit integral differential annihilators | **Proved sufficient certificates** |
| Full acceptance-kernel characterization | Open |
| Actual relative-polynomial membership in that annihilator | Open |
| New infinite-original nonzero $E$ digit or nontrivial $E-r(u)Q$ law | Not obtained |
| Actual content bound enabling a production primitive run | Not obtained |
| Same-index all-prime denominator and nonzero whole-error comparison | Unresolved |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The corrected evaluator is valid with the repaired factor $(1-t)^s$. Its polynomial support and merging claims survive an independent audit, provided support unions are bounded in absolute coordinates and initial assembly cost is retained.

The principal new mathematical result is


$$
\boxed{
\text{complete assembled offset-tail subtraction}
+
\text{complete physical terminal}
=0
\pmod{2^L}.
}
$$


For the exponential response, the proof retains the full source prefix, all finite returns, and both physical terminal terms. It is valid before any primitive division.

The remaining local bottleneck is now more specific: determine the observation of the actual tail-free, common-tuple polynomials at true primitive depth. The explicit identities (7.1)–(7.7) provide a concrete division-free route to a relative-law certificate, but the required source-dependent certificate has not been found.

After that local problem, the actual least clearer, all-prime gcd, primitive denominator, and nonzero whole error still must be controlled on the same infinitely many original indices.

**The boundary-channel cancellation is a new proved reduction. It is not an unconditional proof of either rationality or irrationality of $e+\pi$.**
