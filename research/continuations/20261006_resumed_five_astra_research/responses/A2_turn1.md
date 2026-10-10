> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 1 — A two-observable reduction of the actual truncated kernels modulo $29$

## Executive assessment

The scalar-kernel problem can be advanced substantially at its first digit without replacing the finite cutoff or assuming that the base-$29$ expansion of $b$ is periodic.

The new results are:

1. **A four-state finite-digit evaluator for every individual kernel modulo $29$.**  
   After converting the negative upper binomials with their support conditions intact, three subtraction borrows suffice. Although three bits allow eight formal states, at most **four states are reachable at any digit**. Lucas’s no-carry condition eliminates the need to retain addition-carry states.

2. **A target-specific reduction of the entire $K=1$ kernel table to two high-index scalar observables.**  
   For the actual parameter box
   

$$
0\le a,a'\le124,\qquad -124\le v,v'\le125,\qquad 0\le t\le250,
$$


   the following hold modulo $29$:
   - every kernel containing $A=0$ is zero;
   - every kernel containing $A=-2n-a$ is zero;
   - every kernel with both upper parameters of the form $-a,-a'$, with $a,a'>0$, is zero;
   - every remaining kernel is an explicitly computable low-digit coefficient times **one of two common tail scalars**.

   Each low-digit coefficient requires at most **168 terms**, not an original-length sum.

3. **A two-state digit evaluator for those two common tail scalars.**  
   Both can be evaluated together using two borrow states and four accumulated residues. The remaining input is still approximately $81$ million base-$29$ digits at $u=0$; this is not an exponent-length algorithm.

4. **A complete, but only absolute-precision-one, output cancellation theorem.**  
   On the retained orbit, the reconstructed contact inverse annihilates modulo $29$ every input supported in its first $124$ coordinates. Consequently the complete source-plus-end defect vanishes modulo $29$ for the actual first force, with the complete second force and exterior coordinate retained. This is an operator statement, not a deletion of the source. It does **not** reach the true normalized norm digit.

These results provide a much smaller observable quotient than the previous atom count. They do not evaluate the two tail scalars at the original $u=0$, do not establish a prime-power lift of this quotient, and do not resolve the irrationality of $e+\pi$.

No executable tools were used. The small modular values below are derived explicitly; the proposed implementation checks have not been run.

---

## 1. Scope audit and retained dependencies

I reuse the finite atom identities, the finite contact inverse, the complete source subtraction, the actual squared-weight reconstruction, and the memory theorem at their proved scopes.

The aggregate bounds


$$
V\le32,\qquad D_K=256K+16,\qquad T_K\le100(29K+2)^4
$$


are now accepted with A4’s source-subtraction correction. They need not be reproved.

Three qualifications to the earlier atom report remain important.

### 1.1 An atom factorization is not a scalar evaluation

The factorization


$$
A^{-1}h=\sum_\alpha z_{h,\alpha}E_\alpha\pmod{29^K}
$$


does not evaluate a pairing until its scalar kernels have been evaluated or related. Nor is the full parameter box a practical storage prescription.

The reduction below avoids constructing the dense $K=1$ kernel table: all its values factor through two common tail observables.

### 1.2 Only $A=0$, not the whole $\sigma=0$ sector, is single-term

For $a>0$,


$$
\binom{-a}{k}=(-1)^k\binom{a+k-1}{a-1}
$$


usually has long support. Its small complementary lower index is useful modulo $29$, but does not make the sum single-term.

### 1.3 The original finite domains remain unchanged

Throughout,


$$
b=3^{249005515+574312172u},\qquad n=2001b,\qquad u\ge0.
$$


Contact coordinates remain $0,\ldots,b-1$, recurrence rows remain $1,\ldots,b-2$, and reconstruction retains the separate coordinate $b$.

The kernels are


$$
S_t(A,v;A',v')
=
\sum_{j=0}^{b-1}
\binom{n+2}{j}^{2}\binom jt
\binom A{b+v-j}\binom{A'}{b+v'-j}.
\tag{1.1}
$$



No completed final block will replace this range.

---

## 2. Negative upper binomials: support and signs first

Put $p=29$ and $N=n+2$.

Suppose


$$
A=-\alpha,\qquad A'=-\alpha',\qquad \alpha,\alpha'\ge1,
$$


and define


$$
B=b+v,\qquad B'=b+v',\qquad
D=\alpha-1,\qquad D'=\alpha'-1.
$$



For $k\ge0$,


$$
\binom{-\alpha}{k}=(-1)^k\binom{D+k}{D};
$$


for $k<0$, the original binomial is zero.

Thus, if $B,B'\ge0$, setting


$$
J=\min(b-1,B,B')
$$


gives the exact identity


$$
\boxed{
S_t(-\alpha,v;-\alpha',v')
=
(-1)^{v+v'}
\sum_{j=0}^{J}
\binom Nj^2\binom jt
\binom{D+B-j}{D}
\binom{D'+B'-j}{D'}.
}
\tag{2.1}
$$


If $J<0$, the sum is zero.

The sign is independent of $j$, because


$$
(B-j)+(B'-j)=2b+v+v'-2j.
$$



There is no replacement of a negative lower index by a reflected positive binomial.

### The $A=0$ sector

If $A=0$, only $j=B$ can contribute. For $\alpha'\ge1$,


$$
\boxed{
\begin{aligned}
S_t(0,v;-\alpha',v')
={}&
\mathbf1_{\,0\le B<b}\,
\mathbf1_{\,v'\ge v}\,
\binom NB^2\binom Bt\\
&\times(-1)^{v'-v}
\binom{\alpha'+v'-v-1}{v'-v}.
\end{aligned}
}
\tag{2.2}
$$


If both upper parameters are zero, an additional condition $v=v'$ is required.

These are exact finite-boundary formulas.

---

## 3. A four-state digit evaluator for an individual kernel

This construction applies to (2.1) for arbitrary admissible nonnegative parameters. It is not restricted to the special low digits used later.

### 3.1 Reusable Lucas rule

For nonnegative $x,y$, Lucas’s theorem gives


$$
\binom xy\equiv\prod_i\binom{x_i}{y_i}\pmod p.
$$



In particular,


$$
\binom{D+k}{D}\not\equiv0\pmod p
$$


only if the addition $D+k$ is carry-free.

Here is the useful algorithmic form. Starting with zero incoming addition carry, if at some digit


$$
D_i+k_i\ge p,
$$


the contribution is zero modulo $p$. At the first such carry, the upper digit is


$$
D_i+k_i-p<D_i,
$$


so its Lucas factor vanishes.

Consequently, for a nonzero contribution, addition carries never arise. They need not be stored.

### 3.2 State and transition

Read digits from least significant to most significant.

The state is


$$
\varepsilon=(\varepsilon_J,\varepsilon_B,\varepsilon_{B'})
\in\{0,1\}^3,
$$


the incoming borrows in


$$
J-j,\qquad B-j,\qquad B'-j.
$$



At digit $i$, choose $d=j_i\in\{0,\ldots,28\}$. Reject immediately unless


$$
t_i\le d\le N_i.
$$



For $C\in\{J,B,B'\}$, form


$$
x_C=C_i-d-\varepsilon_C,
$$




$$
z_C=x_C+29\,\mathbf1_{x_C<0},\qquad
\varepsilon_C^{+}=\mathbf1_{x_C<0}.
$$



Thus $z_B,z_{B'}$ are the current digits of $B-j,B'-j$.

Reject the transition if


$$
D_i+z_B\ge29
\quad\text{or}\quad
D_i'+z_{B'}\ge29.
\tag{3.1}
$$



Otherwise multiply its accumulated weight by


$$
\boxed{
\binom{N_i}{d}^{2}
\binom d{t_i}
\binom{D_i+z_B}{D_i}
\binom{D_i'+z_{B'}}{D_i'}.
}
\tag{3.2}
$$



Initialize the zero-borrow state with weight $1$, all others with weight $0$.

Read


$$
L=\max\{\ell_{29}(N),\ell_{29}(J),\ell_{29}(B),
\ell_{29}(B'),\ell_{29}(D),\ell_{29}(D'),\ell_{29}(t)\}
$$


digits, padding the input constants with zeros.

### Terminal acceptance

Accept exactly


$$
\boxed{\varepsilon_J=\varepsilon_B=\varepsilon_{B'}=0.}
\tag{3.3}
$$


Multiply the accepted sum by $(-1)^{v+v'}$.

The final borrow tests enforce $j\le J,B,B'$. The Lucas factor $\binom jt$ enforces the required lower support. No further recurrence or reconstruction coordinate is introduced.

### 3.3 Why only four states are reachable

After $h$ digits, write $m=29^h$ and $r=j\bmod m$. For each constant $C$,


$$
\varepsilon_C=\mathbf1_{\,r>C\bmod m}.
\tag{3.4}
$$



Thus all three borrows are comparisons of the **same** $r$ with three thresholds. As $r$ increases, the borrow vector changes only when one of those thresholds is crossed.

There are therefore at most


$$
\boxed{4}
$$


distinct reachable borrow vectors at any layer, and fewer if thresholds coincide.

This is a genuine state bound derived from the transition geometry. It does not assign one state to each summand or coefficient.

### 3.4 Cost and correctness

A direct implementation needs:

- a table of the $29\times29$ digit binomials;
- at most four live residue accumulators;
- at most $4\cdot29$ candidate transitions per input digit.

The proof of correctness is termwise: each accepted digit path represents exactly one $0\le j\le J$, and its weight is precisely the Lucas reduction of the corresponding summand in (2.1).

This already supplies an actual finite-digit evaluator. The next sections reduce the target much further.

---

## 4. The actual four-digit phase

The first four base-$29$ digits are fixed throughout the original orbit.

Let


$$
M=29^4=707281,\qquad \beta=687936.
$$


Then


$$
\boxed{
b\equiv\beta\pmod M,\qquad
\beta=(27,28,5,28)_{29}.
}
\tag{4.1}
$$


Consequently,


$$
\boxed{
n+2\equiv191112=(2,7,24,7)_{29}\pmod M.
}
\tag{4.2}
$$



### A small exact certificate

The exponent satisfies


$$
249005515+574312172u\equiv432827\pmod{28\cdot29^3}.
$$


Also


$$
3^{28}\equiv694261
=1+15\cdot29+13\cdot29^2+28\cdot29^3
\pmod{29^4}.
$$


Since


$$
432827=3+28\cdot15458,
$$


a binomial expansion through the cubic term gives


$$
(3^{28})^{15458}\equiv418413\pmod{29^4},
$$


and


$$
27\cdot418413\equiv687936\pmod{29^4}.
$$



Finally,


$$
2001\cdot687936
=1946\cdot707281+191110,
$$


which proves (4.2).

These congruences use the actual exponent class. They do not assert anything about a long digit period.

---

## 5. Three exact eliminations in the $K=1$ kernel box

For this section retain exactly the sufficient $K=1$ box from the atom reduction:


$$
0\le a,a'\le124,\qquad
-124\le v,v'\le125,\qquad
0\le t\le250.
\tag{5.1}
$$



The larger upper bound $125$ for $v,v'$ includes the reconstruction shift.

### 5.1 Every $A=0$ kernel vanishes

A possible single term has


$$
j=b+v<b,
$$


so $-124\le v\le-1$. Since


$$
b\bmod841=839,
$$


its low two-digit residue lies in


$$
715\le j\bmod841\le838.
$$



But


$$
N\bmod841=205=(2,7)_{29}.
$$


If $\binom Nj\not\equiv0\pmod{29}$, Lucas requires


$$
j\bmod841=29q+d,\qquad 0\le q\le7,\quad0\le d\le2,
$$


hence $j\bmod841\le205$.

Therefore the single term is zero:



$$
\boxed{
S_t(0,v;A',v')=0\pmod{29}
}
\tag{5.2}
$$


throughout the box. The symmetric statement also holds.

This proof explicitly uses the actual finite boundary $j<b$.

---

### 5.2 Every $\sigma=2$ factor is annihilated pointwise by the weight

Consider


$$
\binom Nj\binom{-2n-a}{b+v-j},
\qquad 0\le a\le124,\quad -124\le v\le125.
$$



If $b+v-j<0$, it is zero by support. Otherwise let


$$
k=b+v-j,\qquad D=2n+a-1.
$$



Suppose the weight is nonzero modulo $29$. Write the four low digits of $j$ as $j_0,j_1,j_2,j_3$. Then


$$
j_0\le2,\qquad j_1\le7,\qquad j_2\le24,\qquad j_3\le7.
\tag{5.3}
$$



The low two-digit part of $D$ is $405+a<841$, and its next two digits are


$$
D_2=19,\qquad D_3=15.
\tag{5.4}
$$



At the third digit of the subtraction $b+v-j$, the effective minuend digit, after its incoming borrow, is either $5$ or $6$. Indeed:

- if $v\le1$, the low two-digit part of $b+v$ is at least $715>205$, so there is no incoming borrow and the third digit is $5$;
- if $v\ge2$, the third digit is $6$, and the incoming borrow is $0$ or $1$.

If subtraction borrowed at this third digit, then


$$
k_2\ge29+5-24=10.
$$


But carry-free addition to $D_2=19$ requires $k_2\le9$. Hence every potentially nonzero term has no outgoing borrow at this digit.

At the fourth digit we therefore have


$$
k_3=28-j_3\ge21.
$$


Adding $D_3=15$ necessarily creates a carry. The negative binomial is zero modulo $29$.

Thus


$$
\boxed{
\binom Nj\binom{-2n-a}{b+v-j}\equiv0\pmod{29}
}
\tag{5.5}
$$


for every actual $j<b$.

It follows immediately that


$$
\boxed{
S_t(-2n-a,v;A',v')\equiv0\pmod{29}.
}
\tag{5.6}
$$



This is pointwise annihilation, stronger than cancellation of a sum.

---

### 5.3 The positive-$a$, $\sigma=0$ sector is totally isotropic

Now take $a,a'>0$. Put


$$
Q=\left\lfloor\frac b{841}\right\rfloor,\qquad
X=\left\lfloor\frac N{841}\right\rfloor.
$$



For a nonzero weight, write


$$
j=841q+r,\qquad
r=29d_1+d_0,\quad
0\le d_1\le7,\quad0\le d_0\le2.
$$



Because $r\le205$, while the low two-digit part of


$$
J=b+\min(-1,v,v')
$$


is at least $715$, the finite condition $j\le J$ is exactly


$$
0\le q\le Q
$$


for all such low residues.

Since $a-1,a'-1,t<841$, every factor other than the high part of the squared weight depends only on $r$. Therefore


$$
S_t(-a,v;-a',v')
=
\lambda\,F(X,Q)\pmod{29},
\tag{5.7}
$$


for an explicitly finite low-digit coefficient $\lambda$, where


$$
F(X,Q)=\sum_{q=0}^{Q}\binom Xq^2.
$$



The actual low digits are


$$
Q_0=5,\qquad X_0=24,
$$


and, one digit higher,


$$
\left\lfloor Q/29\right\rfloor_0=28,\qquad
\left\lfloor X/29\right\rfloor_0=7.
$$



Splitting the finite prefix by its last digit gives


$$
\begin{aligned}
F(X,Q)\equiv{}&
\left(\sum_{d=0}^{28}\binom{24}{d}^2\right)
F\!\left(\lfloor X/29\rfloor,\lfloor Q/29\rfloor-1\right)\\
&+
\left(\sum_{d=0}^{5}\binom{24}{d}^2\right)
\binom{\lfloor X/29\rfloor}{\lfloor Q/29\rfloor}^{2}.
\end{aligned}
\tag{5.8}
$$



The first coefficient is


$$
\binom{48}{24}\equiv0\pmod{29}.
$$


The second boundary binomial is zero by its low digits $7<28$. In fact the displayed partial sum is $9$, but its value is not needed for the vanishing.

Hence


$$
\boxed{
S_t(-a,v;-a',v')\equiv0\pmod{29}.
}
\tag{5.9}
$$



This is a cancellation theorem for the complete finite prefix, not a statement that the summands vanish individually.

---

## 6. The entire remaining table factors through two scalars

After Section 5, every potentially nonzero kernel has parameters $\sigma,\sigma'\in\{0,1\}$, with at least one equal to $1$. If $\sigma=0$, its $a$ must be positive.

Define the exact high parameters


$$
\boxed{
B_*=\frac{b-\beta}{M},\qquad
N_*=\frac{N-191112}{M}=2001B_*+1946.
}
\tag{6.1}
$$



The affine constant $1946$ is essential. It must not be dropped when passing to the high digits.

For $m=1,2$, define


$$
\boxed{
T_m=
\sum_{q=0}^{B_*}
\binom{N_*}{q}^{2}
\binom{N_*+B_*-q}{B_*-q}^{m}
\pmod{29}.
}
\tag{6.2}
$$



These are the only two high-index scalar observables needed for the whole $K=1$ kernel table.

### 6.1 The forced low-digit support of a $\sigma=1$ factor

For


$$
D=n+a-1,\qquad 0\le a\le124,
$$


the relevant digits are


$$
D_2=24,\qquad D_3=7.
$$



The same subtraction analysis as in Section 5.2 shows that a nonzero contribution cannot borrow at digit $2$: a borrow would give $k_2\ge10$, whereas carry-free addition to $24$ requires $k_2\le4$.

At digit $3$,


$$
k_3=28-j_3.
$$


Since $j_3\le7$, carry-free addition to $D_3=7$ forces


$$
\boxed{j_3=7.}
\tag{6.3}
$$



Also $j_2\le6$. Therefore the low four-digit residue of every potentially nonzero summand belongs to


$$
\boxed{
\mathcal L=
\left\{
7\cdot29^3+e\,29^2+q\,29+d:
0\le e\le6,\ 0\le q\le7,\ 0\le d\le2
\right\}.
}
\tag{6.4}
$$


This set has $7\cdot8\cdot3=168$ elements.

Every $s\in\mathcal L$ satisfies


$$
s\le175974<\beta-124.
\tag{6.5}
$$


Thus all subtractions $b+v-j$, $b+v'-j$, and the actual cutoff comparison have **zero borrow into digit $4$**.

This is the reason the high-digit states merge.

### 6.2 Explicit low coefficients

For a surviving sector, set


$$
d_\sigma=
\begin{cases}
a-1,&\sigma=0,\\
191109+a,&\sigma=1,
\end{cases}
$$


and similarly $d_{\sigma'}'$.

Define


$$
\boxed{
\begin{aligned}
\lambda_t(\sigma,a,v;\sigma',a',v')
={}&(-1)^{v+v'}
\sum_{s\in\mathcal L}
\binom{191112}{s}^{2}
\binom{s\bmod841}{t}\\
&\times
\binom{d_\sigma+\beta+v-s}{d_\sigma}
\binom{d_{\sigma'}'+\beta+v'-s}{d_{\sigma'}'}
\pmod{29}.
\end{aligned}
}
\tag{6.6}
$$



All quantities in this formula are bounded integers. They are evaluated by ordinary digit binomials; no nonunit division is performed.

If a low addition has a carry, its binomial factor is zero. Thus a nonzero low coefficient contribution has no carry into the high part.

### Theorem 6.1 — Two-observable kernel quotient

Within (5.1), every surviving kernel satisfies


$$
\boxed{
S_t(-\sigma n-a,v;-\sigma'n-a',v')
=
\lambda_t(\sigma,a,v;\sigma',a',v')\,T_{\sigma+\sigma'}
\pmod{29}.
}
\tag{6.7}
$$



Together with (5.2), (5.6), and (5.9), this determines the entire $K=1$ scalar table from $T_1,T_2$.

#### Proof

Write


$$
j=Mq+s,\qquad s\in\mathcal L.
$$



By (6.5), the original finite condition $j\le b-1$, and both negative-binomial support conditions, become exactly


$$
0\le q\le B_*.
$$


In particular, $q=B_*$ is allowed because the forced low residue lies strictly below the actual endpoint. No extra high block is added.

Lucas gives


$$
\binom Nj^2
=
\binom{191112}{s}^2\binom{N_*}{q}^2\pmod{29}.
$$


Because $t<841$,


$$
\binom jt=\binom{s\bmod841}{t}\pmod{29}.
$$



For a $\sigma=0$ factor, the complementary lower index has no high digits, so its high Lucas factor is $1$.

For a $\sigma=1$ factor, the high complementary lower index is $N_*$, and the high part of $b+v-j$ is $B_*-q$. Its high factor is


$$
\binom{N_*+B_*-q}{N_*}.
$$



All low factors are precisely those in (6.6). Summing over $s$ and then $q$ proves (6.7). ∎

### What this quotient means

It is a scalar observable quotient of the modular kernel table. It is **not** an integer row reduction, a saturation theorem, or permission to remove rows from the actual Gram pair.

---

## 7. A two-state evaluator for $T_1,T_2$

The tails (6.2) have an especially small digit realization.

At each digit, retain one borrow


$$
\varepsilon\in\{0,1\}
$$


for $B_*-q$. Maintain two residue arrays, one for each $m=1,2$.

At digit $i$, choose $d=q_i$ with


$$
0\le d\le (N_*)_i.
$$


Form


$$
x=(B_*)_i-d-\varepsilon,\qquad
k=x+29\,\mathbf1_{x<0},\qquad
\varepsilon^+=\mathbf1_{x<0}.
$$



Reject if


$$
(N_*)_i+k\ge29.
$$


Otherwise the two transition weights are


$$
\boxed{
w_m=
\binom{(N_*)_i}{d}^{2}
\binom{(N_*)_i+k}{k}^{m},
\qquad m=1,2.
}
\tag{7.1}
$$



Initialize each channel in borrow state $0$ with value $1$. After all digits of $N_*,B_*$, accept only borrow $0$.

This is a complete evaluation algorithm for both actual tails modulo $29$.

### Reachable size and operation count

The joint evaluator uses:

- two borrow states;
- four accumulated residues;
- at most $58$ candidate edges per digit, shared by the two channels;
- two channel updates per accepted edge.

No coefficient-sized state space is present.

### The input is still long

At $u=0$,


$$
\ell_{29}(b)=
1+\left\lfloor249005515\log_{29}3\right\rfloor,
$$


approximately $81.24$ million digits.

By contrast, the exponent $249005515$ has only six base-$29$ digits, or $28$ binary bits.

The theorem removes almost the entire **observable-table dimension**. It does not replace the approximately $81$-million-digit scan by a six-digit scan.

A worst-case direct joint implementation still examines about


$$
58\,\ell_{29}(b)\approx4.7\times10^9
$$


candidate edges. That is a meaningful, explicit workload, but not a claim of a cheap original-index computation. Obtaining the actual digit stream is an additional task.

No short period of the base-$29$ expansion has been assumed or proved.

---

## 8. Consequence for the complete source-plus-end combination

The actual columns remain


$$
\theta=A^{-1}f^0,\qquad \psi=A^{-1}\mathbf r,
$$




$$
Z_w=\mathcal R\theta,\qquad
Y=\mathcal R\psi+W_be_b.
$$



The first force remains


$$
f_i^0=\frac{(n+i)!}{n!}
[t^n](1+2t+2t^2)^n(1+t)^i.
\tag{8.1}
$$



The complete second force remains


$$
\mathbf r=r_0h^{(0)}+r_1h^{(1)}+\tau,
$$


with


$$
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}\right),
\qquad i=0,1,
\tag{8.2}
$$


and complete source


$$
\mathcal H_i=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b},
\qquad1\le i\le b-2.
\tag{8.3}
$$


The definitions of $T_m,L_m$, including factorial subtraction and the logarithmic contribution, are unchanged.

### 8.1 A universal short-head annihilation theorem

Modulo $29$, the accepted finite inverse simplifies to


$$
A^{-1}\equiv \mathsf R^{\,2}\mathsf P_-.
\tag{8.4}
$$


Here the divided-power factor is the identity and the complete endpoint update is zero modulo $29$. This is a proved specialization of the actual finite inverse, not an omitted endpoint correction at higher precision.

Finite triangular convolution gives


$$
(\mathsf R^2)_{jk}=\binom{-2n}{k-j}.
$$


For a head input $h$ supported in $0\le i<L$, the finite head formula therefore expresses $A^{-1}h$ using atoms


$$
E(-2n-t-1,b-1-t;i-t),\qquad0\le t\le i<L.
\tag{8.5}
$$



If $L\le124$, every such atom lies in the $\sigma=2$ range proved in Section 5.2. The reconstruction identity


$$
jE(A,b+v;r)_{j-1}-E(A,b+v;r)_j
=
(r+1)E(A,b+v+1;r+1)_j-E(A,b+v;r)_j
$$


keeps both terms in that range.

Also


$$
W_b=\binom{n+2}{b}\equiv0\pmod{29},
$$


because its low digits are $2<27$.

Hence:



$$
\boxed{
\mathcal RA^{-1}h\equiv0\pmod{29}
\quad\text{for every head input of length }L\le124.
}
\tag{8.6}
$$



The terminal reconstruction row is included in this statement.

### 8.2 Complete cancellation, not source deletion

The actual $f^0$ has head length at most $29$ modulo $29$. Thus (8.6) implies, for every integral complete second input,


$$
\mathcal N\equiv0,\qquad \mathcal C\equiv0\pmod{29}.
$$



Equivalently, the complete expression


$$
\begin{aligned}
&(r_0-29\rho_nf_0^0)\mathcal Q(f^0,h^{(0)})
+(r_1-29\rho_nf_1^0)\mathcal Q(f^0,h^{(1)})\\
&\qquad+\mathcal Q(f^0,\tau)
+bW_b^2(A^{-1}f^0)_{b-1}
\end{aligned}
\tag{8.7}
$$


is zero modulo $29$.

Every source row and both initial charges remain present. The conclusion follows from annihilation of the complete first output functional, not from assuming that an interior source impulse is invisible.

### Exact limitation

For the actual columns, stronger common divisibility was already retained in the sources. Therefore (8.7) is **not a new norm-relative digit**.

Its new content is the explicit short-head output annihilator and the two-observable description of the surrounding scalar kernel table.

---

## 9. Higher precision: what must be lifted

The two-observable theorem is presently proved only modulo $29$, on the displayed $K=1$ offset box.

It cannot be promoted to modulo $29^K$ by replacing the digit binomials with arbitrary residues:

- binomials with one or more carries are no longer automatically zero;
- their unit parts depend on additional digit information;
- low/high interfaces can carry nontrivial states;
- the actual source, endpoint solve, and atom coefficients must all be retained at the working precision.

### 9.1 A concrete next lemma

The next useful target is:

> **Carry-budget lift of the two-observable quotient.**  
> Construct, first modulo $29^2$, a boundary-compatible digit realization for the complete weighted contraction in which the carry valuations and binomial unit parts are retained, and determine whether the two-observable quotient acquires only finitely many explicitly described correction channels.

For one kernel summand the exact valuation budget is


$$
2e_W+e_t+e_A+e_{A'},
\tag{9.1}
$$


where these are the valuations of its four binomial factors, with the weight counted twice.

Modulo $29^2$, a surviving term must have


$$
e_W=0,\qquad e_t+e_A+e_{A'}\le1.
\tag{9.2}
$$


This is a concrete starting restriction. It does not by itself evaluate the unit parts or their weighted sum.

Classical prime-power binomial evaluation and Lucas generalizations are reused background. No detailed theorem hidden in uninspected HTML images is needed as a premise here.

### 9.2 Nonunit factorial guards

For nonnegative $x\ge y$, one may always separate


$$
e=v_{29}(x!)-v_{29}(y!)-v_{29}((x-y)!)
$$


and use


$$
\binom xy
=
29^e
\frac{U(x)}{U(y)U(x-y)},
\qquad
U(m)=\frac{m!}{29^{v_{29}(m!)}}.
\tag{9.3}
$$


Only unit parts are inverted.

For the small-index arithmetic in the atom construction, retain the earlier sufficient guard


$$
v_{29}\bigl((3R_*+3)!\bigr),\qquad R_*=120K+4.
\tag{9.4}
$$


The digit identities above do not license division by $r!$, $t!$, or a norm factor modulo $29^K$.

### 9.3 True-norm and logarithmic guards remain

Let


$$
d=v_{29}(\mathcal N)=2c+4+\nu,
\qquad
\nu=v_{29}(x^Tx)
$$


in the retained primitive-vector notation.

The actual local target is still


$$
\boxed{
\mathcal C-29\rho_n\mathcal N\equiv0\pmod{29^{d+2}}.
}
\tag{9.5}
$$



The independent $\rho_n$ must be supplied independently of the mixed/norm ratio.

Logarithmic omission still requires


$$
\boxed{
N_{\log}\ge c+4+\nu,
}
\tag{9.6}
$$


where


$$
N_{\log}
=
2v_{29}(n!)-v_{29}(b!)
-\lfloor\log_{29}(2n+b-1)\rfloor.
$$


Until this is certified, (8.2) must retain the complete logarithmic initial values.

---

## 10. New bounded controls

These controls concern the new digit transitions and observable quotient. They do not rerun the accepted contact-inverse, memory, or aggregate-bound computations.

### 10.1 Full-kernel control on the four-digit phase

Use


$$
\boxed{
b=687936,\qquad n=2001b=1376559936.
}
\tag{10.1}
$$


This is an auxiliary input, not an original power $3^a$.

It has the required four-digit phase and $B_*=0$, so


$$
T_1=T_2=1.
$$



For each selected kernel, compare:

1. direct enumeration of exactly $0\le j<b$, using Lucas on each supported summand;
2. the four-state digit evaluator of Section 3;
3. the two-observable formula where applicable.

Useful exact expected residues are


$$
\begin{array}{c|c}
\text{kernel}&\text{residue modulo }29\\ \hline
S_0(-1,-1;-1,-1)&0\\
S_0(0,-1;-n,2)&0\\
S_0(-2n,2;-n,2)&0\\
S_0(-n,2;-n,2)&24\\
S_0(-1,-1;-n,2)&10.
\end{array}
\tag{10.2}
$$



The last two values are nonzero controls, so an implementation returning zero everywhere will fail.

For transparency, the surviving $-n,2$ factor restricts the low digits to $j_0=0$, $j_1=0$ or $7$, $j_3=7$. Its third-digit coefficients are


$$
(1,-4,6,-4,1),
$$


and


$$
\binom{24}{d}^2\bmod29
=(1,25,22,7,28,13,20),\qquad0\le d\le6.
$$


The two squared contributions are $7$ and $17$, giving $24$. The mixed contributions sum to $130-120=10$ modulo $29$.

These are hand-derived finite identities, not reported execution results.

### 10.2 Tail-transition controls

For


$$
B_*\in\{0,1,28,29,30\},\qquad N_*=2001B_*+1946,
$$


compare direct summation of (6.2) with the joint two-state evaluator.

The expected pairs are


$$
\boxed{
\begin{array}{c|cc}
B_*&T_1&T_2\\ \hline
0&1&1\\
1&13&25\\
28&28&1\\
29&4&7\\
30&21&0.
\end{array}
}
\tag{10.3}
$$



The largest direct tail sum here has only $31$ terms. These controls test borrow transitions, a terminal boundary, nonzero outputs, and cancellation in one channel but not the other.

Required output is equality of the independently assembled residues, together with the terminal borrow state and the maximum number of live states observed.

No original-index value of $T_1,T_2$ is predicted.

---

## 11. Primitive arithmetic and the whole error are unchanged

The modular observable quotient does not alter any original row content or either corrected column.

Retain the least actual two-column clearer $d_B$, the complete weighted integer Gram pair


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


and the all-prime final reduction


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
}
\tag{11.1}
$$


The primitive multiplier remains $d_B^2/g_B$.

With the retained local notation,


$$
v_{29}(q_n)
=
\max\{0,\,2F_n-F_b-1+\delta-\mu\}.
\tag{11.2}
$$


The actual denominator still requires


$$
\boxed{
\log q_n
=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{11.3}
$$



For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the relevant evaluated form is the whole same-index expression


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{11.4}
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



Nothing proved here supplies the all-prime denominator bound needed to make this whole nonzero form tend to zero.

---

## Proof-status ledger

| Statement | Status |
|---|---|
| A4’s corrected aggregate representation bounds | Reused; not reproved |
| Negative-binomial support and constant pair sign | Proved explicitly |
| Four-state evaluator for an individual truncated kernel modulo $29$ | Proved |
| Actual four-digit phase of $b,n+2$ | Certified by small exact arithmetic |
| $A=0$ sector, with the finite boundary retained | Proved zero modulo $29$ in the stated box |
| Every $\sigma=2$ weighted atom | Proved pointwise zero modulo $29$ in the stated box |
| $\sigma=0$–$\sigma=0$ kernel sector | Proved zero by complete finite-prefix cancellation |
| Entire $K=1$ kernel table factors through $T_1,T_2$ | Proved |
| Low coefficients require at most $168$ terms | Proved |
| Joint two-state evaluator for $T_1,T_2$ | Proved |
| Original $u=0$ values of $T_1,T_2$ | Not computed |
| Short-head reconstructed-output annihilation modulo $29$ | Proved, including the terminal row |
| Complete defect modulo $29$ | Proved; not a new norm-relative digit |
| Prime-power lift of the two-observable quotient | Open |
| Alignment at $v_{29}(\mathcal N)+2$ | Open |
| Final all-prime denominator/whole-error comparison | Open |
| Irrationality of $e+\pi$ | Unresolved |

## Conclusion

The outstanding scalar problem is no longer merely represented by a polynomial-sized atom table.

At its first digit, the actual finite kernel table has a proved **two-observable quotient**:


$$
\boxed{
S_t(-\sigma n-a,v;-\sigma'n-a',v')
\in
\{0,\ \lambda T_1,\ \lambda T_2\}\pmod{29},
}
$$


with explicit low coefficients of at most $168$ terms and exact retention of $j\le b-1$.

The two remaining tail scalars have an actual two-state digit evaluator. This is a genuine compression of the observable calculation, but not a compression of the original digit stream to the length of its exponent.

The next local bottleneck is precise: lift this quotient, or a comparably small boundary-compatible realization, through the carry valuations and unit-factor corrections needed to reach the **actual** norm-sensitive precision. The complete forcing, endpoint return, logarithmic protection, and independent $\rho_n$ must accompany that lift.

The new bounded controls in Section 10 are small enough for personal implementation and test the new constructions rather than already accepted computations.

Even a successful norm-relative $29$-adic law would leave the all-prime final gcd, actual primitive denominator, and whole same-index error to be controlled. Therefore:



$$
\boxed{\text{An unconditional proof or disproof of the irrationality of }e+\pi
\text{ remains unresolved.}}
$$


