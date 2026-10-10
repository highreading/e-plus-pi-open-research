> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 — a complete fifth-precision $Q$-lift and a next-norm classification; the fifth discrepancy remains unresolved

I do **not** obtain a proved value of


$$
\Delta _5=\frac{H-N}{32}\pmod2
$$


on its true common-zero locus. In particular, I do not infer its value from the fourth-level pair pattern.

There are, however, two new exact results:

1. The seven factorial residues, seven boundary values, and the **complete second-column lift modulo $128$** can be derived. The $64U$ contact correction contributes essentially.
2. The existing first-column lift gives an explicit classification of
   

$$
\frac N{32}\pmod2
$$


   on the entire true common-zero locus. In particular,
   

$$
\boxed{r=50+128w,\quad w\ge0\quad\Longrightarrow\quad N\equiv0\pmod{64}.}
$$


   This conclusion concerns $N$, not $H$: on that subclass the present result is $\alpha\ge6,\ \gamma\ge5$.

The unresolved part is identified precisely below. No newly computed finite evidence is used.

---

## 1. Domain and actual quantities

Throughout,


$$
b=9^r,\qquad n=4002b,\qquad r=18+32u,\quad u\ge0,
$$


and


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532.
$$


Thus


$$
D\text{ is odd},\qquad C\equiv2\pmod4.
$$



Keep


$$
a=\frac{C-2}{4},\qquad v=\left\lfloor\frac D4\right\rfloor.
$$


The assigned true common-zero locus is


$$
\boxed{\mathcal Z=\{r=18+32u:\ v\mathbin{\&}(a+1)\ne0\}.}
$$


The already evaluated fourth norm digit and audited fourth discrepancy give


$$
N,H\in32\mathbb Z_2\qquad(r\in\mathcal Z).
$$



The actual columns and metric remain


$$
h=\frac n2,\qquad R=2^h\binom{2h}{h},
\qquad \lambda=\frac{(n!)^2}{2^n},
$$




$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},
$$




$$
W_j=\binom{n+2}{j},\qquad
\omega_j=j!W_j=(n+2)_{\underline j},
\qquad
\Omega=\operatorname{diag}(\omega_j^2)_{0\le j\le b}.
$$


Set


$$
N=X^TX>0,\qquad H=X^TY,\qquad
\alpha=v_2(N),\quad\gamma=v_2(H).
$$


The retained original-family mixed nonvanishing is not inferred from any residue calculation here.

Every actual inverse below has indices $0\le i,j<b$. Every reconstruction retains the endpoint $+1$.

---

# Part I. The complete second-column lift modulo $128$

## 2. Seven residues and seven exterior boundary values

Put


$$
f_s=\frac{(b+s)!}{b!}.
$$


Since $b\equiv81\pmod{128}$, direct multiplication gives


$$
\boxed{
(f_0,\ldots,f_6)
\equiv(1,82,22,56,24,16,112)\pmod{128}.
}
\tag{1}
$$


Their exact depths are


$$
(0,1,1,3,3,4,4).
$$


Moreover, $b+7\equiv88\pmod{128}$, so


$$
v_2(f_7)=7.
$$


Consequently every tail beginning at $b+7$ vanishes modulo $128$ **before** application of the integral contact and inverse operators.

Define, as in the original finite-boundary construction,


$$
B_s=\sum_{t=s}^{6}f_t\binom{2n}{t-s}.
$$


The bounded binomial information needed is


$$
\binom{2n}{1}\equiv4\pmod{64},\qquad
\binom{2n}{2}\equiv6\pmod{64},
$$




$$
\binom{2n}{3}\equiv4\pmod{16},\qquad
\binom{2n}{4}\equiv1\pmod{16},
$$




$$
\binom{2n}{5},\binom{2n}{6}\equiv0\pmod8.
$$


These hold uniformly because $2n=132+256C$, with $C\equiv2\pmod4$. Combining them with (1) yields


$$
\boxed{
(B_0,\ldots,B_6)
\equiv(69,106,54,56,120,80,112)\pmod{128}.
}
\tag{2}
$$



For example,


$$
B_0\equiv1+82\cdot4+22\cdot6+56\cdot4+24
\equiv69\pmod{128}.
$$



**Parameter dependence at this precision:** all fourteen residues in (1)–(2) are constant on the entire original exponent domain. No unspecified higher digit remains in them.

The complete logarithmic force still vanishes at this precision. Indeed, its supplied whole-force bound is at least


$$
2000b+2-2\lfloor\log_2(8005b-1)\rfloor>7
$$


for $b\ge81$. This disposes of the whole force, not a selected summand.

---

## 3. The corrected boundary polynomial modulo $64$

Let $E(n)$ denote the contact operator associated with $U$:


$$
E(n)_{ik}
=
\sum_{s=1}^{4}c_s\sum_{t=0}^{s}
\binom i{s-t}\binom nt
\binom{-t}{k+s-i-t},
\qquad(c_1,c_2,c_3,c_4)=(-1,2,-3,3).
\tag{3}
$$


Write $E_0=E(2)$.

Since $n=2+64e$, where


$$
e=2C+1\equiv1\pmod4,
$$


one has


$$
\binom n1\equiv2,\quad
\binom n2\equiv33,\quad
\binom n3\equiv0,\quad
\binom n4\equiv16\pmod{64}.
$$


Therefore


$$
\boxed{
E(n)\equiv E_0+32J_2+48T(-4)\pmod{64},
}
\tag{4}
$$


where


$$
(J_2)_{ik}
=\sum_{s=2}^{4}c_s\binom i{s-2}
\binom{-2}{k+s-i-2}.
$$



Let $a_{64}$ be the signed exterior-boundary polynomial:


$$
a_{64}(i)\equiv(-1)^i
\sum_{s=0}^{6}E(n)_{i,b+s}B_s\pmod{64}.
$$



### 3.1 Reference part

Modulo $64$,


$$
\sum_{s=0}^{6}(-1)^sB_s=49,\qquad
\sum_{s=0}^{6}s(-1)^sB_s=10.
$$


Using the reference exterior formula from the supplied lift gives


$$
a_{\mathrm{ref}}(X)
\equiv
42+50X+24\binom X2+31\binom X3\pmod{64}.
\tag{5}
$$



### 3.2 The $32J_2$ correction

Only parity is needed. In the exterior sum, only $B_0$ is odd. The signed $J_2$-boundary contribution is


$$
X(1-X)+X\binom X2
\equiv\binom X3\pmod2.
$$


Hence this correction is


$$
32\binom X3.
$$



### 3.3 The $48T(-4)$ correction

Modulo $4$, its unsigned boundary polynomial is


$$
\begin{aligned}
F(X)
&=\sum_{s=0}^{6}(-1)^sB_s
  \binom{b+s+3-X}{3}\\
&\equiv
\binom{4-X}{3}
+2\binom{5-X}{2}\\
&\equiv X-\binom X3\pmod4.
\end{aligned}
$$


The signed correction is thus


$$
-48F(X)\equiv16X-16\binom X3\pmod{64}.
$$



Combining all three parts,


$$
\boxed{
a_{64}(X)=42+2X+24\binom X2+47\binom X3
\pmod{64}.
}
\tag{6}
$$


It reduces to the previously supplied


$$
a_{32}(X)=10+2X+24\binom X2+15\binom X3
\pmod{32}.
$$



---

## 4. Retaining the $64U$ contact correction

The established next contact congruence is


$$
\phi^{2h}\equiv1+66U\pmod{128}.
$$


Accordingly, the second-column polynomial is


$$
Q_5
=
66\sum_{\ell=0}^{5}(-66\mathscr E)^\ell a_{64}
\pmod{128},
\tag{7}
$$


where $\mathscr E$ is the signed finite operator for the actual parameters.

The coefficient $66$ cannot be replaced by $2$ in the zeroth inverse term. For powers $p\ge2$, however,


$$
66^p\equiv2^p\pmod{128}.
$$


Thus the direct contact change contributes $64a_{64}$.

There is also one surviving $n$-parameter correction in the inverse. From (4),


$$
E(n)-E_0\equiv16T(-4)\pmod{32}.
$$


Only the first inverse term can retain this correction modulo $128$; it contributes


$$
-64\mathscr T a_{64},
$$


where $\mathscr T$ is the signed $T(-4)$-operator.

Modulo $2$, $a_{64}=\binom X3$. On the original finite boundary $b\equiv1\pmod8$,


$$
\boxed{\mathscr T\binom X3\equiv\binom X7\pmod2.}
\tag{8}
$$


To see this directly, its value at $i$ is


$$
\sum_{k=i}^{b-1}\binom{k-i+3}{3}\binom k3\pmod2.
$$


The first factor is odd precisely when $k-i\equiv0\pmod4$. The second then forces $i\equiv3\pmod4$. Writing $i=4s+3$, the remaining number of terms has parity $s$, because $(b-1)/4$ is even. This is exactly $\binom i7\bmod2$. The polynomial degree is at most seven, so the identity also holds in the integral Newton-polynomial interpretation.

Since


$$
a_{64}-a_{32}=32\left(1+\binom X3\right),
$$


the two $\binom X3$-corrections cancel. The complete result is the particularly convenient formula


$$
\boxed{
Q_5(X)=
2\sum_{\ell=0}^{5}(-2\mathscr E_0)^\ell a_{32}(X)
+64\left(1+\binom X7\right)
\pmod{128},
}
\tag{9}
$$


with the reference signed operator at $n=2,b=81$.

The extra $64(1+\binom X7)$ is not optional. It incorporates both the new contact coefficient and the boundary/contact-parameter corrections.

### Weighted transfer and degree

The reference substitution in (9) applies only to the bounded polynomial operations. The largest boundary-dependent lower indices for $\ell=1,\ldots,5$ are


$$
7,\ 11,\ 15,\ 19,\ 23.
$$


Since $v_2(b-81)=7$, the corresponding available depths are


$$
5,\ 4,\ 4,\ 3,\ 3.
$$


After multiplication by the inverse-term factors $2^{\ell+1}$, all differences vanish modulo $128$. The $n$-correction that does not vanish has already been retained explicitly above.

Moreover,


$$
\boxed{\deg Q_5\le23.}
$$



Equation (9) is a complete coefficient formula: if $q_r=[\binom Xr]Q_5$, then


$$
q_r\equiv
2\sum_{\ell=0}^{5}(-2)^\ell
\sum_{i=0}^{r}(-1)^{r-i}\binom ri
(\mathscr E_0^\ell a_{32})(i)
+64(\mathbf1_{r=0}+\mathbf1_{r=7})
\pmod{128},
\tag{10}
$$


for $0\le r\le23$, with $q_r=0$ for $r>23$.

---

## 5. Full raw $4Y\bmod128$, with the actual endpoint

Using (2) and (9), the actual finite solution is


$$
\boxed{
\eta_i\equiv
-\sum_{s=0}^{6}B_s\binom{-2n}{b+s-i}
+\bigl(T(-2n)\mathcal S_bQ_5\bigr)_i
\pmod{128},
\qquad0\le i<b.
}
\tag{11}
$$


Here $T(-2n)$, $n,b$, and the inverse range are the original ones—not their reference values.

Extend $\eta$ by zero at $-1,b$. Then


$$
\boxed{
4Y_j\equiv
W_b\mathbf1_{j=b}
+W_j(j\eta_{j-1}-\eta_j)
\pmod{128},
\qquad0\le j\le b.
}
\tag{12}
$$


This supplies the requested second raw column at fifth precision.

I have **not** completed the independent normalized $P$-forcing modulo $64$, so I do not claim a corresponding full formula for $2X\bmod64$.

---

# Part II. The next norm digit from the existing first-column lift

The following calculation needs only the supplied actual $P\bmod32$, not the unresolved $P\bmod64$.

## 6. A sharper first-column formula at every surviving coordinate

The established support refinement gives


$$
8\mid X_j\qquad(32\nmid j).
$$


Thus only $32$-divisible coordinates can contribute to $N\bmod64$. The endpoint is already covered by its stronger valuation.

Put


$$
e=2C+1,\qquad
L=b-1-j=16q
$$


for $32\mid j<b$. Every such $q$ is positive and odd.

The supplied Newton vector is


$$
P_{32}=
2+31X+7\binom X2+5\binom X3
+16\binom X4+12\binom X5+4\binom X6+4\binom X7
+8\binom X9+24\binom X{10}+8\binom X{11}.
$$



For $j=32\zeta$, bounded translation gives


$$
P_{32}(j+x)\equiv P_{32}(x)+16\zeta(1+x)\pmod{32}.
\tag{13}
$$


The resulting correction to $X_j\bmod16$ vanishes:

* if $\zeta$ is even, it has the required factor directly;
* if $\zeta$ is odd, $W_j$ is even.

Thus it is legitimate to use the unshifted bounded polynomial **after** this weight check.

The bounded moment products $p_s\binom{s+3}{3}$ give


$$
\begin{aligned}
J_{32}(L)={}&
2\binom{L+4}{4}
+28\binom{L+4}{5}
+6\binom{L+4}{6}
+4\binom{L+4}{7}\\
&+16\binom{L+4}{8}
+16\binom{L+4}{10}
+16\binom{L+4}{14}
\pmod{32}.
\end{aligned}
\tag{14}
$$



### A new sampled identity

For every $s\ge0$,


$$
\boxed{J_{32}(8s)\equiv2+20s\pmod{32}.}
\tag{15}
$$



Here is a direct derivation. Write $B=\binom{8s+4}{4}$. Then


$$
B\equiv8s^2+6s+1\pmod{16},
$$




$$
\binom{8s+4}{6}\equiv4sB\pmod{16}.
$$


The terms with lower indices $5,7$ vanish after their displayed coefficients. Lucas eliminates the $10,14$ terms, while


$$
16\binom{8s+4}{8}\equiv16s\pmod{32}.
$$


Consequently


$$
J_{32}(8s)
\equiv2B+24sB+16s
\equiv2+20s\pmod{32}.
$$



Now use


$$
(1-z)^{-128e}\equiv(1-z^8)^{-16e}\pmod{32}.
$$


The actual convolution at $L=16q$ is therefore


$$
\theta_j\equiv
2\binom{16e+2q}{2q}
+20\binom{16e+2q}{2q-1}
\pmod{32},
$$


apart from the already disposed-of translation correction. The adjacent-binomial ratio gives


$$
\frac12\theta_j
\equiv
(1+4q)\binom{16e+2q}{2q}\pmod{16}.
$$


Also,


$$
\binom{16e+2q}{2q}
\equiv\binom{8e+q}{q}\pmod{16}.
$$


Indeed, after separating even factors, the remaining odd-factor ratio is a product of terms $1+16e/(2i-1)$.

The reconstruction term multiplied by $j$ vanishes modulo $16$. Hence


$$
\boxed{
X_j\equiv
-(1+4q)W_j\binom{8e+q}{q}\pmod{16},
\qquad
q=\frac{b-1-j}{16},\quad32\mid j<b.
}
\tag{16}
$$



This is stronger than the previous modulo-$8$ formula and retains the actual large binomial.

---

## 7. Complete norm accounting modulo $64$

Define


$$
E_t=\binom Ct\binom{e+D-t}{D-t},
\qquad0\le t\le D,
$$


and the actual finite counts


$$
C_1=\#\{t:v_2(E_t)=1\},\qquad
C_2=\#\{t:v_2(E_t)=2\}.
\tag{17}
$$


Every $E_t$ is even.

The ranges are:

* $j=128t,128t+32,128t+64$: $0\le t\le D$;
* $j=128t+96$: $0\le t\le D-1$.

The last class still has $8\mid X_j$, so its squares vanish modulo $64$.

### 7.1 Prescribed pairs: the new unit comparison

For $d=D-t$, the two $q$-values in (16) are $8d+5$ and $8d+1$. Both coordinates have the truncated valuation of $E_t$.

For depth-one pairs, units now matter. Their weight ratio satisfies


$$
\frac{W_{128t+64}}{W_{128t}}
\equiv
\begin{cases}
5,&t\text{ even},\\
1,&t\text{ odd}
\end{cases}
\pmod8
\tag{18}
$$


as a $2$-adic unit ratio. One way to verify this is to use the odd factorial product


$$
U(m)=\prod_{\substack{1\le k\le m\\k\text{ odd}}}k\pmod8,
\qquad U(m+8)=U(m).
$$


In the factorial-unit quotient, levels $0,\ldots,5$ cancel; level $6$ leaves


$$
\frac{2(C-t)+1}{2t+1}\pmod8,
$$


which is (18).

For


$$
T_q=\binom{8e+q}{q},
$$


an adjacent-factor calculation gives


$$
\frac{T_{8d+1}}{T_{8d+5}}
\equiv
\begin{cases}
7,&d\text{ even},\\
3,&d\text{ odd}
\end{cases}
\pmod8.
\tag{19}
$$


Since $D$ is odd, $d$ and $t$ have opposite parity. Multiplying (18)–(19), the pair ratio is always $-1\bmod8$. The factors $1+4q$ in (16) agree modulo $16$.

Therefore:

* a depth-one pair contributes $8\bmod64$;
* a depth-two pair contributes $32\bmod64$;
* deeper pairs contribute zero.

Thus


$$
\sum_{t=0}^{D}
\left(X_{128t}^2+X_{128t+64}^2\right)
\equiv8C_1+32C_2\pmod{64}.
\tag{20}
$$



### 7.2 The $128t+32$ residuals

These coordinates have depth two precisely when $v_2(E_t)=1$. Their square is then $16\bmod64$. Consequently,


$$
\sum_{t=0}^{D}X_{128t+32}^2
\equiv16C_1\pmod{64}.
\tag{21}
$$



All other coordinates have already been accounted for by actual divisibility, including every odd coordinate and the endpoint. Combining (20)–(21),


$$
\boxed{N\equiv24C_1+32C_2\pmod{64}.}
\tag{22}
$$



---

## 8. Evaluate the depth-two count parity

Write


$$
C=2c,\quad c=2a+1,\qquad
D=2d+1,\quad d=2v+\varepsilon,\quad\varepsilon\in\{0,1\}.
$$


Let


$$
T=
\#\left\{
0\le i\le v:
\binom ai\text{ odd},\
\binom{2a+1+v-i}{v-i}\text{ odd}
\right\}.
\tag{23}
$$


The previously proved exact count identity is $C_1=2T$.

The new depth-two parity is


$$
\boxed{
C_2\equiv
a\binom{a+v+\varepsilon+1}{v+\varepsilon-1}
\pmod2,
}
\tag{24}
$$


with a negative lower index interpreted as zero.

### Derivation

The exact valuation reductions for even and odd $t$ are


$$
v_2(E_{2s})
=
1+v_2\left[
\binom cs\binom{2c+d-s+1}{d-s}
\right],
$$




$$
v_2(E_{2s+1})
=
1+v_2\left[
(c-s)\binom cs\binom{2c+d-s}{d-s}
\right].
$$



For the first bracket, $d-s$ odd produces at least two internal carries, so it cannot have valuation one. If $s=2i+\varepsilon$, its valuation is that of


$$
F_i=\binom ai\binom{2a+1+v-i}{v-i}.
$$


In the second bracket, the even $s=2i$ terms have exactly the same valuation pattern. These two depth-one counts cancel modulo $2$.

Only odd $s=2i+1$ remain in the second bracket. Put


$$
w=v+\varepsilon-1.
$$


Their bracket has valuation one exactly when


$$
a\binom{a-1}{i}
\binom{2a+1+w-i}{w-i}
$$


is odd. Summing its parity gives


$$
\begin{aligned}
C_2
&\equiv
a[z^w](1+z)^{a-1}(1-z)^{-2a-2}\\
&\equiv
a[z^w](1+z)^{-a-3}\\
&=
a\binom{a+w+2}{w}\pmod2,
\end{aligned}
$$


which is (24).

On the actual original parameter relation,


$$
a=
\begin{cases}
4002v+1633,&D=4v+1,\\
4002v+3634,&D=4v+3.
\end{cases}
$$


Therefore (24) simplifies to


$$
\chi:=
C_2\bmod2=
\begin{cases}
\displaystyle\binom{a+v+1}{v-1}\bmod2,&D\equiv1\pmod4,\\[2mm]
0,&D\equiv3\pmod4.
\end{cases}
\tag{25}
$$



Equations (22)–(25) give the new full-parent-domain formula


$$
\boxed{N\equiv48T+32\chi\pmod{64}.}
\tag{26}
$$



---

## 9. An explicit next-norm carry classification on the true zero locus

The parity of $T$ is the previously evaluated fourth norm bit. Hence $T$ is even on $\mathcal Z$, and (26) yields


$$
\boxed{
\frac N{32}\equiv\frac T2+\chi\pmod2
\qquad(r\in\mathcal Z).
}
\tag{27}
$$



The quantity $T\bmod4$ admits a bounded-state, exact binary evaluation; it need not be left as a growing-index binomial sum.

Write $a_k,v_k$ for the binary digits of the **actual** integers $a,v$, and set


$$
h_0=a_0,\qquad h_k=1+a_k-a_{k-1}\quad(k\ge1).
$$


Thus $h_k\in\{0,1,2\}$. For $h\in\{0,1,2\}$ and $d\in\{0,1\}$, define the two-state matrix


$$
\mathcal M_{h,d}(c,c')
=
\binom h{d+2c'-c},
\qquad c,c'\in\{0,1\}.
\tag{28}
$$


Out-of-range binomials are zero.

For any $L$ with $2^L>v$,


$$
\boxed{
T\equiv
(1,0)\left(\prod_{k=0}^{L-1}\mathcal M_{h_k,v_k}\right)
\binom10
\pmod4.
}
\tag{29}
$$



This is an exact carry-count identity. Indeed, (23) counts decompositions $i+q=v$ with


$$
i\mathbin{\&}\neg a=0,\qquad q\mathbin{\&}(2a+1)=0.
$$


At bit $k$, the number of freely selectable bits among $i_k,q_k$ is exactly $h_k$. The transition (28) imposes the ordinary addition carry. The final zero-carry state ensures the actual finite upper boundary. No high digits are chosen independently.

Thus (25), (27), and (29) give an explicit next-norm classification for every original index in $\mathcal Z$:


$$
\frac T2+\chi=1\Longrightarrow\alpha=5,
\qquad
\frac T2+\chi=0\Longrightarrow\alpha\ge6.
$$


I make no population claim for the first branch.

### The entire original subclass $r=50+128w$

On this subclass the established exponent congruence gives $D\equiv7\pmod8$. Hence $a$ is even and $v$ is odd.

In (23), an admissible $i$ is even because $a$ is even. An admissible $q=v-i$ is even because $2a+1$ is odd. Their sum cannot be the odd integer $v$. Therefore


$$
T=0
$$


as an ordinary integer count, not just modulo $4$. Also $D\equiv3\pmod4$ gives $\chi=0$. Consequently,


$$
\boxed{
r=50+128w,\ w\ge0
\quad\Longrightarrow\quad
N\equiv0\pmod{64}.
}
\tag{30}
$$


No original exponent in this subclass is omitted.

---

# Part III. What is still missing for the fifth discrepancy

## 10. The unresolved first-column forcing and contracted mixed bit

The contact congruence and the $Q$-lift above do **not** determine the normalized $P$-forcing modulo $64$.

The supplied $g_{32}$ fixes only


$$
g_{64}=g_{32}+32F\pmod{64}
$$


for an as-yet unevaluated integral Newton polynomial $F$. The new central-forcing terms cannot be obtained by replacing $2U$ by $66U$: these are separate operations.

Nor can the old $n=2,b=81$ substitution be copied without rechecking it. For example, in the first $P$-inverse term, a boundary-dependent lower index $9$ can lose three of the seven available bits of $b-81$. That leaves depth four, whereas modulo $64$ this unweighted term requires depth five. One must retain the corresponding correction or use and justify a more accurate bounded reference.

This is the precise missing part of the requested raw


$$
2X\bmod64.
$$



More importantly, I have not evaluated


$$
\sum_{j=0}^{b}X_j(Y_j-X_j)\pmod{64}
$$


with all new even and odd classes. The norm calculation above does **not** dispose of those mixed terms. For example, an off-pair coordinate with $v_2(X_j)=3$ and $v_2(Y_j)=2$ has zero square modulo $64$ but can contribute $32\bmod64$ to $X_jY_j$.

Accordingly, the new statements do not imply either


$$
\Delta _5=0
\quad\text{or}\quad
\Delta _5=1
$$


anywhere on $\mathcal Z$, including the subclass (30).

---

## 11. Primitive arithmetic and whole signed error

No primitive normalization or metric is changed.

Let $d_B$ be the least common denominator of the actual two-column lift and


$$
N_B=d_B[u,v].
$$


Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
$$


The primitive multiplier relative to the uncleared quadratic pair is


$$
\frac{d_B^2}{g_B}.
$$


The actual reduced denominator is $q_n$, not $d_B$ or a contact determinant.

The complete center remains


$$
c_n=\frac{2b!}{\lambda R}\frac HN=\frac{p_n}{q_n}.
$$


With $s=s_2(n)$, retain the exact binary interface


$$
v_2(g_B)=
\min\left\{
3n-2s+2+\alpha,\,
\frac{3n}{2}-s+v_2(b!)+3+\gamma
\right\},
$$




$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s-1-(\gamma-\alpha)
\right\}.
$$


In particular, the new $\alpha\ge6,\gamma\ge5$ on (30) does not control $\gamma-\alpha$.

Under the retained complete signed-error theorem,


$$
\epsilon_n=c_n-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The whole primitive evaluated form is still


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n>0}
$$


eventually. Its nonvanishing concerns the whole exponential residual, logarithmic force, finite boundary and endpoint—not a selected error component.

No irrationality or rationality conclusion follows.

---

# Concluding ledger

## (1) New result and proof status

**Proved on the original infinite exponent domain:**

* All seven factorial residues and boundary values modulo $128$, equations (1)–(2).
* The corrected exterior polynomial
  

$$
a_{64}=42+2X+24\binom X2+47\binom X3\pmod{64}.
$$


* The complete degree-$23$ second-column polynomial
  

$$
Q_5=
  2\sum_{\ell=0}^{5}(-2\mathscr E_0)^\ell a_{32}
  +64\left(1+\binom X7\right)\pmod{128},
$$


  with the $64U$ contact correction retained.
* The complete raw $4Y\bmod128$, including its actual finite inverse and endpoint.
* The stronger first-column formula (16), obtained from the existing raw $2X\bmod32$.
* The next-norm classification
  

$$
N\equiv48T+32\chi\pmod{64},
$$


  with $T\bmod4$ given by the exact two-state carry product (29).
* On every original exponent $r=50+128w$,
  

$$
\boxed{N\equiv0\pmod{64}.}
$$



**Not proved:** the fifth contracted discrepancy, the complete normalized $P$-forcing modulo $64$, or an unrestricted-depth bound on $\gamma-\alpha$.

## (2) Exact remaining bottleneck

The immediate missing inputs are:

1. the independent normalized $P$-forcing modulo $64$, with its contact and boundary-parameter losses;
2. the complete mixed contraction modulo $64$, including new off-pair even and odd contributions.

The substantive arithmetic bottleneck remains the actual reduced denominator after the final gcd, on the same indices as the nonzero whole-error estimate. No finite collection of aligned digits resolves it.

## (3) Bounded computation request

A useful exact audit is now fully specified and does **not** require a growing matrix.

**Inputs**

* The signed reference operator $\mathscr E_0$ at $n=2,b=81$, explicitly given in A5turn17, equation (15).
* The Newton polynomial
  

$$
a_{32}=(10,2,24,15).
$$


* The polynomial formula
  

$$
Q_5=
  2\sum_{\ell=0}^{5}(-2\mathscr E_0)^\ell a_{32}
  +64(1+\binom X7)\pmod{128}.
$$



**Expected verifiable output**

1. The complete Newton coefficient vector of $Q_5\bmod128$, through degree $23$.
2. Its reduction modulo $64$, compared entrywise with the supplied fourth-lift $Q$-vector.
3. Exact Newton certificates for the boundary calculation (6) and
   

$$
\mathscr T\binom X3-\binom X7\equiv0\pmod2.
$$



This would audit fixed polynomial identities only. It would not, by itself, evaluate the fifth discrepancy on the infinite true common-zero locus.
