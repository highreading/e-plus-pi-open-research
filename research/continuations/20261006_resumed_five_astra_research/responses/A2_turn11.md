> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 11 — A complete normalization lemma at the $u=2$ phase, its physical norm consequence, and the actual-head hypothesis that must not be inferred from a norm reduction

## Executive assessment

There is a useful complete-column argument at the phase


$$
C\equiv20916\pmod{29^3}.
$$


It is stronger than the atomwise statement $29\mid V(q)$: the extra event occurs at a physical digit that is unchanged by **every shift in the retained finite normal form**.

I prove the following finite-normal-form result.

> **Complete saturation-and-radical lemma.**  
> At the original phase $u\equiv2\pmod{24389}$, suppose the unit-order sector of the actual head has the retained short-head normal form: its only coefficient-unit terms are the $r=0$ unshifted and shifted terms of the short head; every other head term has an explicit coefficient factor $29$. Then, with the actual finite inverse and terminal reconstruction retained,
> 

$$
> \boxed{Z_w\in29^4\mathbb Z_{29}^{\,b+1}.}
>
$$


> Moreover, the complete physical contraction—not merely the leading-atom contraction—satisfies
> 

$$
> \boxed{\frac{Z_w^TZ_w}{29^8}=0\pmod{29}.}
>
$$


> Thus this hypothesis gives $c\ge2$ and $d\ge9$.

The proof permits **arbitrary first-order head, lower, and endpoint-return coefficients**. They are not assumed zero. Their complete contribution factors through a common upper-block radical, which is evaluated below. No value of the pending normalized tail $\mathcal H(t)$, and none of the pending $42$ one-event numerical contributions, is required.

There is, however, a source-verification issue that I must keep explicit. The attached reports prove a short-head expansion and an actual **norm** reduction. They do not explicitly state the actual-head, unit-order identity needed to identify those two coefficient-unit terms as the complete unit-order sector of $f^0$. In particular,


$$
\eta=A_0^2\kappa\pmod{29}
$$


does **not** imply that identity.

Accordingly:

* the saturation-and-radical lemma below is proved;
* its application to the actual first column is conditional on the explicitly identified actual-head interface;
* I do **not** record $c\ge2$, or $d\ge9$, as unconditional actual-original conclusions from the displayed sources alone;
* if that interface is already among the accepted finite-control results, citing its exact statement suffices—no computation should be repeated.

This distinction is substantive. It prevents a contracted radical identity from being promoted to a column-content certificate.

---

## 1. Preserved problem and proof inputs

Throughout,


$$
p=29,\qquad \Lambda=p^6,\qquad \beta=410910916,
$$




$$
b=3^{249005515+574312172u}=\beta+\Lambda C,\qquad n=2001b,\qquad u\ge0.
$$



The domains remain


$$
0\le j<b,\qquad 1\le i\le b-2,\qquad 0\le j\le b
$$


for contact coordinates, source rows, and reconstructed coordinates.

The corrected columns remain


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,\qquad
W_j=\binom{n+2}{j}.
$$



I use the retained finite normal form with integral coefficients and the actual endpoint inverse. At precision $p^6$, its bounds are


$$
M=173,\qquad L=350.
$$


Its reconstructed binomial atoms have the form


$$
W_j\binom{-2n-a}{b+v-j},
\tag{1.1}
$$


with


$$
0\le a\le523,\qquad -350\le v\le346,
\tag{1.2}
$$


using the union of the head and exterior bounds. Integer-valued row factors arising from normal ordering are retained.

The endpoint solution is the actual finite integral solution


$$
q\equiv
\sum_{\ell=0}^{5}(-G)^\ell
K_\times\mathsf D\mathsf R_nw
\pmod{p^6},
\qquad
G=K_\times\mathsf DF\in pM(\mathbb Z_p).
\tag{1.3}
$$


In particular, every endpoint-return coefficient has an explicit factor $p$.

The accepted original residues give


$$
u\equiv2\pmod{24389}
\quad\Longrightarrow\quad
C=20916+p^3t,\qquad t\ge0.
\tag{1.4}
$$


No modular exponentiation is repeated.

### 1.1 The actual-head interface needed for an original-column conclusion

The following is the precise hypothesis used below.

**Actual-head interface $\mathbf H$.** After the accepted finite normal ordering, the coefficient-unit sector of the actual first head is $A_0$ times the coefficient-unit sector of


$$
h_i^{[0]}=
\begin{cases}
i!\bmod p,&0\le i<p,\\
0,&i\ge p.
\end{cases}
$$


Consequently, its only coefficient-unit reconstructed terms are the $r=0$ unshifted and shifted terms described in Turn 7, §4. Every other actual-head term has an explicit coefficient factor $p$.

A sufficient, stronger statement is that the **actual finite head in these coordinates** is


$$
h^{\rm act}\equiv A_0h^{[0]}\pmod p.
\tag{1.5}
$$


This is not an assertion about a head after a nonintegral change of basis.

Turn 7 supplies the normal ordering of $h^{[0]}$. It does not, in the displayed text, supply (1.5) for $f^0$. The actual-head radical used in its norm calculation is not a substitute for $\mathbf H$.

---

## 2. A uniform physical event survives every retained finite shift

Write an atom in positive-binomial form:


$$
W_j\binom{-2n-a}{b+v-j}
=
(-1)^{b+v-j}
W_j
\binom{2n+a-1+b+v-j}{b+v-j},
\tag{2.1}
$$


when $b+v-j\ge0$; otherwise the atom is zero.

Set


$$
D=p^3=24389.
$$


The exact low three-digit residues are


$$
b\bmod D=5044,
$$




$$
(n+2)\bmod D=20389,
$$




$$
2n\bmod D=16385.
\tag{2.2}
$$



For all shifts in (1.2),


$$
4694\le5044+v\le5390,
$$




$$
16384\le16384+a\le16907.
\tag{2.3}
$$


Thus neither bounded shift crosses a three-digit boundary.

Consequently the physical digits $3,4,5$ remain


$$
(W_i,B_i,A_i)=
(7,28,15),\quad(3,0,6),\quad(9,20,18),
\tag{2.4}
$$


where $W=n+2$, $B=b+v$, and $A=2n+a-1$.

The retained all-interface potential certificate therefore supplies at least two valuation events at these positions, for **every** incoming weight borrow, lower-index borrow, and addition carry.

At physical digit $7$, the phase (1.4) gives


$$
(W_7,B_7,A_7)=(8,25,17).
\tag{2.5}
$$


The shifts in (1.2) do not change this triple.

Let $x$ be the digit of $j$, $K$ the lower-index digit, and let $w,k,c\in\{0,1\}$ be incoming weight borrow, lower-index borrow, and addition carry. If this digit had no valuation event, then


$$
x\le8-w,\qquad K\le11-c.
$$


But the subtraction relation requires


$$
x+K+k=25+29k'
$$


for some $k'\in\{0,1\}$, while


$$
x+K+k\le20.
$$


This is impossible.

### Lemma 2.1 — Shift-uniform physical divisibility

At every original index satisfying (1.4), every retained atom (1.1), throughout the original reconstructed range $0\le j\le b$, satisfies


$$
\boxed{
W_j\binom{-2n-a}{b+v-j}\in p^3\mathbb Z_p.
}
\tag{2.6}
$$



This statement is about the actual physical digits and every retained shift. It is not an inference from $p\mid V(q)$.

### Consequence for all positive-order corrections

Every normal-form term with an explicit coefficient factor $p$ is in $p^4$, and every term with an explicit coefficient factor $p^2$ is in $p^5$:


$$
p\cdot\text{atom}\in p^4,\qquad
p^2\cdot\text{atom}\in p^5.
\tag{2.7}
$$



This includes all finite returns from (1.3). It also includes the actual higher head and lower terms **once their coefficient orders have been established**.

---

## 3. The coefficient-unit short-head terms have a fourth event

Under $\mathbf H$, it remains to treat the coefficient-unit part of the short head.

Turn 7’s normal ordering shows that the terms with $1\le r<29$ contain


$$
\binom{2n+r-1}{r}\in p\mathbb Z_p.
$$


The denominators $r!$ are units, so this coefficient factor is paid.

The remaining coefficient-unit terms have upper addend $2n$ and lower index


$$
b-1-j
\quad\text{or}\quad
b-j,
\tag{3.1}
$$


with the retained unshifted or shifted row factor.

In the first two physical digits,


$$
(n+2)\bmod p^2=205,\qquad
2n\bmod p^2=406,
$$




$$
(b-1)\bmod p^2=838,\qquad
b\bmod p^2=839.
$$



If the two weight digits have no borrow, then


$$
j\bmod p^2\le205.
$$


The corresponding two-digit lower index is at least $633$, so adding $406$ forces a carry beyond those two digits. If the weight digits do borrow, a valuation event is already present.

Thus every coefficient-unit term has at least one valuation event in positions $0,1$. Together with Lemma 2.1’s two middle-block events and the event at position $7$, this gives four events.

### Proposition 3.1 — Complete column saturation under $\mathbf H$

At every original index


$$
u\equiv2\pmod{24389},
$$


if $\mathbf H$ holds, then the complete reconstructed first column satisfies


$$
\boxed{Z_w\in p^4\mathbb Z_p^{\,b+1}.}
\tag{3.2}
$$



No first-order head, lower, or finite-return term was discarded in this proof: all of them are covered by (2.7).

---

## 4. The original terminal coordinate is deeper than the required layer

The physical terminal weight is


$$
W_b=\binom{n+2}{b}.
$$



The low nine digits of $b$ and $n+2$, in least-significant-first order, are


$$
b:\quad(27,28,5,28,0,20,7,25,24),
$$




$$
n+2:\quad(2,7,24,7,3,9,19,8,3).
$$



Subtracting $b$ from $n+2$, the outgoing weight borrows at positions


$$
0,1,3,5,7,8
$$


are all $1$. Hence


$$
\boxed{v_p(W_b)\ge6.}
\tag{4.1}
$$



The retained terminal contact value is integral. Therefore the physical terminal coordinate is zero modulo $p^6$.

In particular, the terminal square that must be restored in the general next-norm identity,


$$
22A_0^2\left(\frac{W_b}{p^4}\right)^2,
\tag{4.2}
$$


is indeed retained, but is zero at this phase because


$$
W_b/p^4\in p^2\mathbb Z_p.
$$



This is a phase-specific valuation proof. It is not the earlier argument that the terminal square was below the previous norm precision.

---

## 5. Why every contribution to the new normalized column has the same upper interface

The preceding saturation proof also identifies the only terms that can contribute to


$$
Z_w/p^4\pmod p.
$$



They are:

1. coefficient-unit short-head terms with exactly one event below position $3$;
2. coefficient-$p$ terms with no event below position $3$.

All coefficient-$p^2$ terms are in $p^5$, by (2.7).

### 5.1 Event-free low blocks have zero outgoing interface

Write


$$
j=\ell+DJ,\qquad 0\le\ell<D.
$$


Suppose an atom has no weight-borrow or addition-carry event below position $3$. Then


$$
\ell\le20389,
$$


and its low lower index $K_{\rm low}$ satisfies


$$
K_{\rm low}\le24388-(16384+a)=8004-a.
$$



If a lower-index borrow left this block, then


$$
\ell+K_{\rm low}=5044+v+D.
$$


But the left side is at most $28393-a$, while the right side is at least $29083$. This is impossible.

Thus every event-free low block exits with all three interface bits zero.

### 5.2 Minimal coefficient-unit blocks also exit with all three bits zero

The coefficient-unit terms already have an event in positions $0,1$, by §3. A contribution at total depth exactly $4$ can have no additional low event at position $2$. Its outgoing weight borrow and addition carry are therefore zero.

The same numerical inequality as above excludes an outgoing lower-index borrow. Hence these terms also enter physical position $3$ with the zero interface.

### 5.3 Common exact high kernel after the three-digit split

Define


$$
B=\frac{b-5044}{D},\qquad
W=\frac{n+2-20389}{D}.
$$


Since


$$
\frac{2n-16385}{D}=2W+1,
$$


the common upper kernel is


$$
U(J)=
\binom WJ
\binom{2W+1+B-J}{B-J}.
\tag{5.1}
$$



All terms contributing to $Z_w/p^4\bmod p$ enter this upper problem with zero interface. Their differences are confined to their first three digits, their integral row factors, and their actual coefficients.

Consequently there is a finite low function $a_\ell\in\mathbb F_p$ such that


$$
\boxed{
\left(\frac{Z_w}{p^4}\right)_{\ell+DJ}
=
\varepsilon_{\ell,J}\,a_\ell\,\frac{U(J)}{p^3}
\pmod p,
}
\tag{5.2}
$$


on the actual reconstructed range, where $\varepsilon_{\ell,J}\in\{\pm1\}$ is the common negative-binomial sign.

The sign disappears in the squared norm.

Importantly, $a_\ell$ contains the **sum of all actual first-order head, lower, and return contributions** at that low coordinate. It is not merely the leading-head coefficient.

---

## 6. The low function is finite and all its divisions are paid

For clarity, (5.2) is not an assertion that unspecified rational ratios can be reduced modulo $p$.

For an active normal-form atom, let $e_{\rm low}\in\{0,1\}$ be its low-block event count. Let $f_r=r!\pmod p$, $0\le r<p$. Its normalized low binomial unit is obtained from


$$
(-1)^{e_{\rm low}}
\prod_{i=0}^{2}
\frac{f_{W_i}f_{Z_i}}
     {f_{j_i}f_{L_i}f_{A_i}f_{K_i}},
\tag{6.1}
$$


with the actual subtraction and addition digits $L_i,K_i,Z_i$.

Every denominator in (6.1) is a unit.

The low function $a_\ell$ is the sum of:

* the coefficient-unit terms with $e_{\rm low}=1$, after stripping that one binomial factor $p$;
* the coefficient-$p$ terms with $e_{\rm low}=0$, after dividing their **actual coefficient** by $p$.

Integral row factors are evaluated before reduction. Their bounded integer-valued polynomial indices lie below $p^3$, so their mod-$p$ values depend only on $\ell$, by Lucas reduction of their binomial-basis terms. A nonunit row factor can only make a term deeper; it cannot introduce a denominator.

Thus


$$
\mathscr L:=\sum_{\ell=0}^{D-1}a_\ell^2\in\mathbb F_p
\tag{6.2}
$$


is an explicit finite low contraction.

Its numerical value will not be needed: the complete upper contraction multiplying it is zero. That is why the proof can retain arbitrary actual first-order coefficients without requesting a complete new producer.

---

## 7. The inclusive reconstruction cutoff is not completed silently

For fixed $\ell$, the actual range is


$$
0\le J\le
\begin{cases}
B,&\ell\le5044,\\
B-1,&\ell>5044.
\end{cases}
\tag{7.1}
$$



The endpoint $J=B$ of the common upper kernel has at least four weight borrows. Indeed, the relevant upper digits are


$$
W:(7,3,9,19,8,3),\qquad
B:(28,0,20,7,25,24),
$$


and the outgoing borrows at positions $0,2,4,5$ are $1$. Hence


$$
U(B)\in p^4\mathbb Z_p,
\qquad
U(B)/p^3=0\pmod p.
\tag{7.2}
$$



Therefore the two genuinely different ranges in (7.1) have the same normalized squared contraction modulo $p$. This follows from a proved zero of the missing endpoint; it is not an unrestricted completion of the last block.

Combining (5.2)–(7.2),


$$
\boxed{
\frac{Z_w^TZ_w}{p^8}
=
\mathscr L
\sum_{J=0}^{B}\left(\frac{U(J)}{p^3}\right)^2
\pmod p.
}
\tag{7.3}
$$



The physical terminal coordinate has already been accounted for in §4.

---

## 8. Complete contraction of the common upper block

The first three digits of $U$ are exactly the physical positions $3,4,5$ in (2.4), now entered with zero interface.

The minimal two-event paths can be classified without an additional computation.

* At the first digit,
  

$$
j_3\in\{0,\ldots,7\}\cup\{15,\ldots,28\}.
$$


* A nonzero digit $j_4$ cannot occur on a two-event path. If it did, the lower-index borrow would be $1$, and a zero-event next digit would require simultaneously
  

$$
j_5\le9-w,\qquad j_5\ge9+c,
$$


  even though $w+c\ge1$.
* Hence $j_4=0$, and the interface resets before digit $5$.
* The last digit has
  

$$
0\le j_5\le20.
$$


  The ranges $0\le j_5\le9$ and $10\le j_5\le20$ give the two retained high interfaces.

Reuse the accepted coefficients


$$
K_{34}=12,\qquad 10,\ 19
$$


for this zero-input upper block.

Let


$$
X=2001C+1382,
$$




$$
V(q)=\binom Xq\binom{2X+C-q}{C-q},
$$




$$
F_{\rm I}(q)=(2X+C+1-q)V(q),
$$




$$
F_{\rm II}(q)=(X-q)V(q).
\tag{8.1}
$$



At the present phase, $p\mid V(q)$ for every $0\le q\le C$. Therefore both divisions $F_{\rm I}/p$ and $F_{\rm II}/p$ are integral.

The complete upper contraction is


$$
\boxed{
\sum_{J=0}^{B}\left(\frac{U(J)}{p^3}\right)^2
=
12\left[
10\sum_{q=0}^{C}\left(\frac{F_{\rm I}(q)}p\right)^2
+
19\sum_{q=0}^{C}\left(\frac{F_{\rm II}(q)}p\right)^2
\right]
\pmod p.
}
\tag{8.2}
$$



This is the requested finite-high-observable target after complete contraction. It contains no lifted use of
$\eta=A_0^2\kappa$. It was derived from the new physical normalization (5.2).

---

## 9. The high combination is zero without the pending $42$ numerical values

Define the exact finite moments


$$
T_h=\sum_{q=0}^{C}q^hV(q)^2,\qquad h=0,1,2.
$$


Since $p\mid V(q)$, every $T_h/p^2$ is integral.

The difference of the two normalized interface squares is exactly


$$
\begin{aligned}
\mathcal B(C)
&:=
\sum_{q=0}^{C}\left(\frac{F_{\rm I}(q)}p\right)^2
-
\sum_{q=0}^{C}\left(\frac{F_{\rm II}(q)}p\right)^2\\
&=
\frac{(X+C+1)\bigl((3X+C+1)T_0-2T_1\bigr)}{p^2}.
\end{aligned}
\tag{9.1}
$$



The whole numerator is divided by $p^2$; its integrality also follows term by term from the first line.

### 9.1 The required first-moment relation is symbolic

The three-digit valuation-one classification from Turn 10 gives


$$
\boxed{
2(T_1/p^2)=7(T_0/p^2)\pmod p.
}
\tag{9.2}
$$



This part does not require the numerical values of the $42$ one-event unit contributions.

Indeed, for each low cutoff branch


$$
d+k=7+29\varepsilon,\qquad \varepsilon\in\{0,1\},
$$


the first-digit weight is symmetric in $d,k$. The rest of a valuation-one path depends on the branch $\varepsilon$, not on which of $d,k$ is designated first. Consequently,


$$
2\sum d\,w_dw_k
=
7\sum w_dw_k\pmod p
$$


within **each** branch separately.

The one-event bridge returns to zero interface after the third digit. Its actual terminal relation is


$$
r+s=t,
$$


so no unfinished cutoff carry or infinite tail is introduced.

At the phase in question,


$$
X+C+1\equiv27,\qquad
3X+C+1\equiv7\pmod p.
$$


Equation (9.2) therefore gives


$$
\boxed{\mathcal B(C)=0\pmod p.}
\tag{9.3}
$$



Since $19=-10\pmod{29}$, (8.2) becomes


$$
12\cdot10\,\mathcal B(C)=4\mathcal B(C)=0.
$$



Finally, (7.3) yields


$$
\boxed{
\eta_2=\frac{Z_w^TZ_w}{p^8}=0\pmod p
}
\tag{9.4}
$$


under $\mathbf H$, independently of $\mathscr L$.

This is a complete contraction of all terms that can enter the normalized column. The unevaluated low scalar is harmless because every possible value multiplies a proved zero.

---

## 10. Relation to the complete $Z_w\bmod p^6$ identity

The complete physical identity remains


$$
Z_w\equiv p^3z_0+p^4z_1+p^5z_2\pmod{p^6}.
$$


At a known $d\ge8$ case,


$$
\eta_2=
\frac{
z_0^Tz_0+2p\,z_0^Tz_1+
p^2(z_1^Tz_1+2z_0^Tz_2)
}{p^2}
\pmod p.
\tag{10.1}
$$



Under $\mathbf H$, Proposition 3.1 proves $z_0=0$. Hence


$$
\eta_2=z_1^Tz_1\pmod p.
\tag{10.2}
$$



The treatment of the formerly eliminated terms is now precise:

* coefficient-$p$ head, lower, and finite-return terms are retained in $a_\ell$ and therefore in $z_1$;
* coefficient-$p^2$ terms, including the second-lower and crossed-return sectors, are at least $p^5$ by Lemma 2.1;
* those terms can enter $z_2$; I have not declared them zero modulo $p^6$;
* their contribution to (10.1) disappears because the newly proved complete normalization gives $z_0=0$, not because their old $p^5$ elimination was incorrectly lifted;
* the terminal square is retained and evaluated separately by (4.1).

Thus the proof does not promote the audited mod-$p$ formula for $\eta$ to higher precision.

---

## 11. What is and is not established for the actual original column

The proved implication is


$$
\boxed{
\mathbf H
\quad\Longrightarrow\quad
c\ge2,\qquad d\ge9
}
\tag{11.1}
$$


for every original


$$
u\equiv2\pmod{24389}.
$$



No upper bound on $c$ follows. In particular:

* if $c=2$, then $\nu\ge1$;
* if $c\ge3$, the norm is already in $p^{10}$;
* neither alternative establishes the first nonzero primitive norm digit.

### The precise obstruction to an unconditional actual instantiation

The actual norm reduction


$$
\eta=A_0^2\kappa\pmod p
$$


can hold even when additional actual-head vectors lie in a contracted radical. It does not identify the coefficient-unit sector of the column.

Without $\mathbf H$, an additional coefficient-unit head term need only receive the three uniform events of Lemma 2.1. The displayed sources do not give its actual coefficient, so they do not determine whether the complete $p^3$-residual vanishes.

I therefore do not exhibit a $c=1$ term: no such **actual full-source coefficient** has been supplied or evaluated here. An arbitrary-head example would not answer the assignment.

The outstanding source-specific lemma is now:

> **Actual unit-head lemma.**  
> In the integral finite normal form of the original $f^0$, identify the entire coefficient-unit sector and prove that it is the short-head sector specified by $\mathbf H$, or give the nonzero residual sector with its actual paid coefficients.

If this lemma is already closed in the accepted background, its exact statement instantiates (11.1) immediately. If it is not closed, the actual $c\ge2$ target remains open despite the completed saturation-and-radical argument.

---

## 12. Precision budgets and the next physical layer

The retained budgets are unchanged:


$$
\boxed{K_Z^{\rm norm}\ge d-c-1,}
$$




$$
\boxed{
K_Z^{\rm mixed}\ge d-1,\qquad
K_Y^{\rm mixed}\ge d-c,\qquad
N_{\log}\ge d-c.
}
$$



If $\mathbf H$ is certified, then $c\ge2$ and $d\ge9$. In the case $c=2$, a complete lift modulo $p^6$ is sufficient to determine the next raw norm digit at $p^9$.

That next digit would involve the whole carry in


$$
z_1^Tz_1+2p\,z_1^Tz_2.
$$


The present radical evaluates $z_1^Tz_1\bmod p$; it does not evaluate its lift modulo $p^2$, nor the contraction with $z_2$.

Thus the higher head, second-lower, crossed-return, and higher endpoint pieces cannot be removed from that subsequent calculation.

---

## 13. Complete second force and global normalization are unchanged

The second-force identity remains


$$
p^3U_a^TQ=
p^3(r_0G^{(3)}_{a0}+r_1G^{(3)}_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda'_{a,\ell}
+W_bU_{a,b}.
\tag{13.1}
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



There is no source row at $b-1$. The exterior at $b$ is not another recurrence step. The division in (13.1) belongs to its whole right-hand side.

The unresolved mixed target remains


$$
x^TQ-p^c\rho_nx^Tx
\equiv0\pmod{p^{c+\nu+1}}.
$$



No actual row content, row metric $\Omega$, or least two-column clearer is changed. Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
$$


The gcd remains over all primes, and the primitive multiplier is $d_B^2/g_B$.

In particular,


$$
\log q_n=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
$$



For the same original index,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


and the relevant whole error remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{13.2}
$$



The new local lemma neither bounds this all-prime denominator nor evaluates a nonzero real error.

---

## 14. Bounded exact arithmetic: what is pending and what is newly needed

### 14.1 Existing pending work is not assumed or requested again

The coordinator’s new checks of

* the $42$ one-event contributions;
* the exact complete high sums at bounded $C=20916+29^3t$;
* the actual-original normalized-tail prefix;

remain pending.

The proof above uses the symbolic one-event classification and branchwise first-moment reflection, not the pending numerical coefficients $(23,8,18)$.

The normalized tail test remains a distinct target. Its prescribed input is still


$$
E=1397629859,\qquad R=3^E\bmod29^{41},
$$


followed by the $32$-digit ordinary tail transport. A zero row proves tail annihilation; a nonzero residual row does not prove a nonzero final tail. No rerun is proposed.

### 14.2 The new bounded certificate is an actual-head certificate, not a column scan

First check whether $\mathbf H$ already has an accepted proof. If so, cite it; do not recompute it.

Otherwise the missing bounded task is:

**Inputs**

1. the exact definition or recurrence of the actual finite head entering $w=\mathsf P_-h^{\rm act}$;
2. its retained integral normalization;
3. the original $u=2$ phase;
4. the precision-$p^6$ head cutoff $L=350$;
5. the retained normal-ordering rules.

**Expected verifiable output**

Either:

* a proof-backed residue table showing
  

$$
h_i^{\rm act}\equiv A_0i!\pmod p\quad(0\le i<29),
  \qquad
  h_i^{\rm act}\equiv0\pmod p\quad(29\le i\le350),
$$


  together with the already established truncation beyond the cutoff; or

* the complete nonzero unit-order residual table after subtracting the short-head sector, followed by its actual normal-ordered coefficient classes.

Any factorial or rational denominator in forming those residues must be paid before reduction. The source supplied here does not contain the actual-head recurrence, so I cannot responsibly prescribe its modular guard or invent its output.

This task concerns at most a bounded head table and its finite unit-order conversion. It does not construct the original-length integer, traverse the $b$-row matrix, or rerun an accepted producer.

---

## 15. Proof-status ledger

| Statement | Status |
|---|---|
| Accepted original prefix annihilations and previous bounded controls | Reused at their stated scope |
| New $42$-term and bounded high-sum checks | Pending; not assumed |
| Actual-original normalized-tail prefix test | Pending; distinct target |
| Shift-uniform three-event bound for every retained physical atom | **Proved** |
| Actual terminal $v_p(W_b)\ge6$ at the $u=2$ phase | **Proved** |
| Fourth event for every coefficient-unit short-head term | **Proved** |
| All positive-order finite-return/head/lower terms retained in saturation | **Proved** |
| Common zero-interface factorization of the complete $p^4$-layer under $\mathbf H$ | **Proved** |
| Both original low cutoff branches and inclusive reconstruction endpoint | **Explicitly retained** |
| Complete upper contraction as the two normalized finite interface sums | **Proved** |
| That upper contraction is zero, without the pending $42$ values | **Proved** |
| $\mathbf H\Rightarrow c\ge2,\ d\ge9$ on the original progression | **Proved conditional implication** |
| Actual-head interface $\mathbf H$ for the supplied $f^0$ | Not explicitly established in the attached sources |
| Unconditional actual $c\ge2$, or an actual surviving $c=1$ coefficient | Still unresolved from the displayed data |
| First nonzero primitive norm layer | Open |
| Complete second-force alignment | Open |
| All-prime primitive denominator versus whole nonzero error | Open |

## Conclusion

The new completed mathematical result is a **full-source saturation-and-radical lemma**, not another isolated lift of $T_h$.

At the original $u=2$ phase, every retained finite shift receives the same extra physical event. Once the actual coefficient-unit head sector is identified with the short-head sector, this gives


$$
Z_w\in29^4\mathbb Z_{29}^{\,b+1}.
$$


All first-order head, lower, and finite-return contributions then enter a common complete contraction:


$$
\eta_2
=
12\mathscr L
\left[
10\sum_{q=0}^{C}(F_{\rm I}/29)^2+
19\sum_{q=0}^{C}(F_{\rm II}/29)^2
\right]
=0\pmod{29}.
$$


The terminal square is included and is zero by the stronger actual weight valuation. The second-order corrections are not improperly discarded modulo $29^6$; they fall into $z_2$, which ceases to affect $\eta_2$ only after complete column divisibility has been proved.

The exact local bottleneck is now the **actual unit-head interface**, not a higher carry row or an unread normalized tail. The supplied norm reduction does not certify that interface, and I have not silently promoted it.

Even if that interface is certified and the consequences $c\ge2,\ d\ge9$ become unconditional on the original progression, the complete mixed-force alignment and the all-prime denominator/whole-error comparison remain open. Therefore an unconditional proof or disproof of the irrationality of $e+\pi$ has not been obtained.
