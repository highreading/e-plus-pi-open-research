> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — the actual depth-two norm vanishes on $t\equiv364\pmod{841}$

## Main conclusions

I reuse the independently closed 100 population cylinders, including


$$
t\equiv364\pmod{841}
\quad\Longrightarrow\quad
d=0,\qquad H\equiv20\pmod{29}.
$$


I do not rerun the population calculation, the universal low-polynomial calculation, or the recurrence currently under independent review. No tools were executed.

The requested actual norm digit can be evaluated on this preferred cylinder:



$$
\boxed{
t\equiv364\pmod{841}
\quad\Longrightarrow\quad
\frac{D}{29^2}\equiv0\pmod{29}.
}
\tag{A}
$$



This is an evaluation of the **whole original norm**, not just an auxiliary convolution. Its proof starts from the complete natural-multiplier representation of the actual $P$-column, includes the exterior low blocks and endpoint, and proves that the surviving high contraction is


$$
\boxed{
\frac{D}{29^2}
\equiv C_n^2 f(d)
\sum_{k=0}^{H}\left(\frac{X_k}{29}\right)^2
\pmod{29}
}
\tag{B}
$$


on all 100 accepted population cylinders. In particular, the unit multiplying the auxiliary sum is $5C_n^2$ when $d=0$.

On $d=0,\ H\equiv20\pmod{29}$, an exact one-carry calculation followed by a finite-boundary antisymmetry proves


$$
\sum_{k=0}^{H}\left(\frac{X_k}{29}\right)^2\equiv0\pmod{29}.
$$


The cancellation holds for **every higher part of the actual $H$**.

There are three further advances.

1. The first unresolved actual norm digit has the particularly simple complete reduction
   

$$
\boxed{
   \frac{D}{29^3}
   \equiv
   5C_n^2\,\frac{\mathcal T}{29^3}
   \pmod{29},
   \qquad
   \mathcal T=\sum_{k=0}^{H}X_k^2,
   }
   \tag{C}
$$


   on this preferred cylinder. The division on the right is proved legitimate below.

2. The accepted ordinary-polynomial defect identity, combined with whole-column content, yields an additional mixed-depth congruence:
   

$$
\boxed{
   M-(6C_n)^{-1}D\equiv0\pmod{29^4}
   }
   \tag{D}
$$


   on the preferred cylinder. Consequently, if the still-unresolved quantity
   $\mathcal T/29^3\bmod29$ is a unit at an actual index, then
   

$$
v_{29}(D)=v_{29}(M)=3.
$$


   No exact-depth-two conclusion is available there, because (A) rules it out.

3. There is a general obstruction to the requested type of norm-unit cylinder: **no finite congruence refinement of any of the 100 population cylinders can guarantee $D/29^2$ to be a unit for every original index in that refinement**. Every such refinement has a further, originally reachable refinement on which the entire $P$-column is divisible by $29^2$, and hence $29^4\mid D$. This does not exclude isolated or non-cylindrically described actual norm-depth-two indices elsewhere in the population.

The remaining finite arithmetic task is a small initialization table for an exact one-carry recurrence computing $\mathcal T/29^3\bmod29$. Its bounded inputs and required output are specified in Section 10. A finite table alone will not establish an original-family unit: the subsequent, growing digit string must still be controlled.

---

## 1. Domain and accepted inputs

Throughout,


$$
p=29,\qquad L=p^4=707281,
$$




$$
a=432827+682892t,\qquad t\ge0,\qquad b=3^a,\qquad n=2001b.
$$


The actual column indices remain


$$
0\le j\le b,
$$


and every contact inverse retains its finite indices


$$
0\le i,j<b.
$$



The metric is the falling metric


$$
\omega_j=j!\binom{n+2}{j}=(n+2)_{\underline j},
\qquad
\Omega=\operatorname{diag}(\omega_j^2).
$$


For the already weighted reconstructed columns,


$$
P=\frac{Z_w}{p^2},\qquad
Q=\frac{Y}{p^3},\qquad
Y=\frac{V_w}{b!},
$$


and


$$
D=P^TP,\qquad M=P^TQ.
$$



Write


$$
b=687936+Lh,\qquad h=pH+d,
$$




$$
N=2001h+1946=3+pA,\qquad
A=69h+67=2001H+69d+67.
$$


The high binomial factors are


$$
F(J)=\binom NJ\binom{2N+h-J}{h-J},
\qquad 0\le J\le h,
$$


and


$$
X_k=\binom Ak\binom{2A+H-k}{H-k},
\qquad 0\le k\le H.
$$


Set


$$
\mathcal T=\sum_{k=0}^{H}X_k^2.
$$



The accepted population closure supplies 100 original cylinders with


$$
a_0:=A\bmod p\in\{1,\ldots,14\},
\qquad
z:=H\bmod p\in\{p-a_0,\ldots,p-1\}.
\tag{1.1}
$$


On each,


$$
p\mid X_k\quad(0\le k\le H),
\qquad
p\mid F(J)\quad(0\le J\le h).
\tag{1.2}
$$


These statements include their finite endpoints and hold without conditions on higher digits.

The accepted leading natural low-polynomial identities are


$$
P_x(J)\equiv
\begin{cases}
C_n c(x)\ell_{e(x)}(J),&x\in\mathcal X,\\
0,&x\notin\mathcal X,
\end{cases}
\pmod p,
\tag{1.3}
$$


where


$$
\ell_0(J)=2N+h-J+1,\qquad
\ell_1(J)=N-J,
$$


and


$$
\sum_{\substack{x\in\mathcal X\\e(x)=0}}c(x)^2=11,
\qquad
\sum_{\substack{x\in\mathcal X\\e(x)=1}}c(x)^2=18
\quad\text{in }\mathbb F_p.
\tag{1.4}
$$


Here $C_n$ is a unit on the original domain.

I also reuse the accepted ordinary-polynomial defect identity


$$
R(J)=(27C_n+20J_{29})K_d(J),
\tag{1.5}
$$


where


$$
K_d(J)=11(d+7-J)^2+18(3-J)^2
      =11(d+4)(d+10-2J)
      \quad\text{in }\mathbb F_p[J].
\tag{1.6}
$$


No extension of a pending shifted-class coefficient table is needed.

---

## 2. Division of the actual column: no additional force survives

### 2.1 The complete representation used

The retained precision-three construction gives natural ordinary polynomials


$$
P_x(J),Q_x(J)\in(\mathbb Z/p^3\mathbb Z)[J]
$$


such that, at every actual coordinate $j=LJ+x$,


$$
P_{LJ+x}\equiv(-1)^{j+1}F(J)P_x(J)\pmod{p^3},
\tag{2.1}
$$




$$
Q_{LJ+x}\equiv(-1)^{j+1}F(J)Q_x(J)\pmod{p^3}.
\tag{2.2}
$$



This is the complete actual construction, with raw precision


$$
Z_w\bmod p^5,\qquad Y\bmod p^6.
$$


In particular, it retains:

- the safe positive reconstruction support before graded reduction;
- the complete factorial boundary first through $r=117$, reduced through $r=88$ only after the compulsory reconstruction carry;
- negative Laurent powers through $-89$ at the effective precision;
- the unfrozen unit-boundary insertion
  

$$
\delta Y_{LJ+x}
  \equiv(-1)^{j+1}LJ\,W_jB_{-2}(j)\pmod{p^6};
$$


- the complete logarithmic force, omitted only through its whole-force valuation bound;
- the endpoint formulas
  

$$
Z_{w,b}=W_b\,b\theta^P_{b-1},\qquad
  Y_b=W_b(1+b\theta^Q_{b-1}).
$$



Thus the argument below does not replace the original forcing by its leading positive kernel.

### 2.2 Exact normalization

On the accepted population, write


$$
F(J)=pG(J),\qquad G(J)\in\mathbb Z.
$$


Equation (2.1) means


$$
P_{LJ+x}=(-1)^{j+1}pG(J)P_x(J)+p^3E_{J,x}
$$


for an integral $p$-adic error. Hence


$$
\boxed{
\frac{P_{LJ+x}}p
\equiv(-1)^{j+1}G(J)P_x(J)\pmod{p^2}.
}
\tag{2.3}
$$


In particular,


$$
\boxed{
\frac{P_{LJ+x}}p
\equiv(-1)^{j+1}\frac{F(J)}p\,P_x(J)\pmod p.
}
\tag{2.4}
$$



There is no division of a congruence by a possibly nonunit value of $F(J)$. Only the known factor $p$ is divided, and the modulus decreases accordingly.

All ordinary low-polynomial corrections remain in $P_x$. At the first normalized norm digit only their reductions (1.3) survive. No additional contact, overflow, or endpoint forcing term appears after this division.

### 2.3 Finite boundaries

The actual ranges are


$$
0\le J\le h\quad(0\le x\le687936),
$$




$$
0\le J\le h-1\quad(687936<x<L).
\tag{2.5}
$$


For $x>687936$, the natural $P_x(J)$ contains $h-J$. Extension of its contraction to $J=h$ therefore adds zero, including after division by $p$.

Moreover, $P_x\bmod p=0$ outside $\mathcal X$. Thus


$$
P_{LJ+x}\in p^2\mathbb Z_p
\qquad(x\notin\mathcal X)
\tag{2.6}
$$


on the populated locus.

The actual endpoint $j=b$ has low part $x=687936$, outside the old leading $P$-support. Its normalized norm contribution consequently vanishes not only modulo $p$, but modulo $p^2$:


$$
\left(\frac{P_b}{p}\right)^2\equiv0\pmod{p^2}.
\tag{2.7}
$$


This is an evaluated contribution of the retained endpoint, not its deletion.

### 2.4 Complete weighted norm

Squaring (2.4), summing the actual coordinates, and using (1.3)–(1.4) gives


$$
\boxed{
\frac D{p^2}
\equiv
C_n^2\sum_{J=0}^{h}
K_d(J)\left(\frac{F(J)}p\right)^2
\pmod p.
}
\tag{2.8}
$$



The factor $K_d$, both low support masses $11,18$, and the unit $C_n^2$ are all present. This is the complete original norm at the requested digit.

---

## 3. Fifth-digit evaluation on all 100 population cylinders

The next step is to determine precisely which $F(J)/p$ can survive.

Write


$$
J=pk+s,\qquad0\le s<p.
$$


The exact ranges are


$$
0\le k\le H\quad(s\le d),\qquad
0\le k\le H-1\quad(s>d).
\tag{3.1}
$$



Call $s$ admissible when


$$
0\le s\le3,\qquad0\le d-s\le22.
\tag{3.2}
$$



### Lemma 1 — all nonadmissible fifth digits vanish after division

On every accepted population cylinder,


$$
\frac{F(pk+s)}p\equiv0\pmod p
$$


for every nonadmissible $s$ in its actual finite range.

For admissible $s$,


$$
\boxed{
\frac{F(pk+s)}p
\equiv
\binom3s\binom{d-s+6}{6}\frac{X_k}{p}
\pmod p.
}
\tag{3.3}
$$



#### Proof

For admissible $s$, neither binomial has a first-digit carry. First-level factorial stripping gives a unit multiple of $X_k$; its leading unit is exactly the coefficient in (3.3). Because $p\mid X_k$, division gives the stated congruence.

For nonadmissible digits, first-level stripping has the following high-factor forms. Every unspecified multiplier in this list is a $p$-adic unit coming from factorials with indices below $p$.

| Fifth-digit case | High factor after removing its single low factor $p$ |
|---|---|
| $s\le d,\ s\le3,\ d-s\ge23$ | $(2A+H-k+1)X_k$ |
| $s\le d,\ s\ge4$ | $(A-k)X_k$ |
| $s>d,\ s\le3$ | $(H-k)X_k$ |
| $s>d,\ 4\le s\le d+6$ | At least two low carries |
| $s>d+6$ | $(A-k)\binom Ak\binom{2A+H-k-1}{H-k-1}$ |

The first three rows vanish because $p\mid X_k$. The fourth already vanishes after division by one $p$.

For the last row, let $r=k\bmod p$, and use the population parameters $a_0,z$ from (1.1).

- If $r>a_0$, then $p\mid\binom Ak$.
- If $r=a_0$, then $p\mid A-k$.
- If $r<a_0$, then $r\le a_0-1<z$, so $H-k-1$ has low digit $z-1-r$. Adding it to the low digit $2a_0$ of $2A$ gives
  

$$
2a_0+z-1-r\ge a_0+z\ge p.
$$


  Therefore the second binomial is divisible by $p$.

The last row also vanishes. Every shorter range in (3.1) has been handled before any extension. ∎

Substituting into (2.8), the complete fifth-digit coefficient is


$$
\sum_{\rm adm.\ s}
\binom3s^2\binom{d-s+6}{6}^2K_d(s)=f(d).
$$


Hence:

### Theorem 2 — complete normalized norm transfer on the population

On all 100 accepted original cylinders,


$$
\boxed{
\frac D{p^2}
\equiv
C_n^2 f(d)\,
S
\pmod p,
\qquad
S:=\sum_{k=0}^{H}\left(\frac{X_k}{p}\right)^2.
}
\tag{3.4}
$$



The factor $C_n^2f(d)$ is a unit. Equation (3.4), rather than the auxiliary sum by itself, is the actual norm evaluation.

---

## 4. Exact one-carry calculation for $d=0,\ H\equiv20\pmod{29}$

Now restrict to the original cylinder


$$
t\equiv364\pmod{841}.
$$


Write


$$
H=20+pG.
$$


Since $A=2001H+67$,


$$
A=9+pB,\qquad
B=2001G+1382,\qquad B\equiv19\pmod p.
\tag{4.1}
$$


Define


$$
Y_m=\binom Bm\binom{2B+G-m}{G-m},
\qquad0\le m\le G.
\tag{4.2}
$$



### 4.1 All exact one-carry paths

Write


$$
k=pm+s,\qquad0\le s<p.
$$



- For $0\le s\le9$, the first binomial has no low carry, and the second has exactly one.
- For $10\le s\le20$, the first binomial has exactly one low carry, and the second has none.
- For $21\le s\le28$, both have a low carry. These terms vanish after division by $p$.

For the two contributing ranges, the actual remaining range is exactly $0\le m\le G$. The shorter range $m\le G-1$ occurs only in the last, vanishing group.

Put


$$
u_s=-\frac{9!}{18!\,s!\,(20-s)!}\in\mathbb F_p,
\qquad0\le s\le20.
\tag{4.3}
$$


The minus sign is the leading $28!$ factor belonging to the one carry. First-level factorial stripping gives


$$
\boxed{
\frac{X_{pm+s}}p\equiv
\begin{cases}
u_s(2B+G-m+1)Y_m,&0\le s\le9,\\[2mm]
u_s(B-m)Y_m,&10\le s\le20,\\[2mm]
0,&21\le s\le28,
\end{cases}
\pmod p.
}
\tag{4.4}
$$


Additional higher carries are not suppressed: they make the displayed high factors vanish modulo $p$.

### 4.2 Evaluation of both low coefficient sums

Let


$$
A_*=\sum_{s=0}^{9}u_s^2,\qquad
B_*=\sum_{s=10}^{20}u_s^2.
$$


Because $u_s$ is a fixed unit times $\binom{20}{s}$, Vandermonde gives


$$
\sum_{s=0}^{20}u_s^2
=
\left(\frac{9!}{18!\,20!}\right)^2
\binom{40}{20}
\equiv0\pmod p.
\tag{4.5}
$$


Here Lucas gives $\binom{40}{20}\equiv0$.

Also $u_s=u_{20-s}$, and


$$
u_{10}
=-\frac{9!}{18!\,10!^2}
=\frac1{10}
=3\pmod{29},
\tag{4.6}
$$


using $18!\,10!\equiv-1\pmod{29}$. Thus


$$
2A_*+9=0,\qquad A_*+B_*=0,
$$


so


$$
\boxed{A_*=10,\qquad B_*=19=-10\pmod{29}.}
\tag{4.7}
$$



Consequently,


$$
\begin{aligned}
S
&\equiv10\sum_{m=0}^{G}
\left[(2B+G-m+1)^2-(B-m)^2\right]Y_m^2\\
&=10(B+G+1)
\sum_{m=0}^{G}(3B+G+1-2m)Y_m^2
\pmod p.
\end{aligned}
\tag{4.8}
$$



Since $B\equiv19$ and $3\cdot19+1\equiv0\pmod{29}$,


$$
\boxed{
S\equiv10(G+20)
\sum_{m=0}^{G}(G-2m)Y_m^2\pmod p.
}
\tag{4.9}
$$



The remaining weighted sum must be evaluated with its whole finite boundary; it cannot be replaced by a freely chosen higher parameter.

---

## 5. The higher weighted sum vanishes for every continuation

### Lemma 3 — finite-boundary antisymmetry

If $B\equiv19\pmod{29}$, then for every nonnegative $G$,


$$
\boxed{
\sum_{m=0}^{G}(G-2m)
\binom Bm^2
\binom{2B+G-m}{G-m}^2
\equiv0\pmod{29}.
}
\tag{5.1}
$$



#### Proof

Write


$$
B=19+pC,\qquad G=pR+z,\qquad m=pq+s.
$$


Let


$$
\varepsilon=\mathbf1_{s>z},\qquad
l=z-s+p\varepsilon.
$$


Thus $l$ is the low digit of $G-m$, and


$$
s+l=z+p\varepsilon.
\tag{5.2}
$$



A nonzero $Y_m\bmod p$ requires


$$
0\le s\le19,\qquad0\le l\le19.
\tag{5.3}
$$


Indeed $2B=9+p(2C+1)$, and


$$
\binom{9+l}{l}\equiv(-1)^l\binom{19}{l}\pmod p.
$$


On the nonzero support,


$$
Y_m^2\equiv
\binom{19}{s}^2\binom{19}{l}^2
\left[
\binom Cq
\binom{2C+1+R-q-\varepsilon}{R-q-\varepsilon}
\right]^2
\pmod p.
\tag{5.4}
$$



For fixed $\varepsilon$, the high factor is independent of $s,l$. Its actual range is


$$
0\le q\le R\quad(\varepsilon=0),\qquad
0\le q\le R-1\quad(\varepsilon=1).
\tag{5.5}
$$


Meanwhile


$$
G-2m\equiv z-2s\equiv l-s\pmod p.
$$


For each fixed $\varepsilon$, the involution


$$
(s,l)\longleftrightarrow(l,s)
$$


preserves (5.2), (5.3), and the same high range (5.5). Its squared-binomial weight is symmetric, whereas $l-s$ changes sign. Fixed points contribute zero.

Each of the two finite low sums therefore vanishes separately. This proves (5.1), without any condition on the higher digits. ∎

Combining (4.9) and Lemma 3 gives


$$
\boxed{S\equiv0\pmod p.}
\tag{5.6}
$$


Because $f(0)=5$, Theorem 2 now proves the requested actual result:


$$
\boxed{
\frac D{p^2}\equiv5C_n^2S=0\pmod p.
}
\tag{5.7}
$$



In integer terms,


$$
\boxed{\mathcal T\in p^3\mathbb Z.}
\tag{5.8}
$$



This is cancellation of a normalized norm, not a claim that every $X_k$ has acquired another factor $p$.

### A weighted cancellation needed for the next digit

Define


$$
V=\sum_{k=0}^{H}k\left(\frac{X_k}{p}\right)^2\pmod p.
$$


Let


$$
A_1=\sum_{s=0}^{9}s\,u_s^2,\qquad
B_1=\sum_{s=10}^{20}s\,u_s^2.
$$


The symmetry $u_s^2=u_{20-s}^2$ and (4.5) give


$$
A_1+B_1
=\frac{20}{2}\sum_{s=0}^{20}u_s^2=0.
$$


Thus the same calculation as (4.8), with $10$ replaced by $A_1$, reduces $V$ to the weighted sum in Lemma 3. Therefore


$$
\boxed{V=0\pmod p.}
\tag{5.9}
$$



---

## 6. The first unresolved actual norm digit

The full precision-three representation is sufficient to determine $D/p^2\bmod p^2$, because $P\in p\mathbb Z_p^{b+1}$.

Choose the integer polynomial lift


$$
\widetilde K(J)=11\ell_0(J)^2+18\ell_1(J)^2.
$$


Coefficientwise leading cancellation gives an ordinary polynomial $V_P(J)$ such that


$$
\sum_xP_x(J)^2
=
C_n^2\widetilde K(J)+pV_P(J)\pmod{p^2}.
\tag{6.1}
$$


This $V_P$ includes all ordinary low-polynomial corrections from the actual $P$-construction. It is not assumed to vanish.

Using (2.3),


$$
\frac D{p^2}
\equiv
\sum_{J=0}^{h}
\left(\frac{F(J)}p\right)^2
\left[C_n^2\widetilde K(J)+pV_P(J)\right]
\pmod{p^2}.
\tag{6.2}
$$



On the preferred cylinder, Lemma 1 makes every $s\ne0$ contribution zero modulo $p^2$, since $F(pk+s)/p$ is then divisible by $p$.

Put


$$
Z_k=X_k/p.
$$


At $J=pk$, first-level unit expansion gives


$$
\frac{F(pk)}p
\equiv
Z_k\left[1+p\bigl(H\mathsf H_6+
k(\mathsf H_3-\mathsf H_6)\bigr)\right]
\pmod{p^2},
\tag{6.3}
$$


where $\mathsf H_r=\sum_{i=1}^r i^{-1}$.

For $p=29$,


$$
\mathsf H_6=1,\qquad
\mathsf H_3-\mathsf H_6=25.
\tag{6.4}
$$


Moreover,


$$
\widetilde K(pk)\equiv5+p(4-k)\pmod{p^2},
\tag{6.5}
$$


because $A\equiv9,\ H\equiv20$.

Combining (6.3)–(6.5),


$$
\widetilde K(pk)\left(\frac{F(pk)}p\right)^2
\equiv
Z_k^2\,[5+p(1+17k)]
\pmod{p^2}.
\tag{6.6}
$$


The full low correction contributes


$$
pV_P(0)\sum_{k=0}^{H}Z_k^2=pV_P(0)S\equiv0\pmod{p^2},
$$


by (5.6). Thus it has been evaluated as a whole contraction, not omitted termwise.

Equations (5.6), (5.9), and (6.6) yield


$$
\frac D{p^2}\equiv5C_n^2S\pmod{p^2}.
$$


Equivalently:

### Theorem 4 — whole next-digit norm transfer

On $t\equiv364\pmod{841}$,


$$
\boxed{
D\equiv5C_n^2\mathcal T\pmod{p^4},
\qquad
D,\mathcal T\in p^3\mathbb Z_p.
}
\tag{6.7}
$$


Hence


$$
\boxed{
\frac D{p^3}\equiv
5C_n^2\frac{\mathcal T}{p^3}\pmod p.
}
\tag{6.8}
$$



The immediate unresolved norm quantity is now exactly


$$
\boxed{\mathcal T/p^3\bmod29,}
$$


not an omitted low-polynomial coefficient or endpoint term.

---

## 7. A further mixed congruence from whole-column content

The accepted coefficient identity (1.5) gives, for


$$
r=(6C_n)^{-1},
$$




$$
\sum_x(P_xQ_x-rP_x^2)
\equiv p(27C_n+20J_{29})K_d(J)\pmod{p^2}.
\tag{7.1}
$$



On the population $F\in p\mathbb Z$ and $P,Q\in p\mathbb Z_p^{b+1}$. Therefore errors modulo $p^3$ in either actual column affect their scalar products only modulo $p^4$. Multiplying (7.1) by $F(J)^2$ and retaining the proved finite boundaries gives


$$
M-rD
\equiv
p(27C_n+20J_{29})
\sum_{J=0}^{h}F(J)^2K_d(J)
\pmod{p^4}.
$$


Consequently,


$$
\boxed{
M\equiv(r+p\lambda)D\pmod{p^4},
\qquad
\lambda=\frac{27C_n+20J_{29}}{C_n^2}\pmod p,
}
\tag{7.2}
$$


on all 100 population cylinders.

On the preferred cylinder $p^3\mid D$, so


$$
\boxed{M-rD\equiv0\pmod{p^4}.}
\tag{7.3}
$$



This is an explicit additional derivation using whole-column content; it is not an unsupported extension of the third-defect theorem.

Thus:

- if $\mathcal T/p^3$ is a unit at an actual preferred-cylinder index, then
  

$$
v_p(D)=v_p(M)=3;
$$


- if $\mathcal T/p^3=0\bmod p$, then both valuations are at least $4$.

No all-depth relative-valuation conclusion follows.

---

## 8. Why a finite norm-unit cylinder cannot be supplied on this population

The LTE bijection does not permit selection of the whole growing $H$. It does, however, permit every prescribed **finite extension** of its low digits. That fact proves a useful obstruction.

### Theorem 5 — every finite population cylinder has a deeper-content refinement

Fix any one of the 100 accepted population cylinders and any finite congruence refinement of its original $t$-parameter. There is a further original congruence refinement on which


$$
p^2\mid X_k\quad(0\le k\le H),
$$


and consequently


$$
P,Q\in p^2\mathbb Z_p^{b+1},
\qquad
D,M\in p^4\mathbb Z_p.
\tag{8.1}
$$



#### Proof

Suppose the existing refinement fixes $H\bmod p^m$. Write


$$
A=a_0+p(69H+c),\qquad
c=\frac{69d+67-a_0}{p}.
$$


In the multiplication $69H+c$, the digit of $A$ at position $m+1$ has the form


$$
A_{m+1}\equiv69H_m+u_m\pmod p,
$$


where $u_m$ is determined by the already fixed lower digits.

Since $69\equiv11\pmod p$ is a unit, choose the still-free digit $H_m$ so that


$$
A_{m+1}=2.
$$


Then choose


$$
H_{m+1}=28.
\tag{8.2}
$$



At this digit, the corresponding digit of $2A$ is $4$ or $5$, according to its incoming doubling carry.

For any actual $k$, put $l=H-k$. Let $\sigma\in\{0,1\}$ be the incoming carry in $k+l=H$. If neither binomial defining $X_k$ had an outgoing carry at this digit, then:

- no outgoing borrow in $A-k$ would require $k_{m+1}\le2$;
- no outgoing carry in $2A+l$ would require $l_{m+1}\le24$.

Thus


$$
k_{m+1}+l_{m+1}+\sigma\le27,
$$


contradicting $H_{m+1}=28$.

Therefore every $X_k$ has at least one binomial carry at this new digit. The accepted population obstruction already forces one at digit zero. These are distinct digit positions, so $p^2\mid X_k$.

Lemma 1 now gives $p^2\mid F(J)$ for every actual $J$: its admissible quotients are multiples of $X_k/p$, and its nonadmissible quotients already vanish on the whole population.

The natural representations modulo $p^3$ imply $P,Q\in p^2\mathbb Z_p^{b+1}$.

Finally, the accepted LTE bijection maps this finite extension of $h=d+pH$ to a nonempty original congruence class of $t$. It contains infinitely many nonnegative $t$. No whole integer $H$ has been independently prescribed. ∎

### Consequence

There is no finite congruence subcylinder, contained in the accepted population, on which a proof can validly assert


$$
D/p^2\in\mathbb Z_p^\times
$$


for **every** original index in the subcylinder. Each such subcylinder contains the refinement (8.1).

This theorem does not prove that norm-depth-two indices never occur elsewhere among the 100 cylinders. It proves that their existence cannot be certified by a finite low-digit cylinder whose uncontrolled higher continuations are simply ignored.

For the preferred cylinder the stronger conclusion (A) already holds: no depth-two index occurs there at all.

---

## 9. Exact one-carry recurrence for the remaining norm digit

The next quantity is


$$
S=\sum_{k=0}^{H}(X_k/p)^2\pmod{p^2},
\qquad
\mathcal T/p^3=S/p\pmod p.
$$


Terms with $v_p(X_k)\ge2$ contribute zero to $S\bmod p^2$. Thus the recurrence must retain **exactly one carry in total**, not merely carry-free paths.

Here is a direct factorial-unit formulation, separate from the previously submitted carry-free mod-$841$ recurrence.

### 9.1 Digit states

Let $l=H-k$, $r=A-k$, and $s=2A+l$. At digit $i$, use:

- $\sigma_i$: incoming carry in $k+l=H$;
- $\beta_i$: incoming borrow in $A-k$;
- $\gamma_i$: incoming carry in $2A+l$;
- $v_i\in\{0,1\}$: accumulated binomial carry count.

Given the digits $a_i,\eta_i,c_i$ of $A,H,2A$, choose $k_i$, determine $l_i$ by


$$
k_i+l_i+\sigma_i=\eta_i+p\sigma_{i+1},
$$


and set


$$
r_i=a_i-k_i-\beta_i+p\beta_{i+1},
$$




$$
s_i=c_i+l_i+\gamma_i-p\gamma_{i+1}.
$$


Update


$$
v_{i+1}=v_i+\beta_{i+1}+\gamma_{i+1},
$$


discarding $v_{i+1}>1$.

Accept only the true terminal conditions


$$
\sigma=\beta=\gamma=0,\qquad v=1.
$$


These enforce the original finite summation boundary.

### 9.2 Full factorial units modulo $841$

Put


$$
\mathcal W=28!\pmod{p^2}.
$$


For a local tuple $\tau_i=(a_i,s_i,k_i,r_i,c_i,l_i)$, define


$$
g_i=
\mathcal W^{\,2(\beta_{i+1}+\gamma_{i+1})}
\left(
\frac{a_i!\,s_i!}{k_i!\,r_i!\,c_i!\,l_i!}
\right)^2
\pmod{p^2}.
\tag{9.1}
$$


All displayed factorials are units.

The adjacent-digit correction is


$$
\begin{aligned}
E_i={}&
a_{i+1}\mathsf H_{a_i}
+s_{i+1}\mathsf H_{s_i}
-k_{i+1}\mathsf H_{k_i}
-r_{i+1}\mathsf H_{r_i}\\
&-c_{i+1}\mathsf H_{c_i}
-l_{i+1}\mathsf H_{l_i}.
\end{aligned}
\tag{9.2}
$$


Exact factorial stripping gives, on an accepted one-carry path,


$$
\boxed{
(X_k/p)^2
\equiv
\prod_i g_i\,
\left(1+2p\sum_iE_i\right)
\pmod{p^2}.
}
\tag{9.3}
$$



In particular, $\mathcal W$ is retained modulo $841$, not replaced by $-1$ at this precision.

Equation (9.3) follows from


$$
U_p(pm+r)\equiv(28!)^m r!(1+pm\mathsf H_r)\pmod{p^2}.
$$


The exponent of $28!$ in each factorial ratio is exactly the carry crossing that level. This proves both the valuation selection and the unit weight.

### 9.3 Bounded accumulation

For each carry state store:

- $W\in\mathbb Z/p^2\mathbb Z$;
- six residues $Z\in\mathbb F_p^6$, containing the weighted previous vector
  

$$
(\mathsf H_a,\mathsf H_s,-\mathsf H_k,
   -\mathsf H_r,-\mathsf H_c,-\mathsf H_l).
$$



For current tuple $\tau=(a,s,k,r,c,l)$,


$$
W_{\rm new}\;{+}{=}\;
g\,[W+2p\,\tau\cdot Z]\pmod{p^2},
\tag{9.4}
$$




$$
Z_{\rm new}\;{+}{=}\;
(g\bmod p)(W\bmod p)
(\mathsf H_a,\mathsf H_s,-\mathsf H_k,
-\mathsf H_r,-\mathsf H_c,-\mathsf H_l).
\tag{9.5}
$$


Appending sufficient zero digits drains the actual affine, doubling, summation, and binomial carries and closes the last harmonic term.

The terminal $W$ is exactly $S\bmod p^2$. This recurrence includes all and only exact one-carry paths; it is not a numerical sampling assertion.

---

## 10. A small bounded initialization calculation

A full evaluation at an original $H$ would still process its actual growing digit string. The immediate useful finite calculation is much smaller: compute the first two digit layers of (9.4)–(9.5) symbolically with respect to $G\bmod29$.

### Inputs

For each $z=0,\ldots,28$, use the two low digits


$$
(H_0,H_1)=(20,z),
$$




$$
(A_0,A_1)=(9,19),
$$




$$
((2A)_0,(2A)_1)=(18,9).
$$


Initialize all carries to zero and retain total carry exactly one.

Use:

- $0!,\ldots,28!\bmod841$;
- $\mathsf H_0,\ldots,\mathsf H_{28}\bmod29$;
- $28!\bmod841$, at full precision;
- equations (9.1), (9.4), and (9.5).

After two digits, surviving paths have


$$
\beta=\gamma=0,\qquad v=1,
$$


and only $\sigma=0,1$ remains as a branching carry state.

There are at most


$$
29\cdot21\cdot29=17661
$$


candidate pairs of summation digits.

### Proved divisibility check

For each fixed $z$ and each $\sigma$, the resulting $W_\sigma(z)$ is divisible by $29$.

Indeed, the proof of Lemma 3 cancels the two low-digit norm coefficients separately for each carry $\sigma$, before contraction with any higher binomial factor. Thus this is a coefficientwise boundary-state assertion, not merely a cancellation after an unspecified continuation.

### Expected verifiable output

Return, for every $z$ and $\sigma$,



$$
r_\sigma(z)=W_\sigma(z)/29\bmod29
$$


and the six harmonic-state residues


$$
Z_\sigma(z)\in\mathbb F_{29}^6,
$$


together with the exact-division checks on $W_\sigma(z)$.

This is


$$
29\cdot2\cdot7=406
$$


returned field elements, plus the divisibility receipts.

At the third digit, $W\bmod29=0$, so (9.5) makes all newly propagated harmonic-state residues zero. The normalized weight then becomes


$$
g\,[r_\sigma(z)+2\,\tau\cdot Z_\sigma(z)]\pmod{29},
$$


and all later digits use an ordinary carry-free squared-binomial transfer modulo $29$.

Thus the proposed table produces a concrete, small initialization for the **exact remaining actual norm digit**.

It is not expected or required in advance that the table vanish. A nonzero entry would not itself establish an original norm unit. The subsequent tail contraction, including its terminal carry condition, must still be evaluated or controlled for actual powers $3^a$.

---

## 11. Primitive denominator and whole evaluated error

Retain the actual least two-column denominator


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0.
$$


With the actual falling metric,


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


and the **full final gcd**


$$
g_B=\gcd(A_B,|H_B|).
$$


The primitive pair is


$$
p_n=H_B/g_B,\qquad q_n=A_B/g_B>0.
$$


The primitive multiplier is $1/g_B$ on the integer Gram pair, or $d_B^2/g_B$ on the corresponding rational Gram pair. The actual denominator is $q_n$, not a row-clearer or a local $29$-adic denominator.

Put


$$
F_n=v_{29}(n!),\qquad F_b=v_{29}(b!),
\qquad
\delta=v_{29}(D),\qquad\mu=v_{29}(M).
$$


The exact interface remains


$$
\boxed{
v_{29}(g_B)
=
\min\{4F_n+4+\delta,\ 2F_n+F_b+5+\mu\},
}
$$




$$
\boxed{
v_{29}(q_n)
=
\max\{0,\ 2F_n-F_b-1+\delta-\mu\}.
}
\tag{11.1}
$$



On the preferred cylinder, the new result gives $\delta,\mu\ge3$. If the next norm digit is a unit, the additional mixed congruence gives $\delta=\mu=3$, and then


$$
v_{29}(q_n)=\max\{0,\ 2F_n-F_b-1\}.
$$


If that digit vanishes, deeper relative valuations remain unresolved.

Norm nonvanishing follows from positivity. Mixed nonvanishing retains its supplied original-family dependency; a vanishing residue is not a proof that the integer mixed product vanishes.

For the complete real error


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the whole evaluated form remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{11.2}
$$


At the retained scope and proof status of the supplied signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$


The complete exponential residual, logarithmic force, factorial/contact boundary, and endpoint remain part of this error.

No all-prime bound for $q_n$ has been obtained here. In particular, the present congruences do not prove that the complete nonzero form (11.2) tends to zero.

---

# Concluding proof-status ledger

## New proved results

Using the accepted complete reconstruction and finite low-polynomial inputs:

1. Division of the actual column is legitimate:
   

$$
P_{LJ+x}/29
   \equiv(-1)^{j+1}(F(J)/29)P_x(J)\pmod{29},
$$


   with the stronger modulus-$841$ version needed for the next digit.

2. The complete norm on all 100 population cylinders is
   

$$
D/29^2
   \equiv C_n^2f(d)\sum_{k=0}^{H}(X_k/29)^2\pmod{29}.
$$


   Every nonadmissible fifth-digit contribution is evaluated as zero.

3. On the original cylinder $t\equiv364\pmod{841}$,
   

$$
\boxed{D/29^2=0\pmod{29}.}
$$


   The proof controls every higher digit through exact finite-boundary antisymmetry.

4. On that same cylinder,
   

$$
\boxed{
   D\equiv5C_n^2\mathcal T\pmod{29^4},
   \qquad
   M-(6C_n)^{-1}D\equiv0\pmod{29^4}.
   }
$$


   Thus the first unresolved actual norm digit is a proved unit multiple of $\mathcal T/29^3\bmod29$.

5. Every finite congruence refinement within the accepted population has a further original refinement with $29^4\mid D,M$. Therefore a universal norm-depth-two conclusion cannot be certified by a finite low-digit cylinder there.

## Exact remaining bottleneck

The immediate arithmetic question is


$$
\boxed{
\mathcal T/29^3\bmod29
\quad\text{for the actual }H
\text{ on }t\equiv364\pmod{841}.
}
$$


Its low initialization is bounded, but its higher tail is still the actual growing digit string. The LTE bijection alone cannot select or certify that entire tail.

Beyond this local question, all-depth relative valuation control and control of the **full primitive denominator across all primes** remain necessary for the irrationality objective.

## Bounded calculation requested

Compute the 406 initialization residues in Section 10, with exact division receipts and the complete one-carry factorial units modulo $841$. This is at most 17,661 candidate two-digit paths. It does not rerun population or universal-$\Gamma$ calculations.

That calculation would complete a finite coefficient evaluation for the next actual norm digit. It would not, by itself, prove an original-family unit or an irrationality theorem.

**The irrationality or rationality of $e+\pi$ remains unresolved.**
