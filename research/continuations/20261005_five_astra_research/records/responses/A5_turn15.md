> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 — the seven-boundary discrepancy vanishes on the original class

On the original index domain


$$
\boxed{b=9^r,\qquad n=4002b,\qquad r=18+32u,\quad u\ge0,}
$$


I obtain


$$
\boxed{\Delta _2=0.}
$$



In fact, the calculation gives the stronger conclusion


$$
\boxed{v_2(X^TX)\ge3,\qquad v_2(X^TY)\ge3.}
$$



The important additional support fact is that **both complete normalized columns are even on this particular class**. In particular, the potentially troublesome odd-coordinate contribution is not discarded: its vanishing follows from a fresh evaluation of the odd-coordinate parity of $Y$.

The seven-boundary formulas, their raw precisions, and the degree-$17/15$ closure are retained below. After proving the additional whole-column divisibility, their highest retained bits are shown to annihilate in this scalar. The remaining convolution is evaluated explicitly—not replaced by finite sampling.

This does not establish an all-depth alignment theorem or the required bound on $\gamma-\alpha$, and it does not decide irrationality of $e+\pi$.

---

## 1. Domain, actual columns, and the scalar being evaluated

Keep


$$
h=\frac n2,\qquad R=2^h\binom{2h}{h},\qquad
\lambda=\frac{(n!)^2}{2^n},
$$


and the actual weighted columns


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!}.
$$


The metric is exactly


$$
W_j=\binom{n+2}{j},\qquad
\omega_j=j!W_j=(n+2)_{\underline j},\qquad
\Omega=\operatorname{diag}(\omega_j^2),
\quad 0\le j\le b.
$$


Every contact inverse still has indices $0\le i,j<b$.

Write


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532.
$$


On the assigned class,


$$
D\ \text{is odd},\qquad C\equiv2\pmod4.
$$


For the calculation below it is convenient to put


$$
m=\frac{b-1}{4}=32D+20,\qquad
M=\frac{n+2}{4}=32C+17.
$$


Thus


$$
h=2M-1=64C+33,\qquad m\equiv0\pmod4,\qquad M\equiv1\pmod{16}.
$$



Let


$$
N=X^TX,\qquad H=X^TY,\qquad
\alpha=v_2(N),\qquad \gamma=v_2(H).
$$


The established norm positivity and original-family mixed nonvanishing are retained, so these valuations are finite.

With the complete raw representatives


$$
A_j^+\equiv2X_j\pmod{16},\qquad
B_j^{+,{\rm act}}\equiv4Y_j\pmod{32},
$$


the assigned discrepancy is


$$
\Delta _2=
\frac{\sum_jA_j^+B_j^{+,{\rm act}}
      -2\sum_j(A_j^+)^2}{32}\pmod2
=
\frac{H-N}{4}\pmod2.
\tag{1}
$$


The numerator on the left is evaluated modulo $64$.

---

## 2. The degree-$17/15$ lift and the reference-parameter precision

### 2.1 Complete retained inputs

The seven boundary values remain


$$
(B_0^+,\ldots,B_6^+)
=(5,10,22,24,24,16,16)\pmod{32}.
\tag{2}
$$


The complete logarithmic forcing can be omitted at this precision only because its supplied whole-force bound gives


$$
v_2(h_i^F/b!)
\ge h+1-2\lfloor\log_2(2n+b-1)\rfloor-v_2(b!)
>5.
\tag{3}
$$


Indeed, $h=2001b$ and $v_2(b!)\le b-1$, so this is immediate for $b\ge81$.

The $P$-forcing is


$$
g_{16}(X)=
2-9X+3\binom X2-9\binom X3
+12\binom X4-4\binom X5\pmod{16}.
$$


Keep the full representatives


$$
P^+=\sum_{\ell=0}^{3}(-2\mathscr E)^\ell g_{16}\pmod{16},
\qquad \deg P^+\le17,
\tag{4}
$$




$$
Q^+=2\sum_{\ell=0}^{3}(-2\mathscr E)^\ell a^+\pmod{32},
\qquad \deg Q^+\le15.
\tag{5}
$$



Here the seven-boundary polynomial has the explicit reference value


$$
\boxed{a^+(X)=10+2X+8\binom X2+15\binom X3\pmod{16}.}
\tag{6}
$$



To verify (6), at $n=2$ the exterior-column formula is


$$
E_{ik}=(-1)^{k-i}\bigl((k-i)B_i^\circ+D_i^\circ\bigr),
$$


where


$$
B_i^\circ=2+3i+3\binom i2,\qquad
D_i^\circ=2i+3\binom i2-6\binom i3.
$$


The seven inputs give


$$
\sum_{a=0}^6(-1)^a B_a^+=17,\qquad
\sum_{a=0}^6a(-1)^aB_a^+=74.
$$


Since $b$ is odd,


$$
a^+(i)\equiv
-\bigl((81-i+10)B_i^\circ+D_i^\circ\bigr)\pmod{16},
$$


whose Newton expansion is exactly (6).

The actual solutions are still


$$
\theta^+=T(-2n)\mathcal S_bP^+\pmod{16},
$$




$$
\eta_i^+=-\sum_{a=0}^{6}B_a^+\binom{-2n}{b+a-i}
 +(T(-2n)\mathcal S_bQ^+)_i\pmod{32}.
\tag{7}
$$


Extend them by zero at $-1,b$. The reconstruction, including the endpoint, is


$$
A_j^+=W_j(j\theta^+_{j-1}-\theta_j^+),
$$




$$
B_j^{+,{\rm act}}
=W_b\mathbf1_{j=b}
 +W_j(j\eta^+_{j-1}-\eta_j^+).
\tag{8}
$$



### 2.2 Why $n=2,b=81$ is still valid in the bounded closure

This substitution applies only to the bounded signed-Newton operators, not to $T(-2n)$, the large binomial kernels, or the actual index range.

On the assigned class,


$$
v_2(n-2)=6,\qquad v_2(b-81)=7.
$$


For a fixed lower index $a\ge1$,


$$
v_2\!\left(\binom{x+\delta}{a}-\binom xa\right)
\ge v_2(\delta)-\lfloor\log_2a\rfloor.
\tag{9}
$$


This follows from Vandermonde and
$v_2\binom{\delta}{k}\ge v_2(\delta)-\lfloor\log_2k\rfloor$.

The losses must be compared with the **weighted** inverse terms:

| Term | Largest $b$-dependent lower index | Guaranteed $b$-difference depth | Required unweighted depth |
|---|---:|---:|---:|
| $-2\mathscr E g_{16}$ | $9$ | $4$ | $3$ |
| $4\mathscr E^2g_{16}$ | $13$ | $4$ | $2$ |
| $-8\mathscr E^3g_{16}$ | $17$ | $3$ | $1$ |
| $-4\mathscr E a^+$ | $7$ | $5$ | $3$ |
| $8\mathscr E^2a^+$ | $11$ | $4$ | $2$ |
| $-16\mathscr E^3a^+$ | $15$ | $4$ | $1$ |

The $n$-dependent lower indices are at most $4$, giving depth at least $6-2=4$ before the displayed weights. The boundary polynomial itself needs precision $16$; its $n$-dependence has depth at least $4$, and its $b$-dependent lower indices are at most $3$.

Consequently, all the displayed requirements are met. In particular, the loss at lower index $17$ is accounted for; one does **not** assert an unweighted modulo-$16$ substitution there.

Integral finite differences transfer these value congruences to Newton coefficients.

---

## 3. A stronger parity fact on the original $r\equiv18\pmod{32}$ class

The established paired parity is


$$
e_t=
\binom Ct\binom{2C+1+D-t}{D-t}\pmod2,
\qquad 0\le t\le D.
\tag{10}
$$


But here $C$ is even and $D$ is odd. If the first binomial is odd, $t$ is even. Then $D-t$ is odd, and the second binomial is even because $2C+1$ is odd. Hence


$$
\boxed{e_t=0\quad\text{for every }t.}
\tag{11}
$$


The established complete support of $X\bmod2$ therefore gives


$$
X\in2\mathbb Z_2^{b+1}.
\tag{12}
$$



The corresponding assertion for $Y$ needs the odd coordinates as well.

### 3.1 Fresh evaluation of the odd-coordinate parity of $Y$

For $j<b$, the complete residual formula gives


$$
\eta_j\equiv
\binom{2n+b-1-j}{b-j}\pmod2.
\tag{13}
$$


For odd $j$,


$$
v_2(W_j)\ge2.
$$


If $v_2(W_j)\ge3$, then $Y_j$ is even.

If $v_2(W_j)=2$, Lucas applied to


$$
\frac{W_j}{4}
=\frac{M}{j}\binom{n+1}{j-1}
$$


requires


$$
j\bmod128\in\{1,3,65,67\}.
$$


At residues $3,67$, both terms in $j\eta_{j-1}-\eta_j$ are even.

Consider therefore


$$
j=128t+1\quad\text{or}\quad j=128t+65.
$$


Write $j=4k+1$ and $\ell=m-k$. Formula (13) gives


$$
\eta_j\equiv\binom{h+\ell-1}{\ell}\pmod2,
\qquad \eta_{j-1}\equiv0\pmod2.
$$


For the two positions, respectively,


$$
\ell=32(D-t)+20,\qquad \ell=32(D-t)+4.
$$


Lucas reduction therefore yields, including the weight,


$$
\boxed{
Y_{128t+1}\equiv Y_{128t+65}\equiv e_t\pmod2,
}
\tag{14}
$$


and all other nonterminal odd coordinates are even.

Thus the odd parity is not an uncontrolled contribution: it is the same carry expression (10), shifted by one coordinate. By (11), it vanishes on the assigned class.

The established even-coordinate support of $Y\bmod2$, together with (14), now gives


$$
\boxed{Y\in2\mathbb Z_2^{b+1},}
\tag{15}
$$


subject only to the endpoint check below.

### 3.2 Fresh endpoint check

Use


$$
W_b=\frac{n+2}{b}\binom{n+1}{b-1}.
$$


At binary positions $4,5,6,7$, subtraction of $b-1$ from $n+1$ has four successive borrows:

- $n+1\bmod128=67$, whereas $b-1\bmod128=80$;
- at position $7$, $C$ is even and $D$ is odd.

Kummer therefore gives


$$
v_2(W_b)\ge2+4=6.
\tag{16}
$$


Since the complete endpoint is


$$
X_b=\frac{W_b\,b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4},
$$


with integral reconstructed solutions,


$$
v_2(X_b)\ge5,\qquad v_2(Y_b)\ge4.
\tag{17}
$$


This proves (15) at the endpoint and proves that its contribution to (1) is zero. The endpoint $1$ has been retained before this conclusion.

### 3.3 Why the highest raw bits now annihilate

The complete lift remains (4)–(8). However, because both actual columns are even, the scalar


$$
\frac{X^TY-X^TX}{4}\pmod2
$$


depends only on $X,Y\bmod4$.

Indeed, replacing $X,Y$ by $X+4a,Y+4c$ changes its numerator by


$$
4a^T(Y-2X)+4X^Tc+16(a^Tc-a^Ta),
$$


which is divisible by $8$.

Thus the degree-$17/15$ raw lift is retained, but its highest bits have a proved zero contribution to this scalar. This is why the following calculation can use its reductions modulo $8$ and $16$, including the corresponding reduction of all seven boundary inputs. It is not an omission of the $b+5,b+6$ tails before establishing the requisite divisibility.

---

## 4. Two complete even-coordinate formulas

The supplied exact coefficient receipt, transferred to the original parameters by Section 2, gives


$$
P\bmod8=
2+7\binom X1+7\binom X2+5\binom X3
+4\binom X5+4\binom X6+4\binom X7,
\tag{18}
$$


and


$$
Q-2P\bmod16=
6\binom X1+10\binom X2+12\binom X3
+8\binom X5+8\binom X6.
\tag{19}
$$


These are fixed-polynomial coefficients, not values inferred from sampled growing matrices.

Here are the resulting coordinate identities:


$$
\boxed{
\begin{aligned}
X_{4k}&\equiv-(k+1)F_k\pmod4,\\
Y_{4k}&\equiv-F_k\pmod4,
\end{aligned}
\qquad 0\le k\le m,
}
\tag{20}
$$


where


$$
F_k=
\binom{n+2}{4k}
\binom{h+m-k}{m-k}.
\tag{21}
$$


For the remaining even positions,


$$
\boxed{
Y_{4k+2}\equiv0\pmod4,
\qquad 0\le k<m,
}
\tag{22}
$$


and


$$
\boxed{
X_{4k+2}\equiv
\binom{M-1}{k}
\binom{h+m-k-1}{m-k-1}\pmod4.
}
\tag{23}
$$



I give the derivation, since these identities perform the complete off-pair calculation.

### 4.1 Moment calculation retaining the actual large kernels

Put


$$
a=2n=4h,\qquad L=b-1-j,\qquad
M_v(j)=\binom{a+L}{L-v}.
$$


Let


$$
H_j^\circ=\eta_j-2\theta_j.
$$


The complete boundary and (19) give


$$
\begin{aligned}
(-1)^jH_j^\circ\equiv{}&
M_{-1}+10M_{-2}+14M_{-3}+8M_{-4}+8M_{-5}\\
&+d(j)M_0+8(1+j)M_1+(4+8j)M_2\\
&+8\left(j+\binom j2\right)M_4
\pmod{16},
\end{aligned}
\tag{24}
$$


where


$$
d(j)=6j+10\binom j2+12\binom j3
     +8\binom j5+8\binom j6.
$$



For example, the complete boundary coefficients in the first line are obtained by Vandermonde from


$$
(5,10,6,8,8)\pmod{16};
$$


they are $1,10,14,8,8$, respectively. The finite moment identity used for the polynomial part is the one in the supplied closure proof. The factors


$$
\binom{a+v-1}{v}
$$


are reduced only at their bounded lower indices; the $M_v(j)$ retain the actual $n,b,j$.

For even $j$, put


$$
G_j=H_j^\circ-jH_{j-1}^\circ.
$$


Using


$$
M_v(j-1)=M_{v-1}(j)+M_v(j),
$$


the nonzero coefficients of $G_j\bmod16$ are:



$$
\begin{array}{c|l}
v&[M_v]G_j\\ \hline
-5&8\\
-4&8+6j\\
-3&14\\
-2&10+11j\\
-1&1+j-4\binom j2-2\binom j3+8\binom j7\\
0&6j+6\binom j2+10\binom j3
  +8\binom j5+8\binom j6+8\binom j7\\
1&8+4j\\
2&4+4j\\
4&8\binom j2
\end{array}
\tag{25}
$$



This table is an explicit fixed-degree calculation of the **complete** column difference.

### 4.2 Positions $j=4k$

Set


$$
\ell=m-k,\qquad T=h+\ell,\qquad
B=\binom{4T}{4\ell}.
$$


Substitution of $j=4k$ in (18) and the same moment formula gives


$$
j\theta_{j-1}-\theta_j
\equiv-2(k+1)B\pmod8.
\tag{26}
$$



For clarity, (25) first reduces to


$$
G_j\equiv
8(1+k)\binom{4T}{4\ell+4}
 +(8+12k)B\pmod{16}.
\tag{27}
$$


The elementary adjacent-binomial reductions used here include


$$
\binom{4T}{4\ell+1}\equiv4B\pmod{16},
$$




$$
\binom{4T}{4\ell+2}\equiv(4\ell+6)B\pmod8,
$$




$$
\binom{4T}{4\ell+3}\equiv4B\pmod8,
\qquad
\binom{4T}{4\ell-2}\equiv2\ell B\pmod4.
$$


They use $h\equiv1\pmod{32}$ and only odd denominators.

If $k$ is even, $\ell$ is even and


$$
\binom{4T}{4\ell+4}\equiv B\pmod2.
$$


If $k$ is odd, $B$ is even. Thus (27) simplifies to


$$
G_j\equiv12kB\pmod{16}.
\tag{28}
$$



Finally,


$$
\binom{4T}{4\ell}\equiv\binom T\ell\pmod4.
\tag{29}
$$


One quick proof of the underlying congruence
$\binom{2A}{2B}\equiv\binom AB\pmod4$
is to take even coefficients of


$$
(1+z)^{2A}
\equiv(1+z^2)^A+2Az(1+z^2)^{A-1}\pmod4
$$


and then apply it twice.

Equations (26)–(29), together with


$$
Y_j-X_j=-\frac{W_jG_j}{4},
$$


give (20).

### 4.3 Positions $j=4k+2$

Now put


$$
\ell=m-k\ge1,\qquad T=h+\ell,\qquad
B=\binom{4T-2}{4\ell-2}.
$$


The $P$-moment calculation gives


$$
j\theta_{j-1}-\theta_j
\equiv(1-2k)B\pmod4.
\tag{30}
$$



Every such $W_j$ is even. Moreover,


$$
\frac{W_{4k+2}}2
\equiv-(2k+1)\binom{M-1}{k}\pmod4,
\tag{31}
$$


and


$$
B\equiv-\binom{h+\ell-1}{\ell-1}\pmod4.
\tag{32}
$$


For (31), use an adjacent-binomial ratio with odd denominators and
$\binom{4M}{4k}\equiv\binom Mk\pmod4$.
For (32), apply (29) once and use


$$
\frac{2T-1}{2\ell-1}\equiv-1\pmod4,
$$


because $T-\ell=h$ is odd.

Since


$$
(2k+1)(1-2k)\equiv1\pmod4,
$$


equations (30)–(32) prove (23).

It remains to verify (22). The complete residual formula gives


$$
j\eta_{j-1}-\eta_j\equiv0\pmod4
\qquad(j\equiv2\pmod4).
\tag{33}
$$


Thus $v_2(W_j)\ge2$ already implies $Y_j\equiv0\pmod4$.

If $v_2(W_j)=1$, equation (31) and Lucas force


$$
k\equiv0,16\pmod{32},
\qquad j\equiv2\pmod{32}.
$$


At this residue, (25) gives


$$
G_j\equiv
4M_{-4}+6M_{-3}+7M_{-1}+2M_0+4M_2
\equiv2B\pmod8.
\tag{34}
$$


Indeed, $6M_{-3}\equiv4M_{-4}\pmod8$,
$M_{-1}\equiv4B\pmod8$, and $M_2\equiv B\pmod2$.
Since $k$ is even, (30) gives the reconstruction $B\bmod4$.
Consequently


$$
Y_j
=X_j-\frac{W_jG_j}{4}
\equiv\frac{W_j}{2}B-\frac{W_j}{2}B
\equiv0\pmod4.
$$


This completes the proof of (20)–(23).

---

## 5. Separate contributions to $\Delta _2$, and their evaluated sum

Let


$$
\mathcal P=\{128t,128t+64:0\le t\le D\}
$$


be the prescribed paired coordinates. All quotients below are legitimate by Sections 2–3.

### 5.1 Paired coordinates

The independently certified $\kappa=0$, combined with the proved infinite-class formula, gives


$$
X_j-Y_j\in4\mathbb Z_2\qquad(j\in\mathcal P).
$$


On the assigned subclass $X_j$ is even. Hence


$$
\boxed{
\sum_{j\in\mathcal P}\frac{X_j(Y_j-X_j)}4=0\pmod2.
}
\tag{35}
$$



### 5.2 Off-pair even coordinates divisible by $4$

Since $Y_{4k}$ is even, (20) shows that $F_k$ is even. Put $f_k=F_k/2$.
Then


$$
\frac{X_{4k}}2\equiv-(k+1)f_k,\qquad
\frac{Y_{4k}}2\equiv-f_k\pmod2.
$$


Therefore


$$
\frac{X_{4k}(Y_{4k}-X_{4k})}{4}
\equiv k(k+1)f_k^2=0\pmod2.
\tag{36}
$$


This is coordinatewise; in particular it covers every off-pair coordinate divisible by $4$.

### 5.3 Even coordinates congruent to $2\pmod4$

By (22), $Y_{4k+2}$ is divisible by $4$. Thus their contribution is


$$
\sum_{k=0}^{m-1}\frac{X_{4k+2}(Y_{4k+2}-X_{4k+2})}{4}
\equiv\frac12\sum_{k=0}^{m-1}X_{4k+2}\pmod2.
\tag{37}
$$


Using (23), the required sum modulo $4$ is


$$
\begin{aligned}
\Sigma
&=\sum_{k=0}^{m-1}
\binom{M-1}{k}
\binom{h+m-k-1}{m-k-1}\\
&=[z^{m-1}](1+z)^{M-1}(1-z)^{-2M}.
\end{aligned}
\tag{38}
$$



This is the higher-digit convolution that must actually be evaluated.

Put


$$
A=\frac{M-1}{2}=16C+8.
$$


Since $A$ is even,


$$
(1+z)^{M-1}\equiv(1+z^2)^A\pmod4,
$$


whereas


$$
(1-z)^{-2M}
\equiv
(1+z^2)^{-M}
+2Mz(1+z^2)^{-M-1}\pmod4.
$$


The index $m-1$ is odd. Therefore


$$
\frac{\Sigma}{2}
\equiv
[w^{(m-2)/2}](1+w)^{A-M-1}\pmod2.
$$


Explicitly,


$$
\boxed{
\frac{\Sigma}{2}
\equiv
[w^{16D+9}](1+w)^{-(16C+10)}
=0\pmod2.
}
\tag{39}
$$


The last equality is an infinite identity over $\mathbb F_2$: the exponent $16C+10$ is even, so the series has only even powers, while $16D+9$ is odd.

Thus the contribution (37) is zero.

### 5.4 Odd coordinates, including the endpoint

At every odd coordinate, $X_j$ is divisible by $4$. Section 3 proves that $Y_j$ is even on this original subclass. Consequently


$$
\boxed{
\frac{X_j(Y_j-X_j)}4=0\pmod2
\qquad(j\ \text{odd}).
}
\tag{40}
$$


The endpoint has the stronger bounds (17).

This is a new justification at the lifted digit. The earlier fact $4\mid X_j$ alone would not have justified dropping this contribution if $Y_j$ had remained odd.

### 5.5 Actual sum

Combining (35), (36), (39), and (40),


$$
\boxed{
\Delta _2
=\Delta_{\rm paired}
+\Delta_{\rm off\text{-}pair,\ even}
+\Delta_{\rm odd}
=0+0+0=0.
}
\tag{41}
$$



---

## 6. The norm digit also vanishes: both depths are at least $3$

The same formulas evaluate $N/4\bmod2$.

Odd coordinates contribute zero. The sum of the $4k+2$ contributions is zero by (39), because over $\mathbb F_2$,
$(X_j/2)^2=X_j/2$.

At $j=4k$, formula (20) shows that odd $k$ contribute zero. Thus


$$
\frac N4
\equiv\frac12
\sum_{\substack{0\le k\le m\\k\ {\rm even}}}
\binom Mk\binom{h+m-k}{m-k}\pmod2.
\tag{42}
$$


Here each summand is even on the assigned class, by the proved evenness of $F_k$.

Taking the even part of $(1+z)^M$ modulo $4$, the same calculation as above gives


$$
\sum_{k\ {\rm even}}
\binom Mk\binom{h+m-k}{m-k}
\equiv
\binom{16(C+D)+18}{16D+10}\pmod4.
\tag{43}
$$


Consequently


$$
\frac N4
\equiv
\frac12\binom{16(C+D)+18}{16D+10}\pmod2.
\tag{44}
$$



This binomial is divisible by $4$. Indeed:

- at binary position $3$, its lower argument has digit $1$, while its upper argument has digit $0$, producing a borrow;
- at position $4$, the upper digit is
  $(C+D+1)\bmod2=0$, while the lower digit is $D\bmod2=1$, and the incoming borrow continues.

Kummer gives at least two borrows. Hence


$$
\frac N4=0\pmod2.
$$


Together with (41),


$$
\boxed{N\equiv H\equiv0\pmod8,\qquad \alpha,\gamma\ge3.}
\tag{45}
$$



This is exactly one further proved lower-depth step beyond the previously established $\alpha,\gamma\ge2$. No exact value of either deeper valuation is asserted.

---

## 7. What a useful all-depth invariant would have to preserve

The current cancellation has a concrete integral structure:

1. **Diagonal-type blocks:** after dividing by the common column factor $2$,
   

$$
x_{4k}=(k+1)f_k,\qquad y_{4k}=f_k\pmod2,
$$


   so their defect is killed by $k(k+1)$.

2. **Defect-only blocks:** at $4k+2$, $y=0\pmod2$, and the complete sum of $x$ is an odd coefficient of a series in $w^2$.

3. **Odd blocks:** one normalized column is even, after separately proving the parity of the other complete column.

A useful proposed induction invariant is that, after each necessary scalar carry and boundary enlargement, the complete contracted defect decomposes into these three kinds of blocks, with the defect-only generating series retaining the requisite even-power support. Such an invariant must include the factorial boundary jets, the endpoint, the weighted precision losses, and the scalar carries when a norm digit vanishes.

**That stability has not been proved.** In particular, the present calculation does not authorize iterating the degree-$17/15$ truncation indefinitely.

A scalar formulation of the still-needed alignment invariant is


$$
v_2(N)\ge s
\quad\Longrightarrow\quad
H-N\in2^{s+1}\mathbb Z_2,
\tag{46}
$$


at every subsequent relevant level $s$. The current work establishes the assigned $s=2$ instance and separately proves $N\in8\mathbb Z_2$; it does not establish the $s=3$ instance.

---

## 8. Final gcd, actual primitive denominator, and whole evaluated error

No column, metric, primitive normalization, or real error has changed.

Let $d_B$ be the least common denominator of the actual two-column lift and put


$$
N_B=d_B[u,v].
$$


For the falling-factorial metric specified in Section 1, retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad q_n=\frac{A_B}{g_B}>0.
$$


Thus $q_n$, not a raw determinant or a column clearer, is the actual primitive multiplier.

The actual center remains


$$
c_n=\frac{2b!}{\lambda R}\frac{X^TY}{X^TX}
=\frac{p_n}{q_n}.
$$


With $s=s_2(n)$, the exact binary interface is


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
\tag{47}
$$


The lower bounds $\alpha,\gamma\ge3$ cannot be subtracted to bound their difference.

The retained whole signed-error theorem gives, eventually,


$$
\epsilon_n=c_n-(e+\pi)<0,
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)
 n\log(1+\sqrt2)+o(n).
$$


The complete primitive evaluated form is therefore


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n>0}
$$


eventually, and is nonzero. This is the whole error, with the complete exponential residual, logarithmic force, and endpoint—not a selected residual component.

---

# Concluding ledger

## (1) New result and proof status

**Proved on the original infinite class**


$$
b=9^r,\quad n=4002b,\quad r=18+32u,\quad u\ge0:
$$



- The degree-$17/15$ closure may use $n_{\rm ref}=2,b_{\rm ref}=81$ at its **weighted** precisions; the lower-index-$17$ loss is explicitly accounted for.
- The seven-boundary polynomial is (6).
- Both complete normalized columns are even.
- The odd-coordinate parity of $Y$ is the shifted paired carry expression (14), hence vanishes on this subclass.
- The endpoint contributes zero at the new scalar precision.
- The paired, off-pair even, and odd contributions have been separately evaluated and summed:
  

$$
\boxed{\Delta _2=0.}
$$


- The next norm digit also vanishes:
  

$$
\boxed{\alpha,\gamma\ge3.}
$$



The fixed coefficient receipt is used as an exact bounded-polynomial input, with an explicit infinite parameter-transfer proof. No finite growing-index sample is used to prove these assertions.

## (2) Exact remaining bottleneck

The next unresolved digit is now


$$
\boxed{\frac{X^TY-X^TX}{8}\pmod2.}
$$


The common evenness proved here does not by itself evaluate that digit.

Beyond it, the substantive arithmetic obligation remains


$$
\boxed{\gamma-\alpha\le2000b+o(n),}
$$


or another sufficient estimate on the actual primitive denominator after the final gcd. Neither (45) nor finitely many further aligned bits proves that bound.

No irrationality or rationality conclusion for $e+\pi$ follows.

## (3) Computation request

**No additional computation is needed for the evaluation above.**

If an independent fixed-polynomial audit is desired, its exact inputs are


$$
n_{\rm ref}=2,\quad b_{\rm ref}=81,\quad
g_{16}=(2,-9,3,-9,12,-4),
\quad a^+=(10,2,8,15)
$$


in Newton coordinates, with the supplied signed closure operator. The verifiable outputs would be:

1. $P^+\bmod16$, through degree $17$;
2. $Q^+\bmod32$, through degree $15$;
3. their reductions (18)–(19);
4. the symbolic reconstruction congruences (20), (22), and (23).

Such an audit concerns fixed polynomial identities only; it is not a substitute for the infinite convolution evaluations (39) and (43)–(45).
