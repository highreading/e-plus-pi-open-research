> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5: the binary next-digit defect cancels on the original pair class

I prove


$$
\boxed{\Delta=0\pmod2\qquad(r\equiv2\pmod{16}).}
$$



The cancellation does **not** require $b=81$, a unit norm, or a projection involving division by $6$. The unrestricted higher digits enter an explicit binomial coefficient. Its contribution is identical at the two members of each pair and therefore cancels.

There are two essential parts:

1. The off-pair term vanishes:
   

$$
\boxed{\xi^Tz=0\pmod2.}
$$


2. After bounded signed-polynomial closure, the difference between the two columns at a paired coordinate is governed by one fixed binary constant and one binomial coefficient. The same expression occurs at both paired coordinates.

I also give a complete one-step lift on $r\equiv18\pmod{32}$, with the necessary increased precision and **seven**, rather than five, residual boundary inputs. I do not evaluate that further lifted defect, and I do not obtain the sufficient all-depth bound $\gamma-\alpha\le2000b+o(n)$.

No conclusion about the rationality of $e+\pi$ follows.

---

## 1. Domain and actual quantities

Throughout the main proof,


$$
b=9^r,\qquad n=4002b,\qquad r\ge1,\qquad r\equiv2\pmod{16}.
$$


Put


$$
h=\frac n2,\qquad
R=2^h\binom{2h}{h},\qquad
\lambda=\frac{(n!)^2}{2^n}.
$$



The actual weighted columns and metric remain


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},
$$




$$
W_j=\binom{n+2}{j},\qquad
\omega_j=j!W_j=(n+2)_{\underline j},\qquad
\Omega=\operatorname{diag}(\omega_j^2).
$$


All weighted coordinates have indices $0\le j\le b$. Every contact inverse below has dimension exactly $b$, with indices $0\le i,j<b$.

Write


$$
\alpha=v_2(X^TX),\qquad \gamma=v_2(X^TY).
$$


The norm is positive. The supplied original-family ternary result retains nonvanishing of the complete mixed contraction, so both valuations are finite.

Use the integer parameters


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532.
$$


Thus


$$
h=64C+33,\qquad \frac{b-1}{4}=32D+20.
$$



I reuse the established first-column support:


$$
X_{128t}\equiv X_{128t+64}\equiv e_t\pmod2,
\qquad 0\le t\le D,
$$


where


$$
e_t=
\binom Ct\binom{2C+1+D-t}{D-t}\pmod2,
$$


and $X$ is even elsewhere.

Let $e$ denote the corresponding $0$-$1$ vector. As in the question, write


$$
X=e+2\xi,\qquad Y=e+z+2\upsilon\pmod4,
$$


where $z$ is the $0$-$1$ parity vector of $Y-e$. The defect is


$$
\Delta=e^T(\xi+\upsilon)+\xi^Tz\pmod2.
$$



---

## 2. Bounded integral closure and exact precision

This section specializes the supplied signed-Newton closure; its existence is not claimed as new.

For an integer-valued polynomial $f$, write


$$
(\mathcal S_bf)_i=(-1)^if(i),\qquad 0\le i<b.
$$


Let $\mathscr L_{s,b}$ be the finite signed-Newton operator


$$
\begin{aligned}
\mathscr L_{s,b}\binom Xr
={}&(-1)^s\binom Xs\binom{X-s}{r}\\
&+\sum_{v=1}^s(-1)^{s-v}\binom X{s-v}\binom nv
 \sum_{a=0}^r
 \binom{X-s+v}{r-a}
 \binom{v+a-1}{a}
 \binom{b-1-X+s}{v+a}.
\end{aligned}
\tag{2.1}
$$


Define


$$
\mathscr E=\sum_{s=1}^4c_s\mathscr L_{s,b},
\qquad (c_1,c_2,c_3,c_4)=(-1,2,-3,3).
$$



The finite identity is


$$
E\mathcal S_bf=\mathcal S_b(\mathscr Ef).
\tag{2.2}
$$


In particular, it is the actual finite $E$, not an infinite inverse.

The finite summation behind (2.1) is


$$
\sum_{u=0}^{L}
 \binom{u+v-1}{v-1}\binom ua
=
\binom{v+a-1}{a}\binom{L+v}{v+a}.
$$


It gives


$$
\deg(\mathscr Ef)\le\deg f+4.
\tag{2.3}
$$


Every expression in (2.1) is integer-valued on the integers, so its Newton coefficients are integral finite differences. There is no binary denominator loss in this closure.

### Complete inputs at the present precision

The complete contact modulo $16$ has only $s=0,\ldots,4$. The complete divided residual has the five factorial tails $b,\ldots,b+4$. The whole logarithmic forcing vanishes modulo $16$ after division by $b!$, by the supplied bound


$$
v_2(h_i^F/b!)
\ge h+1-2\lfloor\log_2(2n+b-1)\rfloor-v_2(b!).
\tag{2.4}
$$


On the present domain $b\ge81$, this is well beyond the precisions used here.

The five boundary values are


$$
(B_0,B_1,B_2,B_3,B_4)\equiv(5,10,6,8,8)\pmod{16}.
\tag{2.5}
$$



Put


$$
g(X)=2-X+3\binom X2-\binom X3
       +4\binom X4-4\binom X5,
$$




$$
t(X)=-6-6X+15\binom X3.
$$


Thus the signed boundary vector from the supplied five-boundary reduction is $\mathcal S_bt$.

The needed polynomial representatives are


$$
P=(I-2\mathscr E+4\mathscr E^2)g\pmod8,
\tag{2.6}
$$




$$
Q=2(I-2\mathscr E+4\mathscr E^2)t\pmod{16}.
\tag{2.7}
$$


They satisfy


$$
\boxed{\deg P\le13,\qquad \deg Q\le11.}
\tag{2.8}
$$


Thus the present calculation uses Newton spaces of dimensions at most $14$ and $12$. If the $P$-column is retained one raw bit further, its cubic inverse term gives degree at most $17$.

The actual solutions are


$$
\theta^P=T(-2n)\mathcal S_bP\pmod8,
\tag{2.9}
$$




$$
\eta_i=
-\sum_{a=0}^4B_a\binom{-2n}{b+a-i}
+\bigl(T(-2n)\mathcal S_bQ\bigr)_i
\pmod{16}.
\tag{2.10}
$$


Formula (2.10) retains all five exterior inputs and the correction produced by the actual finite inverse. The original cubic inverse has been combined into the boundary equation before truncation.

Extend $\theta^P,\eta$ by zero at $-1,b$. The actual coordinates are


$$
2X_j\equiv W_j(j\theta^P_{j-1}-\theta^P_j)\pmod8,
\tag{2.11}
$$




$$
4Y_j\equiv W_b\mathbf1_{j=b}
 +W_j(j\eta_{j-1}-\eta_j)\pmod{16}.
\tag{2.12}
$$


These precisions give $X,Y\bmod4$, exactly what $\Delta$ requires.

---

## 3. The off-pair contribution is zero

The new point here is a whole-support assertion, not merely parity agreement on the selected pairs.

### 3.1 $X_j$ is divisible by $4$ at every odd coordinate

Modulo $2$, the inverse correction disappears and


$$
g(i)\equiv
\begin{cases}
0,&i\equiv0\pmod4,\\
1,&i\equiv1,2,3\pmod4.
\end{cases}
$$


Since $2n=4h$,


$$
(1+z)^{-2n}\equiv(1+z^4)^{-h}\pmod2.
$$


Put $M=(b-1)/4$. For $a=1,2,3$,


$$
\theta^P_{4k+a}
\equiv
\binom{h+M-k-1}{M-k-1}\pmod2,
\qquad
\theta^P_{4k}\equiv0\pmod2.
\tag{3.1}
$$



For $j\equiv3\pmod4$, the two terms in
$j\theta^P_{j-1}-\theta^P_j$ cancel modulo $2$.

For $j=4k+1$, the only case needing attention is $W_j/4$ odd. Indeed,


$$
v_2(W_j)\ge2
$$


for odd $j$, and


$$
W_j/4\ \text{odd}
\Longrightarrow
\binom{n+1}{j-1}\ \text{odd}.
$$


Because $n+1\equiv3\pmod8$, Lucas forces $k$ even. But $M$ is even and $h$ is odd, so $M-k-1$ is odd. The binomial in (3.1) is then even by its lowest binary digit. Thus the reconstruction difference is even in this case as well.

Consequently,


$$
\boxed{X_j\equiv0\pmod4\quad\text{for every odd }j<b.}
\tag{3.2}
$$



At the endpoint,


$$
v_2(W_b)
=2+v_2\binom{n+1}{b-1}\ge3:
$$


the low digits $n+1\equiv67\pmod{128}$ do not contain those of
$b-1\equiv80\pmod{128}$. Therefore $X_b\equiv0\pmod4$ too.

### 3.2 The even-coordinate parity of $Y$

Here is a useful general reduction of the complete $\eta\bmod8$.

For $0\le j<b$, put


$$
L=b-1-j,\qquad
M_v=\binom{2n+L}{L-v}.
$$


Finite moment summation in (2.10), using the established
$E\mathcal S_bt\equiv0\pmod2$, gives


$$
\boxed{
\eta_j\equiv(-1)^j
\left[
M_{-1}+2M_{-2}+6M_{-3}
+\left(4(1+j)+6\binom j3\right)M_0
+4jM_2
\right]\pmod8.
}
\tag{3.3}
$$


For clarity, the moment identity used here is


$$
\sum_{k=0}^L
 \binom{2n+k-1}{k}\binom kv
=
\binom{2n+v-1}{v}\binom{2n+L}{L-v}.
$$


Thus (3.3) still concerns the complete residual and its finite boundary.

Modulo $2$, (3.3) says that $\eta_j$ can be odd only for
$j\equiv1\pmod4$.

If $j\equiv2\pmod4$, (3.3) modulo $4$ gives


$$
\eta_j/2\equiv\eta_{j-1}\pmod2.
$$


Since $W_j$ is even, this proves $Y_j$ even.

If $j=4k$, set $\ell=M-k$, so $L=4\ell$. The first three terms in (3.3) show


$$
4\mid\eta_{4k},\qquad
\frac{\eta_{4k}}4\equiv\binom{h+\ell}{\ell}\pmod2.
\tag{3.4}
$$


Indeed, the divided contributions from $M_{-1}$ and $2M_{-2}$ have the same parity and cancel; $6M_{-3}$ vanishes after division by $4$. Also $j\eta_{j-1}\equiv0\pmod8$. Hence


$$
Y_{4k}\equiv
\binom{32C+17}{k}
\binom{h+M-k}{M-k}\pmod2.
\tag{3.5}
$$



The first binomial permits only


$$
k\equiv0,1,16,17\pmod{32}.
$$


The second requires $k$ even, because $h$ is odd and $M$ is even. Thus


$$
\boxed{
Y_j\text{ can be odd at an even }j
\text{ only if }j\equiv0,64\pmod{128}.
}
\tag{3.6}
$$


At these coordinates its parity is the established $e_t$.

Finally, $W_b\in8\mathbb Z_2$ makes the complete endpoint $Y_b$ even, including its $W_be_b$ term.

It follows that $z$ is supported only at odd coordinates. By (3.2),


$$
\boxed{\xi^Tz=0\pmod2.}
\tag{3.7}
$$



This removes the off-pair obstruction completely at this digit.

---

## 4. Removing all growing matrices from the paired discrepancy

For $j\equiv0\pmod{64}$, define


$$
H_j=\eta_j-2\theta^P_j\pmod{16}.
\tag{4.1}
$$


At such a nonterminal coordinate, the $j\theta_{j-1}$ terms vanish at the required precision, so


$$
X_j-Y_j\equiv \frac{W_jH_j}{4}\pmod4.
\tag{4.2}
$$



### 4.1 The closure polynomials have fixed coefficients on this class

In the polynomial operations (2.6)–(2.7), we may replace


$$
(n,b)\quad\text{by}\quad(2,81)
$$


at the stated coefficient precisions.

This is only a substitution in the **bounded polynomial operators**, not in the large binomial kernels. Indeed,


$$
v_2(n-2)\ge6,\qquad v_2(b-81)\ge7.
$$


For lower index $1\le a\le13$,


$$
v_2\!\left(\binom{x+\delta}{a}-\binom xa\right)
\ge v_2(\delta)-\lfloor\log_2a\rfloor.
\tag{4.3}
$$


In (2.1), the lower indices involving $n$ are at most $4$, and those involving $b$ are at most $13$. This gives more than the needed precision. Passing from values to Newton coefficients uses integral finite differences.

Henceforth let $\mathscr E_0$ denote the operator with $n=2,b=81$, and take the integer-valued polynomials


$$
P=g-2\mathscr E_0g+4\mathscr E_0^2g,\qquad
Q=2t-4\mathscr E_0t+8\mathscr E_0^2t.
$$


Write


$$
P=\sum_{r=0}^{13}p_r\binom Xr,\qquad
Q=\sum_{r=0}^{11}q_r\binom Xr,
\qquad d_r=q_r-2p_r,
\tag{4.4}
$$


with missing coefficients zero.

All $d_r$ are even. The degree bounds immediately give


$$
4\mid d_4,\qquad 4\mid d_8,\qquad 8\mid d_{12}.
\tag{4.5}
$$



We also need


$$
\boxed{d_0\equiv0\pmod{16}.}
\tag{4.6}
$$


Here is a direct check. At $n=2,b=81$,


$$
(\mathscr E_0 f)(0)=2\sum_{\ell=0}^{80}\ell f(\ell).
\tag{4.7}
$$


For $f=g$, its parity is $0,1,1,1$ periodically modulo $4$; the sum on the right is even. Also $(\mathscr E_0^2g)(0)$ is even by (4.7). Thus $p_0\equiv2\pmod8$.

For $f=t$, its parity is $\binom{\ell}{3}$, and the relevant odd positions are $3,7,\ldots,79$, twenty positions. Thus $4\mid(\mathscr E_0t)(0)$, while $(\mathscr E_0^2t)(0)$ is even. Therefore $q_0\equiv-12\equiv4\pmod{16}$, proving (4.6).

### 4.2 One fixed integer-valued polynomial

Define


$$
\boxed{
\begin{aligned}
\mathcal H(L)={}&
\sum_{a=0}^4(-1)^aB_a\binom{L+a+4}{3}\\
&+\sum_{r=0}^{13}
d_r\binom{r+3}{3}\binom{L+4}{r+4},
\end{aligned}}
\tag{4.8}
$$


using the integer representatives in (2.5). Its degree is at most $17$.

This fixed polynomial contains:

* all five boundary values;
* both actual inverse corrections;
* the full $P$-forcing at its required precision.

To see why it controls the actual kernels, use


$$
\begin{aligned}
&\sum_{\ell=j}^{b-1}
 \binom{-2n}{\ell-j}(-1)^\ell\binom{\ell}{r}\\
&\quad=(-1)^j
 \sum_{a=0}^r
 \binom j{r-a}
 \binom{2n+a-1}{a}
 \binom{2n+b-1-j}{b-1-j-a}.
\end{aligned}
\tag{4.9}
$$


If $64\mid j$, every term with $r-a>0$ vanishes modulo $8$; the $Q$-coefficients have an additional factor $2$. Also


$$
\binom{2n+r-1}{r}\equiv\binom{r+3}{3}\pmod{16},
\qquad r\le13.
$$


Consequently (4.8) is the reference coefficient sequence after the common large kernel has been extracted.

The remaining large factor is not set to one:


$$
2n-4=128(2C+1).
$$


The binary power congruence gives


$$
(1-z)^{-128(2C+1)}
\equiv(1-z^{16})^{-8(2C+1)}\pmod{16}.
\tag{4.10}
$$


The boundary terms may be represented by Laurent shifts down to degree $-5$. Since (4.10) shifts only by multiples of $16$, none of these negative degrees enters a nonnegative multiple-of-$16$ coefficient.

Thus, if $L=b-1-j=16m$,


$$
\boxed{
H_j\equiv
\sum_{v=0}^{m}
 \binom{16C+8+v-1}{v}\,
 \mathcal H(16(m-v))
\pmod{16}.
}
\tag{4.11}
$$


All unrestricted higher digits are retained in this binomial convolution.

---

## 5. The sampled polynomial has only one possible binary coefficient

The key simplification is


$$
\boxed{\mathcal H(16m)\equiv8\kappa m\pmod{16}}
\tag{5.1}
$$


for one constant $\kappa\in\{0,1\}$, independent of $C,D,m$.

Its value is unnecessary for the scalar cancellation.

### Proof

First consider the boundary part of (4.8). Vandermonde gives


$$
\binom{16m+a+4}{3}
=\sum_{i=0}^3\binom{16m}{i}\binom{a+4}{3-i}.
$$


The constant sum is


$$
5\binom43-10\binom53+6\binom63
 -8\binom73+8\binom83=208\equiv0\pmod{16}.
$$


The $i=1,3$ terms vanish modulo $16$. For $i=2$, the remaining coefficient is


$$
5\cdot4-10\cdot5+6\cdot6-8\cdot7+8\cdot8=14,
$$


which is even, while $8\mid\binom{16m}{2}$. Hence the entire boundary part vanishes modulo $16$.

For the second part, set $N=16m+4$ and $k=r+4$. The identity


$$
\binom{k-1}{3}\binom Nk
=\frac{N(N-1)(N-2)(N-3)}{6k}\binom{16m}{k-4}
\tag{5.2}
$$


shows that for $5\le k\le17$, $4\nmid k$, the product is divisible by $16$. Indeed,


$$
v_2\binom{16m}{k-4}\ge4-v_2(k-4),
$$


and $v_2(k-4)=v_2(k)\le1$. The case $m=0$ is immediate from the zero-binomial convention.

The $k=4$ term vanishes by (4.6). Only $k=8,12,16$ remain. By (4.5),


$$
\begin{aligned}
\mathcal H(16m)\equiv{}&
35d_4\binom{16m+4}{8}
+165d_8\binom{16m+4}{12}\\
&+455d_{12}\binom{16m+4}{16}
\pmod{16}.
\end{aligned}
$$


Binary Vandermonde and Lucas give


$$
\binom{16m+4}{8}\equiv
\binom{16m+4}{12}\equiv2m\pmod4,
$$




$$
\binom{16m+4}{16}\equiv m\pmod2.
$$


Therefore (5.1) holds, with


$$
\kappa\equiv
\frac{d_4}{4}+\frac{d_8}{4}+\frac{d_{12}}8
\pmod2.
$$


Every displayed quotient is an exact integer. ∎

---

## 6. Evaluation of the defect

Because (5.1) has a factor $8$, only the parity of the convolution kernel in (4.11) matters. Over $\mathbb F_2$,


$$
(1-z)^{-(16C+8)}=(1-z^8)^{-(2C+1)}.
$$


Consequently,


$$
\boxed{
\frac{H_j}{8}
\equiv
\kappa\,(m\bmod2)
\binom{2C+\lfloor m/8\rfloor+1}{\lfloor m/8\rfloor}
\pmod2.
}
\tag{6.1}
$$


In particular, $8\mid H_j$ at every coordinate $j\equiv0\pmod{64}$.

For a pair $j=128t,128t+64$, put $d=D-t$. The two values of $m$ are respectively


$$
m=8d+5,\qquad m=8d+1.
$$


Both are odd and have the same quotient $\lfloor m/8\rfloor=d$. Thus


$$
\frac{H_{128t}}8
\equiv
\frac{H_{128t+64}}8
\equiv
\kappa\binom{2C+d+1}{d}\pmod2.
\tag{6.2}
$$



The weights also have the same parity:


$$
W_{128t}\equiv W_{128t+64}\equiv\binom Ct\pmod2.
$$


Using (4.2),


$$
\boxed{
\frac{X_{128t}-Y_{128t}}2
\equiv
\frac{X_{128t+64}-Y_{128t+64}}2
\equiv\kappa e_t\pmod2.
}
\tag{6.3}
$$



On a selected coordinate $e_j=1$,


$$
\xi_j+\upsilon_j\equiv\frac{X_j-Y_j}{2}\pmod2.
$$


Equation (6.3) therefore makes the two contributions of each pair cancel. Together with (3.7),


$$
\boxed{
e^T(\xi+\upsilon)=0,\qquad
\xi^Tz=0,\qquad
\Delta=0\pmod2.
}
\tag{6.4}
$$



This is the desired infinite-class evaluation. It is independent of the value of $\kappa$ and independent of the finite $b=81$ certificate.

In particular,


$$
\boxed{
\frac{X^TY}{2}\equiv
\frac{X^TX}{2}\equiv
\binom{C+D+1}{D}\pmod2.
}
\tag{6.5}
$$


The previously established carry criterion therefore applies to both:


$$
D\mathbin{\&}(C+1)=0
\quad\Longleftrightarrow\quad
\alpha=\gamma=1.
\tag{6.6}
$$


When the carry test fails, the conclusion is only $\alpha,\gamma\ge2$, not equality of their deeper valuations.

---

## 7. One further lift on $r\equiv18\pmod{32}$

Now restrict to


$$
r\equiv18\pmod{32}.
$$


Then $D$ is odd, so the established norm obstruction and (6.5) give


$$
\boxed{\alpha\ge2,\qquad\gamma\ge2.}
\tag{7.1}
$$



The next layer requires $X,Y\bmod8$, not merely modulo $4$.

### 7.1 Complete precision and the enlarged boundary

Here $h\equiv1\pmod{32}$, and in the integral divided-power ring


$$
(1+2U)^h\equiv1+2U\pmod{32}.
$$


Thus contact degrees $s\le4$ still suffice.

The normalized central sums give, modulo $16$,


$$
f^0/R\equiv(2,9,3,9,12,4,0,\ldots).
\tag{7.2}
$$


One way to check the precision is to use the supplied normalized central formulas: $B_\ell$ for $\ell\ge3$ contains $h-1$, hence is divisible by $32$; $B_0,B_1,B_2\equiv2,3,3\pmod{16}$. The remaining factorial products vanish modulo $16$ from forcing index $6$ onward.

Accordingly, use


$$
g_{16}(X)=
2-9X+3\binom X2-9\binom X3
 +12\binom X4-4\binom X5
\pmod{16},
$$


and


$$
P^{+}=(I-2\mathscr E+4\mathscr E^2-8\mathscr E^3)g_{16}
\pmod{16}.
\tag{7.3}
$$


Thus


$$
\deg P^{+}\le17.
$$



For the $Q$-column modulo $32$, the five old tails are insufficient:


$$
v_2((b+5)!/b!)=4,\qquad
v_2((b+6)!/b!)=4.
$$


Both new tails must be retained. The tail starting at $b+7$ vanishes modulo $32$. Hence there are seven boundary inputs, $b,\ldots,b+6$.

Their boundary values are


$$
\boxed{
(B_0^+,\ldots,B_6^+)
\equiv(5,10,22,24,24,16,16)\pmod{32}.
}
\tag{7.4}
$$


They follow directly from


$$
B_a^+=\sum_{u=a}^{6}\frac{(b+u)!}{b!}\binom{2n}{u-a}.
$$



Let $a^+(X)$ be the signed boundary polynomial determined by


$$
\sum_{a=0}^6E_{i,b+a}B_a^+=(-1)^i a^+(i)\pmod{16}.
$$


Its degree is at most $3$. Then


$$
Q^{+}=2(I-2\mathscr E+4\mathscr E^2-8\mathscr E^3)a^+
\pmod{32},
\tag{7.5}
$$


has degree at most $15$.

Thus the further lift needs Newton spaces of dimensions at most $18$ and $16$. The complete logarithmic forcing still vanishes by (2.4), now at precision $32$.

### 7.2 Exact next scalar, retaining the division loss

Compute


$$
\theta^{P,+}=T(-2n)\mathcal S_bP^+\pmod{16},
$$




$$
\eta_i^+=-\sum_{a=0}^6B_a^+\binom{-2n}{b+a-i}
 +(T(-2n)\mathcal S_bQ^+)_i\pmod{32}.
$$


Retain the endpoint and define


$$
A_j^+=W_j(j\theta^{P,+}_{j-1}-\theta^{P,+}_j),
$$




$$
B_j^{+,{\rm act}}
=W_b\mathbf1_{j=b}+W_j(j\eta^+_{j-1}-\eta^+_j).
$$


Then


$$
A_j^+\equiv2X_j\pmod{16},\qquad
B_j^{+,{\rm act}}\equiv4Y_j\pmod{32}.
$$



The next two digits are exactly


$$
\frac{X^TX}{4}
\equiv\frac1{16}\sum_j(A_j^+)^2\pmod2,
$$




$$
\frac{X^TY}{4}
\equiv\frac1{32}\sum_jA_j^+B_j^{+,{\rm act}}\pmod2.
$$


Thus the next possible discrepancy is


$$
\boxed{
\Delta_2=
\frac{
\sum_jA_j^+B_j^{+,{\rm act}}
-2\sum_j(A_j^+)^2
}{32}\pmod2.
}
\tag{7.6}
$$


The numerator is evaluated modulo $64$. The raw precisions $16$ and $32$ suffice because errors multiply coordinates divisible by $4$ and $2$, respectively.

The division by $32$ is legitimate by (7.1). I do **not** evaluate $\Delta_2$ here or claim that this additional digit aligns.

---

## 8. Final gcd, primitive denominator, and whole real error

The actual center remains


$$
c_n=\frac{2b!}{\lambda R}\frac{X^TY}{X^TX}.
$$


Retain the least actual two-column denominator and the final metric-dependent gcd:


$$
N_B=d_B[u,v],\qquad
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad q_n=\frac{A_B}{g_B}>0.
$$


Thus $q_n$, not a raw determinant or column clearer, is the primitive multiplier.

With $s=s_2(n)$,


$$
v_2(g_B)=
\min\left\{
3n-2s+2+\alpha,\,
\frac{3n}{2}-s+v_2(b!)+3+\gamma
\right\},
$$




$$
\boxed{
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s-1-(\gamma-\alpha)
\right\}.
}
\tag{8.1}
$$



The new alignment proves neither an all-depth equality nor


$$
\gamma-\alpha\le2000b+o(n).
$$


That sufficient relative-bound goal remains open.

For the supplied whole signed-error theorem on this fixed-ratio family,


$$
\epsilon_n=c_n-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The actual primitive evaluated form is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n>0}
\quad\text{eventually}.
$$


This retains the complete exponential residual, logarithmic forcing, endpoint, and nonvanishing.

### Scope of the supplied $b=729$ control

The supplied original computation gives


$$
X^TX\equiv2736,\qquad X^TY\equiv1552\pmod{4096},
$$


hence $\alpha=\gamma=4$, with


$$
v_2(q_n)=4375455,\qquad v_2(g_B)=4376909.
$$


This is finite evidence at $r=3$, outside the class proved above. It was not used to prove (6.4). Its complete-forcing depth $1457963$, original inverse, and certified omitted tails remain part of that finite certificate.

---

# Concluding ledger

## (1) New result and proof status

**Proved on the original class $r\equiv2\pmod{16}$:**


$$
\boxed{\Delta=0.}
$$



More specifically:

- $X_j\equiv0\pmod4$ at every odd coordinate.
- The even-coordinate parity of $Y$ is supported only on the prescribed pairs.
- Consequently $\xi^Tz=0$.
- The growing inverse is removed using degree-$13$ and degree-$11$ signed polynomials.
- The paired discrepancy reduces to the fixed sampled polynomial
  $\mathcal H(16m)=8\kappa m\pmod{16}$.
- Binary convolution evaluates its unrestricted higher-digit dependence, and the two members of each pair cancel.
- Therefore both next contraction digits equal
  

$$
\binom{C+D+1}{D}\pmod2.
$$



**Also proved:** a complete bounded one-step lift on $r\equiv18\pmod{32}$, with raw precisions $16,32$, seven boundary inputs, endpoint, and exact lifted defect (7.6).

**Not proved:** evaluation of $\Delta_2$, the sufficient relative-depth bound, or irrationality/rationality of $e+\pi$.

## (2) Exact remaining bottleneck

On $r\equiv18\pmod{32}$, both contractions now have proved depth at least $2$. The immediate arithmetic question is the value of the complete lifted scalar $\Delta_2$ in (7.6).

Beyond that digit, the substantive goal remains


$$
\boxed{\gamma-\alpha\le2000b+o(n),}
$$


not uniform units or an unsupported subtraction of valuation lower bounds.

## (3) Bounded computation request

An independent audit can be confined to the **fixed polynomial certificate**, without another growing-matrix calculation.

**Inputs**


$$
n_{\rm ref}=2,\qquad b_{\rm ref}=81,
$$


the operator (2.1), and the explicit polynomials $g,t$ above.

**Expected verifiable output**

1. Compute the Newton coefficients of
   

$$
P=g-2\mathscr E_0g+4\mathscr E_0^2g\pmod8,
$$


   

$$
Q=2t-4\mathscr E_0t+8\mathscr E_0^2t\pmod{16}.
$$


2. Verify
   

$$
d_0=0\pmod{16},\quad
   4\mid d_4,d_8,\quad8\mid d_{12}.
$$


3. Report
   

$$
\kappa=\frac{d_4}{4}+\frac{d_8}{4}+\frac{d_{12}}8\pmod2.
$$


4. Check the sixteen bounded residues
   

$$
\boxed{\mathcal H(16m)\equiv8\kappa m\pmod{16},
   \qquad 0\le m<16.}
$$



This is an audit of a proved fixed-polynomial identity. The infinite cancellation proof does not depend on the computed value of $\kappa$, and these sixteen evaluations are not being offered as a substitute for that proof.
