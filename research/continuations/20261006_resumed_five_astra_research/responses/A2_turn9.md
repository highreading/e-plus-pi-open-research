> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 9 — An integral digit connection and a density-one original-orbit annihilation theorem

## Executive assessment

The new receipt closes the proposed auxiliary implementation check at exactly its stated scope:



$$
\mathcal N(C)\equiv754,\ 261,\ 290\pmod{841},
\qquad
\kappa(C)\equiv26,\ 9,\ 10\pmod{29},
\quad C=0,1,2.
$$



These are three compatible auxiliary inputs, not original powers and not complete physical $\eta$-evaluations. I do not repeat that calculation or transfer its nonzero values to the original orbit.

Starting from the actual retained row


$$
\boxed{
\kappa(C)=21D(C)+16S_2(C)
 +(25+18C+19C^2+24C^3)S_0(C)\pmod{29},
}
\tag{0.1}
$$


I obtain two new results.

1. **An integral unequal-precision connection.**  
   The whole divided difference $D\bmod29$, initially requiring a numerator modulo $29^2$, reduces to four ordinary finite moments modulo $29$. Those moments admit an explicit two-state digit contraction, with exact terminal acceptance. No singular rational-moment pivot is inverted.

2. **A new original-compatible annihilation theorem.**  
   If the base-$29$ expansion of $C$ contains the consecutive digits
   

$$
\boxed{(0,2,5,28)}
   \tag{0.2}
$$


   in least-significant-first order, then
   

$$
\boxed{D(C)=S_0(C)=S_2(C)=\kappa(C)=0\pmod{29}.}
   \tag{0.3}
$$


   This criterion is independent of all incoming multiplication, subtraction and addition carries.

   On the restricted original power orbit, the criterion holds on a set of **relative natural density one in every original arithmetic progression**. In particular,
   

$$
\boxed{
   \{u\ge0:\kappa(C(u))\ne0\}
   \text{ has relative natural density zero in every progression.}
   }
   \tag{0.4}
$$



This is an actual original-orbit annihilation theorem, not a transfer from an auxiliary nonzero value. It does **not** prove annihilation at every original index: the exceptional original indices avoiding the displayed word remain unresolved. Nor does it identify a first nonzero primitive norm layer or solve the complete mixed-force alignment.

---

# 1. Retained problem and source assessment

Throughout,


$$
p=29,\qquad
\Lambda=29^6=594823321,\qquad
\beta=410910916,
$$




$$
b=3^{249005515+574312172u}
 =\beta+\Lambda C,\qquad n=2001b,\qquad u\ge0.
\tag{1.1}
$$



The original domains remain


$$
0\le j<b,\qquad 1\le i\le b-2,\qquad 0\le j\le b
$$


for contact coordinates, source rows and reconstructed coordinates.

The corrected columns remain


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,
\qquad W_j=\binom{n+2}{j}.
\tag{1.2}
$$



I reuse Turn 8’s evaluated low-interface row (0.1), with


$$
X=2001C+1382,\qquad
V(q)=\binom Xq\binom{2X+C-q}{C-q},
\qquad 0\le q\le C,
\tag{1.3}
$$




$$
S_0=\sum_{q=0}^{C}V(q)^2,\qquad
S_2=\sum_{q=0}^{C}q^2V(q)^2\pmod p,
\tag{1.4}
$$


and


$$
D=
\frac{\displaystyle\sum_{q=0}^{C}
 \left((2X+C+1-q)^2-(X-q)^2\right)V(q)^2}{p}
 \pmod p.
\tag{1.5}
$$



The division in (1.5) is still division of the **whole finite difference**.

## 1.1 What the new receipt establishes

The supplied source:

- constructs exactly the $191268$ retained supported low residues;
- retains $q=0,\ldots,C$ without extending the cutoff;
- evaluates $1147608$ supported atoms across the three auxiliary inputs;
- returns the whole residues $754,261,290\bmod841$;
- verifies $4245$ independent small unit-binomial cases.

The count $4245$ is consistent with


$$
\sum_{t=0}^{89}(t+1)+5\cdot30=4095+150.
$$



The initial provisional assignment to `beta` is overwritten before use by the authoritative digit construction; the asserted value used in the calculation is $410910916$.

The factorial-unit implementation uses the product of all units modulo $29^2$, which is $-1$, and strips factorials through successive divisions by $29$. Its mathematical interpretation is consistent with the retained prime-power factorial decomposition.

The outside-support exclusion is not independently proved by this program. It remains the retained valuation theorem. Nothing in the receipt evaluates an original power, a complete physical column, or the primitive denominator.

## 1.2 Scope of the new derivation

The following connection and annihilation results concern the explicit finite sums (1.3)–(1.5). They do not depend on reopening the actual next head, compatible $\mathsf D_2$, crossed return, or second-return contraction.

A4’s independent acceptance of complete-column unbounded content is retained. Its audit of the full norm-only elimination remains a separate source-assessment issue; the high-observable theorems below do not substitute for that audit.

---

# 2. Removing the first high digit without losing the divided difference

Write


$$
C=\delta+pm,\qquad 0\le\delta<p,
$$


and put


$$
a=69C+47,\qquad B=2a+1.
\tag{2.1}
$$


Then, exactly,


$$
X=19+pa,\qquad 2X=9+pB.
\tag{2.2}
$$



For $q+k=C$, write


$$
q=d+pr,\qquad k=e+ps.
$$


The low addition has two branches:


$$
d+e=\delta+p\varepsilon,\qquad
s=m-\varepsilon-r,\qquad
\varepsilon\in\{0,1\}.
\tag{2.3}
$$



A term can survive in $V(q)^2\bmod p^2$ only if neither binomial in $V(q)$ has a low-digit valuation event. This requires


$$
0\le d\le19,\qquad 0\le e\le19.
\tag{2.4}
$$



Define the exact low sets


$$
\mathcal E_{\delta,\varepsilon}
=\{(d,e):0\le d,e\le19,\ d+e=\delta+p\varepsilon\}.
\tag{2.5}
$$



For each branch define


$$
L_\varepsilon=m-\varepsilon,
$$




$$
U_\varepsilon(r)=
\binom ar\binom{B+L_\varepsilon-r}{L_\varepsilon-r},
\qquad 0\le r\le L_\varepsilon.
\tag{2.6}
$$


If $L_\varepsilon<0$, this is an empty sum.

Thus both cutoff branches remain present, with their actual ranges:


$$
\boxed{0\le r\le m-\varepsilon.}
\tag{2.7}
$$



In particular, the $\varepsilon=1$ branch is neither merged into the first branch nor completed at its endpoint.

---

# 3. The compatible factorial-unit lift and exact low reflection

For $0\le t\le28$, let


$$
H_t=\sum_{j=1}^{t}j^{-1}\in\mathbb F_{29},
\qquad H_0=0.
$$



The no-low-carry factorial-unit identity gives


$$
\binom{ph+\alpha}{pk+\gamma}
\equiv
\binom hk\binom\alpha\gamma
\left[
1+p\bigl(hH_\alpha-kH_\gamma-(h-k)H_{\alpha-\gamma}\bigr)
\right]\pmod{p^2},
\tag{3.1}
$$


when $0\le\gamma\le\alpha<p$.

This congruence does not require the high binomial $\binom hk$ to be a unit. It follows by stripping one factorial level and applying the compatible unit-factorial expansion.

Applied to (2.2)–(2.6), it yields


$$
V(q)^2\equiv
\binom{19}{d}^{2}\binom{9+e}{e}^{2}
U_\varepsilon(r)^2(1+2pE)
\pmod{p^2},
\tag{3.2}
$$


where


$$
\begin{aligned}
E={}&
aH_{19}-rH_d-(a-r)H_{19-d}\\
&+(B+s)H_{9+e}-sH_e-BH_9.
\end{aligned}
\tag{3.3}
$$



Introduce


$$
w_t=\binom{19}{t}^{2},\qquad
h_t=H_{9+t}-H_9,\qquad
t_t=H_{9+t}-H_t
\quad(0\le t\le19).
\tag{3.4}
$$



Since $H_{28-v}=H_v\pmod{29}$,


$$
H_{19-d}=H_{9+d},\qquad H_{19}=H_9.
$$


Consequently


$$
\boxed{
E=-a h_d+B h_e+r t_d+s t_e.
}
\tag{3.5}
$$



There is also a compatible second-digit reflection:


$$
\binom{9+e}{e}
=(-1)^e\binom{-10}{e}
=(-1)^e\binom{19-p}{e}.
$$


All denominators here are units because $e\le19$. Therefore


$$
\boxed{
\binom{9+e}{e}^{2}
\equiv w_e(1+2p h_e)\pmod{p^2}.
}
\tag{3.6}
$$



Equation (3.6), not merely its reduction modulo $p$, supplies the carry required by $D$.

---

# 4. Explicit integral connection for $(D,S_0,S_2)$

For each $(\delta,\varepsilon)$, define four finite coefficients in $\mathbb F_{29}$:


$$
K_{\delta,\varepsilon}
=\sum_{\mathcal E_{\delta,\varepsilon}}w_dw_e,
\tag{4.1}
$$




$$
J_{\delta,\varepsilon}
=\sum_{\mathcal E_{\delta,\varepsilon}}d^2w_dw_e,
\tag{4.2}
$$




$$
H_{\delta,\varepsilon}
=\sum_{\mathcal E_{\delta,\varepsilon}}
(e-d)w_dw_eh_e,
\tag{4.3}
$$




$$
T_{\delta,\varepsilon}
=\sum_{\mathcal E_{\delta,\varepsilon}}
(e-d)w_dw_et_e.
\tag{4.4}
$$



These are genuinely bounded low-digit coefficients. Across all $29$ values of $\delta$ and both branches, their summation sets contain exactly the $20^2=400$ ordered pairs $(d,e)$.

Define ordinary high moments


$$
M_{\varepsilon,0}
=\sum_{r=0}^{L_\varepsilon}U_\varepsilon(r)^2,
\qquad
M_{\varepsilon,1}
=\sum_{r=0}^{L_\varepsilon}r\,U_\varepsilon(r)^2
\pmod p.
\tag{4.5}
$$



### Theorem 4.1 — Unequal-precision digit connection

For every nonnegative compatible $C$,


$$
\boxed{
S_0=\sum_{\varepsilon=0}^{1}
K_{\delta,\varepsilon}M_{\varepsilon,0}\pmod p,
}
\tag{4.6}
$$




$$
\boxed{
S_2=\sum_{\varepsilon=0}^{1}
J_{\delta,\varepsilon}M_{\varepsilon,0}\pmod p,
}
\tag{4.7}
$$


and


$$
\boxed{
\begin{aligned}
D=(20+\delta)\sum_{\varepsilon=0}^{1}
\Bigl[&
(3a+2)(K_{\delta,\varepsilon}+2H_{\delta,\varepsilon})
 M_{\varepsilon,0}\\
&+(K_{\delta,\varepsilon}+2T_{\delta,\varepsilon})
 \bigl(L_\varepsilon M_{\varepsilon,0}
       -2M_{\varepsilon,1}\bigr)
\Bigr]\pmod p.
\end{aligned}
}
\tag{4.8}
$$



Thus the numerator defining $D$ has been processed at precision $p^2$, but all remaining high observables require only precision $p$.

## Proof

Equations (4.6)–(4.7) follow immediately from (3.2), since


$$
q\equiv d\pmod p.
$$



For $D$, factor the exact multiplier:


$$
(2X+C+1-q)^2-(X-q)^2
=(X+C+1)(3X+C+1-2q).
\tag{4.9}
$$


Using $q=d+pr$, $k=e+ps$, this is


$$
\bigl(20+\delta+p(a+m)\bigr)
\bigl(e-d+p(3a+2+s-r)\bigr).
\tag{4.10}
$$



For fixed $(\varepsilon,r)$, the high factor $U_\varepsilon(r)^2$ is independent of $d,e$. The exact symmetry of $w_dw_e$ gives


$$
\sum_{\mathcal E_{\delta,\varepsilon}}
(e-d)w_dw_e=0.
\tag{4.11}
$$



Hence the term $p(a+m)$ in the first factor of (4.10) contributes zero modulo $p^2$ after contraction. There is no division of an individual, possibly nondivisible summand.

By (3.6), the divided contribution from the low lift itself is


$$
2H_{\delta,\varepsilon}.
\tag{4.12}
$$



Using (3.5) and swapping $d,e$,


$$
\sum_{\mathcal E_{\delta,\varepsilon}}
(e-d)w_dw_eE
=(a+B)H_{\delta,\varepsilon}
 +(s-r)T_{\delta,\varepsilon}.
\tag{4.13}
$$


Since $B=2a+1$, the complete divided bracket is


$$
\begin{aligned}
&2H_{\delta,\varepsilon}
 +(3a+2+s-r)K_{\delta,\varepsilon}\\
&\qquad
 +2(3a+1)H_{\delta,\varepsilon}
 +2(s-r)T_{\delta,\varepsilon}\\
&=(3a+2)(K_{\delta,\varepsilon}+2H_{\delta,\varepsilon})
 +(s-r)(K_{\delta,\varepsilon}+2T_{\delta,\varepsilon}).
\end{aligned}
\tag{4.14}
$$



Finally $s-r=L_\varepsilon-2r$, giving (4.8).

Terms excluded by (2.4) have $V(q)^2\in p^2\mathbb Z$, so they contribute zero after the whole numerator is divided by $p$ and reduced modulo $p$. All branch endpoints remain as in (2.7). ∎

### Consequence

The next high unit digit has not been renamed as another divided observable. It has been eliminated by an explicit integral contraction. Only ordinary mod-$29$ moments remain.

---

# 5. The actual carry row after the connection

Put


$$
P(\delta)=25+18\delta+19\delta^2+24\delta^3.
$$


For brevity suppress $\delta$ in the four low coefficients and define


$$
\lambda_\varepsilon
=
21(20+\delta)(3a+2)(K_\varepsilon+2H_\varepsilon)
 +16J_\varepsilon+P(\delta)K_\varepsilon,
\tag{5.1}
$$




$$
\mu_\varepsilon
=
21(20+\delta)(K_\varepsilon+2T_\varepsilon).
\tag{5.2}
$$



Because


$$
a\equiv11\delta+18\pmod{29},
$$


these coefficients depend only on $\delta$, not on the unread high word.

Substitution in the retained actual row proves


$$
\boxed{
\kappa(C)=
\sum_{\varepsilon=0}^{1}
\left[
(\lambda_\varepsilon+\mu_\varepsilon L_\varepsilon)
M_{\varepsilon,0}
-2\mu_\varepsilon M_{\varepsilon,1}
\right]\pmod{29}.
}
\tag{5.3}
$$



This is a connection for the specified row $21D+16S_2+P(C)S_0$, not for a substitute Hahn weight or an unrestricted completed sum.

---

# 6. A two-state integral closure, with terminal acceptance

The remaining moments have a particularly small mod-$29$ closure.

Write the base-$29$ digits of $a,B,m$ as


$$
a_i,\quad B_i,\quad m_i.
$$


For each digit define a $2\times2$ matrix


$$
\boxed{
\mathsf K_i[e,f]
=
\sum_{\substack{
0\le d\le a_i\\
0\le k\le28-B_i\\
d+k=m_i+29f-e}}
\binom{a_i}{d}^{2}
\binom{B_i+k}{k}^{2}
\pmod{29},
}
\tag{6.1}
$$


where $e,f\in\{0,1\}$.

At digit zero also define


$$
\mathsf K_0^{[1]}[e,f]
=
\sum_{\substack{
0\le d\le a_0\\
0\le k\le28-B_0\\
d+k=m_0+29f-e}}
d\binom{a_0}{d}^{2}
\binom{B_0+k}{k}^{2}
\pmod{29}.
\tag{6.2}
$$



Let $L$ be any digit length large enough to contain $a,B,m$, and let $e_0,e_1$ denote the standard coordinate columns. Then


$$
\boxed{
M_{\varepsilon,0}
=e_\varepsilon^T\mathsf K_0\mathsf K_1\cdots
\mathsf K_{L-1}e_0,
}
\tag{6.3}
$$




$$
\boxed{
M_{\varepsilon,1}
=e_\varepsilon^T\mathsf K_0^{[1]}\mathsf K_1\cdots
\mathsf K_{L-1}e_0.
}
\tag{6.4}
$$



The initial state is the retained cutoff branch $\varepsilon$. The final state is **zero**, enforcing the finite equality


$$
r+s=m-\varepsilon.
$$


An unfinished carry is not accepted.

## 6.1 Why these matrices are correct

Modulo $29$, a nonzero term requires:

- no borrow in $a-r$, hence $r_i\le a_i$;
- no carry in $B+s$, hence $s_i\le28-B_i$.

Lucas factorization then gives the product in (6.1). The equality $r+s+\varepsilon=m$ contributes precisely the two addition-carry states. The first moment needs only $r\bmod29=r_0$, which explains (6.2).

This is an explicit finite-range-preserving contraction, not an appeal to generic automaticity.

## 6.2 Saturation and the singular pivot

The connection uses only:

- integer binomial coefficients;
- harmonic denominators $1,\ldots,28$, all units at $29$;
- the already-divisible whole numerator in $D$.

It never divides by the rational telescoping pivot $r+11$. In particular, the singular class $r\equiv18\pmod{29}$ is bypassed rather than inverted.

The tail state lattice is the full free lattice with basis “incoming carry $0$” and “incoming carry $1$.” Every digit matrix has an integral lift. There is no passage through a smaller nonsaturated moment lattice.

One can also check that the two state observations are not concealing a factor of $29$. The empty terminal observation is $(1,0)^T$; the one-digit case $a=B=0,m=1$ gives $(1,1)^T$. These form a determinant-one basis. Thus the state observation lattice is saturated.

This closure is asserted at the required mod-$29$ scope. It is not a claim that the same two states evaluate arbitrary higher-precision moments.

## 6.3 Explicit resource bounds

For each matrix entry, $k$ is determined by $d,e,f,m_i$. Thus one digit needs at most


$$
4\cdot29=116
$$


low summands, followed by a $2\times2$ contraction.

The low connection table requires only $400$ pair contributions. The binomial and harmonic tables have size bounded solely by $29$.

The remaining work is therefore


$$
O(\log_{29}(C+1))
$$


field operations up to an explicit constant, with two tail coordinates and one additional first-digit weighted matrix.

**Limitation.** This is still original-word-linear work. At a genuine original index it is a proved connection, not a completed numerical evaluation. The next section supplies an original-orbit theorem that avoids reading the whole word on a large, explicitly described set.

---

# 7. A four-digit killing word for the actual observables

Let the base-$29$ digits of $C$ be $C_i$, least significant first.

### Theorem 7.1 — Carry-independent annihilating word

Suppose that, for some $h\ge0$,


$$
(C_h,C_{h+1},C_{h+2},C_{h+3})=(0,2,5,28).
\tag{7.1}
$$


Then every $q$ in the original finite range satisfies


$$
\boxed{29\mid V(q).}
\tag{7.2}
$$


Consequently


$$
\boxed{D(C)=S_0(C)=S_2(C)=\kappa(C)=0\pmod{29}.}
\tag{7.3}
$$



## Proof

First examine


$$
a=69C+47.
$$


Let $\tau_i$ be the multiplication carry entering digit $i$:


$$
a_i+29\tau_{i+1}=69C_i+\tau_i,\qquad \tau_0=47.
\tag{7.4}
$$


For every $i$,


$$
0\le\tau_i\le68.
\tag{7.5}
$$



At the four prescribed digits:

1. $C_h=0$ gives
   

$$
\tau_{h+1}\in\{0,1,2\}.
$$



2. $C_{h+1}=2$ gives
   

$$
69\cdot2+\tau_{h+1}\in\{138,139,140\},
$$


   so
   

$$
a_{h+1}\in\{22,23,24\},\qquad \tau_{h+2}=4.
$$



3. $C_{h+2}=5$ gives
   

$$
69\cdot5+4=349=29\cdot12+1,
$$


   hence
   

$$
a_{h+2}=1.
$$



Now $B=2a+1$. Since the previous digit $a_{h+1}$ is at least $22$, the doubling carry into position $h+2$ is $1$, independently of the earlier doubling carry. Therefore


$$
B_{h+2}=2\cdot1+1=3.
\tag{7.6}
$$



Using $X=19+29a$ and $2X=9+29B$, at position


$$
t=h+3
$$


we have


$$
\boxed{X_t=1,\qquad (2X)_t=3,\qquad C_t=28.}
\tag{7.7}
$$



Fix any $0\le q\le C$, and put $k=C-q$. If $V(q)$ were a unit modulo $29$, Kummer’s theorem would require:

- no borrow in $X-q$, so $q_t\le1$;
- no carry in $2X+k$, so $k_t\le25$.

But the addition $q+k=C$ has an incoming carry $\sigma_t\in\{0,1\}$, and therefore


$$
q_t+k_t+\sigma_t=28+29\sigma_{t+1}.
\tag{7.8}
$$


The left side is at most $1+25+1=27$, a contradiction.

Thus $p\mid V(q)$ for every $q$ in the exact finite range.

It follows that $S_0,S_2$ are divisible by $p^2$ as integers. Every summand in the numerator of $D$ is also divisible by $p^2$, so its **whole** quotient by $p$ is zero modulo $p$. Equation (0.1) then gives $\kappa=0$. ∎

## 7.1 Interpretation in the two-state connection

At the corresponding digit of $(a,B,m)$, the triple is


$$
(a_i,B_i,m_i)=(1,3,28).
$$


In (6.1),


$$
d\le1,\qquad k\le25,
$$


whereas


$$
d+k=28+29f-e\ge27.
$$


Thus


$$
\boxed{\mathsf K_i=0.}
\tag{7.9}
$$



The word therefore annihilates every incoming state and every preceding carry row. It is not a cancellation restricted to one seed vector.

## 7.2 Multiple occurrences

At each distinct killing position, at least one of the two Kummer events—weight borrow or positive-binomial carry—must occur. Therefore $R$ disjoint occurrences imply


$$
\boxed{\min_{0\le q\le C}v_{29}(V(q))\ge R.}
\tag{7.10}
$$



This is a valuation theorem for the high weight $V(q)$. It does not, by itself, give a normalized rescaling law for the complete corrected column or its next force.

---

# 8. Original power-orbit consequences

The retained principal-unit parametrization gives a bijection


$$
u\bmod29^N\longmapsto C(u)\bmod29^N
\tag{8.1}
$$


for each $N$. I use this only for a property determined by an actual finite word whose annihilating effect has just been proved.

This is the crucial difference from the invalid transfer of the auxiliary value $26$: here the finite word is a sufficient condition for zero for **every** continuation.

## 8.1 An explicit original progression

The word at $h=0$ is the residue


$$
\omega=2\cdot29+5\cdot29^2+28\cdot29^3
=\boxed{687155}
\pmod{29^4},
\tag{8.2}
$$


with


$$
29^4=707281.
$$



There is a unique residue $u_*\bmod707281$ satisfying


$$
C(u_*)\equiv687155\pmod{707281}.
\tag{8.3}
$$


For every nonnegative original $u$ in that progression,


$$
\boxed{u\equiv u_*\pmod{707281}
\quad\Longrightarrow\quad
D=S_0=S_2=\kappa=0\pmod{29}.}
\tag{8.4}
$$



This is an original-compatible infinite-subfamily evaluation. It is a zero theorem, not a nonzero-subfamily theorem.

## 8.2 Density-one annihilation

Consider the disjoint four-digit blocks


$$
(C_{4j},C_{4j+1},C_{4j+2},C_{4j+3}),
\qquad j=0,\ldots,R-1.
$$


By (8.1), as $u$ runs modulo $29^{4R}$, these blocks are uniformly distributed. The proportion avoiding the word in every one of the $R$ positions is exactly


$$
\left(1-\frac1{29^4}\right)^R.
\tag{8.5}
$$



Every original index with nonzero $\kappa$ must avoid all these occurrences. Hence


$$
\overline{\operatorname{dens}}\{u:\kappa(C(u))\ne0\}
\le
\left(1-\frac1{29^4}\right)^R
$$


for every $R$. Letting $R\to\infty$ proves density zero.

The same argument works inside an arbitrary progression $u\equiv u_0\pmod h$: retain its forced lower $v_{29}(h)$ digits, place the disjoint blocks above them, and use the retained principal-unit bijection together with CRT.

### Theorem 8.1 — Original-orbit density theorem

For every $u_0\ge0$ and $h\ge1$,


$$
\boxed{
\operatorname{dens}_{\,u\equiv u_0\ (h)}
\{u:D(C(u))=S_0(C(u))=S_2(C(u))=\kappa(C(u))=0\}=1.
}
\tag{8.6}
$$



This strengthens “there are infinitely many zero indices in every progression” to a relative density-one statement for the actual row.

### What this theorem does not say

It does not prove:

- that every original index contains the killing word;
- that $\kappa$ vanishes at every original index avoiding the word;
- that the exceptional nonzero set is finite or empty;
- that primitive norm loss is unbounded;
- that a complete normalized high-layer rescaling exists.

A density-zero exceptional set can still be infinite and can still contain all indices relevant to a proposed nonzero-carry construction.

---

# 9. A new bounded exact calculation: instantiate the original progression

No accepted auxiliary calculation needs repeating.

The theorem already specifies $u_*$ uniquely. Its numerical representative can be obtained by a small modular calculation, without constructing an original-length power or scanning its digits.

Set


$$
M=29^{10}=420707233300201,
$$




$$
B_0=3^{249005515}\bmod M,\qquad
G=3^{574312172}\bmod M,
$$


using representatives in $[0,M)$, and define


$$
C_0=\frac{B_0-\beta}{29^6}\pmod{29^4},
\qquad
g=\frac{G-1}{29^6}\pmod{29^4}.
\tag{9.1}
$$


The retained principal-unit valuation makes $g$ a unit modulo $29$.

Since $29^{12}$ is already zero modulo $29^{10}$,


$$
G^u\equiv1+29^6gu\pmod{29^{10}},
$$


and therefore


$$
C(u)\equiv C_0+\beta gu\pmod{29^4}.
$$


Thus


$$
\boxed{
u_*=(687155-C_0)(\beta g)^{-1}\pmod{707281}.
}
\tag{9.2}
$$



## Inputs

- $29^{10}$, $\beta$, the two original exponents;
- the new word residue $687155$;
- ordinary modular exponentiation and one unit inverse.

## Expected verifiable output

The calculation should return:

1. $B_0,G,C_0,g,u_*$, with $0\le u_*<707281$;
2. checks
   

$$
B_0\equiv\beta\pmod{29^6},\qquad
   G\equiv1\pmod{29^6},\qquad g\not\equiv0\pmod{29};
$$


3. the exact congruence
   

$$
\boxed{
   B_0G^{u_*}\equiv
   \beta+29^6\cdot687155\pmod{29^{10}};
   }
   \tag{9.3}
$$


4. the theorem-backed output
   

$$
\boxed{\kappa(C(u_*+707281t))=0\pmod{29}\quad(t\ge0).}
$$



Fewer than $200$ modular multiplications, plus an extended-Euclidean inverse, suffice for the two exponentiations and a direct verification of (9.3).

**Status:** this numerical instantiation is an unevaluated bounded specification here. No numeric representative of $u_*$ is claimed. Its existence, uniqueness and annihilating property are proved independently of executing the specification.

---

# 10. Complete columns, forcing and normalization are unchanged

The new theorem is about the retained carry row. It does not delete any physical coordinate or force.

Retain


$$
P=\frac{Z_w}{p^2}=p^cx,\qquad Q=\frac{Y}{p^3},
\qquad
\nu=v_p(x^Tx),\qquad d=2c+4+\nu.
$$



The physical terminal coordinate remains


$$
\boxed{
\frac{Z_{w,b}}{p^3}
\equiv14pA_0\frac{W_b}{p^4}\pmod{p^2}.
}
\tag{10.1}
$$


Its absence from this particular norm precision is not its removal from the actual next column.

The complete second-force identity remains


$$
\boxed{
p^3U_a^TQ=
p^3(r_0G^{(3)}_{a0}+r_1G^{(3)}_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda'_{a,\ell}
+W_bU_{a,b}.
}
\tag{10.2}
$$


Both initial charges remain


$$
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(
T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}
\right),
\qquad i=0,1,
$$


and every source row remains


$$
\mathcal H_i=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b},
\qquad1\le i\le b-2.
$$



There is no source row at $b-1$, and the exterior at $b$ is not another recurrence step. Division by $p^3$ belongs to the whole right-hand side of (10.2).

The unresolved relative alignment is still


$$
\boxed{
x^TQ-p^c\rho_nx^Tx
\equiv0\pmod{p^{c+\nu+1}},
\qquad
N_{\log}\ge c+4+\nu.
}
\tag{10.3}
$$



No row contents, row metric or least actual two-column clearer have been replaced by the selected-prime statements proved here.

Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
\tag{10.4}
$$


The gcd is over all primes, and


$$
\boxed{
\log q_n=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{10.5}
$$


The primitive multiplier remains $d_B^2/g_B$.

For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the relevant whole same-index error remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{10.6}
$$



Neither the new killing-word theorem nor density-one annihilation controls this all-prime denominator/error comparison.

---

# 11. Precise remaining bottlenecks and follow-on lemmas

## 11.1 The remaining local exceptional-orbit problem

The outstanding carry question is now narrower:

> Evaluate the two-state contraction (5.3), (6.3)–(6.4) on original indices whose $C$-word avoids $(0,2,5,28)$, or prove an additional original-orbit annihilation theorem covering those indices.

The obstruction is explicit. The digit connection is small and integral, but the original exponentiation orbit does not presently come with a theorem forcing an annihilating word at **every** index. Uniform distribution over varying $u$ proves density one, not universal word occurrence.

A concrete follow-on lemma is:

### Exceptional-orbit annihilation lemma

Determine a finite collection of zero products of the explicit matrices (6.1), incorporating the affine digit relations


$$
a=69C+47,\qquad B=2a+1,\qquad m=\lfloor C/29\rfloor,
$$


and prove either:

1. every original $C(u)$ admits one of those zero products; or
2. the surviving products annihilate the specific initial carry row from (5.3); or
3. an explicitly specified infinite original subfamily has a nonzero final contraction.

A finite search for additional killing words would establish only those words. It would not prove that every original word contains one.

## 11.2 The normalized high-layer problem remains distinct

Repeated occurrences of the new word deepen the high weight $V$. The accepted repeated-block theorem deepens the complete first column. Neither statement supplies a relation between successive **primitive** columns after their actual contents are removed.

A normalized rescaling theorem would still have to retain:

- the actual next column, including the terminal coefficient $14$;
- the complete second-force source and return;
- the true content at each index;
- the primitive norm loss after that content is removed.

No such rescaling theorem is asserted here.

---

# 12. Proof-status ledger

| Statement | Status |
|---|---|
| Auxiliary residues $754,261,290\bmod841$ | Accepted finite independent execution |
| Auxiliary carries $26,9,10$ | Analytically proved and now finitely corroborated |
| Outside-support exclusion | Reused retained theorem, not attributed to the evaluator |
| Turn 8 actual low-interface row | Reused starting result |
| Whole-$D$ digit connection (4.8) | **Proved explicitly** |
| Exact retention of both cutoff branches | **Proved** |
| Reduction to ordinary mod-$29$ moments | **Proved** |
| Two-state terminal-preserving closure | **Proved with integral state lattice** |
| Singular rational pivot $r\equiv18$ | **Bypassed, not inverted** |
| Original-word-linear evaluation algorithm | **Proved partial computational result; not executed on an original word** |
| Killing word $(0,2,5,28)$ | **Proved for all incoming carries** |
| $D=S_0=S_2=\kappa=0$ under that word | **Proved** |
| Explicit original annihilating progression | **Proved; numerical representative not computed here** |
| Relative density-one original annihilation | **Proved in every original progression** |
| Universal annihilation on the entire original orbit | Open |
| Nonzero original carry, or nonzero infinite subfamily | Not established |
| Normalized high-layer rescaling | Open |
| Complete second-force relative alignment | Open |
| All-prime primitive denominator versus whole same-index error | Open |

---

## Conclusion

The new local connection eliminates the genuinely unequal-precision obstacle:


$$
\boxed{
D\bmod29
\text{ is expressed integrally through ordinary mod-}29
\text{ high moments, with both cutoff branches retained.}
}
$$



Its remaining mod-$29$ contraction has an explicit two-state closure. This bypasses the singular rational-moment pivot, but by itself remains original-word-linear work.

The new original-compatible theorem is stronger than that recurrence:


$$
\boxed{
(0,2,5,28)\text{ occurring in the base-}29\text{ word of }C
\Longrightarrow
D=S_0=S_2=\kappa=0.
}
$$


It yields an explicit infinite original progression and proves that the actual carry row vanishes on a set of relative natural density one in every original progression.

The exact remaining local bottleneck is the original exceptional set avoiding the annihilating word, together with the action of the surviving two-state products on the actual carry row. The only proposed bounded arithmetic here is the small modular calculation instantiating the proved original progression; no accepted computation is proposed for repetition.

The primitive norm, complete mixed-force alignment, final all-prime gcd and whole same-index error comparison remain unresolved. Accordingly,


$$
\boxed{
\text{No unconditional proof or disproof of the irrationality of }e+\pi
\text{ has been established.}
}
$$


