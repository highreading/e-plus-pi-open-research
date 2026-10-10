> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5: explicit mixed-digit carries, the sharp loss threshold, and a separate CRT-selected unit lemma

There is still no decision about the rationality of $e+\pi$.

I obtain three new results:

1. **An explicit binomial-sum formula for the actual mixed digit**, eliminating the unspecified $\eta_{8k}/4$ coordinates. It includes the residual’s Newton transform in closed form and the contact-inverse carries. A companion formula evaluates the complete mixed contraction modulo $4$, including the endpoint.

2. **The exact critical linear loss** in
   

$$
\gamma-\alpha
   =v_2(X^TY)-v_2(X^TX)
$$


   for the fixed coefficient-$4002$ family. In particular,
   

$$
\gamma-\alpha\le 2000b+o(n)
$$


   would already suffice for the same-center $3+2$ denominator lower rate to exceed the supplied signed-error rate. Units are therefore much stronger than necessary.

3. **A proved, separate CRT-selected arithmetic lemma:** if $h=n/2$ is sufficiently close to $1$ in $\mathbb Z_2$, then the *actual complete* mixed contraction is a unit, not merely the norm. I prove this by evaluating a reference calculation at $n=2$, including its finite-boundary inverse carry. This gives an infinite mesoscopic family with
   

$$
\alpha=\gamma=0.
$$


   It is **not** a subclass of $n=4002b$. The supplied proportional real-error theorem does **not** cover its limiting allocation $b/n\to0$, so I do not promote it to an analytic exclusion theorem.

The unresolved main-family question remains a uniform upper bound on $\gamma-\alpha$, especially when the norm is nonunit.

---

## 1. Fixed-family setting and the actual arithmetic quantities

For the main calculation, retain


$$
b=9^r,\qquad n=4002b,\qquad r\ge1,
$$


and


$$
h=\frac n2,\qquad
d=\frac{b-1}{8},\qquad
A=\frac{h-1}{4},\qquad
W_j=\binom{n+2}{j}.
$$



The normalized actual columns are


$$
X=\frac{Z_w}{2R},\qquad
Y=\frac{V_w}{4b!},\qquad
R=2^{n/2}\binom n{n/2}.
$$


They are $2$-integral by the audited normalizations. Write


$$
\alpha=v_2(X^TX),\qquad
\gamma=v_2(X^TY).
$$


The norm is positive; the actual complete mixed contraction is nonzero by the retained coefficient-$4002$ theorem at $3$. Thus both valuations are finite.

The actual center remains


$$
c_n=\frac{2b!}{\lambda R}\frac{X^TY}{X^TX},
\qquad
\lambda=\frac{(n!)^2}{2^n}.
$$



For the least actual two-column denominator $d_B$, retain


$$
N_B=d_B[u,v],\qquad
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


and, crucially,


$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}.
$$


No raw determinant or column content is substituted for this final gcd.

---

# Part I. Eliminating the unspecified mixed coordinates

## 2. A closed formula for the residual’s inverse-Pascal transform

The following calculation is valid whenever


$$
b\equiv1\pmod8,\qquad h\equiv1\pmod8,
$$


and the complete logarithmic forcing divided by $b!$ vanishes modulo $16$. These conditions hold on the main family.

Put


$$
(\delta_0,\delta_1,\delta_2,\delta_3,\delta_4)
=(1,-2,4,-6,6)
$$


and


$$
a_t=\frac{(b+t)!}{b!},\qquad 0\le t\le4.
$$


The full divided residual modulo $16$ is


$$
r_i=
\sum_{s=0}^4\delta_s\binom{n+i}{s}
\sum_{t=0}^4a_t\binom{2n+i-s}{b+t}
\pmod{16}.
\tag{2.1}
$$



The factorial-tail cutoff and the whole logarithmic-forcing bound are the ones already proved; here I use them rather than replacing the actual residual by an exponential-only definition.

Define the following explicit integers, for $0\le i<b$:


$$
\boxed{
G_i=
\sum_{s=0}^4\delta_s
\sum_{t=0}^4a_t
\sum_{u=0}^s
\binom iu\binom n{s-u}
\binom{2n-s+u}{b+t-i+u}.
}
\tag{2.2}
$$


Then


$$
\boxed{P^{-1}(\rho/b!)\equiv G\pmod{16}.}
\tag{2.3}
$$



### Proof

For an auxiliary pair of variables $x,y$,


$$
\binom{n+i}{s}\binom{2n+i-s}{m}
=[x^sy^m](1+y)^n(1+x+y)^{n+i}.
$$


Taking the $i$-th inverse-Pascal transform replaces


$$
(1+x+y)^{n+i}
$$


by


$$
(1+x+y)^n(x+y)^i.
$$


Expanding


$$
(x+y)^i=\sum_u\binom iu x^uy^{i-u}
$$


therefore gives


$$
\begin{aligned}
&\left(P^{-1}
  \left(\binom{n+j}{s}\binom{2n+j-s}{m}\right)_{j<b}
 \right)_i\\
&\qquad=
\sum_{u=0}^s
\binom iu\binom n{s-u}
\binom{2n-s+u}{m-i+u}.
\end{aligned}
$$


Substitution of $m=b+t$ proves (2.2)–(2.3). All Pascal transforms have their original finite boundaries. ∎

This removes an entire growing inverse-Pascal summation from the mixed-digit calculation: each $G_i$ is now a fixed-length binomial sum.

---

## 3. A closed binomial formula for the contact-inverse carry matrix

Let


$$
(c_1,c_2,c_3,c_4)=(-1,2,-3,3).
$$


The correction matrix from the modulo-$16$ contact reduction is


$$
C_{ij}=\sum_{s=1}^4
c_s\binom{n+i}{s}\binom{n+i-s}{j}.
$$


Instead of leaving


$$
E=P^{-1}CT(-n)
$$


as a matrix product, define its entries explicitly by


$$
\boxed{
E_{ij}=
\sum_{s=1}^4 c_s
\sum_{t=0}^s
\binom i{s-t}\binom nt
\binom{-t}{j+s-i-t},
\qquad 0\le i,j<b.
}
\tag{3.1}
$$


A binomial coefficient with negative lower index is zero; generalized integer upper indices are interpreted in the usual integral sense.

### Proof

First,


$$
(P^{-1}C)_{iv}
=\sum_{s=1}^4
c_s\binom{v+s}{s}\binom n{v+s-i}.
$$


Hence


$$
E_{ij}=
\sum_{s=1}^4c_s
\sum_{v=0}^j
\binom{v+s}{s}\binom n{v+s-i}
\binom{-n}{j-v}.
$$


Put $k=v+s-i$, and expand


$$
\binom{i+k}{s}
=\sum_{t=0}^s\binom i{s-t}\binom kt.
$$


Using


$$
\binom nk\binom kt
=\binom nt\binom{n-t}{k-t}
$$


and Vandermonde convolution yields (3.1).

There is no lost upper boundary: the $T(-n)$ factor forces $v\le j<b$. The zero-binomial conventions justify the extension used in the convolution. ∎

Thus every inverse-carry entry is itself a fixed-length binomial sum.

---

## 4. The actual mixed digit as three explicit scalar carries

The established leading $X$-support is


$$
X_{8k}\equiv
\binom Ak\binom{2A+d-k}{d-k}\pmod2,
\qquad 0\le k\le d,
$$


with all other coordinates zero modulo $2$.

Let $\varepsilon_k\in\{0,1\}$ be that residue. Equivalently,


$$
\varepsilon_k=1
\quad\Longleftrightarrow\quad
k\text{ is a binary submask of }A
\ \text{and}\ 
(d-k)\mathbin{\&}(2A)=0.
\tag{4.1}
$$


Define


$$
L_i=\sum_{\substack{0\le k\le d\\8k\le i}}
\varepsilon_k\binom{-2n}{i-8k},
\qquad 0\le i<b,
\tag{4.2}
$$


and the three explicit integers


$$
\begin{aligned}
D_0&=\sum_{i=0}^{b-1}L_iG_i,\\
D_1&=\sum_{i,j=0}^{b-1}L_iE_{ij}G_j,\\
D_2&=\sum_{i,j,k=0}^{b-1}L_iE_{ij}E_{jk}G_k.
\end{aligned}
\tag{4.3}
$$



Then the requested mixed digit is


$$
\boxed{
X^TY\equiv
\frac{D_0-2D_1+4D_2}{4}\pmod2.
}
\tag{4.4}
$$


The numerator in (4.4) is divisible by $4$. In particular, this is an exact divided integer expression, not division by a nonunit in a residue field.

An economical carry implementation is as follows. Compute


$$
a=D_0\bmod8,\qquad
b_1=D_1\bmod4,\qquad
c=D_2\bmod2,
$$


using integer representatives. Then


$$
a-2b_1\equiv0\pmod4
$$


and


$$
\boxed{
X^TY\equiv \frac{a-2b_1}{4}+c\pmod2.
}
\tag{4.5}
$$



### Proof

Modulo $16$, the exact inverse reduction gives


$$
\eta\equiv
T(-2n)(I-2E+4E^2-8E^3)G.
$$


For each selected index $j=8k$, $W_j$ is odd. Since


$$
Y_j=\frac{W_j(j\eta_{j-1}-\eta_j)}4
$$


at these nonterminal indices, $j\eta_{j-1}$ contributes zero modulo $2$ after division by $4$. The whole-column divisibility also shows $4\mid\eta_{8k}$. Consequently,


$$
X^TY\equiv\sum_k\varepsilon_k\frac{\eta_{8k}}4\pmod2.
$$


Applying the selector to the inverse formula gives


$$
\sum_k\varepsilon_k\eta_{8k}
\equiv D_0-2D_1+4D_2-8D_3\pmod{16}
$$


for the corresponding cubic scalar $D_3$. After division by $4$, its cubic term is even. This proves (4.4).

The endpoint has not been replaced by zero in the actual column: its leading $X_b$-residue is zero, which is why it contributes zero to this particular first digit. The complete next-digit formula below retains it explicitly. ∎

Equations (2.2), (3.1), and (4.1)–(4.5) eliminate all unspecified $\eta/4$ coordinates. They evaluate the actual first mixed digit using finite binomial sums and two inverse-carry levels.

---

## 5. The complete mixed contraction modulo $4$, with endpoint

For completeness, the next digit can also be stated without an unspecified reconstructed vector.

Define


$$
F_i=(-1)^i\left(
2-i+3\binom i2-\binom i3
+4\binom i4-4\binom i5
\right).
\tag{5.1}
$$


This is the inverse-Pascal transform of the actual normalized $P$-forcing modulo $8$.

For $0\le j<b$, form the explicit sums


$$
\begin{aligned}
P_j^*&=\sum_{i=j}^{b-1}\binom{-2n}{i-j}
\left(F_i-2\sum_kE_{ik}F_k
+4\sum_{k,l}E_{ik}E_{kl}F_l\right),\\
Q_j^*&=\sum_{i=j}^{b-1}\binom{-2n}{i-j}
\left(G_i-2\sum_kE_{ik}G_k
+4\sum_{k,l}E_{ik}E_{kl}G_l
-8\sum_{k,l,t}E_{ik}E_{kl}E_{lt}G_t\right).
\end{aligned}
\tag{5.2}
$$


Every unspecific summation index here ranges from $0$ to $b-1$. Extend both arrays by zero at $-1,b$, and put


$$
U_j=jP_{j-1}^*-P_j^*,\qquad
V_j=jQ_{j-1}^*-Q_j^*.
$$



Then


$$
\boxed{
X^TY\equiv
\frac18\sum_{j=0}^b
W_jU_j\left(W_b\delta_{j,b}+W_jV_j\right)
\pmod4.
}
\tag{5.3}
$$


Also,


$$
\boxed{
X^TX\equiv
\frac14\sum_{j=0}^b(W_jU_j)^2\pmod4.
}
\tag{5.4}
$$



These divisions are justified by the actual column normalizations. Indeed, $W_jU_j$ agrees with $Z_{w,j}/R$ modulo $8$, and the second parenthesis agrees with $V_{w,j}/b!$ modulo $16$. Their errors therefore change the product by a multiple of $32$, as required before division by $8$.

This is a complete evaluated-contraction formula. In particular, it keeps the cubic inverse carry and $W_be_b$.

### Exact binomial evaluation

If a literal binary recursion is desired for the binomial residues in these formulas, let


$$
F(m)=v_2(m!),\qquad
U_H(m)=\frac{m!}{2^{F(m)}}\pmod{2^H}.
$$


Then


$$
U_H(m)=U_H(\lfloor m/2\rfloor)
\prod_{\substack{1\le j\le m\\j\text{ odd}}}j
\pmod{2^H},
\qquad U_H(0)=1.
$$


For $0\le t\le m$, put


$$
e=F(m)-F(t)-F(m-t).
$$


If $e\ge H$, the binomial residue is zero; otherwise it is


$$
2^e U_H(m)U_H(t)^{-1}U_H(m-t)^{-1}\pmod{2^H}.
$$


All inverses are of explicitly odd units. Negative upper indices reduce by


$$
\binom{-m}{t}=(-1)^t\binom{m+t-1}{t}.
$$


Together with (4.1), this gives an entirely specified exact recursion for the first two contraction digits.

**Limitation.** These formulas do not prove an all-depth comparison between the contractions. If both first digits vanish, their relative valuation remains a higher-precision question.

---

# Part II. How much relative loss is actually permissible?

## 6. The sharp linear threshold on the coefficient-$4002$ family

Put


$$
s=s_2(n),\qquad F_b=v_2(b!).
$$


The exact identities, including the final gcd, are


$$
\begin{aligned}
v_2(A_B)&=3n-2s+2+\alpha,\\
v_2(H_B)&=\frac{3n}{2}-s+F_b+3+\gamma,\\
v_2(g_B)&=
\min\left\{
3n-2s+2+\alpha,\
\frac{3n}{2}-s+F_b+3+\gamma
\right\},
\end{aligned}
\tag{6.1}
$$


and


$$
\boxed{
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-F_b-s-1-(\gamma-\alpha)
\right\}.
}
\tag{6.2}
$$



At the same centers,


$$
v_3(q_n)=n-\frac{b+15}{2}.
\tag{6.3}
$$


Since


$$
F_b=b+O(\log b),\qquad s=O(\log n),\qquad b/n=1/4002,
$$


a bound


$$
\limsup\frac{\gamma-\alpha}{n}\le L
$$


gives


$$
\liminf\frac{\log q_n}{n}
\ge
\left(1-\frac1{8004}\right)\log3
+
\max\left\{0,\frac32-\frac1{4002}-L\right\}\log2.
\tag{6.4}
$$



Let


$$
\tau=\left(2+\frac1{4002}\right)\log(1+\sqrt2).
$$


The supremal allowed loss coefficient for a **strict** two-prime rate win is


$$
\boxed{
L_{\rm crit}
=
\frac32-\frac1{4002}
-
\frac{
\left(2+\frac1{4002}\right)\log(1+\sqrt2)
-
\left(1-\frac1{8004}\right)\log3
}{\log2}.
}
\tag{6.5}
$$


Numerically,


$$
L_{\rm crit}\approx0.5411.
$$


Thus the sufficient condition is


$$
\limsup\frac{\gamma-\alpha}{n}<L_{\rm crit}.
$$


Equality at the threshold supplies no strict exponential margin.

In units of $b$, the corresponding supremum is


$$
\boxed{
C_{\rm crit}
=
6002-
\frac{8005\log(1+\sqrt2)-\frac{8003}{2}\log3}{\log2}
\approx2165.4.
}
\tag{6.6}
$$



### A particularly simple sufficient bound

The concrete estimate


$$
\boxed{\gamma-\alpha\le2000b+o(n)}
\tag{6.7}
$$


would imply


$$
\liminf\frac{v_2(q_n)}n\ge1,
$$


because


$$
\frac32-\frac{2001}{4002}=1.
$$


Consequently,


$$
\liminf\frac{\log q_n}{n}
\ge \log2+\left(1-\frac1{8004}\right)\log3
>\tau.
\tag{6.8}
$$



This inequality has a comfortable strict margin. For example, the elementary bounds


$$
\log2>0.69,\qquad \log3>1.09,\qquad
\log(1+\sqrt2)<0.882
$$


already certify it.

This would prove growth, rather than shrinking, of this selected primitive center form. It would exclude this center-form shrinking route on the specified sequence; it would not decide the rationality of $e+\pi$.

I do **not** prove (6.7) on an infinite subclass of $n=4002b$ here.

---

# Part III. A separate CRT-selected mixed-unit lemma

## 7. Statement and scope

Here $n$ is allowed to vary independently of the fixed coefficient $4002$.

### Theorem — simultaneous actual units near $h=1$

Let


$$
b=8d+1\ge9,\qquad n=2h,
$$


and suppose


$$
h\ge b,\qquad
h\equiv1\pmod{2^K},
\qquad
K\ge3+\lfloor\log_2(b+4)\rfloor.
\tag{7.1}
$$


Assume also the whole logarithmic-forcing bound


$$
\boxed{
h+1-2\lfloor\log_2(2n+b-1)\rfloor-v_2(b!)\ge4.
}
\tag{7.2}
$$


Use the same actual columns, endpoint, and $m_w=1$ metric.

Then


$$
\boxed{
X\equiv e_0\pmod2,\qquad Y_0\equiv1\pmod2.
}
\tag{7.3}
$$


In particular,


$$
\boxed{
X^TX\equiv X^TY\equiv1\pmod2,
\qquad \alpha=\gamma=0.
}
\tag{7.4}
$$



The conclusion concerns the **actual complete** $Q$-column. The logarithmic part is absent only from its residue at the stated precision, by (7.2).

The proof of $Y_0$ is the new part that is not supplied by a norm-digit argument.

---

## 8. Precision transfer to the reference value $n=2$

For any integers $x,\Delta$ and $0\le j\le M$,


$$
v_2\!\left(\binom{x+\Delta}{j}-\binom xj\right)
\ge v_2(\Delta)-\lfloor\log_2 M\rfloor
\tag{8.1}
$$


when $j>0$. Indeed, Vandermonde gives a sum with factors


$$
\binom{\Delta}{t}
=\frac{\Delta}{t}\binom{\Delta-1}{t-1},
$$


whose valuations are at least $v_2(\Delta)-v_2(t)$.

Under (7.1),


$$
n\equiv2\pmod{2^{K+1}}.
$$


Every binomial lower index in the modulo-$16$ contact and residual formulas is at most $b+4$. Hence (8.1) proves that those finite matrices and residuals agree modulo $16$ with the corresponding formulas at $n=2$. The same holds for $T(-n)$ and the weights.

The contact matrices are invertible over $\mathbb Z_2$, so congruence of the matrices implies congruence of their inverses. Therefore the actual $\eta_0$ modulo $16$ agrees with the reference exponential-residual calculation at $n=2$.

This explains the required size of $K$: the growing binomial transforms cost only $\lfloor\log_2(b+4)\rfloor$ precision bits, not $v_2(b!)$.

---

## 9. Exact reference calculation of $\eta_0/4$

Set


$$
n=2,\qquad B=b-1=8d.
$$


At this reference value,


$$
\phi(z)^2
=1-2z+2z^2-z^3+\frac{z^4}{4},
$$


so the divided coefficients are exactly


$$
1,-2,4,-6,6.
$$



For this section only, use the exponential residual; it is the reference residue to which the actual complete residual transfers.

### 9.1 The residual and its Newton transform have four terminal entries

Because


$$
2n+i-s=4+i-s\le b+3,
$$


the reference residual is zero for $i<b-4$. Modulo $8$, its last four entries, indexed by $B-3,\ldots,B$, are


$$
\boxed{
r\equiv(1,\ 4,\ 4d+7,\ 4)\pmod8.
}
\tag{9.1}
$$



For example, the first three are


$$
\begin{aligned}
r_{B-3}&=1,\\
r_{B-2}&\equiv5-b\equiv4,\\
r_{B-1}&\equiv\binom{b+2}{2}-6b+10
\equiv4d+7
\pmod8.
\end{aligned}
$$


Direct substitution of $b=8d+1$ into the fourth expression gives $4\bmod8$.

Taking the finite inverse-Pascal transform gives


$$
\boxed{
g=P^{-1}r\equiv(1,\ 6,\ 4,\ 4)
}
\tag{9.2}
$$


on those same last four indices, and zero earlier, modulo $8$.

To check the only potentially variable entry,


$$
g_{B-1}
\equiv (4d+7)-4(b-2)+\binom{b-2}{2}
\equiv4\pmod8.
$$


At the last index, the factors $B=8d$, $\binom B2$, and $\binom B3$ show that $g_B\equiv4\pmod8$.

### 9.2 The first row of $T(-4)$

Write


$$
\ell_i=(-1)^i\binom{i+3}{3},
\qquad 0\le i\le B.
$$


Thus $\ell$ is the first row of $T(-4)$.

Equation (9.2) gives


$$
\boxed{\ell g\equiv4\pmod8.}
\tag{9.3}
$$


Indeed, the first three terminal products vanish modulo $8$, whereas


$$
4\binom{B+3}{3}\equiv4\pmod8
$$


because $\binom{8d+3}{3}$ is odd.

### 9.3 The quadratic inverse carry vanishes at this scalar

At $n=2$, formula (3.1) becomes


$$
\begin{aligned}
E_{ij}=\sum_{s=1}^4c_s\bigg[
&\binom is\,\delta_{j,i-s}\\
&+2\binom i{s-1}\binom{-1}{j+s-i-1}\\
&+\binom i{s-2}\binom{-2}{j+s-i-2}
\bigg].
\end{aligned}
\tag{9.4}
$$



Modulo $2$, $\ell_i$ is supported at $i\equiv0\pmod4$. On such a row of $E$, the only surviving term is


$$
E_{i,i-4}\equiv\binom i4\pmod2.
$$


Therefore $\ell E$ is supported at


$$
j\equiv0\pmod8,\qquad j+4\le B.
$$


At an index divisible by $8$, the entire row of $E$ is zero modulo $2$. Hence


$$
\boxed{\ell E^2\equiv0\pmod2.}
\tag{9.5}
$$



This uses the actual finite boundary $B$. No infinite convolution is inserted.

### 9.4 The linear inverse carry also contributes zero

By (9.2),


$$
\ell Eg\equiv
(\ell E)_{B-3}+2(\ell E)_{B-2}\pmod4.
$$


The second matrix entry is even by the support just proved.

For the first, finite binomial summation in (9.4) gives


$$
\boxed{
\begin{aligned}
(\ell E)_{B-3}={}&
-2\binom{B+1}{4}
-6\binom{B+2}{5}\\
&-12\binom{B+3}{6}
+90\binom{B+4}{7}.
\end{aligned}
}
\tag{9.6}
$$


The coefficient $90$ includes the missing terminal $s=4$ contribution; this is precisely the finite-boundary correction.

Here is a check on the summation. Using


$$
\binom{i+3}{3}\binom ik
=\binom{k+3}{3}\binom{i+3}{k+3},
$$


the three terms in (9.4), before the boundary cutoff, have combined coefficient


$$
\binom{s+3}{3}-2\binom{s+2}{3}+\binom{s+1}{3}=s+1.
$$


At $j=B-3,s=4$, the first of these terms lies beyond $B$ and is absent. The coefficient becomes


$$
-2\binom63+\binom53=-30,
$$


which, with its sign and $c_4=3$, gives $90$.

Since $B\equiv0\pmod8$, Lucas parity shows


$$
\binom{B+1}{4},\qquad
\binom{B+2}{5},\qquad
\binom{B+4}{7}
$$


are all even. Equation (9.6) is therefore divisible by $4$, and


$$
\boxed{\ell Eg\equiv0\pmod4.}
\tag{9.7}
$$



### 9.5 The nonzero mixed unit

The inverse expansion modulo $8$ now yields


$$
\begin{aligned}
\eta_0
&\equiv \ell g-2\ell Eg+4\ell E^2g\\
&\equiv4\pmod8.
\end{aligned}
$$


At coordinate zero there is no terminal endpoint contribution, and $W_0=1$. Thus


$$
\boxed{Y_0=-\eta_0/4\equiv1\pmod2.}
\tag{9.8}
$$



This proves the actual mixed-coordinate unit after the precision transfer of Section 8.

---

## 10. Why the entire leading $X$-column is $e_0$

The earlier leading-column derivation uses


$$
b=8d+1,\qquad h\equiv1\pmod8,
$$


but not the equation $h=2001b$. Its finite paired-boundary cancellation and Lucas reduction therefore give, on the present domain,


$$
X_{8k}\equiv
\binom Ak\binom{2A+d-k}{d-k}\pmod2,
\qquad A=\frac{h-1}{4},
$$


with the other coordinates zero.

Under (7.1),


$$
v_2(A)\ge K-2>\log_2 d.
$$


Consequently,


$$
\binom Ak\equiv0\pmod2\qquad(1\le k\le d).
$$


At $k=0$,


$$
\binom{2A+d}{d}\equiv1\pmod2,
$$


because all binary digits of $d$ lie below the first possible nonzero digit of $2A$. Hence


$$
X\equiv e_0\pmod2.
$$


Combined with (9.8), this proves the theorem.

Both normalized columns have common $2$-content zero on this family, and both evaluated contractions are units. This is a proved statement, not an extrapolation from the two supplied finite controls.

---

## 11. An explicit infinite CRT-selected family

For each $r\ge1$, set


$$
b=9^r,\qquad
K=3+\lfloor\log_2(b+4)\rfloor.
$$


Choose $h$ to be the least integer at least $b^3$ satisfying


$$
h\equiv1\pmod{2^K},
\qquad
h\equiv0\pmod{3b},
$$


and put $n=2h$.

The Chinese remainder theorem gives exactly one residue class modulo


$$
3b\,2^K,
$$


so this defines an infinite specified family. Moreover,


$$
b^3\le h<b^3+3b\,2^K=b^3+O(b^2).
$$


Thus


$$
n\sim2b^3,\qquad b/n\to0.
$$



The whole logarithmic-forcing condition (7.2) holds throughout this family. For example,


$$
2^K\le8(b+4),\qquad h<5b^3\quad(b\ge9),
$$


so


$$
\begin{aligned}
&h+1-2\lfloor\log_2(2n+b-1)\rfloor-v_2(b!)\\
&\qquad\ge b^3-b-9-6\log_2 b>4.
\end{aligned}
$$


Therefore


$$
\boxed{\alpha=\gamma=0}
\tag{11.1}
$$


at every selected index.

The ordinary two-column lift is $2$-integral by the same divided-factorial argument: the residual correction is divisible by $b!$, and the $P$-scalar has more than enough valuation to cancel every $j!$, $j<b$. Hence


$$
v_2(d_B)=0.
$$


The actual local denominator and final gcd are consequently


$$
\boxed{
v_2(q_n)=\frac{3n}{2}-v_2(b!)-s_2(n)-1,
}
\tag{11.2}
$$




$$
\boxed{
v_2(g_B)=\frac{3n}{2}-s_2(n)+v_2(b!)+3.
}
\tag{11.3}
$$


The minimum in the final-gcd identity is the mixed Gram valuation, since the difference (11.2) is positive.

### Essential analytic limitation

This family has $b/n\to0$. The supplied signed-rate theorem assumes


$$
b/n\to c,\qquad 0<c<1/1000.
$$


It cannot be applied with $c=0$ by substitution.

Thus the new CRT lemma supplies an infinite **arithmetic** unit family, but not a matching whole real-error theorem. I make no claim of an eventual sign, a nonzero center error, or a mesoscopic rate on this new family. The complete mixed contraction itself is nonzero by (11.1).

---

## 12. What remains on the original fixed family

The binomial sums above now decide the actual first mixed digit, and (5.3) decides the next one. They do not yet yield a uniform upper bound on


$$
\gamma-\alpha
$$


when the norm is nonunit.

This distinction cannot be bypassed using column contents. For example, even the primitive $2$-integral vectors


$$
x=(1,1,2),\qquad y_T=(1,2^T-1,0)
$$


have


$$
v_2(x^Tx)=v_2(6)=1,\qquad
v_2(x^Ty_T)=T,
$$


while both column contents are zero. This is not a counterexample to the actual contact family; it identifies why column primitivity and norm nonvanishing alone cannot prove its needed relative bound.

On the original coefficient-$4002$ sequence, the supplied real theorem gives the **whole** error


$$
\epsilon_n=c_n-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|=-\tau n+o(n).
$$


The actual primitive evaluated form is


$$
\boxed{
L_n=q_n(e+\pi)-p_n=-q_n\epsilon_n>0
\quad\text{eventually},
}
\tag{12.1}
$$


and


$$
\log|L_n|=\log q_n-\tau n+o(n).
$$


These statements retain the complete exponential residual, logarithmic forcing, and endpoint correction. No finite control from the odd family is combined with them.

---

# Concluding ledger

## (1) New result and proof status

**Proved here**

- The closed residual Newton transform (2.2).
- The closed contact-carry entries (3.1).
- The actual mixed-digit formula (4.4)–(4.5), with no unspecified $\eta/4$ coordinates.
- The complete evaluated mixed contraction modulo $4$, including endpoint and cubic inverse carry, in (5.3).
- The exact maximal linear-loss threshold (6.5)–(6.6). The simple bound $2000b+o(n)$ is sufficient for a strict same-center two-prime lower-rate win.
- A separate CRT-selected arithmetic theorem:
  

$$
X\equiv e_0,\quad Y_0\equiv1,\quad
  \alpha=\gamma=0,
$$


  with the actual denominator and final-gcd valuations (11.2)–(11.3).
- The nonzero unit in that theorem is proved by the finite-boundary reference identity
  

$$
\eta_0\equiv4\pmod8,
$$


  not guessed from finite controls.

**Not proved**

- A sufficient relative-depth bound on an infinite subclass of $n=4002b$.
- An all-depth norm/mixed relation surviving arbitrary nonunit norm depth.
- A matching whole real-error theorem for the separate CRT mesoscopic family.
- Irrationality or rationality of $e+\pi$.

## (2) Exact remaining bottleneck

For the original fixed family, prove an estimate such as


$$
\boxed{\gamma-\alpha\le2000b+o(n)}
$$


on an infinite specified subclass, or another bound strictly below (6.6). The explicit scalar carries now expose the actual mixed digit, but their higher-precision behavior remains uncontrolled.

For the separate CRT family, the local arithmetic problem is resolved at $2$; the immediate missing dependency is a **whole evaluated real-error theorem in the mesoscopic domain $n\sim2b^3$**. The supplied positive-proportional theorem does not supply it.

## (3) One bounded exact computation request

No additional scan of the coefficient-$4002$ family is requested.

A single falsification audit of the new scoped lemma would be useful.

**Input**


$$
\boxed{b=9,\qquad h=2241,\qquad n=4482,\qquad m_w=1.}
$$


Here $K=6$, $h\equiv1\pmod{64}$, $27\mid h$, and $h$ is the first CRT-selected value at least $9^3$.

**Expected verifiable output, from original defining coefficients and complete forcing**

1. 
   

$$
X\equiv e_0\pmod2,\qquad Y_0\equiv1\pmod2.
$$


2. 
   

$$
X^TX\equiv X^TY\equiv1\pmod2.
$$


3. The exact local quantities
   

$$
s_2(n)=4,\qquad v_2(9!)=7,
$$


   and therefore
   

$$
\boxed{v_2(q_n)=6711,\qquad v_2(g_B)=6729.}
$$


4. A whole-forcing certificate:
   

$$
v_2(h_i^F/9!)\ge2209,
$$


   so omission of that complete contribution at a small modular precision is justified.
5. Optionally, the independent reference check at $n=2,b=9$:
   

$$
\eta_0\equiv4\pmod8
$$


   for the specified exponential-residual reference calculation.

This would audit the new transfer and boundary calculation at one prescribed index. It would not be the proof of the infinite CRT lemma.
