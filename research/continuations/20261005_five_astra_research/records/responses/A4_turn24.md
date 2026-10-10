> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 — fourth-carry completion and sixth-depth cross-audit

## Verdict and scope

The two audits pass, with the qualifications about primitive arithmetic stated below.

1. On the **same ternary domain**
   

$$
j>0,\qquad243\mid j,\qquad n=4^j+1,\qquad
   H=3^{h-1},\qquad 0<D=H-(n-2)<H/8748,
$$


   A1’s additional support covers and contractions are compatible with the actual block definitions. Combining them with the already established $A_{81}=0$ gives
   

$$
\boxed{T_6=0,\qquad \operatorname{rank}_{\mathbb F_3}T_6=0.}
$$


   The transported endpoint is nonzero and lies outside its image.

2. On the **original binary domain, without an additional subclass**
   

$$
b=9^r,\qquad n=4002b,\qquad r=18+32u,\quad u\ge0,
$$


   the new fixed-degree coefficient receipt, together with the carry arguments audited below, closes the remaining fourth-discrepancy calculation:
   

$$
\boxed{H-N\equiv0\pmod{32}.}
$$


   This conclusion does not assume or evaluate $N/16\bmod2$.

Neither conclusion bounds the unrestricted difference $\gamma-\alpha$, proves decay of the primitive evaluated forms, or decides irrationality of $e+\pi$.

---

## 1. Ternary cross-audit

Retain


$$
A=H-D,\quad d=\frac{3D}{2}-1,\quad
\nu=\frac D2-1,\quad m=\frac{A+1}{2},
$$




$$
r_1=\frac{H-1}{2},\qquad r_2=\frac{H/3-1}{2}.
$$


The columns are the actual monomial columns. HIGH is $d\le a\le m$, and the radical columns are


$$
z_i=y^i(y-1)^D,\qquad0\le i<\nu.
$$



### 1.1 Blocks and division precision

The actual definitions


$$
G=\begin{pmatrix}3L&3X\\3X^T&E\end{pmatrix},
\qquad
F=\frac{E-E_0}{3}-X_U^TL_U^{-1}X_U
$$


give


$$
\widehat E=E_0+3F.
$$


Thus A1 uses the correct LOW-unit correction and the correct single division by $3$. In particular, it does not replace $F$ by $(E-E_0)/3$.

The already audited force estimates apply unchanged:

* the factorial term is in $3^h\mathbb Z_3$ before division;
* the endpoint-subtracted depth-seven error remains in $3^7\mathbb Z_3[y]$ before division;
* the top coefficient vanishes in $X_U,L_U$ by the stated degree inequalities.

These errors cannot affect $F\bmod27$ or $V\bmod81$. The primitive unit stripped is still exactly $\lambda=L_n/3$.

### 1.2 The $Fe_d\bmod27$ cover

Write $w=Fe_d$. In the actual monic-division formula, quotient exponents range over $0\le l\le\nu$. At precision $3^q$, a surviving pole term can occur only at


$$
a=\frac{cH/3^t-1}{2}
-k\frac{H}{3^{q-t-1}}-l-\epsilon,
\qquad \epsilon\in\{0,1\}.
$$


In units $H/(2\cdot3^{q-1})$, its macroscopic numerator is


$$
c3^{q-1-t}-2k3^t,
$$


which is odd.

For $q=3$, intersection with HIGH therefore leaves the bands


$$
a=\frac{bH/9-1}{2}-l-\epsilon,
\qquad b=1,3,5,7,
$$


and the $b=9$ edge band. Since


$$
r_1-\nu=m,
$$


the last band intersects HIGH only at $m,m-1$. This verifies A1’s edge absorption; it does not require cancellation of pole partners.

At precision $9$, the interior bands are divisible by $3$. The surviving nonedge cover is the band at $r_2$, with the displayed quotient shifts. Thus the decomposition


$$
w=u+3v\pmod9
$$


has the claimed supports.

### 1.3 The $J\bmod9$ cover

Apply the same argument to $V\bmod81$, now with $q=4$ and $0\le i<\nu$. It gives odd half-grid bands


$$
\frac{bH/27-1}{2}-i-\epsilon,\qquad b=1,3,\ldots,25,
$$


plus the top edge.

The prescribed corner and $K$-band already lie in this cover. Subtracting them and dividing by $9$ cannot create support outside the cover: at an excluded entry, all three numerator terms are zero modulo $81$. This supplies the precision justification for A1’s assertion about division.

Again the possible top band is confined to the edge cover. No assumption about a missing cutoff partner is used.

### 1.4 Separation and edge terms

Below degree $H$, the inverse coefficient bands modulo $27$ are


$$
[kH/9,kH/9+D].
$$


The nonedge degrees in $KRw$ and $w^TRw$ have odd numerators in units $H/18$, whereas those inverse-band centers have even numerators. Their shifts are $O(D)$. The hypothesis $H>8748D$ leaves more than enough separation.

Likewise, for $KRJ^T\bmod9$, the candidate degree has an odd numerator in units $H/54$; the inverse bands modulo $9$ have centers at multiples of $18H/54$. These bands cannot meet.

The edge reductions are the exact finite-matrix identities


$$
Re_m=e_d,\qquad Re_{m-1}=e_{d+1}+Ae_d.
$$


They use the already established small-corner divisibilities, not an infinite convolution. The HIGH corner of $R$ kills edge–edge terms.

### 1.5 The additional $Fp_i\bmod9$ cover

Here


$$
p_i=y^{H/3+i}(y-1)^D,\qquad0\le i<\nu.
$$


The cover


$$
\operatorname{supp}(Fp_i\bmod9)
 \subseteq\{r_2-i,r_2-i-1,m\}
$$


passes the following finer check.

Modulo $9$, $B_H$ has its endpoint coefficients and possible interior coefficients at $H/3,2H/3$, the latter divisible by $3$.

* $X_Up_i$ has no selected coefficient in its finite LOW range.
* The $c_0E_0$ term has $c_0\equiv3\pmod9$. Its interior $B_H$-coefficients consequently disappear modulo $9$.
* In the linear top term, the $2H/3$-branch can enter HIGH only at $m$: its candidate position exceeds $m$ except at the last radical index.
* In the first lower layer, the endpoint branch gives $r_2-i$, and the linear factor shifts this by one.
* At depth one, the endpoint branches miss HIGH. Interior coefficients or the linear factor supply the additional factor $3$ that annihilates them modulo $9$.

Thus the extra $m$-entry has been retained correctly. Discarding it without the edge identities would not have been justified.

These covers prove all of A1’s stated modulo-$9$ contractions. For the last cubic contraction, writing $w=u+3v$ gives


$$
w^TRFRw
=(Ru)^TF(Ru)+6(Ru)^TF(Rv)\pmod9.
$$


The first term is killed by the small $F$-corner. In the second, the already established edge supports of $Fe_d,Fe_{d+1}\bmod3$ suffice. There is no missing $v^TRFRv$ term modulo $9$.

Consequently the combined result is


$$
A_9\equiv0\pmod{27},\qquad
A_{27}\equiv0\pmod9,\qquad A_{81}\equiv0\pmod3.
$$


The complete sixth identity therefore yields


$$
\boxed{T_6=0.}
$$



Its image is $\{0\}$. Since $D\ge6$, $\nu>0$, and


$$
((-1)^i)_{0\le i<\nu}\ne0,
$$


the actual transported endpoint lies outside that image.

**Arithmetic qualification.** This audit establishes the zero sixth form. It does not independently establish a new global cofactor normalization formula. The explicit numerical bound already supported by the supplied normalization interface remains


$$
v_3(g)\ge d+5\nu=4D-6.
$$


I do not infer an additional numerical gcd exponent merely by naming the sixth rank.

---

## 2. Binary coefficient-transfer audit

Use the notation of A5turn17:


$$
b=128D+81,\quad n=128C+66,\quad
C=4002D+2532,
$$




$$
D\ \text{odd},\quad C\equiv2\pmod4,
$$




$$
m=32D+20,\quad M=32C+17,\quad h=64C+33.
$$



The receipt certifies coefficient identities only. In particular, it does not substitute bounded values into


$$
\mathcal M_v(j)=
\binom{2n+b-1-j}{b-1-j-v}.
$$



### 2.1 Why bounded coefficient verification applies

For any integral Newton polynomial,


$$
v_2\!\left(\binom{x+\delta}{a}-\binom xa\right)
\ge v_2(\delta)-\lfloor\log_2a\rfloor.
$$


This follows from Vandermonde and


$$
\binom{\delta}{k}=\frac{\delta}{k}\binom{\delta-1}{k-1}.
$$


The estimate is uniform in $x$, including arbitrarily large $x$.

Here


$$
v_2(n-66)=v_2(128C)=8,
\qquad
v_2(2n-132)=9.
$$


For bounded lower indices at most $22$, the maximum loss is four bits. Thus the moment coefficients involving $2n$ retain at least five bits under replacement by $132$. The coefficients of $Q^\#$ are all even, supplying the sixth bit when it is needed modulo $64$. The smaller precisions $8,4,16$ in the off-pair receipt are therefore covered with margin.

The $j$-translation must be checked with its Newton coefficients, not from degree alone. The supplied vectors give:

* odd coefficients of $P^\#$ occur only through degree $3$;
* its coefficients in degrees $5,6,7$ are divisible by $4$;
* its coefficients in degrees $9,10,11$ are divisible by $8$;
* all higher coefficients vanish at the retained modulus;
* the analogous $Q^\#$ coefficients have at least the extra divisibility visible in its supplied vector.

Vandermonde with $64\mid\delta$ therefore gives the required periodicity. Multiplication by $j$ in reconstruction preserves it, since the change in that multiplier is itself divisible by $64$.

The formal reconstruction degree is at most $22$. Degree alone would give only a two-bit guarantee for translation by $64$; the displayed coefficient divisibilities are essential. This is precisely why the new receipt is sufficient whereas an unweighted “degree at most $22$” assertion would not be.

The large $\mathcal M_v(j)$ remain unchanged throughout. The receipt consequently supplies valid coefficient identities for (45), (53), (55), (57), and the exceptional $\mathcal M_4$ coefficient on every actual index.

---

## 3. Unbounded even carry classes

For these checks, use Kummer in its exact form


$$
v_2\binom ab=s_2(b)+s_2(a-b)-s_2(a).
$$


Equivalently, count subtraction borrows. High digits may introduce additional borrows; the low-digit arguments below only assert lower bounds.

### 3.1 $j=4k+2$

The exact weight depth is


$$
v_2(W_j)=1+v_2\binom{M-1}{k}.
$$



At weight depth one, Lucas forces


$$
k=32t\ \text{or}\ 32t+16,\qquad \binom Ct\text{ odd}.
$$


Because $C$ is even, $t$ is even, so $d=D-t$ is odd. Hence


$$
\ell=m-k=32d+20\ \text{or}\ 32d+4.
$$


Adding $h$ to $\ell-1$ produces the two low carries and the separate bit-$5$ carry. Therefore $\mathcal M_0=B$ has depth at least three. The adjacent indices in certified formula (45) have the lower bounds


$$
v_2(\mathcal M_{-1}),v_2(\mathcal M_2),
v_2(\mathcal M_3)\ge3,\qquad
v_2(\mathcal M_4)\ge2.
$$


Every term of (45) consequently vanishes modulo $8$.

At weight depth two, the low residues of $k$ are $0,8,16\bmod32$. Each gives $\ell-1\equiv3\pmod4$, hence two carries. At weight depth three, $k$ is even, so $\ell-1$ and $h$ are odd and give one carry. Larger weight depth needs no additional carry.

After the division by $2$ in $X_j$, these cases all yield


$$
8\mid X_{4k+2}.
$$



### 3.2 $j=4k$

Here


$$
v_2(W_j)=v_2\binom Mk,\qquad
D_j^P\equiv-2(k+1)B\pmod8.
$$



The low-digit subtraction from $M\equiv17\pmod{32}$ gives the following exhaustive surviving even residues:



$$
\begin{array}{c|c}
v_2(W_j)&\text{residues potentially contributing to }X_j/4\\ \hline
1&k\equiv8\pmod{32}\\
2&k\equiv8,24\pmod{32}\\
\ge3&\text{none}
\end{array}
$$


The other depth-two even residues $4,12$ require an odd higher weight binomial. Its upper parameter $C$ is even, so the higher lower index is even; $D-t$ is odd and supplies the additional bit-$5$ carry in $B$. Odd $k$ are eliminated by the combined factors $k+1$ and $B$.

At weight depth zero off the prescribed pairs,


$$
k=32t+1\ \text{or}\ 32t+17,\qquad \binom Ct\text{ odd}.
$$


Thus


$$
\ell=32(D-t)+19\ \text{or}\ 32(D-t)+3,
\qquad D-t\text{ odd}.
$$


For the actual moments $-1\le v\le11$, subtraction gives depth at least three except possibly $v=4$, where it gives depth at least two. The receipt verifies that all reconstruction coefficients are even and the $\mathcal M_4$-coefficient is divisible by $8$. Hence $D_j^P\in16\mathbb Z_2$.

This proves


$$
8\mid X_j\qquad(j\text{ even},\ 32\nmid j).
$$



The residual even positions $j\equiv32\pmod{64}$ are handled by the already established sampled difference at precision $32$:


$$
\eta_j-2\theta_j\in16\mathbb Z_2.
$$


Since $W_j$ is even and the reconstruction term multiplied by $j$ is in $32\mathbb Z_2$,


$$
Y_j-X_j\in8\mathbb Z_2.
$$


Together with $4\mid X_j$, this kills their fourth-defect contribution.

Thus the **entire off-pair even contribution is zero modulo $32$**.

---

## 4. Odd carries and cancellation

The established $8\mid X_j$ permits


$$
\frac{X_j(Y_j-X_j)}{16}
\equiv \frac{X_j}{8}\frac{Y_j}{2}\pmod2.
$$


The weight depth is


$$
v_2(W_j)=2+v_2\binom{M-1}{k},
\qquad j=4k+1\text{ or }4k+3.
$$



Depth at least four gives $4\mid Y_j$, so only depths two and three remain.

### Depth two

The same Lucas argument gives $k=32t,32t+16$, with $t$ even and $d=D-t$ odd.

For $j\equiv1\pmod{64}$, the certified coefficient identities (53) and (55), followed by their odd-denominator adjacent-binomial ratios, give


$$
D_j^P\equiv2\frac hT B\pmod8,\qquad
D_j^Q\equiv\frac hT B\pmod4.
$$


Here $h/T$ is a unit and $B$ is even. Therefore the defect is $B/2\bmod2$.

For the two indices


$$
128t+1,\qquad128t+65,
$$


the low blocks introduce no differing carry. Their common higher binomial is


$$
\binom{2C+1+d}{d}.
$$


Consequently $B/2\bmod2$ agrees for the two positions, and their defects cancel.

For $j\equiv3\pmod{64}$, the upper argument in (57) is $17\bmod64$, and the five lower arguments are $14,13,12,11,10\bmod64$. The first has at least three borrows, the next three at least two where required, and the last at least one. With the coefficients in (57), every term vanishes modulo $8$. These defects vanish individually.

### Depth three

The possibilities are exactly:

* $k=32t+8$, with odd higher weight binomial;
* $k=32t,32t+16$, with higher weight binomial of depth one.

In the first case the bit-$5$ overlap makes the relevant $Q$-parity even; thus $4\mid Y_j$. In the second, the $a=3$ positions again vanish. At $a=1$, the lower reconstruction identities give the defect $B\bmod2$. The two shifted positions have identical higher-binomial parity and cancel.

All shifted pairs have $0\le t\le D$; both members are strictly below $b$. No terminal partner is missing.

The full endpoint retains


$$
Y_b=\frac{W_b(1+b\eta_{b-1})}{4}.
$$


The already checked $v_2(W_b)\ge6$ gives


$$
v_2(X_b)\ge5,\qquad v_2(Y_b)\ge4.
$$


Its contribution vanishes without deleting the endpoint $1$.

---

## 5. Completed binary conclusion and primitive bookkeeping

Combining the previously audited paired contribution with Sections 3–4,


$$
\boxed{
H-N=\sum_{j=0}^{b}X_j(Y_j-X_j)\equiv0\pmod{32}.
}
$$



The actual columns and metric remain


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},
\qquad
\Omega=\operatorname{diag}\bigl((n+2)_{\underline j}^{\,2}\bigr)_{0\le j\le b}.
$$


The complete force and seven-boundary lift are unchanged. The new coefficient receipt is not used to evaluate any unbounded binomial by finite sampling.

For the actual cleared columns $N_B=d_B[u,v]$, retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad p_n=\frac{H_B}{g_B}.
$$


The primitive multiplier relative to the uncleared quadratic form is $d_B^2/g_B$. In particular,


$$
v_2(q_n)=
\max\!\left\{0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)\right\}.
$$



The result permits


$$
\alpha=\gamma=4\quad\text{or}\quad\alpha,\gamma\ge5;
$$


it does not select an alternative.

Within the retained complete signed-error theorem,


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
$$


eventually, where


$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


This is the whole evaluated error and its conditional eventual nonvanishing, not a selected forcing term.

For the ternary determinant family, separately,


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),\qquad
q=\frac{|B_{\rm det}|}{g},
$$


and, when $B_{\rm det}\ne0$,


$$
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})\ell^{(n+1)/2}}{g}
 \det H_{\rm complete}.
$$


The multiplier remains $\ell^{(n+1)/2}/g$. Sixth rank zero establishes neither response nonvanishing nor nonvanishing of this whole determinant error.

---

## Closing ledger

### (1) New result and proof status

* **Cross-audit passed:** A1’s actual $Fe_d\bmod27$, $J\bmod9$, and $Fp_i\bmod9$ covers, including precision after division, finite HIGH intersections, and edge contractions.
* **Combined sixth theorem:** $T_6=0$, rank zero, transported endpoint outside its image, on the exact SAME243 domain.
* **Binary audit completed:** the new coefficient receipt transfers at the required weighted precisions; the unbounded carry classes and shifted cancellations give $H-N\equiv0\pmod{32}$ on every $r=18+32u$, with no additional subclass.
* No value of $N/16$, unrestricted-depth alignment, or irrationality conclusion is assumed.

### (2) Exact remaining bottleneck

The arithmetic bottleneck remains control of the **actual reduced denominator after the final gcd**, on the same indices as a nonzero whole-error estimate. In the binary interface this includes control of $\gamma-\alpha$ beyond finitely many aligned digits. In the ternary family it also requires an explicitly justified passage from further residual divisibility to the final coefficient-pair content.

These finite-depth results do not supply an infinite sequence of nonzero primitive forms tending to zero.

### (3) Computation request

None for these two audits. The supplied fixed-degree receipt closes the bounded coefficient gap. A further finite rank or growing-binomial scan would not resolve the remaining unrestricted-depth arithmetic assertion.
