> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 6 — Original-phase third-order divisibility and an integral three-observable reduction

## Executive conclusion

Two substantive advances follow from the supplied material.

1. **The proposed $29^{-2}$ leading column vanishes on the entire original power phase, not only on the tested auxiliary phases.**  
   A six-digit carry argument proves
   

$$
29^3\mid
   \binom{n+2}{j}\binom{-2n-a}{b+v-j}
$$


   for each of the four pairs
   

$$
(a,v)=(1,0),(1,-1),(30,-29),(30,-30).
$$


   Combining this with the complete finite normal ordering gives, for the normalized homogeneous first-force input,
   

$$
\boxed{\mathcal RA^{-1}h\in29^3\mathbb Z_{29}^{\,b+1}.}
$$


   Consequently, in A2’s notation,
   

$$
\boxed{c\ge g+1.}
$$


   This is an original-phase theorem. It is stronger than the auxiliary zero-Gram computations, but it is still only a lower bound on output content. It supplies no upper bound on the primitive norm loss $\nu$.

2. **For the actual shortened binary input, the telescoping boundary is exactly zero, and exact saturation gives three integral observables.**  
   The new common summand has cutoff parameter $L=b$, not $b+176$. Its telescoping coefficient contains $(b-j)^2$, so its upper flux vanishes at $j=b$. The physical terminal coordinate is nevertheless retained in the contraction.

   Moreover, because the telescoping identities hold over the integers, their saturated relations also vanish under the actual integer-valued moment functional. A certified saturated Smith presentation therefore removes the pivot-product guard from the *subsequent observable evaluation*. Before any payload-specific improvement, sufficient pure-observable precisions become
   

$$
\boxed{180\text{ bits for the norm},\qquad177\text{ bits for the mixed form},}
$$


   rather than $341$ and $335$ bits. The physical input remains twenty-bit data.

   This is a proved bound and a concrete specification for the coordinator’s already planned **one new Smith/payload-image postprocessing**. It is not a completed moment evaluation.

I also find the supplied $n=3375$ recurrence producer, primitive-denominator normalization, and fixed-point enclosure method mathematically consistent at their stated finite scope. The five evaluated whole forms are all nonzero and have absolute value greater than one. No infinite-family conclusion follows.

I do not reopen the closed synchronization, exact-window no-overlap, normalized deep-family exclusion, or primary-text reachability results. No rerun of $225$, $3375$, the accepted endpoint solves, or the old operator/jet tests is proposed.

---

## 1. Scope and evidence

Three different arithmetic settings occur here and must not be conflated:

- the finite original $n=3375$, $d=2$ endpoint calculation;
- the original $29$-adic family
  

$$
b=3^{249005515+574312172u},\qquad n=2001b,\qquad u\ge0;
$$


- the fixed binary input
  

$$
b=150094635296999121,\qquad n=4002b
  =600678730458590482242.
$$



The proofs below transfer no finite numerical observation from one setting to another.

I have reviewed the supplied source code and receipts, but have not executed them or independently regenerated their large artifacts. Thus:

- identities derived below are mathematical proofs;
- the supplied numerical outputs are reviewed finite computation results;
- the proposed Smith output is not yet computed;
- no finite receipt is treated as an infinite theorem.

---

# Part I. Review of the complete $n=3375$ calculation

## 2. The integer coefficient recurrences have the correct normalization

Put


$$
\phi(z)=1-z+\frac{z^2}{2},
\qquad
E_m=m!\sum_{r=0}^{m}\frac1{r!}.
$$



Define


$$
m_k=[z^k]\phi(z)^n e^z,
\qquad
\omega_k=[z^k]\phi(z)^n
\sum_{t\ge0}E_{n+t}\frac{z^t}{t!}.
$$


The producer stores


$$
C_k=2^k k!m_k,\qquad W_k=2^k k!\omega_k.
$$



### 2.1 Moment recurrence

From


$$
\phi(z)(\phi^n e^z)'=(\phi+n\phi')\phi^n e^z
$$


one obtains


$$
C_{k+1}
=
2(k+1-n)C_k
+2k(2n-k-1)C_{k-1}
+4k(k-1)C_{k-2}.
$$



This is exactly the recurrence in `coefficient_states`.

The initial values are


$$
C_0=1,\qquad C_{-1}=C_{-2}=0.
$$


The conversion back to $m_k$ is therefore correct.

### 2.2 Complete exponential recurrence

Let


$$
\mathcal E_n(z)=\sum_{t\ge0}E_{n+t}\frac{z^t}{t!}.
$$


Since $E_{m+1}=(m+1)E_m+1$,


$$
(1-z)\mathcal E_n'=(n+1)\mathcal E_n+e^z.
$$


For $\mathcal W=\phi^n\mathcal E_n$, this gives


$$
(1-z)\phi\,\mathcal W'
=
\bigl(n(1-z)\phi'+(n+1)\phi\bigr)\mathcal W
+\phi^{n+1}e^z.
$$


Coefficient extraction, with the same $2^k k!$ normalization, yields


$$
\begin{aligned}
W_{k+1}={}&2(2k+1)W_k
+2k(2n+1-3k)W_{k-1}\\
&+4k(k-1)(k-n-1)W_{k-2}
+2C_k-4kC_{k-1}+4k(k-1)C_{k-2}.
\end{aligned}
$$


Again, this is the implemented recurrence.

Thus the new integer producer is not a truncated-exponential approximation. It generates the exact complete exponential coefficients needed for the three original rows.

### 2.3 Logarithmic-force normalization

The separate non-recurrence input is the full logarithmic companion identity, used at precisely the three required indices:


$$
\widehat w_i
=
\widehat w_i^{\,e}
+
4n!\bigl(\rho_n v_i+\rho_{n+1}w_i\bigr),
\qquad i=0,1,2,
$$


where


$$
(v_0,v_1,v_2)
=
\left(1,\frac12,\frac{n+1}{2(n+2)}\right),
$$




$$
(w_0,w_1,w_2)
=
\left(0,\frac12,\frac{2n+3}{2(n+2)}\right).
$$



The producer uses this identity with the same normalization as the direct producer: the original row force is divided by $(n+i)!$. In particular, no factor $n!$, $(n+i)!$, or $4$ has been lost.

The direct $n=17$ test checks the complete force through index $36$, including three full logarithmic-force comparisons. That is useful independent finite corroboration. It is not, by itself, a proof of the companion identity for arbitrary $n$; the latter must be reused as the established identity at its stated three-row scope.

---

## 3. Reconstruction and primitive denominators

The source retains all four entries of both columns:


$$
u=(-s x_0,\;s x_0-s x_1,\;s x_1-s x_2,\;s x_2),
$$




$$
v=(1-s y_0,\;s y_0-s y_1,\;s y_1-s y_2,\;s y_2).
$$


Here $sx=Sx$, $sy=Sy$, with the displayed triangular $S$.

The exterior $+1$ occurs in $v_0$. It is not replaced by an asymptotic correction.

The least common clearer is taken across **all eight entries**:


$$
d_B=\operatorname{lcm}\{\operatorname{den}(u_j),\operatorname{den}(v_j):0\le j\le3\}.
$$


The row contents are then computed from the actual integer pairs


$$
(U_j,V_j)=d_B(u_j,v_j).
$$



The supplied contents are


$$
\boxed{(113940000,\;9780750,\;10125,\;1).}
$$


These are not common contents inferred from only the endpoint rows.

### 3.1 The two-cancellation large-prime identity

The use of


$$
C^\sharp=\gcd(X,R_0,R_1)
$$


rather than a single cancellation expression is justified.

At a prime $\ell>n+2$, both $L$ and


$$
\Omega=t_0r_1-t_1r_0
$$


are units. Hence the two reference rows form an invertible matrix over $\mathbb Z_\ell$. With


$$
M=\gamma X,\qquad V=\gamma Y+LE,
$$




$$
R_0=t_0V-r_0M,\qquad R_1=t_1V-r_1M,
$$


the pair $R_0,R_1$ detects the relevant common divisibility without requiring either $t_0$ or $t_1$ individually to be a unit.

If $\ell\mid\gamma$, primitivity of $(\gamma,E)$ makes $V$ a unit, so there is no cancellation in $\gcd(M,V)$. If $\ell\nmid\gamma$, invertibility gives the usual equality between the common divisibility measured by $X,V$ and by $X,R_0,R_1$. Thus


$$
d_{\mathrm{large}}
=
\frac{\gamma_{\mathrm{large}}X_{\mathrm{large}}}
     {C^\sharp_{\mathrm{large}}}
$$


has the stated scope.

The receipt reports


$$
\gamma_{\mathrm{large}}=C^\sharp_{\mathrm{large}}=1
$$


at both endpoints, and common defect $W=1$. This is a finite finding, not a theorem that such factors always vanish.

### 3.2 The final probe gcd is genuinely all-prime

The primitive probes do not stop after removing selected prime factors. For a reduced weight $a/k$, the code forms the exact numerator $T$, removes the displayed $F$- and $G$-factors, and then applies


$$
H=\gcd\!\left(h,\frac{|T|}{FG}\right).
$$


The final assertions check both


$$
\gcd(|p|,q)=1
$$


and equality with the original rational combination.

Thus these $q$'s are the actual primitive denominators of the five tested combinations.

The finite imbalance data are


$$
|AB|_{\le3377}
=
3^3\,5^4\,7\,19\,31
=
69\,575\,625.
$$


The selected $3/5$-part is only


$$
3^3 5^4=16875.
$$


The extra factors $7,19,31$, and the $50539$-digit complementary part, cannot be omitted from an actual denominator analysis.

---

## 4. The fixed-point enclosure proof is valid

Let $S=2^{120000}$.

### 4.1 Enclosure of $e$

The finite sum uses $\lfloor S/k!\rfloor$. Each included term loses less than one unit. Once $k!>S$, the remaining positive tail, scaled by $S$, is less than one. Therefore the implemented interval


$$
e_{\rm lo}\le Se\le e_{\rm hi}
$$


with upper allowance $k+2$ is conservative.

### 4.2 Enclosure of $\pi$

Machin’s identity is used in its exact form


$$
\pi=16\arctan(1/5)-4\arctan(1/239).
$$


For each alternating series, the code separately bounds the rounding losses of positive and negative terms. After the next power exceeds $S$, the alternating remainder has absolute value less than one scaled unit.

The subtraction in Machin’s identity correctly reverses the interval endpoints for the $1/239$ term.

### 4.3 Whole-form evaluation

For each already reduced pair $(p,q)$, $q>0$, the enclosure is


$$
\frac{q s_{\rm lo}-pS}{S}
\le q(e+\pi)-p\le
\frac{q s_{\rm hi}-pS}{S}.
$$


This evaluates the **whole same-index form**, not a selected component.

The reported results are:

| Probe | Sign | Certified $\lfloor\log_{10}|q(e+\pi)-p|\rfloor$ |
|---|---:|---:|
| endpoint $3$ | $-$ | $43069$ |
| endpoint $0$ | $-$ | $43068$ |
| half | $-$ | $68342$ |
| $n^2/2$ | $+$ | $68338$ |
| reference-canceling | $-$ | $31327$ |

All five forms are nonzero and have absolute value greater than one.

**Finite conclusion:** these five original $n=3375$ probes do not provide a small nonzero integer linear form. This neither proves an infinite exclusion nor settles irrationality.

---

# Part II. The $29$-adic audit and a new original-phase theorem

## 5. Audit of the leading-unit digit calculation

The leading-unit formula used by the Gram evaluator is correct.

For a nonzero binomial coefficient,


$$
29^{-e}\binom{M}{K}
\equiv
(-1)^e
\prod_i
\frac{M_i!}{K_i!(M-K)_i!}
\pmod{29},
\qquad e=v_{29}\binom{M}{K}.
$$


This follows by recursively stripping the multiples of $29$ from factorials and using Wilson’s theorem.

In the implemented product:

- the weight binomial is squared, so its $(-1)^{e_W}$ factor disappears;
- the two converted negative binomials contribute
  $(-1)^{e_1+e_2}$, implemented by the addition carries;
- their external signs multiply to
  

$$
(-1)^{(b+v_1-j)+(b+v_2-j)}
  =(-1)^{v_1+v_2}.
$$



The coefficient functions also match the proposed four-atom column. In particular, the middle returned coordinate is the Gram entry $G_{AD}$, not the coefficient $2G_{AD}$ in the quadratic polynomial. The separate diagonal and off-diagonal formulas account for this correctly.

The cutoff borrow enforces $j<b$. The two lower-index borrows enforce the zero convention when $b+v-j<0$. Zero-state pruning is legitimate because future contributions depend only on the retained state and remaining fixed digits.

The min-plus program is likewise a complete finite optimization over its digit states. Its floor-factorial witnesses independently certify the valuation at the returned $j$. The witnesses alone would establish only upper bounds on the minima; the exhaustive min-plus transition supplies the lower bounds.

Accordingly, the auxiliary zero Gram and the nine auxiliary minimum tables are credible at their stated finite scope. They do not themselves prove an original-power assertion.

The next result supplies that missing original-phase implication.

---

## 6. Six low digits suffice

Write $p=29$. The original phase has


$$
b\equiv410910916\pmod{29^6}.
$$


The exponent increment is


$$
574312172=\varphi(29^6),
$$


so the congruence is unchanged for every $u\ge0$.

In low-to-high digit order,


$$
b=(27,28,5,28,0,20,\ldots)_{29},
$$


and multiplication by $2001$ gives


$$
n=(0,7,24,7,3,9,\ldots)_{29}.
$$


Consequently,


$$
n+2=(2,7,24,7,3,9,\ldots)_{29},
$$




$$
2n=(0,14,19,15,6,18,\ldots)_{29}.
$$



For a supported atom, set


$$
K=b+v,\qquad A=2n+a-1,\qquad k=K-j.
$$


Then


$$
\binom{-2n-a}{k}=(-1)^k\binom{A+k}{k}.
$$


Its valuation is the number of carries in $A+k$. The valuation of $\binom{n+2}{j}$ is the number of borrows in subtracting $j$ from $n+2$.

Let, at digit $i$,

- $u_i$ be the outgoing weight-subtraction borrow;
- $v_i$ be the outgoing borrow in $K-j$;
- $c_i$ be the outgoing carry in $A+(K-j)$;
- $d_i$ be the digit of $j$.

The valuation contribution at that digit is


$$
u_i+c_i.
$$



### Lemma 6.1 — A direct proof of the required two-carry box

For


$$
0\le a\le435,\qquad -244\le v\le245,
$$


every supported atom satisfies


$$
\boxed{
v_{29}\!\left(
\binom{n+2}{j}\binom{-2n-a}{b+v-j}
\right)\ge2.
}
$$



#### Proof

Throughout this box, the relevant digits remain


$$
(K_3,K_4,K_5)=(28,0,20),
\qquad
(A_3,A_4,A_5)=(15,6,18).
$$



At digit $3$, if there is no outgoing weight borrow, then $d_3\le7$. The lower-index digit is at least


$$
28-7-1=20.
$$


Adding $A_3=15$ therefore forces an addition carry. Thus


$$
u_3+c_3\ge1.
$$



Suppose digit $5$ contributed zero. Then


$$
d_5\le9-u_4,
$$


while absence of the addition carry requires


$$
20-d_5-v_4+18+c_4\le28.
$$


These inequalities force


$$
v_4=1,\qquad u_4=c_4=0,\qquad d_5=9.
$$



But $u_4=0$ implies $d_4\le3$. Since $K_4=0$ and $v_4=1$, the lower-index digit at position $4$ is


$$
29-d_4-v_3\ge25.
$$


Adding $A_4=6$ forces $c_4=1$, a contradiction. Hence


$$
u_5+c_5\ge1.
$$



The contributions at digits $3$ and $5$ prove the result. ∎

This independently supplies the weighted box needed in A2’s finite normal-order argument. No inference from the auxiliary minimum table is involved.

### Theorem 6.2 — Three carries for all four leading atoms

For each pair


$$
(a,v)\in\{(1,0),(1,-1),(30,-29),(30,-30)\},
$$


and on every original phase,


$$
\boxed{
\binom{n+2}{j}\binom{-2n-a}{b+v-j}
\in29^3\mathbb Z_{29}
}
$$


on the original supported range.

#### Proof

The preceding proof already forces one valuation contribution at digit $3$ and one at digit $5$.

For the first two atoms,


$$
(K_1,A_1)=(28,14);
$$


for the last two,


$$
(K_1,A_1)=(27,15).
$$


If the weight subtraction has no borrow at digit $1$, then $d_1\le7$. The lower-index digit is consequently at least $19$, and addition of $A_1\ge14$ forces a carry.

Therefore


$$
u_1+c_1\ge1.
$$


The three distinct positions $1,3,5$ contribute at least three. ∎

The theorem is a divisibility statement, not an exact-minimum statement. The auxiliary witnesses establish exact minimum three for their own inputs; they do not establish equality on every original power.

---

## 7. The finite normal ordering survives the audit

The algebraic identity


$$
(\mathsf R_n\mathsf D_s\mathsf R_n v)_j
=
\sum_{t=0}^s
\binom j{s-t}\binom{-n}{t}
(\mathsf R_{2n+t}v)_{j-s+t}
$$


follows from


$$
\binom{j+\ell}{s}
=
\sum_t\binom j{s-t}\binom{\ell}{t}
$$


and


$$
\binom{-n}{\ell}\binom{\ell}{t}
=
\binom{-n}{t}\binom{-n-t}{\ell-t}.
$$


The nonnegative-index conventions make the apparently out-of-range terms zero. No division by $s!$ is required.

Crucially, the formula must be applied to the complete finite representation


$$
\theta
=
\left.
\mathsf R_n\mathsf D\mathsf R_n(w+z)
\right|_{0\le j<b},
$$


where $z$ is determined by the retained exterior solve. It does not authorize replacing the finite inverse by an uncorrected infinite inverse.

At precision $p^3$:

- the retained bandwidth is $86$;
- every nonconstant lower-inverse coefficient is divisible by $p$;
- the solved exterior vector $z$ is divisible by $p$;
- for heads of length at most $176$, all normal-ordered reconstructed atoms lie in Lemma 6.1’s box.

For the head terms, one may take


$$
a\le86+176=262,\qquad -176\le v\le86.
$$


For exterior terms the offsets remain below the stated $245$ bound.

Thus every nonbaseline term has a factor $p$ from its coefficient and $p^2$ from its reconstructed atom:


$$
\boxed{
\mathcal RA^{-1}h
\equiv
\mathcal R\mathsf R_{2n}\mathsf P_-h
\pmod{p^3}.
}
$$


This proves the required version of A2’s Theorem 6.1 with an explicit digit proof of its weighted hypothesis.

### Terminal coordinate

The original terminal weight is not removed. Direct subtraction of the low digits of $b$ from $n+2$ produces weight borrows at positions $0,1,3,5$. Hence


$$
\boxed{v_{29}(W_b)\ge4.}
$$


Its contribution vanishes at the present normalized precision for a proved reason, not by a changed boundary convention.

---

## 8. Signs and coefficient functions in the four-atom formula

The four-atom formula has the correct signs.

For a homogeneous head with


$$
h_r=r!(A+DL_r),\qquad
h_{29+r}=-Dr!,
\qquad0\le r\le28,
$$


the finite-head summation produces coefficient functions


$$
H_t(j)=\sum_{r\ge t}(-1)^{r+t}h_r\binom j{r-t}.
$$



At the present normalization only $t=0,29$ survive, since


$$
\binom{2n+t-1}{t}\equiv0\pmod{29}
$$


for the other $0\le t\le57$, while the two surviving coefficients are $1$ and $14$.

Lucas reduction gives


$$
H_0(j)=AF_d+D(G_d+eF_d),
\qquad
H_{29}(j)=-DF_d,
$$


where $j_0=d,j_1=e$. In particular, the sign of the $eF_d$ contribution is positive: it comes from combining the odd shift $29$ with $h_{29+r}=-Dr!$.

Reconstruction then gives exactly the four atom parameters in Theorem 6.2:


$$
(1,0),\quad(1,-1),\quad(30,-29),\quad(30,-30).
$$



The low-digit coefficient functions therefore do not rescue a valuation-two contribution. Each weighted atom already has valuation at least three before those coefficients are applied.

---

## 9. New original-phase output-content theorem

### Theorem 9.1

Let $h$ be either integral normalized homogeneous input, or an integral combination of the two, with the accepted homogeneous recurrence and relative finite-memory property. Then on every original phase,


$$
\boxed{
\mathcal RA^{-1}h\in29^3\mathbb Z_{29}^{\,b+1}.
}
$$



#### Proof

Truncate the input at the established precision-three head length $176$; the discarded tail is zero modulo $29^3$.

The complete finite normal-order result gives


$$
\mathcal RA^{-1}h
\equiv
\mathcal R\mathsf R_{2n}\mathsf P_-h
\pmod{29^3}.
$$


After division by the already proved common factor $29^2$, the right side modulo $29$ is the four-atom formula. Theorem 6.2 makes each of its terms zero.

The terminal coordinate is covered by $v_{29}(W_b)\ge4$. ∎

### Consequences for A2’s normalization

Write


$$
f^0=29^g h,\qquad
P=\frac{\mathcal RA^{-1}f^0}{29^2}=29^c x,
$$


with $h$ having a primitive initial pair and $x$ a primitive output vector. Then


$$
\boxed{c\ge g+1.}
$$



For the two normalized homogeneous columns used in A2,


$$
X_a=\frac{\mathcal RA^{-1}h^{(a)}}{29^2},
$$


we now have


$$
X_a\in29\mathbb Z_{29}^{\,b+1},
\qquad
X_a^TX_b\in29^2\mathbb Z_{29}.
$$



Thus the $29^{-2}$ leading Gram matrix is zero on the original family for the stronger reason that the entire leading column is zero.

What does **not** follow is


$$
c=g+1
\quad\text{or}\quad
\nu=0.
$$


The primitive norm loss remains uncontrolled. In particular,


$$
d=2c+4+\nu\ge2g+6,
$$


but this is a lower bound, not the norm-depth estimate needed for the whole-force alignment.

### Correct next $29$-adic target

The next column must be obtained from the complete inverse modulo $29^4$, then divided by $29^3$. It cannot be obtained merely by dividing the old baseline formula one more time.

At that order one must retain:

- the next lift of the homogeneous initial pair;
- the first lower-factor corrections;
- the solved exterior correction;
- the complete reconstruction, including its terminal row.

Terms that were $29$ times a valuation-two atom can now contribute. This is the precise obstruction to promoting the old four-atom baseline into a $29^{-3}$ leading-column formula.

---

# Part III. The actual binary input and a sharper integral observable bound

## 10. What the new polynomial source establishes

The source asserts, using the existing complete numerator artifact, that modulo $2^{20}$:

- both old $n$-branches are zero;
- both wide $2n$-branch numerators have the required factor $z^{176}$;
- the additional $44$ and $48$ factors of $1-z$ divide with zero remainder.

Thus the complete reconstructed series become


$$
\widehat G_f(z)=\frac{A_f(z)}{(1-z)^{2n+81}},
\qquad
\widehat G_e(z)=\frac{A_e(z)}{(1-z)^{2n+77}},
$$


with


$$
\deg A_f=81,\qquad \deg A_e=77.
$$



The code verifies all $92$ factor divisions by exact arithmetic modulo $2^{20}$.

A precision distinction is important: the subsequent two “full polynomial identity” checks are coefficientwise congruences modulo $2^{341}$. The serialized residue polynomials are not claimed to satisfy literal integer equalities without choosing compatible lifts. The fraction-free algorithm itself has an exact integer version, and the checked congruences are sufficient for the displayed guarded uses.

The twelve coefficient-conversion comparisons are finite checks. The general conversion is justified by the falling-factorial identity, not by extrapolating those twelve comparisons.

---

## 11. The common summand and the actual boundary

Set


$$
B=2n,\qquad N=n+2.
$$


For $R_f=81,R_e=77$, define


$$
D_\alpha=B^{\overline{R_\alpha}},
$$




$$
U_\alpha(j)
=
\sum_{r=0}^{R_\alpha}
A_{\alpha,r}
(b-j)_{\underline r}
(B+b-j)^{\overline{R_\alpha-r}}.
$$


Then


$$
[z^{b-j}]
\frac{A_\alpha(z)}{(1-z)^{B+R_\alpha}}
=
\frac{U_\alpha(j)}{D_\alpha}
\binom{B+b-j-1}{b-j}.
$$



Both contractions use the one exact summand


$$
T(j)=
\binom Nj^2
\binom{2n+b-j-1}{b-j}^2,
\qquad0\le j\le b.
$$



Define


$$
\mathcal A(j)=(N-j)^2(b-j)^2,
$$




$$
\mathcal B(j)=j^2(2n+b-j)^2,
$$




$$
\Delta R(j)=\mathcal A(j)R(j+1)-\mathcal B(j)R(j).
$$


The exact ratio identity is


$$
T(j)\mathcal A(j)=T(j+1)\mathcal B(j+1).
$$



### Correction: the new telescoping boundary is zero

Summation over the original range gives


$$
\sum_{j=0}^{b}T(j)\Delta R(j)
=
T(b)\mathcal A(b)R(b+1).
$$


But here


$$
\boxed{\mathcal A(b)=0.}
$$


Therefore


$$
\boxed{
\sum_{j=0}^{b}T(j)\Delta R(j)=0
}
\tag{11.1}
$$


for every polynomial $R$.

The old $176^2$ boundary belonged to $L=b+176$. It does not survive the actual $z^{176}$ cancellation and the new $L=b$ conversion.

The source’s stored value $R(b+1)$ is harmless bookkeeping, but its boundary prefactor is exactly zero.

### Why the physical terminal row has not disappeared

At $j=b$,


$$
T(b)=W_b^2,
\qquad
U_\alpha(b)=D_\alpha A_\alpha(0).
$$


Hence the physical terminal contributions are


$$
W_b^2A_f(0)^2,
\qquad
W_b^2A_f(0)A_e(0).
$$


They remain in the norm and mixed form. In particular, the exterior $+1$ already encoded in the complete exponential numerator remains present.

The vanishing statement concerns the **telescoping flux**, not the terminal summand of the observable.

---

## 12. Rational three-moment reduction and its guards

The leading coefficient is


$$
[j^{k+3}]\Delta j^k=k+\tau,
\qquad
\tau=2n-4.
$$


Thus every payload of degree $D\le162$ reduces over $\mathbb Q$ to degree at most two.

For the two actual payloads,


$$
P_f=U_f^2,\qquad \deg P_f=162,
$$




$$
P_m=U_fU_e,\qquad \deg P_m=158.
$$



The source’s valuations are consistent with the short consecutive products:


$$
v_2(D_f)=80,\qquad v_2(D_e)=77,
$$




$$
v_2(\Gamma_{162})=161,\qquad
v_2(\Gamma_{158})=158.
$$


Therefore the unsaturated multiplier valuations are


$$
161+2(80)=321,
$$




$$
158+80+77=315.
$$



Those are genuine sufficient guards for the displayed fraction-free evaluation. They are not intrinsic lower bounds on the precision required by the actual observable.

The next theorem removes the pivot-product part from the evaluation bound, provided the saturation is certified.

---

## 13. Exact saturation is valid for this observable

Let


$$
R=\mathbb Z_{(2)}
$$


and let $V_D$ be the $R$-module of polynomials of degree at most $D$. Define


$$
\Lambda_D
=
\operatorname{span}_R
\{\Delta j^k:0\le k\le D-3\}.
$$


Its $2$-saturation is


$$
\Lambda_D^{\mathrm{sat}}
=
\{P\in V_D:\;2^tP\in\Lambda_D
\text{ for some }t\ge0\}.
$$



The actual moment functional is


$$
\mathscr L(P)=\sum_{j=0}^{b}T(j)P(j).
$$


It takes values in $\mathbb Z_{(2)}\subset\mathbb Z_2$.

### Theorem 13.1 — Integral three-observable quotient

The functional $\mathscr L$ annihilates $\Lambda_D^{\mathrm{sat}}$. Consequently it factors through a free rank-three $R$-module


$$
\boxed{V_D/\Lambda_D^{\mathrm{sat}}.}
$$



#### Proof

Equation (11.1) gives


$$
\mathscr L(\Lambda_D)=0
$$


as an exact identity, not merely modulo a fixed power of two.

If $2^tP\in\Lambda_D$, then


$$
2^t\mathscr L(P)=0.
$$


Since $\mathbb Z_2$ is torsion-free,


$$
\mathscr L(P)=0.
$$



The nonzero leading pivots $k+\tau$ show that $\Lambda_D$ has rank $D-2$, while $V_D$ has rank $D+1$. Saturation does not change rank and makes the quotient torsion-free. Over $R$, the quotient is therefore free of rank three. ∎

### The distinction from invalid modular division

It would be invalid to infer


$$
y\equiv0\pmod{2^{20}}
$$


from


$$
2^e y\equiv0\pmod{2^{20}}.
$$



That is not the argument above. The saturated relation is justified by an **exact finite summation identity** and torsion-freeness before reduction modulo $2^{20}$.

The nonunit Smith components must therefore be computed and certified; they are not declared units. Once their exact saturated relations are established, their evaluations are exactly zero.

This corrects the overly restrictive interpretation that those components must remain independent moment observables for this particular exact functional.

---

## 14. The correct bounded Smith presentation

A single presentation with $D=162$ accommodates both actual payloads:


$$
\boxed{
L_{162}
=
\bigl([\Delta j^k]_{0\le r\le162}\bigr)_{0\le k\le159},
}
$$


a matrix of size


$$
\boxed{163\times160.}
$$



There is no need for a formal unknown boundary coordinate. Equivalently, an augmented implementation may retain it and add the exact relation that the boundary observable is zero.

### 14.1 Rank and Smith bounds

Modulo $2$,


$$
\mathcal A(j)\equiv\mathcal B(j)\equiv j^2(j+1)^2,
$$


so


$$
\Delta R
\equiv
j^2(j+1)^2\bigl(R(j+1)-R(j)\bigr).
$$


The invariants of the shift $j\mapsto j+1$ are


$$
\mathbb F_2[j^2+j].
$$



On polynomials of degree at most $159$, the shift-difference kernel has dimension $80$. Thus


$$
\boxed{\operatorname{rank}_{\mathbb F_2}L_{162}=80.}
$$


Its rational rank is $160$. Therefore it has exactly


$$
\boxed{80\text{ nonunit }2\text{-primary Smith pivots}.}
$$



The leading triangular minor has determinant $\Gamma_{162}$, whose valuation is $161$. Hence


$$
\sum_i e_i\le161.
$$


Because eighty exponents are positive,


$$
\boxed{\max_i e_i\le161-79=82.}
$$



For the separate $D=158$ presentation the corresponding figures would be


$$
159\times156,\quad
\operatorname{rank}_{\mathbb F_2}=78,\quad
78\text{ nonunit pivots},\quad
\max e_i\le81.
$$


The single $D=162$ calculation is sufficient; no second Smith calculation is required.

These ranks differ from the generic “formal boundary” ranks in A5 for a precise reason: the actual shortened boundary is already known to vanish.

---

## 15. New pure-observable precision bound

Suppose a certified saturated normal form supplies quotient generators


$$
S_1,S_2,S_3\in V_{162}
$$


and free payload coordinates


$$
[P_f]=\sum_{i=1}^3 c_{f,i}[S_i],
\qquad
[P_m]=\sum_{i=1}^3 c_{m,i}[S_i].
$$


Define the three integral observables


$$
I_i=\mathscr L(S_i).
$$



Then exactly, for the chosen integer lifts of the twenty-bit numerators,


$$
D_f^2\,D_{\rm raw}^{\rm lift}
=
\sum_{i=1}^3c_{f,i}I_i,
$$




$$
D_fD_e\,E_{\rm raw}^{\rm lift}
=
\sum_{i=1}^3c_{m,i}I_i.
$$



No factor $\Gamma$ occurs.

Therefore, without any payload-content improvement, it suffices to evaluate the integral observable combinations to


$$
20+v_2(D_f^2)=\boxed{180}
$$


and


$$
20+v_2(D_fD_e)=\boxed{177}
$$


bits.

### Payload-specific sharpening

Let


$$
s_f=\min_i v_2(c_{f,i}),\qquad
s_m=\min_i v_2(c_{m,i}).
$$


After factoring these common powers from the free coordinates, sufficient observable precisions are


$$
\boxed{
K_f=\max(0,180-s_f),\qquad
K_m=\max(0,177-s_m).
}
$$


If a coordinate is only known to vanish to a working cutoff, the conclusion must be stated at that cutoff; no infinite valuation is inferred.

### Physical precision remains twenty bits

The $341$-bit polynomial arithmetic uses chosen integer lifts of known twenty-bit numerator coefficients. Changing those lifts changes each original reconstructed coefficient, and hence each original finite contraction, by a multiple of $2^{20}$.

Thus the new bound does not request a $180$-bit physical force, a new $180$-bit Schur solve, or a higher-precision physical logarithmic omission.

It concerns only the exact integral observables used to evaluate the already fixed twenty-bit contraction.

### Limitation

A rank-three saturated quotient is not automatically a practical evaluator for $I_1,I_2,I_3$ at the original index. Their transport or direct evaluation remains unpaid. No general automaticity or creative-telescoping existence theorem is being substituted for that computation.

---

# Part IV. What the new bounded postprocessing should certify

## 16. One new Smith/payload-image calculation

This is the coordinator’s already planned new postprocessing, with the boundary correction and sharper target made explicit. It does not repeat any old operator or jet calculation.

### Inputs

1. The exact fixed binary $n,b$.
2. The actual $A_f,A_e$ from the supplied short-numerator artifact.
3. The existing $U_f,U_e$, or their chosen integer lifts.
4. The exact polynomials
   

$$
\mathcal A=(n+2-j)^2(b-j)^2,\qquad
   \mathcal B=j^2(2n+b-j)^2.
$$


5. The single $163\times160$ matrix $L_{162}$.
6. The two payloads $U_f^2$ and $U_fU_e$, with the latter padded to degree $162$.

### Expected verifiable output

The postprocessing should certify:

- rational rank $160$;
- binary rank $80$;
- exactly $80$ nonunit $2$-primary pivots;
- total nonunit valuation at most $161$;
- largest nonunit valuation at most $82$;
- a saturated quotient of free rank three;
- three explicit integral quotient generators;
- both actual payload images in that quotient;
- the attained values or certified lower bounds for $s_f,s_m$;
- the resulting sufficient precisions $K_f,K_m$;
- exact verification that the telescoping flux at $j=b$ is zero;
- preservation of the nonzero physical $j=b$ summand in both payloads.

An exact normal-form certificate, or a valuation-aware certificate with every division guarded, is required. Merely reducing the relation matrix modulo $2^{20}$ and inverting its even pivots is not acceptable.

The receipt must separately state whether the three observables themselves have been evaluated. Smith data and payload images alone are not values of $D_{\rm raw}$ or $E_{\rm raw}$.

No new $29$-adic digit scan is needed to establish Theorem 9.1; its proof above is symbolic.

---

# Part V. Complete forcing, final gcd, and the global obstruction

## 17. The remaining local obligations

### 17.1 At $29$

The first possible normalized output depth is now at least three. The remaining task is to determine the actual output content and primitive norm loss, and then evaluate the complete mixed identity at its true relative precision:


$$
x^TQ-29^c\rho_n x^Tx
\equiv0\pmod{29^{c+\nu+1}}.
$$



The complete initial charges, all source rows $1\le i\le b-2$, and the terminal return remain necessary. The new divisibility theorem does not justify discarding the logarithmic contribution at that unknown normalized depth.

### 17.2 At $2$

The immediate finite task is evaluation of the three saturated integral observables at the certified payload-dependent precisions.

Even a completed absolute twenty-bit contraction does not, without certified contents and norm valuations, establish a norm-relative twenty-bit law. The retained logarithmic omission condition must still be checked at the actual norm-relative depth.

---

## 18. All-prime normalization remains mandatory

For the complete integer columns and retained row metric, the final reduction remains


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
}
$$



Neither the new $29$-adic content theorem nor a binary observable computation replaces this all-prime gcd.

The actual primitive denominator is


$$
\log q_n
=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
$$


The relevant real quantity is always


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n,
}
$$


with the same original index in $q_n,p_n,\epsilon_n$.

A local vanishing theorem may increase known content while leaving the primitive denominator comparison unresolved. Likewise, a rapidly decaying approximation error does not suffice if the actual denominator grows too quickly.

To prove irrationality by this route one still needs an infinite original subsequence with complete, nonzero forms satisfying


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0.
$$


The supplied work does not establish that condition.

---

## 19. Proof-status ledger

| Statement | Status |
|---|---|
| Closed synchronization, no-overlap, deep-family exclusion, reachability results | Reused; not reopened |
| Integer moment and exponential recurrences | Independently derived |
| Full-force factorial normalization | Checked; companion identity reused at its three-row scope |
| $n=3375$ contents and primitive probes | Reviewed finite computation |
| Five $n=3375$ whole-form enclosures | Rigorous finite method; supplied outputs all nonzero and $>1$ in absolute value |
| Leading-unit signs and cutoff logic | Audited |
| Auxiliary zero Gram and minimum-three tables | Finite corroboration only |
| Required weighted two-carry box | Proved directly from low digits |
| Four leading atoms divisible by $29^3$ on every original phase | **New proof** |
| Original homogeneous output divisible by $29^3$ | **New proof** |
| $c\ge g+1$ | **New proof** |
| Exact output content or primitive norm loss | Open |
| Actual binary single-summand reduction | Reviewed; twenty-bit physical scope retained |
| New telescoping boundary | **Exactly zero, proved** |
| Physical terminal summand and exterior correction | Retained |
| Saturated integral three-observable quotient | **New proof** |
| Sufficient observable precisions $180/177$ bits | **New bound**, before payload-specific improvement |
| Actual Smith/payload images | Unevaluated new postprocessing |
| Original weighted binary Gram pair | Not evaluated here |
| All-prime denominator versus whole same-index error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The substantive original-phase correction is


$$
\boxed{
29^{-2}\mathcal RA^{-1}h\equiv0\pmod{29}
}
$$


for the homogeneous input space on every original power phase. The auxiliary zero Gram was detecting a column normalization that was still too shallow. The next $29$-adic calculation must include the complete order-three column, not just a deeper evaluation of the old four-atom baseline.

The substantive binary improvement is


$$
\boxed{
\text{the actual shortened problem has zero telescoping flux and a
certifiable integral rank-three observable quotient.}
}
$$


Once the planned saturation is certified, the pivot-product guard is unnecessary in the subsequent observable evaluation. The remaining denominator guards are $160$ and $157$ bits, potentially reduced by the actual free payload contents.

The exact next bounded arithmetic task is the **single $163\times160$ saturated Smith/payload-image postprocessing** described above. Its output will specify three integral observables and their required precisions; it will not, by itself, evaluate them.

Finally, the all-prime final gcd and the whole same-index error remain indispensable. The five supplied $n=3375$ forms are rigorously large, but that is a finite conclusion. Neither the new original-phase divisibility theorem nor the new binary observable bound is an irrationality proof.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


