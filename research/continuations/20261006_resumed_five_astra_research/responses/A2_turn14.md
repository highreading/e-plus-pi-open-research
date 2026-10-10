> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 14 — Complete exterior forcing, the actual mixed $29^3$-zero, and a growing-depth paid-tail theorem

## Executive assessment

The recovered all-row source closes the missing force identification. More importantly, it permits an independent recurrence check: the exponential exterior vector gives **exactly the displayed source on every row $1,\ldots,b-2$**, with the positive sign and the stated normalization, while the logarithmic contribution satisfies the corresponding homogeneous recurrence on those rows.

The subsequent exterior-inverse argument also survives, once its finite-boundary interpretation is made explicit. The inverse used there is the inverse of $\mathsf P_-A_{\rm ext}$, not directly of $A_{\rm ext}$; the finite lower-triangular $\mathsf P_-$ conversion is what makes the interior-zero argument legitimate.

The resulting fixed-layer conclusion is now unconditional at the scope of the retained finite-normal-form and tail results:



$$
\boxed{
u\equiv2\pmod{29^9}
\quad\Longrightarrow\quad
Y\in29^4\mathbb Z_{29}^{b+1},
\qquad
F^TQ\equiv0\pmod{29^3}.
}
$$



Here $F=Z_w/29^4$ and $Q=Y/29^3$ are the actual corrected columns, including their separate physical terminal coordinates.

There is also a new all-depth result. The exterior inverse preserves a growing factorial valuation filtration. Consequently, at precision $29^K$, its actual exterior solution needs only



$$
0\le h\le29(K-1)+1,
$$



and the reconstructed exponential response needs only shifts



$$
0\le v\le29(K-1)+2.
$$



This is a stronger statement than the earlier displacement estimate. The earlier $57v$ bound and $H_6=458$ remain valid; the new theorem explains why the actual factorial exterior data occupy a substantially smaller part of that envelope.

At the **true relative precision**


$$
K=d-c=c+4+\nu,
$$


this produces a proved, complete-force replacement whose error is annihilated modulo $29^{d+2}$ after contraction against the actual first column. The logarithmic force is either paid by its guard or retained as an explicitly bounded actual head. This theorem applies, in particular, along an infinite original subsequence with $c\to\infty$. It does not impose an impossible constant-content cylinder.

This advances the norm-relative problem by proving an actual growing-depth tail separation. It does **not** evaluate the remaining finite primitive mixed contraction or establish its alignment with the independently defined $\rho_n$. The local alignment law, the all-prime denominator comparison, and irrationality of $e+\pi$ remain unresolved.

---

## 1. Preserved objects and accepted arithmetic

Throughout,


$$
p=29,\qquad D=p^3,
$$




$$
b=3^{249005515+574312172u}
  =410910916+p^6C,\qquad n=2001b,\qquad u\ge0.
$$



The domains remain:

- contact coordinates: $0\le j<b$;
- source rows: $1\le i\le b-2$;
- reconstructed coordinates: $0\le j\le b$.

Write


$$
W_j=\binom{n+2}{j},
\qquad
(\mathcal Rx)_j=W_j(jx_{j-1}-x_j),
\qquad x_{-1}=x_b=0.
$$


Thus


$$
(\mathcal Rx)_b=bW_bx_{b-1}.
$$



The actual columns are


$$
Z_w=\mathcal RA^{-1}f^0,
\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b.
$$



Retain


$$
P=\frac{Z_w}{p^2}=p^cx,\qquad x\ \text{primitive at }p,
$$




$$
Q=\frac{Y}{p^3},\qquad F=\frac{Z_w}{p^4},
$$


and


$$
\nu=v_p(x^Tx),\qquad d=2c+4+\nu.
$$



The accepted actual conclusions are


$$
u\equiv2\pmod{p^3}
\Longrightarrow Z_w\in p^4\mathbb Z_p^{b+1},\quad d\ge9,
$$


and


$$
u\equiv2\pmod{p^9}\Longrightarrow d\ge10.
$$



### 1.1 The completed $\Xi$ calculation

The new receipt supplies


$$
(\alpha_{\rm I},\alpha_{\rm II})=(33,837)\pmod{841},
$$




$$
(\beta_{\rm I},\beta_{\rm II})=(5,24)\pmod{29},
\qquad
\gamma=22,
\qquad
\Xi=17.
$$



The short final arithmetic is consistent:


$$
\frac{33+837}{29}=30,\qquad \frac{638}{29}=22,
$$


and


$$
4\cdot22+13\cdot30+11\cdot5+22\cdot24
\equiv17\pmod{29}.
$$


Also,


$$
5+24\equiv0\pmod{29}.
$$



I reuse this finite calculation together with Turn 13’s audited support and division arguments. No $42$-term calculation, $135918$-atom sum, or accepted original-tail computation is repeated.

In particular, $\Xi=17\ne0$ still does not evaluate $\mathscr L$, $\mathscr L_{FG}$, $c$, or the actual primitive norm.

---

# Part I. Exact identification of the recovered complete force

## 2. The finite coordinate conversion agrees with the actual $A$ and $\mathcal R$

Put


$$
\phi(z)=1-z+\frac{z^2}{2},
\qquad a_s(n)=[z^s]\phi(z)^n.
$$



Let $T_n$ and $R_n$ denote the finite upper-triangular matrices


$$
(T_n)_{ij}=\binom n{j-i},
\qquad
(R_n)_{ij}=\binom{-n}{j-i},
\qquad 0\le i,j<b.
$$


They are integral inverses.

The source excerpt gives


$$
\widetilde N_{ij}
=\sum_s a_s(n)(n+i)_{\underline s}
       \binom{n+i-s}{j}.
$$


For $j<b$, finite Vandermonde gives


$$
(\widetilde NT_n)_{ij}
=
\sum_s a_s(n)(n+i)_{\underline s}
       \binom{2n+i-s}{j}.
$$


There is no omitted finite-boundary term: in this upper-triangular product the intermediate index is at most $j<b$.

Thus the actual finite matrix is


$$
A=\widetilde NT_n.
\tag{2.1}
$$



The reconstruction in the excerpt is


$$
\mathcal T=\mathcal RR_n.
$$


Consequently


$$
\mathcal T\widetilde N^{-1}
=\mathcal RA^{-1}.
\tag{2.2}
$$



This verifies the coordinate convention without a divided-factorial rescaling of the force.

For the exterior extension, define


$$
A_{{\rm ext},ij}
=
\sum_s a_s(n)(n+i)_{\underline s}
       \binom{2n+i-s}{j},
\qquad j\ge0.
\tag{2.3}
$$


Each row has finite support. Equation (2.3) is the polynomial extension of the row, not an attempt to extend the finite matrix product beyond its original column range.

---

## 3. The all-row factorial identity and the physical terminal

Let


$$
t_j=j!,\qquad 0\le j<b,
$$


and


$$
z_h=\frac{(b+h)!}{b!},\qquad h\ge0.
$$



The complete exponential force satisfies


$$
h_i^e=\sum_{j\ge0}A_{{\rm ext},ij}j!,
\qquad 0\le i<b,
\tag{3.1}
$$


because


$$
m!\sum_{r=0}^{m}\frac1{r!}
=\sum_{j=0}^{m}\binom mjj!.
$$



Therefore, on **every** contact row,


$$
\boxed{
r_i
=
\frac{h_i^e+h_i^F-(At)_i}{b!}
=
\sum_{h\ge0}A_{{\rm ext},i,b+h}z_h
+\frac{h_i^F}{b!}.
}
\tag{3.2}
$$



The sum is finite for each $i$.

The terminal convention also agrees exactly. Directly,


$$
\mathcal Rt=-e_0+b!W_be_b.
$$


Using (2.2),


$$
V_w
=\mathcal RA^{-1}(h^e+h^F)+e_0
=b!\mathcal RA^{-1}\mathbf r+b!W_be_b.
$$


Hence


$$
\boxed{
Y=\frac{V_w}{b!}
=\mathcal RA^{-1}\mathbf r+W_be_b.
}
\tag{3.3}
$$



The $+W_be_b$ term is not part of an algebraically continued contact atom.

---

## 4. Independent recurrence verification on every source row

The documentary identity can be checked against an explicit recurrence, rather than merely declared to be another description of the same vector.

Define row polynomials in $y=1+x$:


$$
\mathscr A_i(y)
=
y^n\phi(\partial_y)^n y^{n+i},
$$




$$
\mathscr Q_i(y)
=
y^{n+1}\phi(\partial_y)^{n+1}y^{n+i}.
$$


Then


$$
A_{{\rm ext},ij}=[x^j]\mathscr A_i(1+x),
$$


and the supplied complete source is


$$
\mathcal H_i=[x^b]\mathscr Q_i(1+x).
\tag{4.1}
$$



### 4.1 The polynomial recurrence

For $i\ge1$, define


$$
\begin{aligned}
(\mathcal Da)_i={}&a_{i+1}-(2n+2i+1)a_i\\
&+\frac{(n+i)(n+3i-1)}2a_{i-1}\\
&-\frac{(i-1)(n+i)(n+i-1)}2a_{i-2}.
\end{aligned}
\tag{4.2}
$$


At $i=1$, the last coefficient is zero, so no value at index $-1$ is required.

The exact polynomial identity is


$$
\boxed{
(\mathcal D\mathscr A)_i
=(1-\partial_y)\mathscr Q_i.
}
\tag{4.3}
$$



To verify it, put $m=n+i$ and $U=\phi(\partial_y)^n$. On polynomials,


$$
U^{-1}yU=y-n\frac{\phi'(\partial_y)}{\phi(\partial_y)}.
$$


Thus, after removing the common outer factor $y^nU$, the operator on the right of (4.3) is


$$
y(1-\partial_y)\phi(\partial_y)
+n(1-\partial_y)^2-(n+1)\phi(\partial_y).
$$


Its action on $y^m$ is


$$
\begin{aligned}
y^{m+1}
&-(2m+1)y^m
+\frac{m(3m-2n-1)}2y^{m-1}\\
&+\frac{m(m-1)(n+1-m)}2y^{m-2}.
\end{aligned}
$$


Substituting $m=n+i$ gives (4.2).

This derivation fixes the sign and scaling of the recurrence. It uses the source’s $\mathcal H_i$ without an extra factor.

### 4.2 The exponential tail produces exactly $\mathcal H_i$

For a polynomial $g$, define


$$
\mathcal E_b(g)
=
\frac1{b!}\sum_{j\ge b}j![x^j]g(1+x).
$$


A finite telescoping calculation gives


$$
\boxed{
\mathcal E_b((1-\partial_y)g)
=[x^b]g(1+x).
}
\tag{4.4}
$$



Indeed, if $g(1+x)=\sum_jg_jx^j$, then


$$
\sum_{j\ge b}j!\bigl(g_j-(j+1)g_{j+1}\bigr)=b!g_b.
$$



The exponential residual is


$$
r_i^{(e)}=\mathcal E_b(\mathscr A_i).
$$


Applying (4.3)–(4.4),


$$
\boxed{
(\mathcal Dr^{(e)})_i=\mathcal H_i,
\qquad 1\le i\le b-2.
}
\tag{4.5}
$$



Its two initial values are precisely the exponential parts of Turn 0’s charges, since


$$
\mathcal E_b(y^m)=T_m.
$$



### 4.3 The logarithmic part is homogeneous on all source rows

Define the linear functional


$$
\mathcal L_b(y^m)=L_m/b!.
$$


The supplied recurrence for $L_m$ gives


$$
\mathcal L_b((1-\partial_y)y^m)
=\frac{2(m-1)!u_{m-1}}{b!}.
$$



Consequently


$$
\mathcal L_b((1-\partial_y)\mathscr Q_i)
=
\frac{2(n+i)!}{b!}
[z^{n+i}]
\left[
\phi(z)^{n+1}
\frac{d^n}{dz^n}\frac1{\phi(z)}
\right].
\tag{4.6}
$$



The bracketed expression is a polynomial of degree at most $n$. This follows inductively from


$$
R_n(z)=\phi(z)^{n+1}
\frac{d^n}{dz^n}\frac1{\phi(z)},
$$




$$
R_{n+1}=\phi R_n'-(n+1)\phi'R_n,
\qquad \deg R_n\le n.
$$


Therefore (4.6) is zero for every $i\ge1$.

It follows that


$$
\boxed{
(\mathcal Dr^{(F)})_i=0,
\qquad 1\le i\le b-2.
}
\tag{4.7}
$$



Its initial values are exactly the $L_m/b!$ terms in the two complete charges.

### Conclusion of the recurrence audit

The recovered vector has:

- both actual initial charges;
- exactly the source $\mathcal H_i$, with positive sign;
- every source row $1,\ldots,b-2$;
- no added recurrence row at $b-1$.

Since (4.2) determines the next entry from the preceding entries, with its $i=1$ singular term already zero, these data uniquely determine the finite vector.

Thus the recovered identity is fully compatible with the actual recurrence definitions. The former $\mathbf{EF}_K$ is no longer an additional hypothesis.

---

## 5. The logarithmic guard is valid for the whole vector

For a term with $k=n+i-s\ge0$,


$$
(n+i)_{\underline s}(2n+i-s)!
=
\frac{(n+i)!}{k!}(n+k)!
=
(n+i)!\,n!\binom{n+k}{k}.
$$


Using the stated bound for $L_m$, this gives the rowwise estimate


$$
\boxed{
v_p(r_i^{(F)})
\ge
v_p((n+i)!)+v_p(n!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor.
}
\tag{5.1}
$$



In particular,


$$
v_p(r_i^{(F)})\ge N_{\log},
$$


where


$$
N_{\log}
=
2v_p(n!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor.
\tag{5.2}
$$



This is a complete-row bound, not a bound on only the two charges.

On the original family, $N_{\log}>6$. For example,


$$
v_p(n!)\ge n/p=69b,\qquad v_p(b!)\le b/28,
$$


while the logarithmic term is negligible compared with $b$. Hence


$$
\boxed{\mathbf r\equiv A_{IE}z\pmod{p^6}}
\tag{5.3}
$$


is now proved for the actual force.

At norm-relative depth, the comparison $N_{\log}\ge d-c$ is still required before discarding the logarithmic contribution.

---

# Part II. Exterior inverse and finite boundary

## 6. Which full operator is inverted

On nonnegative indices, set


$$
(D_+)_{ij}=a_{i-j}(n)\frac{i!}{j!},
\qquad
(D_-)_{ij}=c_{i-j}(n)\binom ij,
$$




$$
c_s(n)=s![z^s]\phi(z)^{-n}.
$$



The row-generating calculation gives


$$
\boxed{
B_{\rm ext}:=\mathsf P_-A_{\rm ext}=T_nD_+T_n.
}
\tag{6.1}
$$


Its inverse at fixed $p$-adic precision is


$$
\boxed{
\mathcal C_\infty=R_nD_-R_n.
}
\tag{6.2}
$$



This is the inverse of $B_{\rm ext}$, not directly of $A_{\rm ext}$.

Let


$$
I=\{0,\ldots,b-1\},\qquad E=\{b,b+1,\ldots\}.
$$


Because $\mathsf P_-$ is lower triangular,


$$
(B_{\rm ext})_{II}=(\mathsf P_-)_{II}A_{II},
\qquad
(B_{\rm ext})_{IE}=(\mathsf P_-)_{II}A_{IE}.
\tag{6.3}
$$



For the exterior solution


$$
(\mathcal C_\infty)_{EE}v=z,
\tag{6.4}
$$


put


$$
\theta^{(e)}=-(\mathcal C_\infty)_{IE}v.
\tag{6.5}
$$


The vector $\mathcal C_\infty(0,v)$ has exterior part $z$, and its image under $B_{\rm ext}$ has zero interior part. Equations (6.3) therefore imply


$$
\boxed{
A_{II}\theta^{(e)}=A_{IE}z.
}
\tag{6.6}
$$



That is the exact finite-boundary argument. It neither substitutes an infinite inverse for $A_{II}^{-1}$ nor discards a return term.

---

## 7. The exterior kernel and the original $H_6=458$ bound

Vandermonde gives


$$
\boxed{
(\mathcal C_\infty)_{jk}
\equiv
\sum_{s=0}^{pK-1}c_s(n)
\sum_{a=0}^{s}
\binom j{s-a}\binom{-n}{a}
\binom{-2n-a}{k+s-a-j}
\pmod{p^K}.
}
\tag{7.1}
$$



All coefficients are integral at $p$. Only consolidated $2n$-atoms remain.

The earlier truncation argument is valid:

1. $v_p(z_h)\ge\lfloor h/p\rfloor$, so $h\le pK-1$ suffices initially.
2. Every nonzero lower-symbol coefficient is divisible by $p$.
3. If a symbol coefficient has valuation $v\ge1$, its lower displacement is at most
   

$$
s\le(2p-1)v=57v.
$$


4. The inverse of the zeroth-order exterior block is the upper-triangular $T_{2n}$, which cannot increase the largest supported index.
5. A term of total perturbation order below $K$ therefore reaches no farther than
   

$$
H_K=pK-1+57(K-1).
$$



Thus


$$
\boxed{H_6=173+285=458.}
\tag{7.2}
$$



At $K=6$, (7.1), followed by reconstruction, gives the safe box


$$
\boxed{
0\le a\le173,\qquad 0\le v\le632,
}
\tag{7.3}
$$


with row-binomial indices at most $174$.

The finite exterior solve through this envelope includes all returns capable of affecting the output modulo $p^6$.

A sharper result will be proved in Part IV. It is not needed to justify the fixed-layer argument.

---

# Part III. Promotion of the fixed-layer mixed theorem

## 8. Both columns preserve the required physical forcing digits

The retained first-column box is


$$
0\le a\le523,\qquad -350\le v\le346.
$$


The second-column safe box is (7.3).

For atoms


$$
W_j\binom{-2n-a}{b+v-j},
$$


the corresponding positive-binomial addend is $2n+a-1$. The low remainders satisfy:



$$
\begin{array}{c|c|c}
&b+v\bmod D&2n+a-1\bmod D\\ \hline
\text{first column}&4694\ldots5390&16384\ldots16907\\
\text{second column}&5044\ldots5676&16384\ldots16557 .
\end{array}
$$



None crosses a $D$-boundary. Thus both columns retain the physical triples at positions $3,4,5$:


$$
(7,28,15),\qquad(3,0,6),\qquad(9,20,18).
$$


The retained complete potential certificate supplies two events for every incoming interface.

On $u\equiv2\pmod{p^3}$, physical digit $7$ is


$$
(W_7,B_7,A_7)=(8,25,17).
$$


If neither a weight borrow nor an addition carry occurred there, the available digits would satisfy


$$
x\le8-w,\qquad K\le11-c,
$$


but lower-index subtraction would require


$$
x+K+k=25+29k'.
$$


The left side is at most $20$, an impossibility.

Hence every retained atom in **both** columns has at least three physical events.

The second-column row-binomial indices are at most $174<841$; the first-column indices retain their previously proved bound below $841$. Their row factors therefore have the required period $p^3$ modulo $p^2$.

---

## 9. Actual second-column saturation

Modulo $p$,


$$
z_0=1,\qquad z_1=-1,\qquad z_h=0\quad(h\ge2),
$$


because $b\equiv-2\pmod p$.

The exterior block is $R_{2n}$ modulo $p$, with inverse $T_{2n}$. Since $p\mid2n$, the unit-order exterior solution is again


$$
v_0=1,\qquad v_1=-1.
$$



The unit-order contact sector is


$$
-\binom{-2n}{b-j}+\binom{-2n}{b+1-j}.
$$


Its reconstructed interior sector is


$$
W_j\left[
\binom{-2n}{b-j}
-(j+1)\binom{-2n}{b+1-j}
+j\binom{-2n}{b+2-j}
\right].
\tag{9.1}
$$



Every positive-order coefficient receives the three uniform physical events and its explicit factor $p$.

For the first two terms in (9.1),


$$
(n+2)\bmod p^2=205,\qquad
(2n-1)\bmod p^2=405,
$$




$$
b\bmod p^2=839,\qquad (b+1)\bmod p^2=840.
$$


If the weight does not borrow in those two digits, the lower index is at least $634$, so adding $405$ forces a carry.

For the last term, absence of a digit-zero event forces its lower digit to be zero and then $j\equiv0\pmod p$. The row factor $j$ supplies the fourth factor $p$.

Finally, the physical terminal is


$$
Y_b=W_b(b\psi_{b-1}+1).
$$


The actual finite contact solution is integral, and the retained original digits give $v_p(W_b)\ge6$. Thus $Y_b\in p^6\mathbb Z_p$.

We have proved, for the actual complete force,


$$
\boxed{
u\equiv2\pmod{p^3}
\Longrightarrow Y\in p^4\mathbb Z_p^{b+1}.
}
\tag{9.2}
$$



---

## 10. Zero-interface split, complete corrections, and both cutoffs

Put


$$
G=Y/p^4,\qquad Q=pG.
$$



For a term entering $G\bmod p$, coefficient order, row-factor valuation, and low-block event count have total one after the three uniform physical events are removed.

The fourth-event argument above places a unit-sector event in the first two low digits, unless the row factor supplies the factor $p$. Therefore a contributing leading term cannot leave an outgoing weight borrow or addition carry at the end of the three-digit block.

An outgoing lower-index borrow is also impossible. The relevant bounds are


$$
\ell\le20389,\qquad K_{\rm low}\le8004-a,
$$


so


$$
\ell+K_{\rm low}\le28393-a.
$$


For the second-column shifts an outgoing lower borrow would require at least


$$
D+5044+v\ge29433.
$$


For the first column, the previously audited lower bound is $29083$. Both are impossible.

Thus both leading normalized columns enter the common upper problem through interface $000$.

At the next order, both complete columns have the same eight-interface form. For $j=\ell+DJ<b$,


$$
\begin{aligned}
F_j&\equiv(-1)^{b-\ell-J}
\left[
(\widetilde a_\ell+pJb_\ell)K(J)
+p\sum_s c_{\ell,s}K_s(J)
\right],\\
G_j&\equiv(-1)^{b-\ell-J}
\left[
(\widetilde g_\ell+pJd_\ell)K(J)
+p\sum_s e_{\ell,s}K_s(J)
\right]
\pmod{p^2}.
\end{aligned}
\tag{10.1}
$$


All coefficients here are the complete actual coefficients, including finite returns.

The original interior ranges are still


$$
0\le J\le
\begin{cases}
B,&\ell<5044,\\
B-1,&\ell\ge5044.
\end{cases}
\tag{10.2}
$$



The retained radical gives


$$
\sum_JR(J_0)K(J)^2=0\pmod p
$$


for every $R:\mathbb F_p\to\mathbb F_p$, and


$$
\sum_JK(J)K_s(J)=0\pmod p
$$


for all eight interfaces.

Consequently, multiplying the **complete** two expressions in (10.1) eliminates every first-order cross-interface and row-lift term:


$$
\boxed{
F^TG\equiv
\left(\sum_\ell\widetilde a_\ell\widetilde g_\ell\right)
\sum_{J=0}^{B}K(J)^2
\pmod{p^2}.
}
\tag{10.3}
$$



Completing the two cutoff branches is legitimate because $K(B)\in p\mathbb Z_p$:

- the leading endpoint square is zero modulo $p^2$;
- the cross-interface endpoint products carry the displayed additional $p$;
- the actual physical coordinates satisfy $F_b,G_b\in p^2\mathbb Z_p$ and are handled separately.

No continued contact value at $j=b$ has been inserted.

---

## 11. The actual mixed consequence

Let


$$
\mathscr L_{FG}=\sum_\ell a_\ell g_\ell\pmod p.
$$


The completed universal calculation gives


$$
\frac{\sum_JK(J)^2}{p}
=
17\,\mathcal H(t)\pmod p.
$$


Therefore


$$
\boxed{
F^TQ
\equiv
p^2\,17\,\mathscr L_{FG}\mathcal H(t)
\pmod{p^3}.
}
\tag{11.1}
$$



The accepted original-tail certificate has actual terminal acceptance and gives


$$
\mathcal H(t)=0\pmod p
$$


for every continuation on $u\equiv2\pmod{p^9}$. Hence:

### Theorem 11.1 — Actual complete fixed-layer mixed zero

For every original $u\ge0$ with


$$
u\equiv2\pmod{29^9},
$$




$$
\boxed{
Y\in29^4\mathbb Z_{29}^{b+1},
\qquad
F^TQ\equiv0\pmod{29^3}.
}
\tag{11.2}
$$



This is no longer conditional on $\mathbf{EF}_6$.

It does not evaluate $\mathscr L_{FG}$, and it does not reach the norm-relative target


$$
F^TQ-p^2\rho_nF^TF
\equiv0\pmod{p^{d-5}}.
\tag{11.3}
$$


On the reviewed cylinder the required modulus is at least $p^5$, not $p^3$.

---

# Part IV. A new growing-depth complete-force theorem

## 12. A stronger symbol valuation

The earlier $57v$ estimate is valid but not sharp for the actual $n$, which is divisible by $p$.

Since


$$
\phi(z)^{-n}\equiv\phi(z^p)^{-n/p}\pmod p,
$$


its coefficient of $z^s$ is divisible by $p$ whenever $p\nmid s$. Combining this with the factorial in $c_s(n)$ gives


$$
\boxed{
v_p(c_s(n))\ge\left\lceil\frac{s}{p}\right\rceil
\qquad(s\ge1).
}
\tag{12.1}
$$



Indeed:

- if $p\mid s$, $v_p(s!)\ge s/p$;
- if $p\nmid s$, $v_p(s!)\ge\lfloor s/p\rfloor$, and Frobenius supplies one more factor $p$.

Thus a symbol coefficient of valuation $v$ has lower displacement at most $pv$, strengthening—but not invalidating—the retained $57v$ bound.

---

## 13. The exterior inverse preserves the actual factorial filtration

Because $b\equiv p-2\pmod p$, define


$$
w(h)=\left\lfloor\frac{h+p-2}{p}\right\rfloor.
$$


The actual exterior data satisfy


$$
\boxed{v_p(z_h)\ge w(h).}
\tag{13.1}
$$



Consider the closed lattice of exterior sequences


$$
\mathscr X=
\{a=(a_h)_{h\ge0}:v_p(a_h)\ge w(h)\}.
$$



### Lemma 13.1 — Filtration preservation

The operators $(\mathcal C_\infty)_{EE}$, its zeroth-order inverse $T_{2n}$, and the inverse $(\mathcal C_\infty)_{EE}^{-1}$ preserve $\mathscr X$.

#### Proof

A contribution from symbol index $s$ has lower displacement at most $s$. If its output index is $h$ and input index is $k$, then $h\le k+s$. Hence


$$
w(h)-w(k)\le\left\lceil\frac{s}{p}\right\rceil.
$$


Equation (12.1) pays this entire increase.

Upper-triangular factors do not increase the required weight, since $h\le k$ implies $w(h)\le w(k)$.

Write


$$
(\mathcal C_\infty)_{EE}=R_{2n}+E,
\qquad E\in pM(\mathbb Z_p).
$$


Then


$$
(\mathcal C_\infty)_{EE}^{-1}
=
\sum_{r\ge0}(-T_{2n}E)^rT_{2n}.
$$


Every factor preserves $\mathscr X$, and the series converges $p$-adically. Since $\mathscr X$ is closed, the inverse preserves it. ∎

For the actual solution of (6.4), this proves


$$
\boxed{v_p(v_h)\ge w(h).}
\tag{13.2}
$$



The significance is that the finite returns do **not** destroy the factorial decay of the actual exterior data.

---

## 14. An explicit finite solve at arbitrary precision

For $K\ge1$, put


$$
m_K=p(K-1),\qquad r_K=p(K-1)+1.
\tag{14.1}
$$



By (12.1), symbol indices $s>m_K$ are zero modulo $p^K$. By (13.2), exterior indices $h>r_K$ are zero modulo $p^K$.

Therefore the actual exterior solution modulo $p^K$ is obtained from the finite system


$$
\boxed{
\sum_{k=0}^{r_K}
C^{[K]}_{hk}v_k^{[K]}
\equiv z_h\pmod{p^K},
\qquad 0\le h\le r_K,
}
\tag{14.2}
$$


where


$$
C^{[K]}_{hk}
=
\sum_{s=0}^{m_K}c_s(n)
\sum_{a=0}^{s}
\binom{b+h}{s-a}\binom{-n}{a}
\binom{-2n-a}{k+s-a-h}.
\tag{14.3}
$$



Modulo $p$, this is the upper-unipotent $R_{2n}$ block. Thus the solve uses only a unit inverse.

The omitted actual exterior entries already lie in $p^K$. Their contribution to every retained equation is therefore zero modulo $p^K$; no unproved terminal condition is being imposed on (14.2).

The resulting contact response is


$$
\boxed{
\begin{aligned}
\theta_{j}^{(e,[K])}
=-\sum_{h=0}^{r_K}\sum_{s=0}^{m_K}\sum_{a=0}^{s}
&v_h^{[K]}c_s(n)
\binom j{s-a}\binom{-n}{a}\\
&\times\binom{-2n-a}{b+h+s-a-j},
\qquad 0\le j<b.
\end{aligned}
}
\tag{14.4}
$$


It satisfies


$$
\theta^{(e,[K])}\equiv A^{-1}A_{IE}z\pmod{p^K}.
\tag{14.5}
$$



### 14.1 The actual atom support is smaller still

A term in (14.4) can survive only if


$$
w(h)+\left\lceil\frac{s}{p}\right\rceil<K.
$$


Since


$$
h\le pw(h)+1,
$$


this implies


$$
h+s\le p(K-1)+1=r_K.
$$


Thus, after reconstruction,


$$
\boxed{
0\le a\le p(K-1),\qquad
0\le v\le p(K-1)+2,
}
\tag{14.6}
$$


with row-binomial indices at most $p(K-1)+1$.

At $K=6$, this gives


$$
m_6=145,\qquad r_6=146,
$$


and reconstructed shifts at most $147$.

The earlier $H_6=458$ and shift bound $632$ are therefore valid safe envelopes. No accepted calculation using those envelopes needs to be rerun.

At growing $K$, however, (14.4) must use the **actual shifted factorial arguments**. The special fixed-digit $p^3$-forcing proof is not silently extended beyond its shift guard.

---

## 15. Complete logarithmic retention at growing depth

Equation (5.1) gives the stronger row estimate


$$
v_p(r_i^{(F)})
\ge N_{\log}+v_p((n+i)!/n!)
\ge N_{\log}+\lfloor i/p\rfloor.
\tag{15.1}
$$



Consequently, at precision $p^K$, the logarithmic force may be replaced by its actual head of length


$$
\boxed{
L_{\log}(K)
=
\min\!\left(b,\ p\max\{K-N_{\log},0\}\right).
}
\tag{15.2}
$$



This has two cases:

- If $K\le N_{\log}$, the entire logarithmic force is zero modulo $p^K$.
- If $K>N_{\log}$, the first $L_{\log}(K)$ actual logarithmic entries are retained; the remaining rows are paid by (15.1).

The finite contact matrix remains $b\times b$. This is a proved input truncation, not a reduction of the original matrix boundary.

Let $r^{(F,[K])}$ denote that actual truncated head, and define


$$
\boxed{
Y^{[K]}
=
\mathcal R\theta^{(e,[K])}
+W_be_b
+\mathcal RA^{-1}r^{(F,[K])}.
}
\tag{15.3}
$$


Then


$$
\boxed{Y-Y^{[K]}\in p^K\mathbb Z_p^{b+1}.}
\tag{15.4}
$$



This is a complete-force approximation: exponential source, logarithmic source, finite returns, and physical terminal are all accounted for.

---

## 16. A genuine norm-relative paid-tail theorem

### Theorem 16.1 — Complete-force separation at the actual primitive depth

For any original index, let


$$
Z_w=p^{c+2}x,\qquad \nu=v_p(x^Tx),\qquad d=2c+4+\nu,
$$


and choose the **actual**


$$
K=d-c=c+4+\nu.
\tag{16.1}
$$



Construct $Y^{[K]}$ by (14.2)–(15.3). Then


$$
\boxed{
Z_w^T(Y-Y^{[K]})\in p^{d+2}\mathbb Z_p.
}
\tag{16.2}
$$


In particular,


$$
\boxed{
Z_w^TY-p\rho_nZ_w^TZ_w
\equiv
Z_w^TY^{[K]}-p\rho_nZ_w^TZ_w
\pmod{p^{d+2}}.
}
\tag{16.3}
$$



Equivalently, the exact local alignment question is


$$
\boxed{
x^TY^{[K]}-p^{c+3}\rho_nx^Tx
\equiv0\pmod{p^{d-c}}.
}
\tag{16.4}
$$



#### Proof

Equation (15.4) gives a column error in $p^K$. Every coordinate of $Z_w$ is divisible by $p^{c+2}$. Therefore


$$
v_p\!\left(Z_w^T(Y-Y^{[K]})\right)
\ge c+2+K=d+2.
$$


The remaining statements follow by substitution and exact division by $p^{c+2}$. ∎

This theorem is not a generic adjoint identity. It proves that a specific omitted part of the **actual complete force** cannot affect the norm-relative observable, and gives an explicit finite exterior solve and logarithmic head that suffice.

It also does not assume $N_{\log}\ge d-c$: when that inequality is unavailable, the required logarithmic head remains present.

---

## 17. Infinite original subsequence and precise scope of the advance

Reuse the accepted theorem that $c$ is unbounded in every original arithmetic progression.

Within


$$
u\equiv2\pmod{p^9},
$$


choose an increasing sequence $u_r$ with $c(u_r)\ge r$. Such a sequence exists: a finite set of original indices has bounded finite content.

Then


$$
K_r=d(u_r)-c(u_r)
=c(u_r)+4+\nu(u_r)\longrightarrow\infty.
$$



Theorem 16.1 applies to this infinite original subsequence with:

- exterior length $p(K_r-1)+2$;
- actual, possibly growing logarithmic head (15.2);
- complete finite contact inversion;
- the separate physical terminal;
- norm-relative error already paid.

Thus a growing-content, norm-relative complete-force theorem has been obtained on an infinite original subsequence.

What has **not** been proved is the vanishing of the retained expression (16.4). Nor has $c(u_r)$, $\nu(u_r)$, or a first primitive mixed digit been evaluated.

This distinction is essential. The new result removes the uncontrolled exterior tail from the true relative problem; it does not turn a retained finite contraction into zero by definition.

---

# Part V. Remaining bottleneck and exact arithmetic

## 18. What is now closed, and what remains open

The former all-row interface obstruction is closed. It must not be relabeled as a new hypothesis.

The actual fixed-layer result is also closed:


$$
F^TQ\equiv0\pmod{p^3}
\quad\text{on }u\equiv2\pmod{p^9}.
$$



The exact remaining local bottleneck is now:

> Evaluate the retained primitive contraction in (16.4), with the independently supplied $\rho_n$, at $K=d-c$, and prove its vanishing or obtain an actual original-domain nonzero value.

The first unresolved fixed correction is the coefficient of $p^3$ in $F^TQ$ after the ordinary-tail zero. At the following relevant orders, the complete mixed value must be compared with the complete norm term. These questions require paid unit corrections and actual coefficient data beyond the ordinary radical.

The theorem above does not reduce the required precision to a function of the lower bound $d\ge10$. The retained sufficient budgets remain


$$
\boxed{K_Z^{\rm norm}\ge d-c-1,}
$$




$$
\boxed{
K_Z^{\rm mixed}\ge d-1,\qquad
K_Y^{\rm mixed}\ge d-c.
}
$$


Logarithmic deletion still requires $N_{\log}\ge d-c$; otherwise (15.2) specifies what must remain.

---

## 19. Bounded exact arithmetic: what is and is not needed

No new arithmetic is needed to establish:

- the recurrence/source identification;
- the promoted fixed-layer mixed zero;
- the exterior filtration theorem;
- the norm-relative paid-tail theorem.

These are proved above. No accepted bounded producer should be rerun.

A future **actual primitive certificate**, once its original index and true depth have been supplied, has the following exact inputs and output.

### Inputs

1. An original $u$, not an auxiliary $b$.
2. The actual $c,\nu$, hence $K=d-c$.
3. The actual primitive first column data needed at the retained precision.
4. The independent $\rho_n$.
5. The symbols $c_s(n)$ for $0\le s\le p(K-1)$.
6. The actual exterior data $z_h=(b+h)!/b!$ for
   

$$
0\le h\le p(K-1)+1.
$$


7. The logarithmic head in (15.2), unless its whole omission is paid.
8. The original finite cutoff and the separate terminal.

All small factorial divisions must be performed with their demonstrated valuation removed before unit inversion.

### Expected verifiable output

The calculation should return


$$
\boxed{
x^TY^{[K]}-p^{c+3}\rho_nx^Tx
\pmod{p^K},
}
\tag{19.1}
$$


with the separate contributions of:

- the retained interior exponential response;
- the logarithmic response, if present;
- the physical terminal.

A nonzero result is an actual local obstruction at that index. A zero result proves only that index unless accompanied by a proved all-continuation or infinite-subsequence argument.

The current packet does not supply the needed actual primitive-depth inputs. Accordingly, (19.1) is an unevaluated certificate specification, not a claimed computation.

---

# Part VI. Global arithmetic and proof status

## 20. Row contents, least clearer, final gcd, and whole error

None of the physical $p$-adic normalizations above changes a row content, the row metric, or the least simultaneous two-column clearer.

Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,
\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),
\qquad
q_n=\frac{A_B}{g_B},
\qquad
p_n=\frac{H_B}{g_B}.
$$



The gcd is over **all primes**. The actual primitive multiplier remains


$$
d_B^2/g_B,
$$


and


$$
\log q_n
=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
$$



For the same original index,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


so the relevant whole evaluated error is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$



At the retained scope of the signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$



No result here bounds the actual all-prime $q_n$ strongly enough to make this whole nonzero same-index expression tend to zero.

---

## 21. Proof-status ledger

| Statement | Status |
|---|---|
| $\Xi=17$, with complete $220/242$ and $231$ supports and paid divisions | Reused completed finite calculation |
| Finite $T_n,R_n$ conversion and actual reconstruction convention | Verified |
| Complete exterior-force identity on every contact row | Proved from the recovered source |
| Explicit recurrence, positive source sign, and all rows $1,\ldots,b-2$ | Proved |
| Homogeneity of the complete logarithmic contribution on source rows | Proved |
| Full inverse is for $\mathsf P_-A_{\rm ext}$; finite-boundary transfer to $A$ | Verified |
| $57v$, $H_6=458$, and safe shifts through $632$ | Verified |
| Uniform physical forcing for both columns | Verified at the stated shift guards |
| Actual $Y\in p^4$ on $u\equiv2\pmod{p^3}$ | Proved |
| Actual $F^TQ\equiv0\pmod{p^3}$ on $u\equiv2\pmod{p^9}$ | Proved using the retained complete radical and tail theorem |
| Strong symbol bound $v_p(c_s)\ge\lceil s/p\rceil$ | Proved |
| Actual exterior factorial filtration preserved by the inverse | Proved |
| Growing-depth finite exterior solve and paid logarithmic head | Proved |
| Norm-relative complete-force tail separation at $K=d-c$ | Proved |
| Application on an infinite original subsequence with $c\to\infty$ | Proved existence and theorem application |
| Retained primitive mixed contraction vanishes | Open |
| Actual first nonzero primitive norm or mixed digit | Not evaluated |
| All-prime denominator versus whole same-index error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The recovered all-row source does more than supply the two missing initial charges. It yields an exact exterior-force identity, and the explicit recurrence calculation proves that it has the correct complete source on every row $1,\ldots,b-2$.

After the finite inverse, shift, saturation, and terminal audits, Turn 13’s conditional mixed statement is promoted to the actual theorem


$$
\boxed{
u\equiv2\pmod{29^9}
\Longrightarrow F^TQ\equiv0\pmod{29^3}.
}
$$



The new beyond-fixed-layer result is the factorial-filtration theorem for the actual exterior inverse. It gives a growing finite complete-force replacement at the true precision $K=d-c$, with


$$
\boxed{
Z_w^T(Y-Y^{[d-c]})\equiv0\pmod{29^{d+2}}.
}
$$


It retains the logarithmic force whenever its relative omission has not been paid, and it applies along an infinite original subsequence of growing content.

The exact remaining local bottleneck is the value of the retained primitive expression


$$
\boxed{
x^TY^{[d-c]}-29^{c+3}\rho_nx^Tx
\pmod{29^{d-c}}.
}
$$


Neither $\Xi\ne0$ nor the fixed-layer mixed zero evaluates this expression.

Finally, the least simultaneous clearer, all-prime final gcd, actual primitive denominator, and whole nonzero same-index error remain unchanged. Their required infinite-family comparison is still absent. Therefore an unconditional proof or disproof of irrationality of $e+\pi$ remains unresolved.
