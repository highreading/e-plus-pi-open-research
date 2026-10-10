> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 — the third discrepancy vanishes; the next norm digit vanishes too

On the **same original domain**


$$
\boxed{
b=9^r,\qquad n=4002b,\qquad r=18+32u,\quad u\ge0,
}
$$


the complete seven-boundary lift gives


$$
\boxed{\Delta _3=\frac{H-N}{8}\equiv0\pmod2.}
$$



In fact, the new argument proves


$$
\boxed{N\equiv H\equiv0\pmod{16}.}
$$


It does not assume the separately assigned audit conclusion $\alpha,\gamma\ge3$.

There are two new ingredients:

1. At every coordinate outside the prescribed pairs, the complete columns have enough additional divisibility to annihilate the third discrepancy.
2. At a paired coordinate, the full seven-boundary difference reduces to a sampled polynomial equal to $16\bmod32$. Its convolution retains the actual large binomial kernel. After multiplication by the actual weight, the original carry obstruction makes the coordinate difference divisible by $8$.

Thus no additional low-digit subclass is needed, and no original-domain indices are omitted. The existing precisions $A^+\bmod16$, $B^{+,{\rm act}}\bmod32$ suffice throughout.

This is a finite-depth arithmetic result. It does **not** prove an all-depth bound on $\gamma-\alpha$, or decide irrationality of $e+\pi$.

---

## 1. Actual quantities and retained complete lift

Keep


$$
h=\frac n2,\qquad
R=2^h\binom{2h}{h},\qquad
\lambda=\frac{(n!)^2}{2^n},
$$


and the actual normalized weighted columns


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!}.
$$


The metric is precisely


$$
W_j=\binom{n+2}{j},\qquad
\omega_j=j!W_j=(n+2)_{\underline j},\qquad
\Omega=\operatorname{diag}(\omega_j^2),
\quad 0\le j\le b.
$$


Every contact inverse has the actual finite domain $0\le i,j<b$.

Write


$$
N=X^TX,\qquad H=X^TY,\qquad
\alpha=v_2(N),\qquad \gamma=v_2(H).
$$


Norm positivity and the retained original-family mixed nonvanishing make both valuations finite.

The useful parameters are


$$
b=128D+81,\qquad n=128C+66,\qquad
C=4002D+2532,
$$


and


$$
m=\frac{b-1}{4}=32D+20,\qquad
M=\frac{n+2}{4}=32C+17,\qquad
h=64C+33=2M-1.
$$


On **every** assigned index,


$$
\boxed{D\ \text{odd},\qquad C\equiv2\pmod4.}
\tag{1}
$$



### Complete forces and boundaries

The seven boundary values remain


$$
(B_0^+,\ldots,B_6^+)
=(5,10,22,24,24,16,16)\pmod{32}.
\tag{2}
$$


In particular, neither of the factorial tails $b+5,b+6$ is deleted.

The complete logarithmic force is absent modulo $32$ only by the whole-force estimate


$$
v_2(h_i^F/b!)
\ge
h+1-2\lfloor\log_2(2n+b-1)\rfloor-v_2(b!)
>5.
\tag{3}
$$


The factorial tails beginning at $b+7$ vanish at this precision.

Use the already checked degree-$17/15$ closure. Its actual solutions are


$$
\theta_i=T(-2n)\mathcal S_bP^+\pmod{16},
$$




$$
\eta_i=
-\sum_{a=0}^{6}B_a^+\binom{-2n}{b+a-i}
+\bigl(T(-2n)\mathcal S_bQ^+\bigr)_i
\pmod{32}.
\tag{4}
$$


Here $(\mathcal S_bf)_i=(-1)^if(i)$, and all finite matrix operations retain their original boundaries.

The checked coefficient vectors are


$$
\begin{aligned}
P^+\equiv{}&
2+15\binom X1+7\binom X2+5\binom X3
+12\binom X5+4\binom X6+4\binom X7\\
&+8\binom X9+8\binom X{10}+8\binom X{11}
\pmod{16},
\end{aligned}
\tag{5}
$$


and


$$
\begin{aligned}
Q^+\equiv{}&
20+4\binom X1+24\binom X2+6\binom X3
+16\binom X4+16\binom X5\\
&+8\binom X7+16\binom X{11}
\pmod{32}.
\end{aligned}
\tag{6}
$$


Their short displayed support is a coefficient congruence inside the established closure, not an indefinitely iterable degree assertion.

Extending $\theta,\eta$ by zero at $-1,b$, the actual reconstruction is


$$
A_j^+=W_j(j\theta_{j-1}-\theta_j)\equiv2X_j\pmod{16},
$$




$$
B_j^{+,{\rm act}}
=W_b\mathbf1_{j=b}
+W_j(j\eta_{j-1}-\eta_j)
\equiv4Y_j\pmod{32}.
\tag{7}
$$



The reference parameters $n=2,b=81$ have been used only in obtaining the bounded coefficients (5)–(6), at their checked weighted precisions. They are **not** substituted into $T(-2n)$, the binomial kernels below, or any growing index range.

Both complete columns are even on the assigned domain. Consequently $X,Y\bmod8$ determine $H-N\bmod16$; no higher raw precision is used.

---

## 2. New support refinement: off-pair even coordinates are divisible by $4$

Let


$$
\mathcal P=\{128t,128t+64:0\le t\le D\}.
\tag{8}
$$


These are exactly the coordinates below $b$ divisible by $64$.

I use the previously derived complete modulo-$4$ coordinate reductions, obtained from (4) by finite moment summation:


$$
X_{4k}\equiv-(k+1)F_k,\qquad
Y_{4k}\equiv-F_k\pmod4,
\quad 0\le k\le m,
\tag{9}
$$


where


$$
F_k=
\binom{n+2}{4k}\binom{h+m-k}{m-k},
\tag{10}
$$


and


$$
Y_{4k+2}\equiv0\pmod4,
\tag{11}
$$




$$
X_{4k+2}\equiv
\binom{M-1}{k}
\binom{h+m-k-1}{m-k-1}\pmod4,
\quad 0\le k<m.
\tag{12}
$$


These reductions retain the complete residual, finite inverse correction, and actual large binomials. The following additional support conclusions are new.

### 2.1 Positions $4k+2$

Since


$$
v_2(M-1)=4,
$$


if $4\nmid k$, then


$$
v_2\binom{M-1}{k}
\ge 4-v_2(k)\ge3.
$$


If $4\mid k$, put $\ell=m-k$. Then


$$
\ell-1\equiv3\pmod4,\qquad h\equiv1\pmod4.
$$


Adding $h$ and $\ell-1$ produces carries at both of the first two binary positions. Hence


$$
4\mid\binom{h+\ell-1}{\ell-1}.
$$


Thus (12) strengthens to


$$
\boxed{
X_{4k+2}\equiv Y_{4k+2}\equiv0\pmod4.
}
\tag{13}
$$



### 2.2 Positions $4k$ outside $\mathcal P$

Binary scaling preserves the valuation


$$
v_2\binom{n+2}{4k}=v_2\binom Mk.
$$


Put $\ell=m-k$, so the other factor is $\binom{h+\ell}{\ell}$.

If $k$ is odd, this second binomial is even. The first can be odd only when


$$
k\equiv1,17\pmod{32}.
$$


In those two cases $\ell\equiv19,3\pmod{32}$, respectively, so $\ell\equiv3\pmod4$, and the second binomial is divisible by $4$. Therefore $4\mid F_k$ for every odd $k$.

Now let $k$ be even and outside the residues $0,16\bmod32$.

* If $v_2\binom Mk\ge2$, there is nothing to prove.
* If $v_2\binom Mk=1$, examination of the five low digits of
  $M\equiv17\pmod{32}$ forces
  

$$
k=32t+8
$$


  and no carry in the remaining binomial $\binom Ct$. Thus $t$ is a binary submask of $C$, in particular $t$ is even.
  Since $D$ is odd,
  

$$
\ell=32(D-t)+12
$$


  has its $2^5$-digit set. The same digit of $h=64C+33$ is set, so the second binomial is even.

It follows that


$$
4\mid F_k
\qquad
\bigl(k\not\equiv0,16\pmod{32}\bigr).
$$


Together with (9),


$$
\boxed{
X_j\equiv Y_j\equiv0\pmod4
\quad
(j\ \text{even},\ j\notin\mathcal P).
}
\tag{14}
$$



This includes all off-pair even positions, not just those previously contributing to a selected scalar sum.

---

## 3. New odd-coordinate refinement: $8\mid X_j$

The earlier divisibility $4\mid X_j$ at odd coordinates is not, by itself, enough for the present scalar. The stronger statement needed here is


$$
\boxed{X_j\equiv0\pmod8\quad(j\ \text{odd}).}
\tag{15}
$$



### 3.1 Weight classes

For a nonterminal odd coordinate $j=4k+a$, $a=1,3$,


$$
W_j=\frac{4M}{j}\binom{4M-1}{j-1}.
$$


The two low digits introduce no borrow, so


$$
v_2(W_j)=2+v_2\binom{M-1}{k}.
\tag{16}
$$



If $v_2(W_j)\ge4$, (15) follows directly from $X_j=W_j(j\theta_{j-1}-\theta_j)/2$.

If $v_2(W_j)=3$, then $k$ is even: an odd $k$ would make $\binom{M-1}{k}$ divisible by $16$. The complete parity formula for $\theta$ is


$$
\theta_{4k}=0,\qquad
\theta_{4k+a}
=\binom{h+m-k-1}{m-k-1}\pmod2,
\quad a=1,2,3.
\tag{17}
$$


For $a=3$, the reconstruction difference is even by cancellation. For $a=1$, $k$ is even, so $m-k-1$ and $h$ are odd, making the binomial in (17) even. Thus the reconstruction difference is again even, proving (15) in this weight class.

It remains to treat $v_2(W_j)=2$.

### 3.2 The unit-weight case, using the complete $P$-lift modulo $4$

Now Lucas gives


$$
k=32t\quad\text{or}\quad k=32t+16,
\qquad \binom Ct\ \text{odd}.
$$


Thus $t$ is even and


$$
\ell=m-k=32(D-t)+20
\quad\text{or}\quad32(D-t)+4,
\tag{18}
$$


with $D-t$ odd. In particular, $4\mid\ell$.

For a coordinate $j$, set


$$
L=b-1-j,\qquad
\mathcal M_v(j)=\binom{2n+L}{L-v}.
$$


Modulo $4$,


$$
P(X)=2+3X+3\binom X2+\binom X3.
$$


Finite moment summation gives


$$
\theta_j=(-1)^j
\left(P(j)\mathcal M_0(j)+2(3+j)\mathcal M_2(j)\right)\pmod4.
\tag{19}
$$


Here the bounded moment coefficients are exactly


$$
\binom{2n+v-1}{v}\equiv(1,0,2,0)_v\pmod4,
\qquad 0\le v\le3.
$$



Writing $D_j^P=j\theta_{j-1}-\theta_j$, (19) yields, at the relevant residues,


$$
D_j^P\equiv
2\mathcal M_{-1}+3\mathcal M_0
+2\mathcal M_1+2\mathcal M_2\pmod4
\quad(j\equiv1\pmod{64}),
\tag{20}
$$


and


$$
D_j^P\equiv
\mathcal M_{-1}+2\mathcal M_0
+2\mathcal M_1+2\mathcal M_2\pmod4
\quad(j\equiv3\pmod{64}).
\tag{21}
$$



For $j=4k+1$, put $T=h+\ell$. The upper argument in these binomials is $4T-1$. Since $4\mid\ell$ and $T$ is odd,


$$
\mathcal M_0
=\frac{\ell}{T}\binom{4T}{4\ell}\equiv0\pmod4.
$$


Odd-denominator adjacent ratios give $\mathcal M_1,\mathcal M_2\equiv0\pmod4$. Also


$$
\mathcal M_{-1}
=\frac hT\binom{4T}{4\ell}
$$


is even: by (18), both $h$ and $\ell$ have their $2^5$-digits set. Equation (20) therefore gives $D_j^P\equiv0\pmod4$.

For $j=4k+3$, the upper argument is $4T-3\equiv1\pmod{16}$. The lower arguments for $\mathcal M_{-1},\mathcal M_0,\mathcal M_1,\mathcal M_2$ are respectively congruent to


$$
14,\ 13,\ 12,\ 11\pmod{16}.
$$


Kummer gives $4\mid\mathcal M_{-1}$ and $2\mid\mathcal M_0,\mathcal M_1,\mathcal M_2$. Equation (21) again gives $D_j^P\equiv0\pmod4$.

Since $W_j/4$ is a unit, this proves $8\mid X_j$ in the final weight class.

### 3.3 Endpoint

The actual endpoint remains


$$
X_b=\frac{W_b\,b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4}.
\tag{22}
$$


The retained endpoint bound $v_2(W_b)\ge6$ gives


$$
v_2(X_b)\ge5,\qquad v_2(Y_b)\ge4.
\tag{23}
$$


Thus the endpoint is included in (15), with its $Q$-column $1$ retained before valuation.

---

## 4. Paired coordinates: evaluate the full seven-boundary difference

The decisive paired assertion is


$$
\boxed{
X_j-Y_j\equiv0\pmod8
\qquad(j\in\mathcal P).
}
\tag{24}
$$



This requires the complete raw precisions, including both new factorial tails.

### 4.1 Remove the bounded translation, not the large kernel

Put


$$
d_r=q_r-2p_r\pmod{32}.
$$


From (5)–(6),


$$
(d_0,\ldots,d_{11})
=(16,6,10,28,16,24,24,0,0,16,16,0)\pmod{32}.
\tag{25}
$$



For $64\mid j$, bounded binomial translation gives


$$
P(j+q)\equiv P(q)\pmod{16},\qquad
Q(j+q)\equiv Q(q)\pmod{32}.
\tag{26}
$$


For example, $\binom ja$ has valuation at least $6-\lfloor\log_2a\rfloor$, while the coefficients above degree $3$ carry the additional factors displayed in (5)–(6).

Likewise, because $2n-4=128(2C+1)$, the bounded moment coefficients may be replaced by


$$
\binom{2n+v-1}{v}\longmapsto\binom{v+3}{3}.
\tag{27}
$$


The loss is at most three bits for $v\le11$, leaving four bits; every $d_v$ is even, so (27) is sufficient modulo $32$.

Define the fixed reference coefficient sequence, for $L\ge0$, by


$$
\begin{aligned}
K(L)={}&
\sum_{a=0}^{6}(-1)^aB_a^+\binom{L+a+4}{3}\\
&+\sum_{r=0}^{11}
d_r\binom{r+3}{3}\binom{L+4}{r+4}
\pmod{32}.
\end{aligned}
\tag{28}
$$


All seven boundary values occur in this formula.

Its generating expression has Laurent support down to degree $-7$:


$$
\begin{aligned}
\mathcal K(z)={}&
(1-z)^{-4}\sum_{a=0}^{6}(-1)^aB_a^+z^{-1-a}\\
&+(1-z)^{-5}
\sum_{r=0}^{11}d_r\binom{r+3}{3}z^r.
\end{aligned}
\tag{29}
$$


For $j\in\mathcal P$, with $L=b-1-j$,


$$
\eta_j-2\theta_j
\equiv[z^L](1-z)^{-128(2C+1)}\mathcal K(z)
\pmod{32}.
\tag{30}
$$


This is still the actual large kernel at the actual $n,b,j$.

### 4.2 Evaluate the sampled polynomial

The two properties needed are


$$
\boxed{K(8s)\equiv0\pmod2,}
\tag{31}
$$


and


$$
\boxed{K(16s)\equiv16\pmod{32}\qquad(s\ge0).}
\tag{32}
$$



Property (31) follows directly from (28): all $d_r$ and all boundary coefficients except $B_0^+$ are even, while $\binom{8s+4}{3}$ is even.

Here is an explicit proof of (32).

For the boundary part, Vandermonde expansion in $\binom{16s}{i}$ gives the four coefficients


$$
(1440,\ 572,\ 142,\ 17).
$$


Modulo $32$, the constant and linear terms vanish. Moreover,


$$
142\binom{16s}{2}\equiv16s,\qquad
17\binom{16s}{3}\equiv16s\pmod{32}.
$$


Thus the **whole seven-boundary part** is zero modulo $32$.

For the polynomial part, (25) reduces it to


$$
\begin{aligned}
&16\binom{16s+4}{4}
+24\binom{16s+4}{5}
+4\binom{16s+4}{6}\\
&\hspace{25mm}
+16\binom{16s+4}{7}
+16\binom{16s+4}{8}\pmod{32}.
\end{aligned}
\tag{33}
$$


The first binomial is odd. The other four have respective valuation lower bounds


$$
2,\ 3,\ 1,\ 1.
$$


These bounds follow immediately from the low digits, or the factorial products for lower indices $5,6$. Hence (33) is $16\bmod32$, proving (32).

This is a polynomial/binomial derivation, not a finite sampling inference.

### 4.3 Perform the unrestricted convolution

Set $E=2C+1$. The binary power congruence is


$$
(1-z)^{-128E}\equiv(1-z^8)^{-16E}\pmod{32}.
\tag{34}
$$


Every paired $L$ is divisible by $16$. Consequently the convolution in (30) samples only $K(8s)$. No negative boundary degree contributes: the only negative degrees in (29) are $-7,\ldots,-1$, whereas all sampled degrees are multiples of $8$.

If the kernel index $v$ is odd, then


$$
v_2\binom{16E+v-1}{v}\ge4,
$$


so its product with (31) vanishes modulo $32$.

For even $v$, (32) applies. Only the parity of the kernel matters, and


$$
(1-z)^{-16E}\equiv(1-z^{16})^{-E}\pmod2.
$$


Therefore


$$
\frac{\eta_j-2\theta_j}{16}
\equiv
\binom{E+\lfloor L/128\rfloor}{\lfloor L/128\rfloor}
\pmod2.
\tag{35}
$$



For the pair $j=128t,128t+64$, write $d=D-t$. Its two $L$-values are $128d+80$ and $128d+16$. Thus both give


$$
\frac{\eta_j-2\theta_j}{16}
\equiv\binom{2C+1+d}{d}\pmod2.
\tag{36}
$$



The reconstruction terms multiplied by $j$ vanish at the required precision. Hence


$$
\frac{X_j-Y_j}{4}
\equiv
W_j\frac{\eta_j-2\theta_j}{16}
\equiv
\binom Ct\binom{2C+1+D-t}{D-t}\pmod2.
\tag{37}
$$


The right side is zero: if $\binom Ct$ is odd, then $t$ is even; $D-t$ is consequently odd, and $2C+1$ is odd, forcing the second binomial to be even.

This proves (24), on the entire original domain.

---

## 5. Evaluation of the combined scalar

The coordinate classes now give an especially simple conclusion.

* **Paired positions:** $2\mid X_j$ and $8\mid Y_j-X_j$.
* **Off-pair even positions:** $4\mid X_j,Y_j$, by (13)–(14).
* **Odd positions:** $8\mid X_j$ and $2\mid Y_j$, by (15) and the retained whole-column evenness.
* **Endpoint:** the stronger bounds (23) apply to the complete endpoint.

In every case,


$$
X_j(Y_j-X_j)\equiv0\pmod{16}.
$$


Therefore the complete contracted difference satisfies


$$
\boxed{
H-N=\sum_{j=0}^{b}X_j(Y_j-X_j)\equiv0\pmod{16}.
}
\tag{38}
$$



Once divisibility by $8$ is established—as it is independently in the next section—this evaluates the assigned scalar:


$$
\boxed{\Delta_3=0.}
$$



The result is stronger than cancellation after summation: the summands of the complete defect are individually divisible by $16$. It does not, however, assert deeper coordinatewise divisibility.

---

## 6. The actual next norm digit also vanishes

Only paired coordinates can contribute to $N\bmod16$, since $4\mid X_j$ everywhere else.

For $0\le t\le D$, define the actual integer


$$
E_t=\binom Ct\binom{2C+1+D-t}{D-t}.
\tag{39}
$$


Every $E_t$ is even, by the carry argument used in (37).

At the two positions $j=128t,128t+64$, the low-digit blocks introduce no additional carries in either binomial defining $F_k$. Kummer therefore gives


$$
v_2(F_{32t})=v_2(F_{32t+16})=v_2(E_t).
\tag{40}
$$


The factors $k+1$ in (9) are odd at both positions. Thus


$$
\frac{X_{128t}}2
\equiv
\frac{X_{128t+64}}2
\equiv\frac{E_t}{2}\pmod2.
\tag{41}
$$



An even square is $4\bmod16$ precisely when its half is odd. Summing each pair yields


$$
N\equiv
8\sum_{t=0}^{D}\frac{E_t}{2}\pmod{16}.
\tag{42}
$$


In particular, this already proves $8\mid N$, without assuming the separately audited norm claim.

The remaining scalar is an exact convolution:


$$
\sum_{t=0}^{D}E_t
=[z^D](1+z)^C(1-z)^{-2C-2}.
\tag{43}
$$


Put $C=2c$. On the original domain, $c$ is odd. Modulo $4$,


$$
(1+z)^{2c}
\equiv(1+z^2)^c+2cz(1+z^2)^{c-1},
$$




$$
(1-z)^{-2(C+1)}
\equiv
(1+z^2)^{-(C+1)}
+2(C+1)z(1+z^2)^{-(C+2)}.
$$


Their odd part is therefore


$$
2(3c+1)z(1+z^2)^{-c-2}\pmod4.
\tag{44}
$$


Because $c$ is odd, $3c+1$ is even. All odd coefficients in (43) vanish modulo $4$; $D$ is odd, so


$$
\sum_{t=0}^{D}E_t\equiv0\pmod4.
\tag{45}
$$



Combining (42)–(45),


$$
\boxed{\frac N8\equiv0\pmod2.}
\tag{46}
$$


Then (38) gives the corresponding mixed digit:


$$
\boxed{
N\equiv H\equiv0\pmod{16},\qquad
\alpha,\gamma\ge4.
}
\tag{47}
$$



The condition used in (44), namely $C/2$ odd, holds automatically for every $r=18+32u$. There is no further restriction or omitted subclass.

---

## 7. Final gcd, primitive denominator, and whole real error

The complete actual center remains


$$
c_n=\frac{2b!}{\lambda R}\frac{H}{N}.
\tag{48}
$$



Let $d_B$ be the least common denominator of the actual two-column lift, and retain


$$
N_B=d_B[u,v].
$$


For the specified falling-factorial metric,


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
\tag{49}
$$


Thus $1/g_B$ is the final primitive normalization of the integer pair, and $q_n$, not $d_B$ or a row-clearer, is the actual rational denominator and primitive multiplier of $S$.

With $s=s_2(n)$, the exact binary interface is unchanged:


$$
v_2(g_B)=
\min\left\{
3n-2s+2+\alpha,\,
\frac{3n}{2}-s+v_2(b!)+3+\gamma
\right\},
\tag{50}
$$




$$
\boxed{
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s-1-(\gamma-\alpha)
\right\}.
}
\tag{51}
$$



The newly proved $\alpha,\gamma\ge4$ does **not** bound their difference. Nor does (38) establish all-depth equality.

For the retained complete signed-error theorem on this fixed-ratio family,


$$
\epsilon_n=c_n-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
\tag{52}
$$


The whole primitive evaluated form remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
}
\quad\text{eventually}.
\tag{53}
$$


Its nonvanishing and error refer to the complete exponential residual, logarithmic force, endpoint, actual columns, and actual metric.

---

# Concluding ledger

## (1) New result and proof status

**Proved using the existing complete lift, on every original index**


$$
b=9^r,\quad n=4002b,\quad r=18+32u,\quad u\ge0:
$$



- Off-pair even coordinates satisfy $4\mid X_j,Y_j$.
- Every odd coordinate satisfies $8\mid X_j$, including the endpoint.
- Paired coordinates satisfy $8\mid X_j-Y_j$.
- The complete seven-boundary sampled polynomial satisfies
  

$$
K(16s)=16\pmod{32},
$$


  and its actual large-kernel convolution has been evaluated.
- Consequently,
  

$$
\boxed{\Delta_3=0.}
$$


- The next actual norm digit is also evaluated:
  

$$
\boxed{N/8=0\pmod2,\qquad \alpha,\gamma\ge4.}
$$



No additional raw precision, additional index subclass, or finite growing-index evidence was needed.

## (2) Exact remaining bottleneck

The new proof is still finite-depth. The next discrepancy is


$$
\frac{H-N}{16}\pmod2,
$$


and the present coordinatewise divisibility does not evaluate it.

The substantive arithmetic goal remains a justified all-depth estimate such as


$$
\boxed{\gamma-\alpha\le2000b+o(n),}
$$


with every necessary factorial-tail enlargement, finite-boundary correction, and scalar carry retained. The current degree-$17/15$ closure cannot be iterated indefinitely without a uniform proof.

No irrationality or rationality conclusion for $e+\pi$ follows.

## (3) Computation request

**None.** The supplied fixed-operator coefficients suffice. The new sampled-polynomial identity, the unrestricted paired convolution, the off-pair divisibility, and the norm convolution have explicit derivations above; no additional finite computation is being proposed as evidence for the infinite assertions.
