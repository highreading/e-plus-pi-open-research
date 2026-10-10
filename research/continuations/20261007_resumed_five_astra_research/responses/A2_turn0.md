> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 continuation — An exact upper-word action, a unit head multiplier, and the remaining primitive-depth obstruction

## Executive summary

The exceptional-channel cancellation in A2 Turn 16 survives review, with one correction to its lifted proof: the two unweighted branch terms cancel **together** modulo $29^2$; their separate vanishing was not established. This correction does not change the exceptional zero or the first-correction-product zero.

The new results concern the actual upper observations.

1. **The head multiplier never vanishes.** For
   

$$
A_m=\operatorname{CT}(z^{-1}+2+2z)^m,
$$


   every digit value $A_0,\ldots,A_{28}$ is nonzero modulo $29$. Consequently $A_m$ is a $29$-adic unit for every nonnegative integer $m$. On the original family there is the additional exact relation
   

$$
\boxed{q=29W+24,\qquad A_q\equiv25A_W\pmod{29}.}
$$


   Thus the actual head does not require a separate, unrelated suffix word.

2. **The eight paid cross-interface observations reduce to three.** Besides $T$, only
   

$$
V=\frac{\sum J^2K(J)^2}{29},\qquad
   E=\frac{\sum K(J)K_{010}(J)}{29}
   \pmod{29}
$$


   are needed. The complete fixed-layer observation therefore has the form
   

$$
\boxed{
   \kappa=A_q\bigl(\alpha S-\delta k_B^2+\lambda T+\mu V+\chi E\bigr)
   \pmod{29},
   }
$$


   with five actual low coefficient sums. The boundary subtraction remains present.

3. **These particular observations have an explicit, closed digit action.** A five-item rational dictionary, using two fixed denominators, represents their unnormalized numerators. A proved prime-power Cartier action evaluates the complete linear combination modulo $29^9$, follows the actual joint word of $W$ and $B$, and incorporates $A_q$ into the same action. This is more than an unevaluated finite sum or an appeal to automaticity.

These are fixed-layer results. They do **not** evaluate the retained primitive contraction at


$$
K=d-c=c+4+\nu,
$$


nor prove that a zero or nonzero accepting state occurs at infinitely many original indices. The all-prime denominator comparison also remains open. No proof of rationality or irrationality of $e+\pi$ results.

---

## 1. Preserved setting and scope

Throughout,


$$
p=29,\qquad D=p^3,
$$


and the indices remain


$$
b=3^{249005515+574312172u}
  =410910916+p^6C,\qquad n=2001b,
\qquad u\ge0,\quad u\equiv2\pmod{p^9}.
$$



The original domains are unchanged:

- contact coordinates $0\le j<b$;
- recurrence source rows $1\le i\le b-2$;
- reconstructed coordinates $0\le j\le b$.

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



The recovered complete force is retained:


$$
\mathbf r=A_{IE}z+\frac{h^F}{b!},
\qquad z_h=\frac{(b+h)!}{b!}.
$$


Here $h^F$ comes from the logarithmic generating function $F/(1-z)$, not from $F$ alone. The exponential factorial subtraction, both original exponential boundary contributions, the finite returns, and the exterior $+1$ represented by the separate physical terminal remain in force.

Write


$$
Z_w=p^{c+2}x,\qquad
\nu=v_p(x^Tx),\qquad d=2c+4+\nu,
$$


and


$$
F=Z_w/p^4,\qquad G=Y/p^4.
$$


At the reviewed fixed layer,


$$
F,G\in\mathbb Z_p^{b+1},\qquad F^TG\in p^2\mathbb Z_p,
$$


and


$$
\kappa=\frac{F^TG}{p^2}\pmod p.
$$



I reuse the closed complete-force identification, factorial filtration, guarded normal forms, reflection radical, and completed path calculations only at their stated scopes. No closed path enumeration is repeated here.

---

# Part I. Audit of the exceptional zero

## 2. The shifted kernel and its first nonzero residue are consistent

The upper parameters satisfy


$$
W=7663+DX,\qquad B=16848+DC,\qquad A=15327+2DX,
$$


with $X=2001C+1382$. In particular,


$$
\boxed{A=2W+1.}
$$



The exceptional kernel is


$$
K_{010}(J)
=\frac1{p^3}
 \binom WJ
 \binom{A+B-J-1}{B-J-1}.
$$



The shift of $B$ to $B-1$ must precede reduction. The division by $A+B-J$ is not a unit operation on $J\equiv14\pmod p$.

For


$$
J=14+p^2r+Dq,\qquad 0\le r\le20,
$$


the first three digits give two events. The high factorial ratios are respectively


$$
F_{\rm I}(q)=(2X+C-q+1)
 \binom Xq\binom{2X+C-q}{C-q},
$$


and


$$
F_{\rm II}(q)=(X-q)
 \binom Xq\binom{2X+C-q}{C-q}.
$$


Thus the source’s support and paid division agree with the digit calculation.

The low unit is also correct. Its scalar, after extracting $\binom{20}{r}$, is


$$
\frac{3\,7!\,28!\,9!}
 {14!\,22!\,15!\,13!\,18!\,20!}
\equiv22\pmod{29}.
$$


For example, Wilson complement identities reduce this to


$$
\frac{3\cdot7!\cdot9!\cdot6!\cdot10!\cdot8!}{14!},
$$


whose residue is $22$.

Consequently,


$$
K_{010}(14+p^2r+Dq)
\equiv22\binom{20}{r}
\begin{cases}
F_{\rm I}(q)/p,&r\le9,\\
F_{\rm II}(q)/p,&r\ge10
\end{cases}
\pmod p.
$$



The exact range is $0\le q\le C$. At the upper endpoint,


$$
K_{010}(B)=0
$$


by the negative lower index in its second binomial. This is an algebraic boundary zero, not a substitution for the physical terminal.

## 3. The exceptional Gram zero is valid; the lifted proof needs grouping

The two low half-sums are


$$
\sum_{r=0}^{9}\binom{20}{r}^2=10,\qquad
\sum_{r=10}^{20}\binom{20}{r}^2=19
\pmod{29}.
$$


Indeed, their total is $\binom{40}{20}=0\pmod{29}$, while the central square is $9$.

With


$$
H_{\rm I}=\sum_{q=0}^C(F_{\rm I}(q)/p)^2,\qquad
H_{\rm II}=\sum_{q=0}^C(F_{\rm II}(q)/p)^2,
$$


the exceptional sum is therefore


$$
\mathcal E_{\rm exc}
=26(H_{\rm I}-H_{\rm II})=0\pmod p
$$


by the retained reflection.

### Correction to Turn 16, §5

The lifted expression there has the form


$$
\alpha_{\rm I}H_{\rm I}+\alpha_{\rm II}H_{\rm II}
+p\beta_{\rm I}H_{\rm I}^{[1]}
+p\beta_{\rm II}H_{\rm II}^{[1]}
\pmod{p^2},
$$


where


$$
\alpha_{\rm I}+\alpha_{\rm II}\in p\mathbb Z_p.
$$



On the reviewed cylinder, the retained lifted reflection gives


$$
H_{\rm I},H_{\rm II}\in p\mathbb Z_p,\qquad
H_{\rm I}-H_{\rm II}\in p^2\mathbb Z_p,
$$


and


$$
H_{\rm I}^{[1]},H_{\rm II}^{[1]}\in p\mathbb Z_p.
$$



These statements do **not** separately show that
$\alpha_{\rm I}H_{\rm I}$ and
$\alpha_{\rm II}H_{\rm II}$ vanish modulo $p^2$. The correct argument is


$$
\begin{aligned}
\alpha_{\rm I}H_{\rm I}+\alpha_{\rm II}H_{\rm II}
&=\alpha_{\rm I}(H_{\rm I}-H_{\rm II})
 +(\alpha_{\rm I}+\alpha_{\rm II})H_{\rm II}\\
&\in p^2\mathbb Z_p.
\end{aligned}
$$


The two weighted terms are individually in $p^2$.

Thus the lifted exceptional square zero survives. The source’s phrase that “every term” vanishes was stronger than the supplied hypotheses justify, but the grouped cancellation repairs the proof without any new numerical scalar.

Together with the reviewed off-exceptional radical, this proves the whole first-correction-product zero:


$$
\boxed{\sum_{\ell,J}B_\ell(J)E_\ell(J)=0\pmod p.}
$$



This conclusion concerns that complete product. It does not separately annihilate the next lifted leading observation.

---

# Part II. The actual head multiplier is a unit

## 4. A complete digit calculation

Let


$$
A_m=\operatorname{CT}(z^{-1}+2+2z)^m.
$$


Its generating function is


$$
\sum_{m\ge0}A_mt^m=(1-4t-4t^2)^{-1/2}.
$$


Hence


$$
mA_m=(4m-2)A_{m-1}+4(m-1)A_{m-2},
\qquad A_0=1,\quad A_1=2.
$$



For $0\le d<29$, reduction of the generating function gives


$$
A_d=[t^d](1-4t-4t^2)^{14}\pmod{29}.
$$


The factor omitted by Frobenius has no positive degree below $29$.

Put $a=-4$. The polynomial


$$
P(t)=(1-4t-4t^2)^{14}
$$


satisfies


$$
P(t)=a^{14}t^{28}P(1/(at)).
$$


Therefore


$$
\boxed{A_{28-d}=(-4)^{14-d}A_d\pmod{29}.}
$$



The recurrence through $d=14$, followed by this reciprocity, gives the following complete table:


$$
\begin{array}{c|rrrrrrrrrrrrrrr}
d&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14\\ \hline
A_d&1&2&8&3&20&12&14&2&13&24&22&21&21&20&6
\end{array}
$$




$$
\begin{array}{c|rrrrrrrrrrrrrr}
d&15&16&17&18&19&20&21&22&23&24&25&26&27&28\\ \hline
A_d&7&17&19&6&16&4&2&2&18&25&14&15&14&1 .
\end{array}
$$



This is a bounded exact calculation with a short certificate: the first table satisfies the displayed recurrence, and the second satisfies the displayed reciprocity. In particular, no entry is zero.

For $m=d+29r$, Frobenius and the support $[-d,d]\subset[-28,28]$ give


$$
A_m\equiv A_dA_r\pmod{29}.
$$


Iteration proves:

### Theorem 4.1 — No head-digit zero
For every integer $m\ge0$,


$$
\boxed{A_m\not\equiv0\pmod{29}.}
$$



Thus a zero of the actual $\kappa$ cannot be explained by a zero digit factor in $A_q$.

This does not contradict unbounded column content. The complete upper response multiplying $A_q$ can still vanish.

## 5. The head and upper word are exactly linked

The displayed low residues give


$$
b=DB+5044.
$$


A direct calculation yields


$$
\boxed{W=2001B+413.}
$$


Indeed, both sides equal


$$
33713261+2001DC.
$$



Using the actual head index,


$$
q=\frac{69b-7}{29},
$$


we obtain


$$
q=69p^2B+12001=pW+24.
$$


Therefore the Lucas product gives


$$
\boxed{A_q=A_{24}A_W=25A_W\pmod{29}.}
$$



This matters operationally and mathematically: the head multiplier follows the **same actual $W$-word** used by the upper observations. No independent head suffix, free scalar, or auxiliary digit string is needed.

Combining this with Turn 16’s fixed-layer head quotient,


$$
\boxed{\kappa=0\quad\Longleftrightarrow\quad\kappa_{\rm flat}=0\pmod{29}}
$$


at every original index in its proved scope.

---

# Part III. Exact reduction of the paid upper observations

## 6. Unnormalized notation

To avoid premature division, define


$$
h_J=\binom WJ\binom{A+B-J}{B-J},
\qquad 0\le J\le B.
$$


Thus $K(J)=h_J/p^3$.

Set


$$
N=\sum_{J=0}^B h_J^2,\qquad
M_1=\sum_{J=0}^B Jh_J^2,\qquad
M_2=\sum_{J=0}^B J^2h_J^2,
$$


and


$$
R=\sum_{J=0}^B h_JH_{010}(J),
$$


where


$$
H_{010}(J)=\binom WJ\binom{A+B-J-1}{B-J-1}.
$$



The reviewed radicals pay


$$
N\in p^8\mathbb Z_p,\qquad
M_1,M_2,R\in p^7\mathbb Z_p.
$$


For $M_2$, use the weighted radical with weight $J_0^2$.

The particular normalized observations are


$$
S=N/p^8,\qquad T=M_1/p^7,\qquad
V=M_2/p^7,\qquad E=R/p^7
\pmod p.
$$



At the endpoint,


$$
h_B=\binom WB,\qquad
k_B^2=\frac{\binom WB^2}{p^8}\pmod p.
$$



## 7. All eight $U_s$ reduce to $T,V,E$

The following identities are exact integer identities, including at the exceptional residue:


$$
H_{100}(J)=(W-J)h_J,
$$




$$
H_{001}(J)=(A+B-J+1)h_J,
$$




$$
H_{011}(J)=(B-J)h_J,
$$


and


$$
(A+B-J)H_{010}(J)=(B-J)h_J.
$$


The last identity uses multiplication, not division by the exceptional denominator.

Since


$$
W\equiv7,\qquad A\equiv15,\qquad B\equiv28\pmod{29},
$$


division only after summation gives


$$
\boxed{
\begin{array}{c|c}
s&U_s\\ \hline
000&0\\
100&-T\\
001&-T\\
011&-T\\
101&V-22T\\
111&V-6T\\
010&E\\
110&22E-T
\end{array}
\pmod{29}.}
$$



For example,


$$
\frac{\sum h_JH_{101}(J)}{p^7}
=
W(A+B+1)\frac N{p^7}
-(W+A+B+1)T+V,
$$


and $N/p^7\equiv0\pmod p$.

For the exceptional companion,


$$
\begin{aligned}
\sum h_JH_{110}(J)
&=W R-\sum Jh_JH_{010}(J)\\
&=(W-A-B)R+BN-M_1,
\end{aligned}
$$


which gives $U_{110}=22E-T$.

No exceptional residue is omitted in these reductions.

### Boundary check

Replacing $J\le B-1$ by $J\le B$ changes $M_1/p^7$ and $M_2/p^7$ by multiples of $p$, because $h_B^2\in p^8$. The exceptional endpoint is exactly zero.

The same completion changes $N/p^8$ by $k_B^2$, which can survive. Hence the boundary subtraction cannot be absorbed into the radical.

## 8. Five low coefficients, not eleven upper observations

Use the flat first head in Turn 16, and let


$$
\alpha=\sum_{\ell=0}^{D-1}a_\ell g_\ell,\qquad
\delta=\sum_{\ell=5044}^{D-1}a_\ell g_\ell,
$$




$$
\tau=\sum_{\ell=0}^{D-1}(a_\ell d_\ell+g_\ell b_\ell),
$$




$$
L_s=\sum_{\ell=0}^{D-1}
(a_\ell e_{\ell,s}+g_\ell c_{\ell,s})
\pmod p.
$$


These remain the actual complete coefficient sums, including the finite returns.

Define


$$
\lambda=
\tau-L_{100}-L_{001}-L_{011}
-22L_{101}-6L_{111}-L_{110},
$$




$$
\mu=L_{101}+L_{111},\qquad
\chi=L_{010}+22L_{110}.
$$



Substitution into the boundary-correct formula gives:

### Theorem 8.1 — Reduced complete fixed-layer observation
At every original index in the reviewed cylinder,


$$
\boxed{
\kappa
=A_q\bigl(\alpha S-\delta k_B^2+\lambda T+\mu V+\chi E\bigr)
\pmod p.
}
$$



This reduction is independent of any numerical evaluation of the five low coefficients. It reduces the actual upper task and preserves the exceptional channel’s paid lift rather than setting that lift to zero.

---

# Part IV. A closed action on these particular observations

## 9. A five-item rational dictionary

Introduce formal variables $t,x,y,z$, with $z$ Laurent, and put


$$
L=(1-x)^2(1-y)^2,
$$




$$
P=(1+z)(1+xy/z),
$$




$$
\mathcal Q=L-tP,\qquad \mathcal Q_{\rm end}=1-tP.
$$



For a rational series $\Phi$, write


$$
\mathscr C_{W,B}(\Phi)
=[t^Wx^By^Bz^0]\Phi.
$$



Then the required numerators have the exact representations


$$
\boxed{
\begin{array}{c|c}
\text{Numerator}&\text{Rational dictionary entry}\\ \hline
N&1/\mathcal Q\\[1mm]
M_1&t(z+xy)/\mathcal Q^2\\[1mm]
M_2&t(z+xy)/\mathcal Q^2+
       2t^2(z+xy)^2/\mathcal Q^3\\[1mm]
R&y/\mathcal Q\\[1mm]
\binom WB^2&1/\mathcal Q_{\rm end}
\end{array}}
$$


under $\mathscr C_{W,B}$.

### Proof

The basic identity is


$$
\operatorname{CT}_z P^W
=\sum_{J=0}^W\binom WJ^2(xy)^J.
$$


Also,


$$
\frac1{\mathcal Q}
=\sum_{W\ge0}t^W
 \frac{P^W}{(1-x)^{2W+2}(1-y)^{2W+2}}.
$$


Because $A=2W+1$, taking $x^By^B$ gives $N$.

Multiplication by $y$ shifts the second lower index from $B-J$ to $B-J-1$, producing $R$.

For the first moment, mark the exponent selected from $(1+z)^W$. The identity


$$
J\binom WJ=W\binom{W-1}{J-1}
$$


gives, after summing over $W$,


$$
\frac{t\,z(1+xy/z)}{\mathcal Q^2}
=\frac{t(z+xy)}{\mathcal Q^2}.
$$


Using $J^2=J(J-1)+J$ gives the displayed second-moment entry.

Finally,


$$
\frac1{\mathcal Q_{\rm end}}=\sum_{W\ge0}t^WP^W,
$$


whose diagonal coefficient is $\binom WB^2$. ∎

The complete observation is therefore represented by the single paired rational state


$$
\begin{aligned}
\Phi_{\rm obs}={}&
\frac{\alpha}{\mathcal Q}
-\frac{\delta}{\mathcal Q_{\rm end}}\\
&+p\left[
\lambda\frac{t(z+xy)}{\mathcal Q^2}
+\mu\left(
\frac{t(z+xy)}{\mathcal Q^2}
+\frac{2t^2(z+xy)^2}{\mathcal Q^3}
\right)
+\chi\frac y{\mathcal Q}
\right].
\end{aligned}
$$


Its accepting coefficient is divisible by $p^8$, and


$$
\boxed{
\kappa
=A_q\,p^{-8}\mathscr C_{W,B}(\Phi_{\rm obs})
\pmod p.
}
$$



The division is applied to the completed accepting coefficient. No nonintegral rational summand is inverted modulo $p$.

## 10. Explicit prime-power closure

This construction uses the established Cartier/Frobenius method underlying the cited Rowland–Yassawi work. The direct support proof below supplies the hypotheses needed for this Laurent-series representation; the literature’s automaticity theorem is not being used as an evaluation of our response.

For either denominator $\mathcal D\in\{\mathcal Q,\mathcal Q_{\rm end}\}$, define


$$
\mathcal V_{\mathcal D}
=\frac{\mathcal D(t,x,y,z)^p-
\mathcal D(t^p,x^p,y^p,z^p)}p.
$$


It is an integral Laurent polynomial.

For digits $e,d$, let


$$
\Lambda_{e,d,d,0}
\left(\sum a_{i,j,k,l}t^ix^jy^kz^l\right)
=
\sum a_{pi+e,pj+d,pk+d,pl}t^ix^jy^kz^l.
$$



At modulus $p^9$, use states


$$
\sum_{h=1}^{9}p^{h-1}\frac{P_h}{\mathcal D^h},
$$


where


$$
\deg_tP_h\le h,\qquad
\deg_xP_h,\deg_yP_h\le2h,\qquad
\operatorname{supp}_zP_h\subset[-h,h].
$$



For $1\le h\le9<p$,


$$
\begin{aligned}
\Lambda_{e,d,d,0}
\left(p^{h-1}\frac{P_h}{\mathcal D^h}\right)
\equiv
\sum_{k=0}^{9-h}
(-1)^kp^{h-1+k}
\frac{
\Lambda_{e,d,d,0}
(P_h\mathcal D^{p-h}\mathcal V_{\mathcal D}^{\,k})
}{\mathcal D^{k+1}}
\pmod{p^9}.
\end{aligned}
\tag{10.1}
$$



The numerator before Cartier has bounds


$$
\deg_t\le p(k+1),\quad
\deg_x,\deg_y\le2p(k+1),\quad
|\,\deg_z\,|\le p(k+1).
$$


After Cartier it is in the prescribed box for denominator $\mathcal D^{k+1}$. Its coefficient has at least the required factor $p^k$. This proves closure.

The initial entries have denominator powers at most three. One initial application of the same expansion places them in the displayed weighted module, even where the initial coefficient does not have the module’s denominator-dependent weight.

A safe coordinate bound for each denominator is


$$
\sum_{h=1}^9(h+1)(2h+1)^3=168618.
$$


Thus two such blocks give a finite action with at most $337236$ polynomial coordinates. This is a theoretical support bound, not a proposal to store dense transition matrices or to claim practical full-word traversal.

The terminal functional is explicit:


$$
\sum_{h=1}^9p^{h-1}
[t^0x^0y^0z^0]P_h,
$$


because both denominators equal $1$ at $t=x=y=0$.

This supplies a proved transition, initialization, and acceptance rule for the particular complete observation.

## 11. Exact admissible-word dependence and the head multiplier

The action must not read independent $W$- and $B$-words.

Since


$$
W=2001B+413,
$$


the $W$-digits are generated from the actual $B$-digits by a bounded carry. Start with


$$
r_0=413.
$$


On reading a base-$29$ digit $d$ of $B$, set


$$
e=(2001d+r)\bmod29,\qquad
r'=\left\lfloor\frac{2001d+r}{29}\right\rfloor.
$$


Then $e$ is the corresponding digit of $W$. The carry remains in


$$
0\le r\le2000.
$$



After the last actual digit of $B$, append zero $B$-digits until the carry vanishes. This processes precisely the remaining digits of $W$.

To incorporate the head:

- initialize the scalar factor at $25$;
- on the same transition, multiply by $A_e$;
- apply $\Lambda_{e,d,d,0}$ to the rational state.

At acceptance the scalar is


$$
25\prod A_e=25A_W=A_q\pmod p.
$$



Any integer lifts of the $A_e$ may be used modulo $p^9$: their product is correct modulo $p$, and the completed accepting coefficient is in $p^8$, so the choice of lifts disappears after the paid division modulo $p$.

This is a genuine action on the actual head and upper observations. Nevertheless, an arbitrary accepted digit word need not arise from


$$
b=3^{249005515+574312172u}.
$$


The original exponential index condition remains an additional restriction. Closure under digits does not prove that an accepting state is reached infinitely often on that original family.

---

# Part V. What this does—and does not—give at primitive depth

## 12. Fixed-layer zero classification is not primitive alignment

The new action can evaluate the fixed-layer observation after a complete actual word is supplied, or propagate a precise observation state through an actual prefix. It does not by itself prove a nonzero value, universal zero, or infinite-subsequence statement.

In particular, the accepted content theorem still gives


$$
c\ge5\Longrightarrow\kappa=0.
$$


Since $c$ is unbounded in every original arithmetic progression, no nonempty full original cylinder can have uniformly nonzero $\kappa$.

The unit theorem sharpens the interpretation of these forced zeros:


$$
c\ge5\Longrightarrow
\alpha S-\delta k_B^2+\lambda T+\mu V+\chi E=0\pmod p.
$$


They must occur in the complete upper response, not in a vanishing head multiplier.

The present rational action has been derived for the guarded fixed-layer formula. It must **not** be promoted to an all-depth formula merely by increasing its modulus. At growing depth, additional atom shifts, coefficient lifts, and possibly the logarithmic head enter. The three-digit guard used to derive the fixed eight-interface representation is not uniform in arbitrary $K$.

## 13. The actual depth and $\rho_n$-precision

The primitive target remains


$$
K=d-c=c+4+\nu,
$$


with the complete approximation


$$
Y^{[K]}
=\mathcal R\theta^{(e,[K])}
+W_be_b+\mathcal RA^{-1}r^{(F,[K])}.
$$


The exact factorial theorem gives


$$
Z_w^T(Y-Y^{[K]})\in p^{d+2}\mathbb Z_p.
$$



Writing $x^Tx=p^\nu\eta$, the unresolved observation is


$$
\boxed{
x^TY^{[K]}-p^{K-1}\rho_n\eta\pmod{p^K}.
}
\tag{13.1}
$$



This uses the actual $K$, not a lower bound on $d$.

The valuation of $\rho_n$ must be paid:

- If $v_p(\rho_n)\ge1$, the second term is zero modulo $p^K$.
- If $v_p(\rho_n)=0$, the last required digit is $\rho_n\eta\bmod p$.
- If $v_p(\rho_n)=-h<0$, integrality of that term requires $h\le K-1$. Writing $\rho_n=p^{-h}\widetilde\rho_n$, one needs
  

$$
\widetilde\rho_n\eta\pmod{p^{h+1}},
$$


  not merely its reduction modulo $p$.

For approximate physical columns, the retained sufficient first-column budget is


$$
a\ge
\max\{c+2,\ d+2-v_p(Y),\ d-c-1-v_p(\rho_n)\},
$$


and the second-column budget is at least $K=d-c$.

If an actual $\kappa\ne0$ is eventually found, then


$$
v_p(Z_w^TY)=10.
$$


Under the index-specific condition


$$
d+1+v_p(\rho_n)>10,
$$


this obstructs the true alignment at that index. It does not exclude the entire family or prove anything about $e+\pi$ without the further denominator/error argument.

---

# Part VI. A bounded new certificate and the exact follow-on lemma

## 14. The next arithmetic certificate should return five coefficients

The new upper action is symbolic and requires no execution to establish its closure. Its outstanding low input is the five-entry row


$$
\boxed{(\alpha,\delta,\lambda,\mu,\chi)\in\mathbb F_{29}^5.}
$$



A bounded calculation can genuinely settle this row without repeating the closed $231$-path enumeration or the prohibited completed large calculations.

### Inputs

1. The actual low residues of $b,n$, with $b$ odd.
2. The fixed $58$-entry head of Turn 16, with explicitly chosen representatives modulo $p^2$.
3. The complete source and finite-return normal forms, not source-only approximations.
4. The actual second-column exterior response at the needed precision.
5. The original split at $\ell=5044$.
6. The already-proved exceptional and second-remainder cancellations.

For the first-order profiles used in these five sums, physical column precision $p^6$ suffices: it determines $F,G\pmod{p^2}$. The exact factorial filtration therefore permits the $118$-coordinate second-column exterior system at this assembly stage. A previously retained higher-precision solve may of course be reused rather than repeated.

For the bounded binomial and symbol coefficients involved, supplying $b,n\bmod p^7$ is a sufficient safe input precision: their small lower indices are below $p^2$, so the standard integer-valued-binomial continuity loss is at most one digit. High binomial atoms remain symbolic upper kernels; they are not replaced by low residues.

### Expected verifiable output

The certificate should provide:

- the five residues $(\alpha,\delta,\lambda,\mu,\chi)$;
- identities verifying the complete first-order profiles, including both finite returns;
- separate checks of the $\ell<5044$ and $\ell\ge5044$ sums;
- the resulting initial rational state $\Phi_{\rm obs}$.

This establishes only the low observation row. It is not an original-index evaluation and is not an infinite-family certificate.

## 15. Concrete follow-on lemma

The precise next suffix obligation can now be stated without an unspecified automaton:

> **Actual-word observation lemma.**  
> For the five certified low coefficients, characterize the accepting value of the two-block transition (10.1), with carry rule $W=2001B+413$ and multiplier $25A_W$, on the words
> 

$$
> B=\frac{3^{249005515+574312172u}-5044}{29^3},
> \qquad u\ge0,\quad u\equiv2\pmod{29^9}.
>
$$


> Prove either a zero criterion valid on those original words, or an admissible infinite subdomain on which the completed accepting value is nonzero.

A nonzero state before terminal acceptance does not prove this lemma. Nor does a regular-language classification on unrestricted $B$-words establish intersection with the original exponential family.

For primitive alignment, a further all-depth version must retain the additional $K$-dependent atoms and sources and evaluate (13.1). The fixed-layer action is a concrete starting point, not that all-depth theorem.

---

# Part VII. Global denominator, whole error, and proof status

## 16. The final arithmetic objects are unchanged

No result here changes the original row contents or the least simultaneous clearer $d_B$. Retain


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


The gcd remains over **all primes**, and the actual primitive multiplier is $d_B^2/g_B$.

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


An irrationality argument still requires an all-prime bound on the actual $q_n$ making


$$
0<|q_n\epsilon_n|\longrightarrow0
$$


on the **same infinite original indices**. None of the selected-prime results here supplies that bound.

## 17. Proof-status ledger

| Statement | Status |
|---|---|
| Exceptional kernel and its mod-$29$ Gram zero | Reviewed and retained |
| Lifted exceptional square zero | Retained with the grouping correction in §3 |
| Whole first-correction-product zero | Retained at the reviewed fixed layer |
| $A_m\ne0\pmod{29}$ for every $m\ge0$ | **Proved here** |
| Actual relation $q=29W+24$, $A_q=25A_W$ | **Proved here** |
| Reduction of eight $U_s$ to $T,V,E$ | **Proved here, including the exceptional residue** |
| Five-coefficient boundary-correct observation | **Derived here** |
| Rational dictionary and closed actual-word digit action | **Proved here** |
| Five low coefficient values | Not calculated |
| Completed value of $\kappa$ at an original index | Not evaluated |
| Infinite original-domain zero/nonzero classification | Open |
| Primitive contraction at $K=c+4+\nu$ | Open |
| All-prime primitive denominator versus whole same-index error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The principal new result is an explicit action on the **particular complete upper observation**, with its boundary subtraction and actual head dependence:


$$
\boxed{
\kappa
=25A_W\bigl(\alpha S-\delta k_B^2+\lambda T+\mu V+\chi E\bigr)
\pmod{29}.
}
$$


The multiplier $25A_W$ is always a unit. The five observations have a proved rational dictionary and a closed, paid digit transition following the actual affine relation between $W$ and $B$.

The immediate bounded calculation is now the five-entry low coefficient row, with complete source and return data. The exact mathematical bottleneck after that calculation is terminal acceptance on the original exponential words—not ordinary automaticity and not the existence of a finite state representation.

At the required growing depth, the unresolved expression is still


$$
x^TY^{[c+4+\nu]}-29^{c+3}\rho_nx^Tx
\pmod{29^{c+4+\nu}},
$$


with logarithmic forcing retained whenever its guard is insufficient and with $\rho_n$-precision explicitly paid. Even its resolution would not by itself supply the missing all-prime denominator comparison.

Accordingly, this continuation advances the upper-observation problem but does not prove or disprove irrationality of $e+\pi$.
