> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 4 — A two-observable quotient for the normalized Gram matrix, and an exact primitive first-force initial line

## Executive assessment

There are two substantive advances.

1. **The complete leading normalized Gram matrix has a two-observable common-tail formula.**  
   This is not the old absolute-$841$ $T_1,T_2$ quotient. In the normalized calculation, the six fixed low digits already consume the entire two-carry budget of every contributing weighted atom. Consequently, **no further weight borrow or binomial addition carry is permitted in the high word**. After retaining all four reconstruction atoms, their divided leading units, and all three valuation layers, the complete leading Gram matrix takes the form
   

$$
\boxed{\overline G_{A,D}=L_{\mathrm I}\,\mathscr T_{\mathrm I}
          +L_{\mathrm{II}}\,\mathscr T_{\mathrm{II}}.}
$$


   The two matrices $L_{\mathrm I},L_{\mathrm{II}}$ are fixed, explicitly defined six-digit coefficient matrices. The two high observables are ordinary finite binomial sums modulo $29$, displayed below.

2. **The actual first-force input content is exactly zero.**  
   From the complete coefficient formula for $f^0$, not from its unnormalized initial congruence, I prove
   

$$
\boxed{g=0.}
$$


   More strongly, on every original index,
   

$$
\boxed{\frac{f_1^0}{f_0^0}\equiv465=1+16\cdot29\pmod{841}.}
$$


   Thus the primitive initial line is known through two digits. At leading order it is the $D=0$ line of the four-atom formula, and $f_0^0$ is a $29$-adic unit.

The fixed low matrices and the two original high-tail residues are not numerically evaluated here. In particular, I do **not** predict the result of the coordinator’s planned auxiliary Gram calculation. The accepted prefix controls are not repeated.

The remaining leading norm question is now a **single specified linear combination of two normalized common tails**, rather than an unknown primitive initial direction. The complete second-force alignment, higher norm loss if that leading combination vanishes, and the all-prime denominator comparison remain open.

---

## 1. Scope and notation

Retain


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad
n=2001b,\qquad u\ge0.
$$



The domains are unchanged:

- contact coordinates: $0\le j<b$;
- source rows: $1\le i\le b-2$;
- reconstructed coordinates: $0\le j\le b$.

Write


$$
W_j=\binom{n+2}{j},\qquad
(\mathcal R x)_j=W_j(jx_{j-1}-x_j),
$$


with the actual first and terminal rows. The two corrected columns remain


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,
$$


and


$$
P=\frac{Z_w}{p^2},\qquad Q=\frac{Y}{p^3}.
$$



For


$$
P=p^cx,\qquad x\ \text{\(p\)-primitive},\qquad
\nu=v_p(x^Tx),
$$


retain


$$
d=v_p(\mathcal N)=2c+4+\nu.
$$



### Accepted finite computations

The supplied source and receipt establish the stated $64$ exact bounded prefix controls, the listed phase-prefix residues, determinant $17$, and the seventh-digit phase check in all $29$ classes.

They do not evaluate an original normalized Gram matrix, norm digit, or complete-force alignment. Nothing below enlarges their scope.

---

# Part I. Independent audit of the finite normal-order lift

## 2. The full lower inverse is not its first-order truncation

The exact finite lower-triangular inverse is


$$
(H^{-1})_{jk}
=c_{j-k}(n)\binom jk,\qquad
c_s(n)=s![z^s]\phi(z)^{-n},
\qquad
\phi(z)=1-z+\frac{z^2}{2}.
$$



At precision $p^K$, it may be truncated to


$$
0\le s\le M,\qquad M=pK-1,
$$


because


$$
v_p(c_s(n))\ge v_p(s!)\ge\lfloor s/p\rfloor.
$$



The first-order statement is only


$$
\mathsf D\equiv I+p\widetilde{\mathsf D}_1\pmod{p^2},
$$


where a compatible integral lift of $\widetilde{\mathsf D}_1$ has coefficients


$$
\frac{c_s(n)}p\bmod p
=
m_0(s-1)!(21^s+9^s),\quad 1\le s<29,
$$




$$
\frac{c_{29}(n)}p\bmod p=-m_0,\qquad
m_0=n/p\equiv7\pmod p.
$$


The coefficients for $30\le s\le57$ vanish at this first order.

This does **not** identify the full lower inverse modulo $p^3$. At that precision the full bandwidth is $86$, and its higher coefficients must first be retained.

The reason those higher coefficients do not alter the leading $p^{-2}$-normalized output is a separate weighted divisibility argument—not the congruence $\mathsf D=I+p\mathsf D_1\pmod{p^2}$ alone.

---

## 3. Finite normal ordering and the actual endpoint

For


$$
(\mathsf R_\lambda)_{jk}=\binom{-\lambda}{k-j},
\qquad
(\mathsf D_s v)_j=\binom js v_{j-s},
$$


the exact finite-support identity is


$$
\boxed{
(\mathsf R_n\mathsf D_s\mathsf R_n v)_j
=
\sum_{t=0}^s
\binom j{s-t}\binom{-n}{t}
(\mathsf R_{2n+t}v)_{j-s+t}.
}
\tag{3.1}
$$


Terms with $j<s-t$ are zero.

The proof uses


$$
\binom{j+\ell}{s}
=\sum_t\binom j{s-t}\binom\ell t,
\qquad
\binom{-n}{\ell}\binom\ell t
=\binom{-n}{t}\binom{-n-t}{\ell-t},
$$


followed by the finite upper convolution. No factorial denominator is introduced.

Let $w=\mathsf P_-h$, zero-extended after $b-1$. With the complete crossed lower matrix $K_\times$, retain


$$
q=K_\times y,\qquad z=T_{\rm out}q,
$$


and the actual endpoint equation


$$
(I+K_\times\mathsf DF)q
=K_\times\mathsf D\mathsf R_nw.
$$


Then


$$
\boxed{
A^{-1}h
=
\left.
\mathsf R_n\mathsf D\mathsf R_n(w+z)
\right|_{j<b}
\pmod{p^K}.
}
\tag{3.2}
$$



Here $z$ is determined by the finite endpoint solve. It is not an arbitrary extension, and it is not zero in general.

Since every nonidentity lower coefficient is divisible by $p$,


$$
K_\times\equiv0\pmod p,
\qquad q\equiv z\equiv0\pmod p.
$$


The rank-two statement in Turn 3 is a statement about this **first-order crossed return on the specified low phase**. It is not a rank-two formula for the full endpoint at every precision.

---

## 4. Exact offset audit after reconstruction

This is the necessary check behind the normalized lift.

Suppose $h$ has support in $0,\ldots,L-1$. In a normal-ordered head term, write $r\le i<L$ for the finite head-transform index. The resulting negative-upper atom has


$$
a=t+r+1,\qquad
v=s-t-r-1.
$$


Hence


$$
1\le a\le M+L,\qquad
-L\le v\le M-1.
$$


The $j-1$ reconstruction term changes $v$ to $v+1$.

For an exterior component at $b+r_{\rm out}$, with $0\le r_{\rm out}<M$, the corresponding atom has


$$
a=t,\qquad v=r_{\rm out}+s-t,
$$


and reconstruction gives


$$
0\le a\le M,\qquad 0\le v\le2M.
$$



All accompanying factors are integral binomial coefficients or integral polynomial factors in the row index. In particular, the head coefficient


$$
\binom{2n+t+r-1}{r}
$$


is retained as an integer; its possible $p$-divisibility is not inverted.

At $K=3$, $M=86$. For $L\le244$, all these atoms lie in


$$
0\le a\le435,\qquad -244\le v\le245.
$$


Thus the established weighted annihilator applies to **each reconstructed atom**:


$$
W_j\binom{-2n-a}{b+v-j}\in p^2\mathbb Z_p.
$$



Every nonbaseline term in (3.2) has an additional factor $p$, from either $c_s(n)$, $s>0$, or $z$. Therefore


$$
\boxed{
\mathcal RA^{-1}h
\equiv
\mathcal R\mathsf R_{2n}\mathsf P_-h
\pmod{p^3}
\qquad(L\le244).
}
\tag{4.1}
$$



This slightly enlarges the sufficient head range used in Turn 3; it does not change the precision.

### What remains divisible by what

- Each reconstructed normal-ordered weighted atom in the stated box carries $p^2$.
- A nonbaseline lower or exterior term therefore carries at least $p^3$.
- This does not establish a universal $p^4$ bound.
- A merely arbitrary lift of a matrix known modulo $p$ need not preserve the stronger reconstructed $p^2$ statement. The compatible lift supplied by the full normal ordering is essential.
- The terminal reconstructed coordinate remains present. Its leading normalized residue is zero because $v_p(W_b)\ge4$.

For the actual first force, its stronger support bound at precision $p^3$ gives a head of length at most $87$, so (4.1) applies directly.

---

# Part II. The actual primitive first-force initial pair

## 5. A complete-formula evaluation of the input content

Define the integer sequence


$$
J_m=[t^m](1+2t+2t^2)^m.
$$


Then the supplied complete first-force formula gives


$$
f_0^0=J_n.
$$



### 5.1 A digit-product identity

For every nonnegative integer $m=\sum_i m_ip^i$,


$$
\boxed{
J_m\equiv\prod_i J_{m_i}\pmod p.
}
\tag{5.1}
$$



Indeed,


$$
(1+2t+2t^2)^m
\equiv
\prod_i(1+2t^{p^i}+2t^{2p^i})^{m_i}\pmod p.
$$


If a selected exponent in the $i$-th factor is $k_i$, then


$$
0\le k_i\le2m_i,\qquad |k_i-m_i|\le28.
$$


The equation


$$
\sum_i(k_i-m_i)p^i=0
$$


forces $k_0=m_0$ by reduction modulo $p$, then successively $k_i=m_i$ for every $i$. This proves (5.1).

### 5.2 All $29$ digit factors are units

The generating function is


$$
\sum_{m\ge0}J_mz^m=(1-4z-4z^2)^{-1/2}.
$$


Consequently,


$$
(m+1)J_{m+1}=(4m+2)J_m+4mJ_{m-1}.
\tag{5.2}
$$



Starting from $J_0=1,J_1=2$, this gives the following residues:



$$
\begin{array}{c|rrrrrrrrrrrrrrr}
m&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14\\ \hline
J_m\bmod29&
1&2&8&3&20&12&14&2&13&24&22&21&21&20&6
\end{array}
$$




$$
\begin{array}{c|rrrrrrrrrrrrrr}
m&15&16&17&18&19&20&21&22&23&24&25&26&27&28\\ \hline
J_m\bmod29&
7&17&19&6&16&4&2&2&18&25&14&15&14&1 .
\end{array}
$$



Every displayed entry is nonzero. The table is verified by (5.2), using only inverses of $1,\ldots,28$.

Combining this with (5.1) proves the all-index statement


$$
\boxed{29\nmid J_m\quad\text{for every }m\ge0.}
\tag{5.3}
$$



Thus, for the actual complete first force,


$$
\boxed{
g=\min\{v_p(f_0^0),v_p(f_1^0)\}=0.
}
\tag{5.4}
$$



This conclusion does not depend on knowing the high digits of $n$.

---

## 6. An exact normalized initial-pair relation

Put


$$
K_n=[t^{n-1}](1+2t+2t^2)^n.
$$


Reciprocity of $2+t^{-1}+2t$ gives


$$
J_{n+1}=2J_n+4K_n.
$$


Since


$$
f_1^0=(n+1)(J_n+K_n),
$$


equation (5.2) yields the exact identity


$$
\boxed{
f_1^0-f_0^0
=
n\left(\frac32J_n+J_{n-1}\right).
}
\tag{6.1}
$$



Because $J_n$ is a $p$-adic unit,


$$
\boxed{
\frac{f_1^0}{f_0^0}
=
1+n\left(\frac32+\frac{J_{n-1}}{J_n}\right)
\quad\text{in }\mathbb Z_{29}.
}
\tag{6.2}
$$



On the actual phase,


$$
n_0=0,\qquad n_1=7.
$$


Subtracting one changes these digits to $28,6$, without changing the higher digits. Therefore (5.1) gives


$$
\frac{J_{n-1}}{J_n}
\equiv
\frac{J_{28}J_6}{J_0J_7}
=\frac{14}{2}=7\pmod{29}.
$$


Since $n/p\equiv7$,


$$
\frac{f_1^0-f_0^0}{pf_0^0}
\equiv
7\left(\frac32+7\right)
=16\pmod{29}.
$$



Hence


$$
\boxed{
\frac{f_1^0}{f_0^0}\equiv1+16p=465\pmod{841},
\qquad
v_p(f_1^0-f_0^0)=1.
}
\tag{6.3}
$$



After the harmless unit rescaling by $f_0^0$, the primitive initial pair is therefore


$$
\boxed{(1,465)\pmod{841}.}
$$



At leading order,


$$
A=f_0^0\bmod p\ne0,\qquad D=f_1^0-f_0^0\bmod p=0.
$$


The disappearance of the $D$-channel is now an established fact about the normalized original first force, not a conditional inference from an unnormalized congruence.

---

# Part III. The specialized normalized common-tail theorem

## 7. Put the four atoms into a common positive-binomial form

For a general homogeneous initial pair, use coordinates


$$
A=h_0,\qquad D=h_1-h_0
$$


modulo $p$.

Retain the low-digit functions $F_d,G_d$ of Turn 3. For $j_0=d,j_1=e$, define the four row coefficient vectors in the $(A,D)$ basis:


$$
c_1(d,e)=
\begin{cases}
\bigl(dF_{d-1},\,d(G_{d-1}+eF_{d-1})\bigr),&d>0,\\
(0,0),&d=0,
\end{cases}
$$




$$
c_2(d,e)=\bigl(F_d,\,G_d+eF_d\bigr),
$$




$$
c_3(d,e)=
\begin{cases}
(0,14dF_{d-1}),&d>0,\\
(0,0),&d=0,
\end{cases}
\qquad
c_4(d,e)=(0,14F_d).
\tag{7.1}
$$



The four positive binomials are


$$
P_\alpha(j)=
\binom{2n+(a_\alpha-1)+b+v_\alpha-j}{b+v_\alpha-j},
$$


with the original zero convention for a negative lower index, where


$$
\begin{array}{c|rr}
\alpha&a_\alpha&v_\alpha\\ \hline
1&1&0\\
2&1&-1\\
3&30&-29\\
4&30&-30
\end{array}
\tag{7.2}
$$



The sign conversion in all four terms gives


$$
\boxed{
X_{A,D;j}
=
(-1)^{j+1}
\sum_{\alpha=1}^4
\bigl(c_\alpha(d,e)\cdot(A,D)\bigr)
\frac{W_jP_\alpha(j)}{p^2}
\pmod p,
\quad j<b.
}
\tag{7.3}
$$



Every quotient in (7.3) is integral. Only after establishing that integrality have $j$ and the coefficient functions been reduced modulo $p$.

The terminal coordinate remains


$$
X_{A,D;b}=0\pmod p.
$$



---

## 8. Fixed low and genuine high parameters

Set


$$
\Lambda=p^6=594823321,\qquad
\beta=410910916,
$$




$$
N_0=186913296,\qquad
D_0=373826588.
$$


Then


$$
b=\beta+\Lambda C,
$$




$$
n+2=N_0+\Lambda X,\qquad
X=2001C+1382,
$$




$$
2n=D_0+2\Lambda X.
\tag{8.1}
$$



The six digits are


$$
\beta=(27,28,5,28,0,20)_{29},
$$




$$
N_0=(2,7,24,7,3,9)_{29},
$$




$$
D_0=(0,14,19,15,6,18)_{29}.
$$



A useful threshold is


$$
\gamma=D_0+\beta-\Lambda=189914183
=(27,13,25,14,7,9)_{29}.
\tag{8.2}
$$



Write


$$
j=s+\Lambda q,\qquad 0\le s<\Lambda.
$$



For each atom, retain separately:

- the number $e_W^{\rm low}(s)$ of outgoing weight borrows in the six low digits;
- the number $e_\alpha^{\rm low}(s)$ of outgoing addition carries for its positive-binomial conversion;
- the outgoing weight borrow $r$;
- the lower-index subtraction borrow $\varepsilon_\alpha$;
- the outgoing addition carry $\eta_\alpha$.

These are low-prefix counts and boundary bits, not valuations of a binomial obtained by discarding its high part.

---

## 9. Saturation: every contributing atom spends both carries below digit six

### Lemma 9.1 — Low-prefix two-carry bound

For every $s$ and each of the four atoms,


$$
\boxed{
e_W^{\rm low}(s)+e_\alpha^{\rm low}(s)\ge2.
}
\tag{9.1}
$$



#### Proof

The digit argument of the weighted $\sigma=2$ theorem takes place entirely in digits $0,\ldots,5$, and applies to these four offsets.

For completeness:

- If there is no low weight borrow, then
  

$$
s_2\le24,\quad s_3\le7,\quad s_4\le3,\quad s_5\le9.
$$


  The subtraction and addition at digits $2,3$ force an addition carry by digit $3$. Either digit $4$ forces another one, or the absence of that carry forces $s_4=0$, after which digit $5$ forces the second.

- Suppose there is exactly one low weight borrow and no low addition carry. Carry-free addition at digit $3$ forces $s_3\ge14$, so the unique weight borrow occurs there. It must stop at digit $4$, requiring $s_4\le2$. Carry-free addition at digit $4$ then forces $s_4=0$ and no lower-index borrow into digit $5$. Carry-free addition at digit $5$ would require $s_5\ge10$, whereas the already-spent weight borrow budget requires $s_5\le9$. This is impossible.

- Two low weight borrows suffice by themselves. ∎

A normalized atom contributes modulo $p$ only if its total valuation is exactly two. Therefore (9.1) implies


$$
\boxed{
e_W^{\rm low}+e_\alpha^{\rm low}=2,
\qquad
e_W^{\rm high}=e_\alpha^{\rm high}=0.
}
\tag{9.2}
$$



For a Gram summand, this gives exactly the required three layers


$$
\boxed{
(e_W,e_\alpha,e_{\alpha'})
=(0,2,2),\ (1,1,1),\ (2,0,0).
}
\tag{9.3}
$$


None has been discarded.

---

## 10. Only two low/high interfaces survive

There is at least one weight borrow or addition carry in digits $0,\ldots,3$. Indeed, if the weight has no borrow there, the bounds on $s_3$ force an addition carry at digit $3$.

Consequently, a normalized atom cannot have **both** an outgoing weight borrow and an outgoing addition carry at digit $5$: that would give at least three low events.

Now inspect the interface bits.

1. For
   

$$
0\le s\le N_0,
$$


   the weight has outgoing borrow $r=0$, all four lower-index borrows are zero, and all four outgoing addition carries are $\eta=1$.

2. For
   

$$
N_0<s<\gamma,
$$


   one has $r=\eta=1$, so no leading atom survives.

3. At $s=\gamma$, the weight already has more than two low borrows.

4. For
   

$$
\gamma<s<\beta-30,
$$


   one has $r=1$, all lower-index borrows zero, and $\eta=0$.

5. For $\beta-30\le s\le\beta$, the weight has at least three low borrows: one in the first two digits, one at digit $3$, and one at digit $5$.

6. For $s>\beta$, one again has $r=\eta=1$, so no leading atom survives.

Thus the only surviving interface types are


$$
\boxed{
\begin{array}{c|ccc|c}
\text{type}&r&\varepsilon_\alpha&\eta_\alpha&\text{low range}\\ \hline
\mathrm I&0&0&1&0\le s\le N_0\\
\mathrm{II}&1&0&0&\gamma<s<\beta-30.
\end{array}
}
\tag{10.1}
$$



Crucially, within either surviving type the interface is **common to all four atoms**.

### Preservation of the original cutoff

For these surviving residues, all four low lower indices are nonnegative. The original condition $j<b$ is therefore exactly


$$
\boxed{0\le q\le C.}
\tag{10.2}
$$



No completed final block has been substituted for $j<b$. The omitted low residues have been proved to contribute zero at this normalization.

---

## 11. Explicit divided low units

For a low residue $s$, put


$$
w=(N_0-s)\bmod\Lambda,
$$




$$
k_\alpha=(\beta+v_\alpha-s)\bmod\Lambda,
$$




$$
z_\alpha=(D_0+a_\alpha-1+k_\alpha)\bmod\Lambda.
$$



Let subscripts $i=0,\ldots,5$ denote digits. Define


$$
\begin{aligned}
U_\alpha(s)
={}&
\mathbf1_{\,e_W^{\rm low}(s)+e_\alpha^{\rm low}(s)=2}\,
(-1)^{e_W^{\rm low}(s)+e_\alpha^{\rm low}(s)}\\
&\times
\prod_{i=0}^{5}
\frac{(N_0)_i!}{s_i!\,w_i!}
\frac{(z_\alpha)_i!}
     {(D_0+a_\alpha-1)_i!\,(k_\alpha)_i!}
\quad\text{in }\mathbb F_{29}.
\end{aligned}
\tag{11.1}
$$



Every denominator is a unit. The factorial carry sign is explicitly retained; on a surviving atom its exponent is two, so its final value is $+1$.

This is the leading-unit factorial formula, not an ordinary Lucas value substituted for a divided binomial. In particular, a positive valuation does not erase its hidden leading unit.

Define


$$
\ell_s=\sum_{\alpha=1}^4U_\alpha(s)c_\alpha(s_0,s_1)
\in\mathbb F_{29}^{\,2}.
\tag{11.2}
$$



Finally, set


$$
\boxed{
L_{\mathrm I}=\sum_{0\le s\le N_0}\ell_s\ell_s^T,
\qquad
L_{\mathrm{II}}=\sum_{\gamma<s<\beta-30}\ell_s\ell_s^T.
}
\tag{11.3}
$$



These are fixed matrices, independent of $u,C,X$.

If desired, their three valuation layers are retained separately by defining


$$
L_\tau^{(r)}
=
\sum_{\substack{s\text{ of type }\tau\\e_W^{\rm low}(s)=r}}
\ell_s\ell_s^T,\qquad r=0,1,2.
$$


Then


$$
L_\tau=L_\tau^{(0)}+L_\tau^{(1)}+L_\tau^{(2)},
$$


corresponding exactly to (9.3).

---

## 12. The two high functions

Since no high outgoing carry is allowed, the high leading units are elementary.

For the weight:

- with incoming borrow $0$, the high factor is $\binom Xq$;
- with incoming borrow $1$, it is
  

$$
X\binom{X-1}{q}=(X-q)\binom Xq.
$$



Here $X\bmod29=19$, so the incoming borrow can be absorbed without an ambiguous division.

For the positive-binomial factor, put $K=C-q$:

- with incoming addition carry $0$, the high factor is
  

$$
\binom{2X+K}{K};
$$


- with incoming addition carry $1$, it is
  

$$
(2X+K+1)\binom{2X+K}{K}.
$$



The polynomial factor in the second expression also correctly kills the case where adding the incoming $1$ would create a new high carry.

Thus define


$$
V(q)=\binom Xq\binom{2X+C-q}{C-q}\pmod{29},
$$




$$
F_{\mathrm I}(q)=(2X+C+1-q)V(q),
$$




$$
F_{\mathrm{II}}(q)=(X-q)V(q).
\tag{12.1}
$$



Equation (7.3) now factors pointwise:


$$
\boxed{
X_{A,D;s+\Lambda q}
=
(-1)^{s+\Lambda q+1}
\bigl(\ell_s\cdot(A,D)\bigr)F_\tau(q)
}
\tag{12.2}
$$


for a surviving low residue of type $\tau$, and is zero for all other low residues.

This is the desired common-tail factorization of the **whole four-atom column**.

---

## 13. The complete leading Gram quotient

Define


$$
\boxed{
\mathscr T_{\mathrm I}(C)
=
\sum_{q=0}^{C}
(2X+C+1-q)^2
\binom Xq^2
\binom{2X+C-q}{C-q}^{2}
\pmod{29},
}
\tag{13.1}
$$




$$
\boxed{
\mathscr T_{\mathrm{II}}(C)
=
\sum_{q=0}^{C}
(X-q)^2
\binom Xq^2
\binom{2X+C-q}{C-q}^{2}
\pmod{29},
\qquad X=2001C+1382.
}
\tag{13.2}
$$



Squaring (12.2) removes its parity sign, and the two low types have disjoint support. Therefore:

### Theorem 13.1 — Normalized two-observable Gram formula

For every compatible high word $C\ge0$,


$$
\boxed{
\overline G_{A,D}
=
L_{\mathrm I}\mathscr T_{\mathrm I}(C)
+
L_{\mathrm{II}}\mathscr T_{\mathrm{II}}(C).
}
\tag{13.3}
$$



The formula retains:

- the original cutoff $j<b$;
- all four reconstruction atoms;
- the coefficient functions on the first two digits;
- every divided binomial leading unit;
- factorial carry signs;
- all three valuation layers;
- the terminal reconstructed coordinate, whose leading residue is proved zero.

This is a two-observable quotient at the **normalized** level. Its proof does not use the old $T_1,T_2$ absolute quotient.

### Conversion to the original homogeneous basis

If the original homogeneous basis is indexed by $(h_0,h_1)$, then


$$
\binom AD
=
S\binom{h_0}{h_1},
\qquad
S=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
$$


Hence


$$
\boxed{\overline G_{\rm initial}=S^T\overline G_{A,D}S.}
\tag{13.4}
$$


In particular, determinant and anisotropy are unchanged.

---

## 14. Precisely which original high-tail data remain

The quotient reduces the high information to two scalar residues; it does not evaluate them from the six fixed digits.

A further one-digit split makes the remaining inputs explicit. Write


$$
C=\delta+29C_7,\qquad \delta=(9-u)\bmod29,
$$




$$
X=19+29Y,\qquad
Y=2001C_7+69\delta+47.
\tag{14.1}
$$



For a low high-word digit $d=q_0$, put


$$
\varepsilon=\mathbf1_{d>\delta},
\qquad
k_d=\delta-d+29\varepsilon.
$$


Only


$$
0\le d\le19,\qquad 0\le k_d\le19
$$


can contribute.

Define the two ordinary tails


$$
\boxed{
R_\varepsilon(C_7,Y)
=
\sum_{r=0}^{C_7-\varepsilon}
\binom Yr^2
\binom{2Y+1+C_7-\varepsilon-r}{C_7-\varepsilon-r}^{2}
\pmod{29},
}
\tag{14.2}
$$


with an empty sum equal to zero.

Then


$$
\mathscr T_{\mathrm I}
=\sum_{\varepsilon=0}^1 a_\varepsilon(\delta)R_\varepsilon,
\qquad
\mathscr T_{\mathrm{II}}
=\sum_{\varepsilon=0}^1 b_\varepsilon(\delta)R_\varepsilon,
\tag{14.3}
$$


where the bounded coefficients are


$$
a_\varepsilon(\delta)
=
\sum_{\substack{0\le d\le19\\
\mathbf1_{d>\delta}=\varepsilon\\0\le k_d\le19}}
(10+\delta-d)^2
\binom{19}{d}^{2}\binom{9+k_d}{k_d}^{2},
$$




$$
b_\varepsilon(\delta)
=
\sum_{\substack{0\le d\le19\\
\mathbf1_{d>\delta}=\varepsilon\\0\le k_d\le19}}
(19-d)^2
\binom{19}{d}^{2}\binom{9+k_d}{k_d}^{2}.
\tag{14.4}
$$



These formulas preserve the affine constant $69\delta+47$.

For $\delta\ge10$, the $\varepsilon=1$ digit set is empty. For $\delta=9$, its only possible digit is $d=19$, where both polynomial factors vanish. Thus


$$
\boxed{\delta\ge9\implies a_1(\delta)=b_1(\delta)=0.}
\tag{14.5}
$$



The original data still required are therefore:

- the actual high integer $C_7$, or an independently proved evaluation of the relevant tails;
- its affine companion $Y=2001C_7+69\delta+47$;
- one or two residues $R_\varepsilon$, according to (14.5).

A usual Lucas digit evaluator reads the high word. The present proof does **not** establish that such input-linear work is unavoidable, and I make no lower-bound claim from finite controls. Nor does it establish a digit-free evaluation on the original power orbit.

The advance is a proved fixed-dimensional observable quotient with explicit reduction identities, not a claim that fixed dimension makes the original input available.

---

# Part IV. What the quotient decides

## 15. A universal determinant and anisotropy identity

Write


$$
L_{\mathrm I}=\begin{pmatrix}a&b\\b&c\end{pmatrix},
\qquad
L_{\mathrm{II}}=\begin{pmatrix}a'&b'\\b'&c'\end{pmatrix},
$$


and put $T=\mathscr T_{\mathrm I}$, $U=\mathscr T_{\mathrm{II}}$. Then, for every compatible high word,


$$
\boxed{
\det\overline G
=
(ac-b^2)T^2
+(ac'+a'c-2bb')TU
+(a'c'-b'^2)U^2.
}
\tag{15.1}
$$



Since $-1$ is a square in $\mathbb F_{29}$, a binary symmetric form is anisotropic precisely when its determinant is a nonsquare. Thus


$$
\boxed{
\overline G\text{ is anisotropic}
\iff
\chi_{29}\!\left(\det\overline G\right)=-1.
}
\tag{15.2}
$$



This is an exact anisotropy test from two high-tail residues and fixed low coefficients.

A singular Gram matrix is not anisotropic. A nonsingular matrix with square determinant is split. These statements concern the leading quadratic form; they do not assert that a zero norm residue is a zero output vector.

If literal output-vector nonvanishing is needed in an isotropic case, (12.2) supplies the sharper criterion: one needs a nonzero low coefficient on a type and a high function $F_\tau$ that is not identically zero. A sum of squares alone cannot replace that support test.

---

## 16. The actual first-force norm now lies on a known line

By Sections 5–6,


$$
g=0,\qquad (A,D)=(A,0),\qquad A\ne0
$$


for the actual first force.

Therefore


$$
\boxed{
P^TP
\equiv
A^2\left(
(L_{\mathrm I})_{11}\mathscr T_{\mathrm I}
+
(L_{\mathrm{II}})_{11}\mathscr T_{\mathrm{II}}
\right)
\pmod{29}.
}
\tag{16.1}
$$



The exact remaining leading norm scalar is


$$
\boxed{
\mathscr L_{\rm act}
=
(L_{\mathrm I})_{11}\mathscr T_{\mathrm I}
+
(L_{\mathrm{II}})_{11}\mathscr T_{\mathrm{II}}.
}
\tag{16.2}
$$



If


$$
\mathscr L_{\rm act}\ne0,
$$


then rigorously


$$
\boxed{c=0,\qquad \nu=0,\qquad d=4.}
\tag{16.3}
$$



This is a conditional deduction. Neither (16.2) nor the complete auxiliary Gram result is numerically evaluated here.

If (16.2) vanishes, the correct next target is the actual line with its known next initial digit


$$
f_1^0/f_0^0\equiv1+16p\pmod{p^2},
$$


together with the next normalized output terms. There is no longer an unknown positive first-force input content to be guessed.

---

# Part V. Precision, complete forcing, and the global objective

## 17. What is now known about the logarithmic guard

The input-content part is closed:


$$
g=0.
$$



Also,


$$
v_p(n!)\ge n/p=69b,\qquad
v_p(b!)\le b/28.
$$


Thus


$$
N_{\log}
\ge
138b-\frac b{28}
-\lfloor\log_{29}(4003b-1)\rfloor,
\tag{17.1}
$$


which is certainly greater than $4$ on the original family.

But the required guard remains


$$
\boxed{N_{\log}\ge c+4+\nu.}
\tag{17.2}
$$



If (16.2) is nonzero, (16.3) verifies this guard immediately. If it vanishes, this report does not bound the remaining output content $c$ or primitive norm loss $\nu$. In particular, the large size of $N_{\log}$ is not by itself a proof of the required inequality.

The obstruction is now specifically an output-norm obstruction, not an unknown first-force common input factor.

---

## 18. Both complete second initial charges, all source rows, and the whole $p^3$ division remain

Use the original homogeneous initial basis and define


$$
X_a=\frac{\mathcal RA^{-1}h^{(a)}}{p^2},
\qquad
G_{ab}=X_a^TX_b,\qquad a,b\in\{0,1\}.
$$



For the actual terminal-zero adjoint solutions $\lambda_{a,\ell}$, retain the exact identity


$$
\boxed{
p^3X_a^TQ
=
p^2(r_0G_{a0}+r_1G_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda_{a,\ell}
+W_bX_{a,b}.
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



There is no source row at $b-1$, and no replacement of the exterior $b$ by a recurrence step.

The division by $p^3$ in (18.1) is a division of the **whole right-hand side**. Its individual initial, source, and exterior terms are not separately divisible or discardable merely because their sum is.

Even if the leading norm test succeeds, the local alignment still requires


$$
P^TQ-\rho_nP^TP\equiv0\pmod p.
$$


Computing this from (18.1) requires the complete numerator at the corresponding guarded precision. The independent $\rho_n$ must still come from its original definition.

---

## 19. Bounded exact arithmetic isolated by the theorem

No accepted control is requested again, and no outcome of the planned auxiliary Gram calculation is predicted.

### 19.1 The new fixed low-coefficient calculation

The only new bounded coefficient data in (13.3) are the six entries of


$$
L_{\mathrm I},\qquad L_{\mathrm{II}}.
$$



Their inputs are completely fixed:

- $p=29$;
- the six-digit integers $N_0,D_0,\beta$;
- the four pairs in (7.2);
- the functions $F_d,G_d$;
- the leading-unit rule (11.1).

They need not be evaluated by enumerating all $29^6$ low residues.

For each of the sixteen ordered atom pairs, a six-digit contraction can retain:

- five boundary bits: one weight borrow, two lower-index borrows, two addition carries;
- valuation counts $(e_W,e_\alpha,e_{\alpha'})$ with
  

$$
e_W+e_\alpha\le2,\qquad e_W+e_{\alpha'}\le2.
$$



There are only


$$
9+4+1=14
$$


possible count triples, hence at most $32\cdot14=448$ formal states after coefficient assembly on the first two digits.

The accepted terminal states are precisely the three layers (9.3), separated into the two interface types (10.1). Local factorial units and signs are multiplied before state aggregation.

This is a fixed bounded contraction, independent of the original high-word length. It can be extracted as part of the implementation of the already planned normalized evaluator; no second full auxiliary Gram run is needed.

### Expected verifiable output

A numerical coefficient extraction should report:

1. the two symmetric matrices $L_{\mathrm I},L_{\mathrm{II}}$;
2. their three valuation-layer contributions;
3. zero discrepancy in
   

$$
\overline G_{\rm initial}
   =
   S^T\bigl(
   L_{\mathrm I}\mathscr T_{\mathrm I}
   +L_{\mathrm{II}}\mathscr T_{\mathrm{II}}
   \bigr)S
$$


   when compared with the planned four-atom auxiliary evaluator;
4. the actual auxiliary determinant and isotropic lines, without presupposing their values.

Those numerical matrix residues are **not claimed in this report**.

The small table in Section 5 is already an explicit arithmetic certificate for $g=0$: its expected entries are displayed and are checked by the recurrence (5.2). Its use is a finite calculation followed by the proved all-index digit-product theorem, not an extrapolation from a finite nondivisibility scan.

---

## 20. Final all-prime gcd, actual denominator, and whole error

No row content, corrected column, or least actual two-column clearer is changed.

Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
}
\tag{20.1}
$$



The primitive multiplier remains $d_B^2/g_B$, and the actual primitive denominator remains


$$
\boxed{
\log q_n
=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{20.2}
$$



For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the relevant evaluated expression remains the whole same-index form


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



Neither a leading normalized Gram calculation nor a successful local $29$-adic alignment controls the all-prime sum in (20.2).

---

## Proof-status ledger

| Statement | Status |
|---|---|
| Supplied NEWmod841 controls | Accepted at their exact finite scope; not repeated |
| Full lower inverse versus first-order truncation | Distinguished explicitly |
| Complete finite normal ordering, including $q,z$ | Audited with the actual endpoint retained |
| Reconstructed atom ranges at $K=3$ | Explicitly checked |
| Leading normalized lift for short heads | Proved, with sufficient range $L\le244$ |
| $29\nmid J_m$ for every $m\ge0$ | Proved by digit product and the displayed digit table |
| Actual first-force input content $g=0$ | Proved |
| Actual normalized initial ratio $f_1^0/f_0^0\equiv465\pmod{841}$ | Proved |
| Two-observable normalized Gram quotient | Proved for every compatible high word |
| All three normalized valuation layers and divided units | Retained explicitly |
| Universal determinant/anisotropy identity | Proved |
| Numerical fixed low matrices | Not evaluated here |
| Planned auxiliary full Gram result | Unknown; no outcome predicted |
| Original leading norm scalar $\mathscr L_{\rm act}$ | Not evaluated |
| Bound on output content and norm loss if that scalar vanishes | Open |
| Complete normalized second-force alignment | Open |
| All-prime denominator versus whole same-index error | Open |

## Conclusion

The new normalized structural theorem is


$$
\boxed{
\overline G_{A,D}
=
L_{\mathrm I}\mathscr T_{\mathrm I}
+
L_{\mathrm{II}}\mathscr T_{\mathrm{II}}.
}
$$


Its mechanism is stronger than a generic finite-state description: the fixed six-digit phase consumes the entire normalized two-carry budget, leaves only two possible interfaces, and makes the high factor common to all four reconstruction atoms.

Independently, the complete first-force formula gives


$$
\boxed{
g=0,\qquad
\frac{f_1^0}{f_0^0}\equiv1+16\cdot29\pmod{841}.
}
$$


Thus the actual primitive initial direction is no longer an outstanding unknown.

The exact remaining leading local bottleneck is the nonvanishing of


$$
\boxed{
(L_{\mathrm I})_{11}\mathscr T_{\mathrm I}
+
(L_{\mathrm{II}})_{11}\mathscr T_{\mathrm{II}}
}
$$


on the original power orbit. If it is nonzero, then $c=\nu=0$ and $d=4$; the complete-force identity must still be evaluated with both initial charges, every source row $1,\ldots,b-2$, exterior $b$, and the whole division by $p^3$. If it vanishes, the known next initial digit supplies a concrete starting point for the next normalized return.

Finally, even an affirmative local resolution leaves the final all-prime gcd, actual primitive denominator, and whole same-index error comparison unresolved. Therefore


$$
\boxed{\text{An unconditional proof or disproof of the irrationality of }e+\pi
\text{ remains unresolved.}}
$$


