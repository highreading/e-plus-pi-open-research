> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 2 — The $29^2$ lift: a three-channel kernel quotient, but still two channels for the complete short-head defect

## Executive assessment

There is a useful distinction between the sufficient kernel box and the actual complete contraction.

For the sufficient $K=2$ box


$$
R_*=244,\qquad
0\le a,a'\le244,\qquad
-244\le v,v'\le245,\qquad
0\le t\le490,
$$


I obtain the following results modulo $29^2=841$.

1. **The full kernel table has a three-observable quotient.** The two previous tails $T_1,T_2$, now required modulo $841$, suffice except in the positive-$a$, $\sigma=0$–$\sigma=0$ sector. That sector requires one additional common tail, at precision $29$:
   

$$
T_0=\sum_{q=0}^{B_*}\binom{N_*}{q}^{2}\pmod{29}.
$$


   Its coefficient is always divisible by $29$.

2. **The $\sigma=2$ sector still vanishes, now modulo $841$.** This is not a coefficientwise lift of the previous Lucas argument. Two more low digits of the actual phase force a second carry. In fact, the stronger pointwise statement holds:
   

$$
\boxed{
   \binom{n+2}{j}
   \binom{-2n-a}{b+v-j}\equiv0\pmod{841}
   }
$$


   throughout the stated offset box and the supported original range.

3. **No additional tail is needed for the actual norm/defect contraction at this precision.** A head input passes through the accepted finite inverse using only $\sigma=1,2$ atoms. Thus its pairing with the complete second column never uses the new $\sigma=0$–$\sigma=0$ channel. The complete short-head norm and complete source-plus-end defect still factor through just $T_1,T_2$ modulo $841$.

4. **The actual phase has six fixed digits, not merely four.** The four previously used digits remain correct, but the exponent increment is
   

$$
574312172=28\cdot29^5.
$$


   Consequently the next two digits are fixed as well:
   

$$
\boxed{
   b\bmod29^6=(27,28,5,28,0,20)_{29}.
   }
$$


   The first $u$-dependent digit is digit $6$:
   

$$
\boxed{b_6\equiv9-u\pmod{29}.}
$$



5. **There is a bounded counterexample to retaining the old zero classification.** At an explicitly specified auxiliary input matching an actual seven-digit phase,
   

$$
S_0(-1,-1;-1,-1)\equiv812=-29\pmod{841},
$$


   whereas this entire sector was zero modulo $29$. I also give a three-input rank certificate proving that one additional channel is necessary for the uniform six-digit-phase quotient. This is a statement about that phase class, not an evaluated original power.

The remaining original-index tasks are still substantial. In particular, the actual $T_1,T_2$ modulo $841$, the complete scalar coefficients, and the true norm-sensitive digit have not been evaluated. Nothing here proves the required alignment at $v_{29}(\mathcal N)+2$, much less the all-prime denominator estimate needed for irrationality.

No executable tools were used. The bounded numerical residues below are hand-derived certificates for new calculations, not reported execution results.

---

## 1. Retained domain, finite boundaries, and precision correction

Throughout,


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad
n=2001b,\qquad u\ge0.
$$



The domains remain exactly


$$
0\le j<b
$$


for contact coordinates,


$$
1\le i\le b-2
$$


for recurrence/source rows, and


$$
0\le j\le b
$$


for reconstruction.

The kernels remain


$$
S_t(A,v;A',v')
=
\sum_{j=0}^{b-1}
\binom{n+2}{j}^{2}\binom jt
\binom A{b+v-j}
\binom{A'}{b+v'-j}.
\tag{1.1}
$$



I reuse the accepted finite atom factorization, including its source-head subtraction, finite upper-transform tails, endpoint solve, and reconstructed exterior.

I also adopt A4 Turn 2’s precision correction:

> Exact valuation/unit tracking of the summand recurrence requires fixed unit precision, not a cumulative denominator-valuation guard. A temporarily zero summand still needs its hidden unit state because later valuations can decrease.

For a recurrence


$$
U_{j+1}=U_jN_j/D_j,
$$


the correct state is


$$
U_j=p^{e_j}u_j,
$$


with the exact integer valuation $e_j$ and $u_j\bmod p^K$, updated by unit inversion. The summation-length problem remains; cumulative precision loss is not the obstruction.

The new derivation below instead uses a low/high split and keeps carry layers explicitly.

---

## 2. The required actual low phase

### 2.1 Six fixed digits

Set


$$
M=p^4=707281,\qquad \beta=687936.
$$


The established four-digit phase is


$$
\beta=(27,28,5,28)_{29}.
$$



The stronger fixed phase needed here is


$$
\boxed{
\beta_6=b\bmod p^6
=410910916
=(27,28,5,28,0,20)_{29}.
}
\tag{2.1}
$$



Accordingly,


$$
\boxed{
n+2\bmod p^6
=186913296
=(2,7,24,7,3,9)_{29}.
}
\tag{2.2}
$$



These are fixed for every original $u$, because


$$
574312172=\varphi(29^6)=28\cdot29^5.
$$



Thus it would be incorrect to treat digits $4$ and $5$ as free phase variables.

### 2.2 A small arithmetic certificate

Write


$$
249005515=3+28m,\qquad m=8893054.
$$


Then


$$
m=(1,11,18,16,12)_{29}.
$$



Direct integer reduction gives


$$
3^{28}\bmod29^7=3456469227,
$$


whose digits are


$$
(1,15,13,28,14,23,5)_{29}.
$$



A binomial expansion of $(3^{28})^m$ through degree $6$ gives


$$
(3^{28})^m
\equiv
(1,15,4,17,22,15,17)_{29}
\pmod{29^7}.
$$


Multiplication by $27$ gives


$$
\boxed{
3^{249005515}
\equiv
(27,28,5,28,0,20,9)_{29}
\pmod{29^7}.
}
\tag{2.3}
$$



The sixth-digit affine constant below is verified by


$$
2001\cdot410910916
=
1382\cdot594823321+186913294.
\tag{2.4}
$$



### 2.3 The first $u$-dependent digit

Since


$$
3^{28}=1+15p+O(p^2),
$$


we have


$$
3^{28p^5}=1+15p^6+O(p^7).
$$


As $b\bmod p=27$,


$$
27\cdot15\equiv-1\pmod p.
$$


Therefore


$$
\boxed{
b\bmod p^7
=
\beta_6+p^6\delta(u),
\qquad
\delta(u)=(9-u)\bmod29,
}
\tag{2.5}
$$


where $0\le\delta(u)\le28$.

This is an actual modular-exponentiation consequence, not a presumed digit period.

### 2.4 High affine parameters

The useful high parameters are:



$$
B_*=\frac{b-\beta}{p^4},
\qquad
N_*=\frac{n+2-191112}{p^4}=2001B_*+1946.
\tag{2.6}
$$



Their first two digits satisfy


$$
(B_*)_0=0,\quad (B_*)_1=20,
\qquad
(N_*)_0=3,\quad (N_*)_1=9.
\tag{2.7}
$$



After removing digit $4$, put


$$
B_5=B_*/29,\qquad N_5=(N_*-3)/29.
$$


Then


$$
\boxed{N_5=2001B_5+67.}
\tag{2.8}
$$



After removing the six fixed digits, put


$$
C=\frac{b-\beta_6}{p^6},
\qquad
X=\frac{n+2-186913296}{p^6}.
$$


Then


$$
\boxed{X=2001C+1382.}
\tag{2.9}
$$



Finally, writing


$$
C=\delta+29C_7,
$$


gives


$$
\boxed{
\frac{X-19}{29}
=
2001C_7+69\delta+47.
}
\tag{2.10}
$$



The constants $1946,67,1382,69\delta+47$ are retained. None may be dropped in a high-digit calculation.

---

## 3. Carry and unit layers modulo $p^2$

### 3.1 The surviving valuation budget

For a supported negative-upper summand, write


$$
e_W=v_p\binom{n+2}{j},\quad
e_t=v_p\binom jt,
$$


and let $e_A,e_{A'}$ be the valuations of the two converted nonnegative binomials.

The summand valuation is


$$
2e_W+e_t+e_A+e_{A'}.
$$


Consequently, modulo $p^2$, every surviving summand satisfies


$$
\boxed{
e_W=0,\qquad e_t+e_A+e_{A'}\le1.
}
\tag{3.1}
$$



There are two genuinely different layers:

- **valuation zero:** unit parts are needed modulo $p^2$;
- **valuation one:** unit parts are needed only modulo $p$, followed by multiplication by $p$.

The no-carry layer still has nonzero unit corrections.

### 3.2 An explicit unit formula

Let $x=y+z\ge0$, and let $x_i,y_i,z_i$ denote base-$p$ digits. Put


$$
e=v_p\binom xy,\qquad
H_r=\sum_{a=1}^{r}a^{-1}\pmod p,\quad H_0=0,
$$


and


$$
c=(p-1)!\pmod{p^2}.
$$



Separating factorial valuations from unit parts gives, at the required precision,


$$
\binom xy
\equiv
p^ec^e
\prod_i\frac{x_i!}{y_i!z_i!}
\left[
1+p\sum_i
\bigl(
x_{i+1}H_{x_i}
-y_{i+1}H_{y_i}
-z_{i+1}H_{z_i}
\bigr)
\right].
\tag{3.2}
$$


For $e=0$, this is interpreted modulo $p^2$. For $e=1$, only the product modulo $p$ is needed, and $c\equiv-1\pmod p$.

A proof follows from the unit-factorial recurrence


$$
U(m)=g(m)U(\lfloor m/p\rfloor),
$$


where


$$
g(m)\equiv
c^{\lfloor m/p\rfloor}
(m\bmod p)!
\bigl(1+p\lfloor m/p\rfloor H_{m\bmod p}\bigr)
\pmod{p^2}.
$$


The exponent difference of $c$ in the binomial quotient is exactly $e$.

All inversions in (3.2) are unit inversions.

### 3.3 Borrow and carry transitions

For subtraction $B-j$, with incoming borrow $\varepsilon$,


$$
k_i=B_i-j_i-\varepsilon+p\varepsilon^+,
\qquad
\varepsilon^+=\mathbf1_{B_i-j_i-\varepsilon<0}.
\tag{3.3}
$$



For addition $D+(B-j)$, with incoming carry $c_i$,


$$
x_i=D_i+k_i+c_i-pc_{i+1},
\qquad
c_{i+1}=\mathbf1_{D_i+k_i+c_i\ge p}.
\tag{3.4}
$$



Kummer’s valuation is the total number of outgoing carries $c_{i+1}$.

At precision $p^2$, one must distinguish:

- no addition carry;
- one internal low carry that has stopped before the interface;
- one carry crossing the low/high interface;
- a high carry when the low part is carry-free.

The last two cases are not coefficientwise Lucas lifts.

---

## 4. The exact four-digit split preserves the original cutoff

Let


$$
N_0=191112=(2,7,24,7)_{29}.
$$


Because $e_W=0$, the low four digits of $j$ lie in


$$
\boxed{
\mathcal L_2=
\left\{
d+29q+29^2e+29^3f:
0\le d\le2,\;
0\le q\le7,\;
0\le e\le24,\;
0\le f\le7
\right\}.
}
\tag{4.1}
$$


There are


$$
3\cdot8\cdot25\cdot8=4800
$$


such residues.

Write


$$
j=Mq+s,\qquad s\in\mathcal L_2.
$$



Every such $s$ satisfies


$$
s\le N_0=191112<\beta-244.
\tag{4.2}
$$


Therefore:

- the original condition $j<b$ is exactly $0\le q\le B_*$;
- both support conditions $b+v-j\ge0$, $b+v'-j\ge0$ hold throughout that same high range;
- there is no subtraction borrow into digit $4$.

In particular, the last high block $q=B_*$ is retained only because every surviving low residue lies below the actual endpoint. No completed block has been substituted for the original finite range.

### Small lower indices

For $0\le t\le490<p^2$,


$$
\boxed{\binom{Mq+s}{t}\equiv\binom st\pmod{p^2}.}
\tag{4.3}
$$


Indeed, for $1\le k\le t$,


$$
v_p\binom{Mq}{k}\ge4-v_p(k)\ge3,
$$


and Vandermonde applies.

The same argument applies to a complementary lower index $a-1\le243$. Thus a $\sigma=0$, $a>0$ factor has no unresolved high unit correction at this precision.

---

## 5. A strengthened $\sigma=2$ annihilation theorem

The relevant digits of


$$
D=2n+a-1,\qquad 0\le a\le244,
$$


are


$$
D_2=19,\qquad D_3=15,\qquad D_4=6,\qquad D_5=18.
\tag{5.1}
$$


The offset box does not change these four digits.

### Theorem 5.1

For every supported $0\le j<b$, every $0\le a\le244$, and every $-244\le v\le245$,


$$
\boxed{
v_p\left(
\binom{n+2}{j}
\binom{-2n-a}{b+v-j}
\right)\ge2.
}
\tag{5.2}
$$



#### Proof: $e_W=0$

Then


$$
j_2\le24,\quad j_3\le7,\quad j_4\le3,\quad j_5\le9.
$$



At digit $2$, the effective minuend in $b+v-j$ is $5$ or $6$. If subtraction borrows there, then $k_2\ge10$, so adding $D_2=19$ creates a carry. At digit $3$, the resulting $k_3\ge20$, so a second addition carry occurs.

Otherwise there is no subtraction borrow at digit $2$, and


$$
k_3=28-j_3\ge21.
$$


Thus digit $3$ creates an addition carry.

For there to be only this one carry, all earlier addition carries must be absent. At digit $4$:

- if $j_4>0$, then $k_4=29-j_4\ge26$, and
  

$$
D_4+k_4+1\ge33,
$$


  creating another carry;
- if $j_4=0$, no subtraction borrow leaves digit $4$, but at digit $5$,
  

$$
k_5=20-j_5\ge11,
  \qquad D_5+k_5\ge29,
$$


  again creating another carry.

Hence $e_A\ge2$.

#### Proof: $e_W=1$, $e_A=0$ is impossible

Carry-free addition to $D_3=15$ requires $k_3\le13$. This forces $j_3\ge14$, and therefore a borrow in the weight subtraction $(n+2)-j$ at digit $3$.

Since this is the only weight borrow, it must stop at digit $4$, requiring $j_4\le2$. Carry-free addition to $D_4=6$, with $b_4=0$, then forces $j_4=0$.

There is consequently no borrow in $b+v-j$ into digit $5$. Carry-free addition to $D_5=18$ requires $j_5\ge10$, while the weight, having spent its only borrow, requires $j_5\le9$. Contradiction.

The cases $e_W\ge2$ are immediate. ∎

### Consequences

Every kernel containing a $\sigma=2$ factor is zero modulo $841$.

More strongly, the reconstructed output of each $\sigma=2$ atom in the sufficient box is zero modulo $841$, because both reconstructed interior terms retain that upper-parameter type.

The actual terminal coordinate is also harmless at this absolute precision. The first six digits show at least four borrows in


$$
(n+2)-b,
$$


at digits $0,1,3,5$. Thus


$$
\boxed{v_p(W_b)\ge4.}
\tag{5.3}
$$


This is a proved valuation bound on the retained terminal term, not its deletion.

---

## 6. The surviving low/high unit corrections

Define the tails


$$
\boxed{
T_m=
\sum_{q=0}^{B_*}
\binom{N_*}{q}^{2}
\binom{N_*+B_*-q}{B_*-q}^{m},
\qquad m=0,1,2.
}
\tag{6.1}
$$


We require


$$
T_1,T_2\pmod{p^2},\qquad T_0\pmod p.
$$



For a $\sigma=1$ factor set


$$
d_1(a)=191109+a.
$$


For a $\sigma=0$, $a>0$ factor set


$$
d_0(a)=a-1.
$$



For $s\in\mathcal L_2$, write


$$
k_v(s)=\beta+v-s,
\qquad
c_{\sigma,a,v}(s)
=
\left\lfloor
\frac{d_\sigma(a)+k_v(s)}{M}
\right\rfloor.
\tag{6.2}
$$


For $\sigma=0$, this $c$ is always zero. For $\sigma=1$, it is $0$ or $1$.

### 6.1 No-carry interface correction

For a carry-free low $\sigma=1$ factor, the low digit analysis forces


$$
s_3=7,\qquad k_3=21,\qquad d_3=7.
$$


Since


$$
H_7\equiv-3,\qquad H_{21}=H_7,\qquad H_{28}=0\pmod{29},
$$


its interface correction is


$$
3\bigl((N_*)_0+(B_*-q)_0\bigr).
$$



The squared weight contributes


$$
-6\bigl((N_*)_0-q_0\bigr).
$$



For $m$ carry-free $\sigma=1$ factors, the total correction is therefore


$$
(-6+3m)(N_*)_0+3m(B_*)_0+(6-3m)q_0.
\tag{6.3}
$$



On the actual phase,


$$
(N_*)_0=3,\qquad(B_*)_0=0.
$$


Moreover, every nonzero $T_1$ or $T_2$ summand modulo $p$ has $q_0=0$: if $q_0=1,2,3$, then


$$
(B_*-q)_0=29-q_0,
$$


which creates a carry when added to $3$.

Thus the correction is



$$
\boxed{
-9\quad(m=1),\qquad 0\quad(m=2).
}
\tag{6.4}
$$



This nonzero $-9$ is essential in the mixed sector.

### 6.2 A single low carry crossing the interface

For a $\sigma=1$ factor with exactly one low carry, crossing digit $3$, the high factorial ratio becomes


$$
(N_*+B_*-q+1)
\binom{N_*+B_*-q}{B_*-q}.
\tag{6.5}
$$



Modulo $p$, its potentially nonzero summands again require $q_0=0$. Hence the prefactor is


$$
3+0+1=4.
\tag{6.6}
$$



This gives a factor $4$, not the unshifted high Lucas factor.

For two $\sigma=1$ factors, a single interface carry cannot survive: a carry-free companion forces $s_3=7$, whereas a lone interface carry with no earlier carries requires $s_3\le6$. All remaining possibilities spend at least two carries.

---

## 7. Explicit three-observable quotient for the entire $K=2$ box

For $\sigma,\sigma'\in\{0,1\}$, with positive $a$ whenever $\sigma=0$, define the bounded low summand


$$
\begin{aligned}
L_s={}&
\binom{N_0}{s}^{2}\binom st\\
&\times
\binom{d_\sigma(a)+k_v(s)}{d_\sigma(a)}
\binom{d_{\sigma'}(a')+k_{v'}(s)}{d_{\sigma'}(a')}.
\end{aligned}
\tag{7.1}
$$


All low coefficients below use at most $4800$ such terms.

### 7.1 The $(0,0)$ sector

Put


$$
\lambda_{00}=(-1)^{v+v'}\sum_{s\in\mathcal L_2}L_s\pmod{p^2}.
\tag{7.2}
$$



Then


$$
\boxed{\lambda_{00}\equiv0\pmod p.}
\tag{7.3}
$$



Indeed, modulo $p$, the two small-complement factors and $\binom st$ depend only on $s_0,s_1$. Summing over $s_2$ produces


$$
\sum_{e=0}^{24}\binom{24}{e}^{2}
=
\binom{48}{24}\equiv0\pmod p.
$$


The same cancellation removes the weight’s low/high unit correction, which depends on $s_3$ but not on $s_2$.

Consequently,


$$
\boxed{
S_t(-a,v;-a',v')
\equiv\lambda_{00}T_0\pmod{p^2}.
}
\tag{7.4}
$$



Only $T_0\bmod p$ is needed.

### 7.2 The mixed $(0,1)$ sector

Let $c(s)$ denote (6.2) for the $\sigma=1$ factor, and put


$$
C_0=\sum_{\substack{s\in\mathcal L_2\\c(s)=0}}L_s,
\qquad
C_1=\sum_{\substack{s\in\mathcal L_2\\c(s)=1}}L_s.
$$


Then


$$
\boxed{
\lambda_{01}
=
(-1)^{v+v'}
\bigl((1-9p)C_0+4C_1\bigr)
\pmod{p^2},
}
\tag{7.5}
$$


and


$$
\boxed{
S_t(-a,v;-n-a',v')
\equiv\lambda_{01}T_1\pmod{p^2}.
}
\tag{7.6}
$$



The symmetric formula holds for $(1,0)$.

The terms in $C_1$ are already divisible by $p$; their unit precision is only one digit. Terms with an internal low carry and no interface carry occur in $C_0$ and are retained.

### 7.3 The $(1,1)$ sector

Put


$$
\lambda_{11}
=
(-1)^{v+v'}\sum_{s\in\mathcal L_2}L_s
\pmod{p^2}.
\tag{7.7}
$$


Then


$$
\boxed{
S_t(-n-a,v;-n-a',v')
\equiv\lambda_{11}T_2\pmod{p^2}.
}
\tag{7.8}
$$



The zero interface correction in (6.4) is specific to the actual phase and the squared weight.

### 7.4 The $A=0$ sector

Its exact singleton support formula remains unchanged. If $j=b+v<b$, then $v\le-1$, and its low two-digit residue lies between $595$ and $838$, outside the weight’s carry-free low support.

Thus its squared weight is divisible by $p^2$:


$$
\boxed{S_t(0,v;A',v')\equiv0\pmod{p^2}.}
\tag{7.9}
$$



### Theorem 7.1 — Complete $K=2$ kernel quotient

In the sufficient box,


$$
\boxed{
S_t(-\sigma n-a,v;-\sigma'n-a',v')
\in
\left\{
0,\ \lambda_{00}T_0,\ \lambda_{01}T_1,\ \lambda_{11}T_2
\right\}
\pmod{841},
}
\tag{7.10}
$$


with $\lambda_{00}\in29\mathbb Z/841\mathbb Z$.

Thus the full box requires **one additional common tail at one-digit precision** beyond the two lifted tails.

This theorem includes all one-carry strata and the no-carry unit corrections. It is not a coefficientwise lift of the modulo-$29$ classification.

---

## 8. Why the additional channel is real

### 8.1 The simplest newly nonzero kernel

For


$$
S_0(-1,-1;-1,-1),
$$


the negative-binomial product is identically $1$ on the original range. Hence this kernel is


$$
\sum_{j=0}^{b-1}\binom{n+2}{j}^{2}.
$$



Its low coefficient is


$$
\lambda_{00}\equiv\binom{2N_0}{N_0}\pmod{841}.
$$


The doubling of


$$
N_0=(2,7,24,7)_{29}
$$


has exactly one carry. Applying the valuation-one unit formula gives


$$
\frac1{29}\binom{2N_0}{N_0}\equiv23\pmod{29}.
$$


Therefore


$$
\boxed{
S_0(-1,-1;-1,-1)\equiv667\,T_0\pmod{841}.
}
\tag{8.1}
$$



### 8.2 Removing the two additional fixed digits from $T_0$

Define


$$
H_m(C)=
\sum_{q=0}^{C}
\binom{2001C+1382}{q}^{2}
\binom{2002C+1382-q}{C-q}^{m}
\pmod{29}.
\tag{8.2}
$$


Then the fixed digits $(B_*)_{0,1}=(0,20)$, $(N_*)_{0,1}=(3,9)$ give


$$
\boxed{
T_0=H_0(C),\qquad
T_1\equiv20H_1(C),\qquad
T_2\equiv6H_2(C)\pmod{29}.
}
\tag{8.3}
$$



For $T_0$, the two digit multipliers are


$$
\binom63\equiv20,\qquad
\binom{18}{9}\equiv16,
$$


whose product is $1\pmod{29}$.

The multipliers $20,6$ for $T_1,T_2$ are the respective nine-term digit sums


$$
\sum_{d=1}^{9}\binom9d^2\binom{29-d}{9}^{m},
\qquad m=1,2.
$$



### 8.3 A phase-compatible bounded counterexample

Take the auxiliary input


$$
\boxed{
C=8,\quad
b=\beta_6+8p^6=5169497484,\quad
n=2001b.
}
\tag{8.4}
$$


This matches the actual seven-digit phase for $u\equiv1\pmod{29}$, because $\delta=8$.

It is an auxiliary integer, **not** the original power $3^{249005515+574312172u}$.

Here


$$
H_0(8)=\sum_{q=0}^{8}\binom{19}{q}^{2}\equiv5\pmod{29}.
$$


Indeed, the sum through $9$ is half of


$$
\binom{38}{19}\equiv0\pmod{29},
$$


and


$$
\binom{19}{9}^{2}\equiv24.
$$



Thus


$$
\boxed{
S_0(-1,-1;-1,-1)\equiv667\cdot5
=812=-29\pmod{841}.
}
\tag{8.5}
$$



This explicitly disproves the unmodified lift of the old zero sector.

### 8.4 A finite rank certificate for the uniform phase quotient

For $C=0,1,2$, direct small sums give


$$
\begin{array}{c|ccc}
C&H_0&H_1&H_2\\ \hline
0&1&1&1\\
1&14&4&7\\
2&23&15&9
\end{array}
\tag{8.6}
$$


whose determinant is $26\ne0\pmod{29}$.

Equivalently, the rows for $(T_0,T_1,T_2)\bmod29$ are


$$
(1,20,6),\quad(14,22,13),\quad(23,10,25),
$$


with determinant $17\ne0$.

These inputs all have the same six fixed digits, and each seventh digit is compatible with an actual $u$-class. Therefore $T_0$ is not a fixed-coefficient linear combination of $T_1,T_2$ over this six-digit phase class.

More precisely, a representation of $29T_0$ by the two lifted tails with coefficients fixed by those six digits would first force both coefficients to be divisible by $29$; division by $29$ would then contradict the displayed rank.

**Scope qualification.** This proves necessity for the uniform six-digit-phase quotient. It does not prove independence after restricting the high parameter to the actual powers, nor exclude a different quotient whose coefficients use additional high information. No such original-orbit reduction has been established here.

### 8.5 A further boundary reduction of the new channel

Since


$$
X=2001C+1382\equiv19\pmod{29},
$$


and


$$
\sum_{d=0}^{28}\binom{19}{d}^{2}
=\binom{38}{19}\equiv0\pmod{29},
$$


the new tail has the exact finite-prefix reduction


$$
\boxed{
H_0(C)
=
\left(\sum_{d=0}^{\delta}\binom{19}{d}^{2}\right)
\binom{2001C_7+69\delta+47}{C_7}^{2}
\pmod{29}.
}
\tag{8.7}
$$



This is a single boundary-binomial observable rather than an original-length sum.

For $u\equiv0\pmod{29}$, $\delta=9$, so the low coefficient is zero. Thus the new channel vanishes at those original residue classes, including $u=0$. For other classes it need not vanish; its boundary binomial remains unevaluated.

---

## 9. The complete short-head contraction still needs only two tails

This is the target-specific improvement over a generic prime-power automaton.

### 9.1 Head paths contain no $\sigma=0$ atoms

For a head input $h$, the accepted finite formula for


$$
\mathsf R\mathsf P_-h
$$


starts with $\sigma=1$ atoms.

The divided-power operation preserves that upper-parameter type. The final upper transform produces:

- $\sigma=2$ main atoms;
- $\sigma=1$ finite-boundary atoms.

The endpoint columns follow the same pattern. The endpoint unit solve forms scalar combinations and introduces no new atom labels.

Therefore, at $K=2$,


$$
\boxed{
A^{-1}h
\text{ uses only }\sigma=1,2\text{ atoms}
}
\tag{9.1}
$$


for the retained short-head inputs.

The actual first force has head length at most $58$ modulo $841$, so this applies to $f^0$.

### 9.2 Full norm/defect quotient

Let


$$
z_f,\ z_0,\ z_1,\ z_\tau
$$


be the complete accepted atom coefficient vectors at precision $841$.

By Theorem 5.1, every pairing involving a $\sigma=2$ atom is zero modulo $841$. The first column has no $\sigma=0$ atoms. Hence there are explicitly assembled low coefficients


$$
a_f,\quad b_f,\quad c_f\pmod{841}
$$


such that


$$
\boxed{\mathcal N\equiv a_fT_2\pmod{841},}
\tag{9.2}
$$


and


$$
\boxed{
\mathcal C-p\rho_n\mathcal N
\equiv b_fT_1+c_fT_2\pmod{841}.
}
\tag{9.3}
$$



The coefficients in (9.3) are assembled from the complete expression


$$
\begin{aligned}
&(r_0-p\rho_nf_0^0)z_0
+(r_1-p\rho_nf_1^0)z_1
+z_\tau,
\end{aligned}
$$


paired with $z_f$, using the actual reconstruction linearization.

The complete terminal terms remain


$$
b^2W_b^2e_\alpha e_\beta,
\qquad
bW_b^2\sum_\alpha z_{f,\alpha}e_\alpha.
\tag{9.4}
$$


They are zero modulo $841$ by the proved bound $v_p(W_b)\ge4$. They have not been omitted at higher precision.

Thus:



$$
\boxed{
\begin{array}{ll}
\text{entire sufficient }K=2\text{ box:}&3\text{ common observables},\\
\text{actual complete short-head norm/defect:}&2\text{ common observables}.
\end{array}
}
\tag{9.5}
$$



The third channel is needed for possible source-source pairings, not for the actual first-column contraction.

### 9.3 A first-order complete-output identity

There is also a useful output-level refinement.

Theorem 5.1 implies


$$
\boxed{
\mathcal R\mathsf R^2\mathsf P_-h\equiv0\pmod{841}
}
\tag{9.6}
$$


for a head of length at most $244$.

Write


$$
\mathsf D=I+p\mathsf D_1\pmod{p^2}.
$$


The complete endpoint correction is zero modulo $p$, so write its actual finite matrix as


$$
\mathsf U\mathsf S_{\rm end}^{-1}\mathsf V
=p\mathsf E_1\pmod{p^2}.
$$


Then


$$
\boxed{
\mathcal RA^{-1}h
\equiv
p\,\mathcal R
\bigl(
\mathsf R\mathsf D_1\mathsf R\mathsf P_-
-\mathsf E_1
\bigr)h
\pmod{p^2}.
}
\tag{9.7}
$$



This retains the complete first endpoint-return digit. It identifies the obstruction to promoting the full short-head output annihilation from depth one to depth two: the two first-order terms in (9.7) must cancel.

I do **not** assert that they do cancel for arbitrary head inputs.

---

## 10. Complete forcing and true norm depth remain unchanged

The actual first force is still


$$
f_i^0=
\frac{(n+i)!}{n!}
[t^n](1+2t+2t^2)^n(1+t)^i.
\tag{10.1}
$$



The complete second force is still


$$
\mathbf r=r_0h^{(0)}+r_1h^{(1)}+\tau,
$$


with both initial charges


$$
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(
T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}
\right),
\qquad i=0,1,
\tag{10.2}
$$


and all source rows


$$
\mathcal H_i=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b},
\qquad1\le i\le b-2.
\tag{10.3}
$$



The factorial subtraction, logarithmic contribution, source-head correction, and terminal return remain present.

The new quotient is only at absolute precision $841$. The actual target is still


$$
\boxed{
\mathcal C-p\rho_n\mathcal N
\equiv0\pmod{p^{d+2}},
\qquad d=v_p(\mathcal N)=2c+4+\nu.
}
\tag{10.4}
$$



An absolute low-digit cancellation does not determine $d$, $\nu$, or the normalized defect. The independent $\rho_n$ must still come from its original definition.

Likewise, logarithmic omission still requires the established guard


$$
\boxed{
N_{\log}\ge c+4+\nu.
}
\tag{10.5}
$$


Until that is certified at the true norm depth, (10.2) must remain complete.

---

## 11. Precision and resource ledger

| Layer | Required precision | Work or remaining input |
|---|---:|---|
| Fixed phase through digit $5$ | $b\bmod29^6$ | Bounded modular exponentiation |
| First variable digit | $b\bmod29^7$ | $\delta=9-u\bmod29$ |
| Valuation-zero binomial units | $29^2$ | Adjacent-digit harmonic correction retained |
| Valuation-one binomial units | $29$ | Multiply by $29$ after unit evaluation |
| Low coefficients $\lambda_{01},\lambda_{11}$ | $29^2$ | At most $4800$ bounded terms each |
| Low coefficient $\lambda_{00}/29$ | $29$ | Same bounded sum, with proved divisibility |
| $T_1,T_2$ | $29^2$ | Genuine original high-tail inputs |
| $T_0$ | $29$ | Reducible to the boundary binomial in (8.7) |
| Atom/source/end coefficients | $29^2$ | Complete accepted construction; high inputs still required |
| Actual alignment | $29^{d+2}$ | Not reached |

The low binomials have bounded upper indices below roughly $1.1$ million and at most five base-$29$ digits. They can be evaluated by unit-factorial tables and exact valuations; no large integer binomial need be constructed.

For inherited small-index atom generation, the former sufficient scalar guard is


$$
v_{29}((3R_*+3)!)=v_{29}(735!)=25.
$$


It is an independent scalar-generation guard, not a cumulative loss. Exact valuation/unit generation can instead keep fixed unit precision.

No original digit scan is authorized or required by these statements. In particular, a small formal state count does not make the original $81$-million-digit input available.

---

## 12. Genuinely new bounded arithmetic

The coordinator’s five earlier phase-kernel checks, five small tail controls, and fresh parameter tests should proceed independently. Nothing below requests their repetition.

### 12.1 Phase certificate

Check


$$
\operatorname{powmod}(3,249005515,29^7)=5764320805,
$$


and


$$
\operatorname{powmod}(3,574312172,29^7)
\equiv1+15\cdot29^6\pmod{29^7}.
$$



Expected output:

- digits $(27,28,5,28,0,20,9)$ for the first value;
- the exact affine rule $\delta(u)=9-u\bmod29$;
- the affine constants in (2.6)–(2.10).

Only fixed-size modular arithmetic is involved.

### 12.2 New prefix and rank controls

Use


$$
b_C=410910916+594823321C,\qquad n_C=2001b_C,
$$


for


$$
C\in\{0,1,2,8\}.
$$



Expected values for the complete original-prefix kernel are


$$
\boxed{
\begin{array}{c|c}
C&S_0(-1,-1;-1,-1)\bmod841\\ \hline
0&667\\
1&87\\
2&203\\
8&812
\end{array}
}
\tag{12.1}
$$



For $C=0,1,2$, independently check the tail residues


$$
\boxed{
\begin{array}{c|ccc}
C&T_0&T_1\bmod29&T_2\bmod29\\ \hline
0&1&20&6\\
1&14&22&13\\
2&23&10&25
\end{array}
}
\tag{12.2}
$$


and determinant $17\pmod{29}$.

### 12.3 A modest independent full-prefix evaluator

For these new prefix controls, no enumeration of $j<b_C$ is needed.

Because the weight is squared, retain only carry-free weight digits


$$
0\le d_i\le N_i.
$$


Use a digit DP storing:

- the borrow in $(b_C-1)-j$;
- the previous chosen digit $d_{i-1}$;
- an ordinary product accumulator modulo $841$;
- a harmonic-correction accumulator modulo $29$.

When digit $d_i$ is selected, apply the completed correction for digit $i-1$:


$$
2\left[
N_iH_{N_{i-1}}
-d_iH_{d_{i-1}}
-(N_i-d_i)H_{N_{i-1}-d_{i-1}}
\right].
\tag{12.3}
$$


The local ordinary factor is


$$
\binom{N_i}{d_i}^{2}\pmod{841}.
$$


Accept only final cutoff borrow zero, with a padded zero digit to complete the last correction.

This is an independent application of (3.2) to the **entire original prefix**.

There are at most $58$ formal states and at most $29$ candidate edges per state per digit. The displayed auxiliary inputs need fewer than ten digits. Thus each prefix test uses fewer than


$$
10\cdot58\cdot29=16820
$$


candidate edges, plus small tables. A budget below $10^6$ small modular operations and below one MiB of residue storage is ample for the displayed new controls.

These calculations establish only the stated finite identities and the phase-class rank obstruction.

---

## 13. Concrete next lemma

The next useful target is no longer a generic large-state prime-power automaton.

> **Complete first-order short-head return lemma.**  
> Evaluate, or prove a target-specific relation for,
> 

$$
> \mathcal R
> \bigl(
> \mathsf R\mathsf D_1\mathsf R\mathsf P_-
> -\mathsf E_1
> \bigr)h
> \pmod{29}
>
$$


> on the actual first-force head, with the complete endpoint return retained; then propagate the resulting normalized output information together with both complete second-force charges and the source.
>
> The required result must identify a nonzero norm digit or prove a further annihilation depth. It must not infer norm-relative alignment from the absolute congruence alone.

In parallel, a compressed evaluation theorem for $T_1,T_2\bmod841$ remains necessary unless the complete scalar coefficients in (9.3) annihilate those observables identically. Equations (9.2)–(9.3) give the exact two-dimensional scalar target for that question.

---

## 14. Final gcd, actual denominator, and whole error

No row content, corrected column, or lattice normalization has changed.

Retain the least actual two-column clearer $d_B$, the actual weighted integer Gram pair


$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$


and the all-prime reduction


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
}
\tag{14.1}
$$



The primitive multiplier remains $d_B^2/g_B$. The actual denominator remains


$$
\boxed{
\log q_n
=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{14.2}
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
\tag{14.3}
$$



The retained signed-error asymptotic does not become an irrationality proof until this actual primitive denominator is controlled strongly enough to make the whole nonzero form tend to zero.

---

## Proof-status ledger

| Statement | Status |
|---|---|
| Complete finite atom factorization and source subtraction | Reused at accepted scope |
| Fixed-unit-precision correction | Reused from A4 Turn 2 |
| Six fixed phase digits and first variable digit | Explicit arithmetic derivation |
| Carry/unit formula used at $29^2$ | Derived from unit factorials |
| Original cutoff preserved by the four-digit split | Proved |
| Weighted $\sigma=2$ atoms vanish modulo $841$ | Proved pointwise |
| Full $K=2$ box factors through $T_0,T_1,T_2$ | Proved |
| Only one-digit precision is needed for $T_0$ | Proved |
| Uniform six-digit-phase two-tail closure fails | Proved by finite rank certificate |
| Actual-orbit minimality of three channels | Not asserted |
| Complete short-head norm/defect still uses only $T_1,T_2$ | Proved |
| Complete first-order output identity, including endpoint return | Proved |
| Actual $T_1,T_2\bmod841$ | Not evaluated |
| New bounded checks | Specified with hand-derived expected output; not executed |
| True norm-relative alignment | Open |
| All-prime denominator/whole-error comparison | Open |
| Irrationality of $e+\pi$ | Unresolved |

## Conclusion

The modulus-$841$ lift is substantially smaller than a generic prime-power state construction.

For the full sufficient kernel box,


$$
\boxed{
\text{two lifted tails at precision }841
\;+\;
\text{one additional tail at precision }29
}
$$


suffice. The new channel is real for the uniform phase class and can itself be reduced to a boundary binomial.

For the **actual complete short-head norm and source-plus-end defect**, that extra channel does not occur:


$$
\boxed{
\mathcal N\equiv a_fT_2,\qquad
\mathcal C-29\rho_n\mathcal N\equiv b_fT_1+c_fT_2
\pmod{841}.
}
$$



The main new mechanism is the use of the actual fifth and sixth fixed digits to force a second carry in every weighted $\sigma=2$ atom. The main remaining local bottleneck is the complete first-order return and the evaluation or annihilation of the two surviving tails at the **true norm-sensitive precision**.

Even that local resolution would leave the all-prime final gcd, actual primitive denominator, and whole same-index error to be controlled. Therefore


$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


