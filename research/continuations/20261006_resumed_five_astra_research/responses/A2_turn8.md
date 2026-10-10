> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 8 — An evaluated two-unit-digit interface for the square carry, with exact high-moment reduction

## Executive assessment

I retain the original family


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad
n=2001b,\qquad u\ge0,
$$


and the original cutoff $0\le j<b$ in the single-atom norm. The actual next head, second-return charges, and correction-contraction zeros established in Turn 7 are reused at their stated precisions; none is reopened as an unknown input.

The main new result is an **evaluated low-interface formula** for the entire carry. Put


$$
\Lambda=29^6,\qquad \beta=410910916,\qquad
b=\beta+\Lambda C,\qquad X=2001C+1382,
$$


and, throughout this report,


$$
K=C-q,\qquad 0\le q\le C.
$$


Define


$$
V(q)=\binom Xq\binom{2X+C-q}{C-q},
$$




$$
F_{\mathrm I}(q)=(2X+C+1-q)V(q),\qquad
F_{\mathrm{II}}(q)=(X-q)V(q).
$$


The three high observables needed below are


$$
D(C)=\frac{\displaystyle\sum_{q=0}^{C}
\bigl(F_{\mathrm I}(q)^2-F_{\mathrm{II}}(q)^2\bigr)}{29}\pmod{29},
\tag{E.1}
$$




$$
S_0(C)=\sum_{q=0}^{C}V(q)^2\pmod{29},\qquad
S_2(C)=\sum_{q=0}^{C}q^2V(q)^2\pmod{29}.
\tag{E.2}
$$


The division in $D(C)$ is of the **whole finite difference**. Its integrality follows from the retained finite-range symmetry.

Then the remaining carry has the explicit reduction


$$
\boxed{
\kappa(b,n)
=
21D(C)+16S_2(C)
+\bigl(25+18C+19C^2+24C^3\bigr)S_0(C)
\pmod{29}.
}
\tag{E.3}
$$



This is obtained by:

1. a compatible factorial-unit expansion modulo $29^2$;
2. evaluation of the cross-digit harmonic coefficients;
3. elimination of a common, unevaluated unit lift by the already-proved high-sum symmetry;
4. an additional weighted finite-range symmetry;
5. an exact zero-flux telescoping identity, with both endpoints retained.

In particular, no low coefficient remains to be computed in (E.3).

The result does **not** evaluate these high observables at a genuine original power-orbit index. It reduces the problem to three explicitly specified scalar observables, but it does not bound the cost of reading or eliminating the original high word.

There is also a useful new obstruction to a phase-wide digit-free answer. The same formulas give the analytically evaluated auxiliary values


$$
\boxed{
\kappa\bigl(\beta+\Lambda C,\;2001(\beta+\Lambda C)\bigr)
=
26,\ 9,\ 10
\quad\text{for }C=0,1,2,
}
\tag{E.4}
$$


whereas


$$
\boxed{
C=\beta\,29^h\quad\Longrightarrow\quad \kappa=0
\qquad(h\ge0).
}
\tag{E.5}
$$


Thus no fixed finite prefix of $C$ determines $\kappa$ on the entire phase-compatible family. This statement concerns that enlarged auxiliary family—not a nonzero value at an original power-orbit index.

---

# 1. Retained results and scope of the new receipt

The corrected columns remain


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,
\qquad W_j=\binom{n+2}{j}.
$$


The finite domains remain


$$
0\le j<b,\qquad 1\le i\le b-2,\qquad 0\le j\le b
$$


for contact coordinates, source rows, and reconstructed coordinates respectively.

I retain


$$
P=\frac{Z_w}{p^2}=p^cx,\qquad Q=\frac{Y}{p^3},
\qquad
\nu=v_p(x^Tx),\qquad d=2c+4+\nu.
$$



The Turn 7 reduction is


$$
\eta=A_0^2\kappa(b,n),
$$


where


$$
\kappa(b,n)=
\frac1{p^7}
\sum_{j=0}^{b-1}
\binom{n+2}{j}^{2}
\binom{2n+b-1-j}{b-1-j}^{2}
\pmod p.
\tag{1.1}
$$



The following are reused as closed contributions to this norm:

- the actual next-head radical;
- the compatible $\mathsf D_2$ elimination;
- the crossed $\mathsf D_1z_1$ elimination;
- the first-lower contraction zero;
- the first-return contraction zero;
- the evaluated second-return charges
  

$$
z_{2,r}=13(-1)^rF_{r-2}\pmod{29}\qquad(2\le r\le28);
$$


- the complete second-return contraction zero;
- the baseline short-head multiplier contraction zero.

The physical terminal coordinate is still


$$
\frac{Z_{w,b}}{p^3}
\equiv
14pA_0\frac{W_b}{p^4}\pmod{p^2}.
\tag{1.2}
$$


Its square does not contribute at the norm precision in (1.1), but the coordinate has not been deleted from the column.

The new coordinator receipt verifies exactly:

- $696$ incoming-state/digit potential inequalities;
- $2003$ weight-offset cases;
- $4004$ upper-offset cases;
- $3$ lower-offset cases.

I use those checks at that finite scope. The complete-column integrality and unbounded-content argument remains subject to the independent audit stipulated in the assignment. The new single-atom calculation below does not need to infer that full-column theorem from the receipt.

---

# 2. Why only the retained three-event support is needed

Write


$$
j=s+\Lambda q,\qquad
s=(d,e,f,t,0,\ell)_{29}.
$$


The retained support is


$$
d\in\{0,1,2\},
$$




$$
e\in\{0,\ldots,7\}\cup\{14,\ldots,28\},
$$




$$
f\in\{0,\ldots,5\},
$$




$$
t\in\{0,\ldots,7\}\cup\{15,\ldots,28\},
\qquad 0\le\ell\le20.
\tag{2.1}
$$



There are


$$
3\cdot23\cdot6\cdot22\cdot21=191268
$$


such low residues.

Every atom has valuation at least three. Outside (2.1), it has valuation at least four, so its square is zero modulo $p^8$. Within (2.1), a possible further high valuation is retained by the high factor itself.

Every supported $s$ is strictly below $\beta$. Consequently the supported original cutoff is exactly


$$
\boxed{0\le q\le C.}
\tag{2.2}
$$


No completion of a last block is made.

At the six-digit interface there are two cases:


$$
\begin{array}{c|cc}
&\text{weight borrow}&\text{positive-binomial carry}\\ \hline
\mathrm I:\ 0\le\ell\le9&0&1\\
\mathrm{II}:\ 10\le\ell\le20&1&0.
\end{array}
\tag{2.3}
$$


These give precisely the high factorial ratios $F_{\mathrm I}$ and $F_{\mathrm{II}}$ displayed above.

---

# 3. A compatible two-unit-digit factorial expansion

For $0\le a\le28$, put


$$
H_a=\sum_{r=1}^{a}\frac1r\in\mathbb F_{29},
\qquad H_0=0,
$$


and let


$$
\mathcal F(m)=\prod_{\substack{1\le r\le m\\29\nmid r}}r.
$$



For $m=29h+a$,


$$
\boxed{
\mathcal F(29h+a)
\equiv
(28!)^h\,a!\,(1+29hH_a)
\pmod{841}.
}
\tag{3.1}
$$



Indeed, each complete block has product $28!$ modulo $841$, since


$$
H_{28}=0\pmod{29},
$$


and the last partial block gives the displayed harmonic factor. This is the standard prime-power factorial-unit mechanism; here it is applied with the actual factorial arguments and six-digit boundary.

Apply factorial stripping through six levels to


$$
\binom{n+2}{j}\binom{2n+b-1-j}{b-1-j}.
$$


On (2.1), the low valuation exponent is exactly three. After division by $p^3$, its square has the form


$$
\boxed{
g_\alpha\binom{20}{\ell}^{2}
\left(1+2p\sum_{r=0}^{5}E_r\right)
F_{\tau}(q)^2
\pmod{p^2},
}
\tag{3.2}
$$


where

- $\alpha=(d,e,f,t)$;
- $\tau=\mathrm I$ or $\mathrm{II}$, according to (2.3);
- $g_\alpha$ is a fixed unit-ratio coefficient modulo $841$;
- $E_r$ is the signed factorial-unit harmonic correction at digit $r$.

The common Wilson-factor contribution is included in $g_\alpha$. It is not chosen independently of the factorial lift.

The accepted leading coefficients imply


$$
\boxed{\sum_\alpha g_\alpha=5\pmod{29}.}
\tag{3.3}
$$


Indeed,


$$
5\cdot10=21,\qquad 5\cdot19=8\pmod{29},
$$


which agrees with the corrected complete low pair $21,8$.

The work remaining is to determine which parts of the second unit digit survive the contraction. It is not necessary to calculate every $g_\alpha$ modulo $841$ separately.

---

# 4. Cross-digit corrections below the high interface

For $r\le3$, $E_r$ is independent of $\ell,C,q$.

At digit four, the only relevant distinction is the range of $t$. The lower-index digit is zero, while the weight-complement and positive-top digits are


$$
\begin{array}{c|cc}
t&\text{weight complement at digit 4}&\text{positive top at digit 4}\\ \hline
0\le t\le7&3&7\\
15\le t\le28&2&6.
\end{array}
$$


The next digits of those two factorial arguments are both $9-\ell$ modulo $29$. Hence


$$
E_4
=
9H_3-18H_6
+(9-\ell)(H_{\rm top}-H_{\rm comp}).
$$


Using


$$
H_3=26,\quad H_7=26,\quad H_2=16,\quad H_6=1,
$$


this becomes


$$
\boxed{
E_4=
\begin{cases}
13,&0\le t\le7,\\
23+15\ell,&15\le t\le28.
\end{cases}
}
\tag{4.1}
$$



Thus all corrections below digit five have the form


$$
E_0+\cdots+E_4=A_\alpha+B_\alpha\ell.
\tag{4.2}
$$



They cannot simply be discarded separately on the two interfaces. Their elimination in the **sum of the two interface constants** follows from the exact identities


$$
\sum_{\ell=0}^{20}\binom{20}{\ell}^{2}
=\binom{40}{20},
$$




$$
\sum_{\ell=0}^{20}\ell\binom{20}{\ell}^{2}
=10\binom{40}{20},
\tag{4.3}
$$


both of which are zero modulo $29$.

This is the required cross-digit accounting: the terms in (4.1) are retained first, and their aggregate contribution is then proved to vanish.

---

# 5. The digit-five harmonic interface

Set


$$
R_\ell=
\begin{cases}
9-\ell,&0\le\ell\le9,\\
38-\ell,&10\le\ell\le20.
\end{cases}
$$


The digit-five factorial ratios cancel to


$$
\frac{9!}{18!\,20!}\binom{20}{\ell}
$$


before squaring.

At this digit, the harmonic correction is


$$
\begin{aligned}
E_5={}&
XH_9-qH_\ell
-(X-q-w)H_{R_\ell}\\
&+(2X+C-q+c)H_{R_\ell}
-2XH_{18}-(C-q)H_{20-\ell}.
\end{aligned}
$$


Here $w+c=1$, by (2.3). Since $X\equiv19\pmod{29}$,


$$
\boxed{
\begin{aligned}
E_5={}&19(H_9-2H_{18})+20H_{R_\ell}\\
&+C(H_{R_\ell}-H_{20-\ell})
+q(H_{20-\ell}-H_\ell)
\pmod{29}.
\end{aligned}
}
\tag{5.1}
$$



This explicitly includes the coupling between the last low digit and the genuine high factorial arguments.

## 5.1 Evaluated harmonic sums

For reproducibility, the squared binomial residues for $0\le\ell\le10$ are


$$
\binom{20}{\ell}^{2}
=
(1,23,24,23,4,5,24,9,7,6,9)\pmod{29},
$$


and the remaining entries follow by reflection.

The required sums are:


$$
\begin{array}{c|rr}
\text{sum, weighted by }\binom{20}{\ell}^2
&\mathrm I&\mathrm{II}\\ \hline
1&10&19\\
H_{R_\ell}&24&1\\
H_{R_\ell}-H_{20-\ell}&3&24\\
H_{20-\ell}-H_\ell&28&1.
\end{array}
\tag{5.2}
$$



Multiplication by the squared-norm factor $2$ and the common coefficient $5$ therefore gives the evaluated slopes


$$
\boxed{
\begin{array}{c|rr}
& C&q\\ \hline
\mathrm I&1&19\\
\mathrm{II}&8&10.
\end{array}
}
\tag{5.3}
$$



These coefficients are small but consequential: in particular, the $q$-terms are not absent.

---

# 6. The whole low carry, including the ordinary integer carry

Let $\lambda_{\mathrm I},\lambda_{\mathrm{II}}\in\mathbb Z/841\mathbb Z$ be the actual two interface constants at $C=q=0$, using the compatible factorial lift above. Thus the actual low contractions have the form


$$
\lambda_{\mathrm I}+29(C+19q),
\qquad
\lambda_{\mathrm{II}}+29(8C+10q).
\tag{6.1}
$$


Their reductions are


$$
\lambda_{\mathrm I}=21,\qquad
\lambda_{\mathrm{II}}=8\pmod{29}.
$$



What matters is not an arbitrary choice of lifts of $21$ and $8$, but the actual sum of the two lifted constants.

First,


$$
\frac1{29}\binom{40}{20}
\equiv-\frac{11!}{(20!)^2}=2\pmod{29}.
\tag{6.2}
$$


Thus the ordinary binomial-sum carry contributes


$$
5\cdot2=10.
$$



By (4.2)–(4.3), every correction from digits zero through four contributes zero to the divided sum of the interface constants.

For digit five, the constant part of (5.1) contributes


$$
\sum_{\ell=0}^{20}
\binom{20}{\ell}^{2}
\bigl(19(H_9-2H_{18})+20H_{R_\ell}\bigr)
=20(24+1)=7\pmod{29}.
$$


Its squared-unit contribution is therefore


$$
2\cdot5\cdot7=12.
$$


Combining the two contributions proves


$$
\boxed{
\lambda_{\mathrm I}+\lambda_{\mathrm{II}}
=29\cdot22\pmod{841}.
}
\tag{6.3}
$$



This includes the carry after the whole leading cancellation. In particular, $21+8=29$ has not been silently replaced by an integer zero.

## 6.1 Eliminating the common lift rather than leaving it unevaluated

Write


$$
\lambda_{\mathrm I}=21+29a.
$$


Then (6.3) gives


$$
\lambda_{\mathrm{II}}=-21+29(22-a).
$$


The $a$-dependent contribution to the whole norm is


$$
29a\sum_{q=0}^{C}
\bigl(F_{\mathrm I}(q)^2-F_{\mathrm{II}}(q)^2\bigr),
$$


which is zero modulo $841$ by the retained finite-range symmetry.

Consequently the common lift is **eliminated**, not retained as a computational input.

The resulting fully evaluated, norm-effective low interface is


$$
\boxed{
\begin{aligned}
\mathcal N(C)\equiv
\sum_{q=0}^{C}\bigl[
&\bigl(21+29(C+19q)\bigr)F_{\mathrm I}(q)^2\\
+&\bigl(-21+29(22+8C+10q)\bigr)F_{\mathrm{II}}(q)^2
\bigr]\pmod{841},
\end{aligned}
}
\tag{6.4}
$$


where


$$
\mathcal N(C)=
\frac1{29^6}\sum_{j=0}^{b-1}
\binom{n+2}{j}^{2}
\binom{2n+b-1-j}{b-1-j}^{2}.
$$


As before,


$$
\kappa=\mathcal N(C)/29\pmod{29}.
$$



Equation (6.4) is an identity for the **contracted norm**. It is not a claim that the two actual interface constants separately equal the displayed representatives.

---

# 7. A weighted symmetry on the exact finite high range

Define


$$
T(C)=\sum_{q=0}^{C}F_{\mathrm{II}}(q)^2\pmod{29},
\qquad
M(C)=\sum_{q=0}^{C}qF_{\mathrm{II}}(q)^2\pmod{29}.
$$



The retained symmetry has the following weighted extension:


$$
\boxed{
\sum_{q=0}^{C}qF_{\mathrm I}(q)^2
=
CT(C)-M(C)\pmod{29}.
}
\tag{7.1}
$$



To check the boundary, write


$$
C=\delta+29C_7,\qquad
q=d+29r,\qquad
C-q=k+29(C_7-r-\varepsilon),
$$


where


$$
d+k=\delta+29\varepsilon.
$$


On nonzero low support, $d,k\le19$, and for fixed $\varepsilon$ the range remains


$$
0\le r\le C_7-\varepsilon.
$$


Exchanging $d$ and $k$ preserves this range and the higher factor. It exchanges the squared interface multipliers, while replacing $q\bmod29$ by $C-q\bmod29$. This proves (7.1) without reflecting or completing the entire high word.

Dividing (6.4) only after the whole cancellation now yields


$$
\boxed{
\kappa
=
21D(C)+(22-C)T(C)+20M(C)
\pmod{29}.
}
\tag{7.2}
$$



This is already a three-observable reduction with evaluated coefficients. The next step replaces the weighted interface observables by degree-zero and degree-two moments of one common high weight.

---

# 8. Exact coefficient-weighted telescoping

Put


$$
S_r=\sum_{q=0}^{C}q^rV(q)^2.
$$


The exact ratio is


$$
\frac{V(q+1)^2}{V(q)^2}
=
\frac{(X-q)^2(C-q)^2}
{(q+1)^2(2X+C-q)^2}.
$$


Define


$$
\mathcal A(q)=(X-q)^2(C-q)^2,
\qquad
\mathcal B(q)=q^2(2X+C+1-q)^2.
$$


For every polynomial $R$,


$$
\boxed{
\sum_{q=0}^{C}V(q)^2
\bigl(\mathcal A(q)R(q+1)-\mathcal B(q)R(q)\bigr)=0.
}
\tag{8.1}
$$


The boundary terms vanish exactly:


$$
\mathcal B(0)=0,\qquad \mathcal A(C)=0.
$$


The term $q=C$ is present in the sum; zero flux is not deletion of that term.

For $R=1$, expansion gives


$$
\begin{aligned}
0={}&2(X+1)S_3
-(3X^2+4X+2C+1)S_2\\
&-2XC(X+C)S_1+X^2C^2S_0.
\end{aligned}
\tag{8.2}
$$


At the present phase,


$$
2(X+1)=11\pmod{29},
$$


a unit. Thus this particular cubic reduction is integral at the required prime.

Since


$$
T=X^2S_0-2XS_1+S_2,
$$




$$
M=X^2S_1-2XS_2+S_3,
$$


subtracting $15$ times (8.2) from the polynomial representing


$$
(22-C)T+20M
$$


gives


$$
\begin{aligned}
(22-C)T+20M
={}&16S_2\\
&+(4+22C+19C^2)S_1\\
&+(25+16C+8C^2)S_0
\pmod{29}.
\end{aligned}
\tag{8.3}
$$



The same low-digit reflection, now without an interface multiplier, gives


$$
\boxed{2S_1=CS_0\pmod{29}.}
\tag{8.4}
$$


Substitution in (8.3) proves the announced formula


$$
\boxed{
\kappa
=
21D(C)+16S_2(C)
+\bigl(25+18C+19C^2+24C^3\bigr)S_0(C)
\pmod{29}.
}
\tag{8.5}
$$



For clarity, the remaining divided observable also has the exact expression


$$
\boxed{
D(C)=
\frac{X+C+1}{29}
\bigl((3X+C+1)S_0-2S_1\bigr)\pmod{29},
}
\tag{8.6}
$$


where the product in the numerator is divided as a whole. Formula (8.6) does not authorize division of either factor separately.

This completes the low-interface evaluation and the safe degree reduction.

---

# 9. What obstructs a further digit-free elimination?

There are two distinct issues.

## 9.1 A small parameter shift is not uniformly small for these binomial coefficients

One might try to use


$$
3X+1=29(207C+143)
$$


and replace


$$
-2X-1=X-(3X+1)
$$


by $X$ in a first-order reflection argument.

For $q<29$, ordinary polynomial differentiation makes this legitimate at controlled precision. It is not uniformly legitimate for $q\le C$.

For example, the derivative of


$$
\binom z{29}
$$


at $z=19$ has valuation $-1$: its numerator derivative is a unit, while $29!$ contains one factor $29$. A shift of size $29$ can therefore change this binomial coefficient already modulo $29$.

Thus a Taylor expansion treating the entire high range as if all binomial denominators were units loses precisely the higher-digit information under investigation.

The retained leading symmetry avoids that error by swapping only the lowest high digits while keeping the higher factor and its exact range fixed. That argument establishes divisibility of the whole difference, but not its next digit.

## 9.2 Rational rank three is not an unrestricted integral reduction theorem

For $R(q)=q^r$, the leading coefficient of the telescoping polynomial in (8.1) is


$$
r+2X+2.
$$


Modulo $29$, this is $r+11$, which is singular when


$$
r\equiv18\pmod{29}.
$$


The particular cubic reduction used above is safe. An unrestricted appeal to the rational three-dimensional quotient would not establish a saturated integral observable module at arbitrary degrees or precisions.

Accordingly, (8.5) supplies a concrete three-scalar reduction, but not a general prime-power closure theorem that evaluates the original high word at bounded total cost.

---

# 10. Evaluated auxiliary values $C=0,1,2$

The new formula permits hand evaluation for the initially proposed small auxiliary inputs. These are analytical finite evaluations, not results attributed to an executed program.

For these three values, the denominators occurring in the relevant binomial polynomials are units at $29$. The computations give


$$
\begin{array}{c|rrrr}
C&D(C)&T(C)&M(C)&\kappa\\ \hline
0&18&13&0&26\\
1&18&2&7&9\\
2&19&25&15&10.
\end{array}
\tag{10.1}
$$



Here are explicit checks of the divided column.

### $C=0$

Then $X=1382$, and


$$
D=\frac{(2X+1)^2-X^2}{29}
=\frac{(X+1)(3X+1)}{29}
=18\pmod{29}.
$$


Therefore


$$
\kappa=21\cdot18+22\cdot13=26\pmod{29}.
$$



### $C=1$

The two middle squares cancel exactly, giving


$$
\sum(F_{\mathrm I}^2-F_{\mathrm{II}}^2)
=
(3X+1)(X+2)(5X^2+5X+2).
$$


Here $X=3383$, so


$$
D=18\pmod{29},
$$


and


$$
\kappa=21\cdot18+21\cdot2+20\cdot7=9\pmod{29}.
$$



### $C=2$

The exact difference is a polynomial with unit denominators and has a factor $3X+1$. At $X\equiv19\pmod{29}$, its derivative is $24$. Since


$$
\frac{3X+1}{29}=557=6\pmod{29},
$$




$$
D=\frac63\cdot24=19\pmod{29}.
$$


The other values in (10.1) give


$$
\kappa=21\cdot19+20\cdot25+20\cdot15=10\pmod{29}.
$$



These inputs are


$$
b=\beta,\quad \beta+\Lambda,\quad \beta+2\Lambda,
\qquad n=2001b.
$$


They are not original power-orbit evaluations.

---

# 11. A proved obstruction to a phase-wide finite-prefix law

The auxiliary nonzero value at $C=0$ can be combined with the repeated-block potential without using the disputed step from atom valuations to the complete corrected column.

Take


$$
C_h=\beta\,29^h,\qquad
b_h=\beta+\Lambda\beta\,29^h,\qquad h\ge0.
$$


The lower six digits give the retained three-event bound. The additional prescribed $\beta$-block gives at least two more events for the single atom


$$
W_j\binom{2n+b_h-1-j}{b_h-1-j}
=
(-1)^{b_h-1-j}
W_j\binom{-2n-1}{b_h-1-j}.
$$


This is exactly the atom form covered by the potential, with offsets $a=1,v=-1$.

Hence every atom has valuation at least five. Its square is divisible by $29^{10}$, and therefore


$$
\boxed{\kappa(b_h,2001b_h)=0\pmod{29}.}
\tag{11.1}
$$



But


$$
C_h\equiv0\pmod{29^h},
$$


while the value at $C=0$ is $26$.

### Theorem 11.1 — No fixed-prefix law on the whole compatible family

There is no fixed integer $m$ such that $\kappa$ on all nonnegative phase-compatible $C$ is determined by $C\bmod29^m$.

### Proof

Choose $h\ge m$. The inputs $C=0$ and $C=C_h$ have the same residue modulo $29^m$, but their values are $26$ and $0$. ∎

This is a genuine high-dependence obstruction, extending arbitrarily far above the retained low block.

It does **not** prove that the restriction to the original power orbit is nonconstant, or that any original index has nonzero carry. In particular, principal-unit realization of a finite prefix cannot transfer the auxiliary value $26$ to an original index: the theorem shows why such a transfer would be invalid.

Nor have I used finite-prefix rigidity to infer a zero before proving a finite-prefix law. No such law has been established on the original orbit.

---

# 12. The remaining original-compatible bottleneck

The concrete original problem is now:

> Evaluate, or eliminate by a further exact identity, the combination
> 

$$
> 21D(C)+16S_2(C)
> +(25+18C+19C^2+24C^3)S_0(C)
>
$$


> for
> 

$$
> C=\frac{3^{249005515+574312172u}-\beta}{29^6},
> \qquad u\ge0.
>
$$



The low contraction has been completed. The unresolved quantity is no longer a family of low factorial coefficients or a correction-column contribution.

The exact remaining precision requirement is:

- $S_0,S_2$ modulo $29$;
- the whole difference defining $D$ modulo $29^2$, before division by $29$.

The observable count is three. The total original-input evaluation cost is not yet bounded independently of the high word.

A concrete follow-on lemma is therefore:

### Outstanding high-carry connection lemma

Construct a finite-range-preserving transformation of the triple


$$
(D,S_0,S_2)
$$


under removal of one high base-$29$ digit, with:

1. explicit integral coefficients at the stated unequal precisions;
2. the two cutoff branches $\varepsilon=0,1$ retained;
3. a proved closed observable space of bounded size;
4. an evaluation or annihilation of the specific row
   

$$
\bigl(21,\ 25+18C+19C^2+24C^3,\ 16\bigr),
$$


   rather than closure alone.

The last condition is essential. A bounded-dimensional transport that still requires the entire original digit word would not by itself settle the desired original-index carry.

---

# 13. A genuinely new bounded auxiliary check

No accepted bounded computation needs to be rerun.

A new implementation check can directly test the two-unit-digit square carry at


$$
C=0,1,2.
$$



## Inputs

- $p=29$, $\Lambda=29^6$, $\beta=410910916$;
- $b=\beta+\Lambda C$, $n=2001b$;
- the $191268$ supported low residues in (2.1);
- $q=0,\ldots,C$, with the exact cutoff retained;
- the factorial-unit formula (3.1), using actual factorial-digit ratios modulo $841$;
- the exact high factors $F_{\mathrm I},F_{\mathrm{II}}$.

This requires


$$
191268(1+2+3)=1147608
$$


supported atom evaluations, not enumeration of $j=0,\ldots,b-1$.

## Expected verifiable output

The direct sparse calculation should return


$$
\boxed{
\mathcal N(C)\pmod{841}
=
754,\ 261,\ 290
\quad(C=0,1,2),
}
\tag{13.1}
$$


and, after checking divisibility by $29$,


$$
\boxed{\kappa=26,\ 9,\ 10.}
\tag{13.2}
$$



It should also compare its result with the independently reduced high-observable table (10.1).

These are predictions proved by the derivation above; there is no supplied execution receipt for this new calculation. An implementation agreement would corroborate this new precision layer at these three auxiliary inputs only. It would not establish an original-index constant.

---

# 14. Complete forcing and normalization remain separate

Nothing in the square-carry reduction changes the complete second-force obligation:


$$
\boxed{
p^3U_a^TQ
=
p^3(r_0G^{(3)}_{a0}+r_1G^{(3)}_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda'_{a,\ell}
+W_bU_{a,b}.
}
\tag{14.1}
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


There is no source row at $b-1$; the exterior at $b$ is not a recurrence step. Division by $p^3$ in (14.1) belongs to its whole right-hand side.

The target and guard remain


$$
x^TQ-p^c\rho_nx^Tx
\equiv0\pmod{p^{c+\nu+1}},
\qquad
N_{\log}\ge c+4+\nu.
\tag{14.2}
$$



True content $c$, primitive norm loss $\nu$, and the present unprimitive carry are not interchangeable. A nonzero original $\kappa$, with the retained unit $A_0$, would force the corresponding $c=1,\nu=1,d=7$ conclusion. The auxiliary nonzero values do not do so.

No row content, row metric, or least actual two-column clearer is changed. Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B},
$$


with the all-prime denominator


$$
\boxed{
\log q_n=
\sum_{\ell}
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{14.3}
$$


The primitive multiplier remains $d_B^2/g_B$.

For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the relevant evaluated error remains the whole same-index expression


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{14.4}
$$



---

# 15. Proof-status ledger

| Statement | Status |
|---|---|
| Turn 7 second-return charges and correction-contraction zeros | Reused at stated precision |
| New $696$-case potential and offset receipt | Accepted finite corroboration |
| Full original-column integrality/unbounded-content audit | Still separate |
| Compatible two-unit-digit factorial expansion for the single atom | **Derived explicitly** |
| Digit-four cross-digit correction | **Evaluated and retained before elimination** |
| Digit-five $C,q$ coefficients | **Evaluated: $(1,19)$, $(8,10)$** |
| Whole sum of interface constants | **Evaluated: $29\cdot22\bmod841$** |
| Common interface lift | **Eliminated by a proved contraction zero** |
| Norm-effective interface formula (6.4) | **Proved** |
| Weighted high symmetry with exact cutoff | **Proved** |
| Safe cubic telescoping reduction | **Proved with zero-flux endpoints** |
| Three-observable carry formula (8.5) | **Proved** |
| Auxiliary values $C=0,1,2$ | **Analytically evaluated: $26,9,10$** |
| Independent sparse implementation of those values | Not executed here |
| Fixed-prefix law on all phase-compatible $C$ | **Disproved** |
| Nonzero carry at a genuine original index | Not established |
| Complete original carry evaluation | Open |
| Primitive norm-loss control and complete second-force alignment | Open |
| All-prime denominator versus whole same-index error | Open |

---

## Conclusion

The new local result is the fully evaluated low-interface reduction


$$
\boxed{
\kappa
=
21D(C)+16S_2(C)
+(25+18C+19C^2+24C^3)S_0(C)
\pmod{29},
}
$$


with the original finite range $0\le q\le C$, the whole divided difference $D$, and all two-unit-digit harmonic and ordinary carry terms accounted for.

The auxiliary evaluations


$$
\boxed{26,\ 9,\ 10\quad\text{at }C=0,1,2}
$$


and the forced-block zeros prove that a fixed-prefix law on the entire phase-compatible family is impossible. They do not establish a nonzero value on the original power orbit.

The exact remaining local bottleneck is an original-compatible evaluation or annihilation of the three high observables in the displayed combination—especially the whole next-digit difference $D(C)$. The proposed sparse auxiliary calculation is a new, bounded implementation test with expected outputs $754,261,290\bmod841$; it is not an original-orbit evaluation.

The complete second-force relative alignment and all-prime primitive-denominator comparison remain unresolved. Therefore


$$
\boxed{
\text{An unconditional proof or disproof of the irrationality of }e+\pi
\text{ remains unresolved.}
}
$$


