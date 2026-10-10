> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 Turn 3 — Analytic vanishing of the second-column profiles and a paid normalized-source feedback identity

## Abstract

The corrected interpretation of the saved calculation is consistent with the mathematics: the first-column profiles are not zero, while the three extracted second-column profiles are zero. No change of formula or sign is needed.

This report proves the second-column vanishing analytically. The mechanism is a combination of low-digit carries and divisibility of the row-binomial factors. In particular, the potentially exceptional branch with lower shift $b+2$ is not missing: its reconstruction factor $j$ pays the divisibility that its low factorial factors do not supply.

Using the retained guarded upper-kernel and weighted-radical results at their stated scope, the analytic argument also proves


$$
Y\in29^5\mathbb Z_{29}^{b+1},
\qquad
\kappa=0,
$$


and strengthens the short-source observation bound to


$$
(\mathcal RA^{-1}e_i)^TY\in29^{10}\mathbb Z_{29},
\qquad 0\le i\le202.
$$


These conclusions preserve the original contact cutoffs and physical terminal.

The recovered independent definition


$$
\rho_n=(6C_n)^{-1},\qquad C_n=f_0^0,
$$


allows a further source-specific improvement. After normalizing the whole first force by $C_n$, its order-$29$ scalar head ambiguity disappears. I derive an exact normalized-source decomposition and prove that the complete relative defect agrees with the normalized flat-head defect modulo $29^{12}$. I then derive the next, fully paid feedback digit, including the original $29^7$-tail contribution. That tail is an explicit obstruction to extending the flat-head identity one more digit without new information.

These are finite-depth identities on the original family. They do not establish the alignment at the unbounded actual depth $K=c+4+\nu$, and they do not provide the all-prime primitive-denominator estimate needed for an irrationality proof of $e+\pi$.

---

## 1. Original objects and retained hypotheses

Throughout,


$$
p=29,\qquad D=p^3=24389,
$$


and the original family is


$$
b=3^{249005515+574312172u},\qquad n=2001b,
$$


with


$$
u\ge0,\qquad u\equiv2\pmod{p^9}.
$$



The domains remain exactly:

- contact coordinates $0\le j<b$;
- recurrence source rows $1\le i\le b-2$;
- reconstructed coordinates $0\le j\le b$.

Put


$$
W_j=\binom{n+2}{j},\qquad
(\mathcal Rx)_j=W_j(jx_{j-1}-x_j),
\qquad x_{-1}=x_b=0,
$$


and abbreviate


$$
L=\mathcal RA^{-1}.
$$


The actual columns are


$$
Z_w=Lf^0,\qquad
Y=L\mathbf r+W_be_b,
$$


where


$$
\mathbf r=A_{IE}z+\frac{h^F}{b!},
\qquad
z_h=\frac{(b+h)!}{b!}.
$$



Thus $Y$ includes the complete exponential force, both original initial charges, every recurrence source row, the finite returns, and the logarithmic force formed from $F/(1-z)$. The physical terminal is separate.

The original split is


$$
j=\ell+DJ<b,\qquad
0\le J\le B-\mathbf1_{\ell\ge5044},
$$


where


$$
b=DB+5044,\quad
n+2=DW+20389,\quad
2n-1=DA+16384.
$$


In particular, the split remains at $\ell=5044$, not at the endpoint of an auxiliary low-row table.

### Retained mathematics used below

I reuse, rather than recompute:

1. the complete-force identification and finite inverse/return formula;
2. the growing-depth factorial filtration theorem;
3. the guarded three-event upper forcing and its eight integral kernels $K_s$;
4. the weighted interface radical
   

$$
\sum_J R(J\bmod p)K_s(J)K_t(J)\equiv0\pmod p;
$$


5. the lifted ordinary square divisibility
   

$$
\sum_JK(J)^2\in p^2\mathbb Z_p;
$$


6. the original terminal estimate $W_b\in p^6\mathbb Z_p$;
7. the actual head expansion quoted in §5 below.

Both original upper cutoffs satisfy the radical identities. For the lifted ordinary square, removing the endpoint changes the sum by $K(B)^2\in p^2\mathbb Z_p$, so its divisibility also survives the original cutoff.

These are established inputs at the stated guarded scope. The new arguments below do not infer them from the numerical profile certificate.

---

## 2. Why the complete displayed second-column profiles vanish

### 2.1 The second-column dictionary

The displayed dictionary is


$$
\begin{aligned}
\mathscr Y={}&
(1+6p)\Psi_{0,0,0}+(-1+16p)\Psi_{0,1,0}\\
&+\sum_{h=0}^{1}\sum_{s=1}^{29}
\varepsilon_hc_s\Psi_{0,h+s,s}\\
&+\sum_{h=0}^{1}
\varepsilon_hc_{29}\binom{-n}{29}\Psi_{29,h,0},
\end{aligned}
\tag{2.1}
$$


where


$$
\varepsilon_0=1,\quad \varepsilon_1=-1,\quad
c_s\in p\mathbb Z_p\quad(1\le s\le29).
$$



For an atom $T\Psi_{\alpha,v,r}$, the two reconstructed branches have lower shifts and row factors


$$
(v',R_\ell)=(v,\binom\ell r),
\qquad
(v+1,(r+1)\binom\ell{r+1}),
$$


up to the prescribed common signed coefficient. Signs do not affect the divisibility argument.

The relevant fixed digits are


$$
20389=(2,7,24)_{29},\qquad
16384=(28,13,19)_{29},
$$


and


$$
5044=(27,28,5)_{29}.
$$



Let $e_{01}=w_0+w_1+c_0+c_1$ count the weight-borrow and addition-carry events in the first two digits. Let $e$ include the third digit as well.

A branch contributes to:

- a leading profile only if
  

$$
v_p(C_\ell)+e=1;
$$


- an $011$ first correction only if
  

$$
v_p(C_\ell)+e=2,
$$


  with interface $011$.

The interface $011$ necessarily has $c_2=1$, hence


$$
e\ge e_{01}+1.
\tag{2.2}
$$



We will prove stronger, branchwise inequalities that exclude both possibilities.

---

### 2.2 The two unit return atoms

The four branches of the first line of (2.1) have


$$
(v',R_\ell)=(0,1),(1,\ell),(1,1),(2,\ell).
\tag{2.3}
$$



#### Shifts $v'=0,1$

The first two digits of $5044+v'$ are respectively


$$
(27,28),\qquad(28,28).
$$



I claim


$$
e_{01}\ge2.
\tag{2.4}
$$



If $\ell_0>2$, there is a weight borrow in digit zero. Unless $\ell_0$ equals the lower digit $27$ or $28$, the addition also carries in digit zero, and (2.4) follows immediately.

In the exceptional equality case, digit-zero addition has no carry, but the weight borrow enters digit one. Avoiding a digit-one weight borrow requires $\ell_1\le6$, whereas avoiding the digit-one addition carry would require $\ell_1\ge13$. They cannot both be avoided.

If $\ell_0\le2$, digit zero has an addition carry and no weight borrow. In digit one:

- the addition carries for $\ell_1\le13$;
- the weight subtraction borrows for $\ell_1\ge8$.

Again at least one further event occurs. This proves (2.4).

Consequently these branches have total low order at least two, and at least three on interface $011$.

#### Shift $v'=2$, with row factor $\ell$

Here


$$
5046=(0,0,6)_{29}.
$$


The low factorial factors alone can have fewer events. The reconstruction factor $\ell$ must therefore be retained.

The precise inequality is


$$
\boxed{e_{01}+v_p(\ell)\ge2.}
\tag{2.5}
$$


At $\ell=0$, the branch is zero.

If $\ell_0\ne0$, digit zero has an addition carry. If $\ell_0>2$, it also has a weight borrow. For $\ell_0=1,2$, the digit-one addition carries when $\ell_1\le13$, while the weight subtraction borrows when $\ell_1\ge8$. Thus $e_{01}\ge2$.

If $\ell_0=0$ and $\ell_1\ne0$, then $v_p(\ell)\ge1$. At least one digit-one event occurs by the same comparison.

If $\ell_0=\ell_1=0$, then $v_p(\ell)\ge2$.

This proves (2.5).

Thus the $b+2$ branch also has total order at least two, and at least three on $011$. It is not a missing unit contribution.

---

### 2.3 Positive-symbol atoms with $\alpha=0$

These branches have coefficient valuation at least one, and


$$
(v',R_\ell)
=
(h+s,\binom\ell s)
$$


or


$$
(v',R_\ell)
=
(h+s+1,(s+1)\binom\ell{s+1}),
$$


where $h=0,1$ and $1\le s\le29$.

It suffices to prove


$$
\boxed{e_{01}+v_p(R_\ell)\ge1.}
\tag{2.6}
$$



Suppose $e_{01}=0$. The absence of a weight borrow gives


$$
\ell_0\le2,\qquad \ell_1\le7.
$$


Since the first addition digit is $28+k_0^{\rm dig}$, no addition carry is possible only when


$$
k_0^{\rm dig}=0.
$$


Thus $\ell_0$ equals the low digit of $5044+v'$.

For $1\le v'\le31$, the only possibilities are:

- $v'=2,3,4$, with
  

$$
\ell_0=v'-2,\qquad \ell_1=0;
$$


- $v'=31$, with
  

$$
\ell_0=0,\qquad \ell_1\le1.
$$



For $v'=2,3,4$, the row degree in either branch is at least $v'-1$, strictly larger than $\ell_0=v'-2$. Lucas reduction therefore makes the row-binomial factor zero modulo $p$.

The case $v'=31$ occurs only for the second branch with $h=1,s=29$. Its row degree is $30=(1,1)_{29}$, while $\ell_0=0$, so its row-binomial factor is again zero modulo $p$.

This proves (2.6).

Including the coefficient factor $p$, every such branch has total order at least two. On $011$, equation (2.2) raises that lower bound to three.

---

### 2.4 The $\alpha=29$ atoms

Now


$$
16384+29=(28,14,19)_{29}.
$$


The branches again have shifts $v'=0,1,1,2$ and row factors $1,\ell,1,\ell$, but their coefficients are divisible by $p$.

The proof in §2.2 remains valid when the digit-one addition parameter changes from $13$ to $14$: the intervals forcing an addition carry and a weight borrow still overlap. In particular, the same inequalities (2.4)–(2.5) hold.

These branches therefore cannot contribute to any of the three extracted profiles either.

---

### 2.5 Analytic conclusion

Every branch of the displayed second-column dictionary has


$$
v_p(C_\ell)+e\ge2,
$$


and every branch on interface $011$ has


$$
v_p(C_\ell)+e\ge3.
$$



Hence, without summing different atoms,


$$
\boxed{g_\ell=d_\ell=e_{\ell,011}=0\qquad(0\le\ell<D).}
\tag{2.7}
$$



The $JK$ profile vanishes because it is extracted only from leading branches, and there are no such branches.

This proves the mathematical explanation of the corrected certificate. The first-column values $a_0=14$, $b_0^{\rm prof}=20$, and the reported first-column support counts are compatible with (2.7).

---

## 3. Completeness and observable-order omissions

### 3.1 Why the exterior support really is two-dimensional at coefficient order one

The two-coordinate exterior result need not be recomputed, but its support can be checked analytically.

The original low residue gives


$$
b\equiv-2\pmod{p^2}.
$$


Thus


$$
z_h=(b+1)\cdots(b+h)\in p^2\mathbb Z_p
\qquad(h\ge2).
\tag{3.1}
$$



At modulus $p^2$, the growing-depth theorem retains $s\le29$ and exterior rows $h\le30$. For $h\ge2$ and $k=0,1$, the only potentially nonzero order-one contribution to $C_{hk}$ is


$$
c_{h-k}\binom{b+h}{h-k},
\tag{3.2}
$$


when $1\le h-k\le29$.

Indeed:

- the $s=0$ term has a negative lower index;
- $1\le a<29$ supplies an extra factor $p$;
- $a=s=29$ again has a negative lower index;
- with $a=0$, the remaining lower binomial is zero modulo $p$ unless its lower index is zero.

For $2\le h\le28$, the low digit of $b+h$ is $h-2$, smaller than either $h$ or $h-1$. Hence the binomial in (3.2) is zero modulo $p$.

At $h=29,30$, the digit-one value of $b+h$ is zero modulo $p$, because $b\equiv-2\pmod{p^2}$; the remaining lower-index possibilities are likewise zero by Lucas reduction.

Thus


$$
C_{h0},C_{h1}\in p^2\mathbb Z_p\qquad(h\ge2)
$$


at the retained precision. Together with (3.1), this verifies that the retained solution


$$
v_0^Y=1+6p,\qquad v_1^Y=-1+16p,\qquad
v_h^Y=0\pmod{p^2}\ (h\ge2)
$$


solves all retained equations, not merely the first two.

---

### 3.2 Coefficient-order-two omissions do not recreate these profiles

After extracting the common upper factor $p^3$ and normalizing by $p^4$, an atom of coefficient order $t$ and low event count $e$ occurs at order


$$
p^{t+e-1}.
$$



For $t=2$, a first correction requires $e=0$. The guarded low comparison then forces interface $000$. Its leading stripped coefficient is independent of $J$, so it changes only a constant multiple of $pK(J)$.

It cannot change:

- the leading profile;
- the $JK$ profile;
- the $011$ profile.

Terms of coefficient order at least three do not enter these first corrections.

Thus (2.7) survives the observable-order omissions. Constant $000$ first corrections remain, and are not asserted to vanish.

---

### 3.3 The additional form needed to conclude $\kappa=0$

For completeness, the argument for $\kappa$ must account for one more normalized order, rather than merely point to three zero arrays.

The complete second column has the guarded form


$$
\frac{Y_{\ell+DJ}}{p^4}
=
pE_\ell(J)+p^2Q_\ell(J)\pmod{p^3},
\tag{3.3}
$$


where:

1. $E_\ell$ is a linear combination of $K_s$ with low coefficients independent of $J$;
2. its $011$ coefficient is zero;
3. its $110$ and $111$ coefficients are supported on $\ell>20389$;
4. on $\ell\le20389$,
   

$$
E_\ell(J)=\beta_\ell K(J);
$$


5. $Q_\ell$ is a linear combination
   

$$
Q_\ell(J)=\sum_sR_{\ell,s}(J\bmod p)K_s(J).
   \tag{3.4}
$$



Here is why the last assertion does not require an unproved second lift of a leading atom. Section 2 showed that no second-column atom starts at normalized order zero. Through normalized order two, only the first unit lift of an order-one atom is needed. The stripped factorial-unit formula gives dependence on $J\bmod p$; the row-binomial corrections do the same. Coefficient-order-two and -three additions have the same guarded interface form.

The needed source support is still within the established guard. At physical precision $p^7$, the growing-depth theorem has symbol index at most $174$ and exterior index at most $175$, with reconstructed shifts at most $176$. After the common upper $p^3$ is accounted for, coefficient orders at most three suffice; their surviving shifts are at most $89$. These bounds lie within the retained fixed-layer guard. No new exterior solve is required to prove the form (3.3)–(3.4).

The logarithmic force is also paid at this fixed precision. Indeed,


$$
N_{\log}
=
2v_p(n!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor
$$


is much larger than $7$ on the original family. A crude sufficient bound uses


$$
v_p(n!)\ge n/p=69b,\qquad v_p(b!)\le b/28.
$$


This fixed-depth omission does not apply when the actual growing $K$ exceeds $N_{\log}$.

Finally, the physical terminal remains separate; its product with either actual reconstructed column is in $p^{12}$.

---

### 3.4 Whole fixed-layer vanishing

The first column has


$$
\frac{Z_w}{p^4}
=
a_\ell K+pB_\ell+p^2C_\ell\pmod{p^3},
$$


where $a_\ell=0$ for $\ell>20389$, and $B_\ell$ is a residue-weighted combination of the interface kernels.

Multiplying by (3.3), the order-$p$ part is


$$
p\,a_\ell K E_\ell.
$$


On the support of $a_\ell$, this is


$$
p\,a_\ell\beta_\ell K^2.
$$


Its completed sum is in $p^3$, by the lifted square divisibility.

The order-$p^2$ terms are


$$
p^2(a_\ell KQ_\ell+B_\ell E_\ell).
$$


Their completed sums are in $p^3$, by the weighted interface radical.

The physical terminal contributes only at a higher order. Therefore


$$
\boxed{Y\in p^5\mathbb Z_p^{b+1},\qquad
Z_w^TY\in p^{11}\mathbb Z_p,\qquad \kappa=0.}
\tag{3.5}
$$



This is an analytic consequence of the complete guarded response and radical theorems, not an extrapolation from the $5075$-row computation.

---

## 4. A stronger paid observation for short source directions

Let


$$
T_i=Le_i,\qquad 0\le i\le202.
$$



The retained guarded source-response theorem gives


$$
T_i\in p^3\mathbb Z_p^{b+1}.
$$


Its leading contact interface is $000$, supported on $\ell\le20389$, and its first correction is a residue-weighted combination of the $K_s$.

Using (3.3), the same calculation as in §3.4 now starts at physical order $p^{3+5}=p^8$:

- the leading product is an ordinary square, paid by two more powers of $p$;
- the next product is paid by one coefficient power and one radical power.

Thus


$$
\boxed{T_i^TY\in p^{10}\mathbb Z_p
\qquad(0\le i\le202).}
\tag{4.1}
$$



This improves the previously retained $p^9$ bound by one digit.

We will also use two elementary consequences of the same forms. If $U$ is any integral linear combination of $T_0,\ldots,T_{202}$, and


$$
Z_*=\frac12L\widehat f,
$$


then


$$
U\in p^3,\qquad Z_*\in p^4,
$$


and


$$
\boxed{Z_*^TU\in p^9\mathbb Z_p,\qquad U^TU\in p^8\mathbb Z_p.}
\tag{4.2}
$$



For example, $Z_*^TU$ begins at $p^7$. Its leading square is in $p^2$; its first-correction products have one explicit factor $p$ and one radical factor $p$. All remaining terms are already in $p^9$. The proof for $U^TU$ is identical, starting at $p^6$.

No positive-definiteness argument is used for these $p$-adic divisibilities.

---

## 5. Exact unit normalization of the actual first force

### 5.1 The recovered $\rho_n$

The independent definition is


$$
C_n=\operatorname{CT}(z^{-1}+2+2z)^n=f_0^0,
\qquad
\rho_n=\frac1{6C_n}.
$$


The established universal unit theorem gives


$$
C_n\in\mathbb Z_p^\times,\qquad \rho_n\in\mathbb Z_p^\times.
$$



Thus no negative-valuation branch is relevant here.

The identities


$$
C_n\equiv2C_q\equiv21C_W\pmod p
$$


are retained unit identities. They are not evaluations of the full original word.

Define


$$
\bar f=\frac{f^0}{C_n},\qquad
\bar Z=L\bar f=\frac{Z_w}{C_n}.
$$


Then


$$
\bar f_0=1
$$


exactly.

---

### 5.2 Removing the order-$p$ scalar ambiguity

Let


$$
h_i=
\begin{cases}
i!,&0\le i<29,\\
0,&i\ge29.
\end{cases}
$$


Choose the displayed flat representatives in the form


$$
\widehat f=2h+pt,
\qquad t_0=0.
\tag{5.1}
$$



The retained actual expansion is


$$
f^0=C_q\widehat f+p\delta_0h+p^2v+p^7w,
\tag{5.2}
$$


where $v$ is supported in $0,\ldots,202$.

At coordinate zero,


$$
C_n=2C_q+p\delta_0+p^2v_0+p^7w_0.
\tag{5.3}
$$



Set


$$
f_*=\frac{\widehat f}{2}=h+\frac p2t.
$$


Subtracting $C_nf_*$ from (5.2) gives the exact identity


$$
\boxed{\bar f=f_*+p^2\bar v+p^7\bar w,}
\tag{5.4}
$$


where


$$
\boxed{
\bar v=
\frac{v-v_0f_*-\frac{\delta_0}{2}t}{C_n},
\qquad
\bar w=\frac{w-w_0f_*}{C_n}.}
\tag{5.5}
$$



Both divisions are by the proved unit $C_n$. Moreover,


$$
\bar v_0=\bar w_0=0,
$$


and $\bar v$ is supported in $0,\ldots,202$.

This is a source-specific effect of the independent normalization: the order-$p$ direction $\delta_0h$ is removed, not merely renamed.

---

### 5.3 Evaluated normalized first relative digit

The supplied short array gives


$$
t_i=7i!(2H_i+14\xi_i+8\zeta_i)\pmod p
\qquad(0\le i<29),
$$


and


$$
t_{29+r}=24r!\pmod p
\qquad(0\le r<29).
$$



Consequently,


$$
\boxed{
\bar f_i\equiv
i!+\frac{7p}{2}i!(2H_i+14\xi_i+8\zeta_i)
\pmod{p^2}
\quad(0\le i<29),}
\tag{5.6}
$$


and


$$
\boxed{\bar f_{29+r}\equiv12p\,r!\pmod{p^2}
\quad(0\le r<29).}
\tag{5.7}
$$


For $i\ge58$,


$$
\bar f_i\equiv0\pmod{p^2}.
$$



For example,


$$
\bar f_{29}\equiv\bar f_{30}\equiv348\pmod{841}.
$$



This entire first relative digit is independent of a separately evaluated high unit $C_q$ or $C_W$.

The next normalized source digit is not determined by the flat array:


$$
\bar v\bmod p
=
\frac{v-v_0h-\frac{\delta_0}{2}t}{2C_q}\pmod p.
\tag{5.8}
$$


The sources do not evaluate this vector. Equation (5.8) identifies the exact missing relative combination; knowledge of $v$ without its zeroth-coordinate subtraction would be insufficient.

---

## 6. A new complete relative-defect identity through $p^{12}$

Define the normalized whole defect


$$
\Delta(\bar f)=6\bar Z^TY-p\,\bar Z^T\bar Z.
\tag{6.1}
$$


This is exactly the original defect divided by $C_n^2$:


$$
\Delta(\bar f)
=
\frac{6C_nZ_w^TY-pZ_w^TZ_w}{C_n^2}.
$$



Put


$$
Z_*=Lf_*,\qquad U=L\bar v,\qquad V=L\bar w.
$$


Equation (5.4) becomes


$$
\bar Z=Z_*+p^2U+p^7V.
\tag{6.2}
$$



The relevant paid bounds are


$$
Y\in p^5,\quad Z_*\in p^4,\quad U\in p^3,\quad V\in\mathbb Z_p^{b+1},
$$




$$
U^TY\in p^{10},\quad Z_*^TU\in p^9,\quad U^TU\in p^8.
\tag{6.3}
$$


The integrality of $V$ uses the retained integral finite inverse; no short-support assertion is made for $\bar w$.

Expanding the whole defect, without dropping its norm part, gives


$$
\begin{aligned}
\Delta(\bar f)-\Delta(f_*)
={}&6p^2U^TY+6p^7V^TY
-2p^3Z_*^TU-p^5U^TU\\
&-2p^8Z_*^TV-2p^{10}U^TV-p^{15}V^TV.
\end{aligned}
\tag{6.4}
$$



Every term on the right is in $p^{12}$. Therefore:

### Theorem 6.1 — Paid normalized flat-head identity
On every original index,


$$
\boxed{\Delta(\bar f)\equiv\Delta(f_*)\pmod{p^{12}},\qquad
f_*=\frac12\widehat f.}
\tag{6.5}
$$



This identity uses the complete actual $Y$, not merely its displayed coefficient-order-one dictionary.

In particular, the next mixed digit after the proved fixed-layer zero is invariant under the normalized discarded head directions:


$$
\boxed{
\frac{\bar Z^TY}{p^{11}}
\equiv
\frac{Z_*^TY}{p^{11}}\pmod p.}
\tag{6.6}
$$


Both divisions are paid by §3.4 and its application to $Z_*$.

Equation (6.5) is a genuine improvement over the previous observable flat-head statement. It is nevertheless a finite-depth identity. It does not assert alignment, because the right-hand side still has to be evaluated on the actual original word.

---

### 6.1 The next feedback digit exposes the original tail

Equation (6.4) also identifies precisely what happens one digit later. Divide by $p^{12}$, using the established divisibilities. The quadratic terms $p^5U^TU$, $p^{10}U^TV$, and $p^{15}V^TV$ disappear modulo $p$. Thus


$$
\boxed{
\begin{aligned}
\frac{\Delta(\bar f)-\Delta(f_*)}{p^{12}}
\equiv{}&
6\,\frac{U^TY}{p^{10}}
-2\,\frac{Z_*^TU}{p^9}\\
&+
V^T\left(6\,\frac{Y}{p^5}
          -2\,\frac{Z_*}{p^4}\right)
\pmod p.
\end{aligned}}
\tag{6.7}
$$



All divisions displayed in (6.7) are paid.

The last term,


$$
\boxed{
V^T\left(6Y/p^5-2Z_*/p^4\right)\pmod p,}
\tag{6.8}
$$


is an explicit contribution of the original $p^7$-tail after normalization. It cannot be omitted from the next relative digit merely because the tail was harmless for $\kappa$ or for (6.5).

This is the precise obstruction to promoting the finite flat-head identity by one more modulus. The packet supplies neither a proof that (6.8) vanishes nor its evaluated value.

---

## 7. Actual primitive depth and required normalized-source information

Write, as before,


$$
Z_w=p^{c+2}x,\qquad x^Tx=p^\nu\eta,
$$


with $x$ primitive at $p$ and $\eta$ a unit. Put


$$
d=2c+4+\nu,\qquad K=d-c=c+4+\nu.
$$



Since $C_n$ is a unit,


$$
\bar x=x/C_n
$$


is also primitive, and


$$
\bar x^T\bar x=p^\nu\bar\eta,\qquad
\bar\eta=\eta/C_n^2\in\mathbb Z_p^\times.
$$



The exact normalized primitive target is


$$
\boxed{
6\bar x^TY^{[K]}-p^{K-1}\bar\eta
\equiv0\pmod{p^K}.}
\tag{7.1}
$$


Equivalently,


$$
\Delta(\bar f)\equiv0\pmod{p^{d+2}}.
$$



The complete $Y^{[K]}$ remains the one supplied by the growing-depth theorem:

- symbol indices $0\le s\le p(K-1)$;
- exterior indices $0\le h\le p(K-1)+1$;
- the actual finite exterior solve and return;
- logarithmic head length
  

$$
L_{\log}(K)
  =\min\!\left(b,\ p\max\{K-N_{\log},0\}\right);
$$


- the physical terminal $W_be_b$.

Its error is already paid:


$$
\bar Z^T(Y-Y^{[K]})\in p^{d+2}\mathbb Z_p.
$$



### 7.1 A useful improved sufficient source budget

Suppose $\widetilde f$ approximates $\bar f$ modulo $p^a$. Since $L$ is integral, the reconstructed error is in $p^a$. Let


$$
y=v_p(Y)\ge5.
$$


A sufficient first-source budget for preserving the whole defect modulo $p^{d+2}$ is


$$
\boxed{
a\ge
\max\{c+2,\ d+2-y,\ d-c-1\}.}
\tag{7.2}
$$



Indeed, the mixed error is in $p^{a+y}$, the linear norm error in $p^{a+c+3}$, and the quadratic norm error is paid by $a\ge c+2$.

Using only the newly proved $y\ge5$, it is sufficient that


$$
a\ge\max\{c+2,\ d-3,\ d-c-1\}.
\tag{7.3}
$$


This saves one source-precision digit relative to the earlier bound using only $Y\in p^4$.

It does not bound $a$ uniformly on the original family.

### 7.2 What head data actually suffice

The normalized decomposition gives the following precise sufficiency statements.

- Modulo $p^2$, the $58$-entry normalized flat head suffices.
- At source precision $p^a$ with $3\le a\le7$, the additional required data are the relative vector
  

$$
\bar v_1,\ldots,\bar v_{202}\pmod{p^{a-2}}.
$$


  The zeroth coordinate is exactly zero.
- Above source precision $p^7$, the actual normalized tail must be retained unless a separate paid observation annihilates it.
- For the particular whole defect, Theorem 6.1 is stronger than this raw source budget: the flat head alone determines the defect modulo $p^{12}$.
- At the next defect digit, the additional information is exactly the paid combination in (6.7), not merely $C_n\bmod p$, not merely the first $58$ normalized entries, and not merely the unnormalized head correction.

No minimality claim beyond these proved sufficiency and obstruction statements is made.

---

## 8. Concrete follow-on obligation

The next substantive lemma should address the actual vectors in (6.7):

> **Normalized-source feedback lemma.**  
> For the original family, evaluate
> 

$$
> 6\,\frac{U^TY}{p^{10}}
> -2\,\frac{Z_*^TU}{p^9}
> +V^T(6Y/p^5-2Z_*/p^4)\pmod p,
>
$$


> where $U=L\bar v$ and $V=L\bar w$ are defined by the exact normalized decomposition (5.4)–(5.5). The evaluation must use the actual complete exponential/logarithmic force and finite return, and must establish any asserted tail cancellation rather than discard it.

For growing depth, an iterated version must retain the subsequent normalized-source digits and evaluate the completed defect at the actual $d+2$. A fixed value of $c$ is not assumed.

The present sources do not supply an evaluated $\bar v$, an evaluated normalized tail projection, or an all-depth feedback identity. Equation (6.7) identifies the exact first missing source term instead of hiding it in an unspecified contraction.

---

## 9. Bounded exact arithmetic: what is and is not needed

### 9.1 No repetition of the closed calculations

No new calculation is needed to verify:

- the analytic profile-zero proof in §2;
- the corrected $a_0=14$, $b_0^{\rm prof}=20$;
- the already checked central-unit table;
- the retained two-coordinate exterior values;
- the original $5075$-row coefficient certificate.

Those computations should not be repeated.

### 9.2 A bounded next complete-force lift

If a coefficient-level certificate for the next paid observation is desired, the following is a bounded new task.

To determine the relevant complete second-column response at physical precision $p^8$, the growing-depth theorem gives


$$
m_8=203,\qquad r_8=204.
$$


The exact finite inputs are:

1. $b,n\bmod p^9$;
2. $c_s(n)\bmod p^8$, $0\le s\le203$;
3. $z_h=(b+h)!/b!\bmod p^8$, $0\le h\le204$;
4. the $205\times205$ matrix
   

$$
C^{[8]}_{hk}
   =
   \sum_{s=0}^{203}c_s(n)
   \sum_{a=0}^{s}
   \binom{b+h}{s-a}\binom{-n}{a}
   \binom{-2n-a}{k+s-a-h}.
$$



The low inputs are uniformly bounded on the original family. Indeed,


$$
574312172=28p^5,
$$


so $u\equiv2\pmod{p^9}$ fixes $b\bmod p^9$, with representative specified by


$$
b\equiv3^{1397629859}\pmod{p^9},
\qquad n\equiv2001b\pmod{p^9}.
$$



The short symbol array can be extended by the exact recurrence


$$
c_{s+1}=(n+s)c_s
-s\left(n+\frac{s-1}{2}\right)c_{s-1},
\qquad c_0=1,\quad c_1=n.
$$



Expected verifiable outputs are:

- the exterior vector modulo $p^8$;
- the exact residual certificate
  

$$
C^{[8]}v^{[8]}-z\equiv0\pmod{p^8};
$$


- the reconstructed finite atom dictionary, with coefficient valuations and paid support bounds;
- explicit retention of the physical terminal.

Existing lower-precision solutions may be reused and lifted. This is not a proposal to redo the closed lower-order solves.

This calculation would certify a higher-order complete-force dictionary only. It would not evaluate the enormous original upper word, the normalized first-source residual, the final gcd, or an infinite-family accepting value.

---

## 10. All-prime arithmetic and the whole same-index error

The local normalization does not change the actual integer rows, their contents, or the least simultaneous clearer $d_B$. In particular, it is not an all-prime primitive normalization.

Retain


$$
\omega_j=\frac{(n+2)!}{(n+2-j)!},
\qquad
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2),
$$




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



At the same original index,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
\qquad
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$



At its retained scope, the signed-error theorem supplies eventual nonzero whole error and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$



An irrationality proof still requires an all-prime estimate for the actual $q_n$ giving


$$
0<|q_n\epsilon_n|\longrightarrow0
$$


on the **same infinite original indices**.

Neither a selected-prime alignment nor the new finite-depth feedback identity supplies that denominator estimate.

---

## 11. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| The three displayed second-column profiles vanish | **Analytically proved, branch by branch** |
| The $b+2$ reconstructed branch is accounted for | **Proved; its factor $j$ pays the missing low divisibility** |
| Coefficient-order-two omissions preserve those three zeros | **Proved at observable scope** |
| $Y\in29^5$, and $\kappa=0$ on the original family | **Derived from the analytic source audit and retained guarded radical theorems** |
| $T_i^TY\in29^{10}$, $0\le i\le202$ | **New paid observation bound** |
| $\rho_n=(6C_n)^{-1}$ is a unit | Established independent definition plus retained universal unit theorem |
| Exact normalized decomposition (5.4) | **Proved** |
| Normalized first relative head digit (5.6)–(5.7) | **Evaluated at finite source depth** |
| Whole normalized defect agrees with the flat-head defect modulo $29^{12}$ | **New proved finite-depth identity** |
| Next feedback digit, including normalized tail term (6.7) | **Exact paid identity; its value remains open** |
| Alignment at actual $K=c+4+\nu$ | Open |
| All-prime primitive denominator versus whole same-index error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

The principal new result is not merely a corrected interpretation of a table. It is the analytic chain


$$
\boxed{
g=d=e_{011}=0
\ \Longrightarrow\
Y\in29^5,\quad \kappa=0,\quad T_i^TY\in29^{10},
}
$$


followed by the source-specific normalized identity


$$
\boxed{
6(L\bar f)^TY-29\|L\bar f\|^2
\equiv
6(L(\widehat f/2))^TY
-29\|L(\widehat f/2)\|^2
\pmod{29^{12}}.
}
$$



The exact next obstruction is the paid feedback expression (6.7), especially the original normalized-tail contribution (6.8). At growing primitive depth, further actual source digits, the complete $K$-dependent return, and the logarithmic head must be retained.

Even an eventual resolution of that local alignment problem would leave the indispensable all-prime comparison between the actual primitive denominator and the nonzero whole error on the same infinite original indices. No unconditional proof or disproof of the irrationality of $e+\pi$ is obtained here.
