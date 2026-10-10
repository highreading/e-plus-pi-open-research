> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 Turn 4 — The first whole-defect digit, a sharper leading response, and the actual tail test

## Abstract

The first digit of the whole normalized defect not covered by the retained results is the coefficient of $29^{11}$, not a digit of the mixed product alone. In this report I derive a sufficient observation for that digit, retaining the norm term, the original contact cutoff, the complete finite returns, and the physical terminal.

There are four new proved advances.

1. **The leading second column is more restricted than previously stated.** After division by $29^5$, its entire leading contact response lies in the ordinary $000$ kernel:
   

$$
\frac{Y_{\ell+29^3J}}{29^5}
   \equiv (-1)^{b-\ell-J}\beta_\ell K(J)\pmod{29}.
$$


   In particular, there are no leading $110$ or $111$ contributions at this new normalization.

2. **The first whole-defect digit reduces to three paid upper observations.** Its low coefficient row is new; it is not the previously certified zero row. A reconstruction correction that first becomes visible at this normalization changes one of the new coefficients by
   

$$
\boxed{14\pmod{29}}.
$$


   Thus simply reusing the old harmonic extraction would give an incorrect new observation.

3. **The complete feedback vector has an exact content-dependent classification.** If
   

$$
\mathcal Q=6Y/29^5-2Z_*/29^4,
$$


   then, under the retained original-family hypotheses,
   

$$
\boxed{\mathcal Q\equiv0\pmod{29}\quad\Longleftrightarrow\quad c\ge3.}
$$


   Consequently the actual normalized tail is annihilated at the displayed feedback digit whenever $c\ge3$. This is a new pointwise argument, not an application of the old fixed-layer omission guard.

4. **The physical terminal at the next flat-defect digit is evaluated.** Its contribution to $\Delta(f_*)/29^{12}$, when that quotient is being evaluated, is
   

$$
\boxed{14\,k_B^2\pmod{29}.}
$$



The whole $29^{11}$-digit is also proved to be zero at every original index with $c\ge4$. The retained unbounded-content theorem therefore supplies an infinite original subsequence on which this is an evaluated whole-defect value.

The corresponding accepting value on the entire original family, including its $c=2,3$ strata, is not yet established. A new bounded low-row calculation is specified below. If its row is nonzero, a concrete higher paid invariant of the actual upper word remains necessary. At the next digit, the actual tail on the $c=2$ stratum requires a source-specific identity that is not supplied in the packet.

None of these fixed-depth advances proves the growing-depth alignment, the all-prime denominator estimate, or the irrationality of $e+\pi$.

---

## 1. Original objects, hypotheses, and proof status

Put


$$
p=29,\qquad D=p^3=24389,
$$


and retain exactly


$$
b=3^{249005515+574312172u},\qquad n=2001b,
$$


where


$$
u\ge0,\qquad u\equiv2\pmod{p^9}.
$$



The domains remain:

- contact coordinates $0\le j<b$;
- recurrence source rows $1\le i\le b-2$;
- reconstructed coordinates $0\le j\le b$.

Let


$$
W_j=\binom{n+2}{j},\qquad
(\mathcal Rx)_j=W_j(jx_{j-1}-x_j),\qquad x_{-1}=x_b=0,
$$


and write


$$
L=\mathcal RA^{-1}.
$$


The actual columns are


$$
Z_w=Lf^0,\qquad
Y=L\mathbf r+W_be_b,
$$


with


$$
\mathbf r=A_{IE}z+\frac{h^F}{b!},\qquad
z_h=\frac{(b+h)!}{b!}.
$$



Thus the complete force includes both exponential initial charges, the factorial subtraction, every original recurrence source row, the logarithmic force formed from $F/(1-z)$, and both finite returns. The physical terminal remains separate.

The split is


$$
b=DB+5044,\qquad n+2=DW+20389,\qquad 2n-1=DA+16384,
$$


where


$$
W=2001B+413,\qquad A=2W+1.
$$


For $j=\ell+DJ<b$, the upper range is


$$
0\le J\le
\begin{cases}
B,&\ell<5044,\\
B-1,&\ell\ge5044.
\end{cases}
\tag{1.1}
$$



### 1.1 Retained results

I reuse the following at their documented scope:

- the complete-force identification and exact finite inverse/return formulas;
- the growing-depth symbol and exterior filtration theorem;
- the guarded three-event upper forcing;
- the residue-weighted interface radical;
- the lifted ordinary-square divisibility;
- the original terminal bound $v_p(W_b)\ge6$;
- the analytic branchwise second-column profile zero from A2 Turn 3;
- A4 Turn 2’s completed omission accounting;
- the independent normalization and normalized-source decomposition.

Several proofs of the original guard and radical assertions are not reproduced in the supplied packet. Accordingly, original-family conclusions using them are consequences of those expressly retained hypotheses. I do not replace them by the finite dictionary certificate.

In particular, I do not rerun the old $5075$-row audit, the unit table, or the two-coordinate exterior solve. The accepted fixed-layer zero is not in dispute.

### 1.2 Independent unit normalization

The independent definition is


$$
C_n=[z^n](1+2z+2z^2)^n=f_0^0,\qquad
\rho_n=\frac1{6C_n}.
$$


The retained unit theorem gives $C_n\in\mathbb Z_p^\times$.

Let


$$
\bar f=f^0/C_n,\qquad \bar Z=L\bar f,
\qquad f_*=\widehat f/2,\qquad Z_*=Lf_*.
$$


The exact retained decomposition is


$$
\bar f=f_*+p^2\bar v+p^7\bar w,
\qquad
\bar Z=Z_*+p^2U+p^7V,
\tag{1.2}
$$


where


$$
U=L\bar v,\qquad V=L\bar w,
$$


$\bar v$ is supported in $0,\ldots,202$, and


$$
\bar v_0=\bar w_0=0.
$$



The paid bounds are


$$
Y\in p^5,\quad Z_*\in p^4,\quad U\in p^3,\quad V\in\mathbb Z_p^{b+1},
\tag{1.3}
$$


and


$$
U^TY\in p^{10},\qquad Z_*^TU\in p^9,\qquad U^TU\in p^8.
\tag{1.4}
$$



Define the whole normalized defect


$$
\Delta(\bar f)=6\bar Z^TY-p\bar Z^T\bar Z,
\qquad
\Delta(f_*)=6Z_*^TY-pZ_*^TZ_*.
\tag{1.5}
$$


The retained theorem gives


$$
\Delta(\bar f)\equiv\Delta(f_*)\pmod{p^{12}}.
\tag{1.6}
$$


This is an equality of whole defects. It is not an evaluation of their common residue.

---

## 2. A stronger exact exterior filtration

The exterior filtration can be sharpened for the actual factorial data. This supplies the next useful exterior coefficients without a new dense solve.

Let


$$
\lambda(h)=v_p(z_h).
$$



### Theorem 2.1 — Exact factorial-weight preservation

The actual exterior solution


$$
(\mathcal C_\infty)_{EE}v=z
$$


satisfies


$$
\boxed{v_p(v_h)\ge v_p(z_h)\quad(h\ge0).}
\tag{2.1}
$$



Moreover,


$$
\boxed{
\frac{v_h}{z_h}
\equiv [z^h]\frac{\phi(z)^n}{1-z}\pmod p,
\qquad
\phi(z)=1-z+\frac{z^2}{2}.
}
\tag{2.2}
$$



All ratios in (2.2) are integral by (2.1).

### Proof

The retained factorization is


$$
\mathcal C_\infty=R_nD_-R_n,
$$


where


$$
(R_n)_{jk}=\binom{-n}{k-j},
\qquad
(D_-)_{jk}=c_{j-k}\binom jk,
\qquad
c_s=s![z^s]\phi(z)^{-n}.
$$



Scale full coordinates by $j!$. The scaled upper factor has entries


$$
\binom{-n}{r}\frac{(j+r)!}{j!},
\qquad r\ge0,
$$


which are integral. The scaled lower factor has entries


$$
\frac{c_s}{s!}=[z^s]\phi(z)^{-n}\in\mathbb Z_p.
$$


Thus each factor preserves the exact factorial lattice, and so does the exterior block.

Write the exterior block as $R_{2n}+E$, with $E\in pM(\mathbb Z_p)$. Its zeroth-order inverse $T_{2n}$ is upper triangular and also preserves the exact factorial lattice. At any fixed modulus the Neumann expansion


$$
\sum_{r\ge0}(-T_{2n}E)^rT_{2n}
$$


is finite modulo that modulus. Every term preserves the lattice, proving (2.1). This argument may be performed in the finite truncation justified by the retained growing-depth theorem, so it does not impose an artificial exterior terminal condition.

For (2.2), consider the scaled upper factor modulo $p$. If $1\le r<p$, then $p\mid\binom{-n}{r}$, since $p\mid n$. If $r\ge p$, the consecutive product $(j+r)!/j!$ is divisible by $p$. Hence the scaled upper factors are the identity modulo $p$.

The scaled exterior block is therefore, modulo $p$, the lower Toeplitz operator with generating function $\phi(z)^{-n}$. The scaled right side is the constant sequence $1$. Its solution has generating function


$$
\phi(z)^n(1-z)^{-1}.
$$


This proves (2.2). ∎

### 2.1 The new order-two exterior entries

Here


$$
b+2\equiv6p^2\pmod{p^3}.
$$


For $2\le h\le30$,


$$
\frac{z_h}{p^2}\equiv-6(h-2)!\pmod p.
\tag{2.3}
$$



Also $n/p\equiv7\pmod p$, so Frobenius gives


$$
[z^h]\frac{\phi(z)^n}{1-z}
\equiv
\begin{cases}
1,&0\le h\le28,\\
1-7=23,&h=29,30
\end{cases}
\pmod p.
$$


Consequently,


$$
\boxed{
\frac{v_h}{p^2}\equiv
\begin{cases}
-6(h-2)!,&2\le h\le28,\\
7,&h=29,\\
22,&h=30
\end{cases}
\pmod p.
}
\tag{2.4}
$$



No unknown order-two corrections to $v_0,v_1$ are needed for the particular observation derived below.

For later bounded lifting, the exact weights through $h=204$ are


$$
\lambda(0)=\lambda(1)=0,\qquad
\lambda(h)=2+\left\lfloor\frac{h-2}{29}\right\rfloor
\quad(2\le h\le204).
\tag{2.5}
$$


In particular, at coefficient precision $p^5$, only $h\le88$ survives.

---

## 3. The leading $Y/p^5$ response has only interface $000$

Set


$$
\mathsf F=Z_*/p^4,\qquad \mathsf G=Y/p^5.
$$


Use


$$
h_J=\binom WJ\binom{A+B-J}{B-J},
\qquad
K(J)=h_J/p^3.
$$



### Theorem 3.1 — Sharpened leading second-column form

On the original contact domain,


$$
\boxed{
\mathsf G_{\ell+DJ}
\equiv(-1)^{b-\ell-J}\beta_\ell K(J)\pmod p.
}
\tag{3.1}
$$


The leading profile is supported within


$$
0\le\ell\le5104.
\tag{3.2}
$$



### Proof

A contribution to $Y/p^5\bmod p$, after the common upper $p^3$ has been removed, must have total low order two.

For the two unit return atoms, A2 Turn 3 proved


$$
e_{01}+v_p(\text{row factor})\ge2.
$$


An outgoing $011$ interface supplies a further addition carry. An outgoing $110$ or $111$ interface supplies a further weight borrow. Thus none of these non-$000$ interfaces can occur at total order two.

For the positive-symbol coefficient-order-one atoms, the proved inequality is


$$
e_{01}+v_p(\text{row factor})\ge1.
$$


Adding their coefficient factor $p$ already gives order two. Again, any outgoing addition carry or weight borrow raises the order to at least three.

The $\alpha=29$ order-one atoms have an even stronger lower bound.

Finally, a coefficient-order-two atom can enter this leading response only with no low event. The guarded low comparison then forces interface $000$. Terms of coefficient order at least three cannot enter.

This proves (3.1). At coefficient order at most two, the complete exterior/source dictionary has $s\le58$, $h=0,1$, together with the new $s=0$ exterior entries $2\le h\le30$. Its largest reconstructed lower shift is $60$. Hence a leading $000$ term has


$$
\ell\le5044+60=5104.
$$


∎

This strengthens A2 Turn 3’s form: the previously allowed leading $110$ and $111$ coefficients are also zero.

---

## 4. The first unprotected digit of the whole defect

The retained ordinary-square and interface-radical results imply


$$
Z_*^TZ_*\in p^{10},\qquad Z_*^TY\in p^{11}.
$$


Therefore


$$
\boxed{\Delta(f_*)\in p^{11}.}
\tag{4.1}
$$



Thus the first not-already-protected digit is


$$
\delta_{11}
=
\frac{\Delta(f_*)}{p^{11}}\pmod p.
\tag{4.2}
$$


By (1.6), it is also the corresponding whole digit of $\Delta(\bar f)$.

Since


$$
\Delta(f_*)=p^9\bigl(6\mathsf F^T\mathsf G-\mathsf F^T\mathsf F\bigr),
\tag{4.3}
$$


we need the normalized pairing modulo $p^3$, not merely its leading or first-order terms.

### 4.1 Why normalized second-order terms are paid

At these fixed precisions, all required atoms remain inside the retained guard:

- for $Z_*\bmod p^7$, the complete source has $i\le57$, $s\le174$, hence
  

$$
\alpha\le232,\qquad -58\le v\le174;
$$


- for $Y\bmod p^8$, the complete factorial filtration gives
  

$$
\alpha\le203,\qquad 0\le v\le205.
$$



The complete first return has the same paid displacement bound: an exterior source of coefficient order $q$ reaches at most $29q-1$, and further return steps add at most $29$ per paid coefficient order. These ranges remain in the documented fixed guard. Row degrees are below $p^2$.

For the low factorial-unit expansion modulo $p^3$, one may use


$$
\prod_{\substack{1\le a\le pq+r\\p\nmid a}}a
\equiv
((p-1)!)^q r!
\left(
1+pqH_r+\frac{p^2q^2}{2}(H_r^2-H_r^{(2)})
\right)
\pmod{p^3}.
\tag{4.4}
$$


The complete-block correction vanishes modulo $p^3$: for $p\ge5$,


$$
\sum_{a=1}^{p-1}a^{-1}\in p^2\mathbb Z_p,
\qquad
\sum_{a=1}^{p-1}a^{-2}\in p\mathbb Z_p.
$$


These follow by pairing $a$ with $p-a$ and summing powers in $\mathbb F_p^\times$.

After the three low levels are stripped, the first $J$-dependent correction is $pJ\Gamma$. The genuinely second-order remainder is a residue-weighted combination of interface kernels. Short row-binomial expansions have the same property. The reconstruction correction requiring separate treatment is derived in §5.

Consequently, normalized second-order terms pair to zero modulo $p^3$, by the full residue-weighted radical. This is the higher-order accounting needed here; it is not supplied merely by the earlier three profile zeros.

### 4.2 The new sparse row

Write the relevant first corrections as


$$
\begin{aligned}
\mathsf F_{\ell+DJ}
&\equiv \sigma_{\ell,J}
\left[
a_\ell K+
p\left(u_\ell K+b_\ell JK+\sum_s c_{\ell,s}K_s\right)
\right]\pmod{p^2},\\
\mathsf G_{\ell+DJ}
&\equiv \sigma_{\ell,J}
\left[
\beta_\ell K+
p\left(v_\ell K+d_\ell JK+\sum_s e_{\ell,s}K_s\right)
\right]\pmod{p^2},
\end{aligned}
\tag{4.5}
$$


where $\sigma_{\ell,J}=(-1)^{b-\ell-J}$.

Here $a,b,c$ are the retained first-column profiles divided by $2$. The profiles $\beta,d,e$ are new: they belong to $Y/p^5$, not to the old normalization $Y/p^4$.

As before, only $011$ can meet a leading profile in a first-order cross term. Also


$$
K_{011}=(B-J)K.
$$


The constant $K$-corrections $u_\ell,v_\ell$ contribute multiples of
$p\sum K^2\in p^3$, and disappear.

Define


$$
\begin{aligned}
\mathcal A
&=\sum_{\ell=0}^{5104}a_\ell(6\beta_\ell-a_\ell),\\
\mathcal D
&=\sum_{\ell=5044}^{5104}a_\ell(6\beta_\ell-a_\ell),\\
\mathcal L
&=\sum_{\ell=0}^{5104}
\left[
6a_\ell(d_\ell-e_{\ell,011})
+(6\beta_\ell-2a_\ell)(b_\ell-c_{\ell,011})
\right]
\end{aligned}
\pmod p.
\tag{4.6}
$$



The genuinely sufficient upper data are


$$
S=\frac{\sum_{J=0}^{B}K(J)^2}{p^2},\qquad
T=\frac{\sum_{J=0}^{B}J K(J)^2}{p},\qquad
k_B=K(B)/p
\pmod p.
\tag{4.7}
$$



Then the complete, boundary-correct first whole-defect digit is


$$
\boxed{
\delta_{11}
=\mathcal A S-\mathcal D k_B^2+\mathcal L T
\pmod p.
}
\tag{4.8}
$$



The original split at $5044$ produces exactly the $-\mathcal D k_B^2$ term. Endpoint changes in the $T$-terms have an additional factor $p$ and vanish at this digit.

Equation (4.8) is substantially smaller than a full $p^8$ response calculation. It does not, by itself, evaluate the accepting value: the new low row and, if that row is nonzero, the indicated actual-word invariant must still be evaluated.

---

## 5. A reconstruction term newly visible at this digit

The old harmonic rule is not the complete $JK$ extraction for $Y/p^5$.

The unit second-column branch with lower shift $b+2$ has row factor $j$. At


$$
\ell=t p^2,\qquad 0\le t\le6,
$$


its low event count is zero, and


$$
\frac{j}{p^2}=t+pJ.
$$


The $pJ$ term contributes directly to $d_\ell$.

The resulting row-lift profile is


$$
d^{\mathrm{rec}}_{t p^2}
=
\binom{24}{t}\binom{25-t}{6-t}
\pmod p,
\qquad 0\le t\le6,
\tag{5.1}
$$


and is zero elsewhere.

For completeness, positive-symbol row factors of degree $29$ or $30$ do not add another first-order row lift here. The only potentially relevant derivative has denominator $29$. For degree $29$, the required zero-event interface is impossible; for degree $30$, it forces $\ell\equiv0\pmod p$, which kills the derivative coefficient. Coefficient-order-two row factors first affect normalized order two, already paid by the radical.

The seven exact values in (5.1) are


$$
\boxed{(26,21,5,11,26,3,7).}
\tag{5.2}
$$



### 5.1 Seven analytically evaluated leading rows

At the same seven rows, the complete leading first profile is


$$
a_{t p^2}=-2(6-t)d^{\mathrm{rec}}_{t p^2}.
\tag{5.3}
$$


Indeed, only the unit $s=r=i=0$ first-source branch survives at leading order there. The other short source branches either have an additional low event or a row-binomial factor divisible by $p$; the possible order-one return has zero leading coefficient at the required shift.

Similarly, the leading second profile is


$$
\beta_{t p^2}
=-\frac52(6-t)d^{\mathrm{rec}}_{t p^2}
=\frac54a_{t p^2}.
\tag{5.4}
$$


The contributions are:

- the two unit return branches:
  

$$
-\frac32(6-t)d^{\mathrm{rec}}_{t p^2};
$$


- the unit reconstructed $j$-branch:
  

$$
t\,d^{\mathrm{rec}}_{t p^2};
$$


- the new $v_2/p^2=-6$ exterior entry:
  

$$
-6\,d^{\mathrm{rec}}_{t p^2}.
$$



Thus


$$
\begin{array}{c|rrrrrrr}
t&0&1&2&3&4&5&6\\ \hline
a_{tp^2}&7&22&18&21&12&23&0\\
\beta_{tp^2}&16&13&8&19&15&7&0\\
d^{\mathrm{rec}}_{tp^2}&26&21&5&11&26&3&7
\end{array}
\tag{5.5}
$$



These are small explicit arithmetic evaluations, not a repetition of the old low-row audit.

### 5.2 The reconstruction correction changes the new row by $14$

Its contribution to $\mathcal L$ is


$$
6\sum_{t=0}^{6}a_{tp^2}d^{\mathrm{rec}}_{tp^2}.
$$


The seven products sum to $12\pmod{29}$, so


$$
\boxed{\Delta\mathcal L=6\cdot12=14\pmod{29}.}
\tag{5.6}
$$



All of this nonzero correction lies below the original split: the only row above $5044$ is $t=6$, where $a_{6p^2}=0$.

This gives a precise obstruction to a naive extension of the previous calculation: retaining only the old harmonic $JK$ extraction would miss a nonzero contribution to the new whole-defect row.

### 5.3 The first row of the new observation

At $\ell=0$, the three stripped units relevant to $\beta_0$ are


$$
L_0=9,\qquad L_1=18,\qquad L_2=26.
$$


Hence


$$
\beta_0=L_0+L_1-6L_2=16.
$$


The harmonic contribution to $d_0$ is $1$, and the reconstruction lift adds $26$. Thus


$$
\boxed{\beta_0=16,\qquad d_0=27,\qquad e_{0,011}=0.}
\tag{5.7}
$$



Reusing the closed first-column values gives


$$
a_0=7,\qquad b_0=10,\qquad c_{0,011}=0.
$$


The row-zero contributions to $(\mathcal A,\mathcal D,\mathcal L)$ are therefore


$$
\boxed{(14,0,11).}
\tag{5.8}
$$



A nonzero individual row does not prove that the completed coefficient row is nonzero. It does prove that the new calculation is not pointwise the old zero calculation.

---

## 6. What actual upper-word invariant is missing?

In raw binomial form, the observations in (4.7) are


$$
\begin{aligned}
S&=
\frac{1}{p^8}
\sum_{J=0}^{B}
\binom WJ^2
\binom{A+B-J}{B-J}^2
\pmod p,\\
T&=
\frac{1}{p^7}
\sum_{J=0}^{B}
J\binom WJ^2
\binom{A+B-J}{B-J}^2
\pmod p,\\
k_B^2&=\frac{\binom WB^2}{p^8}\pmod p.
\end{aligned}
\tag{6.1}
$$



Every division is paid by the retained square, radical, and endpoint theorems. Determining these values requires respectively the raw sums modulo $p^9,p^8,p^9$.

These are invariants of the actual upper word


$$
B=\frac{3^{249005515+574312172u}-5044}{29^3},
$$


not of a freely chosen continuation or merely of $b,n\bmod p^9$.

For an alternative exact specification, the unweighted raw sum is


$$
[x^B y^B z^0]\,
\frac{(1+z)^W(1+xy/z)^W}
     {(1-x)^{A+1}(1-y)^{A+1}}.
\tag{6.2}
$$


The weighted sum is obtained by introducing $txy/z$ and applying
$t\partial_t$ at $t=1$. Since $A+1=2W+2$, these are also constant-term observations of a fixed rational expression raised to the actual $W=2001B+413$.

The retained radical establishes divisibility of these observations. It does not supply their next paid digits. In particular:

- $\sum K^2\in p^2$ does not determine $S\bmod p$;
- the residue-weighted radical does not determine $T\bmod p$;
- $K(B)\in p$ does not determine $k_B^2\bmod p$.

Thus the precise missing accepting invariant, after the bounded low row has been obtained, is


$$
\boxed{
\mathcal A S-\mathcal D k_B^2+\mathcal L T
}
\tag{6.3}
$$


on the actual original upper words.

I do not claim that three independent upper values are mathematically necessary in every case: the new coefficient row might be zero or have further dependencies. The rigorously justified reduction is that no larger upper Gram jet is needed for this first whole digit. Determining whether it reduces further requires the new coefficient row, not the already closed one.

---

## 7. An evaluated whole value on an infinite original subsequence

The new leading form gives more than a sparse observation.

Define


$$
\mathcal Q=6Y/p^5-2Z_*/p^4.
\tag{7.1}
$$


Write, as in the original work,


$$
Z_w=p^{c+2}x,\qquad x\ \text{primitive at }p.
$$



### Theorem 7.1 — Exact leading-content and feedback classification

Under the retained hypotheses,


$$
\boxed{
c\ge3
\quad\Longleftrightarrow\quad
K(J)\equiv0\pmod p\ \text{for every }0\le J\le B.
}
\tag{7.2}
$$


Furthermore,


$$
\boxed{
c\ge3\Longrightarrow Y\in p^6\mathbb Z_p^{b+1},
}
\tag{7.3}
$$


and


$$
\boxed{
\mathcal Q\equiv0\pmod p
\quad\Longleftrightarrow\quad c\ge3.
}
\tag{7.4}
$$



### Proof

From (1.2),


$$
\bar Z-Z_*\in p^5.
$$


At $\ell=0$, the complete leading first response is


$$
Z_{*,DJ}/p^4\equiv(-1)^{b-J}7K(J)\pmod p.
\tag{7.5}
$$


The original $\ell=0$ range contains every $0\le J\le B$.

If $c\ge3$, then $\bar Z\in p^5$, hence $Z_*\in p^5$. Equation (7.5) forces every $K(J)$ to be zero modulo $p$.

Conversely, if every $K(J)$ is zero, the complete leading first profile vanishes. The physical first terminal is already in $p^6$, so $Z_*\in p^5$, and then $\bar Z\in p^5$. Thus $c\ge3$. This proves (7.2).

Theorem 3.1 now makes every contact coordinate of $Y/p^5$ zero. The physical terminal is in $p^6$, proving (7.3).

Finally,


$$
\mathcal Q_{DJ}
\equiv(-1)^{b-J}(6\beta_0-2a_0)K(J)
=(-1)^{b-J}24K(J)\pmod p.
\tag{7.6}
$$


Thus $\mathcal Q\equiv0$ implies all $K(J)\equiv0$. The converse follows from the complete leading forms of both columns and their terminal valuations. ∎

### Corollary 7.2 — Evaluated first whole-defect digit

For every original index with $c\ge4$,


$$
\boxed{\Delta(\bar f)\equiv\Delta(f_*)\equiv0\pmod{p^{12}}.}
\tag{7.7}
$$



Indeed, $Y\in p^6$, so


$$
6\bar Z^TY\in p^{c+8},\qquad
p\bar Z^T\bar Z\in p^{2c+5}.
$$


Both are in $p^{12}$ when $c\ge4$. Equation (1.6) transfers the result to $f_*$.

This is an evaluated **whole** defect, not a replacement of it by a named flat contraction.

The retained theorem that $c$ is unbounded in every original progression allows an increasing sequence


$$
u_r\equiv2\pmod{p^9},\qquad c(u_r)\ge\max\{r,4\}.
$$


Thus (7.7) holds on an infinite sequence of unchanged original indices.

It does not settle the $c=2,3$ strata of the original family, and it does not settle the growing primitive-depth target on the chosen subsequence.

---

## 8. The next feedback digit and the actual normalized tail

The exact retained expansion gives


$$
\begin{aligned}
\frac{\Delta(\bar f)-\Delta(f_*)}{p^{12}}
\equiv{}&
6\,\frac{U^TY}{p^{10}}
-2\,\frac{Z_*^TU}{p^9}
+V^T\mathcal Q
\pmod p.
\end{aligned}
\tag{8.1}
$$



All displayed divisions are paid by (1.3)–(1.4).

### 8.1 What is now genuinely annihilated

Theorem 7.1 proves


$$
\boxed{c\ge3\Longrightarrow V^T\mathcal Q=0\pmod p.}
\tag{8.2}
$$



This conclusion applies to the actual $V=L\bar w$. It does not delete the tail because it was harmless at an earlier fixed layer. Instead, the entire tested vector $\mathcal Q$ is proved zero modulo $p$, under the explicit and verifiable hypothesis $c\ge3$.

On the $c=2$ stratum, $\mathcal Q$ is nonzero. That does **not** prove the actual tail pairing is nonzero: $L^T\mathcal Q$ could vanish, or the actual source could be orthogonal to it.

### 8.2 An exact finite adjoint test

Let


$$
(\mathsf P_-)_{ki}=(-1)^{k-i}\binom ki.
$$


Modulo $p$, the complete finite inverse is


$$
A^{-1}\equiv R_{2n,II}\mathsf P_-\pmod p.
\tag{8.3}
$$


The finite return is accounted for here: its $EI$ factor is zero modulo $p$.

Define


$$
s_j=(j+1)W_{j+1}\mathcal Q_{j+1}-W_j\mathcal Q_j,
\qquad 0\le j<b,
\tag{8.4}
$$


including the actual $j=b-1$ term. Put


$$
S(z)=\sum_{j=0}^{b-1}s_jz^j,
$$




$$
M(z)=\bigl[(1+z)^{-2n}S(z)\bigr]_{<b},
\qquad
\Lambda(X)=M(X-1).
\tag{8.5}
$$


Then


$$
\boxed{[X^i]\Lambda(X)=(L^T\mathcal Q)_i\pmod p.}
\tag{8.6}
$$



This follows by successively applying $\mathcal R^T$, the transpose upper convolution, and the transpose finite binomial transform. The truncation before substituting $X-1$ is essential: it retains the original finite boundary.

Since $T_i=Le_i\in p^3$ for $0\le i\le202$,


$$
[X^i]\Lambda=0\qquad(0\le i\le202).
$$


For $i>202$, (1.2) gives


$$
\bar w_i=\frac{f_i^0}{p^7C_n}.
$$


Therefore the actual tail term is exactly


$$
\boxed{
V^T\mathcal Q
=
C_n^{-1}
\sum_{i=203}^{b-1}
\frac{f_i^0}{p^7}[X^i]\Lambda(X)
\pmod p.
}
\tag{8.7}
$$



This is an explicit finite source test on the actual first force, not an assertion about an arbitrary tail.

Also, because $W_b\mathcal Q_b=0\pmod p$, the recurrence (8.4) shows


$$
L^T\mathcal Q=0
\quad\Longleftrightarrow\quad
W_j\mathcal Q_j=0\ \text{for all }0\le j\le b
\pmod p.
\tag{8.8}
$$


Thus the adjoint offers a concrete possible annihilation law, but it must be checked in the actual weighted column.

### 8.3 A concrete one-digit source lemma that would finish the tail issue

The short-source pointwise bound extends to


$$
\boxed{Le_i\in p^3\mathbb Z_p^{b+1}\qquad(0\le i\le231).}
\tag{8.9}
$$



To verify this extension, work only modulo $p^3$. The exact finite source formula has $s\le58$. For $i\le231$,


$$
\alpha\le290,\qquad -232\le v\le58,
$$


and row degrees remain below $p^2$. The finite return has exterior displacement at most $57$ at this precision. These are within the retained three-event guard; the physical terminal is separately divisible by $p^6$.

It follows that the sum in (8.7) can start at $232$.

Hence the following is a sufficient, source-specific follow-on lemma:

> **Actual first-force tail lemma $\mathbf{H}_8$.**  
> Prove, from the original generating definition of $f^0$, that
> 

$$
> f_i^0\in p^8\mathbb Z_p\qquad(232\le i<b).
>
$$


> Then $V\equiv0\pmod p$, and the normalized tail term in (8.1) vanishes on the entire original family.

A stronger identity $f_i^0\in i!\mathbb Z_p$ would imply $\mathbf H_8$, since $v_p(232!)=8$. But the supplied packet does not contain an all-row proof of that first-force identity. The $p^7$-tail statement alone does not imply it.

This is therefore a **conditional annihilation lemma and a precise open source obligation**, not a proved deletion of the actual tail on the $c=2$ stratum.

---

## 9. Both terminal terms at the next digit

Let


$$
\chi=A^{-1}f_*,
\qquad
\psi=A^{-1}\mathbf r.
$$


The physical coordinates are exactly


$$
Z_{*,b}=bW_b\chi_{b-1},\qquad
Y_b=W_b(b\psi_{b-1}+1).
\tag{9.1}
$$



The $+1$ is the separate physical terminal. It is not part of an analytically continued contact value.

### 9.1 Terminal units

From (8.3), the last row of the finite inverse gives


$$
\chi_{b-1}\equiv
\sum_{i=0}^{28}(-1)^{b-1-i}\binom{b-1}{i}i!
\pmod p.
$$


Since $b-1$ is even and $(b-1)\bmod p=26$,


$$
\chi_{b-1}\equiv
\sum_{i=0}^{26}(-1)^i(26)_{\underline i}
=22\pmod p.
\tag{9.2}
$$


The last value is checked by the short recurrence


$$
d_0=1,\qquad d_m=1-md_{m-1}\pmod{29}.
$$



For the complete second contact solution, the logarithmic force is zero modulo $p$ by its whole-row guard. The leading exterior entries are $v_0=1,v_1=-1$; the two relevant upper displacements from $b-1$ are $1,2$, and their negative binomials are divisible by $p$. Hence


$$
\psi_{b-1}\equiv0\pmod p.
\tag{9.3}
$$



Thus both physical column factors have been evaluated:


$$
\chi_{b-1}\equiv22,\qquad b\psi_{b-1}+1\equiv1\pmod p.
$$



In particular, the actual normalized first column has the same terminal unit, because $\bar f\equiv f_*\pmod p$. Therefore


$$
v_p(Z_{w,b})=v_p(Y_b)=v_p(W_b),
\tag{9.4}
$$


and


$$
c+2\le v_p(W_b).
\tag{9.5}
$$



### 9.2 Evaluated terminal contribution

The three low weight digits give


$$
\frac{W_b}{p^6}\equiv11\,k_B\pmod p.
\tag{9.6}
$$


Indeed, the low borrow digits are $(4,7,18)$, and the stripped unit is


$$
\frac{2!}{27!\,4!}\,
\frac{7!}{28!\,7!}\,
\frac{24!}{5!\,18!}
\equiv11\pmod{29}.
$$



Consequently,


$$
\frac{6Z_{*,b}Y_b}{p^{12}}
\equiv
6\cdot27\cdot22\cdot11^2\,k_B^2
=14k_B^2\pmod p.
\tag{9.7}
$$


The terminal norm term $pZ_{*,b}^2$ is in $p^{13}$.

Thus the physical terminal contributes


$$
\boxed{14k_B^2}
$$


to the next flat-defect digit. Both parts of $Y_b$ were retained; (9.3), rather than a boundary omission, pays the reconstructed part at this digit.

If $c\ge5$, (9.5) forces $v_p(W_b)\ge7$, so this terminal contribution then vanishes. No such deletion is justified uniformly on the original family.

---

## 10. The bounded new low-row certificate

Only a coefficient-order-two second-column lift is needed for (4.8). A $205\times205$ solve is not needed.

### 10.1 New symbols, without repeating the old symbol table

Retain the already established $c_s/p\bmod p$ for $1\le s\le29$. Define


$$
E_\phi(z)=\frac{\phi(z)^p-\phi(z^p)}p.
$$


This belongs to $\mathbb Z_{(p)}[z]$. Its division by $p$ is paid by Frobenius; denominators are powers of $2$, hence units.

For $1\le r\le28$,


$$
\boxed{
\frac{c_{p+r}}{p^2}
\equiv
7r!\bigl([z^{p+r}]E_\phi+8[z^r]E_\phi\bigr)
\pmod p,
}
\tag{10.1}
$$


and


$$
\boxed{c_{58}/p^2\equiv20\pmod p.}
\tag{10.2}
$$



To derive (10.1), write $n=pm$ and expand


$$
\phi(z)^{-pm}
\equiv
\phi(z^p)^{-m}
-pm E_\phi(z)\phi(z^p)^{-m-1}
\pmod{p^2}.
$$


For degrees $p+r$ not divisible by $p$, the first term is zero. Also


$$
(p+r)!/p\equiv-r!\pmod p.
$$


Equation (10.2) follows from


$$
[z^{2p}]\phi(z)^{-n}\equiv m^2/2=10\pmod p,
\qquad
(2p)!/p^2\equiv2\pmod p.
$$



### 10.2 The reduced, complete-at-observation-scope dictionary

Use the retained order-zero/one second dictionary, and add:

1. for $h=0,1$, $1\le s\le29$, and $1\le a\le\min(s,28)$,
   

$$
\varepsilon_h c_s\binom{-n}{a}
   \Psi_{a,h+s-a,s-a};
$$


2. for $h=0,1$, $30\le s\le58$, and
   $a\in\{0,29,58\}$, $a\le s$,
   

$$
\varepsilon_h c_s\binom{-n}{a}
   \Psi_{a,h+s-a,s-a};
$$


3. the $29$ terms
   

$$
v_h^{(2)}\Psi_{0,h,0},\qquad 2\le h\le30,
$$


   with (2.4).

The new bounded coefficient values use


$$
\frac1p\binom{-n}{a}
\equiv 7\frac{(-1)^a}{a}\pmod p
\quad(1\le a\le28),
$$


and, for $a=0,29,58$,


$$
\binom{-n}{a}\equiv1,\ 22,\ 28\pmod p.
$$



The omitted order-two corrections to already present order-one atoms affect only a constant $pK$ term or a higher paid remainder. Coefficient-order-three terms enter the relevant first correction only with no low event, hence again as a constant $pK$. Their next normalized order is killed by the full weighted radical. This is an observation-scope statement, not equality of physical columns.

### 10.3 Extraction and bounded size

For each reconstructed branch with signed row coefficient $C_\ell$:

- if $v_p(C_\ell)+e=2$, add
  

$$
p^{e-2}C_\ell L
$$


  to $\beta_\ell$, and its harmonic multiple to $d_\ell$;
- add the explicit seven-row correction (5.2) to $d_\ell$;
- if the interface is $011$ and $v_p(C_\ell)+e=3$, add
  

$$
p^{e-3}C_\ell L
$$


  to $e_{\ell,011}$.

These divisions require at most coefficient and row-binomial information modulo $p^3$, and are paid by the stated valuation tests.

A safe atom count is


$$
62+868+118+29=1077.
$$


Thus at most


$$
2\cdot1077\cdot5105=10\,996\,170
$$


new branch-row evaluations are required.

The first-column profiles on $0,\ldots,5074$ are reused from the existing data. Only $c_{\ell,011}$ on the additional $30$ rows $5075,\ldots,5104$ may need extending. The old $5075$-row first-column calculation is not repeated.

A Pascal table with


$$
0\le\ell\le5104,\qquad 0\le r\le59
$$


has $306300$ entries. No large exterior solve occurs.

### Expected verifiable output

A coordinator-authored certificate should return:

- the new $29$-entry symbol array (10.1)–(10.2);
- the $29$ exterior residues (2.4);
- $\beta_0=16$, $d_0=27$, $e_{0,011}=0$;
- the seven-row table (5.5);
- the reconstruction subtotal $14$, entirely below the original split;
- the completed $(\mathcal A,\mathcal D,\mathcal L)\in\mathbb F_{29}^3$;
- lower/upper and source/return subtotals;
- the exact identity (4.8).

No value for the completed triple is invented here.

If it is zero, the first whole-defect digit is zero on the entire retained original family. If it is nonzero, the next obligation is the actual-word value (6.3), not another low audit.

---

## 11. If a full $p^8$ second-response certificate is desired

The preceding observation does not require it. Nevertheless, a full certificate can be assembled without a dense $205$-square solve or a triple coefficient summation.

At physical precision $p^8$, the full retained support remains inside the fixed guard. Its common upper $p^3$ means coefficient precision $p^5$ suffices for contact reconstruction. By (2.5), only exterior indices


$$
0\le h\le88
$$


are needed, and $s\le116$.

Let $H=88$, $m=116$. A product by the exterior block $C_{EE}$ can be evaluated directly from $R_nD_-R_n$. For input $v_0,\ldots,v_H$, form


$$
a_r=\sum_{k=\max(0,r)}^H\binom{-n}{k-r}v_k,
\qquad -m\le r\le H,
$$




$$
b_t=\sum_{s=0}^m c_s\binom{b+t}{s}a_{t-s},
\qquad 0\le t\le H+m,
$$


with $a_r=0$ outside its range, and then


$$
(Cv)_h=\sum_{t=h}^{H+m}\binom{-n}{t-h}b_t,
\qquad 0\le h\le H.
\tag{11.1}
$$



This is the normal-ordered coefficient structure, evaluated as two triangular convolutions and one banded lower operation. There is no $(h,k,s,a)$ assembly.

Write $C=R_{2n}+E$, $E\in pM$. Modulo $p^5$,


$$
v=\sum_{r=0}^{4}(-T_{2n}E)^rT_{2n}z.
\tag{11.2}
$$


A direct count gives fewer than $3\times10^5$ modular multiplication-additions for these matrix-vector stages, excluding preparation of the bounded binomial tables.

Inputs $b,n\bmod p^6$ suffice for the needed small-index binomials modulo $p^5$; they are available from the specified original exponent residue. Exact products with their $p$-valuations removed, or exact integer binomial recurrences, pay all nonunit divisions.

Expected outputs are the exterior vector, its residual


$$
Cv-z\equiv0\pmod{p^5},
$$


the filtered reconstructed dictionary, and a separate physical-terminal record.

This would certify a fixed-depth complete response only. It would not evaluate the enormous upper word, prove an all-depth source identity, or determine an all-prime primitive denominator.

---

## 12. Growing precision is still indispensable

Retain


$$
Z_w=p^{c+2}x,\qquad x^Tx=p^\nu\eta,\qquad
d=2c+4+\nu,
$$


and the actual depth


$$
K=d-c=c+4+\nu.
$$



Because $C_n$ is a unit, the normalized primitive target remains


$$
\boxed{
6\bar x^TY^{[K]}-p^{K-1}\bar\eta
\equiv0\pmod{p^K}.
}
\tag{12.1}
$$



The complete $Y^{[K]}$ retains:

- symbols through $s=p(K-1)$;
- the actual finite exterior solve and return;
- the physical terminal;
- the logarithmic head
  

$$
L_{\log}(K)
  =
  \min\!\left(b,\ p\max\{K-N_{\log},0\}\right),
$$


  where
  

$$
N_{\log}
  =
  2v_p(n!)-v_p(b!)
  -\lfloor\log_p(2n+b-1)\rfloor.
$$



At the present fixed depths $N_{\log}>8$, so its omission is paid. This does not authorize omission once the actual $K$ exceeds that threshold.

The retained error estimate remains


$$
\bar Z^T(Y-Y^{[K]})\in p^{d+2}\mathbb Z_p.
$$



The new content transfer improves the elementary whole-defect bound to


$$
c\ge3\Longrightarrow
\Delta(\bar f)\in p^{c+8}.
\tag{12.2}
$$


But the target is $p^{d+2}=p^{2c+6+\nu}$. The remaining gap is


$$
c-2+\nu,
$$


which is unbounded along the retained growing-content subsequence.

Thus the new fixed digit and feedback annihilation do not stabilize the required precision.

---

## 13. Actual contents, least clearer, all-prime gcd, and whole error

Nothing here changes the original row contents or the actual least simultaneous clearer $d_B$. Division by the $29$-adic unit $C_n$ is not an all-prime primitive normalization.

Retain the original integer columns $N_{B,1},N_{B,2}$ and


$$
\omega_j=\frac{(n+2)!}{(n+2-j)!},
\qquad
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2).
$$


The actual arithmetic is


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),
\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$



The gcd is over **all primes**, and the actual primitive multiplier remains


$$
d_B^2/g_B.
$$


In particular,


$$
\log q_n
=
\sum_{\ell\ {\rm prime}}
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
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
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$



The selected increasing original sequence $u_r$ with $c(u_r)\to\infty$ is legitimate for these same-index statements. What remains absent is an all-prime estimate for its actual $q_n$ proving


$$
0<|q_n\epsilon_n|\longrightarrow0.
$$


If that held, rationality of $e+\pi$ would contradict the lower bound for a nonzero integer multiple of a fixed rational denominator. No estimate in this report establishes it.

---

## 14. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Old fixed-layer omission accounting and zero row | Reused; not recomputed |
| $v_p(v_h)\ge v_p(z_h)$ for the actual exterior solution | **New proved filtration statement** |
| Leading exterior quotient (2.2), and order-two entries (2.4) | **New proved and evaluated statements** |
| Entire leading $Y/p^5$ response has interface $000$ | **New proved statement under the retained guard** |
| First unprotected whole-defect digit is at $p^{11}$ | **Proved** |
| Complete first-digit reduction (4.8) | **Proved; accepting value not yet evaluated on the entire family** |
| Seven-row reconstruction correction changes $\mathcal L$ by $14$ | **Explicitly evaluated** |
| $\mathcal Q\equiv0\pmod p$ iff $c\ge3$ | **New proved classification** |
| Actual normalized-tail feedback vanishes for $c\ge3$ | **Proved by pointwise annihilation** |
| $\delta_{11}=0$ for every original index with $c\ge4$ | **Evaluated whole-defect result** |
| Infinite original subsequence with this evaluated value and $c\to\infty$ | Consequence of the retained unbounded-content theorem |
| Physical terminal at the next flat digit is $14k_B^2$ | **Explicitly evaluated** |
| Tail annihilation on the $c=2$ stratum | Open; exact adjoint/source test supplied |
| First-force lemma $\mathbf H_8$ | Conditional sufficient lemma; not validated by the packet |
| Growing-depth alignment at $K=c+4+\nu$ | Open |
| All-prime denominator versus nonzero whole same-index error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### Final assessment

The new result is not merely another equality with an unevaluated flat defect. It includes:

- a stronger analytic description of the complete leading second response;
- an explicit nonzero correction to the first new whole-defect observation;
- a content-dependent evaluation of the complete feedback vector;
- an evaluated whole-defect zero on an infinite original subsequence;
- an evaluated physical-terminal contribution at the next digit.

The immediate bounded obligation is the new three-residue row


$$
(\mathcal A,\mathcal D,\mathcal L)
$$


specified in §10. It uses the stored first-column profiles, new coefficient-order-two second-column data, and the explicit reconstruction correction. It does not require repeating the closed audit or solving a dense $205$-square system.

If that row is nonzero, the exact first-digit bottleneck is the actual-word invariant (6.3). At the next feedback digit, the $c=2$ stratum requires the actual source identity (8.7), or a proof of the concrete tail lemma $\mathbf H_8$. At growing precision, further source digits, finite returns, and the logarithmic head remain necessary.

Finally, even a complete local alignment theorem would leave the indispensable all-prime comparison with the actual primitive denominator and the nonzero whole error at the same infinite original indices. An unconditional proof or disproof of the irrationality of $e+\pi$ is not obtained.
