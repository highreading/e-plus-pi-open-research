> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — partial second-depth evaluation on the true MAIN29 norm-zero locus

**Status.** I do not obtain the complete second-depth zero classification for $0\le d\le24$. In particular, I do **not** establish an actual proportional-unit relation for $M_1$, or prove


$$
D_1=0\Longrightarrow M_1=0
$$


on that part of the original domain.

There are, however, two new evaluations:

1. On $0\le d\le24,\ T=0$, the second normalized **norm** digit reduces to two explicitly defined, finite-boundary residual quantities:
   

$$
\boxed{D_1=C_n^2\bigl(f(d)T_1+\beta(d)U\bigr)\pmod{29}.}
$$


   The coefficient $\beta(d)$ is given below by an explicit sum of at most four terms involving only factorials and harmonic numbers with indices at most $28$.

2. On $25\le d\le28$, normalization of the actual $P$-column gives a stronger result than the scalar lower bound alone:
   

$$
\boxed{\frac{M}{29}\equiv0\pmod{29}.}
$$


   Thus $\mu\ge2$ there. This follows from a support calculation for the newly normalized column, not from subtracting scalar valuation bounds. Its next norm coefficient is also evaluated:
   

$$
\boxed{\frac{D}{29^2}\equiv
   C_n^2\bigl(\rho_0(d)R_0+\rho_1(d)R_1\bigr)\pmod{29},}
$$


   with the numerical coefficient table
   

$$
\begin{array}{c|rrrr}
   d&25&26&27&28\\ \hline
   \rho_0(d)&11&14&14&2\\
   \rho_1(d)&18&10&10&18.
   \end{array}
$$



The unresolved mixed digit on $d\le24,\ T=0$ includes newly admitted support and a genuine endpoint contribution. I evaluate that endpoint contribution explicitly below, without identifying it with the whole mixed discrepancy.

---

## 1. Domain, corrected metric, and notation

Throughout,


$$
p=29,\qquad b=3^a,\qquad n=2001b,\qquad m_w=1,
$$




$$
a\ge1,\qquad a\equiv432827\pmod{682892}.
$$


The column indices are $0\le j\le b$; every contact inverse retains the finite index range $0\le i,j<b$.

The actual metric is **falling**:


$$
\boxed{\omega_j=j!\binom{n+2}{j}=(n+2)_{\underline j}},
\qquad
\Omega=\operatorname{diag}(\omega_j^2).
$$


There is no rising product in the argument.

Use the actual reconstructed coordinates


$$
W_j=\binom{n+2}{j},\qquad
\widehat P=\frac{Z_w}{p^2},\qquad
\widehat Q=\frac{Y}{p^3},\qquad Y=\frac{V_w}{b!},
$$


and write


$$
D=\widehat P^T\widehat P,\qquad M=\widehat P^T\widehat Q.
$$



Retain


$$
L=p^4,\qquad b=687936+Lh,\qquad h=pH+d,\quad 0\le d<p,
$$




$$
N=2001h+1946=3+pA,\qquad A=69h+67.
$$


Here $h,H,d,A$ are determined by the original power $3^a$.

Define the **integer**, not merely residual, sum


$$
\mathcal T(A,H)=
\sum_{k=0}^{H}X_k^2,\qquad
X_k=\binom Ak\binom{2A+H-k}{H-k}.
\tag{1.1}
$$


Thus the established $T$ is $\mathcal T\bmod p$. On $T=0$, set


$$
T_1=\frac{\mathcal T}{p}\pmod p,\qquad
U=\sum_{k=0}^{H}kX_k^2\pmod p.
\tag{1.2}
$$


Every sum retains its displayed finite boundary.

I reuse the established first-depth result


$$
D\bmod p=C_n^2f(d)T,
$$


with $f(d)\ne0$ for $0\le d\le24$, and the established first-depth mixed zero alignment. I do not rederive the first carry or $K_{01}=0$.

---

## 2. Precision audit: one extra digit, complete boundary, and full log force

For the present scalar digit, $Z_w\bmod p^4$ and $Y\bmod p^5$ suffice. The bounded construction can safely be run **one precision higher**:



$$
Z_w\bmod p^5,\qquad Y\bmod p^6.
$$



Let


$$
d_s=s![z^s](1-z+z^2/2)^n,\qquad
F_r=\frac{(b+r)!}{b!}.
$$


The retained valuation bound gives


$$
v_p(d_s)\ge1+v_p((s-1)!).
$$


Consequently:

* for $P\bmod p^5$, retain $s\le116$ and the forcing indices $0\le i\le144$;
* for $Q\bmod p^6$, retain $s\le145$;
* because $b+2=p^2K$, $K\equiv6\pmod p$, the complete factorial tail for $Q\bmod p^6$ is
  

$$
\boxed{0\le r\le117.}
$$



In particular, the blocks


$$
60\le r\le88,\qquad89\le r\le117
$$


are retained at this audit precision.

Using the signed-Newton operators already established in the supplied archive, the inverse polynomials can be formed as


$$
h_P=(I-\mathscr V+\mathscr V^2-\mathscr V^3+\mathscr V^4)g_P
\pmod{p^5},
$$


and, after the complete exterior boundary has been combined into $a_Q$,


$$
h_Q=(I-\mathscr V+\mathscr V^2-\mathscr V^3+\mathscr V^4)a_Q
\pmod{p^6}.
$$


The graded bounds give effective Newton degree at most $144$ in both cases. The complete $Q$-boundary has coefficients


$$
c_s=\sum_{r=s}^{117}F_r\binom{2n}{r-s},\qquad0\le s\le117.
\tag{2.1}
$$


Thus the reconstructed positive support is at most $145$, and the complete negative boundary support extends to $-118$.

The full logarithmic contribution is absent at these precisions only because its **whole-force** bound gives


$$
v_p(h_i^F/b!)
\ge F_n-F_b-\lfloor\log_p(2n+b-1)\rfloor\ge6.
\tag{2.2}
$$


For example,


$$
F_n\ge69b,\qquad F_b\le b/28,\qquad
\lfloor\log_{29}(4003b-1)\rfloor\le b
$$


already makes (2.2) more than sufficient on the assigned domain.

The endpoint remains


$$
Z_{w,b}=W_b\,b\theta^P_{b-1},\qquad
Y_b=W_b(1+b\theta^Q_{b-1}).
\tag{2.3}
$$


The $1$ in the second expression is never deleted.

---

## 3. A new support refinement needed for the second digit

Put


$$
B_q(j)=\binom{2n+b-j-1}{b-j-q}.
$$


The reconstruction remains


$$
\mathscr R\!\left(\sum_q a_q(j)r^q\right)_j
=(-1)^{j+1}W_j\sum_q a_q(j)B_q(j).
\tag{3.1}
$$



Let $\mathcal X$ denote the established four-digit support of the leading $P$-column: the low indices $x\in[0,687936]$ for which the $\tau=0$ binomial product has exactly two low-block carries. Write


$$
j=LJ+x,\qquad
e(x)=\mathbf1_{x>191112}.
$$


On $\mathcal X$, the established leading factorization is


$$
\widehat P_{LJ+x}\equiv
(-1)^{j+1}C_n\,c(x)\ell_{e(x)}(J)F(J)\pmod p,
\tag{3.2}
$$


where


$$
F(J)=\binom NJ\binom{2N+h-J}{h-J},
$$




$$
\ell_0(J)=2N+h-J+1,\qquad
\ell_1(J)=N-J,
\tag{3.3}
$$


and


$$
\sum_{x\in\mathcal X,\ e(x)=0}c(x)^2=11,\qquad
\sum_{x\in\mathcal X,\ e(x)=1}c(x)^2=18.
\tag{3.4}
$$



### Lemma 3.1 — the first corrected positive kernel creates no new two-carry low support

For $0\le q\le58$, a nonzero residue


$$
p^{-2}W_jB_q(j)\pmod p
$$


is supported on $x\in\mathcal X$. Its remaining high factorial ratio is the same


$$
\ell_{e(x)}(J)F(J).
\tag{3.5}
$$



#### Proof

Write $q=pq_1+q_0$, $0\le q_0<p$, so $q_1\le2$.

The two compulsory carry positions $1,3$ are retained. Hence two-carry support requires $j_0\le2$, since otherwise the weight itself has an additional digit-zero borrow.

If $q_0=0$, the second binomial has the additional digit-zero carry already used for $B_0$, so two-carry support is impossible.

For $q_0>0$, absence of that additional carry requires


$$
q_0+j_0\le27.
$$


At digit one, a borrow caused by


$$
j_1+q_1>28
$$


would produce a second carry there in addition to the weight borrow. Thus it too is excluded on two-carry support.

Under these two restrictions, the changes $+q_1$ and $-q_1$ in the two digit-one addends cancel without a borrow. All subsequent carry states agree with those of the $\tau=0$ product. Thus $x\in\mathcal X$.

There is also no borrow through the entire four-digit block in $b-j-q$. Such a borrow would add a second final carry to the one already compulsory at digit three, giving at least three carries. Separating the first four factorial levels therefore leaves exactly (3.5). ∎

This lemma is only a statement about the indicated support and precision. It is not an all-depth extension of the coarse carry lemma.

---

## 4. Evaluation of $D_1$ on $0\le d\le24,\ T=0$

On this domain, the supplied first-depth result gives $p\mid D,M$. Define


$$
D_1=D/p\bmod p,\qquad M_1=M/p\bmod p.
$$



### 4.1 Why the first corrected $P$-kernel drops out here

Write the actual bounded $P$-kernel as


$$
\mathcal P=\mathcal P_0+p\mathcal P_1+O(p^2),
\qquad
\mathcal P_0=C_n(r+1-h_0(j)),
$$


where $\mathcal P_1$ has positive Laurent support at most $58$.

By Lemma 3.1, the leading reconstructed contribution of $\mathcal P_1$, wherever it can pair with the leading $P$-column, has the same high factor (3.5). Its contraction therefore reduces modulo $p$ to a low-digit multiplier times $T$. It vanishes on the presently assigned locus $T=0$.

The $h_0B_0$ correction in $\mathcal P_0$ is handled similarly: its extra low factor is already present, and its leading high ratio on the old support is again (3.5).

The remaining first-order variation of the four-digit factorial units also contributes only a multiple of $T$. To see this without truncating higher indices, use


$$
(pm+r)!_{\text{\(p\)-free}}
\equiv ((p-1)!)^m r!\bigl(1+pmH_r\bigr)\pmod{p^2}.
$$


At each of the first four levels, the first-order unit correction depends only on the next quotient modulo $p$. After four levels, its dependence on $J$ is therefore only through $J\bmod p$. The fifth section then leaves a scalar multiple of $\sum X_k^2=T$.

It follows that, on $T=0$,


$$
D_1\equiv
C_n^2\,\frac1p
\sum_{J=0}^{h}
\bigl(11\ell_0(J)^2+18\ell_1(J)^2\bigr)F(J)^2
\pmod p.
\tag{4.1}
$$


The displayed division is exact because the sum is zero modulo $p$.

### 4.2 Fifth-digit expansion with its actual boundary

Put


$$
B_v=\binom{v+6}{6}\pmod p\quad(0\le v\le22),
$$


and let $H_s=\sum_{i=1}^s1/i\in\mathbb F_p$, with $H_0=0$.

Only


$$
J=pk+t,\qquad0\le t\le3,\qquad v=d-t\in[0,22]
\tag{4.2}
$$


can contribute to (4.1) modulo $p^2$. All other $F(J)$ are divisible by $p$, so their squares vanish at this precision.

For every admissible $t$, the actual remaining range is exactly $0\le k\le H$. The standard one-step binomial expansion gives


$$
F(pk+t)
\equiv
\binom3t B_vX_k
\left(1+p(E_t+k\,r_t)\right)\pmod{p^2},
\tag{4.3}
$$


where the $k$-independent $E_t$ is irrelevant on $T=0$, and


$$
r_t=H_{3-t}-H_t+H_v-H_{v+6}.
\tag{4.4}
$$


Also


$$
\ell_0(pk+t)=v+7+p(2A+H-k),
$$




$$
\ell_1(pk+t)=3-t+p(A-k).
\tag{4.5}
$$



Substituting (4.3)–(4.5) into (4.1) yields the evaluated formula


$$
\boxed{
D_1=C_n^2\bigl(f(d)T_1+\beta(d)U\bigr)\pmod p,
}
\tag{4.6}
$$


where


$$
\boxed{
\begin{aligned}
\beta(d)=2
\sum_{\substack{0\le t\le3\\0\le d-t\le22}}
\binom3t^2B_{d-t}^2
\Big[
&\bigl(11(d-t+7)^2+18(3-t)^2\bigr)\\
&\quad{}\times
\bigl(H_{3-t}-H_t+H_{d-t}-H_{d-t+6}\bigr)\\
&-11(d-t+7)-18(3-t)
\Big].
\end{aligned}}
\tag{4.7}
$$


This is an explicit fixed-coefficient formula, not a ghost-path prescription. It contains at most four terms.

For checks,


$$
\boxed{\beta(0)=17,\quad\beta(1)=25,\quad
\beta(23)=4,\quad\beta(24)=12.}
\tag{4.8}
$$



### Consequence for the second norm-zero condition

Since $C_n$ and $f(d)$ are units for $d\le24$,


$$
\boxed{
D_1=0
\iff
T_1=-f(d)^{-1}\beta(d)U
\quad\text{in }\mathbb F_{29}.
}
\tag{4.9}
$$


Thus $T_1$ alone does not describe the second norm digit: a first moment $U$ of the residual squared-binomial distribution appears.

If every $X_k$ is divisible by $p$, then $T_1=U=0$. This is the shifted-common-content case inside $T=0$, distinct from a nonzero isotropic residual vector.

---

## 5. The four column-zero classes: normalize the column first

Now assume $25\le d\le28$, and define the actual normalized column


$$
P^\sharp=\widehat P/p=Z_w/p^3.
$$


The supplied result already makes this integral.

### 5.1 Its leading support and the next mixed coefficient

For every $J\in[0,h]$,


$$
\ell_0(J)F(J)\equiv\ell_1(J)F(J)\equiv0\pmod p.
\tag{5.1}
$$



Indeed, for $d\ge26$, a nonzero $F(J)\bmod p$ is impossible: the first low binomial requires $t\le3$, while the second requires $d-t\le22$. For $d=25$, the sole possible choice is $t=3$, and then both linear factors vanish.

Lemma 3.1 and (5.1) show that the first corrected $P$-kernel contributes zero to $Z_w/p^3\bmod p$.

For the base term, low indices with three low carries have a high ratio


$$
F(J)(N-J)^e(2N+h-J+1)^u,\qquad e+u\ge1.
$$


This also vanishes by (5.1). Indices $x>687936$ have at least four low carries in the $\tau=0$ product; their contribution vanishes at this precision. One can see the extra two carries at the final low-block position directly: the subtraction $b-j$ borrows through the block, while the weight also borrows there; the lower positions supply the remaining two.

The $B_0$ term similarly vanishes after division by $p^3$. Consequently,


$$
\boxed{
P^\sharp_{LJ+x}\equiv
(-1)^{j+1}C_n c(x)
\frac{\ell_{e(x)}(J)F(J)}p\pmod p
\quad(x\in\mathcal X),
}
\tag{5.2}
$$


and $P^\sharp\equiv0$ outside this low-block support.

On $\mathcal X$, the supplied complete first $Q$-digit has the factor $\ell_e(J)F(J)$. Hence (5.1) gives


$$
\widehat Q_{LJ+x}=0\pmod p\qquad(x\in\mathcal X).
\tag{5.3}
$$


Combining (5.2) and (5.3),


$$
\boxed{
\frac Mp=(P^\sharp)^T\widehat Q\equiv0\pmod p.
}
\tag{5.4}
$$



Thus


$$
\boxed{25\le d\le28:\qquad \delta\ge2,\quad\mu\ge2.}
\tag{5.5}
$$


The mixed bound has now been proved by the actual column support; it was not inferred from $\delta\ge2$.

### 5.2 Evaluated next norm coefficient

Define


$$
R_0=\sum_{k=0}^{H}(2A+H-k+1)^2X_k^2\pmod p,
$$




$$
R_1=\sum_{k=0}^{H}(A-k)^2X_k^2\pmod p.
\tag{5.6}
$$



A one-carry fifth-digit separation of (5.2) gives


$$
\boxed{
\frac D{p^2}
\equiv C_n^2\bigl(\rho_0(d)R_0+\rho_1(d)R_1\bigr)\pmod p,
}
\tag{5.7}
$$


with


$$
\boxed{
\begin{array}{c|rrrr}
d&25&26&27&28\\ \hline
\rho_0(d)&11&14&14&2\\
\rho_1(d)&18&10&10&18.
\end{array}}
\tag{5.8}
$$



Here is the finite coefficient calculation behind the table.

For $23\le v\le28$, put


$$
K_v=-\frac{(v-23)!}{6v!};
\qquad
(K_{23},\ldots,K_{28})=(9,4,27,2,25,20).
$$


For $4\le t\le28$, put


$$
C_t=\frac{6(-1)^{t-4}(t-4)!}{t!}.
$$


Then


$$
\begin{aligned}
\rho_0(d)
={}&11\mathbf1_{d=25}\\
&+\sum_{\substack{0\le t\le3\\23\le d-t\le28}}
\binom3t^2K_{d-t}^2
\bigl(11(d-t+7)^2+18(3-t)^2\bigr),
\end{aligned}
\tag{5.9}
$$


and


$$
\begin{aligned}
\rho_1(d)
={}&18\mathbf1_{d=25}\\
&+\sum_{t=\max(4,d-22)}^{d}
C_t^2B_{d-t}^2
\bigl(11(d-t+7)^2+18(3-t)^2\bigr).
\end{aligned}
\tag{5.10}
$$



For $d=25$, the parenthesized expression is identically zero modulo $29$; only the exceptional no-carry term $t=3$, where both $\ell_e$ supply the factor $p$, remains.

For $d=26,27,28$, respectively,


$$
C_tB_{d-t}
=\pm22(t+1)(t+2),\quad
\pm22(t+1)(t-4),\quad
\pm22(t-4)(t-5).
$$


After squaring, the finite sums can be completed to all of $\mathbb F_{29}$. The resulting polynomials have degree below $28$, so their complete sums vanish. Subtracting the omitted terms $t=0,1,2,3$ gives the second row of (5.8). No infinite summation or omitted terminal term is used.

---

## 6. What is still missing for $M_1$ on $d\le24,\ T=0$

Equation (4.6) does **not** determine $M_1$.

At this depth,


$$
M_1
$$


contains both:

* the lift of the old-support mixed contraction;
* the product of the newly admitted $P$-digit with the leading $Q$-digit outside the old $P$-support.

The latter is not a norm correction. The argument that removes the first corrected $P$-kernel from $D_1$ does not remove these mixed terms.

Nor has the supplied first-depth theorem evaluated the two mixed low constants sufficiently to justify a proportional-unit relation away from its zero locus. Therefore I cannot presently replace $M_1$ by


$$
(6C_n)^{-1}D_1.
$$



If that particular unit is tested, the exact outstanding scalar is


$$
\boxed{
M_1-\frac{C_n}{6}
\bigl(f(d)T_1+\beta(d)U\bigr).
}
\tag{6.1}
$$


Its vanishing is **not** proved here.

### An evaluated boundary term in the missing scalar

The endpoint already contributes at this new mixed depth, although it contributed zero to $D\bmod p$ and contributes zero to $D_1$.

The low factorial-unit calculation gives


$$
\boxed{
W_b/p^3\equiv5(N-h)\binom Nh\pmod p.
}
\tag{6.2}
$$


Also


$$
h_0(27)=16,\qquad1-h_0(27)=14,
$$


and the complete endpoint satisfies


$$
Y_b/W_b\equiv1\pmod p.
$$


Thus its contribution to $M_1$ is


$$
\boxed{
\left[\frac{M}{p}\right]_{\!j=b}
=
2C_n(N-h)^2\binom Nh^2\pmod p.
}
\tag{6.3}
$$


After the fifth digit,


$$
\boxed{
\left[\frac{M}{p}\right]_{\!j=b}
=C_n\,\eta(d)\binom AH^2,
\qquad
\eta(d)=
\begin{cases}
18,&d=0,2,\\
14,&d=1,\\
0,&3\le d\le28.
\end{cases}}
\tag{6.4}
$$



This is a contribution, **not** an evaluated whole discrepancy. Interior terms may cancel it. It identifies a concrete finite-boundary datum that a complete $M_1$ reduction must retain.

On $d=25,\ldots,28$, the next unresolved mixed coefficient is now $M/p^2\bmod p$. Computing it requires the next $Q$-coefficient on the shifted support in (5.2), together with the next $P$-coefficient paired against the old $Q$-column. The old support lemma alone does not decide it.

---

## 7. Actual primitive normalization, nonvanishing, and whole error

Retain the actual least two-column denominator $d_B$:


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0.
$$


With the corrected falling metric,


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B>0.
$$


The primitive multiplier on the actual integer coefficient pair is $1/g_B$. The reduced denominator is $q_n$, not $d_B$ or a row-clearer.

Put


$$
\delta=v_{29}(D),\qquad\mu=v_{29}(M).
$$


The retained exact arithmetic interface is


$$
\boxed{
v_{29}(g_B)=
\min\{4F_n+4+\delta,\ 2F_n+F_b+5+\mu\},
}
$$




$$
\boxed{
v_{29}(q_n)=
\max\{0,\ 2F_n-F_b-1+\delta-\mu\}.
}
$$


The norm is nonzero by positivity. Finiteness of the mixed valuation retains the supplied original-family nonvanishing dependency; it is not inferred from a finite residue.

At the supplied status of the complete signed-error theorem,


$$
\epsilon_n=p_n/q_n-(e+\pi)>0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$


The whole primitive evaluated form is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n<0
\quad\text{eventually}.
}
$$


All prime contributions remain in $q_n$. The complete exponential residual, factorial boundary, endpoint, and logarithmic force remain part of this real error.

No irrationality or rationality conclusion follows.

---

# Concluding ledger

## (1) New result and proof status

**Proved using the supplied bounded kernels and established first-depth support:**

* The support refinement in Lemma 3.1.
* On the original domain $0\le d\le24,\ T=0$,
  

$$
D_1=C_n^2\bigl(f(d)T_1+\beta(d)U\bigr),
$$


  with the explicit fixed coefficients (4.7).
* On $25\le d\le28$, after normalizing the actual column,
  

$$
M/p=0\pmod{29}.
$$


  Hence both $\delta,\mu\ge2$ there.
* The next norm coefficient on those four classes is (5.7), with the evaluated table (5.8).
* The actual endpoint contribution to $M_1$ is (6.4).

**Unresolved:** the whole $M_1$ on $d\le24,\ T=0$, its actual proportional-unit relation if any, and the implication $D_1=0\Rightarrow M_1=0$. No original-domain counterexample is established.

## (2) Exact remaining bottleneck

For $0\le d\le24$, evaluate the complete mixed lift on


$$
T=0,\qquad f(d)T_1+\beta(d)U=0,
$$


including newly admitted low support and the endpoint term (6.4). The unresolved quantity is the whole scalar (6.1), not an old-support norm multiplier.

For $25\le d\le28$, the next obligation has shifted to


$$
M/p^2\bmod29,
$$


to be compared with the evaluated norm (5.7). Neither common column content nor the two scalar lower bounds controls their subsequent difference.

## (3) Bounded exact computation request

A useful next computation is **the two leading mixed low-block constants**, not a growing-dimensional inverse.

Use the representative


$$
h=1,\quad b=687936+29^4=1395217,\quad n=2001b,
$$


only to evaluate the fixed low constants on $x\in\mathcal X$, with $J=0$. Use the complete bounded boundary


$$
\mathcal Q_0+p^2\mathcal T_2
$$


from turn18, reconstructed modulo $p^4$. On this support its first contact term contributes zero at that precision.

Here


$$
F(0)\equiv7,\qquad \ell_0(0)\equiv8,\qquad\ell_1(0)\equiv3,
$$


all units. Thus obtain $\xi(x)$ by exact division of the reconstructed $Y_x/p^3$ by its signed high factor, and return


$$
g_0=\sum_{x\in\mathcal X,\ e(x)=0}c(x)\xi(x),\qquad
g_1=\sum_{x\in\mathcal X,\ e(x)=1}c(x)\xi(x).
$$



**Expected verifiable output:** the two residues $g_0,g_1$, together with termwise divisibility receipts. In particular, test—but do not impose—the values


$$
g_0=26,\qquad g_1=3,
$$


which would give the candidate leading proportional unit $(6C_n)^{-1}$.

This bounded computation would fix the previously unevaluated mixed multiplier. It would **not** by itself prove second-depth alignment: the new-support and higher-coefficient contribution in (6.1) would still have to be evaluated.
