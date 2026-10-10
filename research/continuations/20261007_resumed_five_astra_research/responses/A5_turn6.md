> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 6 — The complete next binary digit, a sharp content-one criterion, and an evaluated source-parity theorem

## Abstract

The rationality or irrationality of $e+\pi$ remains unresolved.

This report evaluates the complete finite inverse modulo $8$ on the unchanged original family


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


The calculation includes the finite contact projections, the return terms, and every physical reconstruction row. It does not assume that the modulo-$4$ inverse remains valid after another division.

The principal new results are:

1. **An explicit inverse modulo $8$.** Every contact coordinate is given by at most three ordinary binomial coefficients; no original-length sum remains.

2. **A necessary and sufficient criterion for actual content one.** Writing
   

$$
h=\frac n2,\qquad d=\frac{b-1}{4},\qquad g=\frac{h+1}{2},
$$


   one has
   

$$
\boxed{
   a=1
   \iff
   \exists\,s\in[0,d],\ s\text{ even}:
   v_2\binom gs+
   v_2\binom{h+d-s}{d-s}=1.
   }
$$


   This criterion covers **all** physical rows, not merely the previously evaluated even-row witness family.

3. **A paid source-parity theorem.** For the complete exponential source, including its exterior factorial prefix and finite returns,
   

$$
\boxed{\tau\in8\mathbb Z_2^{b+1},\qquad E\in2\mathbb Z_2.}
$$


   Thus the first primitive exponential-source digit is evaluated: it is zero, independently of the still unknown actual content $a$.

4. **An evaluated norm consequence of the parent identity.**
   

$$
\boxed{\sum_{j=0}^{b}x_j\in4\mathbb Z_2,\qquad x^Tx\in8\mathbb Z_2.}
$$


   In particular,
   

$$
\boxed{a=1\Longrightarrow Q\equiv0\pmod2.}
$$



The remaining content question is now exact and finite-state, but is not settled here on the infinite original family. No original $a=1$ witness is claimed. A new, bounded, eight-state calculation at $u=0$ is specified below; unlike the previous cost calculation, its output decides the complete content-one question at that original index.

---

## 1. Original objects and proof scope

Throughout,


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


Contact indices are exactly $0\le i,j<b$. Physical reconstruction has exactly $0\le j\le b$.

Retain


$$
R=2^h\binom nh,\qquad
\Lambda=\frac{(n!)^2}{2^n},\qquad
\phi(z)=1-z+\frac{z^2}{2},
$$




$$
\lambda_s=s![z^s]\phi(z)^n,\qquad W_j=\binom{n+2}{j},
$$


and


$$
A_{ij}=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j}.
$$


The exact normalized force remains


$$
\mathfrak f_i=
\frac{(n+i)!}{n!R}
[t^n](1+2t+2t^2)^n(1+t)^i.
$$



For a contact vector $z$, put


$$
\Delta_jz=jz_{j-1}-z_j,\qquad z_{-1}=z_b=0,
$$




$$
(\mathcal Rz)_j=W_j\Delta_jz.
$$


The complete corrected columns are


$$
x=\frac12\mathcal RA^{-1}\mathfrak f,
\qquad
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$


In particular, the logarithmic force $h^F$ is not removed.

Write


$$
z^f=A^{-1}\mathfrak f,\qquad x=2^ax_0,
$$


where $a=\min_jv_2(x_j)$ is the **actual** content. Also retain


$$
z^k=A^{-1}k,\qquad
k=\frac{h^e-A(j!)_{0\le j<b}}{b!}.
$$



The complete raw forms are


$$
\mathcal U=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)^2
+b^2W_b^2(z^f_{b-1})^2,
\tag{1.1}
$$




$$
\mathcal V=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)(\Delta_jz^k)
+W_b^2bz^f_{b-1}(bz^k_{b-1}+1),
\tag{1.2}
$$


with


$$
Q=2^{-2a-2}\mathcal U=x_0^Tx_0,\qquad
E=2^{-a-3}\mathcal V.
\tag{1.3}
$$



### 1.1 Results reused, not recalculated

The following are reused at their proved scope:

- the whole original force modulo $8$,
  

$$
\mathfrak f\equiv(2,1,3,1,4,4,0,\ldots)^T\pmod8;
  \tag{1.4}
$$


- the finite modulo-$4$ inverse and the all-original Lucas-mask rejection;
- the resulting universal bound $a\ge1$;
- the corrected higher-precision evaluator and completed-boundary theorem, subject to their stated precision hypotheses;
- the integral torsion description of the terminal derivative quotient.

The new parent certificate gives, for $u=0,\ldots,20$, upper bounds on $a$ from one evaluated row family. Its costs are not sharp contents. In particular, the certificate gives


$$
1\le a(0)\le10.
\tag{1.5}
$$


Its 41 auxiliary comparisons establish only those finite comparisons. No closed calculation from that certificate is repeated below.

Useful original congruences are


$$
b\equiv209\pmod{256},\qquad
d\equiv52\pmod{64},\qquad
h\equiv33\pmod{128},
\tag{1.6}
$$




$$
g\equiv81\pmod{128},\qquad n\equiv2\pmod{64}.
\tag{1.7}
$$



---

## 2. The complete finite inverse modulo $8$

Use divided powers $z^{[j]}=z^j/j!$, and let


$$
D=\partial_z,\qquad U_\gamma=(1+D)^\gamma.
$$


Let $\pi$ restrict to the $b$ contact coordinates and $\iota$ zero-pad them. These projections remain part of every finite operator.

The established factorization is


$$
A=P_bM_b,\qquad
M_b=\pi U_nH_{\phi^n}U_n\iota.
\tag{2.1}
$$



### 2.1 The symbol modulo $8$

Exactly,


$$
\phi^2=1+2\eta,\qquad
\eta=-z^{[1]}+2z^{[2]}-3z^{[3]}+3z^{[4]}.
\tag{2.2}
$$


Every positive-degree integral divided-power polynomial has an even square: cross terms have a factor $2$, and
$\binom{2r}{r}$ is even for $r\ge1$. Thus $\eta^2$ is even, and


$$
\phi^4\equiv1+4\eta\pmod8,\qquad
\phi^8\equiv1\pmod8.
$$


Since $n\equiv2\pmod8$,


$$
H_{\phi^n}\equiv1+2H_\eta\pmod8.
\tag{2.3}
$$



Define the full conjugated operator


$$
C=U_nH_\eta U_{-n}.
$$


The finite matrix therefore satisfies


$$
M_b=(1+2C_b)U_{2n}^{(b)}\pmod8,\qquad C_b=\pi C\iota.
\tag{2.4}
$$


Conjugation occurs **before** contact restriction, so this includes paths leaving the contact range under multiplication and returning under $U_n$.

The divided-power Leibniz rule gives


$$
C=\sum_{r=0}^{4}\binom nr H_{\eta^{(r)}}U_{-r}.
$$


Using $n\equiv2\pmod{64}$,


$$
\boxed{
C\equiv H_\eta+2H_{\eta'}U_{-1}+H_{\eta''}U_{-2}\pmod4.
}
\tag{2.5}
$$


Consequently,


$$
\boxed{
z^f=
U_{-2n}^{(b)}
\bigl(q-2C_bq+4C_b^2q\bigr)\pmod8,
\qquad q=P_b^{-1}\mathfrak f.
}
\tag{2.6}
$$



The quadratic term is not omitted without proof.

### 2.2 Evaluation of the finite correction

From (1.4),


$$
q_i=(-1)^i\left(
2-i+3\binom i2-\binom i3
+4\binom i4-4\binom i5
\right)\pmod8.
\tag{2.7}
$$


For computing $C_bq\pmod4$, only the first four terms are needed.

Put $B=b-1=4d$. Finite summation gives, for $0\le i\le B$,


$$
(U_{-1}^{(b)}q)_i
=
(-1)^i\left(
2-2i+\binom i2-3\binom i3+\binom i4
\right)\pmod4,
\tag{2.8}
$$




$$
(U_{-2}^{(b)}q)_i
=
(-1)^i\left(
2-2i+2\binom i2-\binom i3
+3\binom i4-\binom i5
\right)\pmod4.
\tag{2.9}
$$



Here the constants come from the actual upper endpoint $B$. For example,


$$
\sum_{k=0}^{B}
\left(2-k+3\binom k2-\binom k3\right)
=
2b-\binom b2+3\binom b3-\binom b4
\equiv2\pmod4.
$$


Likewise, the weighted total needed for (2.9) is $2(1-i)\pmod4$.
These follow from $b\equiv17\pmod{32}$; they are not infinite-tail substitutions.

It is convenient to record the finite polynomial calculation in exponential-generating form. Modulo $4$, the sequences in (2.7)–(2.9) have, on the contact range, the forms $e^{-z}$ times divided-power polynomials with coefficient lists


$$
[2,1,3,1],\quad
[2,2,1,3,1],\quad
[2,2,2,1,3,1],
$$


respectively. Substitution into (2.5) yields


$$
C_bq=e^{-z}[0,0,2,3,2,0,2,2]\pmod4
\tag{2.10}
$$


on the contact coordinates. In this notation the list records divided-power coefficients.

The return responsible for $C_b^2q$ can also be evaluated completely. Modulo $2$,


$$
C=H_\gamma+H_{\gamma''}U_{-2},
\qquad
\gamma=z^{[1]}+z^{[3]}+z^{[4]}.
\tag{2.11}
$$


The contact sequence $q\pmod2$ is $0,1,1,1$, periodically. Directly at the four possible exterior positions $b,\ldots,b+3$,


$$
(1-\iota\pi)C\iota q=0\pmod2.
\tag{2.12}
$$


Indeed, the endpoint input is $q_{4d}=0$, and the remaining possible multiplication coefficients contain either that input or $\binom{4d+r}{4}\equiv d\equiv0\pmod2$.

Moreover,


$$
C^2=U_nH_{\eta^2}U_{-n}\equiv0\pmod2.
$$


Together with (2.12), this proves


$$
\boxed{C_b^2q=0\pmod2.}
\tag{2.13}
$$



Thus all finite corrections in (2.6) have been evaluated:


$$
\boxed{z^f=U_{-2n}^{(b)}w\pmod8,}
\tag{2.14}
$$


where $w=q-2C_bq$ has exponential-generating polynomial


$$
e^{-z}[2,1,7,3,0,4,4,4].
$$


Equivalently,


$$
\boxed{
w_{4s}=2+2s,\qquad
w_{4s+2}=7-2s,\qquad
w_{2s+1}=-1\pmod8.
}
\tag{2.15}
$$



This is the new finite inverse reduction. It includes the complete transformed force and its finite returns.

---

## 3. Closed binomial formulas for every inverse coordinate

Define, for $r\ge0$,


$$
B_r=\binom{h+r}{r},\qquad
C_r=\binom{h+r}{r-1},\qquad
D_r=\binom{h+r}{r-2},
\tag{3.1}
$$


with negative lower indices interpreted as zero.

### Theorem 3.1 — Complete original inverse modulo $8$

For $0\le s\le d$, with $r=d-s$,


$$
\boxed{
z^f_{4s}\equiv(-1)^r(2B_r-4C_r)\pmod8.
}
\tag{3.2}
$$


For $0\le s<d$, with $r=d-s-1$,


$$
\boxed{
z^f_{4s+1}\equiv(-1)^r(B_r-4C_r+4D_r)\pmod8,
}
\tag{3.3}
$$




$$
\boxed{
z^f_{4s+2}\equiv(-1)^r(B_r+4D_r)\pmod8,
}
\tag{3.4}
$$




$$
\boxed{
z^f_{4s+3}\equiv-(-1)^r(B_r-4C_r+4D_r)\pmod8.
}
\tag{3.5}
$$



#### Proof

Reverse the contact coordinates about the physical endpoint $B=4d$. Since $d\equiv0\pmod4$, (2.15) gives the reverse generating series


$$
\sum_{r\ge0}w_{B-r}X^r
=
\frac{2-X+X^2-X^3}{1-X^4}
+\frac{2(X^2-1)X^4}{(1-X^4)^2}
\pmod8,
\tag{3.6}
$$


where the extension beyond the required prefix is used only for coefficient extraction through degree $B$.

Writing $Y=X^4$,


$$
(1+X)^{-4h}
\equiv
(1+Y)^{-h}
-(4X+6X^2+4X^3)(1+Y)^{-h-1}
+4Y(1+Y)^{-h-2}
\pmod8.
\tag{3.7}
$$


Multiplying (3.6) by (3.7), the four reverse residue classes are


$$
\begin{array}{c|c}
\text{reverse class}&\text{generating function in }Y\\ \hline
0&2(1+Y)^{-h}(1-Y)^{-1}\\
1&-(1+Y)^{1-h}(1-Y)^{-2}\\
2&(1+Y)^{1-h}(1-Y)^{-2}
 +4Y(1+Y)^{-h-1}(1-Y)^{-1}\\
3&(1+Y)^{1-h}(1-Y)^{-2}.
\end{array}
\tag{3.8}
$$



Finally,


$$
\frac1{1-Y}
\equiv
\frac1{1+Y}
+\frac{2Y}{(1+Y)^2}
+\frac{4Y^2}{(1+Y)^3}\pmod8,
$$


and


$$
\frac1{(1-Y)^2}
\equiv
\frac1{(1+Y)^2}
+\frac{4Y}{(1+Y)^3}
+\frac{4Y^2}{(1+Y)^4}\pmod8.
$$


Coefficient extraction gives (3.2)–(3.5). ∎

These are evaluated finite-inverse formulas, rather than an unevaluated original-length convolution.

### 3.1 All reconstructed differences

For later verification, the corresponding differences are also explicit. For $j=4s$, $r=d-s$,


$$
\boxed{
\Delta_{4s}z^f
\equiv(-1)^r\bigl(-(4s+2)B_r+4C_r\bigr)\pmod8.
}
\tag{3.9}
$$


For $j=4s+1,4s+2,4s+3$, put $r=d-s-1$ and


$$
J_r=\binom{h+r}{r+1}.
$$


Then


$$
\boxed{
\Delta_{4s+1}z^f
\equiv(-1)^r(B_r-2J_r-4D_r)\pmod8,
}
\tag{3.10}
$$




$$
\boxed{
\Delta_{4s+2}z^f
\equiv(-1)^r((4s+1)B_r+4D_r)\pmod8,
}
\tag{3.11}
$$




$$
\boxed{
\Delta_{4s+3}z^f
\equiv4(-1)^r((s+1)B_r-C_r)\pmod8.
}
\tag{3.12}
$$


At the actual physical terminal,


$$
z^f_{b-1}\equiv2\pmod8,\qquad
\boxed{\Delta_bz^f=bz^f_{b-1}\equiv2b\pmod8.}
\tag{3.13}
$$


The physical value remains $z_b^f=0$.

---

## 4. What the next digit says about actual content

The complete modulo-$8$ calculation reduces the content-one question to a precise binary optimization.

### Theorem 4.1 — Sharp criterion for $a=1$

On every original index,


$$
\boxed{
a=1
\iff
\exists\,s,\quad 0\le s\le d,\quad s\text{ even},\quad
v_2\binom gs+
v_2\binom{h+d-s}{d-s}=1.
}
\tag{4.1}
$$



#### Proof

A coordinate has valuation one exactly when


$$
v_2(W_j)+v_2(\Delta_jz^f)=2.
\tag{4.2}
$$



For $j=4s$,


$$
v_2(W_{4s})=v_2\binom gs.
\tag{4.3}
$$



Suppose first that $W_{4s}$ is odd. Then $s$ is a submask of $g$, so


$$
s\bmod64\in\{0,1,16,17\}.
$$


If $s$ is even, $r=d-s\equiv52$ or $36\pmod{64}$. Consequently:

- $B_r$ is even, because $h$ and $r$ share bit $5$;
- $C_r$ is even, because $h+1$ and $r-1$ share bit $1$.

Equation (3.9) therefore gives


$$
\Delta_{4s}z^f\equiv-2B_r\pmod8.
$$


Hence this row has valuation one in $x$ precisely when $v_2(B_r)=1$.

If $s$ is odd, then $r\equiv51$ or $35\pmod{64}$. Addition of $h$ and $r$ has carries at bits $0,1,5$, so $B_r$ is divisible by $8$. Again $C_r$ is even. Such a row cannot witness $a=1$.

Next suppose $v_2(W_{4s})=1$. Modulo $4$, (3.9) is $-2(-1)^rB_r$. It gives a content-one row precisely when $B_r$ is odd. Since $h$ is odd, this requires $r$, hence $s$, to be even.

If $v_2(W_{4s})=2$, the difference is already even; larger weight valuations cannot produce valuation one either. Thus the $4s$ rows give exactly (4.1).

It remains to exclude every other row. The exact weight valuations are


$$
v_2(W_{4s+2})=1+v_2\binom{g-1}{s},
\tag{4.4}
$$




$$
v_2(W_{4s+1})=v_2(W_{4s+3})
=2+v_2\binom{g-1}{s}.
\tag{4.5}
$$



- If $v_2(W_{4s+2})=1$, then $s\subseteq g-1$. Its low six bits are $0$ or $16$, and $r=d-s-1\equiv51$ or $35\pmod{64}$. Thus $B_r$ is divisible by $4$, and (3.11) gives $\Delta_{4s+2}z^f\equiv0\pmod4$.

- If $v_2(W_{4s+2})=2$, then $v_2\binom{g-1}{s}=1$. Because $v_2(g-1)=4$, an odd $s$ would create at least four borrows. Hence $s$ is even, $r$ is odd, and $B_r$ is even. The difference is therefore even.

- For $4s+1$, a weight of valuation two requires $s\subseteq g-1$, so $s$ is even and $r$ is odd. Equation (3.10) then gives an even difference.

- Equation (3.12) makes every $4s+3$ difference divisible by four.

Finally,


$$
v_2(W_b)=2+v_2\binom{g-1}{d}\ge3,
$$


since the low bits of $d$ are not a submask of those of $g-1$. The physical terminal cannot witness content one.

Together with the established $a\ge1$, this proves (4.1). ∎

### 4.1 Status of the universal assertion $a\ge2$

Theorem 4.1 does **not** prove that $a\ge2$ on the entire original family. It identifies the exact missing assertion:


$$
\boxed{
\forall u\ge0,\ \forall s\in[0,d]\text{ even}:\quad
v_2\binom gs+
v_2\binom{h+d-s}{d-s}\ge2.
}
\tag{4.6}
$$



Conversely, one original word and one even $s$ with total valuation one refutes the universal assertion and supplies the actual physical witness $j=4s$.

The parent certificate tests only the branch in which the second valuation is zero. It does not test the newly evaluated branch


$$
v_2\binom gs=0,\qquad
v_2\binom{h+d-s}{d-s}=1.
$$


It therefore cannot decide (4.6).

---

## 5. Complete exponential returns and the next source digit

A stronger source theorem can be proved without knowing the sharp content.

Define the complete physical source vector


$$
\tau_j=W_j\Delta_jz^k\quad(j<b),\qquad
\tau_b=W_b(bz^k_{b-1}+1).
\tag{5.1}
$$



### 5.1 The complete paid exterior source at modulus $8$

The factorial coefficients satisfy


$$
a_0=1,\qquad a_1=b+1\equiv2,\qquad
a_2=(b+1)(b+2)\equiv6\pmod8,
$$


while $a_t\equiv0\pmod8$ for $t\ge3$. Thus the complete source at this precision is


$$
s_{\rm ext}=e_b+2e_{b+1}+6e_{b+2}\pmod8.
\tag{5.2}
$$


No higher-precision claim is attached to this truncation.

Put $v=U_{2n}s_{\rm ext}$. Its exterior part is


$$
v_{\rm ext}=5e_b+2e_{b+1}+6e_{b+2}\pmod8.
\tag{5.3}
$$


Applying the finite inverse to the actual transformed source gives


$$
\begin{aligned}
z^k={}&-\pi U_{-2n}v_{\rm ext}
+2U_{-2n}^{(b)}\pi Cv_{\rm ext}\\
&-4U_{-2n}^{(b)}C_b\pi Cv_{\rm ext}
\pmod8.
\end{aligned}
\tag{5.4}
$$


The last two terms are retained finite returns.

Modulo $2$, $v_{\rm ext}=e_b$. Directly,


$$
(1-\iota\pi)Ce_b=e_{b+2}+e_{b+4}\pmod2.
$$


For either exterior odd index $m=b+2,b+4$, the contact part of $Ce_m$ is the same vector, supported on $j\equiv3\pmod4$. Since $C^2=0\pmod2$,


$$
C_b\pi Ce_b=0\pmod2.
\tag{5.5}
$$


Thus the quadratic source return in (5.4) has been evaluated and vanishes modulo $8$.

For $i<b$, finite exterior summation gives


$$
(U_{-1}v_{\rm ext})_i=-(-1)^i\pmod4,\qquad
(U_{-2}v_{\rm ext})_i=i(-1)^i\pmod4.
$$


The multiplication part $H_\eta v_{\rm ext}$ has no contact contribution. Therefore


$$
\pi Cv_{\rm ext}
=e^{-z}(-2\eta'-z\eta'')
=e^{-z}[2,2,0,1]\pmod4.
\tag{5.6}
$$


Equivalently,


$$
2(\pi Cv_{\rm ext})_i
=(-1)^i\left(4-4i-2\binom i3\right)\pmod8.
\tag{5.7}
$$



These formulas specify the whole finite source correction, not only its first exterior column.

### 5.2 Source coordinates needed for physical divisibility

Coefficient extraction from (5.4)–(5.7), using (3.7), gives


$$
\boxed{
z^k_{4s}\equiv
4\binom{h+d-s}{d-s}\pmod8.
}
\tag{5.8}
$$



For completeness, the short calculation behind this particular digit is as follows. The reverse correction sequence in (5.7) has class-zero and class-two generating functions $4/(1-Y)$. Multiplication by $U_{-2n}$ gives the class-zero correction


$$
4(1+Y)^{-h}(1-Y)^{-1}.
$$


The exterior terms in that class contribute


$$
4(1+Y)^{-h-1}+4(1+Y)^{-h-1}=0\pmod8.
$$


Reducing the remaining factor modulo $2$ gives (5.8).

Also, for $r=d-s-1$, put


$$
c_r=[Y^{r+1}](1+Y)^{-h}.
$$


The other source coordinates needed modulo $4$ are


$$
z^k_{4s+1}\equiv-c_r\pmod4,\qquad
z^k_{4s+2}\equiv-2c_r\pmod4.
\tag{5.9}
$$


Consequently,


$$
\boxed{\Delta_{4s+2}z^k\equiv0\pmod4.}
\tag{5.10}
$$


Equation (5.8) likewise gives


$$
\Delta_{4s}z^k\equiv0\pmod4.
\tag{5.11}
$$


The source parity is supported only on $j\equiv1\pmod4$, consistently with the previously established parity calculation.

### Theorem 5.1 — Complete physical source divisible by eight

On every original index,


$$
\boxed{\tau\in8\mathbb Z_2^{b+1}.}
\tag{5.12}
$$



#### Proof

If $W_j$ is odd, then $j=4s$ with $s\subseteq g$. The binomial in (5.8) is even by the already proved original mask obstruction. Hence $z^k_{4s}\equiv0\pmod8$. Moreover $z^k_{4s-1}$ is even, so


$$
\Delta_{4s}z^k\equiv0\pmod8.
$$



If $v_2(W_j)=1$, then $j$ is even. Equations (5.10)–(5.11) make its difference divisible by four.

If $v_2(W_j)=2$ and $j$ is even, source parity makes its difference even. For odd $j\equiv3\pmod4$, the difference is again even.

The remaining case is $j=4s+1$ with $v_2(W_j)=2$. Here $s\subseteq g-1$. The parity of $c_r$ is


$$
c_r\equiv\binom{h+r}{r+1}\pmod2.
$$


It vanishes because $h-1$ and


$$
r+1=d-s\equiv52\ \text{or }36\pmod{64}
$$


share bit $5$. Thus this difference is even as well.

At the physical terminal, $v_2(W_b)\ge3$, so the complete factor


$$
W_b(bz^k_{b-1}+1)
$$


is divisible by eight. ∎

### 5.3 Actual primitive payment

Since


$$
\mathcal Rz^f=2^{a+1}x_0,
\qquad
\mathcal V=(\mathcal Rz^f)^T\tau,
$$


the division is paid exactly:


$$
E=2^{-a-3}\mathcal V=x_0^T(\tau/4).
$$


Theorem 5.1 proves


$$
\boxed{E\in2\mathbb Z_2}
\tag{5.13}
$$


for the **actual** content $a$, not an assumed value or an upper bound.

An independently specified coefficient is therefore


$$
\boxed{r_0(u)=0,\qquad E-r_0(u)Q\equiv0\pmod2.}
\tag{5.14}
$$


This coefficient is justified by the actual source calculation, not by $E/Q$. It is only a depth-one zero-source law, not the sought nontrivial relative scalar law or a nonzero primitive digit.

For the full mixed column $y$, the corresponding conclusion requires that the original logarithmic guard protect this paid digit. Without that guard, the logarithmic contribution must be included explicitly; (5.13) is not silently promoted to a statement about $x_0^Ty$.

---

## 6. Evaluating the parent’s linear norm acceptance

The proposed identity is correct with the physical boundary $z_b=0$.

Indeed,


$$
(j+1)W_{j+1}=(n+2-j)W_j
$$


implies


$$
\sum_{j=0}^{b}(\mathcal Rz)_j
=\sum_{j=0}^{b-1}(n+1-j)W_jz_j.
$$


Thus, with


$$
S=\sum_{j=0}^{b-1}(n+1-j)W_jz^f_j,
$$


one has exactly


$$
\boxed{\sum_{j=0}^{b}x_j=S/2.}
\tag{6.1}
$$



The sum $S$ can be evaluated modulo $8$, rather than left as a named contact functional.

### 6.1 Evaluation of the adjoint contact functional

Let


$$
\ell_j=(n+1-j)W_j.
$$


From (2.14),


$$
S=\ell^TU_{-2n}^{(b)}w\pmod8.
$$


For coefficients through degree $B=b-1$,


$$
\sum_k(\ell^TU_{-2n}^{(b)})_kt^k
=(n+1-t)(1+t)^{1-n}.
\tag{6.2}
$$


The finite truncation is harmless here because a coefficient of index $k\le B$ uses only $\ell_0,\ldots,\ell_k$.

Write


$$
w_k=(-1)^k\sum_{r=0}^{7}t_r\binom kr,
\qquad
(t_0,\ldots,t_7)=(2,-1,7,-3,0,-4,4,-4).
\tag{6.3}
$$


Finite hockey-stick summation gives


$$
\sum_{k=0}^{B}
\binom kr\binom{n+k-2}{k}
=
\binom{n+r-2}{r}\binom{n+B-1}{B-r}.
\tag{6.4}
$$


For the second coefficient in (6.2), replacing $k$ by $k-1$ and using
$\binom kr=\binom{k-1}{r}+\binom{k-1}{r-1}$ gives two analogous terms.

For $r\le7$,


$$
\binom{n+r-2}{r}\equiv1\pmod8,
$$


and, for $r\ge1$,


$$
\binom{n+r-3}{r-1}\equiv1\pmod8.
$$


These reductions are paid: write $n-2=N$, with $64\mid N$, and use Vandermonde together with


$$
v_2\binom Nk\ge v_2(N)-v_2(k)\ge4
\quad(1\le k\le7).
$$



Putting $M=n+B-1$, equations (6.2)–(6.4) reduce the entire contact acceptance to


$$
S\equiv
4\left[
\binom M{B-1}+\binom M{B-2}+\binom M{B-3}
\right]
-2\binom{M-1}{B}\pmod8.
\tag{6.5}
$$


The first two binomials are even by their low two bits. The parity of the third is


$$
\binom{g+d-1}{d-1}\equiv0\pmod2,
$$


since its upper argument is even and its lower argument is odd.

Finally,


$$
\binom{M-1}{B}
=
\binom{4(g+d-1)}{4d}
\equiv\binom{g+d-1}{d}\pmod4.
$$


The last congruence follows by extracting multiples of four from


$$
(1+t)^{4A}\equiv
(1+t^4)^A+2At^2(1+t^4)^{A-1}\pmod4.
$$


Therefore


$$
\boxed{
S\equiv-2\binom{g+d-1}{d}\pmod8.
}
\tag{6.6}
$$



Addition of $g-1$ and $d$ has carries at bits $4$ and $5$, because


$$
g-1\equiv16,\qquad d\equiv52\pmod{64}.
$$


Thus the binomial in (6.6) is divisible by four, proving


$$
\boxed{S\equiv0\pmod8.}
\tag{6.7}
$$



### Theorem 6.1 — Evaluated norm consequence

On every original index,


$$
\boxed{\sum_jx_j\in4\mathbb Z_2,\qquad \mathcal N=x^Tx\in8\mathbb Z_2.}
\tag{6.8}
$$



Indeed $x/2$ is integral by the established $a\ge1$, and


$$
\sum_j(x_j/2)\equiv
\sum_j(x_j/2)^2\pmod2.
$$


Equation (6.7) makes the left side even.

After **actual** content division, the parent identity gives


$$
Q\equiv2^{-a-1}S\pmod2.
\tag{6.9}
$$


The available precision pays this division when $a=1$, yielding


$$
\boxed{a=1\Longrightarrow Q\equiv0\pmod2.}
\tag{6.10}
$$


When $a\ge2$, (6.7) does not determine primitive norm parity. Dividing a residue known only modulo $8$ by a larger power of two would be invalid.

This is precisely where the parent’s useful identity stops at the present precision.

---

## 7. A bounded new calculation that decides the complete next digit

No tools were used. The following calculation is new and is not a repetition of the parent’s even-row dynamic program.

### 7.1 Mathematical object

Define


$$
\nu(u)=
\min_{\substack{0\le s\le d\\s\ {\rm even}}}
\left[
v_2\binom gs+
v_2\binom{h+d-s}{d-s}
\right].
\tag{7.1}
$$


Theorem 4.1 proves


$$
\boxed{\nu(u)=1\iff a(u)=1,\qquad
\nu(u)\ge2\iff a(u)\ge2.}
\tag{7.2}
$$



The minimum has an explicit eight-state binary evaluation.

Introduce


$$
s+R=d,\qquad s+T_0=g.
$$


At bit $k$, choose digits $\sigma,\rho,\tau\in\{0,1\}$, with incoming carries


$$
(\alpha,\beta,\gamma)\in\{0,1\}^3.
$$


Require


$$
\sigma+\rho+\alpha=d_k+2\alpha',
$$




$$
\sigma+\tau+\beta=g_k+2\beta',
$$


and define $\gamma'$ by


$$
h_k+\rho+\gamma=\upsilon+2\gamma',
\qquad \upsilon\in\{0,1\}.
\tag{7.3}
$$


Impose $\sigma=0$ at bit zero. The transition cost is


$$
\beta'+\gamma'.
$$


Start and finish in state $(0,0,0)$, processing the entire words with enough zero padding to clear all carries.

Kummer’s theorem identifies the cost with


$$
v_2\binom gs+v_2\binom{h+R}{R}.
$$


This is an exact optimization over a new mathematical object: both valuation channels are charged. It is not a random mask search.

### 7.2 Bounded input

Use just the original index $u=0$:


$$
\begin{aligned}
b&=150094635296999121,\\
d&=37523658824249780,\\
h&=300339365229295241121,\\
g&=150169682614647620561.
\end{aligned}
$$


Seventy-two binary positions suffice. There are eight states and at most eight digit triples per state, so fewer than


$$
72\cdot8\cdot8=4608
$$


candidate transitions are required.

The old certificate already supplies $\nu(0)\le10$, because its cost-ten row has the second valuation zero. The proved modulo-$4$ obstruction gives $\nu(0)\ge1$.

### 7.3 Expected verifiable output

The coordinator should inspect:

1. the complete minimum-cost table over the 72 positions and eight states;
2. the minimum accepting cost $\nu(0)$;
3. an accepting predecessor path and its exact $s,R,T_0$;
4. the identities
   

$$
s+R=d,\qquad s+T_0=g,\qquad s\text{ even};
$$


5. the independent digit-sum checks
   

$$
v_2\binom gs=s_2(s)+s_2(g-s)-s_2(g),
$$


   

$$
v_2\binom{h+R}{R}
   =s_2(h)+s_2(R)-s_2(h+R).
$$



If $\nu(0)=1$, the output must additionally identify the actual row $j=4s$ and verify its valuation-one reconstruction using (3.9). This refutes universal $a\ge2$ by a fully specified original finite word.

If $\nu(0)\ge2$, the table certifies


$$
2\le a(0)\le10.
$$


It does not prove the corresponding assertion for any other original index.

---

## 8. Higher precision, logarithmic source, and actual arithmetic scale

The modulo-$8$ simplifications above must not replace the complete higher-precision assembly.

At raw precision $2^L$, retain


$$
I=\min(b-1,8L-2),\qquad m=4(L-1),
$$




$$
T=\min(2L-1,2n-1),\qquad V=T+m,
$$


and the proved scope condition


$$
\boxed{n>4(I+2m+T+4)+2.}
\tag{8.1}
$$


The complete exponential source remains


$$
k=\sum_{t=0}^{2n-1}\frac{(b+t)!}{b!}\mathbf a_{b+t},
$$


with the appropriately paid prefix at each precision.

Both completed return channels remain


$$
\eta_f=U_n^{(m)}KS^{-1}D_f,
$$




$$
\xi_v=
\sum_{t=0}^{T}a_t
\sum_{\substack{0\le r\le t\\0\le v-r\le m}}
\binom n{t-r}\lambda_{v-r}\binom{b+v}{v-r},
$$




$$
\delta=KS^{-1}G^{[V]}\xi-\xi,\qquad
\theta_v=\sum_{w=v}^{V}\binom n{w-v}\delta_w.
\tag{8.2}
$$


Here these are the established finite Schur-completion objects, not infinite-matrix replacements. Their completed identities retain


$$
\widehat z^f=\overline z^f,\qquad
\widehat z^k=\overline z^k-s\pmod{2^L}.
$$


The auxiliary value $\widehat z_b^k=-1$ is used only in completed-boundary cancellation; the physical value remains $z_b^k=0$.

Both differential boundaries $C_{b-1}+C_b$, both mixed terminal terms in (1.2), and the norm terminal in (1.1) remain present.

The logarithmic source retains


$$
\mathcal L_s=s![z^s]\frac{F(z)}{1-z},
\qquad
B_\star=n-v_2(b!)-1-2s_2(n)-\ell.
\tag{8.3}
$$


It may be suppressed only when this original bound protects the requested normalized observation after all divisions. The new exponential theorem does not extend that guard.

For an independently specified integral $r(u)$, the paid relative observation still is


$$
E-r(u)Q
=
2^{-2a-2}\bigl(2^{a-1}\mathcal V-r(u)\mathcal U\bigr),
\tag{8.4}
$$


because $a\ge1$. A primitive congruence of depth $K$ requires the actual $a$ and sufficient raw precision, for example


$$
L\ge2a+K+3.
\tag{8.5}
$$


Neither a characteristic-zero telescope nor a derivative-image identity permits unpaid binary division. The torsion-aware terminal certificate class is available, but no nontrivial source-derived $r(u)$ with an infinite-family higher-depth acceptance theorem is proved here.

### Scale assessment

The new source gain is one binary digit. The new norm gain is also a fixed low-precision gain. Even the existing endpoint bound


$$
a\le v_2\binom gd=O(\log n)
$$


allows only a polynomial-size factor $2^a$ in $n$.

These facts do not establish the exponentially scaled, all-prime denominator improvement and simultaneous error estimate that the global objective may require. Moreover, an extra power of two in a norm or a mixed observation is not automatically a denominator saving: the actual valuation difference and final gcd decide its direction and size.

---

## 9. Least simultaneous clearer, all-prime gcd, and whole error

No local content result changes the definitions of the producer’s integer pair.

Retain


$$
\omega_j=j!W_j,\qquad
u_j=\frac{2\Lambda R\,x_j}{\omega_j},\qquad
v_j=\frac{4b!\,y_j}{\omega_j},
$$


and the **actual least simultaneous clearer**


$$
\boxed{
d_B=\operatorname{lcm}_{0\le j\le b}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\}.
}
\tag{9.1}
$$


No reconstructed row content, and no uncomputed second-column content, is divided out.

With


$$
\mathcal N=x^Tx,\qquad \mathcal H=x^Ty,
$$


retain


$$
A_B=d_B^2\,4\Lambda^2R^2\mathcal N,\qquad
H_B=d_B^2\,8\Lambda Rb!\mathcal H,
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
\tag{9.2}
$$


This is the final gcd over **all primes**.

The primewise identity remains


$$
v_p(q_n)=
\max\left\{
v_p\!\left(\frac{\Lambda R}{2b!}\right)
+v_p(\mathcal N)-v_p(\mathcal H),0
\right\}.
\tag{9.3}
$$


The previously established original-family ternary law is retained at its stated scope:


$$
\boxed{v_3(q_n)=n-\frac{b+15}{2}.}
\tag{9.4}
$$


It is neither recalculated nor strengthened here.

Finally,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
\qquad
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{9.5}
$$


A producer-based irrationality proof still requires, on the **same infinitely many original indices**, a nonzero whole error and an estimate involving the actual primitive denominator. For example,


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0
$$


would suffice. None of the new binary statements proves that whole-error assertion.

---

## 10. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Parent’s costs at $u=0,\ldots,20$ | Finite upper bounds from the specified row family |
| Universal $a\ge1$, modulo-$4$ inverse, whole force modulo $8$ | Reused proved tools |
| Complete finite inverse modulo $8$, including returns | **Newly proved** |
| Formulas for every contact coordinate and physical difference | **Newly proved** |
| Criterion (4.1) covering all possible $a=1$ rows | **Newly proved** |
| Universal $a\ge2$, or an original $a=1$ witness | **Not settled** |
| Complete physical exponential source $\tau\in8\mathbb Z_2^{b+1}$ | **Newly proved** |
| Actual primitive exponential digit $E\equiv0\pmod2$ | **Newly proved** |
| Evaluated summed reconstruction and $\mathcal N\in8\mathbb Z_2$ | **Newly proved** |
| $a=1\Rightarrow Q$ even | **Newly proved conditional implication** |
| Nontrivial higher-depth $E-r(u)Q$ law | Open |
| Same-index primitive denominator versus nonzero whole error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

The next inverse digit has now been evaluated in the original finite objects. Its precise content obstruction is


$$
\min_{\substack{0\le s\le d\\s\ {\rm even}}}
\left[
v_2\binom gs+
v_2\binom{h+d-s}{d-s}
\right].
$$


The old certificate does not evaluate this minimum. The new eight-state calculation does, with fewer than 4,608 candidate transitions at the specified original word $u=0$.

Independently of that outstanding calculation, the source and norm acceptances have advanced beyond unchanged scalar definitions:


$$
\boxed{
E\equiv0\pmod2,\qquad
x^Tx\equiv0\pmod8,\qquad
a=1\Longrightarrow Q\equiv0\pmod2.
}
$$



These are rigorous paid binary results. They are not a proof of universal content two, a nonzero primitive scalar theorem, an all-prime denominator saving, or a conclusion about $e+\pi$. The global bottleneck remains the actual primitive denominator and the nonzero whole evaluated error on one and the same infinite original subfamily.
