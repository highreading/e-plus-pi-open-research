> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 7 — Explicit second-return charges, vanishing correction contractions, and a strengthened unbounded-content theorem

## Executive assessment

The arithmetic correction is accepted:


$$
K_{34}=12,\qquad
L_{\mathrm I}^{(3)}=21,\qquad
L_{\mathrm{II}}^{(3)}=8=-21\pmod{29}.
$$


Accordingly, every occurrence of $11(\mathscr T_{\mathrm I}-\mathscr T_{\mathrm{II}})$ in the dependent leading-norm formulas must be replaced by


$$
21(\mathscr T_{\mathrm I}-\mathscr T_{\mathrm{II}}).
$$


The exact high-sum symmetry, the bound $d\ge7$, and the short-head radical survive. Their vanishing mechanism uses $10+19=0$, not the erroneous value of $K_{34}$.

I obtain the following new results.

1. **The second endpoint charges that can affect the requested norm are evaluated.**  
   With the exterior coordinates numbered $b+r$, the second-order return satisfies
   

$$
\boxed{
   z_{2,r}=13(-1)^rF_{r-2}\pmod{29},
   \qquad 2\le r\le28,
   }
$$


   and $z_{2,r}=0$ for $r\ge29$. In particular,
   

$$
\boxed{z_{2,2}=13,\qquad z_{2,3}=0,\qquad z_{2,4}=13.}
$$


   The second-order charges at $r=0,1$ do not enter the output modulo $29^5$.

2. **The complete second-return contraction is evaluated: it is zero.**  
   Its only potentially contributing rows on the support of the leading column have $j_1=0$. Their combined multiplier is explicitly
   

$$
\boxed{\frac{21}{6-j_2}},
$$


   independent of the remaining low digits and of the high word. The enlarged low-multiplier radical then gives a symbolic zero.

3. **The compatible $\mathsf D_2$ contribution and the crossed $\mathsf D_1z_1$ contribution vanish at the required output precision.**  
   These terms are retained first and eliminated by additional coefficient-weighted divisibility arguments. The support through $58$ of $\mathsf D_2$ is essential to the argument.

4. **The remaining first-lower and first-return norm contractions also vanish.**  
   Consequently the complete short-input norm reduces to the carry of the single leading weighted atom:
   

$$
\boxed{
   \eta_{\mathrm{short}}
   =
   \frac1{29^7}
   \sum_{j=0}^{b-1}
   \binom{n+2}{j}^{\!2}
   \binom{2n+b-1-j}{b-1-j}^{\!2}
   \pmod{29}.
   }
   \tag{E.1}
$$


   The division here is of the **whole finite sum**. The numerator is known to be divisible by $29^7$, but its residue after that division is **not evaluated in this report**.

5. **The repeated-block argument is strengthened to an explicit transition/potential certificate.**  
   It handles every incoming borrow and addition carry, both bounded offsets, and a possible incoming $-1,0,1$ without assuming that an offset disappears in a long zero prefix. The endpoint integrality argument is also made explicit.

Thus this report closes the second-return and correction-contraction parts of the assignment, but **does not finish the whole $\eta_{\mathrm{short}}$ evaluation**. The exact outstanding local bottleneck is now the carry in (E.1), not an unknown next head, $\mathsf D_2$, or second endpoint charge.

---

## 1. Retained finite problem and accepted arithmetic

Throughout,


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad n=2001b,\qquad u\ge0.
$$


The domains remain


$$
0\le j<b,\qquad 1\le i\le b-2,\qquad 0\le j\le b
$$


for contact coordinates, source rows, and reconstructed coordinates.

The corrected columns remain


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,
\qquad W_j=\binom{n+2}{j}.
$$


Also retain


$$
P=\frac{Z_w}{p^2}=p^cx,\qquad Q=\frac{Y}{p^3},
\qquad
\nu=v_p(x^Tx),\qquad d=2c+4+\nu.
$$



The supplied new receipt checks the $120$ second-lower symbols and $120$ literal-lift conversions against the exact recurrence. I reuse those results at that finite scope. The proof of support beyond the checked range remains the factorial/Frobenius argument in Turn 6; a check through $120$ is not, by itself, a proof for all indices.

No accepted producer, symbol audit, low-product audit, or binary contraction needs repeating.

The corrected leading norm is


$$
\left(\frac{Z_w}{p^3}\right)^T
\left(\frac{Z_w}{p^3}\right)
\equiv
21A_0^2(\mathscr T_{\mathrm I}-\mathscr T_{\mathrm{II}})
=0\pmod p.
\tag{1.1}
$$


Here the high sums retain exactly their original ranges $0\le q\le C$.

The eleven proved obstructions are also retained:


$$
\boxed{
C\equiv2+29\gamma\pmod{841},\qquad18\le\gamma\le28
\ \Longrightarrow\ c\ge2,\ d\ge8.
}
\tag{1.2}
$$


These are sufficient conditions, not an exact content classification.

---

# Part I. A larger evaluated radical

## 2. The leading column and a three-digit multiplier radical

Put


$$
K_j=b-1-j,\qquad
P_j=\binom{2n+K_j}{K_j},
$$


and define the integral column


$$
V_j=(-1)^{j+1}\frac{W_jP_j}{p^3}\quad(j<b),
\qquad V_b=0.
$$


Let


$$
S=V\bmod p.
$$



The established support of $S$, writing


$$
j=(d,e,f,t,k,\ell)_{29}+p^6q,
$$


is


$$
\begin{aligned}
&d\in\{0,1,2\},\\
&e\in\{0,\ldots,7\}\cup\{14,\ldots,28\},\\
&f\in\{0,\ldots,5\},\\
&t\in\{0,\ldots,7\}\cup\{15,\ldots,28\},\\
&k=0,\qquad 0\le\ell\le20.
\end{aligned}
\tag{2.1}
$$



### Lemma 2.1 — Three-digit multiplier radical

For every function


$$
H:\{(d,e,f)\text{ allowed in (2.1)}\}\longrightarrow\mathbb F_{29},
$$


one has


$$
\boxed{\sum_{j=0}^{b-1}S_j^2H(j_0,j_1,j_2)=0\pmod p.}
\tag{2.2}
$$



### Proof

Inserting $H$ changes only the contraction over digits $0,1,2$. The factor over digits $3,4$ remains $K_{34}=12$, and the digit-five factors remain $10,19$. Thus the contraction has the form


$$
K_H\cdot12\,
\bigl(10\mathscr T_{\mathrm I}+19\mathscr T_{\mathrm{II}}\bigr).
$$


The exact finite-range identity


$$
\mathscr T_{\mathrm I}=\mathscr T_{\mathrm{II}}\pmod p
$$


and $10+19=0\pmod p$ prove the result. ∎

This explains the precise dependency of Turn 6’s radical on the corrected arithmetic. Replacing $27$ by $12$ in $K_{34}$ changes the common scalar but cannot change the zero.

---

# Part II. Retaining and eliminating the second lower terms

## 3. Expansion of the complete finite inverse

Use the accepted precision-$p^5$ bounds


$$
M=144,\qquad L=292.
$$


Let


$$
w=\mathsf P_-h^{[0]},\qquad
h_i^{[0]}=
\begin{cases}
i!\bmod p,&0\le i<29,\\
0,&i\ge29,
\end{cases}
$$


with fixed integral representatives.

Take the compatible expansion


$$
\mathsf D=I+p\mathsf D_1+p^2\mathsf D_2\pmod{p^3},
\qquad
z=pz_1+p^2z_2\pmod{p^3}.
$$


Then, before any elimination,


$$
\begin{aligned}
\mathcal RA^{-1}h^{[0]}
\equiv{}&
\mathcal R\mathsf R_{2n}w\\
&+p\,\mathcal R\mathsf R_n\mathsf D_1\mathsf R_nw
+p\,\mathcal R\mathsf R_{2n}z_1\\
&+p^2\,\mathcal R\mathsf R_n\mathsf D_2\mathsf R_nw\\
&+p^2\,\mathcal R\mathsf R_n\mathsf D_1\mathsf R_nz_1
+p^2\,\mathcal R\mathsf R_{2n}z_2
\pmod{p^5}.
\end{aligned}
\tag{3.1}
$$


Terms of coefficient order at least three are discarded only after applying the accepted weighted $p^2$ safeguard.

The crossed term on the penultimate line of (3.1) must not be omitted from this expansion.

---

## 4. A third factor for all second-lower symbols

### Lemma 4.1

For the short head $h^{[0]}$ and every $0\le s\le58$,


$$
\boxed{
\mathcal R\mathsf R_n\mathsf D_s\mathsf R_nw
\in p^3\mathbb Z_p^{\,b+1}.
}
\tag{4.1}
$$



### Proof

The normal-ordered terms contain


$$
\binom{-n}{t}
\binom{2n+t+r-1}{r},
\qquad 0\le t\le s,\quad0\le r<29.
$$


Modulo $p$, the first factor vanishes unless $t$ is a multiple of $29$. In the surviving cases, the second factor vanishes unless $r=0$.

Every term eliminated in this way already has a coefficient factor $p$, in addition to the weighted $p^2$ safeguard.

It remains to treat


$$
t\in\{0,29,58\},\qquad r=0.
$$


Write $a=s-t$. The unshifted reconstructed atom has row factor $\binom ja$ and lower index


$$
b-1-j+a.
$$


The shifted atom has row factor


$$
j\binom{j-1}{a}
$$


and lower index $b-j+a$.

If either of the first two weight digits borrows, the required additional event is already present. Otherwise


$$
J:=j\bmod p^2\le205.
$$


A nonzero unshifted row factor modulo $p$ implies $a\le J$. The low two-digit lower index is therefore


$$
838+a-J\in[633,838].
$$


The upper addend is $406+t$, so their sum exceeds $841$.

For a nonzero shifted row factor, $j_0\ne0$ and $a\le J-1$. Its low lower index is


$$
839+a-J\in[634,838],
$$


and again an addition carry is forced.

Digits $3,4,5$ provide the other two events. The terminal row has the stronger weight divisibility and is harmless. ∎

Since the complete compatible $\mathsf D_2\bmod p$ has support through $58$,


$$
\boxed{
p^2\mathcal R\mathsf R_n\mathsf D_2\mathsf R_nw
\equiv0\pmod{p^5}.
}
\tag{4.2}
$$



This is an elimination of the **complete compatible** second lower correction, not an assumption that its coefficients above $29$ vanish.

---

## 5. The lower correction applied to the first return

The first return is supported at $b,b+1$:


$$
z_1=z_{1,0}e_b+z_{1,1}e_{b+1}.
$$



### Lemma 5.1

For $r=0,1$,


$$
\boxed{
\mathcal R\mathsf R_n\mathsf D_1\mathsf R_ne_{b+r}
\in p^3\mathbb Z_p^{\,b+1}.
}
\tag{5.1}
$$



### Proof

As before, normal-order terms with $t\notin\{0,29\}$ have a coefficient factor $p$.

For $t=0$, a nonzero unshifted row factor gives $s\le J$, and the low lower index is


$$
839+r+s-J\le840.
$$


It is large enough to force an addition carry whenever the two low weight digits do not borrow.

For the shifted term, the row factor gives $s\le J-1$, and the same upper bound $840$ follows.

For $s=t=29$, the upper addend is $2n+28$. Offsets $0,1$ force the extra low event directly. The shifted offset $2$ can lose that event only at $j_0=0$, where the reconstruction factor $j$ supplies $p$.

Digits $3,4,5$ supply two further events in all cases. ∎

Consequently,


$$
\boxed{
p^2\mathcal R\mathsf R_n\mathsf D_1\mathsf R_nz_1
\equiv0\pmod{p^5}.
}
\tag{5.2}
$$



---

# Part III. Solving the second endpoint return at the required precision

## 6. Crossed lower coefficients

Let $H=\mathsf D^{-1}$ be the lower matrix in the established full inverse. Its coefficient expansion is


$$
H=I-p\mathsf D_1
+p^2(\mathsf D_1^2-\mathsf D_2)\pmod{p^3}.
\tag{6.1}
$$


The crossed block $K_\times$ has entries


$$
(K_\times)_{r,k}
=
h_{b+r-k}(n)\binom{b+r}{b+r-k},
\qquad k<b.
\tag{6.2}
$$


The second-order symbol in (6.1) has support through $58$.

The endpoint equation remains


$$
(I+K_\times\mathsf DF)q
=
K_\times\mathsf D\mathsf R_nw,
\qquad
z=T_{\rm out}q.
\tag{6.3}
$$



For exterior rows $r\ge2$, the first-order crossed block is zero modulo $p^2$. Thus the second charge in these rows is obtained directly from the second-order crossed block acting on


$$
y_0=\mathsf R_nw\bmod p.
$$


Feedback involving $q$ cannot affect those rows at this order.

---

## 7. Which crossed coefficients survive?

For $2\le r\le28$,


$$
b+r\equiv r-2\pmod{p^2}.
\tag{7.1}
$$


If $r<s<29$, subtracting $s$ from $b+r$ borrows in both digits zero and one. Hence


$$
\binom{b+r}{s}\in p^2\mathbb Z_p.
\tag{7.2}
$$


These entries, multiplied by a first-order lower coefficient, are zero modulo $p^3$.

For $s=29$,


$$
\boxed{
\frac1p\binom{b+r}{29}\equiv6\pmod p,
\qquad2\le r\le28.
}
\tag{7.3}
$$


Indeed,


$$
b+r=p^2A+(r-2),\qquad A\equiv6\pmod p.
$$


Vandermonde’s identity shows that all terms except $\binom{p^2A}{p}$ vanish modulo $p^2$, and


$$
\binom{p^2A}{p}\equiv pA\pmod{p^2}.
$$



The second-order lower coefficients with $s\le58$ contribute nothing in these rows modulo $p^3$, because


$$
\binom{b+r}{s}\equiv0\pmod p\qquad(s>r).
\tag{7.4}
$$


The same Lucas check gives no second-order charge for $29\le r\le57$. Beyond $57$, the second-order crossed bandwidth is exhausted.

Since the first coefficient at $s=29$ is


$$
-pk_{29}=7p,
$$


equations (7.2)–(7.4) give


$$
q_{2,r}=13\,y_{0,b+r-29}\pmod p,
\qquad2\le r\le28.
\tag{7.5}
$$



---

## 8. Evaluation of the contact values and charges

Let


$$
F_0=1,\qquad F_d=1-dF_{d-1}.
$$


The finite short-head identity, at distance at most $26$ from the endpoint, gives


$$
y_{0,b+r-29}=(-1)^rF_{r-2}\pmod p.
\tag{8.1}
$$


Therefore


$$
\boxed{
q_{2,r}=13(-1)^rF_{r-2},
\qquad2\le r\le28.
}
\tag{8.2}
$$



On this range, the off-diagonal entries of $T_{\rm out}$ are zero modulo $p$, so the same formula holds for $z_2$:


$$
\boxed{
z_{2,r}=13(-1)^rF_{r-2},
\quad2\le r\le28;
\qquad z_{2,r}=0\quad(r\ge29).
}
\tag{8.3}
$$


In particular,


$$
z_{2,2}=13,\qquad z_{2,3}=0,\qquad z_{2,4}=13.
\tag{8.4}
$$



The second charges $z_{2,0},z_{2,1}$ are not needed: their reconstructed atoms already carry $p^3$, and their coefficient $p^2$ makes them zero modulo $p^5$. This is a precision-based elimination, not an assertion that those charges themselves are zero.

---

## 9. Explicit contraction of the second return

Write


$$
E_r=\mathcal R\mathsf R_{2n}e_{b+r}.
$$


We need


$$
G=\sum_r z_{2,r}\frac{E_r}{p^2}\pmod p.
$$



On the support of $S$, a term $E_r/p^2$ can contribute only when $e=j_1=0$:

- its unshifted part requires $r=d+2$;
- its shifted part requires $r=d+1$.

All other cases have an additional low weight borrow, addition carry, or reconstruction factor.

A direct ratio against $P_j$ gives, in these exceptional cases,


$$
\frac{G_j}{S_j}
=
\frac{14}{6-f}
\left(
(-1)^{d+1}z_{2,d+2}
+(-1)^d d\,z_{2,d+1}
\right).
\tag{9.1}
$$


The denominator is a unit because $0\le f\le5$.

Substituting (8.4), the expression in parentheses is $-13$ for each $d=0,1,2$. Hence


$$
\boxed{
G_j
=
S_j\,\frac{21}{6-f}\,\mathbf1_{e=0}
\pmod p.
}
\tag{9.2}
$$



Lemma 2.1 now evaluates the complete contraction:


$$
\boxed{
S^TG
=
\sum_jS_j^2\frac{21}{6-j_2}\mathbf1_{j_1=0}
=0\pmod p.
}
\tag{9.3}
$$



Thus the complete second endpoint return contributes zero to $\eta_{\mathrm{short}}$. This is a symbolic zero for every compatible high continuation.

---

# Part IV. The remaining correction contractions

## 10. The first endpoint return vanishes pointwise on the leading support

For $r=0,1$, compare the positive-binomial part of $E_r$ with $P_j$. Its ratio contains


$$
2n\,
\frac{(2n+b-j)^{\overline r}}
     {(b-j)^{\overline{r+1}}}.
\tag{10.1}
$$



For $r=0$, all reconstruction denominators are units on $d=0,1,2$.

For $r=1$, the shifted term may contain $b+2-j$. If $d=0$, the support conditions give


$$
v_p(b+2-j)\le v_p(j):
$$


when $e\ne0$, both relevant valuations are one; when $e=0$, the denominator has valuation two because its next unit is $6-f$, while $j$ has valuation at least two.

Thus the reconstruction factor $j$ pays for this possible denominator. The remaining $2n$ supplies a factor $p$. Therefore


$$
\boxed{
\left(\frac{E_r}{p^3}\right)_j=0\pmod p
\quad\text{whenever }S_j\ne0,\qquad r=0,1.
}
\tag{10.2}
$$


It follows that the first endpoint contribution to the divided norm is zero, independently of the values of the two first charges.

---

## 11. The first-lower contraction is a low-multiplier contraction

Set


$$
L_1=\mathcal R\mathsf R_n\mathsf D_1\mathsf R_nw.
$$


Its coefficient-weighted terms are individually divisible by $p^3$, as proved in Turns 5–6.

For completeness, the additional fact needed here is that, on the support of $S$,


$$
\boxed{
\frac{L_{1,j}}{p^3}=S_j\,H_1(d,e,f)\pmod p
}
\tag{11.1}
$$


for a function of the first three digits only.

This does not require evaluating $H_1$. It follows from the exact rational ratios of each normal-ordered atom against $P_j$. For a term indexed by $s,t,r$, put $a=s-t$ and let $\varepsilon=0,1$ distinguish the two reconstruction rows. The positive-binomial ratio is


$$
\frac{(N_j+1)^{\overline{s+\varepsilon}}}
     {(2n+1)^{\overline{t+r}}}
\frac{K_j!}{(K_j+a-r+\varepsilon)!},
\qquad N_j=2n+K_j,
\tag{11.2}
$$


multiplied by the retained integral row and head factors.

Here $s\le29$, $r<29$. On the support of $S$:

- a denominator near $b-j$ has valuation at most two, with its possible second unit $6-f$;
- the only possible multiple of $p$ in $(2n+1)^{\overline{t+r}}$ is $2n+29$, of valuation one;
- these two losses cannot occur together: $t+r\ge29$ forces $a-r+\varepsilon\le1$, where the denominator near $b-j$ is a unit;
- the exceptional factorial denominator at $a=29,t=0$ is paid for by the displayed row factor. When $e=0$, that row factor contains a factor of valuation at least two, while the numerator in (11.2) contains a factor with first unit $14$.

After these explicit cancellations, the reduction depends only on $b,n,j\bmod p^3$. The fixed phases of $b,n$ therefore leave only $d,e,f$. This proves (11.1).

Applying Lemma 2.1,


$$
\boxed{
S^T\frac{L_1}{p^3}=0\pmod p.
}
\tag{11.3}
$$



---

## 12. The baseline short-head correction also lies in the radical

Let


$$
U=p^{-3}\mathcal R\mathsf R_{2n}w.
$$


The finite-head identity and


$$
\binom{2n+r-1}{r}
\binom{2n+K_j}{K_j-r}
=
P_j\,\frac{2n}{2n+r}\binom{K_j}{r}
$$


show that, on the support of $S$,


$$
U_j=V_j\bigl(1+pH_0(d,e)\bigr)\pmod{p^2}.
\tag{12.1}
$$


All denominators $2n+r$, $1\le r<29$, are units; the adjacent reconstruction denominator $b-j$ is also a unit there.

Off the support of $S$, both $U_j$ and $V_j$ are divisible by $p$, so their squares vanish modulo $p^2$. On the support, Lemma 2.1 gives


$$
U^TU-V^TV
\equiv2p\sum_jS_j^2H_0(d,e)
=0\pmod{p^2}.
\tag{12.2}
$$



Combining Sections 3–12 proves the reduction (E.1).

---

## 13. What has—and has not—been evaluated

The following contributions to the complete first divided norm are now evaluated:


$$
\begin{array}{c|c}
\text{Contribution}&\text{Value}\\ \hline
\text{Actual next head}&0\quad\text{by the retained short-head radical}\\
\mathsf D_2&0\quad\text{already at output precision }p^5\\
\mathsf D_1z_1&0\quad\text{already at output precision }p^5\\
\mathsf D_1w\text{ contraction}&0\\
z_1\text{ contraction}&0\\
z_2\text{ contraction}&0\\
\text{Baseline short-head multiplier correction}&0
\end{array}
$$



The remaining quantity is


$$
\kappa(b,n):=
\frac1{p^7}
\sum_{j=0}^{b-1}
\binom{n+2}{j}^{2}
\binom{2n+b-1-j}{b-1-j}^{2}
\pmod p.
\tag{13.1}
$$


Thus


$$
\boxed{\eta=A_0^2\eta_{\mathrm{short}}
=A_0^2\kappa(b,n).}
\tag{13.2}
$$



Equation (13.1) is an **exact reduction**, not an evaluation of $\kappa$. In particular, the modulo-$p$ identity between the two high sums does not determine the carry obtained after dividing their whole lifted combination by $p$.

The physical terminal coordinate remains


$$
\boxed{
\frac{Z_{w,b}}{p^3}
\equiv14pA_0\frac{W_b}{p^4}\pmod{p^2}.
}
\tag{13.3}
$$


It has not been deleted from the column. Its square is zero modulo $p^2$, which is why it does not occur in (13.1).

---

# Part V. A finite transition/potential certificate for repeated blocks

## 14. Exact transition rules

For one digit, let

- $w\in\{0,1\}$ be the incoming weight borrow;
- $k\in\{0,1\}$ the incoming lower-index borrow;
- $c\in\{0,1\}$ the incoming addition carry;
- $x\in\{0,\ldots,28\}$ the digit of $j$.

For fixed digits $W,B,A$, define


$$
w'=\mathbf1_{x+w>W},
\qquad
k'=\mathbf1_{x+k>B},
$$




$$
K=B-x-k+29k',
\qquad
c'=\mathbf1_{A+K+c\ge29}.
\tag{14.1}
$$


The valuation cost is


$$
C=w'+c'.
$$



The three forcing positions have


$$
(W,B,A)=(7,28,15),\quad(3,0,6),\quad(9,20,18).
\tag{14.2}
$$



Define the potential


$$
\Phi(k)=1-k.
$$



The following inequalities hold for **every** incoming $(w,k,c)$ and every $x$:



$$
\begin{array}{c|c}
\text{Position}&\text{Certified inequality}\\ \hline
3&C_3\ge1\\
4&C_4+\Phi(k_4')\ge1\\
5&C_5-\Phi(k_5)\ge0
\end{array}
\tag{14.3}
$$


Since $k_5=k_4'$, summation gives


$$
\boxed{C_3+C_4+C_5\ge2.}
\tag{14.4}
$$



### Verification of all incoming states

At position $3$, if $w'=0$, then $x\le7-w$, and


$$
K\ge28-(7-w)-k\ge20.
$$


Hence $15+K+c\ge35$, so $c'=1$.

At position $4$, if $C_4=0$, then $x\le3-w$. If $k'=1$, the lower digit is at least $25$, and adding $6+c$ forces a carry. Thus $C_4=0$ implies $k'=0$, giving $\Phi(k')=1$.

At position $5$, only $k=0$ requires proof. If $w'=0$, then $x\le9-w$, so


$$
K=20-x\ge11,
$$


and $18+K+c\ge29$. Hence $C_5\ge1=\Phi(0)$. For $k=1$, the inequality is simply $C_5\ge0$.

These arguments cover all eight incoming triples, including states that might not be reachable from a particular lower prefix. An additional cutoff-borrow bit does not affect these inequalities.

---

## 15. Both bounded offsets and a long zero prefix

Let


$$
\Lambda=29^6,\qquad \beta=410910916,
$$


and prescribe a $\beta$-block above a lower prefix of length $m$.

For the lower minuend $b+v$, choose $29^m>|v|$. Its incoming offset at the first prescribed block is exactly


$$
\delta_B=
\left\lfloor\frac{b_{\rm low}+v}{29^m}\right\rfloor
\in\{-1,0,1\}.
\tag{15.1}
$$


This formula remains correct if the offset propagated through an arbitrarily long string of zeros.

At the $\beta$-block,


$$
0<\beta+\delta_B<\Lambda,
$$


so the outgoing offset is zero. Also


$$
\beta\bmod29^3=5044,
$$


and adding any of $-1,0,1$ does not change digits $3,4,5$.

For $n+2$, the incoming multiplication carry is bounded, and


$$
2001\beta=1382\Lambda+186913294.
$$


The last three-digit remainder is $20387$. Even allowing the slightly enlarged interval


$$
-1\le\mu_W\le2001,
$$


one has


$$
0<20387+\mu_W<29^3.
$$


Thus digits $3,4,5$ remain $(7,3,9)$, and the outgoing multiplication carry is exactly $1382$.

Similarly,


$$
4002\beta=2764\Lambda+373826588,
$$


whose last three-digit remainder is $16385$. For


$$
-1\le\mu_A\le4002,
$$




$$
0<16385+\mu_A<29^3.
$$


Therefore digits $3,4,5$ of $2n+a-1$ remain $(15,6,18)$, and the outgoing multiplication carry is $2764$.

This accounts explicitly for:

- the bounded offset $v$ in $b+v$;
- the bounded offset $a-1$ in $2n+a-1$;
- every incoming subtraction borrow and addition carry;
- any incoming $-1,0,1$ caused by propagation below the block.

Hence each prescribed block contributes at least two events to every supported atom


$$
W_j\binom{-2n-a}{b+v-j}.
\tag{15.2}
$$



---

# Part VI. Integral full endpoint charges and unbounded actual content

## 16. Endpoint integrality at arbitrary finite precision

Fix precision $p^K$, and use the established truncations


$$
M=29K-1,\qquad L=58K+2.
$$



The relevant matrices $\mathsf D,F,\mathsf R_n,T_{\rm out}$ have integral entries. The crossed block satisfies


$$
K_\times\in pM(\mathbb Z_p).
$$


Therefore


$$
E:=I+K_\times\mathsf DF
$$


is invertible over $\mathbb Z_p$.

More explicitly, with $G=K_\times\mathsf DF$,


$$
\boxed{
q\equiv
\sum_{\ell=0}^{K-1}(-G)^\ell
K_\times\mathsf D\mathsf R_nw
\pmod{p^K}.
}
\tag{16.1}
$$


This is a finite integral certificate for the precision-$K$ endpoint solution. Multiplication by $I+G$ leaves a residual divisible by $p^K$. In particular,


$$
q\in p\mathbb Z_p^M,\qquad z=T_{\rm out}q\in p\mathbb Z_p^M.
$$



The bandwidth truncation is compatible with the exterior support: the crossed lower block has exterior rows $0,\ldots,M-1$, and the upper-triangular exterior map does not enlarge that support.

After the accepted finite normal ordering and reconstruction, the atoms have precisely the retained bounds


$$
a\le M+L=87K+1,\qquad -L\le v\le M
$$


for head terms, and


$$
0\le a\le M,\qquad0\le v\le2M
$$


for exterior terms. All coefficients, including the solved charges (16.1), are integral.

Thus there is no hidden division in passing from atom valuations to the complete column.

---

## 17. Strengthened unbounded-content theorem

Choose $m$ so that


$$
29^m>87K+2,
$$


and prescribe $r$ consecutive $\beta$-blocks above the retained lower prefix.

Sections 14–15 give at least $2r$ valuation events for every atom in the complete precision-$K$ normal form. If $2r\ge K$, all interior reconstructed coordinates vanish modulo $p^K$.

At the physical terminal coordinate, each block forces weight borrows at its positions $3$ and $5$, since


$$
28>7,\qquad20>9.
$$


The integral terminal contact value therefore gives the same conclusion at $j=b$.

Consequently,


$$
Z_w\in p^K\mathbb Z_p^{\,b+1},
\qquad c\ge K-2.
\tag{17.1}
$$



Reusing the established principal-unit bijection and CRT argument, the prescribed finite prefix can be realized inside every original progression $u\equiv u_0\pmod h$, while preserving its necessary lower digits.

### Theorem 17.1

For every $u_0\ge0$, $h\ge1$, and $R\ge0$, infinitely many original indices satisfy


$$
\boxed{u\equiv u_0\pmod h,\qquad c\ge R.}
\tag{17.2}
$$



The strengthened proof includes the complete finite return and terminal reconstruction. It does not imply unbounded primitive norm loss $\nu$.

The conditional rigidity statement remains valid: if $\eta$ depended only on a fixed original residue class, it would have to vanish identically. That observation still does not evaluate (13.1).

---

# Part VII. Complete forcing and the global objective

## 18. The second-force obligation remains unchanged

Retain


$$
p^3U_a^TQ
=
p^3(r_0G^{(3)}_{a0}+r_1G^{(3)}_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda'_{a,\ell}
+W_bU_{a,b}.
\tag{18.1}
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


There is no source row at $b-1$. The exterior at $b$ is not a recurrence step.

The division by $p^3$ in (18.1) belongs to its whole right-hand side. The still-open target is


$$
\boxed{
x^TQ-p^c\rho_nx^Tx
\equiv0\pmod{p^{c+\nu+1}},
}
$$


with independently defined $\rho_n$ and guard


$$
N_{\log}\ge c+4+\nu.
$$



---

## 19. All-prime normalization and the whole same-index error

No row content, row metric, or least actual two-column clearer has been changed.

Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad p_n=\frac{H_B}{g_B}.
$$


The primitive multiplier remains $d_B^2/g_B$, and


$$
\boxed{
\log q_n
=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{19.1}
$$



For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the relevant evaluated expression remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n}
\tag{19.2}
$$


at the same original index.

Neither the selected-prime content theorem nor the correction-contraction zeros control (19.1). The full same-index denominator/error comparison remains open.

---

# Part VIII. Exact remaining calculation and proof status

## 20. The outstanding bounded coefficient calculation is now smaller

The remaining local task is **only the next digit of the whole leading-atom norm**:


$$
\sum_{j=0}^{b-1}
\binom{n+2}{j}^{2}
\binom{2n+b-1-j}{b-1-j}^{2}
\pmod{p^8}.
\tag{20.1}
$$



The low extraction must preserve the original finite cutoff. Since each divided atom is integral, coordinates vanishing modulo $p$ contribute zero to its squared norm modulo $p^2$. Thus only the established leading support (2.1) is needed for this carry calculation. This is a reduction in the required contraction, not permission to complete the last block.

### Inputs

- $p=29$;
- the fixed six-digit phase of $b,n$;
- the supported residues (2.1);
- prime-power factorial units through the next digit;
- the original high integer $C$, symbolically retained;
- the exact cutoff $0\le q\le C$;
- the corrected low coefficients $21,8$, not $11,18$.

No head coefficients, lower symbols, or endpoint charges remain as unresolved inputs to this norm calculation.

### Required verifiable output

The calculation must supply:

1. the next low-unit coefficients for the **whole squared atom**, including their carries;
2. an explicit contraction against the genuine high observables;
3. the carry resulting from the leading modulo-$p$ cancellation;
4. either a symbolic zero for every compatible high continuation, or explicit surviving high observables with evaluated low coefficients.

A formula that simply renames (20.1) as an observable does not meet that final evaluation requirement. Nor would a finite set of auxiliary high-word values establish an all-continuation identity.

---

## 21. Proof-status ledger

| Statement | Status |
|---|---|
| Corrected $K_{34}=12$, low pair $21,8$ | Accepted exact finite arithmetic and audited derivation |
| Exact high-sum symmetry and $d\ge7$ | Reused closed results |
| Eleven obstructed $C$-classes | Reused proved sufficient conditions |
| Actual next head removed from this norm | Reused radical result |
| Three-digit multiplier radical | **Proved here** |
| Complete $\mathsf D_2$ contribution at output precision $p^5$ | **Proved zero** |
| Crossed $\mathsf D_1z_1$ contribution | **Proved zero** |
| Required second endpoint charges $z_{2,r}$, $r\ge2$ | **Explicitly solved** |
| Complete second-return contraction | **Explicitly evaluated: zero** |
| First-return contraction | **Proved zero pointwise on leading support** |
| First-lower contraction | **Proved zero by the enlarged radical** |
| Reduction of $\eta_{\mathrm{short}}$ to the whole leading-atom carry | **Proved** |
| Value of that carry | **Not evaluated** |
| Repeated-block transition/potential certificate | **Explicitly proved for all incoming states** |
| Offset propagation, including incoming $-1,0,1$ | **Accounted for explicitly** |
| Integral precision-dependent endpoint solution | **Proved by a finite Neumann certificate** |
| Actual content unbounded on every original progression | **Proved using the strengthened certificates** |
| Primitive norm loss $\nu$ | Open |
| Full second-force relative alignment | Open |
| All-prime denominator versus whole same-index error | Open |

---

## Conclusion

The new evaluated endpoint result is


$$
\boxed{
z_{2,r}=13(-1)^rF_{r-2}\quad(2\le r\le28),
}
$$


and its complete norm contribution is the symbolic zero


$$
\boxed{
\sum_jS_j^2\frac{21}{6-j_2}\mathbf1_{j_1=0}=0.
}
$$



Together with the retained actual-head radical and the newly proved lower/crossed-return eliminations, this reduces the entire requested short-input norm to


$$
\boxed{
\eta_{\mathrm{short}}
=
\frac1{29^7}
\sum_{j=0}^{b-1}
\binom{n+2}{j}^{2}
\binom{2n+b-1-j}{b-1-j}^{2}
\pmod{29}.
}
$$



That whole leading-square carry is the exact remaining local bottleneck. It has not been evaluated here, so the assignment’s final $\eta_{\mathrm{short}}$ target remains open. The report does not substitute conditional finite-prefix rigidity for that calculation.

Independently, the complete-column unbounded-content theorem now has an explicit all-interface block certificate and an integral finite endpoint certificate. It remains a theorem about $c$, not about $\nu$.

The complete second-force alignment and all-prime primitive-denominator comparison are still unresolved. Therefore


$$
\boxed{
\text{An unconditional proof or disproof of the irrationality of }e+\pi
\text{ remains unresolved.}
}
$$


