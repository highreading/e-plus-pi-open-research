> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 Turn 1 — A sparse low observation row and an explicit bounded assembly

## Abstract and proof status

The five-coefficient input in the preceding report was not evaluated. Nor did the observable flat-head theorem, by itself, justify replacing every first-correction coefficient by its flat-head analogue.

This report gives a more economical continuation.

1. **Two of the five coefficients vanish structurally:**
   

$$
\boxed{\mu=\chi=0.}
$$


   This is a support-separation result for the complete source-and-return normal forms. It is not a consequence of setting the exceptional kernel equal to zero.

2. **Only one nonleading interface can contribute to the low mixed row:**
   

$$
\boxed{\lambda=\tau-L_{011}.}
$$


   The other seven interface contractions either vanish pointwise against the leading profiles or are already radical at the required paid observation.

3. **Coefficient-order two can be omitted from this particular low row.** Its possible surviving contribution is only a constant multiple of $pK$, whose completed mixed observation vanishes. Consequently, the two explicit first-order dictionaries in Turn 16 suffice for the whole low row—not merely for its exceptional part. This extension requires the support and event argument supplied below.

4. **No new $118$- or $147$-coordinate exterior solve is needed.** The retained two-coordinate second-column solve and the explicit first-column return suffice. The remaining arithmetic is an assembly over at most $5\,075$ low rows using at most $1\,454$ reconstructed atoms.

The resulting observation is


$$
\boxed{
\kappa
=25A_W\bigl(\alpha S-\delta k_B^2+\lambda T\bigr)
\pmod{29}.
}
\tag{A}
$$



I do **not** report invented values for $\alpha,\delta,\lambda$. Their bounded assembly is specified completely below, including input residues, symbol arrays, atom coefficients, returns, event extraction, paid divisions, and expected certificates. Thus this report proves a sparse-row reduction and removes several implementation dependencies, but does not claim that the remaining three-residue calculation has been executed.

The global rationality or irrationality of $e+\pi$ remains unresolved.

---

## 1. Original objects and exact scope

Put


$$
p=29,\qquad D=p^3=24389.
$$


The original family remains


$$
b=3^{249005515+574312172u}
  =410910916+p^6C,\qquad n=2001b,
$$


with


$$
u\ge0,\qquad u\equiv2\pmod{p^9}.
$$



The domains are unchanged:

- contact coordinates $0\le j<b$;
- recurrence source rows $1\le i\le b-2$;
- reconstructed coordinates $0\le j\le b$.

Write


$$
W_j=\binom{n+2}{j},\qquad
(\mathcal Rx)_j=W_j(jx_{j-1}-x_j),\qquad x_{-1}=x_b=0.
$$


The actual columns are


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,
$$


with the complete recovered force


$$
\mathbf r=A_{IE}z+\frac{h^F}{b!},
\qquad
z_h=\frac{(b+h)!}{b!}.
$$



The logarithmic term here is the one formed from $F/(1-z)$. The exponential factorial subtraction, both initial exponential charges, all recurrence source rows, finite returns, and the separate physical terminal are retained.

At the reviewed fixed layer,


$$
F=Z_w/p^4,\qquad G=Y/p^4,\qquad
\kappa=\frac{F^TG}{p^2}\pmod p.
$$



The upper parameters satisfy


$$
b=DB+5044,\qquad
n+2=DW+20389,\qquad
2n-1=DA+16384,
$$


where


$$
A=2W+1,\qquad W=2001B+413.
$$


The original contact cutoffs are therefore


$$
0\le J\le
\begin{cases}
B,&0\le\ell<5044,\\
B-1,&5044\le\ell<D,
\end{cases}
\qquad j=\ell+DJ<b.
\tag{1.1}
$$



In particular, the physical coordinate $j=b$ is not an additional contact atom.

---

## 2. What is reused, and what is newly proved

The following are retained results at their stated fixed-layer scope:

- the complete-force identification;
- the guarded three-event upper forcing for every incoming interface;
- the ordinary weighted radical;
- the ordinary lifted-square divisibility;
- the reflected exceptional square cancellation;
- the exact factorial exterior filtration;
- the actual head expansion and its paid original tail;
- the original terminal valuation $v_p(W_b)\ge6$.

Several of their original proofs or computation receipts are referenced rather than reproduced in the supplied sources. I therefore distinguish:

- algebraic consequences proved below from explicitly stated retained hypotheses;
- the retained hypotheses themselves;
- a proposed finite certificate that has not been executed here.

No new path enumeration, no reevaluation of $\Xi=17$, and no old exterior solve is proposed.

The new source-response arguments below are checkable from the displayed finite kernels. They do not require accepting the earlier exceptional coefficient dictionary as an unexplained instruction.

---

# Part I. The weighted radical and the flat-head scope

## 3. The full weighted radical needed by the mixed product

Define


$$
h_J=\binom WJ\binom{A+B-J}{B-J},
\qquad K(J)=h_J/p^3.
$$


The eight unnormalized kernels are


$$
\begin{array}{c|l}
s&H_s(J)\\ \hline
000&h_J\\
100&(W-J)h_J\\
001&(A+B-J+1)h_J\\
011&(B-J)h_J\\
101&(W-J)(A+B-J+1)h_J\\
111&(W-J)(B-J)h_J\\
010&\displaystyle\binom WJ
             \binom{A+B-J-1}{B-J-1}\\
110&(W-J)H_{010}(J),
\end{array}
\qquad K_s=H_s/p^3.
\tag{3.1}
$$



The retained ordinary weighted radical is the assertion


$$
\sum_{J=0}^{B}R(J\bmod p)K(J)^2=0\pmod p
\tag{3.2}
$$


for every function $R:\mathbb F_p\to\mathbb F_p$, on the original cylinder under consideration.

Its scope is stronger than an unweighted norm zero. That distinction is essential.

### 3.1 Extension to the interface family

Away from $J\equiv14\pmod p$, every $K_s$ is a residue-dependent multiple of $K$, because


$$
A+B-J\not\equiv0\pmod p.
$$


Thus (3.2), with the appropriate residue function, gives


$$
\sum_{J\not\equiv14}R(J_0)K_s(J)K_t(J)=0\pmod p.
$$



On $J_0=14$, the retained shifted-kernel calculation gives


$$
K=0,\qquad
K_s=\eta_sK_{010}\pmod p,
$$


where only $\eta_{010}=1$ and $\eta_{110}=22$ can be nonzero. The exceptional reflection supplies


$$
\sum_{J\equiv14}K_{010}(J)^2=0\pmod p.
$$


Consequently,


$$
\boxed{
\sum_{J=0}^{B}R(J_0)K_s(J)K_t(J)=0\pmod p
}
\tag{3.3}
$$


for all eight $s,t$ and every residue weight $R$.

In particular,


$$
\sum_JJ^2K(J)^2=0,\qquad
\sum_JJ K(J)K_s(J)=0\pmod p.
\tag{3.4}
$$


These are the missing explicit dependencies needed for products containing $JK$. An unweighted Gram zero alone would not imply them.

### 3.2 Endpoint check

At $J=B$,


$$
K_{010}(B)=K_{110}(B)=0
$$


exactly. Every other $K_s(B)$ is an integral polynomial multiple of $K(B)$, and the retained ordinary-tail result gives


$$
K(B)\in p\mathbb Z_p.
$$


Therefore the endpoint products in (3.3) vanish modulo $p$. Both original cutoffs in (1.1) have the same weighted radical.

This does **not** remove the later leading-square correction


$$
k_B^2=\frac{K(B)^2}{p^2}\pmod p.
$$



---

## 4. A compact proof package for the observable flat head

Let


$$
T_i=\mathcal RA^{-1}e_i,\qquad 0\le i\le202,
$$


and


$$
h_i^{[0]}=
\begin{cases}
i!,&0\le i<29,\\
0,&i\ge29.
\end{cases}
$$



The guarded complete source-and-return form gives $T_i\in p^3$. Its leading upper interface is $000$: zero low weight-borrow and addition-carry events cannot coexist with an outgoing lower-index borrow, because the guarded low remainders imply


$$
\ell+K_{\rm low}\le20389+8004-\alpha
< D+4841.
\tag{4.1}
$$



At first order, the response has the same eight-interface form, including the possible $JK$ term. Contracting it against $Y/p^4$, equations (3.3)–(3.4) and


$$
\sum_JK(J)^2\in p^2\mathbb Z_p
\tag{4.2}
$$


give


$$
T_i^TY\in p^9\mathbb Z_p.
\tag{4.3}
$$



For $h^{[0]}$, the additional low event places its response in $p^4$, with leading interface again $000$. The same contraction gives


$$
(\mathcal RA^{-1}h^{[0]})^TY\in p^{10}\mathbb Z_p.
\tag{4.4}
$$



The terminal is separate. Since the finite inverse is integral,


$$
T_{i,b}=bW_b(A^{-1}e_i)_{b-1}\in p^6\mathbb Z_p,
\qquad Y_b\in p^6\mathbb Z_p.
$$


Their product is in $p^{12}$, more than sufficient for (4.3). The same applies to the short factorial response.

Now use the retained actual head expansion


$$
f^0-A_q\widehat f
=p\delta_0h^{[0]}+p^2v+p^7w,
\tag{4.5}
$$


where $v$ is supported in $0,\ldots,202$, and the last term is the paid original tail. Equations (4.3)–(4.5) give


$$
\boxed{
\kappa=A_q\,\frac{(\mathcal RA^{-1}\widehat f)^TY}{p^{10}}
\pmod p.
}
\tag{4.6}
$$



This is the observable statement. The stronger coefficient statement required below needs an additional argument.

---

## 5. Which first-correction coefficients survive the discarded head directions?

Consider the normalized response modulo $p^2$. An atom with coefficient valuation $t$ and $e$ low weight-borrow/addition-carry events contributes at low order $p^{t+e-1}$, after the common upper division $p^3$.

For the $p^2v$ term in (4.5), a possible first-correction contribution requires $t=2,e=0$. By (4.1), its outgoing interface is $000$. Its low unit and row factor modulo $p$ are independent of the high index $J$. Thus it contributes only a constant multiple of $pK$.

For $p h^{[0]}$:

- a unit source atom already has an event in the first two low digits;
- an outgoing weight borrow or addition carry at the third digit would add another event;
- a coefficient-order-one source or return atom with no low event can leave only $000$.

Hence, after multiplication by the additional $p$, the surviving first correction is again only a constant multiple of $pK$.

The $p^7$ tail does not enter the normalized first correction.

Therefore


$$
\boxed{
\frac{\mathcal RA^{-1}(f^0-A_q\widehat f)}{p^4}
\equiv
p\,\beta_\ell K(J)
\pmod{p^2}
}
\tag{5.1}
$$


on the contact coordinates, for suitable low constants $\beta_\ell$.

Consequences:

- the leading profile is unchanged up to $A_q$;
- the $JK$ coefficient is unchanged up to $A_q$;
- every non-$000$ first-correction coefficient is unchanged up to $A_q$;
- the first-order constant $K$-coefficient need not be unchanged.

This is precisely the stronger scope needed here. It does not claim equality of all first-correction coefficients.

---

# Part II. Complete source and return forms at observable order

## 6. An exact finite source identity

Use


$$
\Psi_{\alpha,v,r}(j)=W_j\left[
\binom jr\binom{-2n-\alpha}{b+v-j}
-(r+1)\binom j{r+1}
\binom{-2n-\alpha}{b+v+1-j}
\right].
\tag{6.1}
$$



Let


$$
c_s=s![z^s]\phi(z)^{-n},\qquad
\phi(z)=1-z+\frac{z^2}{2}.
$$


The retained inverse kernel is


$$
C_{jk}
=\sum_s c_s\sum_{a=0}^s
\binom j{s-a}\binom{-n}{a}
\binom{-2n-a}{k+s-a-j}.
\tag{6.2}
$$



For a finite input $f$, the source part of
$\mathcal RC_{II}P_-f$ is


$$
\boxed{
-\sum_{i,s,a,r}
f_i(-1)^{b-1-i}c_s
\binom{-n}{a}\binom{-2n-a}{r}
\binom{s-a+i-r}{s-a}
\Psi_{a+r+1,\ s-a-r-1,\ s-a+i-r},
}
\tag{6.3}
$$


where $0\le a\le s$ and $0\le r\le i$.

To check (6.3), put $t=s-a$ and expand


$$
\binom ki
=\sum_r\binom{k+t-j}{r}\binom{j-t}{i-r}.
$$


Then use


$$
\binom M L\binom Lr=\binom Mr\binom{M-r}{L-r}
$$


and the finite alternating hockey-stick identity through $k=b-1$. Reconstruction sends the resulting contact atom to $-\Psi$. Thus the finite endpoint $b-1$ is retained explicitly.

The return is


$$
-\mathcal RC_{IE}C_{EE}^{-1}C_{EI}P_-f.
\tag{6.4}
$$


It is not replaced by an infinite inverse without a return.

---

## 7. Why coefficient-order two is irrelevant to this low row

At physical precision $p^6$, the coefficient-order-two source and return terms remain within the guarded boxes. The full source formula (6.3), together with the displacement valuation, gives bounded shifts; the return has the same paid support property.

A term of coefficient valuation at least two can affect the normalized first correction only when its low event count is zero. Such a term:

1. leaves $000$, by (4.1);
2. has row factor periodic modulo $p$;
3. has stripped low unit independent of $J$ modulo $p$.

It therefore changes only the first-order constant coefficient of $K$. Its completed mixed contribution is a multiple of


$$
p\sum_JK(J)^2,
$$


which is zero modulo $p^3$ by (4.2). Its endpoint correction has the same sufficient valuation.

Thus:

### Observable-order lemma

For the five-coefficient row, it is sufficient to retain coefficient orders zero and one in the complete source-and-return normal forms. Omitted coefficient-order-two terms cannot change $\alpha,\delta,\lambda,\mu,\chi$.

This is an observable statement, not a claim that the physical columns are determined modulo $p^6$ by coefficient-order one.

---

## 8. Explicit short symbol arrays

Only $c_s$ for $0\le s\le29$ are needed:


$$
c_0=1,\qquad c_s=p\sigma_s\pmod{p^2},
$$


where


$$
\sigma_s=7(s-1)!\,T_s\pmod p\quad(1\le s<29),
\qquad \sigma_{29}=22,
\tag{8.1}
$$


and


$$
T_0=2,\qquad T_1=1,\qquad
T_s=T_{s-1}-\tfrac12T_{s-2}\pmod p.
\tag{8.2}
$$



For $s<p$, (8.1) follows by writing


$$
-\log\phi(z)=\sum_{s\ge1}\frac{T_s}{s}z^s
$$


and using $n/p\equiv7\pmod p$. For $s=p$, Frobenius gives the coefficient $7$, and
$(p-1)!\equiv-1$, yielding $\sigma_p=-7=22$.

For the flat head, put


$$
P(z)=1+2z+2z^2,\qquad
E(z)=\frac{P(z)^p-P(z^p)}p.
$$


For $0\le i<29$, define


$$
\xi_i=\sum_{t=1}^{i}\binom it[z^{29-t}]E(z),\qquad
\zeta_i=\sum_{t=1}^{i}\binom it[z^{58-t}]E(z),
$$


and


$$
\mathsf H_i=\sum_{a=1}^{i}a^{-1}\pmod p.
$$


Then use the specified representatives modulo $p^2$:


$$
\widehat f_i=
2i!+p\,7i!(2\mathsf H_i+14\xi_i+8\zeta_i),
\quad 0\le i<29,
\tag{8.3}
$$




$$
\widehat f_{29+r}=p\,24r!,
\quad 0\le r<29.
\tag{8.4}
$$



These are arrays of lengths $30$ and $58$, not high-index head data.

---

## 9. Complete first-column dictionary at observable order

The required dictionary is


$$
\begin{aligned}
\mathscr Z={}&
-\sum_{i=0}^{57}\sum_{r=0}^{i}
\widehat f_i(-1)^{b-1-r-i}
\binom{2n+r-1}{r}\Psi_{r+1,-1-r,i-r}\\
&-\sum_{i=0}^{28}\sum_{s=1}^{29}
2i!(-1)^{b-1-i}c_s
\binom{i+s}{s}\Psi_{1,s-1,i+s}\\
&-\sum_{i=0}^{28}
2i!(-1)^{b-1-i}c_{29}\binom{-n}{29}
\Psi_{30,-1,i}\\
&+\sum_{h=0}^{28}v_h^Z\Psi_{0,h,0},
\end{aligned}
\tag{9.1}
$$


with coefficients taken modulo $p^2$.

The first three lines follow from (6.3):

- $s=0$ gives the first line;
- at positive coefficient order one, $a=0,r=0$ gives the second;
- the additional unit value $a=29,r=0,s=29$ gives the third.

All other terms have coefficient valuation at least two and are covered by the observable-order lemma.

### 9.1 The first finite return

Set


$$
\mathfrak d(x)=\sum_{i=0}^{28}(-1)^ii!\binom xi.
$$


The complete return is


$$
\boxed{
v_h^Z=
2\sum_{s=h+1}^{29}
c_s\binom{b+h}{s}
(-1)^{b+h-s}\mathfrak d(b+h-s)
\pmod{p^2},
\quad 0\le h\le28.
}
\tag{9.2}
$$



Here is a direct check.

The exterior source $C_{EI}P_-\widehat f$ is zero at coefficient order zero. At order one, the source formula has $a=r=0$, and


$$
\binom{-2n-1}{s-1-h}\equiv(-1)^{s-1-h}\pmod p.
$$


Also


$$
\binom{s+i}{s}\binom{b+h}{s+i}
=\binom{b+h}{s}\binom{b+h-s}{i}.
$$


Summing over $i$ gives (9.2).

The exterior source is supported in $0\le h\le28$ and is divisible by $p$. On this range $C_{EE}\equiv I\pmod p$, since every positive upper displacement is less than $p$. Hence its inverse does not alter this order-one source modulo $p^2$. This proves the return formula rather than merely naming a dictionary.

---

## 10. Complete second-column dictionary and retained exterior solve

At this coefficient precision, exact factorial filtration gives


$$
v_h^Y=0\pmod{p^2}\qquad(h\ge2).
$$


The retained exterior system is


$$
\begin{pmatrix}
1+7c_{29}&-2n\\
-n&1+7c_{29}
\end{pmatrix}
\binom{v_0^Y}{v_1^Y}
=
\binom{1}{-1}\pmod{p^2}.
\tag{10.1}
$$


Equivalently, its matrix is


$$
I+p\begin{pmatrix}9&-14\\-7&9\end{pmatrix}.
$$


The closed receipt is


$$
v_0^Y=1+6p,\qquad v_1^Y=-1+16p\pmod{p^2}.
\tag{10.2}
$$



Reusing it, rather than solving again, gives


$$
\begin{aligned}
\mathscr Y={}&
(1+6p)\Psi_{0,0,0}+(-1+16p)\Psi_{0,1,0}\\
&+\sum_{h=0}^{1}\sum_{s=1}^{29}
\varepsilon_hc_s\Psi_{0,h+s,s}\\
&+\sum_{h=0}^{1}
\varepsilon_hc_{29}\binom{-n}{29}\Psi_{29,h,0},
\end{aligned}
\tag{10.3}
$$


where $\varepsilon_0=1,\varepsilon_1=-1$.

The complete logarithmic force is omitted here only because its whole-row guard exceeds this fixed precision. It must return at primitive depth whenever that guard is insufficient.

The separate $W_be_b$ terminal is not included in (10.3). Its direct product is zero in $\kappa$, while its effect on the finite contact convention has already been retained.

---

# Part III. New sparse source-response identities

## 11. Only four interfaces occur in these short dictionaries

Consider either reconstructed branch of an atom in (9.1) or (10.3). Write its shifts as $(\alpha,v')$, so that


$$
a_0=16384+\alpha,\qquad b_0=5044+v'.
$$


The dictionaries satisfy


$$
0<b_0<20389<a_0+b_0<D.
\tag{11.1}
$$



For example, in the source family before the second reconstructed branch,


$$
\alpha+v=s,
$$


and the second branch increases this sum by one. Return and second-column atoms have the same nonnegative, small total shift. Thus $a_0+b_0$ lies near $21428$, safely between $20389$ and $24389$.

The outgoing interface is determined by the ordinary integer comparisons:



$$
\begin{array}{c|c}
\ell\text{ range}&\text{interface}\\ \hline
0\le\ell\le b_0&000\\
b_0<\ell\le20389&011\\
20389<\ell\le a_0+b_0&111\\
a_0+b_0<\ell<D&110.
\end{array}
\tag{11.2}
$$



This follows directly:

- the weight borrow is $1$ exactly when $\ell>20389$;
- the lower borrow is $1$ exactly when $\ell>b_0$;
- with a lower borrow, the addition carries exactly when $\ell\le a_0+b_0$;
- without a lower borrow, (11.1) forbids an addition carry.

Thus the interfaces


$$
100,\quad001,\quad101,\quad010
\tag{11.3}
$$


do not occur in these observable-order dictionaries.

This is stronger and more explicit than using only a ratio between upper kernels.

---

## 12. Leading profiles and weight-borrowed corrections have disjoint support

A leading normalized contribution has total low order one. The fourth-event argument ensures that it leaves $000$. Therefore


$$
a_\ell=g_\ell=0\qquad(\ell>20389).
\tag{12.1}
$$



Every $110$ or $111$ correction, on the other hand, is supported on $\ell>20389$. Hence, pointwise in $\ell$,


$$
a_\ell e_{\ell,110}=g_\ell c_{\ell,110}
=a_\ell e_{\ell,111}=g_\ell c_{\ell,111}=0.
\tag{12.2}
$$



Together with (11.3), this proves


$$
L_{100}=L_{001}=L_{101}=L_{111}
=L_{010}=L_{110}=0.
\tag{12.3}
$$



Recall


$$
\mu=L_{101}+L_{111},\qquad
\chi=L_{010}+22L_{110}.
$$


We have therefore proved


$$
\boxed{\mu=\chi=0.}
\tag{12.4}
$$



This does **not** assert that the individual exceptional coefficients are zero. A $110$ correction may be nonzero. It cannot meet a leading profile at the same low coordinate.

The remaining coefficient is


$$
\boxed{
\lambda
=\sum_{\ell=0}^{D-1}
\left(a_\ell d_\ell+g_\ell b_\ell
-a_\ell e_{\ell,011}-g_\ell c_{\ell,011}\right).
}
\tag{12.5}
$$



The exceptional $010/110$ channels remain present in the complete correction-product argument of §3; their absence from (12.5) is a separate pointwise support result.

---

## 13. A further finite-support reduction

For $000$, equation (11.2) requires $\ell\le b_0$.

The largest reconstructed $b_0$ in the first-column dictionary is


$$
5044+29=5073,
$$


but its potential extreme branch has row degree $58$ with coefficient already at the relevant paid order. A safe common assembly range is


$$
\boxed{0\le\ell\le5074.}
\tag{13.1}
$$


The second-column maximum is $5044+30=5074$.

It is unnecessary to rely on an additional endpoint pruning: using all $5\,075$ rows in (13.1) is small and safe. All remaining low rows make zero contribution to $\alpha,\delta,\lambda$.

The original split is still imposed at


$$
\ell=5044.
$$


It has not moved to a convenient auxiliary boundary.

---

# Part IV. Explicit event and unit extraction

## 14. Three-digit event computation

For a branch with shifts $(\alpha,v')$, expand


$$
20389=\sum_{t=0}^2N_tp^t,\quad
16384+\alpha=\sum_{t=0}^2a_tp^t,\quad
5044+v'=\sum_{t=0}^2b_tp^t,\quad
\ell=\sum_{t=0}^2j_tp^t.
$$



Start


$$
w_{-1}=k_{-1}=c_{-1}=0.
$$


For $t=0,1,2$, perform:

1. **Weight subtraction**
   

$$
u=N_t-j_t-w_{t-1},\qquad
   l_t=u\bmod p,\qquad w_t=\mathbf1_{u<0}.
$$



2. **Lower-index subtraction**
   

$$
v=b_t-j_t-k_{t-1},\qquad
   k_t^{\rm dig}=v\bmod p,\qquad k_t=\mathbf1_{v<0}.
$$



3. **Addition**
   

$$
z=a_t+k_t^{\rm dig}+c_{t-1},\qquad
   z_t=z\bmod p,\qquad c_t=\mathbf1_{z\ge p}.
$$



Then


$$
e=\sum_{t=0}^2(w_t+c_t),\qquad s=(w_2,k_2,c_2).
\tag{14.1}
$$


The stripped low unit is


$$
\boxed{
L=(-1)^e
\prod_{t=0}^2
\frac{N_t!\,z_t!}
 {j_t!\,l_t!\,a_t!\,k_t^{\rm dig}!}
\pmod p.
}
\tag{14.2}
$$


Only factorials below $29$ are inverted.

---

## 15. The $JK$ coefficient is a harmonic response of the leading atom

Define


$$
H_r=\sum_{a=1}^{r}a^{-1}\pmod p,\qquad H_0=0.
$$


For a leading $000$ atom, put


$$
\boxed{
\Gamma=H_{l_2}+H_{k_2^{\rm dig}}-H_{j_2}-H_{z_2}\pmod p.
}
\tag{15.1}
$$



Then its first-order $JK$ coefficient is its leading coefficient multiplied by $\Gamma$.

Here is the unit-factor proof. For $x=pq+r$, $0\le r<p$,


$$
\prod_{\substack{1\le a\le x\\p\nmid a}}a
\equiv
((p-1)!)^q\,r!\,(1+pqH_r)\pmod{p^2}.
\tag{15.2}
$$


The complete $p$-blocks are independent of their block index modulo $p^2$, because $\sum_{a=1}^{p-1}a^{-1}=0\pmod p$.

Apply (15.2) at the three stripped factorial levels. At the first two levels, the $J$-dependence is multiplied by an additional $p$ and disappears modulo $p^2$. At the third level, the high factorial arguments are


$$
W,\quad A+B-J-k+c,\quad
J,\quad W-J-w,\quad A,\quad B-J-k.
$$


Their logarithmic $J$-derivative is exactly (15.1). Hence


$$
U(J)=U(0)(1+pJ\Gamma)\pmod{p^2}.
\tag{15.3}
$$



There is no missing row-binomial contribution at this order:

- coefficient-order-one terms have row factors periodic modulo $p^2$;
- unit first-column source terms have row degree below $29$;
- the unit second-column exceptional reconstruction factor is $j=\ell+D J$, whose difference from $\ell$, even after its possible division by $p$, is zero modulo $p^2$.

Thus (15.1) is the complete $JK$ extraction needed for this row.

---

## 16. Branch-by-branch extraction rule

For an atom $T\Psi_{\alpha,v,r}$, make two branches:



$$
\begin{array}{c|c|c}
\text{branch}&v'&\text{signed row coefficient }C_\ell\\ \hline
1&v&(-1)^vT\binom\ell r\\
2&v+1&(-1)^vT(r+1)\binom\ell{r+1}.
\end{array}
\tag{16.1}
$$



The common sign in the two rows is correct: the minus sign in reconstruction is cancelled by the extra negative-binomial sign in the second branch.

Compute $e,s,L,\Gamma$ from §§14–15.

### Leading and $JK$ extraction

If


$$
v_p(C_\ell)+e=1,
$$


the interface is $000$, and the branch contributes


$$
A_\ell=p^{e-1}C_\ell L\pmod p
\tag{16.2}
$$


to the leading profile, and


$$
A_\ell\Gamma
\tag{16.3}
$$


to its $JK$ coefficient.

### $011$ extraction

If


$$
s=011,\qquad v_p(C_\ell)+e=2,
$$


the branch contributes


$$
C_{\ell,011}=p^{e-2}C_\ell L\pmod p
\tag{16.4}
$$


to the $011$ correction.

All displayed divisions are paid:

- in (16.2), $e=0$ requires $p\mid C_\ell$;
- in (16.4), $e=1$ requires $p\mid C_\ell$;
- $e=0,s=011$ is impossible.

Only $C_\ell\bmod p^2$ is needed. A coefficient known to be zero modulo $p^2$ cannot affect these extractions.

---

# Part V. Complete bounded arithmetic specification

## 17. Exact inputs

The assembly uses the following bounded data.

### 17.1 Original low residues and parity

Use


$$
\boxed{
b\bmod p^3=5044,\qquad n\bmod p^3=20387,\qquad b\text{ odd}.
}
\tag{17.1}
$$


The parity is supplied separately; the small residue $5044$ must not be used as the parity of the original $b$.

These residues suffice. The small lower indices are at most $58<p^2$. Integer-valued binomial continuity loses at most one $p$-adic digit, so inputs modulo $p^3$ determine the required binomial coefficients modulo $p^2$.

### 17.2 Short arrays

Construct:

- factorials and inverse factorials modulo $p$, indices $0,\ldots,28$;
- harmonic numbers $H_r\bmod p$, indices $0,\ldots,28$;
- $T_s$, $0\le s<29$, by (8.2);
- $c_s\bmod p^2$, $0\le s\le29$, by (8.1);
- the $58$-entry $\widehat f$ by (8.3)–(8.4);
- the $29$-entry return $v_h^Z$ by (9.2);
- the retained exterior values
  

$$
v_0^Y=175,\qquad v_1^Y=463\pmod{841}.
$$



### 17.3 Binomial evaluation

For the first source line, evaluate


$$
\binom{2n+r-1}{r}\pmod{p^2},
\qquad 0\le r\le57,
$$


using $n=20387$ as a residue representative.

A verifiable procedure is to form the bounded numerator product and $r!$, remove their exact powers of $p$, and invert only the remaining unit denominator. Since $r\le57$, the denominator has valuation at most one. Precision $p^3$ before that removal is sufficient.

For


$$
\binom{-n}{29}\pmod p
$$


one may use the exact integer product with the same paid division, or Lucas:


$$
\binom{-n}{29}\equiv-7=22\pmod p.
$$



All other binomials in the atom coefficients have bounded nonnegative arguments and may be computed by exact Pascal recurrence.

---

## 18. Assembly instructions

1. Form all atom coefficients in (9.1) and (10.3) modulo $841$.

2. Delete coefficients that are zero modulo $841$. This is legitimate by the observable-order lemma and the extraction rules.

3. For every
   

$$
0\le\ell\le5074,
$$


   process both reconstructed branches of every retained atom.

4. Accumulate six arrays modulo $29$:
   

$$
a_\ell,\ b_\ell,\ c_{\ell,011},
   \qquad
   g_\ell,\ d_\ell,\ e_{\ell,011}.
$$



5. Return
   

$$
\boxed{
   \alpha=\sum_{\ell=0}^{5074}a_\ell g_\ell,
   }
   \tag{18.1}
$$


   

$$
\boxed{
   \delta=\sum_{\ell=5044}^{5074}a_\ell g_\ell,
   }
   \tag{18.2}
$$


   

$$
\boxed{
   \lambda=\sum_{\ell=0}^{5074}
   \left(
   a_\ell d_\ell+g_\ell b_\ell
   -a_\ell e_{\ell,011}-g_\ell c_{\ell,011}
   \right),
   }
   \tag{18.3}
$$


   together with the proved entries
   

$$
\boxed{\mu=0,\qquad\chi=0.}
   \tag{18.4}
$$



These instructions do not contain an undefined “exact dictionary” step: the dictionaries, their coefficients, both returns, and the extraction functional have all been displayed.

---

## 19. Precision ledger

| Operation | Required information before division | Result |
|---|---|---|
| $E=(P^p-P(z^p))/p$ | Numerator coefficients modulo $p^2$, or exact integers | $E\bmod p$ |
| Small binomial with lower index $29\le r\le57$ | Numerator and denominator with exact $p$-valuation; numerator modulo $p^3$ | Binomial modulo $p^2$ |
| $c_s/p$ | $c_s\bmod p^2$ | $\sigma_s\bmod p$ |
| Leading extraction with $e=0$ | $C_\ell\bmod p^2$, with $p\mid C_\ell$ proved | $C_\ell/p\bmod p$ |
| $011$ extraction with $e=1$ | $C_\ell\bmod p^2$, with $p\mid C_\ell$ proved | $C_\ell/p\bmod p$ |
| Low factorial ratios | Factorials $<p$ only | Unit inversion modulo $p$ |
| Exterior solve | Retained unit matrix (10.1) and right side | Reuse (10.2); no new solve |

No division by $A+B-J$ occurs on the exceptional residue.

---

## 20. Resource estimate and expected certificate

After removing coefficient-order-two terms, a safe atom count is:

- first source line: at most $493$ atoms;
- second source line: $841$;
- third source line: $29$;
- first return: $29$;
- second-column dictionary: $62$.

Thus at most


$$
1454
$$


atoms and


$$
2\cdot1454\cdot5075=14\,758\,100
$$


branch-row evaluations are needed.

A Pascal table


$$
\binom\ell r\bmod841,\qquad
0\le\ell\le5074,\quad0\le r\le58,
$$


has fewer than $300\,000$ entries. The six output profiles have $30\,450$ entries.

A straightforward implementation therefore needs only a few megabytes of storage. A conservative arithmetic estimate is several hundred million small modular operations, rather than an original-word traversal or a large dense transition construction. More aggressive caching is optional, not part of the proof.

### Required verifiable output

The coordinator’s certificate should contain:

1. $(\alpha,\delta,\lambda,0,0)\in\mathbb F_{29}^5$;
2. separate subtotal checks for $\ell<5044$ and $\ell\ge5044$;
3. source and return subtotals in each column;
4. confirmation that every leading contribution leaves $000$;
5. confirmation of the interval classification (11.2);
6. counts of retained atoms and paid divisions;
7. the final identity
   

$$
\kappa=25A_W(\alpha S-\delta k_B^2+\lambda T)\pmod{29}.
$$



This finite calculation would settle exactly the low coefficient row. It would not evaluate the original high word.

---

# Part VI. Consequences and remaining obligations

## 21. The reduced complete observation

Retain


$$
S=\frac{\sum_{J=0}^{B}K(J)^2}{p^2},\qquad
T=\frac{\sum_{J=0}^{B}J K(J)^2}{p},\qquad
k_B=K(B)/p
\pmod p.
$$


The boundary-correct formula and §§11–12 give


$$
\kappa=A_q\bigl(\alpha S-\delta k_B^2+\lambda T\bigr)\pmod p.
\tag{21.1}
$$



The exact original relation


$$
q=29W+24
$$


and the retained digit computation give


$$
A_q=25A_W\pmod p,
$$


with $A_W\ne0\pmod p$. Therefore (A) follows.

The source-response identity is genuinely sparse: the second moment $V$ and exceptional paid observation $E$ are no longer needed for this fixed-layer accepting value. This removes two upper observations without claiming that either observation itself vanishes.

No theorem here forces $\alpha,\delta,\lambda$ individually to vanish. The remaining $JK$ harmonic response and the $011$ boundary-interface response can overlap the leading profiles. Their cancellation, if it occurs, is an arithmetic fact to be established by (18.1)–(18.3), not a consequence of the radical alone.

---

## 22. What a zero low row would settle

If the bounded certificate gives


$$
\alpha=\delta=\lambda=0,
$$


then


$$
\kappa=0
$$


for every original continuation in the reviewed fixed-layer scope, without evaluating the original high word.

If the row is nonzero, the remaining task is evaluation of


$$
\alpha S-\delta k_B^2+\lambda T
$$


on the actual upper words


$$
B=\frac{3^{249005515+574312172u}-5044}{29^3},
\qquad u\ge0,\quad u\equiv2\pmod{29^9}.
$$


A nonzero coefficient row does not imply a nonzero accepting value.

This is the precise consequence that the low calculation can settle. It does not prove an infinite original-index nonzero statement.

---

## 23. Primitive depth remains a different problem

Write


$$
Z_w=p^{c+2}x,\qquad
\nu=v_p(x^Tx),\qquad d=2c+4+\nu.
$$


The true depth remains


$$
K=d-c=c+4+\nu.
$$



The complete retained approximation is


$$
Y^{[K]}
=
\mathcal R\theta^{(e,[K])}
+W_be_b
+\mathcal RA^{-1}r^{(F,[K])},
$$


with the logarithmic head retained whenever its guard does not pay its omission.

The proved tail separation is


$$
Z_w^T(Y-Y^{[K]})\in p^{d+2}\mathbb Z_p.
$$


The unresolved primitive contraction is still


$$
\boxed{
x^TY^{[K]}-p^{c+3}\rho_nx^Tx
\pmod{p^K}.
}
\tag{23.1}
$$



Neither (A) nor a zero fixed-layer row evaluates (23.1). The valuation and required precision of $\rho_n$ must be paid separately; $p$-integrality cannot be assumed.

---

## 24. Actual contents, least clearer, final gcd, and whole error

Nothing in the low-profile normalization changes the original row contents or the least simultaneous clearer $d_B$.

Retain


$$
\omega_j=\frac{(n+2)!}{(n+2-j)!},\qquad
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2),
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


The gcd is over **all primes**, and the actual primitive multiplier remains


$$
d_B^2/g_B.
$$



At the same original index,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
\qquad
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$


The retained signed-error theorem supplies eventual nonzero whole error and


$$
\log|\epsilon_n|
=-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$



An irrationality proof still requires an all-prime bound on the actual primitive denominator making


$$
0<|q_n\epsilon_n|\longrightarrow0
$$


on the **same infinite original indices**. No selected-prime fixed-layer result in this report supplies that comparison.

---

## 25. Final ledger

| Statement | Status |
|---|---|
| Full weighted interface radical, including $JK$ and $J^2K^2$ uses | Derived from the explicitly stated retained ordinary radical and exceptional reflection |
| Observable flat-head quotient | Retained, with complete-response and terminal dependencies made explicit |
| Non-$000$ first-correction invariance under discarded head directions | Proved by the event/return argument |
| Coefficient-order-two omission from this particular low row | Proved |
| Extension of the short Turn 16 dictionaries to the whole low row | Proved at observable scope |
| Only $000,011,111,110$ occur in those dictionaries | Proved |
| $\mu=\chi=0$, $\lambda=\tau-L_{011}$ | **New proved sparse-row identities** |
| Values of $\alpha,\delta,\lambda$ | Not executed here; fully bounded specification supplied |
| Original high-word accepting value | Unevaluated unless the remaining row is certified zero |
| Primitive contraction at $K=c+4+\nu$ | Open |
| $\rho_n$-integrality and required precision | Separate open input obligation |
| All-prime denominator versus whole same-index error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The new result is a complete-source support identity:


$$
\boxed{
(\alpha,\delta,\lambda,\mu,\chi)
=(\alpha,\delta,\tau-L_{011},0,0).
}
$$


It preserves both finite returns, the original $\ell=5044$ split, the exceptional channels at their actual scope, and the separate physical terminal.

The immediate remaining bounded obligation is the three-residue calculation (18.1)–(18.3). It needs only the short arrays and explicit atoms given here; it does not need a new exterior solve or a generic Cartier enlargement. Its expected output is an auditable low row, not an assertion about an unevaluated enormous exponent word.

After that calculation, the exact fixed-layer bottleneck is either removed by a certified zero row or reduced to the actual-word evaluation of three upper observations. The growing-depth primitive contraction, $\rho_n$-precision, and the all-prime comparison with the nonzero whole error remain separate and unresolved.
