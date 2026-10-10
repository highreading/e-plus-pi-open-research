> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 — the fourth contracted carry is zero on the original domain

On the unchanged index domain


$$
\boxed{
b=9^r,\qquad n=4002b,\qquad r=18+32u,\quad u\ge0,
}
$$


I obtain


$$
\boxed{\frac{H-N}{16}\equiv0\pmod2.}
$$


Thus


$$
\boxed{H\equiv N\pmod{32}.}
$$



The cancellation is genuinely contracted. At this depth, I do **not** obtain divisibility by $32$ of every individual defect summand. The paired positions and certain shifted odd positions cancel in pairs; the remaining even positions vanish individually.

The proof derives the complete lift at raw precisions $32,64$, including:

* the contact identity in the integral divided-power ring;
* a separate calculation of the normalized $P$-forcing;
* all seven factorial residues and boundary values modulo $64$;
* a correction in the degree-three boundary polynomial that is invisible modulo $16$;
* degree bounds $21,19$, with the weighted parameter-substitution losses accounted for.

The actual norm digit $N/16\bmod2$ is not evaluated here. Consequently, the conclusion is


$$
\alpha=\gamma=4
\quad\text{or}\quad
\alpha,\gamma\ge5,
$$


not an assertion selecting one of these alternatives.

No conclusion about rationality or irrationality of $e+\pi$ follows.

---

## 1. Domain, actual columns, and precision

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


The metric remains exactly


$$
W_j=\binom{n+2}{j},\qquad
\omega_j=j!W_j=(n+2)_{\underline j},\qquad
\Omega=\operatorname{diag}(\omega_j^2),
\quad 0\le j\le b.
$$


Every finite contact inverse below has indices $0\le i,j<b$.

Write


$$
N=X^TX,\qquad H=X^TY,\qquad
\alpha=v_2(N),\qquad \gamma=v_2(H).
$$


The retained norm positivity and original-family mixed nonvanishing make both valuations finite.

As before, set


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532,
$$




$$
m=\frac{b-1}{4}=32D+20,\qquad
M=\frac{n+2}{4}=32C+17.
$$


On every assigned index,


$$
D\ \text{is odd},\qquad C\equiv2\pmod4,\qquad
h=64C+33.
\tag{1}
$$



I reuse the established lower-layer conclusions


$$
X,Y\in2\mathbb Z_2^{b+1},\qquad N,H\in16\mathbb Z_2.
\tag{2}
$$


Because both columns are even, $X,Y\bmod16$ determine $H-N\bmod32$. Hence the complete raw representatives required here are


$$
A_j\equiv2X_j\pmod{32},\qquad
B_j^{\rm act}\equiv4Y_j\pmod{64}.
\tag{3}
$$


The earlier raw precisions $16,32$ cannot simply be substituted for (3).

---

# Part I. The complete $32/64$ lift

## 2. Audit of the contact congruence modulo $64$

Work in the integral divided-power ring, whose basis elements satisfy


$$
x^{[a]}x^{[b]}=\binom{a+b}{a}x^{[a+b]}.
$$


Thus products of integral divided-power coefficient vectors remain integral.

Here


$$
\phi^2=1+2U,
$$


where the divided-power coefficients of $U$ are


$$
(-1,2,-3,3)
$$


in degrees $1,2,3,4$. In ordinary polynomial notation,


$$
U=-x+x^2-\frac{x^3}{2}+\frac{x^4}{8}.
$$


The apparent ordinary denominators do not constitute a loss in the divided-power ring.

Put


$$
h=1+32e,\qquad e=2C+1\ \text{odd}.
$$


For $k=2,3,4,5$, respectively,


$$
v_2\binom hk=4,4,3,3.
$$


Therefore


$$
v_2\!\left(2^k\binom hk\right)\ge6.
$$


For $k\ge6$, the factor $2^k$ alone suffices. Also


$$
2(h-1)U\in64\mathbb Z_2\langle x\rangle.
$$


Consequently,


$$
\boxed{\phi^{2h}=(1+2U)^h\equiv1+2U=\phi^2\pmod{64}.}
\tag{4}
$$



This proves the coordinator’s contact observation at the stated precision. It does **not** determine the normalized $P$-forcing; that calculation is separate below.

The actual contact correction is therefore still


$$
E_{ij}=
\sum_{s=1}^4c_s\sum_{t=0}^s
 \binom i{s-t}\binom nt
 \binom{-t}{j+s-i-t},
\qquad(c_1,c_2,c_3,c_4)=(-1,2,-3,3),
\tag{5}
$$


at its required precision.

---

## 3. Seven actual factorial residues and the whole-force cutoff

Let


$$
f_a=\frac{(b+a)!}{b!}.
$$


Since $b\equiv17\pmod{64}$, direct multiplication gives


$$
\boxed{
(f_0,f_1,\ldots,f_6)
\equiv(1,18,22,56,24,16,48)\pmod{64}.
}
\tag{6}
$$



For clarity, these are recomputed modulo $64$, not copied from the modulo-$32$ lift:


$$
\begin{array}{c|c|c}
a&f_a\bmod64&v_2(f_a)\\ \hline
0&1&0\\
1&18&1\\
2&22&1\\
3&56&3\\
4&24&3\\
5&16&4\\
6&48&4
\end{array}
$$


Moreover $b+7\equiv24\pmod{64}$, so


$$
\boxed{v_2(f_7)=7.}
\tag{7}
$$


All later factorial tails have valuation at least $7$. They therefore vanish modulo $64$ before application of the integral contact and inverse operators. This proves the complete exponential-tail cutoff at $b,\ldots,b+6$.

The full logarithmic forcing satisfies the retained whole-force estimate


$$
v_2(h_i^F/b!)
\ge h+1-2\lfloor\log_2(2n+b-1)\rfloor-v_2(b!).
\tag{8}
$$


Since $h=2001b$ and $v_2(b!)\le b-1$, its right side is greater than $6$ throughout the present domain. Thus its omission modulo $64$ concerns the **whole force**, not one selected term.

Define the seven exterior values


$$
B_a=\sum_{u=a}^6f_u\binom{2n}{u-a}.
$$


Using $2n\equiv132\pmod{256}$ and (6) gives


$$
\boxed{
(B_0,\ldots,B_6)
\equiv(5,42,54,56,56,16,48)\pmod{64}.
}
\tag{9}
$$


For example, the needed bounded binomial residues are


$$
\binom{2n}{1}\equiv4\pmod{32},\quad
\binom{2n}{2}\equiv6\pmod{32},
$$




$$
\binom{2n}{3}\equiv4\pmod8,\quad
\binom{2n}{4}\equiv1\pmod8,\quad
\binom{2n}{5},\binom{2n}{6}\equiv0\pmod4.
$$


Together with the valuations in the table, these determine every entry in (9).

---

## 4. The normalized $P$-forcing modulo $32$

The normalized central formulas supplied in the archive give


$$
B^{\rm cen}_0\equiv2,\qquad
B^{\rm cen}_1\equiv B^{\rm cen}_2\equiv3\pmod{32},
\qquad
B^{\rm cen}_\ell\equiv0\pmod{32}\quad(\ell\ge3).
\tag{10}
$$



Here is the precision check.

* For $\ell\ge3$, the falling-factorial prefactor contains $h-1$, of valuation $5$. The remaining normalized sum is $2$-integral.
* For $\ell=0$, all terms with central summation index $r\ge2$ vanish modulo $32$: for $2\le r\le7$, the two binomial factors contribute enough depth, and for $r\ge8$, $v_2(r!)\ge7$.
* For $\ell=1,2$, the $r=1$ term contains $(h-1)(h+1)$, of valuation $6$; the $r=2$ term has depth at least $5$; the remaining terms vanish by the same bounded-index estimates.

Substitution into the exact normalized forcing formula, using the actual factorial products, yields


$$
\boxed{
f^0/R\equiv(2,9,19,25,12,4,16,16,0,\ldots)\pmod{32}.
}
\tag{11}
$$


In particular, the indices $6,7$ do **not** vanish modulo $32$. From index $8$ onward, the remaining factorial product already has depth at least $5$.

After inverse-Pascal transformation, the complete signed forcing is


$$
\boxed{
\begin{aligned}
g_{32}(X)={}&2-9X+19\binom X2-25\binom X3
 +12\binom X4-4\binom X5\\
&+16\binom X6-16\binom X7
\pmod{32}.
\end{aligned}}
\tag{12}
$$


This calculation is independent of the contact congruence (4).

---

## 5. The corrected boundary polynomial modulo $32$

There is a new boundary correction at this precision.

Because $n=2+64e$, with $e$ odd,


$$
\binom n1\equiv2,\quad
\binom n2\equiv1,\quad
\binom n3\equiv0,\quad
\binom n4\equiv16\pmod{32}.
$$


Thus, if $E_0$ denotes the $n=2$ contact operator,


$$
\boxed{E\equiv E_0+16T(-4)\pmod{32}.}
\tag{13}
$$


This correction is invisible in the earlier boundary calculation modulo $16$.

For exterior columns, the reference formula is


$$
(E_0)_{ik}=(-1)^{k-i}\bigl((k-i)B_i^\circ+D_i^\circ\bigr),
$$


where


$$
B_i^\circ=2+3i+3\binom i2,\qquad
D_i^\circ=2i+3\binom i2-6\binom i3.
$$


From (9),


$$
\sum_{a=0}^6(-1)^aB_a=49,\qquad
\sum_{a=0}^6a(-1)^aB_a=330.
$$


The reference part of the signed boundary polynomial is therefore


$$
10+18X+24\binom X2+31\binom X3\pmod{32}.
$$


The correction from (13) is


$$
-16\binom{84-X}{3}
\equiv16\left(X+\binom X3\right)\pmod{32}.
$$


Hence the complete boundary polynomial is


$$
\boxed{
a_{32}(X)=10+2X+24\binom X2+15\binom X3\pmod{32}.
}
\tag{14}
$$



In particular, merely lifting the earlier reference polynomial without the $16T(-4)$ contribution would give the wrong degree-three forcing.

---

## 6. Complete polynomial lift and degree bounds $21,19$

Let $\mathscr E_0$ be the signed finite-Newton operator at reference parameters $n=2,b=81$. For an integer-valued polynomial $f$, it satisfies


$$
E_0\mathcal S_{81}f=\mathcal S_{81}(\mathscr E_0f),
\qquad
(\mathcal S_bf)_i=(-1)^if(i).
$$



An explicit polynomial form, useful for bounded verification, is as follows. Put


$$
S_f(X)=\sum_{k=X}^{80}f(k),\qquad
T_f(X)=\sum_{k=X}^{80}(k-X+1)f(k),
$$


where the sums are interpreted by their integer-valued polynomial continuations. Then


$$
\begin{aligned}
\mathscr E_0f={}&
\left(2+3X+3\binom X2\right)T_f
+\left(-2-X-6\binom X3\right)S_f\\
&-6\binom X3f(X-1)
-\left(\binom X2+6\binom X3\right)f(X-2)\\
&-3\binom X3f(X-3)+3\binom X4f(X-4).
\end{aligned}
\tag{15}
$$


This follows directly by combining the $t=0,1,2$ terms of (5). It proves


$$
\deg(\mathscr E_0f)\le\deg f+4.
\tag{16}
$$


All operations are integral in the Newton basis.

Define


$$
P^\#=\sum_{\ell=0}^4(-2\mathscr E_0)^\ell g_{32}\pmod{32},
\tag{17}
$$




$$
Q^\#=2\sum_{\ell=0}^4(-2\mathscr E_0)^\ell a_{32}\pmod{64}.
\tag{18}
$$


The last two coefficients of $g_{32}$ have a factor $16$, so they disappear from every term with $\ell\ge1$. The remaining forcing has degree at most $5$. Therefore


$$
\boxed{\deg P^\#\le21,\qquad \deg Q^\#\le19.}
\tag{19}
$$


The first bound is not obtained by incorrectly asserting $\deg g_{32}\le5$.

### Weighted parameter transfer

The substitution $n=2,b=81$ is made only in these bounded polynomial operations. It is not made in the actual inverse range or in $T(-2n)$.

The estimate


$$
v_2\!\left(\binom{x+\delta}{a}-\binom xa\right)
\ge v_2(\delta)-\lfloor\log_2a\rfloor
\tag{20}
$$


gives the following bounds:



$$
\begin{array}{c|c|c|c}
\text{term}&\text{largest }b\text{-index}
&\text{available depth}&\text{required depth}\\ \hline
-2\mathscr Eg&9&4&4\\
4\mathscr E^2g&13&4&3\\
-8\mathscr E^3g&17&3&2\\
16\mathscr E^4g&21&3&1\\ \hline
-4\mathscr Ea&7&5&4\\
8\mathscr E^2a&11&4&3\\
-16\mathscr E^3a&15&4&2\\
32\mathscr E^4a&19&3&1
\end{array}
$$


The $n$-dependent lower indices are at most $4$, giving depth at least $4$. Thus all weighted requirements hold. The unweighted boundary correction was already retained separately in (14).

The actual solutions are consequently


$$
\theta=T(-2n)\mathcal S_bP^\#\pmod{32},
$$




$$
\eta_i=
-\sum_{a=0}^6B_a\binom{-2n}{b+a-i}
+\bigl(T(-2n)\mathcal S_bQ^\#\bigr)_i
\pmod{64}.
\tag{21}
$$


Extending by zero at $-1,b$, reconstruct


$$
A_j=W_j(j\theta_{j-1}-\theta_j)\pmod{32},
$$




$$
B_j^{\rm act}
=W_b\mathbf1_{j=b}+W_j(j\eta_{j-1}-\eta_j)\pmod{64}.
\tag{22}
$$


These are the complete raw representatives in (3).

---

# Part II. Evaluation of the paired contribution

## 7. A new sampled-polynomial periodicity

Let


$$
d_r=[\binom Xr](Q^\#-2P^\#).
$$


The retained lower-precision coefficients give


$$
(d_0,\ldots,d_{11})
\equiv(16,6,10,28,16,24,24,0,0,16,16,0)\pmod{32},
\tag{23}
$$


and $d_r\equiv0\pmod{32}$ for $12\le r\le21$.

For $L\ge0$, define


$$
\boxed{
K(L)=
\sum_{a=0}^6(-1)^aB_a\binom{L+a+4}{3}
+\sum_{r=0}^{21}
d_r\binom{r+3}{3}\binom{L+4}{r+4}
\pmod{64}.
}
\tag{24}
$$


This includes the new complete forces from Part I.

The correct reference generating series is


$$
\mathcal K(z)=
(1-z)^{-4}\sum_{a=0}^6(-1)^aB_az^{-1-a}
+\sum_{r=0}^{21}
d_r\binom{r+3}{3}\frac{z^r}{(1-z)^{r+5}}.
\tag{25}
$$


The denominator of the $r$-th Newton term is $(1-z)^{r+5}$, not a common $(1-z)^5$. Keeping this $r$-dependence is necessary for the coefficient identity (24).

For $64\mid j$, bounded translation and bounded moment reduction give


$$
\eta_j-2\theta_j
\equiv[z^L](1-z)^{-128e}\mathcal K(z)\pmod{64},
\qquad L=b-1-j.
\tag{26}
$$


The losses are covered by (23): for example, replacing
$\binom{2n+r-1}{r}$ by $\binom{r+3}{3}$ loses at most
$\lfloor\log_2r\rfloor$ of the seven available bits, and the $d_r$ supply the remaining factors.

### Three sampled facts

The following are sufficient:


$$
K(4s)\equiv0\pmod4,
\tag{27}
$$




$$
K(16s)\equiv16\pmod{32},
\tag{28}
$$




$$
\boxed{K(16s+64)\equiv K(16s)\pmod{64}.}
\tag{29}
$$



Equation (28) is the retained complete seven-boundary sampled identity. The new facts (27), (29) follow directly from (24).

Indeed, the boundary part has Newton coefficients


$$
(6272,2396,526,49)
$$


in degrees $0,1,2,3$. These prove (27) for the boundary part and prove its $64$-periodicity on multiples of $16$.

For the polynomial part, put


$$
m_r=d_r\binom{r+3}{3}.
$$


Equation (23) gives


$$
v_2(m_r)\ge\lfloor\log_2(r+4)\rfloor
\qquad(0\le r\le21).
\tag{30}
$$


Vandermonde and


$$
v_2\binom{64}{a}\ge6-\lfloor\log_2a\rfloor
$$


then prove its $64$-periodicity. Also every $m_r$ is divisible by $4$, proving the rest of (27).

Thus


$$
K(16)=16\kappa,\qquad \kappa\ \text{odd modulo }4,
\tag{31}
$$


and its actual value is unnecessary.

---

## 8. Perform the unrestricted convolution

The binary power congruence is


$$
(1-z)^{-128e}\equiv(1-z^4)^{-32e}\pmod{64}.
\tag{32}
$$


Write its coefficient at $z^{4v}$ as


$$
c_v=\binom{32e+v-1}{v}.
$$


For $v>0$,


$$
v_2(c_v)\ge5-v_2(v).
\tag{33}
$$



Suppose $16\mid L$. In the convolution:

* odd $v$ vanish by (27), (33);
* $v\equiv2\pmod4$ vanish by the same facts;
* $v\equiv4\pmod8$ vanish by (28);
* $v\equiv8\pmod{16}$ vanish by (28).

Only $v=16w$ remain. By (29), their sampled factor is $K(L)$. Since this factor has depth $4$, only


$$
c_{16w}\equiv\binom{2e+w-1}{w}\pmod4
$$


is required. Consequently,


$$
\eta_j-2\theta_j
\equiv
K(L)\binom{2e+\lfloor L/64\rfloor}{\lfloor L/64\rfloor}
\pmod{64}.
\tag{34}
$$



The only possible negative sampled boundary degree is $-4$; its kernel index is odd, and its boundary coefficient is divisible by $4$. It therefore vanishes by (33). No endpoint of the Laurent convolution has been deleted without a valuation check.

Now take the prescribed pair


$$
j_0=128t,\qquad j_1=128t+64,\qquad 0\le t\le D,
$$


and put $d=D-t$. The two values of $L$ are $128d+80$ and $128d+16$, both $16\bmod64$. Let


$$
Z_d=\binom{e+d}{d}.
$$


Binary scaling and an adjacent-binomial ratio give


$$
\binom{2e+2d}{2d}\equiv Z_d\pmod4,
$$




$$
\binom{2e+2d+1}{2d+1}\equiv3Z_d\pmod4.
\tag{35}
$$


Thus the two values of $(\eta_j-2\theta_j)/16$ are


$$
3\kappa Z_d,\qquad \kappa Z_d\pmod4.
\tag{36}
$$



The two weights satisfy


$$
W_{128t}\equiv W_{128t+64}\equiv\binom Ct\pmod4.
\tag{37}
$$


For example, after the modulo-$4$ binary scaling to $\binom Mk$, the correction in
$(1+z)^{32C}$ has coefficient $2C$, which vanishes modulo $4$ because $C$ is even.

Define the actual integer


$$
E_t=\binom Ct\binom{2C+1+D-t}{D-t}.
\tag{38}
$$


Every $E_t$ is even on the original domain. Therefore the two expressions in (36), after multiplication by the weights, are equal modulo $4$. Since $\kappa$ is odd,


$$
\boxed{
\frac{X_{128t}-Y_{128t}}8
\equiv
\frac{X_{128t+64}-Y_{128t+64}}8
\equiv\frac{E_t}{2}\pmod2.
}
\tag{39}
$$



The retained first-column formula also gives


$$
\frac{X_{128t}}2
\equiv\frac{X_{128t+64}}2
\equiv\frac{E_t}{2}\pmod2.
\tag{40}
$$


Hence the two fourth-defect contributions of every pair are equal and cancel:


$$
\boxed{
\sum_{j\in\mathcal P}\frac{X_j(Y_j-X_j)}{16}=0\pmod2.
}
\tag{41}
$$



This is an infinite convolution evaluation. It does not depend on a computed value of $\kappa$.

---

# Part III. Off-pair even and odd contributions

## 9. Even coordinates: a further support refinement

The new support statement needed here is


$$
\boxed{
8\mid X_j\qquad
(j\ \text{even},\ 32\nmid j).
}
\tag{42}
$$


Together with the retained $4\mid X_j,Y_j$ off the prescribed pairs, this makes all such defect summands divisible by $32$.

I give the details because the earlier modulo-$4$ support statement alone does not suffice.

### 9.1 Positions $j=4k+2$

Put $\ell=m-k$ and


$$
B=\binom{4(h+\ell)-2}{4\ell-2}.
$$


The retained complete moment calculation gives


$$
D_j^P:=j\theta_{j-1}-\theta_j
\equiv(1-2k)B\pmod4.
\tag{43}
$$


Also


$$
v_2(W_j)=1+v_2\binom{M-1}{k}.
\tag{44}
$$



If $v_2(W_j)=1$, Lucas forces


$$
k=32t\quad\text{or}\quad32t+16,\qquad \binom Ct\ \text{odd}.
$$


Thus $t$ is even and $D-t$ is odd. The integer $\ell-1$ has its bits $0,1,5$ set, whereas $h$ has bits $0,5$ set. Kummer gives $v_2(B)\ge3$.

At these residues $j\equiv2\pmod{64}$, the complete $P\bmod8$ moment formula is


$$
D_j^P\equiv-
\left(2\mathcal M_{-1}+\mathcal M_0
 +2\mathcal M_2+4\mathcal M_3+4\mathcal M_4\right)\pmod8,
\tag{45}
$$


where


$$
\mathcal M_v=\binom{2n+b-1-j}{b-1-j-v}.
$$


Here $\mathcal M_0=B$. Adjacent-binomial valuations give


$$
v_2(\mathcal M_{-1}),v_2(\mathcal M_2)\ge3,\qquad
v_2(\mathcal M_3)\ge3,\qquad
v_2(\mathcal M_4)\ge2.
$$


Thus $D_j^P\equiv0\pmod8$.

If $v_2(W_j)=2$, the possible low residues of $k$ are $0,8,16\bmod32$. In each case $\ell-1\equiv3\pmod4$, so $v_2(B)\ge2$, and (43) suffices.

If $v_2(W_j)=3$, then $k$ is even, so $\ell-1$ and $h$ are odd. Thus $B$ is even. Larger weight valuations are immediate.

Therefore


$$
\boxed{8\mid X_{4k+2}\quad(0\le k<m).}
\tag{46}
$$



### 9.2 Positions $j=4k$

Put


$$
B=\binom{4(h+m-k)}{4(m-k)},\qquad
w=v_2(W_{4k})=v_2\binom Mk.
$$


The complete lower-precision formula is


$$
D_{4k}^P\equiv-2(k+1)B\pmod8.
\tag{47}
$$



For $w=1$, the only even low residue that can survive in $X/4$ is $k\equiv8\pmod{32}$. Odd $k$ give $(k+1)B\in4\mathbb Z_2$.

For $w=2$, the only possible surviving even residues are


$$
k\equiv8,24\pmod{32}.
$$


Indeed, the other even low residues are $4,12$, with an odd higher weight binomial. Their higher index is even, so $D-t$ is odd, and the bit-$5$ overlap makes $B$ even. Odd $k$ are again eliminated by $k+1$.

For $w\ge3$, $D_{4k}^P$ is even, and $8\mid X_{4k}$ follows.

It remains to handle $w=0$ off the prescribed pairs. Then


$$
k=32t+1\quad\text{or}\quad32t+17,\qquad \binom Ct\ \text{odd}.
$$


The corresponding $\ell=m-k$ is $32(D-t)+19$ or $32(D-t)+3$, with $D-t$ odd.

Use the complete $P\bmod16$ vector from the supplied lower lift. In its moment expansion at $j\equiv4\pmod{64}$, every coefficient is even. All $\mathcal M_v$, $-1\le v\le11$, have depth at least $3$, except possibly $\mathcal M_4$, which has depth at least $2$. Its coefficient is divisible by $8$: the unshifted contribution is


$$
35\left(4\cdot12+6\cdot4+4\cdot4\right)=35\cdot88,
$$


and the reconstruction terms multiplied by $j$ have at least the same required depth. Thus $D_j^P\equiv0\pmod{16}$.

This proves (42).

### 9.3 The remaining off-pair even positions

The only remaining off-pair even coordinates are $j\equiv32\pmod{64}$. At these positions, the bounded translations in the complete difference polynomial already vanish modulo $32$. The sampled calculation used at the preceding depth therefore applies with $32\mid j$, and gives


$$
\eta_j-2\theta_j\in16\mathbb Z_2.
\tag{48}
$$


Also $j(\eta_{j-1}-2\theta_{j-1})\in32\mathbb Z_2$, and $W_j$ is even. Hence


$$
Y_j-X_j
=-\frac{W_j}{4}
 \left[(\eta_j-2\theta_j)-j(\eta_{j-1}-2\theta_{j-1})\right]
\in8\mathbb Z_2.
\tag{49}
$$


Since $4\mid X_j$, these terms also vanish in the fourth defect.

Thus


$$
\boxed{
\sum_{\substack{j\ {\rm even}\\j\notin\mathcal P}}
\frac{X_j(Y_j-X_j)}{16}=0\pmod2.
}
\tag{50}
$$



---

## 10. Odd positions: the surviving terms cancel in shifted pairs

At odd positions, the retained result is $8\mid X_j$. Therefore


$$
\frac{X_j(Y_j-X_j)}{16}
\equiv\frac{X_j}{8}\frac{Y_j}{2}\pmod2.
\tag{51}
$$


The $X_j^2$ term is already zero at this precision.

Write $j=4k+a$, $a=1,3$. Then


$$
v_2(W_j)=2+v_2\binom{M-1}{k}.
\tag{52}
$$


If $v_2(W_j)\ge4$, then $4\mid Y_j$, so (51) vanishes. Only weight depths $2,3$ remain.

### 10.1 Weight depth $2$

Here


$$
k=32t\quad\text{or}\quad32t+16,\qquad \binom Ct\ \text{odd},
$$


so $t$ is even and $d=D-t$ is odd. Put


$$
\ell=m-k=32d+20\quad\text{or}\quad32d+4,
$$




$$
T=h+\ell,\qquad B=\binom{4T}{4\ell}.
$$


In particular, $4\mid\ell$, $v_2(\ell)=2$, and $B$ is even.

At $j\equiv1\pmod{64}$, the complete $P\bmod8$ expansion gives


$$
D_j^P\equiv
2\mathcal M_{-1}+7\mathcal M_0
 +2\mathcal M_1+2\mathcal M_2+4\mathcal M_4
\pmod8.
\tag{53}
$$


Adjacent-binomial ratios reduce this to


$$
D_j^P\equiv2\frac hT B\pmod8.
\tag{54}
$$


The complete $Q\bmod4$ reconstruction is


$$
D_j^Q:=j\eta_{j-1}-\eta_j
\equiv
2\mathcal M_{-4}+2\mathcal M_{-3}
+\mathcal M_{-2}+2\mathcal M_{-1}
\equiv\frac hT B\pmod4.
\tag{55}
$$


Consequently,


$$
\frac{X_j}{8}\frac{Y_j}{2}
\equiv\frac B2\pmod2.
\tag{56}
$$


The two positions $128t+1,128t+65$ have the same valuation of $B$, because their low blocks introduce no differing carries and their common higher binomial is


$$
\binom{2C+1+d}{d}.
$$


Thus their contributions in (56) are equal and cancel.

At $j\equiv3\pmod{64}$, the complete expansion is


$$
D_j^P\equiv
5\mathcal M_{-1}+6\mathcal M_0
 +2\mathcal M_1+6\mathcal M_2+4\mathcal M_3
\pmod8.
\tag{57}
$$


The upper argument is $17\bmod64$, and the five lower arguments are $14,13,12,11,10\bmod64$. Kummer gives enough depth to make (57) zero modulo $8$. Hence $16\mid X_j$, and these terms vanish individually.

### 10.2 Weight depth $3$

The possibilities are:

1. $k=32t+8$, with $\binom Ct$ odd;
2. $k=32t$ or $32t+16$, with $v_2\binom Ct=1$.

In the first case, $d=D-t$ is odd. For $a=1$, the complete $Q$-parity is


$$
D_j^Q\equiv\binom{h+\ell-1}{\ell}\pmod2,
$$


and the bit-$5$ overlap makes it even. For $a=3$, it is already even. Thus $4\mid Y_j$.

In the second case, $a=3$ again contributes zero. For $a=1$, the modulo-$4$ reduction gives


$$
\frac{D_j^P}{2}\equiv B\pmod2,\qquad
D_j^Q\equiv B\pmod2.
$$


Hence


$$
\frac{X_j}{8}\frac{Y_j}{2}\equiv B\pmod2.
\tag{58}
$$


The two positions $128t+1,128t+65$ again have identical higher-binomial parity. Their contributions cancel.

All shifted pairs used here have $0\le t\le D$, and both members lie strictly below $b$.

### 10.3 Full endpoint

The actual endpoint remains


$$
X_b=\frac{W_b\,b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4}.
$$


The retained endpoint bound $v_2(W_b)\ge6$ gives


$$
v_2(X_b)\ge5,\qquad v_2(Y_b)\ge4.
$$


Thus the endpoint contribution is zero, with its $Q$-column $1$ retained before taking valuations.

Combining the odd classes,


$$
\boxed{
\sum_{\substack{0\le j\le b\\j\ {\rm odd}}}
\frac{X_j(Y_j-X_j)}{16}=0\pmod2.
}
\tag{59}
$$



---

## 11. The fourth contracted scalar

Equations (41), (50), and (59) give


$$
\begin{aligned}
\frac{H-N}{16}
&=
\sum_{j\in\mathcal P}\frac{X_j(Y_j-X_j)}{16}\\
&\quad+
\sum_{\substack{j\ {\rm even}\\j\notin\mathcal P}}
 \frac{X_j(Y_j-X_j)}{16}
+
\sum_{j\ {\rm odd}}\frac{X_j(Y_j-X_j)}{16}\\
&\equiv0+0+0\pmod2.
\end{aligned}
$$


Therefore


$$
\boxed{\frac{H-N}{16}\equiv0\pmod2}
\qquad
\text{for every }r=18+32u,\ u\ge0.
\tag{60}
$$



No additional subclass has been imposed. In particular, the oddness of $D$, the congruence $C\equiv2\pmod4$, and every paired range used above follow from the original domain.

This establishes


$$
\boxed{H\equiv N\pmod{32}.}
$$


It does not evaluate $N/16\bmod2$, and it does not establish a stable all-depth induction.

---

## 12. Final gcd, actual denominator, and whole real error

The complete actual center is unchanged:


$$
c_n=\frac{2b!}{\lambda R}\frac{H}{N}.
$$



Let $d_B$ be the least common denominator of the actual two-column lift, and put


$$
N_B=d_B[u,v].
$$


For the stated falling-factorial metric, retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
\tag{61}
$$


Thus $1/g_B$ is the final primitive normalization of the integer pair, and $q_n$ is the actual reduced denominator and primitive multiplier of $S$.

With $s=s_2(n)$,


$$
v_2(g_B)=
\min\left\{
3n-2s+2+\alpha,\,
\frac{3n}{2}-s+v_2(b!)+3+\gamma
\right\},
\tag{62}
$$




$$
\boxed{
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s-1-(\gamma-\alpha)
\right\}.
}
\tag{63}
$$


The new congruence does not bound $\gamma-\alpha$ at unrestricted depth.

For the retained whole signed-error theorem,


$$
\epsilon_n=c_n-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The whole primitive evaluated form is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
}
\quad\text{eventually}.
\tag{64}
$$


Its nonvanishing and error concern the complete exponential residual, logarithmic force, endpoint, actual columns, and actual metric.

---

# Concluding ledger

## (1) New result and proof status

**Proved, using the retained exact lower-layer identities, on every original index**


$$
b=9^r,\quad n=4002b,\quad r=18+32u,\quad u\ge0:
$$



* The contact congruence modulo $64$ is valid in the integral divided-power ring.
* The complete normalized $P$-forcing is (12), including its degree-$6,7$ terms.
* The seven actual factorial residues and boundary values modulo $64$ are (6), (9).
* The whole-force cutoff is justified.
* The complete degree-three boundary forcing is (14), including the new $16T(-4)$ correction.
* The complete lift has proved degree bounds $21,19$, with weighted substitution losses retained.
* The paired contribution is evaluated through the new sampled periodicity (29) and the unrestricted convolution.
* Off-pair even and odd contributions, including the full endpoint, are evaluated separately.
* The fourth contracted carry is
  

$$
\boxed{(H-N)/16=0\pmod2.}
$$



The proof does not require a finite growing-index computation or the value of the fixed odd constant $\kappa$.

## (2) Exact remaining bottleneck

The actual next norm digit


$$
N/16\bmod2
$$


has not been evaluated here. Accordingly, the present result permits either


$$
\alpha=\gamma=4
\quad\text{or}\quad
\alpha,\gamma\ge5.
$$



The next discrepancy beyond the proved result is


$$
\frac{H-N}{32}\pmod2.
$$


More substantively, there is still no stable induction proving an all-depth estimate such as


$$
\boxed{\gamma-\alpha\le2000b+o(n).}
$$


A finite sequence of aligned carries cannot replace that estimate or a sufficient global bound on the actual primitive denominator.

## (3) Computation request

**No computation is necessary for the proof above.**

An optional bounded independent audit can use only


$$
n_{\rm ref}=2,\qquad b_{\rm ref}=81,
$$


the operator (15), and the Newton vectors


$$
g_{32}=(2,-9,19,-25,12,-4,16,-16),
\qquad
a_{32}=(10,2,24,15).
$$



Expected verifiable outputs would be:

1. $P^\#\bmod32$, through degree $21$;
2. $Q^\#\bmod64$, through degree $19$;
3. their reductions to the supplied earlier coefficient vectors;
4. the value of $K(16)/16\bmod4$, necessarily odd;
5. symbolic verification of
   

$$
K(4s)\in4\mathbb Z_2,\qquad
   K(16s+64)-K(16s)\in64\mathbb Z_2.
$$



Such an audit concerns fixed polynomial identities only. It is not a substitute for the infinite convolution and original-domain arguments above.
