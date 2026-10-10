> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 16 — The exceptional channel vanishes, and the actual head reduces to one observable

## Executive assessment

The exceptional channel does **not** produce a new nonzero contribution to the next physical mixed coefficient.

Its definition was already present in the eight-interface factorial strip. What is new here is its explicit evaluation on the previously excluded residue $J_0=14$. The shifted channel has the digit kernel


$$
\boxed{
K_{010}(14+29^2r+29^3q)
\equiv
22\binom{20}{r}
\begin{cases}
F_{\rm I}(q)/29,&0\le r\le9,\\
F_{\rm II}(q)/29,&10\le r\le20
\end{cases}
\pmod{29}.
}
$$


All other indices on that residue give zero modulo $29$. The displayed division by $29$ is paid by the retained upper forcing theorem.

Consequently,


$$
\boxed{\mathcal E_{\rm exc}=0\pmod{29}.}
$$


In fact, on the reviewed cylinder, the same lifted reflection already used in Turn 12 proves the stronger statement


$$
\boxed{
\sum_{\substack{0\le J\le B\\J\equiv14\;(\mathrm{mod}\ 29)}}
K_{010}(J)^2\equiv0\pmod{29^2}.
}
$$


No new universal scalar, and no reevaluation of $\Xi=17$, is needed.

This resolves one named term of the **whole** mixed sum:


$$
\boxed{\sum_{\ell,J}B_\ell(J)E_\ell(J)=0\pmod{29}.}
$$


Thus Turn 15’s rank-at-most-one Gram matrix is actually zero on the stated family.

There is also an actual observable reduction for the first head. At this fixed physical layer, all higher head digits can be eliminated from the mixed observation—not merely represented by a 371-coordinate module. The result is


$$
\boxed{
\kappa(u)=A_q\,\kappa_{\mathrm{flat}}(b)\pmod{29},
\qquad
q=\frac{69b-7}{29}.
}
$$


Here $\kappa_{\mathrm{flat}}$ uses an explicitly specified, fixed 58-entry head. This quotient is closed for every original compatible continuation. It does **not** evaluate the remaining upper-digit mixed observation, nor make traversal of the original enormous digit word feasible.

Below I also give explicit assembled formulas for


$$
c_{\ell,010}+22c_{\ell,110},
\qquad
e_{\ell,010}+22e_{\ell,110},
$$


including the source contribution and the finite return in each column. They are coefficient formulas, not a claim that their $24\,389$-entry tables have been numerically certified.

The complete coefficient $\kappa$, primitive alignment on an infinite original subsequence, and the all-prime denominator/error comparison remain open.

---

## 1. Preserved setting

Write


$$
p=29,\qquad D=p^3,
$$




$$
b=3^{249005515+574312172u}=410910916+p^6C,\qquad n=2001b,
$$


and work on


$$
u\equiv2\pmod{p^9}.
$$



The original domains remain


$$
0\le j<b,\qquad 1\le i\le b-2,\qquad 0\le j\le b
$$


for contact coordinates, recurrence source rows, and reconstructed coordinates, respectively.

The actual columns are


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,
$$


where


$$
W_j=\binom{n+2}{j},\qquad
(\mathcal Rx)_j=W_j(jx_{j-1}-x_j),\qquad x_{-1}=x_b=0.
$$


In particular, the physical terminal is not a continued contact atom.

Retain


$$
Z_w=p^{c+2}x,\qquad
\nu=v_p(x^Tx),\qquad d=2c+4+\nu,
$$


and


$$
F=Z_w/p^4,\qquad G=Y/p^4,\qquad Q=pG.
$$


The accepted conclusions give


$$
F,G\in\mathbb Z_p^{b+1},\qquad d\ge10,\qquad F^TG\in p^2\mathbb Z_p.
$$


The target is


$$
\kappa=\frac{F^TG}{p^2}\pmod p.
$$



I reuse the exact factorial filtration. The actual second-column exterior solve has:

- $118$ coordinates $h=0,\ldots,117$ at precision $p^6$;
- $147$ coordinates $h=0,\ldots,146$ at precision $p^7$.

These sizes are not replaced by the older staircase envelopes.

---

# Part I. Explicit evaluation of the exceptional channel

## 2. Shift the binomial before reducing it

The upper parameters are


$$
W=7663+DX,\qquad B=16848+DC,\qquad A=15327+2DX,
$$


where


$$
X=2001C+1382.
$$


Their three low digits are


$$
W:(7,3,9),\qquad B:(28,0,20),\qquad A:(15,6,18).
$$



The exceptional kernel is exactly


$$
K_{010}(J)=\frac1{p^3}
\binom WJ\binom{A+B-J-1}{B-J-1},
\tag{2.1}
$$


with value zero when $B-J-1<0$.

Thus it is the ordinary two-binomial kernel with the cutoff shifted from $B$ to $B-1$. One must make this shift **before** reducing modulo $p$. Dividing the ordinary kernel by $A+B-J$ on $J_0=14$ is not legitimate.

Put


$$
J=14+pj_1+p^2j_2+Dq.
$$



### First digit

At digit zero:

- the weight subtraction $7-14$ borrows;
- the lower subtraction is $28-14-1=13$, with no borrow;
- $15+13=28$, with no addition carry.

There is exactly one event, and the outgoing state is


$$
(w,k,c)=(1,0,0).
$$



### Second digit

At digit one the possibilities are:

| $j_1$ | outgoing state | number of events at this digit |
|---|---|---:|
| $0$ | $000$ | $0$ |
| $1,2$ | $011$ | $1$ |
| $3,\ldots,6$ | $111$ | $2$ |
| $7,\ldots,28$ | $110$ | $1$ |

If $j_1\ne0$, the third digit supplies at least one further event. The retained later forcing supplies at least one event for every incoming interface. Such terms therefore have total valuation at least four and vanish after division by $p^3$, modulo $p$.

For $j_1=0$, the third digit has exactly one event precisely when


$$
0\le j_2\le20.
$$


Its outgoing state is


$$
001\quad(0\le j_2\le9),\qquad
100\quad(10\le j_2\le20).
$$



This proves that the only possible support modulo $p$ on the exceptional residue is


$$
\boxed{J=14+p^2r+Dq,\qquad 0\le r\le20.}
\tag{2.2}
$$



---

## 3. The paid digit kernel

Use the existing high factors


$$
V(q)=\binom Xq\binom{2X+C-q}{C-q},
$$




$$
F_{\rm I}(q)=(2X+C-q+1)V(q),\qquad
F_{\rm II}(q)=(X-q)V(q).
$$



For (2.2), the first three digits supply exactly $p^2$. The remaining factorial ratio is $F_{\rm I}$ or $F_{\rm II}$. Both are divisible by $p$ at the retained scope.

The stripped low unit is


$$
\frac{3\,7!\,28!}{14!\,22!\,15!\,13!}
\frac{9!}{18!\,r!\,(20-r)!}
\equiv22\binom{20}{r}\pmod{29}.
\tag{3.1}
$$


The cancellation giving the second fraction is the same in both ranges $r\le9$ and $r\ge10$.

Therefore


$$
\boxed{
K_{010}(14+p^2r+Dq)
\equiv22\binom{20}{r}
\begin{cases}
F_{\rm I}(q)/p,&r\le9,\\
F_{\rm II}(q)/p,&r\ge10
\end{cases}
\pmod p.
}
\tag{3.2}
$$



This is an explicit digit kernel, not an unevaluated original-length sum.

### Exact finite ranges and boundary zero

Because


$$
14+p^2r<16848\qquad(0\le r\le20),
$$


both branches in (3.2) have exactly


$$
0\le q\le C.
$$



Moreover,


$$
H_{010}(B)=0
$$


by its negative lower index. Consequently the exceptional scalar is identical for the two original interior ranges


$$
J\le B\quad(\ell<5044),\qquad
J\le B-1\quad(\ell\ge5044).
$$


No physical terminal has been substituted for this boundary zero.

---

## 4. Its whole square sum is the old radical, not a new witness

Let


$$
H_{\rm I}=\sum_{q=0}^{C}(F_{\rm I}(q)/p)^2,\qquad
H_{\rm II}=\sum_{q=0}^{C}(F_{\rm II}(q)/p)^2.
$$



The elementary half-sums are


$$
\sum_{r=0}^{9}\binom{20}{r}^2=10,\qquad
\sum_{r=10}^{20}\binom{20}{r}^2=19
\pmod{29}.
\tag{4.1}
$$


For example, symmetry and Vandermonde give their sum as
$\binom{40}{20}=0\pmod{29}$, while the central square is
$\binom{20}{10}^2=9$.

Equation (3.2) now gives


$$
\mathcal E_{\rm exc}
=22^2(10H_{\rm I}+19H_{\rm II})
=26(H_{\rm I}-H_{\rm II})
\pmod{29}.
$$


The already-proved branch reflection gives $H_{\rm I}-H_{\rm II}=0$. Hence:

### Theorem 4.1 — Exceptional Gram cancellation
For every compatible original continuation on the reviewed phase,


$$
\boxed{\mathcal E_{\rm exc}=0\pmod{29}.}
\tag{4.2}
$$



This is not a new Frobenius radical. It is a new connection of the shifted exceptional channel to the **existing** branch-reflection radical.

Combined with Turn 15’s rank-one relation,


$$
\boxed{
\sum_JK_s(J)K_t(J)=0\pmod{29}
\quad\text{for all eight interfaces }s,t.
}
\tag{4.3}
$$



---

## 5. The lifted exceptional square also vanishes on the reviewed cylinder

The preceding argument can be lifted one step without calculating another universal scalar.

Only the same minimal paths contribute to the exceptional square modulo $p^2$: every other path has $K_{010}\in p\mathbb Z_p$.

The low unit on each minimal path is affine in the high index modulo $p^2$, by the already-established factorial-strip lift. Thus its complete square has the form


$$
\alpha_{\rm I}H_{\rm I}+\alpha_{\rm II}H_{\rm II}
+p\beta_{\rm I}H_{\rm I}^{[1]}
+p\beta_{\rm II}H_{\rm II}^{[1]}
\pmod{p^2},
\tag{5.1}
$$


with


$$
\alpha_{\rm I}\equiv26,\qquad
\alpha_{\rm II}\equiv-26\pmod p.
$$


These coefficients concern this shifted channel; they are not being identified with the previously evaluated $\alpha$'s for the ordinary channel.

Turn 12 already proves


$$
\frac{H_{\rm I}-H_{\rm II}}p=22\,\mathcal H(t)\pmod p,
$$




$$
H_{\rm I}=H_{\rm II}=13\mathcal H(t)\pmod p,
$$




$$
H_{\rm I}^{[1]}=11\mathcal H(t),\qquad
H_{\rm II}^{[1]}=22\mathcal H(t)\pmod p.
$$


Since $\mathcal H(t)=0$ on the reviewed cylinder, every term in (5.1) vanishes modulo $p^2$. Therefore


$$
\boxed{
\sum_{\substack{0\le J\le B\\J_0=14}}K_{010}(J)^2
\in p^2\mathbb Z_p.
}
\tag{5.2}
$$



This advances the lifted channel using closed results. It requires neither a new “exceptional $\Xi$” nor an old computation.

---

# Part II. The actual head observable is much smaller than the proposed head module

## 6. A guarded normal form for arbitrary short input rows

The following extension is needed to distinguish an actual observable quotient from a generic head representation.

Let


$$
T_i=\mathcal RA^{-1}e_i,\qquad 0\le i\le202.
$$


At precision $p^7$, the complete finite normal form for these responses has consolidated $2n$-atoms satisfying the safe bounds


$$
0\le\alpha\le377,\qquad -203\le v\le174,
\tag{6.1}
$$


with reconstructed row-binomial degrees at most $377<841$.

Here is a direct support derivation.

Write the finite input after Pascal conversion as


$$
(P_-f)_k=\sum_i(-1)^{k-i}\binom ki f_i.
$$


Using the displayed kernel for $\mathcal C_\infty$, the source part
$(\mathcal C_\infty)_{II}P_-f$ is a sum with


$$
0\le s\le174,\quad 0\le a\le s,\quad 0\le r\le i\le202.
$$


Finite hockey-stick summation gives the contact atom


$$
\binom j{s-a+i-r}
\binom{-2n-a-r-1}{b-1-r+s-a-j}.
\tag{6.2}
$$


Its upper shift is $\alpha=a+r+1$, and its lower shift is
$v=-1-r+s-a$, proving the source part of (6.1).

The finite correction is exactly


$$
-(\mathcal C_\infty)_{IE}
(\mathcal C_\infty)_{EE}^{-1}
(\mathcal C_\infty)_{EI}P_-f.
\tag{6.3}
$$


A term entering $E$ with total symbol valuation $t$ reaches at most
$h\le29t-1$. Subsequent lower displacements cost their corresponding symbol valuations; upper-triangular factors do not increase the largest index. Before total order seven, reconstruction therefore gives $v\le174$. This proves the return bound without deleting any return.

The bounds preserve the low three-digit remainders:


$$
4841\le5044+v\le5218,\qquad
16384\le16384+\alpha\le16761.
$$


Thus the retained three-event forcing applies to every atom:


$$
\boxed{T_i\in p^3\mathbb Z_p^{b+1}\quad(0\le i\le202).}
\tag{6.4}
$$



This auxiliary return bound is not a replacement for the sharper $147$-coordinate factorial-data solve for the actual second column.

---

## 7. Two mixed divisibilities eliminate the unnecessary head digits

The leading profile of $T_i/p^3$ enters through $000$.

Indeed, a coefficient-unit contribution has no low event. Hence its outgoing weight borrow and addition carry are zero. An outgoing lower-index borrow would require


$$
\ell+K_{\rm low}=D+5044+v,
$$


whereas


$$
\ell+K_{\rm low}\le20389+8004-\alpha=28393-\alpha
< D+4841.
$$


It is impossible.

At the next order, the same eight-interface strip and row-periodicity argument applies. Contracting against $G$, the existing enlarged radical and


$$
\sum_JK(J)^2\in p^2\mathbb Z_p
$$


therefore give


$$
\boxed{T_i^TY\in p^9\mathbb Z_p,\qquad 0\le i\le202.}
\tag{7.1}
$$



For the short factorial head


$$
h_i^{[0]}=
\begin{cases}
i!,&0\le i<29,\\
0,&i\ge29,
\end{cases}
$$


the previously proved fourth-event argument gives
$\mathcal RA^{-1}h^{[0]}\in p^4$. Applying the same mixed contraction yields


$$
\boxed{
(\mathcal RA^{-1}h^{[0]})^TY\in p^{10}\mathbb Z_p.
}
\tag{7.2}
$$



Consequently, modulo $p^{11}$:

- changing any $f_i^0$, $i\le202$, by a multiple of $p^2$ changes $Z_w^TY$ by zero;
- changing the first head by $p\delta h^{[0]}$ changes it by zero;
- rows $i\ge203$ are already paid by the original $p^7$ head truncation and $Y\in p^4$.

Thus the complete $\kappa$-observation needs only the actual first head modulo $p^2$, modulo the additional direction $ph^{[0]}$.

---

## 8. Assemble those actual head entries

Put


$$
\mathscr P(z)=1+2z+2z^2,\qquad
E(z)=\frac{\mathscr P(z)^p-\mathscr P(z^p)}p\in\mathbb Z[z].
$$


For $0\le i<29$, define the fixed residues


$$
\xi_i=[z^{29}]E(z)((1+z)^i-1),\qquad
\zeta_i=[z^{58}]E(z)((1+z)^i-1),
$$


and let


$$
\mathsf H_i=\sum_{a=1}^i a^{-1}\pmod{29}.
$$



Write $m=n/p=7+pq$. Expanding $\mathscr P^{pm}$ modulo $p^2$ gives


$$
\frac{J_i-J_0}{p}
=
7(\xi_i B_m+\zeta_i C_m)\pmod p.
$$


Using the accepted actual relation


$$
(A_m,B_m,C_m,D_m)=(2,14,8,24)A_q\pmod p,
$$


we obtain


$$
f_i^0
\equiv
J_0 i!+
pA_q\,7i!(2\mathsf H_i+14\xi_i+8\zeta_i)
\pmod{p^2},
\qquad i<29.
\tag{8.1}
$$



For $i=29+r$, $0\le r<29$,


$$
\frac{(n+i)!}{p\,n!}\equiv-8r!,
\qquad
J_i\equiv A_m+D_m=26A_q,
$$


so


$$
\boxed{f_{29+r}^0/p=24r!A_q\pmod p.}
\tag{8.2}
$$


All rows $i\ge58$ vanish modulo $p^2$.

Define the fixed 58-entry head $\widehat f$, modulo $p^2$, by


$$
\widehat f_i=
2i!+
p\,7i!(2\mathsf H_i+14\xi_i+8\zeta_i),
\qquad 0\le i<29,
\tag{8.3}
$$




$$
\widehat f_{29+r}=p\,24r!,\qquad0\le r<29.
\tag{8.4}
$$



Equations (8.1)–(8.4) say precisely


$$
f^0-A_q\widehat f
\in p\mathbb Z_p\,h^{[0]}+p^2\mathbb Z_p^{203}
+p^7\mathbb Z_p^b,
$$


with the last term denoting the paid original tail.

### Theorem 8.1 — Closed actual-head observable quotient
Let


$$
\widehat Z=\mathcal RA^{-1}\widehat f.
$$


Then $\widehat Z\in p^4$, and


$$
\boxed{
\kappa(u)=A_q\,\frac{\widehat Z^TY}{p^{10}}\pmod p.
}
\tag{8.5}
$$



This is an identity for the actual complete columns. It is not an arbitrary assignment of head scalars.

### Actual suffix input and closure

The only unread first-head input is now


$$
q=\frac{69b-7}{29},
\qquad
A_q=\operatorname{CT}(z^{-1}+2+2z)^q\pmod{29}.
$$


Its digit transition is the classical one-dimensional Lucas transition


$$
a\longmapsto aA_d
$$


when a base-$29$ digit $d$ is read.

The unread word must be the actual remaining digit word of this $q$. Low residues of $u$ do not authorize an arbitrary replacement word.

The head quotient is closed for every compatible continuation, by (7.1)–(8.5). The **whole mixed upper observation** is not thereby evaluated. No 371-coordinate transition certificate or 6.9-million-entry construction is needed for this head reduction.

---

# Part III. Explicitly assembled exceptional coefficients

## 9. A low extraction functional

For


$$
\Psi_{\alpha,v,r}(j)=W_j\left[
\binom jr\binom{-2n-\alpha}{b+v-j}
-(r+1)\binom j{r+1}
\binom{-2n-\alpha}{b+v+1-j}
\right],
\tag{9.1}
$$


the sign after extracting $(-1)^{b-\ell-J}$ is $(-1)^v$ in **both** reconstructed terms.

For an individual positive-binomial atom, let

- $e_{\alpha,v}(\ell)$ be its exact number of low weight-borrow and addition-carry events;
- $s_{\alpha,v}(\ell)$ its outgoing interface;
- $L_{\alpha,v}(\ell)\in\mathbb F_p^\times$ its stripped low unit.

These are explicit three-digit quantities. In digit factorials,


$$
L_{\alpha,v}(\ell)
=(-1)^{e_{\alpha,v}(\ell)}
\prod_{t=0}^{2}
\frac{w_t!\,z_t!}{j_t!\,l_t!\,a_t!\,k_t!},
\tag{9.2}
$$


using the actual subtraction and addition digits for


$$
n+2-\ell,\qquad b+v-\ell,\qquad
(2n+\alpha-1)+(b+v-\ell).
$$


Only factorials below $29$ are inverted.

The interface $010$ is impossible throughout the guarded boxes: its zero weight borrow and addition carry give the same contradictory inequality used in §7. Therefore


$$
\boxed{c_{\ell,010}=e_{\ell,010}=0.}
\tag{9.3}
$$



Define a linear extraction on a term $T\Psi_{\alpha,v,r}$ by


$$
\begin{aligned}
\mathfrak X_\ell(T\Psi_{\alpha,v,r})
=22(-1)^vT\bigg[
&\mathbf1_{s_{\alpha,v}=110}
p^{e_{\alpha,v}-2}\binom\ell r L_{\alpha,v}\\
+&\mathbf1_{s_{\alpha,v+1}=110}
p^{e_{\alpha,v+1}-2}(r+1)\binom\ell{r+1}L_{\alpha,v+1}
\bigg]\pmod p,
\end{aligned}
\tag{9.4}
$$


discarding terms with $e>2$.

The divisions for $e=1$ are paid:

- positive-order source coefficients supply $p$;
- the coefficient-unit first-column sector has an earlier low event, so cannot have $e=1$ at $110$;
- in the exceptional coefficient-unit second-column case, the reconstruction factor $j$ supplies $p$.

Thus (9.4) is an integral extraction, not division of a nonintegral summand.

---

## 10. The source and finite return of the first column

Let


$$
c_s=s![z^s]\phi(z)^{-n}.
$$


At coefficient precision $p^2$, only $s\le29$ is needed for (9.4). Their required values are explicit:


$$
c_0=1,\qquad c_{29}/p=22\pmod p,
$$


and, for $1\le s<29$,


$$
c_s/p=7(s-1)!\,T_s\pmod p,
$$


where


$$
T_0=2,\quad T_1=1,\quad T_s=T_{s-1}-\tfrac12T_{s-2}.
\tag{10.1}
$$



Put


$$
\mathfrak d(z)=\sum_{i=0}^{28}(-1)^i i!\binom zi.
$$



The following is the assembled coefficient-level dictionary for the flat first head, sufficient for its exceptional first correction:


$$
\begin{aligned}
\mathscr Z_{\rm exc}={}&
-\sum_{i=0}^{57}\sum_{r=0}^{i}
\widehat f_i(-1)^{b-1-r-i}
\binom{2n+r-1}{r}\,
\Psi_{r+1,-1-r,i-r}\\
&-\sum_{i=0}^{28}\sum_{s=1}^{29}
2i!(-1)^{b-1-i}c_s
\binom{i+s}{s}\,
\Psi_{1,s-1,i+s}\\
&-\sum_{i=0}^{28}
2i!(-1)^{b-1-i}c_{29}\binom{-n}{29}
\Psi_{30,-1,i}\\
&+\sum_{h=0}^{28}v_h^{Z}\Psi_{0,h,0},
\end{aligned}
\tag{10.2}
$$


where


$$
\boxed{
v_h^{Z}=
2\sum_{s=h+1}^{29}
c_s\binom{b+h}{s}
(-1)^{b+h-s}\mathfrak d(b+h-s)
\pmod{p^2}.
}
\tag{10.3}
$$



The last line is the **finite return**, not an optional correction. It follows by expanding the exact Schur correction (6.3) to first coefficient order. In that order, exterior displacements below $29$ make the relevant $T_n$ and $R_n$ blocks diagonal modulo $p$, yielding (10.3).

Accordingly the requested actual assembled first coefficient is


$$
\boxed{
c_{\ell,010}+22c_{\ell,110}
=A_q\,\mathfrak X_\ell(\mathscr Z_{\rm exc})
\pmod p.
}
\tag{10.4}
$$



Every input in (10.2)–(10.4), other than the already identified actual $A_q$, is a fixed bounded polynomial or a retained low residue. There is no hidden actual-head row in this formula.

---

## 11. The exterior source and finite return of the second column

Exact factorial filtration gives $v_h=0\pmod{p^2}$ for $h\ge2$. The retained two-coordinate equations, expanded symbolically, give


$$
v_0=1+6p,\qquad v_1=-1+16p\pmod{p^2}.
\tag{11.1}
$$


For transparency, the relevant block is


$$
C_{00}=C_{11}=1+7c_{29},\qquad
C_{01}=-2n,\qquad C_{10}=-n\pmod{p^2},
$$


with right side $(1,-1)$. Thus (11.1) includes the finite return already at this order; it is not the uncorrected choice $(1,-1)$.

Let $\varepsilon_0=1,\varepsilon_1=-1$. The assembled dictionary is


$$
\begin{aligned}
\mathscr Y_{\rm exc}={}&
(1+6p)\Psi_{0,0,0}+(-1+16p)\Psi_{0,1,0}\\
&+\sum_{h=0}^{1}\sum_{s=1}^{29}
\varepsilon_hc_s\Psi_{0,h+s,s}\\
&+\sum_{h=0}^{1}
\varepsilon_hc_{29}\binom{-n}{29}\Psi_{29,h,0}.
\end{aligned}
\tag{11.2}
$$


Hence


$$
\boxed{
e_{\ell,010}+22e_{\ell,110}
=\mathfrak X_\ell(\mathscr Y_{\rm exc})\pmod p.
}
\tag{11.3}
$$



The complete logarithmic force is paid at this fixed precision by its whole-row guard. Its deletion here is not extended to arbitrary primitive depth. The physical terminal remains separate and has zero contribution to this coefficient.

Equations (10.4) and (11.3) are the requested assembled coefficients. They are explicit formulas, not a claim of an executed coefficient-table certificate.

Nevertheless their contraction requires no table:


$$
\boxed{
\mathcal E_{\rm exc}
\sum_\ell
(c_{\ell,010}+22c_{\ell,110})
(e_{\ell,010}+22e_{\ell,110})=0.
}
\tag{11.4}
$$



---

# Part IV. The complete lifted observation for $\kappa$

## 12. Why the genuinely second-order remainder is radical

At precision $p^7$, the guarded atom bounds of §6 and the sharper actual exterior bounds preserve the same eight upper kernels.

Two elementary facts control the extra lift.

1. For row degree $r<841$,
   

$$
\binom{\ell+p^3J}{r}
   =\binom\ell r+p^2J\,R_r(\ell)\pmod{p^3}.
$$


   This follows directly from Vandermonde; only $k$ divisible by $p$ can survive after division by $p^2$.

2. A balanced three-digit unit-factorial ratio modulo $p^3$ has the form
   

$$
L_0+pJ L_1+p^2J^2L_2\pmod{p^3},
$$


   with the constant and linear coefficients retained at their appropriate precisions. This follows from the partial-block product expansion; complete blocks use
   $\sum a^{-1}=0\pmod{p^2}$ and $\sum a^{-2}=0\pmod p$.

Therefore, after removing the displayed order-zero and order-one terms, each second-order remainder modulo $p$ is a linear combination of


$$
R(J_0)K_s(J).
$$


On the support of $K$, the ratios $K_s/K$ are functions of $J_0$, with unit denominator. Hence the existing weighted radical proves


$$
\sum_JK(J)\,R(J_0)K_s(J)=0\pmod p.
\tag{12.1}
$$



Thus the $F_0^TG_2+F_2^TG_0$ contribution in formula 7.2 is eliminated **after its complete source and return representation has been retained**. It is not discarded by extrapolating a shallower precision.

Together with (11.4), this leaves only the paid lifts of the leading and first-order contractions.

---

## 13. The boundary-correct complete formula

Define the following actual upper observations:


$$
S=\frac{\sum_{J=0}^{B}K(J)^2}{p^2}\pmod p,
$$




$$
T=\frac{\sum_{J=0}^{B}J K(J)^2}{p}\pmod p,
\qquad
U_s=\frac{\sum_{J=0}^{B}K(J)K_s(J)}p\pmod p,
$$


and


$$
k_B=K(B)/p\pmod p.
\tag{13.1}
$$


All divisions are paid by the retained radical and ordinary-tail zero.

Using the complete order-one coefficients of Turn 14, one obtains


$$
\begin{aligned}
\kappa={}&
S\sum_{\ell=0}^{D-1}a_\ell g_\ell
-k_B^2\sum_{\ell=5044}^{D-1}a_\ell g_\ell\\
&+T\sum_{\ell=0}^{D-1}(a_\ell d_\ell+g_\ell b_\ell)\\
&+\sum_sU_s
\sum_{\ell=0}^{D-1}(a_\ell e_{\ell,s}+g_\ell c_{\ell,s})
\pmod p.
\end{aligned}
\tag{13.2}
$$



This is the complete lifted observation connected to formula 7.2.

The subtraction in the first line is essential. Completing the branch $J\le B-1$ to $J\le B$ is no longer free at this precision:


$$
\frac{K(B)^2}{p^2}=k_B^2
$$


can survive. In contrast, the endpoint corrections in $T$ and $U_s$ are zero after their displayed divisions.

The actual physical terminal satisfies $F_b,G_b\in p^2$, so its product is zero in $\kappa$. Its influence on the finite contact solves remains present.

By Theorem 8.1, all first-column coefficient dependence in this observation may be replaced by the flat head and the single multiplier $A_q$. Thus (13.2) is a genuine observable quotient, not merely a rational-function state representation.

### What remains unevaluated

The mixed linear combination (13.2), with its actual higher-digit upper observations, has not been evaluated. In particular:

- $\mathcal H(t)=0$ does not evaluate $S$;
- the radical only pays the divisions defining $T,U_s$;
- a nonzero intermediate moment would not by itself establish nonzero $\kappa$;
- the endpoint subtraction cannot be omitted.

The unresolved fixed-layer problem is now this **specific mixed observation**, rather than an unrestricted 371-coordinate head problem.

---

# Part V. Original-domain and primitive implications

## 14. No uniform nonzero cylinder is sought

The accepted content consequence remains


$$
c\ge5\Longrightarrow\kappa=0.
$$


Because content is unbounded in every original arithmetic progression, a full nonempty original cylinder with uniformly nonzero $\kappa$ is excluded.

Nothing in the head quotient changes that fact. The upper mixed observation in (13.2) still depends on the actual continuation.

If an actual original index gives $\kappa\ne0$, then


$$
v_p(Z_w^TY)=10.
$$


Under the index-specific condition


$$
d+1+v_p(\rho_n)>10
$$


—in particular under $v_p(\rho_n)\ge0$—one obtains


$$
v_p(Z_w^TY-p\rho_nZ_w^TZ_w)=10<d+2.
$$


That is an obstruction at the evaluated index, not a family-wide disproof.

---

## 15. The infinite-subsequence primitive target is unchanged

At the actual depth


$$
K=d-c=c+4+\nu,
$$


retain the complete approximation


$$
Y^{[K]}=
\mathcal R\theta^{(e,[K])}
+W_be_b+\mathcal RA^{-1}r^{(F,[K])}.
$$


The logarithmic head remains whenever its guard does not pay its omission.

The exact factorial theorem still gives


$$
Z_w^T(Y-Y^{[K]})\in p^{d+2}\mathbb Z_p.
$$


The unresolved primitive observation is


$$
\boxed{
x^TY^{[K]}-p^{c+3}\rho_nx^Tx\pmod{p^K}.
}
\tag{15.1}
$$



The existence of an infinite original subsequence with $c\to\infty$ is reused. Neither the exceptional cancellation nor the fixed-layer head quotient proves (15.1) on that subsequence.

---

# Part VI. Arithmetic task, global denominator, and proof status

## 16. What bounded arithmetic is now justified

No accepted prefix, $\Xi$, old norm, or old exterior computation needs to be repeated.

No large head-transition construction is proposed.

The newly justified bounded arithmetic, if undertaken, is **mixed-observation assembly**, with inputs:

1. the already retained original low residues;
2. the fixed head (8.3)–(8.4);
3. the explicit source and return dictionaries above;
4. the required higher coefficient digits of the guarded finite normal form;
5. the actual $147$-coordinate second-column exterior solve at precision $p^7$;
6. the original split at $\ell=5044$.

Its expected verifiable output is the low coefficient row multiplying


$$
(S,\ k_B^2,\ T,\ (U_s)_s)
$$


in the **whole** expression (13.2), with the flat-head factorization checked and both finite returns included.

That output would establish only the assembled low observation. A further proof or certificate must evaluate its action on the actual compatible upper suffixes. There is no established practical traversal bound for the original enormous digit word.

The proofs of the exceptional zero and the head quotient require no execution of this proposed arithmetic.

---

## 17. Global objects remain unchanged

Retain the original row contents, the falling row metric


$$
\omega_j=\frac{(n+2)!}{(n+2-j)!},
\qquad
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2),
$$


and the least simultaneous clearer $d_B$.

The final objects are still


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


The gcd is over **all primes**, and the actual primitive multiplier is $d_B^2/g_B$.

For the same original index,


$$
\epsilon_n=p_n/q_n-(e+\pi),
\qquad
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$


The retained signed-error theorem supplies eventual nonzero error and its stated exponential decay. Nothing here supplies the required all-prime upper bound for the actual $q_n$.

---

## 18. Proof-status ledger

| Statement | Status |
|---|---|
| Exact factorial filtration; exterior sizes $118/147$ | Reused |
| Actual four-head relation $(2,14,8,24)A_q$ | Reused |
| Rank-one exceptional Gram relation | Reused |
| Explicit $J_0=14$ shifted digit kernel (3.2) | **Proved** |
| Both original cutoff branches and exact $J=B$ zero | **Proved** |
| $\mathcal E_{\rm exc}=0\pmod p$ | **Proved** |
| Lifted exceptional square is zero modulo $p^2$ on the reviewed cylinder | **Proved using the retained lifted reflection** |
| Entire first-correction product $\sum BE=0\pmod p$ | **Proved** |
| Actual fixed-layer head quotient through $A_q$ and a fixed 58-entry head | **Proved for all compatible continuations** |
| Explicit assembled exceptional coefficients, including both returns | **Derived; coefficient tables not executed** |
| Complete lifted observation (13.2), including the cutoff correction | **Derived** |
| Actual numerical value or universal vanishing of $\kappa$ | **Not established** |
| Uniform nonzero $\kappa$ on a full cylinder | Excluded; not sought |
| Primitive relative alignment on an infinite original subsequence | Open |
| All-prime denominator versus whole same-index error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The named new term is resolved:


$$
\boxed{\mathcal E_{\rm exc}=0,\qquad \sum_{\ell,J}B_\ell(J)E_\ell(J)=0\pmod{29}.}
$$


The exceptional denominator opens a shifted channel, but that channel returns to the existing branch-reflection radical; it supplies no nonzero cylinder witness.

The actual first-head problem also contracts substantially:


$$
\boxed{\kappa=A_q\,\kappa_{\rm flat}\pmod{29},}
$$


with a fixed, explicitly assembled 58-entry head and a closed one-dimensional head suffix transition. This is an observable reduction, not a claim that a large rational-function module can be traversed feasibly.

The exact remaining fixed-layer bottleneck is the boundary-correct **whole mixed observation** (13.2). Its low coefficient row can now be assembled without a large head automaton, but its action on the actual upper continuation has not been evaluated.

At primitive depth the outstanding target remains (15.1), with complete exterior forcing, logarithmic retention when necessary, and the physical terminal. At global scale, the all-prime final gcd and actual primitive denominator still have not been compared with the whole nonzero same-index error. Accordingly, no irrationality proof or disproof is claimed.
