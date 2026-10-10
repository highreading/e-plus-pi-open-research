> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 10 — A paid one-carry connection at an original parameter, and the next complete-column precision budget

## Executive assessment

The new computations establish the stated original zero layer. After inspecting both implementations, I find no defect in the implication


$$
\text{both prefix products are zero}
\quad\Longrightarrow\quad
D=S_0=S_2=\kappa=0\pmod{29}
$$


for every continuation, including the actual finite endpoint.

I retain, without requesting repetition:

- the $400$ low ordered-pair contributions;
- the $90$ complete auxiliary comparisons;
- the $302$ finite high-moment comparisons;
- the $138$ killing-word interfaces;
- the original progression
  

$$
u\equiv381475\pmod{707281};
$$


- the original prefix annihilations at $u=0,1,2,381475$, after $5,13,1,3$ processed high digits.

The principal new result is a **paid higher-layer connection at the original parameter $u=2$**. It includes the previously discarded valuation-one atoms, rather than lifting only the vanished unit-support sum.

Write


$$
T_h(C)=\sum_{q=0}^{C}q^h
 \binom{X}{q}^{2}
 \binom{2X+C-q}{C-q}^{2},
\qquad X=2001C+1382,\qquad h=0,1,2,
$$


as exact integer sums, and write


$$
\mathcal D(C)=
\frac{(X+C+1)\bigl((3X+C+1)T_0(C)-2T_1(C)\bigr)}{29}.
$$


Thus the old $D$ is $\mathcal D\bmod29$.

For every


$$
\boxed{C=20916+29^3t,\qquad t\ge0,}
$$


I prove


$$
\boxed{
(T_0,T_1,T_2)
\equiv
29^2(23,8,18)\,\mathcal H(t)
\pmod{29^3},
}
\tag{E.1}
$$


where the remaining ordinary finite tail is


$$
\mathcal H(t)=
\sum_{r=0}^{t}
\binom{1716+2001t}{r}^{2}
\binom{3432+4002t+t-r}{t-r}^{2}
\pmod{29}.
\tag{E.2}
$$



In particular, the whole divided difference is evaluated one layer further:


$$
\boxed{\mathcal D(C)=0\pmod{29^2}.}
\tag{E.3}
$$


No value of the unread tail $\mathcal H(t)$ is needed for (E.3).

The accepted original modular data give


$$
C(u)\equiv7752+6582u\pmod{29^3}.
$$


Consequently the new theorem applies not merely to one auxiliary input, but to


$$
\boxed{
u\equiv2\pmod{24389},\qquad u\ge0.
}
\tag{E.4}
$$


In particular, it gives an actual original higher-layer certificate at $u=2$.

This is **not** an evaluation of the next physical norm digit. The identity


$$
\eta=A_0^2\kappa
$$


has been established at its stated mod-$29$ scope; it cannot be lifted merely by lifting its displayed high observables.

For that physical next layer, I give the complete quadratic connection, including the returning terminal contribution, and the exact precision budgets


$$
\boxed{
K_Z^{\rm norm}\ge d-c-1=c+3+\nu,
}
\tag{E.5}
$$


and, using only the retained contents of the two columns,


$$
\boxed{
K_Z^{\rm mixed}\ge d-1,\qquad
K_Y^{\rm mixed}\ge d-c,\qquad
N_{\log}\ge d-c=c+4+\nu.
}
\tag{E.6}
$$



No assertion $c=1$ is made at any of the four zero cases.

---

# 1. Preserved objects and scope

Throughout,


$$
p=29,\qquad
\Lambda=29^6,\qquad
\beta=410910916,
$$




$$
b=3^{249005515+574312172u}
=\beta+\Lambda C,\qquad n=2001b,\qquad u\ge0.
$$



The domains remain exactly:

- contact coordinates: $0\le j<b$;
- source rows: $1\le i\le b-2$;
- reconstructed coordinates: $0\le j\le b$.

The two corrected columns remain


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,
\qquad W_j=\binom{n+2}{j}.
$$



I reuse the accepted complete norm-only reduction


$$
\eta=\frac{Z_w^TZ_w}{p^7}\pmod p
=A_0^2\kappa\pmod p,
$$


including A4’s explicit payment of the exceptional factorial division in the first-lower argument.

The corrected retained row is still


$$
\kappa
=
21D+16S_2+
(25+18C+19C^2+24C^3)S_0
\pmod p.
\tag{1.1}
$$



The new higher-layer theorem below concerns the exact finite high sums underlying this row. It does not replace either corrected physical column by a leading atom.

---

# 2. Audit of the two prefix products

## 2.1 The bounded residue supplies the correct digits

The original-prefix source computes


$$
b\bmod p^{135}
$$


and therefore obtains


$$
C\bmod p^{129}.
$$



For the first $128$ digits of


$$
a=69C+47,\qquad B=2a+1,\qquad m=\lfloor C/p\rfloor,
$$


this is sufficient:

- multiplication by $69$, addition of $47$, and doubling determine a low prefix from the corresponding low prefix of $C$;
- the division defining $m$ needs one additional $C$-digit.

Thus the matrices used before stopping are the matrices of the actual original integers. Replacing the unread part of $C$ by any continuation leaves those processed matrices unchanged.

The source computes a bounded residue containing more digits than are ultimately processed. It does not construct or traverse the original-length integer.

## 2.2 The weighting is applied at precisely the correct digit

The ordinary product is


$$
P_L=\mathsf K_0\mathsf K_1\cdots\mathsf K_{L-1}.
$$


The weighted product is


$$
P_L^{[1]}=
\mathsf K_0^{[1]}\mathsf K_1\cdots\mathsf K_{L-1}.
$$



The implementation’s `weighted and first`, and equivalently its `i == 0`, apply the factor $d$ only at digit zero. This is correct because


$$
r\equiv r_0\pmod p.
$$



Checking only $P_L=0$ would not generally suffice: changing the first matrix can change the surviving row space. The source correctly checks both products.

There are two useful structural checks.

### Original $u=2$

The original data give the initial high triple


$$
(a_0,B_0,m_0)=(8,17,25).
$$


A unit transition would require


$$
d\le8,\qquad k\le11,\qquad d+k+e=25+29f.
$$


But the left side is at most $20$. Hence the first matrix, including its first-digit-weighted version, is zero **because its admissible sets are empty**, not because of cancellation.

### Original $u=0$

The first high triple is


$$
(a_0,B_0,m_0)=(1,3,6).
$$


Directly,


$$
\mathsf K_0=
\begin{pmatrix}13&0\\11&0\end{pmatrix},
\qquad
\mathsf K_0^{[1]}=
\begin{pmatrix}4&0\\7&0\end{pmatrix}.
\tag{2.1}
$$


Both products therefore propagate the same subsequent row $e_0^T$, with different nonzero initial column factors. At this input, vanishing of the ordinary product forces vanishing of the weighted product as well.

For $u=381475$, the previously proved word supplies an actual zero digit matrix. For $u=1$, the independent weighted-product test remains necessary and is present.

The abbreviated receipt does not include the full stage arrays for the five- and thirteen-digit cases. I therefore retain those stopping lengths as inspected-source finite execution evidence, rather than inventing an unprovided stage-by-stage arithmetic trace.

## 2.3 Terminal carry zero is retained

The moment represented by the transport is


$$
\sum_{\substack{r,s\ge0\\r+s+\varepsilon=m}}
 \binom ar^2\binom{B+s}{s}^2.
$$


Its final observation is $e_0$, enforcing zero outgoing addition carry after the actual finite word.

If a prefix product is the zero matrix, then for every remaining product $T$,


$$
P_LT e_0=0,\qquad P_L^{[1]}T e_0=0.
$$


The endpoint is therefore annihilated **with its required terminal acceptance**, not replaced by an unrestricted or infinite tail.

This proves the advertised all-continuation implication. It does not imply that a vanishing matrix product is always atomwise vanishing: products can vanish by cancellation. That distinction is important for column content.

---

# 3. A specific higher-layer target

A general mod-$p^2$ lift of the old unit-weight contraction is not the most economical next step at $u=2$. At this input the unit support is empty, but atoms of valuation exactly one can survive after division by $p$.

I therefore evaluate the complete contribution of those atoms through the first three digits.

The target is the exact finite squared-binomial kernel


$$
V(q)=\binom Xq\binom{2X+C-q}{C-q},
\qquad 0\le q\le C.
\tag{3.1}
$$



The relevant three-digit phase is


$$
C\equiv20916=(7,25,24)_{29}\pmod{p^3}.
\tag{3.2}
$$


At this phase,


$$
X\equiv2774=(19,8,3)_{29}\pmod{p^3},
$$




$$
2X\equiv5548=(9,17,6)_{29}\pmod{p^3}.
\tag{3.3}
$$



These are digits of the actual high kernel, not digits of an auxiliary replacement for $b$.

---

# 4. The carry-valued state and its paid arithmetic

For one digit, let

- $\alpha\in\{0,1\}$: incoming subtraction borrow in $X-q$;
- $\gamma\in\{0,1\}$: incoming carry in $2X+k$;
- $\sigma\in\{0,1\}$: incoming carry in $q+k=C$;
- $d,k\in\{0,\ldots,28\}$: digits of $q$ and $C-q$.

For input digits $A,B,M$ of $X,2X,C$, respectively, put


$$
\alpha'=\mathbf1_{d+\alpha>A},
\qquad
\ell=A-d-\alpha+p\alpha',
\tag{4.1}
$$




$$
\gamma'=\left\lfloor\frac{B+k+\gamma}{p}\right\rfloor,
\qquad
z=B+k+\gamma-p\gamma',
\tag{4.2}
$$


and require


$$
d+k+\sigma=M+p\sigma'.
\tag{4.3}
$$



The valuation increment is


$$
\alpha'+\gamma'.
\tag{4.4}
$$



Thus a valuation-at-most-one transport has the explicit finite state


$$
(\alpha,\gamma,\sigma,h),
\qquad
\alpha,\gamma,\sigma\in\{0,1\},\quad h\in\{0,1\},
$$


with transitions exceeding $h=1$ discarded. There are at most $16$ states.

Let


$$
f_j=j!\pmod p,\qquad 0\le j<p.
$$


The local squared factorial-unit weight is


$$
\boxed{
\left(
\frac{f_Af_z}{f_df_\ell f_Bf_k}
\right)^2.
}
\tag{4.5}
$$


Every denominator in (4.5) is a unit.

The usual factorial stripping, equivalently the mod-$p$ part of the prime-power binomial formula, gives this weight after the valuation has been separated. The possible Wilson signs disappear on squaring.

### Precision payment

To determine $V(q)^2\bmod p^3$:

- valuation-zero atoms would require their units modulo $p^3$;
- valuation-one atoms require only $(V(q)/p)^2\bmod p$;
- valuation at least two contributes zero, since
  

$$
p^4\mid V(q)^2.
$$



At the phase (3.2), valuation-zero atoms do not exist. Therefore (4.5) supplies all required arithmetic. No harmonic correction has been omitted at this precision: after the factor $p^2$ is paid, only an ordinary mod-$p$ unit remains.

This simplification is special to the proved phase. It is not a general justification for omitting harmonic interfaces.

---

# 5. Classification of every potentially surviving atom

## 5.1 The first digit must have no valuation event

At digit zero the input is


$$
(A,B,M)=(19,9,7).
$$



If a valuation-one atom had already spent its event here, then at digit one a zero-cost transition would have


$$
d\le8-\alpha,\qquad k\le11-\gamma,
\qquad \alpha+\gamma=1.
$$


Its digit sum would be at most $18$, while the cutoff equation requires at least $24$. This is impossible.

Hence every atom contributing modulo $p^3$ has no event at digit zero. Its low digits satisfy


$$
0\le d_0,k_0\le19,\qquad
d_0+k_0=7+29\varepsilon,\quad \varepsilon\in\{0,1\}.
\tag{5.1}
$$



Both cutoff branches are retained.

## 5.2 Exactly one event occurs at digit one

At digit one the input is


$$
(A,B,M)=(8,17,25),
$$


with incoming cutoff carry $\varepsilon$ and no incoming binomial borrow or carry.

An event-free transition is impossible. A transition with outgoing cutoff carry one requires


$$
d+k=54-\varepsilon,
$$


which forces both a subtraction borrow and an addition carry. It has valuation cost two and is discarded only after the $p^4$ square bound.

The valuation-one possibilities are exactly:

| Type | Digit range | Outgoing $(\alpha',\gamma',\sigma')$ |
|---|---|---|
| A | $0\le d\le8,\ k=25-\varepsilon-d$ | $(0,1,0)$ |
| B | $14-\varepsilon\le d\le25-\varepsilon,\ k=25-\varepsilon-d$ | $(1,0,0)$ |

No other valuation-one cases remain.

## 5.3 The third digit is a unique bridge

At digit two the input is


$$
(A,B,M)=(3,6,24).
$$


The incoming state has $\alpha+\gamma=1$ and cutoff carry zero.

To avoid a second event,


$$
d\le3-\alpha,\qquad k\le22-\gamma.
$$


Their maximum sum is exactly $24$. Therefore the transition is unique:


$$
d=3-\alpha,\qquad k=22-\gamma,
$$


and all outgoing carries are zero.

The squared bridge weights are:

- type A, incoming $(0,1,0)$:
  

$$
\left(\frac{f_{28}}{f_6f_{21}}\right)^2=20;
$$


- type B, incoming $(1,0,0)$:
  

$$
\left(\frac{f_3}{f_2}\right)^2
  \left(\frac{f_{28}}{f_6f_{22}}\right)^2=9.
$$



Thus the third digit returns every surviving path to the same ordinary zero-carry interface.

This is why a common finite tail can be factored out. The merger of branches occurs only after this explicit return calculation.

---

# 6. Evaluation of the new one-event coefficients

Let $A_\varepsilon$ and $B_\varepsilon$ be the digit-one sums of types A and B.

For type A,


$$
A_\varepsilon=
\sum_{d=0}^{8}
\binom8d^2
\left(
\frac{f_{13-\varepsilon-d}}
     {f_{17}f_{25-\varepsilon-d}}
\right)^2.
\tag{6.1}
$$



For type B, write $k=25-\varepsilon-d$, so $0\le k\le11$:


$$
B_\varepsilon=
\sum_{k=0}^{11}
\left(
\frac{f_8f_{17+k}}
 {f_{25-\varepsilon-k}f_{12+\varepsilon+k}f_{17}f_k}
\right)^2.
\tag{6.2}
$$



These are $42$ new unit-factorial contributions. Their individual residues are:

| Sum | Summand residues in the displayed order | Sum mod $29$ |
|---|---|---:|
| $A_0$ | $5,20,23,7,4,16,25,25,23$ | $3$ |
| $A_1$ | $13,22,9,13,25,13,9,22,13$ | $23$ |
| $B_0$ | $5,7,13,28,16,16,4,5,5,23,25,24$ | $26$ |
| $B_1$ | $13,4,16,4,20,4,4,20,4,16,4,13$ | $6$ |

Including the bridge gives


$$
R_0=20A_0+9B_0=4,
\qquad
R_1=20A_1+9B_1=21
\pmod p.
\tag{6.3}
$$



In particular, the normalized one-event interface is **not zero**. The old zero matrix cannot simply be divided by $p$ and treated as another zero matrix.

For the original first digit, put


$$
w_d=\binom{19}{d}^2\pmod p.
$$


The reflection


$$
\binom{9+k}{k}^2\equiv w_k\pmod p
$$


gives the low coefficients


$$
L_{\varepsilon,h}
=
\sum_{\substack{0\le d,k\le19\\d+k=7+29\varepsilon}}
d^h w_dw_k.
$$


Their values are


$$
\begin{array}{c|ccc}
&h=0&h=1&h=2\\ \hline
\varepsilon=0&10&6&11\\
\varepsilon=1&13&2&25
\end{array}
\tag{6.4}
$$


with the first-moment column also following from symmetry:


$$
2L_{\varepsilon,1}=7L_{\varepsilon,0}\pmod p.
$$



These low coefficients are consistent with the accepted low connection; their full $400$-pair calculation is not proposed again.

Finally,


$$
\begin{aligned}
E_0&=4\cdot10+21\cdot13=23,\\
E_1&=4\cdot6+21\cdot2=8,\\
E_2&=4\cdot11+21\cdot25=18
\end{aligned}
\pmod p.
\tag{6.5}
$$



---

# 7. The paid three-digit connection

### Theorem 7.1

Let


$$
C=20916+p^3t,\qquad t\ge0,
\qquad X=2001C+1382.
$$


Define the exact finite moments $T_h$ as in the executive assessment. Then


$$
\boxed{
T_h(C)\equiv p^2E_h\mathcal H(t)\pmod{p^3},
\qquad
(E_0,E_1,E_2)=(23,8,18),
}
\tag{7.1}
$$


where $\mathcal H(t)$ is the finite sum (E.2).

Moreover,


$$
\boxed{
p\mid V(q)\quad(0\le q\le C),
}
\tag{7.2}
$$




$$
\boxed{2T_1(C)\equiv7T_0(C)\pmod{p^3},}
\tag{7.3}
$$


and


$$
\boxed{\mathcal D(C)\equiv0\pmod{p^2}.}
\tag{7.4}
$$



### Proof

The first two digits admit no path of valuation zero, proving (7.2).

Modulo $p^3$, atoms with at least two events may be discarded because their squares are divisible by $p^4$. Sections 5–6 classify and evaluate every remaining path.

After digit two, all three carries are zero. Consequently, if $r,s$ are the remaining high parts of $q,C-q$, their exact relation is


$$
r+s=t,\qquad 0\le r\le t.
\tag{7.5}
$$


There is no extra endpoint and no unfinished cutoff carry.

The upper parameters split exactly as


$$
X=2774+p^3(1716+2001t),
$$




$$
2X=5548+p^3(3432+4002t).
$$


Factorial stripping therefore leaves the common high kernel in (E.2).

The square has already supplied $p^2$, so for $T_h\bmod p^3$ only


$$
q^h\equiv d_0^h\pmod p
$$


is needed. Equations (6.3)–(6.5) give (7.1).

Because


$$
2E_1=16=7E_0\pmod p,
$$


equation (7.3) follows.

Finally,


$$
X+C+1\equiv27,\qquad
3X+C+1\equiv7\pmod p.
$$


Using (7.1),


$$
\begin{aligned}
&(X+C+1)
\bigl((3X+C+1)T_0-2T_1\bigr)\\
&\qquad\equiv
p^2\cdot27\,(7\cdot23-2\cdot8)\mathcal H(t)
=0\pmod{p^3},
\end{aligned}
$$


since $7\cdot23-2\cdot8=145=5p$.

Dividing this **whole numerator** by $p$ proves (7.4). ∎

### What has been evaluated

The theorem evaluates $\mathcal D\bmod841$ for every continuation of the specified prefix. It also proves


$$
T_0=T_1=T_2=0\pmod{841}.
$$



It does **not** evaluate $\mathcal H(t)$. Accordingly, the normalized squared-weight moment


$$
T_0/p^2=23\mathcal H(t)\pmod p
$$


may vanish further.

This is an actual higher-layer connection and an actual higher divided-difference zero—not a claim that the first nonzero normalized norm has been found.

---

# 8. Instantiation on the original orbit

The accepted modular exponentiation data give


$$
C(u)\equiv276031+128527u\pmod{707281}.
\tag{8.1}
$$


For clarity, the slope follows from


$$
\beta g\equiv128527\pmod{707281}.
$$



Reducing (8.1) modulo $p^3=24389$,


$$
C(u)\equiv7752+6582u\pmod{24389}.
\tag{8.2}
$$


Since $6582\not\equiv0\pmod{29}$, this is a unit-affine parametrization at this precision. At $u=2$,


$$
7752+2\cdot6582=20916.
$$



Thus:

### Corollary 8.1 — Original higher-layer zero progression

For every nonnegative original index


$$
u\equiv2\pmod{24389},
$$


the exact high sums satisfy


$$
\boxed{
T_0=T_1=T_2=0\pmod{841},
\qquad
\mathcal D=0\pmod{841}.
}
\tag{8.3}
$$



This progression is different from the earlier four-digit killing-word progression. Its new conclusion concerns a paid higher layer of the high observables.

No new modular exponentiation is required to establish (8.3): the accepted original residues already supply its input congruence.

---

# 9. What the four physical zero cases imply about content

Retain


$$
P=\frac{Z_w}{p^2}=p^cx,\qquad
Q=\frac Y{p^3},\qquad
\nu=v_p(x^Tx),
$$


with $x$ primitive at $p$, and


$$
d=v_p(Z_w^TZ_w)=2c+4+\nu.
\tag{9.1}
$$



At each of $u=0,1,2,381475$, the accepted complete reduction and the evaluated $\kappa=0$ give


$$
d\ge8.
\tag{9.2}
$$



This yields the rigorous alternatives


$$
\boxed{
c=1\Longrightarrow\nu\ge2;
\qquad
c\ge2\text{ remains possible}.
}
\tag{9.3}
$$



A vanished physical norm digit does not decide between an isotropic primitive reduction and extra column content.

Nor does the atomwise high-kernel statement (7.2), by itself, prove the same additional factor for the complete corrected first column. The actual head, lower corrections and finite return must be handled before making that transfer.

---

# 10. The next complete physical norm connection

There is a useful exact connection at the next physical layer which makes the content alternatives explicit.

Assume the retained $c\ge1$, and obtain the **complete** column modulo $p^6$. Write its successive digit vectors as


$$
Z_w\equiv p^3z_0+p^4z_1+p^5z_2\pmod{p^6},
\tag{10.1}
$$


with all coordinates $0\le j\le b$ retained.

At any of the four zero cases, define


$$
\eta_2=\frac{Z_w^TZ_w}{p^8}\pmod p.
$$


Then


$$
\boxed{
\eta_2=
\frac{
z_0^Tz_0+2p\,z_0^Tz_1+
p^2(z_1^Tz_1+2z_0^Tz_2)
}{p^2}
\pmod p.
}
\tag{10.2}
$$


The numerator is divided as a whole. Its divisibility by $p^2$ follows from the already established $d\ge8$.

This gives three distinct cases.

1. **If $c=1$:** $z_0\ne0$, and the term $2z_0^Tz_2$, together with the whole carry from the first two terms, is indispensable.

2. **If $c=2$:** $z_0=0$, $z_1\ne0$, and
   

$$
\eta_2=z_1^Tz_1\pmod p.
$$



3. **If $c\ge3$:** $z_0=z_1=0$, so $\eta_2=0$.

In particular, if a future complete calculation gives $\eta_2\ne0$, then $d=8$, but there are still two possibilities:


$$
(c,\nu)=(1,2)\quad\text{or}\quad(2,0).
\tag{10.3}
$$



Thus even a nonzero next physical norm digit does not identify content without a separate column certificate.

## 10.1 The terminal coordinate returns at this layer

The retained terminal formula is


$$
\frac{Z_{w,b}}{p^3}
\equiv14pA_0\frac{W_b}{p^4}\pmod{p^2}.
$$


Hence


$$
z_{0,b}=0,\qquad
z_{1,b}\equiv14A_0\frac{W_b}{p^4}\pmod p.
$$



Its contribution to (10.2) is therefore


$$
\boxed{
z_{1,b}^2
=
22A_0^2\left(\frac{W_b}{p^4}\right)^2
\pmod p.
}
\tag{10.4}
$$


This term was invisible in the preceding physical norm digit. It is now present unless its actual factors vanish.

This is one precise obstruction to interpreting a lifted leading-atom row as the next complete physical norm.

## 10.2 The previously eliminated corrections cannot simply be dropped

For a complete output modulo $p^6$, the retained finite bounds become


$$
M=29\cdot6-1=173,\qquad
L=58\cdot6+2=350.
$$



The full integral endpoint solution remains available through


$$
(I+G)^{-1}
\equiv\sum_{\ell=0}^{5}(-G)^\ell\pmod{p^6},
\qquad
G=K_\times\mathsf DF\in pM(\mathbb Z_p).
\tag{10.5}
$$



The earlier statements


$$
p^2\mathcal R\mathsf R_n\mathsf D_2\mathsf R_nw
\equiv0\pmod{p^5},
$$


and


$$
p^2\mathcal R\mathsf R_n\mathsf D_1\mathsf R_nz_1
\equiv0\pmod{p^5}
$$


do not make those terms zero modulo $p^6$. They can enter $z_2$ and hence (10.2).

The actual higher head and the complete higher return must likewise be retained. Equation (10.2) is a proved connection for a complete producer, not an evaluation of that producer.

---

# 11. Exact relative precision budgets

## 11.1 Norm precision

Suppose


$$
Z_w-\widetilde Z\in p^{K_Z}\mathbb Z_p^{b+1},
\qquad
Z_w,\widetilde Z\in p^{c+2}\mathbb Z_p^{b+1}.
$$


Because $p$ is odd,


$$
Z_w^TZ_w-\widetilde Z^T\widetilde Z
\in p^{K_Z+c+2}\mathbb Z_p
$$


when $K_Z\ge c+2$.

To determine the first nonzero raw norm digit, modulo $p^{d+1}$, it suffices that


$$
\boxed{
K_Z\ge d-c-1=c+3+\nu.
}
\tag{11.1}
$$



At the currently killed layer, a uniform complete lift modulo $p^6$ determines the norm modulo $p^9$, using only $c\ge1$. It does not guarantee that the first nonzero digit occurs there.

## 11.2 Mixed precision

The outstanding alignment is


$$
x^TQ-p^c\rho_nx^Tx
\equiv0\pmod{p^{c+\nu+1}}.
\tag{11.2}
$$


In raw columns this is exactly


$$
\boxed{
Z_w^TY-p\rho_n Z_w^TZ_w
\equiv0\pmod{p^{d+2}}.
}
\tag{11.3}
$$



Using only


$$
v_p(Z_w)\ge c+2,\qquad v_p(Y)\ge3,
$$


sufficient separate physical precisions are


$$
\boxed{
K_Z\ge d-1,\qquad K_Y\ge d-c.
}
\tag{11.4}
$$



Indeed, the two mixed perturbations have depths at least $K_Z+3$ and $K_Y+c+2$, respectively. Both must reach $d+2$. The norm term imposes no stronger requirement.

The retained logarithmic guard is


$$
\boxed{
N_{\log}\ge c+4+\nu=d-c.
}
\tag{11.5}
$$



These are budgets in the actual $c,d,\nu$, not budgets obtained by silently setting $c=1$.

---

# 12. Both complete second-force initial charges remain

The second-force identity is unchanged:


$$
\boxed{
p^3U_a^TQ=
p^3(r_0G^{(3)}_{a0}+r_1G^{(3)}_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda'_{a,\ell}
+W_bU_{a,b}.
}
\tag{12.1}
$$



Both initial charges are


$$
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(
T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}
\right),
\qquad i=0,1.
\tag{12.2}
$$


Every source row remains


$$
\mathcal H_i=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b},
\qquad1\le i\le b-2.
\tag{12.3}
$$



There is no source row at $b-1$. The exterior contribution at $b$ is not another recurrence step. The division by $p^3$ belongs to the whole right-hand side of (12.1).

Neither the new high-kernel connection nor the physical quadratic identity proves this complete mixed alignment.

---

# 13. A small, genuinely new follow-on calculation

The new theorem leaves one particularly concrete target:


$$
\mathcal H(t)\pmod{29}
$$


at


$$
t=\frac{C(2)-20916}{29^3}.
$$



This is a **normalized tail after the valuation-one block has been paid**. It is not the already accepted unnormalized product that vanished at the first high digit.

A bounded prefix test for this tail would require only ordinary two-state arithmetic.

## Inputs

Set


$$
E=1397629859,\qquad \text{cap}=32,
$$


and compute


$$
R=3^E\bmod29^{41}.
$$


Then


$$
C_{\rm part}=\frac{R-\beta}{29^6}
$$


determines $C(2)\bmod29^{35}$, and


$$
t_{\rm part}=\frac{C_{\rm part}-20916}{29^3}
$$


determines $t\bmod29^{32}$.

Use the first $32$ digits of


$$
A=1716+2001t,\qquad B=2A,\qquad M=t.
$$



Starting from the row $e_0^T$, use


$$
K_i[e,f]=
\sum_{\substack{
0\le d\le A_i\\
0\le k\le28-B_i\\
d+k=M_i+29f-e}}
\binom{A_i}{d}^2\binom{B_i+k}{k}^2
\pmod{29}.
\tag{13.1}
$$



## Expected verifiable output

Return:

1. the exact bounded residue and the $32$-digit input prefixes;
2. the successive two-coordinate rows;
3. either the first zero row, or the final nonzero row with no further conclusion.

A zero row would prove


$$
\mathcal H(t)=0\pmod{29}
$$


for the actual original parameter, independently of its unread digits and with terminal carry zero retained. By (7.1), it would then evaluate


$$
T_0=T_1=T_2=0\pmod{29^3}
$$


at $u=2$.

A nonzero residual row would **not** prove a nonzero final $\mathcal H(t)$.

The digit part needs at most


$$
32\cdot116=3712
$$


low summands, plus bounded modular exponentiation. This is an unevaluated specification here. No accepted computation is proposed for repetition, and no execution is assumed.

The new theorem (7.4) does not depend on this follow-on calculation.

---

# 14. All-prime normalization and the whole error

No row contents, row metric or least actual two-column clearer have been changed.

Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
\tag{14.1}
$$


The gcd is over all primes, and the primitive multiplier remains


$$
\frac{d_B^2}{g_B}.
$$



In particular,


$$
\boxed{
\log q_n=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{14.2}
$$



For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the relevant whole same-index expression remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{14.3}
$$



The density-one zero theorem and the complete-column unbounded-content theorem remain valid at their different stated scopes. Neither bounds (14.2), and neither supplies the required nonzero real error comparison.

The literature gate is used at precisely its established scope: Lucas/Kummer and prime-power factorial methods justify the digit arithmetic; general Cartier existence is not being offered as a completed physical evaluation. No universal novelty claim is made.

---

# 15. Proof-status ledger

| Statement | Status |
|---|---|
| Accepted $400/90/302/138$ bounded controls | Reused; no repetition requested |
| Original progression $381475\bmod707281$ | Accepted exact modular instantiation |
| Original prefix zero lengths $5,13,1,3$ | Accepted finite execution after source audit |
| Correct first-digit weighting | Independently checked |
| Actual terminal carry zero retained | Proved |
| Unit support empty at original $u=2$ | Proved from the first high digit |
| Three-digit valuation-one state classification | **Proved explicitly** |
| New $42$ one-event factorial-unit contributions | **Evaluated explicitly** |
| Normalized interface coefficients $R_0=4,R_1=21$ | **Evaluated** |
| Paid connection $(T_0,T_1,T_2)=p^2(23,8,18)\mathcal H\bmod p^3$ | **Proved** |
| $\mathcal D=0\bmod841$ for $C\equiv20916\bmod24389$ | **Proved and evaluated for every continuation** |
| Original progression $u\equiv2\bmod24389$ for that higher zero | **Proved from accepted original residues** |
| Value of the remaining normalized tail $\mathcal H$ | Unevaluated |
| Complete next physical norm connection, including terminal square | **Proved** |
| Exact norm and mixed precision budgets | **Proved** |
| Actual $c$ and first nonzero primitive norm layer at the four cases | Open |
| Complete second-force relative alignment | Open |
| All-prime primitive denominator versus whole nonzero error | Open |

---

## Conclusion

The new result goes beyond the evaluated zero layer by paying for the first discarded nonunit support. At the actual original progression


$$
u\equiv2\pmod{24389},
$$


the complete valuation-one calculation gives


$$
\boxed{
(T_0,T_1,T_2)
\equiv29^2(23,8,18)\mathcal H
\pmod{29^3},
}
$$


and consequently the whole divided difference satisfies the new higher-precision evaluation


$$
\boxed{\mathcal D=0\pmod{841}.}
$$



The normalized one-event interface itself is nonzero: its branch coefficients are $4$ and $21$. Thus this result does not arise from incorrectly dividing a zero unit matrix. It arises from retaining the missing carry states, evaluating their unit weights, proving their common terminal return, and then evaluating the resulting first-moment cancellation.

The exact remaining local bottleneck is now twofold:

1. evaluate the displayed normalized tail if a further high-kernel norm digit is wanted;
2. for the **physical primitive norm**, obtain the actual complete column content and a sufficiently deep complete lift, including higher head, lower corrections and finite return.

The second task cannot be replaced by the first. In particular, the terminal square already returns at the next physical norm layer.

Finally, the global bottleneck remains


$$
\boxed{
\text{the actual all-prime primitive denominator compared with the whole,
nonzero, same-index error on an infinite original sequence}.
}
$$


No supplied or newly proved result establishes that comparison. Therefore an unconditional proof or disproof of the irrationality of $e+\pi$ remains unresolved.
