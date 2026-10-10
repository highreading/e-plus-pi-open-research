> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 5 — The complete $29^{-3}$ first-force column, its vanishing leading norm, and an obstruction to $c=1$

## Executive assessment

The stronger fixed-prefix certificate changes the conclusion of Turn 4 decisively:



$$
\boxed{L_{\mathrm I}=L_{\mathrm{II}}=0}
$$



at the former $29^{-2}$ normalization. Consequently, Turn 4’s alternative $c=\nu=0$, $d=4$ cannot occur. This is a pointwise column zero on every compatible high word, not merely a zero auxiliary Gram matrix.

At the next normalization, I obtain a complete formula for the **actual first force**. Write


$$
A_0=f_0^0\bmod29\ne0.
$$


Then, with the original cutoff and terminal row retained,


$$
\boxed{
\frac{Z_{w,j}}{29^3}
\equiv
A_0(-1)^{j+1}
\frac{\displaystyle
 \binom{n+2}{j}
 \binom{2n+b-1-j}{b-1-j}}
 {29^3}
\pmod{29},
\qquad 0\le j<b,
}
\tag{E.1}
$$


and


$$
\boxed{\frac{Z_{w,b}}{29^3}\equiv0\pmod{29}.}
\tag{E.2}
$$



The quotient in (E.1) is integral. Establishing this formula requires retaining the first-force head modulo $841$, the compatible $p\mathsf D_1$ terms, and the first finite endpoint return. They cannot be omitted merely because the preceding normalized column vanished. Below I prove, separately, the additional weighted divisibility that makes their contribution zero **at this particular next level**.

There are two further consequences.

1. **The meaningful leading norm also vanishes, now by an evaluated identity.**  
   The actual-line Gram quotient at the $29^{-3}$ level is
   

$$
\boxed{
   \left(\frac{Z_w}{29^3}\right)^T
   \left(\frac{Z_w}{29^3}\right)
   \equiv
   11A_0^2\bigl(\mathscr T_{\mathrm I}-\mathscr T_{\mathrm{II}}\bigr)
   =0\pmod{29}.
   }
   \tag{E.3}
$$


   Here the two high sums are exactly the original finite sums, not completed blocks. Their equality follows from a one-digit symmetry proved below.

2. **A uniform assertion $c=1$ is false.**  
   If
   

$$
\boxed{C\equiv814=(2,28)_{29}\pmod{841},}
   \tag{E.4}
$$


   the entire column in (E.1) is zero. These compatible low classes occur on the original power orbit. Thus an infinite arithmetic progression of original indices satisfies
   

$$
\boxed{c\ge2.}
   \tag{E.5}
$$



The results are therefore stronger than another finite zero, but they do **not** identify the first nonzero output level uniformly. They prove


$$
\boxed{g=0,\qquad c\ge1,\qquad d\ge7,}
\tag{E.6}
$$


and give an exact formula and an explicit obstruction for the next local problem. A uniform upper bound for $c$, a bound for the primitive norm loss $\nu$, the complete second-force alignment, and the all-prime denominator comparison remain open.

---

## 1. Scope, corrected columns, and retained normalizations

Throughout,


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad
n=2001b,\qquad u\ge0.
$$



The domains remain


$$
0\le j<b,\qquad
1\le i\le b-2,\qquad
0\le j\le b
$$


for contact coordinates, source rows, and reconstructed coordinates respectively.

Set


$$
W_j=\binom{n+2}{j},\qquad
(\mathcal R\theta)_j=W_j(j\theta_{j-1}-\theta_j),
$$


using the actual first and terminal reconstruction rows. The corrected columns are unchanged:


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,
$$


and


$$
P=\frac{Z_w}{p^2},\qquad Q=\frac{Y}{p^3}.
$$



As before,


$$
P=p^cx,\qquad x\text{ \(p\)-primitive},\qquad
\nu=v_p(x^Tx),
$$


so


$$
\boxed{d=v_p(\mathcal N)=2c+4+\nu.}
\tag{1.1}
$$



The established first-force input result is retained:


$$
\boxed{
g=0,\qquad
\frac{f_1^0}{f_0^0}\equiv465=1+16p\pmod{p^2}.
}
\tag{1.2}
$$



No accepted bounded kernel, auxiliary Gram, or prefix computation is requested again.

---

# Part I. Audit of the stronger prefix certificate

## 2. What the supplied evaluator proves

For a positive-binomial atom, put


$$
K=b+v-j,\qquad A=2n+a-1.
$$


The evaluator tracks


$$
(q_{\rm cut},q_W,q_K,c_A),
$$


namely:

- the borrow in $(b-1)-j$;
- the borrow in $(n+2)-j$;
- the borrow in $(b+v)-j$;
- the carry in $A+K$.

Its transition cost is


$$
q_W'+c_A'.
$$


For an accepted complete path this is exactly


$$
v_p\binom{n+2}{j}+v_p\binom{A+K}{K},
$$


by the borrow and carry forms of Kummer’s theorem.

Keeping only the least accumulated cost for a fixed interface is legitimate: future transitions depend only on that interface and the future input digits. All future costs are nonnegative.

The supplied six-digit minima are:



$$
\begin{array}{c|rrrrrr}
(a,v)&0001&0100&1111&0101&1100&0111\\ \hline
(1,0)&3&3&4&6&4&-\\
(1,-1)&3&3&4&6&-&-\\
(30,-29)&3&3&4&6&-&8\\
(30,-30)&3&3&4&6&-&8
\end{array}
\tag{2.1}
$$



These are finite transition data. Their extension to every compatible high word is rigorous because:

1. the first six input digits are fixed;
2. the listed offsets do not cross the six-digit boundary;
3. every reachable six-digit interface already has cost at least three;
4. extending a path cannot reduce its cost.

The $36$ floor-factorial witnesses corroborate the reported full minima for their nine auxiliary inputs. They are not the reason for the universal lower bound.

I have not claimed a new execution of those programs. The following direct digit argument independently proves the lower bound needed here and explains why it is stronger than Turn 4’s Lemma 9.1.

---

## 3. An independent two-part digit proof

The relevant fixed digits are


$$
(n+2)_{3,4,5}=(7,3,9),\quad
(b+v)_{3,4,5}=(28,0,20),\quad
(2n+a-1)_{3,4,5}=(15,6,18)
\tag{3.1}
$$


throughout the offset ranges used below.

### Lemma 3.1 — Digits $3,4,5$ always contribute at least two events

For every choice of incoming interface bits, the sum of weight borrows and addition carries in digits $3,4,5$ is at least two.

**Proof.**

At digit $3$, absence of a weight borrow requires $j_3\le7$. The lower-index digit is then at least


$$
28-j_3-1\ge20.
$$


Adding the digit $15$ therefore creates an addition carry. Thus digit $3$ contributes at least one event.

Suppose digits $4$ and $5$ both contributed zero. At digit $4$, absence of a weight borrow gives $j_4\le3$. If the lower subtraction had an outgoing borrow, its digit would be at least $25$; adding $6$ would force an addition carry. Hence the lower borrow into digit $5$ must be zero.

At digit $5$, absence of a weight borrow gives $j_5\le9$. The lower digit is then $20-j_5\ge11$, and adding $18$ forces a carry. Contradiction. ∎

### Lemma 3.2 — The four baseline atoms have an additional event in digits $0,1$

For the four atoms in (2.1),


$$
e_W^{[0,1]}+e_A^{[0,1]}\ge1.
$$



**Proof.**

If neither low weight digit borrows, then


$$
j_0\le2,\qquad j_1\le7.
$$


For $(a,v)=(1,0),(1,-1)$, the lower digit at position $1$ is $28-j_1$, and the upper addend digit is $14$. Their sum is at least $35$.

For $(a,v)=(30,-29),(30,-30)$, the corresponding digits are $27-j_1$ and $15$, again giving at least $35$. An addition carry is unavoidable. ∎

Combining the lemmas gives, independently of the high word,


$$
\boxed{
W_jP_\alpha(j)\in p^3\mathbb Z_p
\quad\text{for all four baseline atoms and every original }0\le j<b.
}
\tag{3.2}
$$



This proves the decisive portion of the supplied certificate without scanning $29^6$ residues.

### Correction to Turn 4

Every divided unit selected by the indicator


$$
e_W^{\rm low}+e_\alpha^{\rm low}=2
$$


in Turn 4 is zero. Hence


$$
\boxed{
L_{\mathrm I}=L_{\mathrm{II}}=0,\qquad
X_{A,D}\equiv0\pmod p
}
\tag{3.3}
$$


at the $p^{-2}$ normalization.

The old two-observable identity survives only as a zero identity. Its nonzero-norm alternative does not.

---

# Part II. Retaining and evaluating the next-order terms

## 4. Precision and the complete finite normal form

Use the established boundary-aware identity


$$
A^{-1}h
=
\left.
\mathsf R_n\mathsf D\mathsf R_n(w+z)
\right|_{j<b},
\qquad w=\mathsf P_-h,
\tag{4.1}
$$


where $z=T_{\rm out}q$ is determined by the actual endpoint equation


$$
(I+K_\times\mathsf DF)q
=
K_\times\mathsf D\mathsf R_nw.
\tag{4.2}
$$



For computing $Z_w\bmod p^4$, take the full safe truncation


$$
K=4,\qquad M=115.
$$


The accepted homogeneous memory bound permits a head of length


$$
L=58\cdot4+2=234.
$$



The normal-ordered head atoms then satisfy


$$
a\le M+L=349,\qquad -234\le v\le115,
$$


and the exterior atoms, including reconstruction, satisfy


$$
0\le a\le115,\qquad 0\le v\le230.
$$


These lie within the previously established weighted $p^2$ box.

Consequently, after reconstruction, a coefficient divisible by $p^2$ contributes zero modulo $p^4$. We may therefore use the **compatible** expansion


$$
\mathsf D=I+p\mathsf D_1+O(p^2),\qquad
z=pz_1+O(p^2),
\tag{4.3}
$$


but only after this full truncation and offset audit.

---

## 5. The entire first-force head modulo $841$ is retained

Normalize by the unit $f_0^0$:


$$
h=\frac{f^0}{f_0^0}.
$$


Write its complete head modulo $p^2$ as


$$
h=h^{[0]}+ph^{[1]}\pmod{p^2},
\tag{5.1}
$$


with


$$
h^{[0]}_i=
\begin{cases}
i!\bmod p,&0\le i\le28,\\
0,&i\ge29,
\end{cases}
$$


and the actual, not freely chosen, next head $h^{[1]}$. In particular,


$$
\boxed{h^{[1]}_0=0,\qquad h^{[1]}_1=16.}
\tag{5.2}
$$



Thus the primitive initial ratio remains exactly $465\bmod841$. All other entries of the complete next head remain in (5.1). The argument below annihilates their **whole contribution as an operator statement**; it does not replace them by zero input values.

Let


$$
B=\mathcal R\mathsf R_{2n}\mathsf P_-.
$$


Before any further simplification,


$$
\begin{aligned}
\mathcal RA^{-1}h
\equiv{}&
Bh^{[0]}+pBh^{[1]}\\
&+p\,\mathcal R\mathsf R_n\mathsf D_1\mathsf R_n\mathsf P_-h^{[0]}
+p\,\mathcal R\mathsf R_{2n}z_1
\pmod{p^4}.
\end{aligned}
\tag{5.3}
$$



This is the complete expression that must be audited at the new level.

---

## 6. A stronger baseline lemma annihilates the next head

The exact finite head identity is


$$
\begin{aligned}
(\mathsf R_\lambda\mathsf P_-h)_j
={}&(-1)^{b-1}
\sum_{i=0}^{L-1}\sum_{r=0}^{i}
(-1)^{i+r}h_i
\binom j{i-r}
\binom{\lambda+r-1}{r}\\
&\hspace{35mm}\times
\binom{-\lambda-r-1}{b-1-j-r}.
\end{aligned}
\tag{6.1}
$$



It follows by finite Vandermonde expansion and the finite hockey-stick identity. No endpoint is added or completed.

For $\lambda=2n$, the reconstructed atoms have


$$
(a,v)=(r+1,-r-1),\qquad (r+1,-r).
\tag{6.2}
$$



### Lemma 6.1 — Every baseline short-head atom used here is divisible by $p^3$

For $0\le r\le233$, both weighted atoms in (6.2) are divisible by $p^3$.

**Proof.**

Lemma 3.1 supplies two events in digits $3,4,5$.

If the first two weight digits do not borrow, then


$$
j\bmod p^2\le2+7p=205.
$$


The low two-digit upper addend is $406+r$, while the two possible lower minuends are $838-r$ and $839-r$. Both lower minuends exceed $205$, so no two-digit lower borrow occurs. The sum of upper addend and lower index is at least


$$
1244-205=1039>841.
$$


Thus the first two digits contain an addition carry. ∎

Therefore


$$
\boxed{Bh'\in p^3\mathbb Z_p^{b+1}}
\tag{6.3}
$$


for every integral head $h'$ of the stated length, and in particular


$$
\boxed{pBh^{[1]}\equiv0\pmod{p^4}.}
\tag{6.4}
$$



This is why the complete first-force head modulo $841$, including its actual next initial digit $16$, does not contribute to (E.1). The reason is the new lemma, not the old $p^{-2}$ zero.

---

## 7. The compatible $p\mathsf D_1$ contribution

Retain


$$
\mathsf D_1=\sum_{s=1}^{29}k_s\mathsf D_s,
$$


where


$$
k_s=7(s-1)!(21^s+9^s)\quad(1\le s<29),
\qquad k_{29}=-7.
\tag{7.1}
$$



Normal ordering gives


$$
\mathsf R_n\mathsf D_s\mathsf R_n
=
\sum_{t=0}^s
\binom j{s-t}\binom{-n}{t}\,
\mathsf R_{2n+t}
\quad\text{at the shifted row }j-s+t.
\tag{7.2}
$$



For $1\le t<29$,


$$
\binom{-n}{t}\equiv0\pmod p.
$$


Since $h^{[0]}$ has support below $29$, the finite head coefficient


$$
\binom{2n+t+r-1}{r}
$$


also eliminates $r>0$ modulo $p$ in the surviving cases $t=0$ and $t=29$.

Thus it suffices to retain the following reconstructed terms:



$$
\begin{array}{c|c|c}
\text{normal-order term}&(a,v)\text{ before/after the }j-1\text{ shift}
&\text{row factors}\\ \hline
1\le s<29,\ t=0&(1,s-1),(1,s)
&\binom js,\quad j\binom{j-1}s\\
s=29,\ t=0&(1,28),(1,29)
&\binom j{29},\quad j\binom{j-1}{29}\\
s=t=29&(30,-1),(30,0)&1,\quad j
\end{array}
\tag{7.3}
$$



The bounded head polynomial factors are also retained; they are integral and do not weaken divisibility.

### Lemma 7.1 — These coefficient-weighted terms have a third low event

Every term in (7.3), including its displayed row factor, is divisible by $p^3$.

**Proof.**

Two events are supplied by Lemma 3.1.

For $s<29$, suppose the first two weighted digits have no event. Then $j_0\le2$, $j_1\le7$. A nonzero $\binom js\bmod p$ requires $s\le j_0$, leaving only $s=1,2$; for these, the lower offset $s-1$ still forces a first-two-digit addition carry. For the shifted term, a nonzero $j\binom{j-1}s\bmod p$ requires $j_0\ge s+1$, leaving only $s=1$, again forcing that carry.

For $s=29,t=0$, the row factors are $j_1$, and $j_0j_1$ when $j_0\ne0$. With offsets $28,29$, absence of a first-two-digit event forces $j_1=0$. The row factor therefore vanishes.

For $s=t=29$, the two-digit upper addend is $435$, and the lower minuends are $838,839$. Their sums after subtracting a no-borrow weight index exceed $841$, forcing a carry. ∎

Hence


$$
\boxed{
p\,\mathcal R\mathsf R_n\mathsf D_1
       \mathsf R_n\mathsf P_-h^{[0]}
\equiv0\pmod{p^4}.
}
\tag{7.4}
$$



This proves the needed cancellation at the reconstructed, coefficient-weighted level. It does **not** assert that every atom with a positive offset has valuation at least three.

---

## 8. The actual first endpoint return

The established first-order crossed return has support in exterior rows $b,b+1$. Modulo $p$, applying $T_{\rm out}$ does not enlarge that support: its off-diagonal coefficient at distance one is $n\equiv0\pmod p$.

Thus write


$$
z_1=z_{1,0}e_b+z_{1,1}e_{b+1},
\tag{8.1}
$$


where both coefficients are the actual solved endpoint charges. Neither is assumed zero.

After applying $\mathsf R_{2n}$ and reconstruction, the weighted atoms have


$$
(a,v)=(0,0),(0,1),(0,2),
$$


with the $v=2$ atom carrying the factor $j$.

For $v=0,1$, the first two digits force an event in addition to Lemma 3.1. For $v=2$, a first-two-digit event can disappear, but only when $j_0=0$; the reconstruction factor $j$ then supplies the missing factor $p$.

Therefore


$$
\boxed{
p\,\mathcal R\mathsf R_{2n}z_1\equiv0\pmod{p^4}.
}
\tag{8.2}
$$



The endpoint was retained, normal ordered, and then eliminated by a proved weighted statement. It was not deleted from the finite problem.

Combining Sections 5–8,


$$
\boxed{
\mathcal RA^{-1}h\equiv Bh^{[0]}\pmod{p^4}.
}
\tag{8.3}
$$



---

# Part III. The complete $p^{-3}$ actual column

## 9. Reduction to one weighted atom

In (6.1), with $h=h^{[0]}$, every $r>0$ term has an additional factor $p$, while Lemma 6.1 supplies $p^3$. Only $r=0$ remains modulo $p^4$.

Let


$$
F_d=\sum_{r=0}^d(-1)^r(d)_{\underline r},
\qquad F_d=1-dF_{d-1}.
$$


The resulting reconstructed expression is


$$
\begin{aligned}
\frac{Z_{w,j}}{p^3}
\equiv A_0(-1)^{j+1}\frac{W_j}{p^3}
\biggl[
dF_{d-1}\binom{2n+b-j}{b-j}
+
F_d\binom{2n+b-1-j}{b-1-j}
\biggr],
\end{aligned}
\tag{9.1}
$$


where $d=j_0$, and the first term is absent for $d=0$.

If $d>2$, the two low digits contribute at least two events: the weight borrows at digit zero, and either borrows again at digit one or the positive binomial carries there. Lemma 3.1 then gives total valuation at least four.

For $d=0,1,2$, the denominator $b-j$ is a unit and


$$
\frac{\binom{2n+b-j}{b-j}}
     {\binom{2n+b-1-j}{b-1-j}}
=
1+\frac{2n}{b-j}
\equiv1\pmod p.
$$


Since


$$
dF_{d-1}+F_d=1,
$$


equation (9.1) reduces to (E.1).

### Theorem 9.1 — Complete actual-line formula

For every original index,


$$
\boxed{
\frac{Z_{w,j}}{p^3}
\equiv
A_0(-1)^{j+1}
\frac{W_j\binom{2n+b-1-j}{b-1-j}}{p^3}
\pmod p,\qquad j<b.
}
\tag{9.2}
$$



The terminal coordinate is zero at this precision because $v_p(W_b)\ge4$ and the contact solution is integral.

In particular,


$$
\boxed{c\ge1.}
\tag{9.3}
$$



---

## 10. Exact low support of the divided atom

Write


$$
j=s+p^6q,\qquad
s=(d,e,f,t,k,\ell)_{29}.
$$



For the atom in (9.2), equality in the low valuation bound is possible exactly on


$$
\boxed{
\begin{aligned}
&d\in\{0,1,2\},\\
&e\in\{0,\ldots,7\}\cup\{14,\ldots,28\},\\
&f\in\{0,\ldots,5\},\\
&t\in\{0,\ldots,7\}\cup\{15,\ldots,28\},\\
&k=0,\qquad \ell\in\{0,\ldots,20\}.
\end{aligned}
}
\tag{10.1}
$$



Here:

- digits $0,1$ contribute exactly one event;
- digit $2$ contributes none and resets the weight, lower, and addition interface bits to zero;
- digit $3$ contributes one event;
- digit $4$ must be zero and resets those bits again;
- digit $5$ contributes the third event.

The outgoing interface is



$$
\begin{array}{c|c|ccc}
\text{type}&\ell&r&\varepsilon&\eta\\ \hline
\mathrm I&0\le\ell\le9&0&0&1\\
\mathrm{II}&10\le\ell\le20&1&0&0.
\end{array}
\tag{10.2}
$$



Every residue in (10.1) satisfies $s<\beta$. Hence the original cutoff is exactly


$$
\boxed{0\le q\le C.}
\tag{10.3}
$$



No final block is completed.

---

# Part IV. An evaluated small Gram quotient

## 11. High factors

Retain


$$
b=\beta+p^6C,\qquad
n+2=N_0+p^6X,\qquad
X=2001C+1382.
$$


Thus


$$
X\equiv19\pmod{29}.
$$



Once the three low events have occurred, no further weight borrow or addition carry is allowed. The high factors are therefore


$$
V(q)=\binom Xq\binom{2X+C-q}{C-q}\pmod p,
$$




$$
F_{\mathrm I}(q)=(2X+C+1-q)V(q),
\qquad
F_{\mathrm{II}}(q)=(X-q)V(q).
\tag{11.1}
$$



Let $u(s)$ be the divided low factorial unit of the single atom in (9.2). Then


$$
\boxed{
\frac{Z_{w,s+p^6q}}{p^3}
=
A_0(-1)^{s+p^6q+1}u(s)F_\tau(q)
\pmod p
}
\tag{11.2}
$$


on the support of type $\tau$, and zero elsewhere.

---

## 12. Evaluation of the low scalar coefficients

The low norm coefficient factors into contributions from digits $0,1,2$, digits $3,4$, and digit $5$.

### 12.1 Digits $0,1,2$

The digit-zero squared factor sums to


$$
1^2+2^2+1^2=6.
$$



Using Wilson’s identity to combine the other two digit factors gives


$$
K_{012}
=
6\left(\frac{7!}{14!}\right)^2
\binom{24}{5}^{\!2}
S_6\,(T_{25}-T_{24}),
\tag{12.1}
$$


where


$$
S_6=\sum_{a=0}^{7}\bigl((a+1)\cdots(a+6)\bigr)^2,
$$




$$
T_z=\sum_{f=0}^{5}(z-f)^2\binom5f^2.
$$



The complementary range $a=8,\ldots,22$ contributes $-S_6$: the full finite-field sum of the degree-$12$ polynomial is zero, and its values at $23,\ldots,28$ vanish.

The required residues are


$$
\left(\frac{7!}{14!}\right)^2=22,\quad
\binom{24}{5}^2=13,\quad
S_6=22,\quad
T_{25}-T_{24}=10.
$$


Thus


$$
\boxed{K_{012}=27.}
\tag{12.2}
$$



For the last identity, one may use


$$
\sum_f\binom5f^2=\binom{10}{5},\qquad
\sum_f f\binom5f^2=\frac52\binom{10}{5}.
$$



### 12.2 Digits $3,4$

The same factorial combination gives


$$
K_{34}
=
\left(\frac{7!}{15!}\right)^2(7^2-3^2)
\sum_{a=0}^{7}\bigl((a+1)\cdots(a+7)\bigr)^2.
\tag{12.3}
$$


The residues are


$$
\left(\frac{7!}{15!}\right)^2=1,\qquad
7^2-3^2=11,\qquad
\sum_{a=0}^{7}\bigl((a+1)\cdots(a+7)\bigr)^2=13,
$$


so


$$
\boxed{K_{34}=27.}
\tag{12.4}
$$



### 12.3 Digit $5$

For both interface types the digit-five unit is simply


$$
\binom{20}{\ell}.
$$


Indeed,


$$
\frac{9!}{18!\,20!}=1\pmod{29}.
$$



Moreover,


$$
\sum_{\ell=0}^{20}\binom{20}{\ell}^2
=\binom{40}{20}\equiv0\pmod{29},
$$


and


$$
\binom{20}{10}\equiv-3\pmod{29}.
$$


By symmetry,


$$
\sum_{\ell=0}^{9}\binom{20}{\ell}^2=10,\qquad
\sum_{\ell=10}^{20}\binom{20}{\ell}^2=19.
$$



Since $27^2=4\pmod{29}$, the two complete low coefficients are


$$
\boxed{
L_{\mathrm I}^{(3)}=11,\qquad
L_{\mathrm{II}}^{(3)}=18=-11.
}
\tag{12.5}
$$



These are evaluated residues, not an unevaluated matrix specification.

---

## 13. The actual-line normalized Gram formula

Define the original finite sums


$$
\mathscr T_{\mathrm I}
=
\sum_{q=0}^{C}
(2X+C+1-q)^2
\binom Xq^2
\binom{2X+C-q}{C-q}^{2},
$$




$$
\mathscr T_{\mathrm{II}}
=
\sum_{q=0}^{C}
(X-q)^2
\binom Xq^2
\binom{2X+C-q}{C-q}^{2}
\pmod{29}.
\tag{13.1}
$$



Equations (11.2) and (12.5) prove


$$
\boxed{
\left(\frac{Z_w}{p^3}\right)^T
\left(\frac{Z_w}{p^3}\right)
\equiv
11A_0^2(\mathscr T_{\mathrm I}-\mathscr T_{\mathrm{II}})
\pmod p.
}
\tag{13.2}
$$



This is a genuinely small quotient for the complete actual column. It does not assume that this column is primitive.

---

## 14. The two high sums are equal

Write


$$
C=\delta+pC_7,\qquad X=19+pY,
$$


and


$$
q=d+pr,\qquad C-q=k+p(C_7-r-\varepsilon),
$$


where


$$
d+k=\delta+p\varepsilon,\qquad \varepsilon\in\{0,1\}.
$$



A nonzero digit contribution requires


$$
0\le d,k\le19.
$$


Its squared low weight is


$$
\binom{19}{d}^2\binom{9+k}{k}^2
=
\binom{19}{d}^2\binom{19}{k}^2,
\tag{14.1}
$$


because


$$
\binom{9+k}{k}\equiv(-1)^k\binom{19}{k}\pmod{29}.
$$



For each fixed $\varepsilon$, the high factor is independent of $d,k$. Meanwhile,


$$
\begin{aligned}
&(10+\delta-d)^2-(19-d)^2\\
&\hspace{15mm}\equiv
(\delta+20)(\delta-2d)\pmod{29}.
\end{aligned}
\tag{14.2}
$$



The admissible set is invariant under $d\leftrightarrow k$, its squared weight is symmetric, and


$$
\delta-2k\equiv-(\delta-2d)\pmod{29}.
$$


Thus each fixed-$\varepsilon$ digit sum cancels.

Therefore


$$
\boxed{\mathscr T_{\mathrm I}=\mathscr T_{\mathrm{II}}\pmod{29}}
\tag{14.3}
$$


for every compatible high word.

Combining this with (13.2),


$$
\boxed{v_p(\mathcal N)\ge7.}
\tag{14.4}
$$



If $c=1$, this says $\nu\ge1$. If $c\ge2$, the norm is already divisible by $p^8$. A zero norm residue must not be confused with a zero column.

---

# Part V. Why $c=1$ cannot hold uniformly

## 15. A two-high-digit obstruction

Assume


$$
C\equiv814=(2,28)_{29}\pmod{p^2}.
$$


Then


$$
X=2001C+1382
$$


has its first two digits


$$
X_0=19,\qquad X_1=11,
$$


while


$$
(2X)_0=9,\qquad (2X)_1=23.
$$



If $V(q)\ne0$, Lucas and the no-carry condition require, with $K=C-q$,


$$
q_0\le19,\quad K_0\le19,
\qquad
q_1\le11,\quad K_1\le5.
\tag{15.1}
$$



But $q+K=C$. The carry from digit zero is $\varepsilon\in\{0,1\}$, so digit one would require


$$
q_1+K_1=28-\varepsilon\in\{27,28\}.
$$


This contradicts


$$
q_1+K_1\le16.
$$



Hence


$$
\boxed{
C\equiv814\pmod{841}
\Longrightarrow
V(q)=0\ \text{for every }q,
}
\tag{15.2}
$$


and the complete column (9.2) vanishes.

---

## 16. These classes occur on the original power orbit

Put


$$
T=574312172=28\cdot29^5.
$$


A direct bounded modular calculation gives


$$
3^{28}\equiv436=1+15\cdot29\pmod{841}.
$$


Therefore


$$
v_{29}(3^T-1)=6,\qquad
\frac{3^T-1}{29^6}\equiv15\pmod{29}.
\tag{16.1}
$$



Since $\beta\equiv27\pmod{29}$,


$$
27\cdot15\equiv-1\pmod{29}.
$$


The map


$$
u\longmapsto
C(u)=\frac{3^{249005515+Tu}-\beta}{29^6}
$$


is consequently a bijection modulo $29^k$, as $u$ varies modulo $29^k$. This follows inductively from the unit first derivative, or from the cyclic principal-unit group modulo $29^{6+k}$.

In particular, there is one residue class $u\bmod841$ for which


$$
C(u)\equiv814\pmod{841}.
$$


Every nonnegative member of that class is an original index, and satisfies


$$
\boxed{c\ge2.}
\tag{16.2}
$$



Thus “prove $c=1$ uniformly” is not a viable next lemma. A uniform upper bound, or a stratified content law on the power orbit, is the appropriate target.

---

# Part VI. The next proof obligation and the complete second force

## 17. The next norm digit must use the whole next column

Let


$$
T=\frac{Z_w}{p^3}.
$$


We have proved


$$
T^TT\equiv0\pmod p.
$$


The next norm quantity is


$$
\boxed{\eta=\frac{T^TT}{p}\pmod p,}
\tag{17.1}
$$


provided the whole norm is first formed and divided.

If $T$ is primitive and $\eta\ne0$, then


$$
c=1,\qquad \nu=1,\qquad d=7.
\tag{17.2}
$$


Neither hypothesis has been proved on the entire original orbit; Section 16 disproves the first one uniformly.

Computing $\eta$ requires $T\bmod p^2$, hence $Z_w\bmod p^5$. The next calculation must retain:

- the actual first-force head modulo $841$, including its initial ratio $465$;
- the compatible second lower coefficients;
- the next solved finite endpoint charge;
- cross terms between the leading column and the next column;
- the whole divided norm, not termwise divisions of a zero congruence.

The new annihilation lemmas justify why the head modulo $841$ is sufficient for this next output precision: a $p^2$-change in the short head has reconstructed output divisible by $p^5$.

### A concrete follow-on lemma

> **Next-content and whole-norm lemma.**  
> Derive the complete $Z_w\bmod29^5$ finite normal form from the actual head modulo $841$, including the second lower and endpoint terms. Reduce its coordinate content and its whole norm modulo $29^8$ to explicit high-word observables. Prove a uniform content bound, or a finite-state content stratification valid on every original high word; then evaluate the first nonzero primitive norm digit on each surviving stratum.

This is now a precise next-order obligation. It is not a request to repeat the old Gram calculation.

---

## 18. Both initial charges, every source row, and the endpoint remain

For homogeneous basis columns define


$$
U_a=\frac{\mathcal RA^{-1}h^{(a)}}{p^3},
\qquad
G^{(3)}_{ab}=U_a^TU_b.
$$


These are integral: the corrected baseline valuation and the already retained nonbaseline factor $p$ give $p^3$-divisibility for the homogeneous outputs.

With the actual terminal-zero adjoint solutions $\lambda'_{a,\ell}$, the finite identity becomes


$$
\boxed{
p^3U_a^TQ
=
p^3(r_0G^{(3)}_{a0}+r_1G^{(3)}_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda'_{a,\ell}
+W_bU_{a,b}.
}
\tag{18.1}
$$



The complete initial charges remain


$$
\boxed{
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(
T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}
\right),
\qquad i=0,1,
}
\tag{18.2}
$$


and the complete source rows remain


$$
\boxed{
\mathcal H_i=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b},
\qquad1\le i\le b-2.
}
\tag{18.3}
$$



There is no source row at $b-1$. The exterior term at $b$ is not a recurrence step.

The division by $p^3$ in (18.1) belongs to the **whole right-hand side**. A possible cancellation between its normal-ordered source and endpoint must be proved before division or omission.

The actual target is still


$$
\boxed{
x^TQ-p^c\rho_nx^Tx
\equiv0\pmod{p^{c+\nu+1}}.
}
\tag{18.4}
$$


For example, only conditionally on $c=1,\nu=1$ would the required contraction precision be $p^3$, requiring the whole numerator in (18.1) modulo $p^6$.

The independent $\rho_n$ remains defined by its original formula. It is not inferred from a mixed/norm ratio.

Likewise, the logarithmic omission guard remains


$$
\boxed{N_{\log}\ge c+4+\nu.}
\tag{18.5}
$$


No logarithmic part of either initial charge is discarded without that guard.

The complete-force evaluation at the true relative depth is therefore still open. The present norm zero does not supply that evaluation.

---

# Part VII. Bounded arithmetic and global proof status

## 19. New bounded calculation needed

No accepted auxiliary Gram or earlier kernel control needs to be rerun.

The next useful bounded coefficient calculation is the **complete next-order actual-line normal form**, not another evaluation of the now-proved zero leading Gram.

### Inputs

1. $p=29$, the fixed low phase of $b,n$, and the original finite boundary.
2. The complete normalized first-force head modulo $841$, with initial pair
   

$$
(1,465).
$$


3. A safe precision-$p^5$ normal-order truncation:
   

$$
M=144,\qquad L=292.
$$


4. The full lower coefficients and actual endpoint solve through the order needed modulo $p^5$.
5. The single-atom leading column (9.2), including its exact support (10.1).

For these larger offsets, the digit-$3,4,5$ proof in Lemma 3.1 still applies: the relevant small shifts do not change those digits. Thus the required weighted $p^2$ safeguard is available; it need not be guessed from the previous offset box.

### Expected verifiable output

The calculation should return:

- an explicit finite atom assembly for $Z_w/p^3\bmod p^2$;
- separate displayed interior and solved-endpoint contributions, followed by their combined expression;
- zero discrepancy against (9.2) after reduction modulo $p$;
- the whole next norm numerator and its proved divisibility by $p$;
- an explicit observable formula for $\eta$, or a proof that it vanishes further;
- a content test that detects the obstruction $C\equiv814\pmod{841}$;
- a proof certificate for any claimed uniform or stratified content bound.

Those next-order outputs are **not claimed as evaluated here**.

An optional small modular calculation can identify the unique obstructed residue $u\bmod841$, by solving


$$
3^{249005515+574312172u}
\equiv484597094210\pmod{29^8}.
$$


Its expected output is one residue class, together with direct modular verification. The existence and uniqueness of that class have already been proved in Section 16; this numerical label is not needed for the theorem.

---

## 20. All-prime gcd, actual primitive denominator, and whole error

No row content, corrected column, or least actual two-column clearer $d_B$ has been changed.

Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


and


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
}
\tag{20.1}
$$



The primitive multiplier is still $d_B^2/g_B$. The actual denominator satisfies


$$
\boxed{
\log q_n=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{20.2}
$$



For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the evaluated expression remains the whole same-index form


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{20.3}
$$



At the stated scope of the retained signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
\qquad
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$



Neither the present local column formula nor a future successful $29$-adic alignment controls the all-prime sum (20.2). That denominator must still be compared with the whole same-index error.

No automatic-sequence existence theorem, standard Hahn measure, or telescoping existence theorem is being used here to bypass those target-specific obligations.

---

## Proof-status ledger

| Statement | Status |
|---|---|
| Supplied auxiliary and prefix computations | Accepted at their exact finite scope; not requested again |
| Universal baseline $p^3$-divisibility | Independently proved by fixed-digit arguments |
| Former $p^{-2}$ low matrices and column | Proved identically zero |
| $g=0$ and primitive initial ratio $465\bmod841$ | Retained established results |
| Complete $p^{-3}$ expansion before simplification | Derived with full head, lower correction, and finite endpoint |
| Elimination of the next head at this level | Proved by a stronger baseline operator lemma |
| Elimination of compatible $p\mathsf D_1$ and first endpoint terms | Proved after retaining their row factors |
| Actual $p^{-3}$ column | Explicit single-atom formula proved |
| Original cutoff and terminal coordinate | Retained |
| Actual-line low Gram coefficients $11,18$ | Explicitly evaluated |
| Equality $\mathscr T_{\mathrm I}=\mathscr T_{\mathrm{II}}$ | Proved for every compatible high word |
| $c\ge1$, $d\ge7$ | Proved |
| $c\ge2$ on an infinite original-index progression | Proved |
| Uniform claim $c=1$ | Disproved |
| Uniform upper bound for $c$, or complete content stratification | Open |
| First nonzero primitive norm digit | Open |
| Complete second-force alignment at actual relative depth | Open |
| All-prime denominator versus whole same-index error | Open |

## Conclusion

The repaired next-level statement is not merely that the old Gram matrix was zero. It is the complete formula


$$
\boxed{
\frac{Z_{w,j}}{29^3}
\equiv
A_0(-1)^{j+1}
\frac{\binom{n+2}{j}\binom{2n+b-1-j}{b-1-j}}{29^3}
\pmod{29},
\quad j<b,
}
$$


with the actual terminal coordinate zero at this precision.

Its derivation retains the complete first-force head modulo $841$, the compatible first lower correction, and the finite endpoint, and proves why their extra contributions vanish here. The resulting actual-line Gram quotient has evaluated low coefficients $11,-11$, but its two high observables are equal. Thus


$$
\boxed{c\ge1,\qquad d\ge7.}
$$



There is also a concrete obstruction to the simplest proposed content law:


$$
\boxed{
C\equiv814\pmod{841}\Longrightarrow c\ge2,
}
$$


and these classes occur on the original power orbit.

The exact remaining local bottleneck is therefore a **next-order, complete finite-return content and norm law**, not the old two-carry Gram and not an unknown primitive initial direction. The next bounded coefficient calculation must produce $Z_w/29^3\bmod841$ and the whole next norm, while preserving source/end cancellation at the actual relative depth.

Finally, the all-prime gcd, actual primitive denominator, and whole same-index error comparison remain unresolved. Accordingly,


$$
\boxed{\text{An unconditional proof or disproof of the irrationality of }e+\pi
\text{ remains unresolved.}}
$$


