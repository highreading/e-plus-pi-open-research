> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 12 — The recovered actual head, a complete $29^9$-norm factorization, and an original $29^{10}$-norm zero

## Executive assessment

The recovered head identification is valid in the required integral coordinates. It closes the hypothesis $\mathbf H$ from Turn 11 without a head-table calculation:



$$
f^0=J_0h^{[0]}+29h^{[1]},\qquad h^{[1]}\in\mathbb Z_{29}^{\,b}.
$$



The remainder is retained throughout this report. It is not zero, and it can contribute to the first nonzero normalized column.

After auditing the finite shifts, row factors, zero-interface split, and actual terminal reconstruction, I obtain the unconditional original-family conclusion


$$
\boxed{
u\equiv2\pmod{29^3}
\quad\Longrightarrow\quad
Z_w\in29^4\mathbb Z_{29}^{\,b+1},\qquad
Z_w^TZ_w\in29^9\mathbb Z_{29}.
}
$$



Thus **$c\ge2$ and $d\ge9$ are now unconditional on the original progression $u\equiv2\pmod{24389}$**.

There is also a new complete physical result beyond that closed radical. Write


$$
C=20916+29^3t,
$$


and retain the ordinary normalized tail


$$
\mathcal H(t)=
\sum_{r=0}^{t}
\binom{1716+2001t}{r}^{2}
\binom{3432+4002t+t-r}{t-r}^{2}\pmod{29}.
$$


I prove a factorization


$$
\boxed{
\frac{Z_w^TZ_w}{29^9}
=
\mathscr L\,\Xi\,\mathcal H(t)\pmod{29}.
}
\tag{E.1}
$$


Here:

* $\mathscr L$ is the complete low contraction of the actual normalized first column, including the actual first-order head, lower, and endpoint-return coefficients;
* $\Xi\in\mathbb F_{29}$ is a universal, explicitly specified bounded low-digit constant;
* the derivation includes the lift of $z_1^Tz_1$ and the complete cross term $2p\,z_1^Tz_2$;
* no second-lower, crossed-return, or higher-head term is deleted by lifting an earlier precision-specific elimination.

The newly completed six-digit normalized-tail certificate gives $\mathcal H(t)=0$ at original $u=2$, independently of every unread continuation. Consequently,


$$
\boxed{d\ge10\quad\text{at original }u=2.}
\tag{E.2}
$$


More generally, compatibility of the original principal-unit parametrization gives the realizable cylinder


$$
\boxed{
u\equiv2\pmod{29^9}
\quad\Longrightarrow\quad c\ge2,\qquad d\ge10.
}
\tag{E.3}
$$



No value of $\Xi$ or $\mathscr L$ is needed for these zeros. Their unevaluated values must not, however, be used to assert an exact content or a first nonzero primitive norm digit.

There is a decisive obstruction to one proposed alternative target: the accepted unbounded-content theorem in every original progression rules out a nonempty full original cylinder on which $c$ is a fixed finite integer. An all-depth interface, rather than a purported constant-content cylinder, is therefore the appropriate direction. I give such an exact factorial-strip interface below, with its scope and guards explicit.

The complete mixed-force alignment, actual all-prime denominator, and whole same-index error comparison remain unresolved. This report does not prove or disprove the irrationality of $e+\pi$.

---

## 1. Preserved problem and notation

Throughout,


$$
p=29,\qquad D=p^3,\qquad \Lambda=p^6,
$$




$$
\beta=410910916,\qquad
b=3^{249005515+574312172u}=\beta+\Lambda C,
\qquad n=2001b,\qquad u\ge0.
$$



The domains remain:

* contact coordinates: $0\le j<b$;
* source rows: $1\le i\le b-2$;
* reconstructed coordinates: $0\le j\le b$.

The corrected columns are


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,
\qquad W_j=\binom{n+2}{j}.
$$



The reconstruction is the finite one:


$$
(\mathcal Rx)_j=W_j(jx_{j-1}-x_j),
$$


where $x_{-1}=x_b=0$ is imposed for reconstruction. In particular,


$$
(\mathcal Rx)_b=bW_bx_{b-1}.
\tag{1.1}
$$


There is no term $-W_bx_b$ from an algebraically continued contact atom.

Retain


$$
P=\frac{Z_w}{p^2}=p^cx,\qquad Q=\frac{Y}{p^3},
$$


with $x$ primitive at $p$, and


$$
\nu=v_p(x^Tx),\qquad d=2c+4+\nu.
\tag{1.2}
$$



---

## 2. The recovered actual-head identity is valid

The exact first force is


$$
f_i^0=\frac{(n+i)!}{n!}J_i,\qquad
J_i=[t^n](1+2t+2t^2)^n(1+t)^i.
\tag{2.1}
$$



Since $2001=29\cdot69$, $p\mid n$. Frobenius gives


$$
(1+2t+2t^2)^n
\equiv
(1+2t^p+2t^{2p})^{n/p}\pmod p.
$$


For $0\le i<p$, the degree of $(1+t)^i$ is below $p$. Because $n$ is a multiple of $p$, only its constant term can contribute to the coefficient of $t^n$. Hence


$$
J_i\equiv J_0\pmod p\qquad(0\le i<p).
$$



Also,


$$
\frac{(n+i)!}{n!}=(n+1)\cdots(n+i)
\equiv i!\pmod p
$$


on that range. For $i\ge p$, the same integral product contains $n+p$, so it is divisible by $p$. Therefore


$$
\boxed{
f_i^0\equiv
\begin{cases}
J_0i!&0\le i<p,\\
0&i\ge p
\end{cases}
\pmod p.
}
\tag{2.2}
$$



The factor order is equally important. Turn 0 retains this $f^0$ as the input head and applies the integral $\mathsf P_-$ afterward. No divided-factorial change of coordinates intervenes in (2.2).

Choose the retained integral representatives of $h^{[0]}$. Then


$$
\boxed{f^0=J_0h^{[0]}+ph^{[1]},\qquad h^{[1]}\ \text{integral}.}
\tag{2.3}
$$


Neither $J_0$ nor $h^{[1]}$ is assumed to be a unit or zero.

At precision $p^6$, the original first-force truncation $f_i^0\equiv0\pmod{p^6}$ for $i\ge174$, and the larger retained head envelope, are compatible with this decomposition. Applying the finite integral normal form preserves the explicit $p$ multiplying $h^{[1]}$.

**Conclusion:** the recovered note proves precisely the interface needed in Turn 11. A head-table rerun would add no missing hypothesis.

---

## 3. Audit of the complete $p^4$-column saturation

### 3.1 Finite normal-form bounds

At output precision $p^6$, retain


$$
M=173,\qquad L=350.
$$


After the accepted finite-return consolidation, the first-column atoms are


$$
W_j\binom{-2n-a}{b+v-j},
\tag{3.1}
$$


with


$$
0\le a\le523,\qquad -350\le v\le346.
\tag{3.2}
$$



These are the consolidated first-column atoms. Intermediate $\sigma=1$ boundary atoms in Turn 0 must first be combined according to the finite endpoint identity; the following $2n$-digit argument is not an atomwise argument for those unconsolidated intermediate expressions.

All row factors remain integral integer-valued polynomials. Their binomial-basis indices, including reconstruction, are below $p^2=841$.

The endpoint solution remains the actual finite integral one:


$$
q\equiv
\sum_{\ell=0}^{5}(-G)^\ell K_\times\mathsf D\mathsf R_nw
\pmod{p^6},
\qquad G\in pM(\mathbb Z_p).
\tag{3.3}
$$


Every endpoint return thus has an explicit coefficient factor $p$.

### 3.2 Every retained shift preserves the forcing digits

The low three-digit residues are


$$
b\bmod D=5044,\qquad
(n+2)\bmod D=20389,\qquad
2n\bmod D=16385.
$$


For every shift in (3.2),


$$
4694\le5044+v\le5390,
$$




$$
16384\le16384+a\le16907.
\tag{3.4}
$$


Neither shifted quantity crosses a $D$-boundary.

Consequently the physical triples at positions $3,4,5$ remain


$$
(7,28,15),\qquad(3,0,6),\qquad(9,20,18).
$$


The retained potential certificate supplies at least two valuation events there for **every incoming interface**.

On


$$
u\equiv2\pmod{p^3},
$$


the original residue gives


$$
C\equiv20916\pmod{p^3},
$$


and physical position $7$ has


$$
(W_7,B_7,A_7)=(8,25,17).
$$


If that digit had no weight-borrow or addition-carry event, its digits would obey


$$
x\le8-w,\qquad K\le11-c,
$$


whereas the lower-index subtraction requires


$$
x+K+k=25+29k'.
$$


The left side is at most $20$, which is impossible.

Thus every nonzero retained atom in (3.1) is divisible by $p^3$.

### 3.3 The coefficient-unit sector has a fourth event

By (2.3), the entire coefficient-unit sector is the short-head sector multiplied by $J_0$. Its non-$r=0$ normal-ordered coefficients contain


$$
\binom{2n+r-1}{r}\in p\mathbb Z_p
\qquad(1\le r<29).
$$



The remaining coefficient-unit atoms have addend $2n$ and lower index $b-1-j$ or $b-j$. In the first two digits,


$$
(n+2)\bmod p^2=205,\quad
2n\bmod p^2=406,\quad
(b-1)\bmod p^2=838,\quad
b\bmod p^2=839.
$$


If the weight does not borrow there, then $j\bmod p^2\le205$; the lower index is at least $633$, so adding $406$ forces a carry. Otherwise the weight itself supplies the event.

Every coefficient-unit term therefore receives four events. Every positive-order coefficient receives at least the three uniform atom events plus its explicit coefficient factor.

This includes $ph^{[1]}$, the complete lower corrections, and the complete solved finite return.

### 3.4 The actual terminal is separate and sufficiently deep

The retained low nine digits give outgoing weight borrows at positions


$$
0,1,3,5,7,8
$$


when subtracting $b$ from $n+2$. Hence


$$
v_p(W_b)\ge6.
\tag{3.5}
$$


The actual terminal contact value is integral, so (1.1) gives


$$
Z_{w,b}\in p^6\mathbb Z_p.
$$



We have proved


$$
\boxed{Z_w\in p^4\mathbb Z_p^{\,b+1}.}
\tag{3.6}
$$



No norm cancellation was used to obtain this column-content statement.

---

## 4. The zero-interface split and the finite cutoff

Put


$$
W=\frac{n+2-20389}{D},\qquad
B=\frac{b-5044}{D},\qquad A=2W+1,
$$


and define


$$
U(J)=\binom WJ\binom{A+B-J}{B-J}.
\tag{4.1}
$$



For a term entering $Z_w/p^4\bmod p$, coefficient order plus low-block event count is exactly one.

* A coefficient-$p$ term must have no low event.
* A coefficient-unit term has exactly its forced low event in positions $0,1$, with no additional event at position $2$.

Both cases have zero outgoing weight borrow and addition carry. An outgoing lower-index borrow would require


$$
\ell+K_{\rm low}=5044+v+D.
$$


But


$$
\ell\le20389,\qquad K_{\rm low}\le8004-a,
$$


so the left side is at most $28393-a$, while the right side is at least $29083$. It cannot occur.

Thus all these terms enter the upper problem with interface $000$.

Writing $j=\ell+DJ$, there are complete low coefficients $a_\ell\in\mathbb F_p$ such that, on the interior rows,


$$
\left(\frac{Z_w}{p^4}\right)_{\ell+DJ}
=
(-1)^{b-\ell-J}a_\ell\,\frac{U(J)}{p^3}\pmod p.
\tag{4.2}
$$


The signs $(-1)^v$ specific to an atom have been absorbed into its coefficient.

### A cutoff clarification

For the interior $j<b$, the exact range is


$$
0\le J\le
\begin{cases}
B,&\ell<5044,\\
B-1,&\ell\ge5044.
\end{cases}
\tag{4.3}
$$


The inclusive reconstructed range adds the separate physical coordinate $j=b$.

This is the clean way to use Turn 11’s inclusive cutoff: do not evaluate an algebraically continued contact atom at $b$ and then also add the physical terminal.

The distinction does not alter the norm conclusions. Indeed,


$$
v_p(U(B))\ge4,
\tag{4.4}
$$


from the upper weight borrows at positions $0,2,4,5$. Thus $U(B)/p^3\in p\mathbb Z_p$. The omitted upper endpoint has square zero modulo $p^2$, while the actual physical terminal has square in $p^{12}$.

---

## 5. The closed $p^8$-radical is now unconditional

Set


$$
K(J)=U(J)/p^3,\qquad
\mathscr L=\sum_{\ell=0}^{D-1}a_\ell^2\pmod p.
$$



The retained minimal-path classification through physical positions $3,4,5$ gives


$$
\sum_{J=0}^{B}K(J)^2
=
12\left(10H_{\rm I}+19H_{\rm II}\right)\pmod p,
\tag{5.1}
$$


where


$$
H_{\rm I}=\sum_{q=0}^{C}\left(\frac{F_{\rm I}(q)}p\right)^2,\qquad
H_{\rm II}=\sum_{q=0}^{C}\left(\frac{F_{\rm II}(q)}p\right)^2,
$$




$$
F_{\rm I}(q)=(2X+C+1-q)V(q),\quad
F_{\rm II}(q)=(X-q)V(q),
$$




$$
V(q)=\binom Xq\binom{2X+C-q}{C-q},\qquad X=2001C+1382.
$$



Their difference is the whole divided expression


$$
\mathcal B(C):=H_{\rm I}-H_{\rm II}
=
\frac{(X+C+1)((3X+C+1)T_0-2T_1)}{p^2}.
\tag{5.2}
$$


The branchwise reflection proves $\mathcal B(C)=0\pmod p$, independently of the tail value.

Since $19=-10\pmod p$, (5.1) is zero. Equations (3.6), (4.2), and the separate endpoint analysis therefore prove


$$
\boxed{
u\equiv2\pmod{24389}
\Longrightarrow c\ge2,\quad d\ge9.
}
\tag{5.3}
$$



This is no longer conditional on a missing head identification.

---

## 6. Scope of the completed one-event and tail receipt

The newly completed receipt establishes the following distinct facts.

1. The $42$ stripped one-event contributions agree with the prescribed residues.
2. The $135918$ complete bounded auxiliary atoms at
   

$$
C=20916,\ 45305,\ 69694
$$


   corroborate the paid connection and the whole divided difference at the stated precision.
3. At actual original $u=2$, the normalized-tail row starting at $e_0^T$ is zero after six digits.

The first two are finite arithmetic corroboration. The third, combined with the proved finite transport identity, gives an all-continuation conclusion with actual terminal $e_0$:


$$
\mathcal H(t)=0\pmod p.
\tag{6.1}
$$



The source computes the original residue modulo $p^{41}$, which supplies more than the $p^9$-precision in $C$ needed for those six normalized-tail digits. The conclusion depends only on


$$
C\bmod p^9,
$$


and hence holds throughout


$$
u\equiv2\pmod{p^9}.
\tag{6.2}
$$


This uses the retained compatible original parametrization; it does not identify auxiliary $C$-values with original indices.

No part of this completed work is proposed for repetition.

---

# Part I. The next complete physical contraction

## 7. An exact factorial-strip interface

The following elementary identity is useful because it separates valuation, low units, and the upper factorial ratio without inverting a high binomial.

Define


$$
F_p(N)=\prod_{\substack{1\le r\le N\\p\nmid r}}r,
\qquad
\mathcal P_m(N)=\prod_{i=0}^{m-1}F_p\!\left(\left\lfloor N/p^i\right\rfloor\right).
$$


For $N\ge0$,


$$
N!
=
p^{\sum_{i=1}^{m}\lfloor N/p^i\rfloor}
\left\lfloor N/p^m\right\rfloor!\,
\mathcal P_m(N).
\tag{7.1}
$$


Every $\mathcal P_m(N)$ is a $p$-adic unit.

Apply this to the two positive binomials of a reconstructed atom. At a cut $D=p^m$, let $w,k,c$ be the outgoing weight borrow, lower-index borrow, and addition carry. With common upper quotients $W,A,B$, the exact upper factorial ratio is


$$
H_{wkc}(J)=
(W-J)^w(A+B-J-k+1)^c
\binom WJ\binom{A+B-J-k}{B-J-k}.
\tag{7.2}
$$


The whole atom is


$$
p^{e_{\rm low}}\times
(\text{explicit unit ratio of }\mathcal P_m)
\times H_{wkc}(J),
\tag{7.3}
$$


where $e_{\rm low}$ counts the low weight-borrow and addition-carry events.

The convention is $H_{wkc}(J)=0$ when $B-J-k<0$. All lower indices and the original row cutoff remain explicit.

For the present physical cut $m=3$, the forcing certificate proves


$$
H_{wkc}(J)\in p^3\mathbb Z_p
\tag{7.4}
$$


for all relevant interfaces and indices. Write


$$
K_{wkc}(J)=H_{wkc}(J)/p^3.
$$


In particular $K_{000}=K$.

### 7.1 The low unit lift is affine in the upper index modulo $p^2$

The elementary block formula


$$
F_p(pq+r)
\equiv ((p-1)!)^q r!\bigl(1+pq\,\mathsf H_r\bigr)\pmod{p^2},
\qquad 0\le r<p,
\tag{7.5}
$$


uses $\mathsf H_r=\sum_{a=1}^r a^{-1}\pmod p$.

In a balanced factorial ratio, the block powers cancel up to a fixed low carry. At a three-digit cut, dependence on the upper index modulo $p^2$ occurs only through the last low digit and is affine:


$$
L(J)\equiv L(0)+pJ\,L^{[1]}\pmod{p^2}.
\tag{7.6}
$$



For a zero outgoing interface, the coefficient of $J$ in the first-order logarithmic correction is


$$
\mathsf H_{L_2}-\mathsf H_{j_2}
+\mathsf H_{K_2}-\mathsf H_{Z_2},
\tag{7.7}
$$


where $L_2,K_2,Z_2$ are the actual subtraction and addition digits. The other terms depend only on the low data and the fixed upper parameters modulo $p$.

No factorial denominator divisible by $p$ is inverted in this derivation.

### 7.2 Row-factor guard at the current precision

For every $r<p^2$,


$$
\binom{j+p^3}{r}\equiv\binom jr\pmod{p^2}.
\tag{7.8}
$$


Indeed, in Vandermonde’s formula,


$$
v_p\binom{p^3}{k}=3-v_p(k)\ge2
\qquad(1\le k\le r<p^2).
$$


The same periodicity covers the retained shifted reconstruction factors.

Thus the row factors in the complete $p^6$ first-column normal form depend only on $\ell$, even modulo $p^2$. They do not introduce an unrecorded upper-index dependence.

---

## 8. The complete normalized column modulo $p^2$

Put


$$
F=Z_w/p^4.
$$


The preceding strip identity gives, for $j=\ell+DJ<b$,


$$
\boxed{
F_j\equiv
(-1)^{b-\ell-J}
\left[
(\widetilde a_\ell+pJb_\ell)K(J)
+
p\sum_{s\in\{0,1\}^3}c_{\ell,s}K_s(J)
\right]
\pmod{p^2}.
}
\tag{8.1}
$$


Here:

* $\widetilde a_\ell\bmod p=a_\ell$;
* all coefficients are actual complete-source coefficients;
* the first term contains coefficient order plus low-event count equal to one;
* the $c_{\ell,s}$ contain every term with that total equal to two.

In particular, (8.1) includes:

* the lift of the actual $ph^{[1]}$ contribution;
* higher actual-head coefficients that enter at this precision;
* the compatible second-lower contribution;
* lower corrections applied to first returns;
* second and crossed finite returns;
* their actual solved endpoint coefficients.

Terms with coefficient order plus low-event count at least three are in $p^2F$, by (7.4). This is the present precision justification—not an extrapolation of their earlier elimination modulo $p^5$.

The physical terminal satisfies $F_b\in p^2\mathbb Z_p$.

---

## 9. A larger upper radical removes the complete cross term

The minimal support of $K\bmod p$ has


$$
J_0\in\{0,\ldots,7\}\cup\{15,\ldots,28\},
\qquad J_1=0.
\tag{9.1}
$$


The interface resets before the next digit.

Consequently, for **every** function $R:\mathbb F_p\to\mathbb F_p$,


$$
\boxed{
\sum_{J=0}^{B}R(J_0)K(J)^2=0\pmod p.
}
\tag{9.2}
$$


The proof is the same complete upper contraction as (5.1), with its first-digit scalar replaced by the $R$-weighted scalar. The remaining factor is still


$$
10H_{\rm I}+19H_{\rm II}=10\mathcal B=0\pmod p.
$$



This radical controls all eight cross-interface contractions. On the support of $K\bmod p$,


$$
\frac{H_{w0c}(J)}{U(J)}
=(W-J)^w(A+B-J+1)^c,
\tag{9.3}
$$


while


$$
\frac{H_{w1c}(J)}{U(J)}
=(W-J)^w(B-J)(A+B-J)^{c-1}.
\tag{9.4}
$$


The only possible denominator in (9.4) is a unit there:


$$
A+B-J\equiv14-J_0\pmod p,
$$


and $J_0=14$ is excluded by (9.1).

Thus


$$
\sum_JK(J)K_s(J)=0\pmod p
\tag{9.5}
$$


for every relevant interface $s$. Also


$$
\sum_JJ\,K(J)^2=0\pmod p.
$$



Squaring (8.1), retaining all cross terms, and using (9.2)–(9.5) yields


$$
\boxed{
F^TF
\equiv
\left(\sum_\ell\widetilde a_\ell^2\right)
\sum_{J=0}^{B}K(J)^2
\pmod{p^2}.
}
\tag{9.6}
$$


The different interior cutoff branches can be completed here because $K(B)^2\in p^2\mathbb Z_p$; the physical terminal is separately zero at this precision.

Since $\sum K^2\in p\mathbb Z_p$, only $\mathscr L=\sum a_\ell^2\bmod p$ remains after division:


$$
\boxed{
\frac{Z_w^TZ_w}{p^9}
=
\mathscr L\,
\frac{\sum_{J=0}^{B}U(J)^2}{p^7}
\pmod p.
}
\tag{9.7}
$$



This is the requested complete next contraction. In canonical digit notation it evaluates


$$
\frac{z_1^Tz_1+2p\,z_1^Tz_2}{p}\pmod p
$$


as a whole. The cross term has not been omitted; its full-source contribution is eliminated by the proved radical (9.5).

---

# Part II. Factoring the remaining lift through the accepted normalized tail

## 10. The upper three-digit lift has only two interfaces

The upper parameters split exactly as


$$
W=7663+DX,\qquad
B=16848+DC,\qquad
A=15327+2DX.
\tag{10.1}
$$



The minimal two-event low paths are


$$
r=j_0+p^2j_2,\qquad
j_0\in\{0,\ldots,7\}\cup\{15,\ldots,28\},
\quad 0\le j_2\le20.
$$


There are:

* $220$ paths with $0\le j_2\le9$, producing interface I;
* $242$ paths with $10\le j_2\le20$, producing interface II.

Every other low path is too deep for the square modulo $p^8$, because the later phase supplies at least one more event.

By the affine unit lift (7.6), there are fixed constants


$$
\alpha_{\rm I},\alpha_{\rm II}\in\mathbb Z/p^2\mathbb Z,
\qquad
\beta_{\rm I},\beta_{\rm II}\in\mathbb F_p
$$


such that


$$
\begin{aligned}
\sum_JK(J)^2\equiv{}&
\alpha_{\rm I}H_{\rm I}
+\alpha_{\rm II}H_{\rm II}\\
&+p\beta_{\rm I}H_{\rm I}^{[1]}
+p\beta_{\rm II}H_{\rm II}^{[1]}
\pmod{p^2},
\end{aligned}
\tag{10.2}
$$


where


$$
H_{\rm I}^{[1]}=\sum_{q=0}^{C}q(F_{\rm I}(q)/p)^2,
\qquad
H_{\rm II}^{[1]}=\sum_{q=0}^{C}q(F_{\rm II}(q)/p)^2.
$$



These constants depend only on the displayed low digits and $X,C\bmod p=(19,7)$. They are independent of the remaining $t$.

The accepted leading coefficients give


$$
\alpha_{\rm I}\equiv4,\qquad
\alpha_{\rm II}\equiv-4\pmod p.
\tag{10.3}
$$



Both exact finite ranges remain $0\le q\le C$. No extra terminal carry is accepted.

---

## 11. A lifted branch reflection removes the derivative tail

A new useful fact is that the next divided difference itself factors through the **ordinary** normalized tail:


$$
\boxed{
\frac{\mathcal B(C)}p=\gamma\,\mathcal H(t)\pmod p
}
\tag{11.1}
$$


for a fixed explicitly bounded constant $\gamma\in\mathbb F_p$.

### Proof

Only valuation-one paths can contribute to $\mathcal B\bmod p^2$. The Turn 10 classification gives exactly $231$ low three-digit paths:

* the first digit has
  

$$
d_0+k_0=7+29\varepsilon,\qquad0\le d_0,k_0\le19;
$$


* the second digit is type A or B;
* the third digit is the unique bridge;
* all three outgoing interfaces are zero.

Write a surviving lower index as


$$
q=q_s+Dr.
$$


Its exact high factor is


$$
V_{\rm tail}(r)=
\binom{1716+2001t}{r}
\binom{3432+4002t+t-r}{t-r}.
$$



The difference multiplier


$$
\Delta(q)=(X+C+1)(3X+C+1-2q)
$$


is, modulo $p^2$, independent of $r$ and of the higher digits of $t$, since $D=p^3$.

The stripped low unit lift is affine in the high parameters and $r$. Its high-dependent first-order part comes only from the third low digit. For fixed cutoff branch and type, that bridge is independent of which first digit is called $d_0$ or $k_0$.

Modulo $p$,


$$
\Delta(q)\equiv15+4d_0=4(d_0-7/2).
$$


The first-digit squared weight is symmetric under $d_0\leftrightarrow k_0$, and $d_0+k_0\equiv7\pmod p$. Hence its contraction against this multiplier is zero separately within every branch and type.

Therefore:

* the leading low coefficient is divisible by $p$;
* every first-order high-parameter correction cancels;
* every first-order $r$-correction cancels.

The remaining low coefficient is a fixed $p\gamma\bmod p^2$. Thus


$$
\mathcal B(C)
\equiv
p\gamma\sum_{r=0}^{t}V_{\rm tail}(r)^2
\pmod{p^2},
$$


which is (11.1). ∎

This is not obtained by dividing a zero matrix. It is a paid lifted reflection of the complete valuation-one support.

---

## 12. The needed ordinary moments are explicit

The one-event factorization applies to any polynomial in $q\bmod p$, not only degrees $0,1,2$. The same unique bridge leaves the same tail.

Let $E_h$ denote its low coefficient. The accepted values are


$$
E_0=23,\qquad E_1=8,\qquad E_2=18.
$$


Reflection gives


$$
2E_3=7^3E_0-3\cdot7^2E_1+3\cdot7E_2,
$$


and therefore


$$
\boxed{E_3=22\pmod{29}.}
\tag{12.1}
$$



Since


$$
2X+C+1\equiv17,\qquad X\equiv19\pmod p,
$$


direct substitution gives


$$
\boxed{
H_{\rm I}=H_{\rm II}=13\mathcal H(t)\pmod p,
}
\tag{12.2}
$$




$$
\boxed{
H_{\rm I}^{[1]}=11\mathcal H(t),\qquad
H_{\rm II}^{[1]}=22\mathcal H(t)\pmod p.
}
\tag{12.3}
$$



These are symbolic consequences of the accepted connection and reflection, not additional auxiliary computations.

Define


$$
\boxed{
\Xi=
4\gamma+
13\,\frac{\alpha_{\rm I}+\alpha_{\rm II}}p
+11\beta_{\rm I}+22\beta_{\rm II}
\pmod p.
}
\tag{12.4}
$$


The displayed division is legitimate by (10.3), and its value is independent of the chosen residue lifts.

Dividing (10.2) as a whole, then using (11.1)–(12.3), proves


$$
\boxed{
\frac{\sum_{J=0}^{B}U(J)^2}{p^7}
=\Xi\,\mathcal H(t)\pmod p.
}
\tag{12.5}
$$



Combining (9.7) and (12.5) establishes the complete physical factorization (E.1).

---

## 13. New unconditional original consequence

The completed six-digit tail receipt gives $\mathcal H(t)=0$ on the cylinder (6.2). Thus:

### Theorem 13.1 — Complete next physical norm zero

For every nonnegative original index


$$
u\equiv2\pmod{29^9},
$$


the actual corrected first column satisfies


$$
\boxed{
Z_w\in29^4\mathbb Z_{29}^{\,b+1},
\qquad
Z_w^TZ_w\in29^{10}\mathbb Z_{29}.
}
\tag{13.1}
$$



This includes actual $u=2$.

The proof uses the complete output modulo $p^6$. Since $Z_w\in p^4$, that precision determines its norm modulo $p^{10}$. The terminal square is in $p^{12}$. All required precision is therefore paid.

### What this does not say

It does not determine $c$. The possibilities include


$$
c=2,\ \nu\ge2,
\qquad\text{or}\qquad
c\ge3.
$$


Nor does it evaluate the first nonzero primitive norm digit.

On the larger phase $u\equiv2\pmod{p^3}$, a future actual evaluation


$$
\mathscr L\,\Xi\,\mathcal H(t)\ne0
$$


would imply


$$
d=9,\qquad c=2,\qquad \nu=1.
\tag{13.2}
$$


That is a conditional deduction, not an evaluated original instance.

---

# Part III. All-depth interface and the exact-content obstruction

## 14. Why a full constant-content original cylinder cannot exist

The accepted complete-column theorem states that, in every original progression $u\equiv u_0\pmod h$, the content $c$ is unbounded.

It follows immediately that there is no nonempty full original arithmetic cylinder on which


$$
c=c_*
$$


for a fixed finite $c_*$.

This rules out, in particular, a proposed full-cylinder certificate simultaneously fixing a finite exact $c$ and a first primitive norm digit. A finite low-prefix unit witness with that all-continuation conclusion would contradict the established unbounded-content theorem.

This is a mathematical obstruction, not merely an absent computation.

One can still seek:

* an evaluated individual original index;
* a thinner original subsequence with additional non-cylinder conditions;
* or an all-depth interface that separately tracks content and norm.

The third option is developed next.

---

## 15. An exact all-depth complete-column interface

Fix any finite precision $p^K$. Reuse Turn 0’s complete finite atom factorization, including all finite boundary terms and the actual endpoint solve.

For each reconstructed interior atom:

1. convert a negative upper binomial to its positive-binomial form;
2. choose a cut $p^m$;
3. retain the actual low remainders of its shifted parameters;
4. retain the resulting upper quotient shifts;
5. apply the exact factorial identity (7.1).

This gives an exact integral representation by:

* the low residue $\ell$;
* the three outgoing interface bits $w,k,c$;
* the actual finite atom label and its upper quotient shifts;
* the explicit low event count;
* an explicit unit ratio of $\mathcal P_m$;
* the high factorial ratio (7.2), with the actual shifts;
* the original finite cutoff.

For upper parameter $0$, the corresponding binomial is a singleton support condition and is handled directly.

### Precision and periodicity

At unit precision $p^s$, the balanced low unit ratio depends on the high index modulo $p^{s-1}$. This follows from


$$
F_p(N+p^s)\equiv-F_p(N)\pmod{p^s}
$$


and cancellation of the paired block signs.

For a row factor of binomial-basis degree $r$, a sufficient period in the physical index is


$$
p^{s+\lfloor\log_p r\rfloor}\qquad(r\ge1).
$$


Choosing $m>\lfloor\log_p r\rfloor$ makes a high-index residue modulo $p^{s-1}$ sufficient for both the unit ratio and the row factor.

Thus, at every fixed depth, the complete column factors through an explicit finite collection of masked high kernels


$$
\mathbf1_{J\equiv a\;(\mathrm{mod}\ p^{s-1})}
H_{wkc}^{\rm shifted}(J),
\tag{15.1}
$$


with actual integral coefficients and actual finite endpoints.

This is an **all-depth exact interface**, not an evaluated all-depth automaton. Its coefficients still include genuine high-index head and force data. Its size need not be practically small, and no fixed-depth cylinder theorem for exact content follows from it.

### Scope of the physical normalization

The special uniform $p^3$-atom bound and the eight-channel collapse in §§7–9 use the retained $K=6$ shift box. At arbitrary $K$, larger shifts must be processed by their actual quotient changes; they must not be assumed to preserve the same low forcing digits.

The general interface remains exact. The special physical radical has precisely the guard stated above.

---

# Part IV. A concrete mixed observable and the complete force

## 16. The physical normalization reduces an actual mixed observable

Set


$$
F=Z_w/p^4,\qquad \lambda=d-8=v_p(F^TF).
$$


Then


$$
Z_w^TY-p\rho_nZ_w^TZ_w
=
p^7\left(F^TQ-p^2\rho_nF^TF\right).
$$


The exact mixed target is therefore


$$
\boxed{
F^TQ-p^2\rho_nF^TF
\equiv0\pmod{p^{\lambda+3}}.
}
\tag{16.1}
$$



At the first ordinary layer, the complete normalized first column reduces this to the concrete family


$$
\mathcal M_\ell(Q)=
\sum_{\substack{J\ge0\\\ell+DJ<b}}
(-1)^{b-\ell-J}K(J)\,Q_{\ell+DJ}\pmod p,
\tag{16.2}
$$


with


$$
\boxed{
F^TQ=\sum_{\ell=0}^{D-1}a_\ell\mathcal M_\ell(Q)\pmod p.
}
\tag{16.3}
$$


The terminal is zero at this layer, by its proved valuation.

This is a genuine mixed observable: the second factor is the complete corrected $Q$, not another copy of the first-column kernel. The squared-kernel radical does not automatically annihilate it.

At higher precision, the same construction uses the complete interface (8.1), or its all-depth extension, against the complete second-column representation from Turn 0.

---

## 17. Both initial charges, all source rows, and the exterior remain

Let $g^{(i)}$ denote the original finite recurrence impulse at source row $i$, so that


$$
\tau=\sum_{i=1}^{b-2}\mathcal H_i g^{(i)}.
$$


Then the exact contraction is


$$
\begin{aligned}
p^3F^TQ={}&
r_0\,F^T\mathcal RA^{-1}h^{(0)}
+r_1\,F^T\mathcal RA^{-1}h^{(1)}\\
&+\sum_{i=1}^{b-2}
\mathcal H_i\,F^T\mathcal RA^{-1}g^{(i)}
+W_bF_b.
\end{aligned}
\tag{17.1}
$$


Division by $p^3$ belongs to this whole right-hand side.

The charges remain


$$
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(
T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}
\right),
\qquad i=0,1,
\tag{17.2}
$$


and the complete source remains


$$
\mathcal H_i=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b},
\qquad1\le i\le b-2.
\tag{17.3}
$$



There is no source row $b-1$. The exterior at $b$ is not another recurrence step.

The original adjoint form is unchanged:


$$
p^3U_a^TQ=
p^3(r_0G^{(3)}_{a0}+r_1G^{(3)}_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda'_{a,\ell}
+W_bU_{a,b}.
\tag{17.4}
$$



The retained sufficient precision budgets remain


$$
K_Z^{\rm norm}\ge d-c-1,
$$




$$
K_Z^{\rm mixed}\ge d-1,\qquad
K_Y^{\rm mixed}\ge d-c,\qquad
N_{\log}\ge d-c.
\tag{17.5}
$$


The newly proved lower bound $d\ge10$ is not an upper bound that would justify choosing a final norm-relative precision.

---

# Part V. New bounded arithmetic, proof status, and the global objective

## 18. A genuinely new bounded calculation: the universal constant $\Xi$

No additional arithmetic is needed for Theorem 13.1. Nevertheless, evaluating $\Xi$ would decide whether the new factorization vanishes throughout the entire $u\equiv2\pmod{p^3}$ phase or only where one of its other factors vanishes.

This is a new low-unit lift, not a rerun of the accepted $42$ contributions or the accepted complete auxiliary sums.

### 18.1 Inputs for $\alpha_{\rm I},\alpha_{\rm II},\beta_{\rm I},\beta_{\rm II}$

Use the bounded reference parameters


$$
W_*=7663+19D,\qquad
B_*=16848+7D,\qquad
A_*=15327+38D.
$$


For each of the $462$ minimal low indices


$$
r=j_0+p^2j_2,
$$


with $j_0$ and $j_2$ as in §10, evaluate at $q=0,1$ the unit ratio


$$
L_r(q)=
\frac{\mathcal P_3(W_*)}
{\mathcal P_3(r+Dq)\mathcal P_3(W_*-r-Dq)}
\,
\frac{\mathcal P_3(A_*+B_*-r-Dq)}
{\mathcal P_3(A_*)\mathcal P_3(B_*-r-Dq)}
\pmod{p^2}.
\tag{18.1}
$$



Then


$$
\alpha_\varepsilon=\sum_{r\in\varepsilon}L_r(0)^2\pmod{p^2},
$$




$$
\beta_\varepsilon=
2\sum_{r\in\varepsilon}
L_r(0)\frac{L_r(1)-L_r(0)}p\pmod p.
\tag{18.2}
$$


The differences in (18.2) are divisible by $p$, by the proved unit-periodicity lemma.

### 18.2 Inputs for $\gamma$

Use


$$
C_*=20916,\qquad X_*=2001C_*+1382=41854298.
$$


Enumerate the $231$ classified low valuation-one paths, with


$$
q_s=d_0+pd_1+p^2d_2,
$$


where $d_2=3$ for type A and $d_2=2$ for type B.

Compute the corresponding low unit $L_s$ by the same explicit $\mathcal P_3$-ratio, with upper parameters $X_*,2X_*,C_*$, and put


$$
\gamma=
\frac{
\sum_s
(X_*+C_*+1)(3X_*+C_*+1-2q_s)L_s^2
}{p}
\pmod p.
\tag{18.3}
$$


The sum is accumulated modulo $p^2$ before its demonstrated division by $p$.

Only unit factorial products are inverted. Their modular evaluation can use


$$
F_p(N)\equiv
(-1)^{\lfloor N/p^2\rfloor}
F_p(N\bmod p^2)\pmod{p^2},
$$


so no original-length factorial or matrix is constructed.

### Expected verifiable output

Return


$$
(\alpha_{\rm I},\alpha_{\rm II},
\beta_{\rm I},\beta_{\rm II},\gamma,\Xi),
$$


together with:

* the $220/242$ branch counts and the $231$-path count;
* the checks $\alpha_{\rm I}\equiv4$, $\alpha_{\rm II}\equiv25\pmod{29}$;
* divisibility of every difference in (18.2);
* divisibility of the whole numerator in (18.3);
* the value of (12.4).

No nonzero value is predicted here. This calculation is **specified, not executed**.

---

## 19. Final gcd, actual primitive denominator, and whole error

None of the preceding physical divisions changes a row content, the row metric, or the least actual two-column clearer.

Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
\tag{19.1}
$$


The gcd is over all primes. The actual primitive multiplier remains


$$
d_B^2/g_B.
$$



In particular,


$$
\log q_n=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
\tag{19.2}
$$



For the same original index,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


and the whole evaluated form is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{19.3}
$$



At the retained scope of the complete signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$


and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
\tag{19.4}
$$


The missing global comparison is an actual all-prime bound on $q_n$ strong enough to make the whole nonzero expression (19.3) tend to zero along an infinite original sequence.

Additional selected-prime content, or another vanished norm digit, does not establish that comparison.

---

## 20. Proof-status ledger

| Statement | Status |
|---|---|
| Actual head $f^0=J_0h^{[0]}+ph^{[1]}$ in the required coordinates | **Proved from the exact source** |
| Integral remainder retained | **Yes, throughout** |
| All retained $p^6$ shifts preserve the three uniform events | **Audited and proved** |
| Fourth event for the complete coefficient-unit sector | **Proved** |
| Actual terminal $v_p(W_b)\ge6$ | **Proved** |
| Interior cutoff versus separate inclusive terminal | **Explicitly distinguished** |
| $c\ge2,\ d\ge9$ on original $u\equiv2\pmod{24389}$ | **Unconditional** |
| Completed $42$-term and $135918$-atom controls | Reused at their finite scope |
| Six-digit actual normalized-tail annihilation | Reused with all-continuation terminal-zero implication |
| Eight-interface normalized column modulo $p^2$ | **Proved complete factorization** |
| Full $2p\,z_1^Tz_2$ contraction | **Retained and proved zero by the enlarged radical** |
| Lifted difference $\mathcal B/p=\gamma\mathcal H$ | **Proved** |
| Complete physical factorization $N/p^9=\mathscr L\Xi\mathcal H$ | **Proved** |
| $d\ge10$ at original $u=2$, and on $u\equiv2\pmod{29^9}$ | **Unconditional consequence** |
| Numerical value of $\Xi$ | Unevaluated bounded specification |
| Exact $c$ and first nonzero primitive norm digit | Open |
| Full original cylinder with fixed finite $c$ | **Excluded by the accepted unbounded-content theorem** |
| All-depth factorial-strip interface | **Proved exact representation; not a completed evaluator** |
| Complete mixed-force alignment | Open |
| All-prime denominator versus whole nonzero same-index error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The recovered source closes the actual-head interface without computation. After the full finite audit,


$$
\boxed{
u\equiv2\pmod{24389}\Longrightarrow c\ge2,\ d\ge9
}
$$


is an unconditional statement about the actual original corrected column.

The new advance is the complete next-layer factorization


$$
\boxed{
\frac{Z_w^TZ_w}{29^9}
=
\mathscr L\,\Xi\,\mathcal H(t)\pmod{29}.
}
$$


It includes the lifted leading square and every correction that can enter the cross term at this precision. Their elimination is explained by an explicit eight-interface upper radical, not by reusing a shallower norm reduction outside its scope.

The accepted six-digit normalized-tail zero therefore supplies a new actual physical conclusion:


$$
\boxed{
u\equiv2\pmod{29^9}\Longrightarrow Z_w^TZ_w\in29^{10}\mathbb Z_{29}.
}
$$



The exact remaining local bottleneck is now to obtain an **actual nonzero primitive certificate**, while evaluating the mixed observable against the complete second force. A full constant-content original cylinder is unavailable in principle, because actual content is unbounded in every original progression. The all-depth interface given here preserves the data needed to pursue individual-index or thinner-subsequence certificates instead.

The only new bounded arithmetic proposed is the explicit $p^2$ low-unit calculation of $\Xi$. It does not repeat the accepted controls, and it is not needed for the new $d\ge10$ theorem.

Finally, the all-prime final gcd, actual primitive denominator, and whole nonzero same-index error have not been compared at the required infinite-family scale. Therefore an unconditional proof or disproof of the irrationality of $e+\pi$ remains unresolved.
