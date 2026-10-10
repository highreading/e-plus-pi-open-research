> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The next ternary return: a complete finite-block cancellation and the remaining projection digit

## Abstract

The information gap from Turn 17 can now be resolved. **A4 Turn 15’s boundary-column extension is valid under the corrected-column support hypotheses used in A1 Turn 12.** In particular, its use of the nonterminal adjoining column, its exclusion of the unit-weight pole, and its higher-order support inequalities are compatible with the original finite boundaries. Thus the following are closed at their stated precision:


$$
(\bar L_ce_0)_u=[y^{E-\ell-u}](1-y)^{-b},
\qquad
G^T\bar L_ce_0=0,
$$


and


$$
G^T(\mathcal S^{(2)}_{\rm act}-\mathcal S^{(2)}_c)G\in81M.
$$



This report advances beyond that single boundary column. The same original support estimates, with additional finite-boundary checks, evaluate **every nonterminal column of the actual $K$-to-$J$ core coupling**:


$$
\boxed{
(\bar L_c)_{u,v-\ell}
=[y^{E-u-v}](1-y)^{-b},
\quad
0\le u<\ell,\quad \ell\le v\le\tau-2.
}
\tag{A}
$$


Consequently, the complete radical coupling is supported only at the physical terminal:


$$
\boxed{
G^T\bar L_c=\gamma_c\delta_J^T,
}
\tag{B}
$$


where $\gamma_c=G^T\bar L_c\delta_J$ is the actual, retained terminal column—not a column inferred from its unit status.

Using the already evaluated finite inverse direction


$$
\bar B^{-1}\delta_J=-e_0,
\qquad
\delta_J^T\bar B^{-1}\delta_J=0,
$$


one obtains a new complete pairing:


$$
\boxed{
27G^TL_\alpha B_\alpha^{-1}L_\alpha^TG\in81M,
\qquad \alpha\in\{c,\mathrm{act}\}.
}
\tag{C}
$$


Thus **each first-radical matrix return vanishes separately at normalized order $27$**. Previously, only their producer difference had been shown to vanish there. The endpoint returns do not vanish by this argument.

A second new calculation evaluates the complete uncorrected core pairing on the radical combinations:


$$
\boxed{
G_c(Z_G,Z_G)\in3^{30}M,
\qquad
(Z_G)_a=x^{D+b}y^{R_*+a},\quad 0\le a\le b/2.
}
\tag{D}
$$


This uses the complete finite moment sum through precision $30$, with its factorial term paid. It is not a statement about the corrected columns.

Together, these results locate the next unresolved digit more sharply: it is an actual LOW/HIGH-plus-prefix projection digit, not an unpaid first-radical matrix return. That projection digit is not evaluated here. In particular, this report does **not** complete the entire next radical operator, prove the final directional inverse bound, or establish irrationality of $e+\pi$.

---

## 1. Original domain and objects

All assertions below concern sufficiently large indices in the unchanged original family


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


subject to


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



The fixed accepted subwindow is


$$
\boxed{
\frac{103}{1000}<\frac{N_0}{P_0}<\frac{104}{1000}.
}
\tag{1.1}
$$


We retain


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$


and, importantly, the original relation


$$
4^j=243(3^{26}-1)P-243r+1.
\tag{1.2}
$$


The accepted density result is used only to supply infinitely many original indices in this fixed subwindow.

Put


$$
x=y-1,\qquad Q=\frac{P_0}{9},\qquad b=Q-N_0.
$$


Then


$$
D=10Q-b,
\qquad
\frac{64}{1000}<\frac bQ<\frac{73}{1000},
\tag{1.3}
$$


and $b$ is an even positive multiple of $243$.

The finite coordinates remain


$$
U_s=x^s\quad(0\le s<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_t=y^t\quad(d\le t\le m),
\qquad
\nu=\frac D2-1,\qquad d=D+\nu.
$$


The physical HIGH terminal is $Y_m$.

The residual indices are


$$
R_*=\frac{P_0+1}{2},\qquad
\tau=\frac{N_0-3}{2},\qquad
\ell=\frac{3b}{2}+1,
$$




$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\},
$$




$$
n_J=\tau-\ell=\frac{Q-4b-5}{2},
\qquad E=\frac{Q-3}{2}.
\tag{1.4}
$$


A tail index $v$ means the original middle index $R_*+v$. The last tail index $v=\tau-1$ is the terminal middle direction.

### 1.1 Complete core

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!,
\tag{1.5}
$$


on polynomials of degree at most $2n-1$. The largest pole denominator is exactly


$$
4n-3=4H-4D+5<3^{h+1}.
$$


Thus


$$
\mathcal M\bigl(\mathbb Z_3[y]_{\le2n-1}\bigr)\subseteq\mathbb Z_3.
\tag{1.6}
$$



The complete core form is


$$
G_c(f,g)=\mathcal M(Q_cfg),
\qquad
Q_c=(y+1)x^A(\beta+3y),
\qquad \beta=-71-A.
$$



With $W=[U\ Y]$, write


$$
E_c=G_c(W,W),\qquad C_i=G_c(W,z_i),
$$




$$
F_i=z_i-WE_c^{-1}C_i.
\tag{1.7}
$$


These are the exact corrected columns:


$$
G_c(W,F)=0,\qquad S_c=G_c(F,F).
$$



We reuse the accepted facts that $[W,F]$ is integral unimodular,


$$
E_c^{-1},E_{\rm act}^{-1}\in3^{-1}M,
\qquad S_c\in3^{26}M,
$$


and that the precision-$20$ representatives have the supplied support bounds and strict degree gap.

---

## 2. Audit of A4’s adjoining-column proof

Turn 17 correctly recorded that A4 Turn 15 was not among its supplied sources. It did not thereby disprove A4’s theorem. With the missing section now supplied, the extension can be checked directly.

### 2.1 The column is genuinely nonterminal

The adjoining column is


$$
j_0=R_*+\ell.
$$


Since


$$
\nu-1=R_*+\tau-1,
$$


we have


$$
(\nu-1)-j_0=n_J-1.
$$


For sufficiently large original indices, $n_J\ge2$, so


$$
j_0\le\nu-2.
\tag{2.1}
$$


It therefore has the same zero order-one jet as the columns used in the original H2 calculation.

### 2.2 The representative substitution is paid

For a precision-$20$ representative, write


$$
F_i^*=F_i+3^{20}\Delta_i,
\qquad \deg\Delta_i\le m.
$$


Exact orthogonality and the integral unimodular basis imply


$$
G_c(F_i,\Delta)\in3^{26}\mathbb Z_3
\quad\text{for every integral }\deg\Delta\le m.
\tag{2.2}
$$


Hence


$$
\begin{aligned}
G_c(F_i^*,F_j^*)-G_c(F_i,F_j)
={}&3^{20}G_c(F_i,\Delta_j)
+3^{20}G_c(\Delta_i,F_j)\\
&+3^{40}G_c(\Delta_i,\Delta_j)
\in3^{40}\mathbb Z_3.
\end{aligned}
\tag{2.3}
$$


This is the correct stationarity payment. No precision-$20$ approximation is being inserted into an uncontrolled mixed pairing.

### 2.3 The support comparisons remain valid

For $0\le u,v\le\ell$, the low polynomial used in the moment evaluation has degree at most


$$
19Q+2b+4.
$$


Since


$$
2D=20Q-2b,
$$


the required inequality is


$$
4b+4\le Q,
$$


which holds with a growing margin under (1.3).

The order-three terms have one raw factor and one higher digit. The strict degree gap, together with nonterminality, excludes the unit-weight pole. The remaining support comparisons are precisely the ones used in Turn 12:


$$
\frac72D+3<\frac{9P_0-1}{2},
\qquad
4D+3<\frac{9P_0-1}{2}.
\tag{2.4}
$$


Indeed,


$$
\frac72(1.104)<4.5,\qquad 4(1.104)<4.5.
$$


Higher-order grids increase geometrically while the support widths increase only linearly, as in the accepted corrected-column argument.

There is therefore no failed support inequality in this one-column extension.

### 2.4 Decision

The following conclusions are accepted at their stated first digit:


$$
\boxed{
(\bar L_ce_0)_u=[y^{E-\ell-u}](1-y)^{-b},
\qquad
G^T\bar L_ce_0=0.
}
\tag{2.5}
$$


Here $G$ has columns


$$
g_a=x^by^a,\qquad 0\le a\le b/2,
\tag{2.6}
$$


in the $K$-coordinates.

Consequently, the complete first producer matrix return is paid modulo $81$:


$$
\boxed{
G^T(\mathcal S^{(2)}_{\rm act}-\mathcal S^{(2)}_c)G\in81M.
}
\tag{2.7}
$$



The raw adjoining strip and Turn 17’s prefix selector need not be recalculated.

---

## 3. New theorem: every nonterminal $J$-column is evaluated

The adjoining-column proof extends farther than one column, but this requires new boundary checks. In particular, near the far end of $J$, some exclusions have a fixed positive margin rather than a growing one. Those margins must be computed exactly.

### Theorem 3.1 — Complete nonterminal coupling strip

For the actual core coupling $L_c=\mathcal R_{c,KJ}/9$,


$$
\boxed{
(\bar L_c)_{u,v-\ell}
=[y^{E-u-v}](1-y)^{-b},
\quad
0\le u<\ell,\quad \ell\le v\le\tau-2.
}
\tag{3.1}
$$



This theorem does not include the terminal column $v=\tau-1$.

### Proof

Let


$$
i=R_*+u,\qquad j=R_*+v,
\qquad s=u+v.
$$


Both columns are nonterminal. Their first two relevant jets are therefore


$$
F_i\equiv x^D(y^i-9y^{H/3+i})\pmod{27},
$$


and similarly for $F_j$.

#### Step 1: corrected-column comparison

The enlarged range satisfies


$$
s\le(\ell-1)+(\tau-2)
=\frac Q2+b-\frac72.
\tag{3.2}
$$


The low polynomial $x^D(\beta+3y)y^{i+j}$ has degree at most


$$
D+1+i+j
=19Q-b+2+s
\le\frac{39Q-3}{2}<2D.
\tag{3.3}
$$



The order-two shifted moment is governed by the same complete shifted formula as in Turn 12. Its principal coefficient index is


$$
k=\frac{9Q-3}{2}-s.
\tag{3.4}
$$


Throughout this strip,


$$
k\ge4Q-b+2>N_0,
\qquad k<9Q=P_0.
\tag{3.5}
$$


Thus its reduction lies in the characteristic-$3$ gap of $x^D$.

For total order three, the unit pole remains absent: each term has a raw nonterminal factor, and the other factor has the accepted strict degree gap. The remaining support width is bounded by the same global $\frac72D+O(1)$ estimate used in Turn 12. Total order four uses the same $4D+O(1)$ bound. These estimates were stated for the original corrected columns; moving within the nonterminal middle range does not enlarge the global bounds. Inequalities (2.4) therefore apply. Higher orders are paid by the accepted growing grids.

Together with (2.3), this proves


$$
(S_c)_{ij}\equiv G_c(z_i,z_j)\pmod{3^{29}}
\tag{3.6}
$$


on the whole displayed strip.

#### Step 2: complete moment extraction

Reuse the complete moment formula modulo $3^{29}$ from Turn 12. At the principal extraction, (3.5) gives


$$
k\ge 3Q+N_0+2.
\tag{3.7}
$$


Thus the band beginning at $3Q$ ends at least two positions before $k$; the one-step shift associated with $3y$ still misses it.

Modulo $27$, the only remaining band that can contribute is the band beginning at $4Q$. Therefore


$$
\frac{(S_c)_{ij}}{3^{28}}
\equiv[y^{E-u-v}]x^{N_0}\pmod3.
\tag{3.8}
$$



The other moment extractions remain excluded. Their exact lower bounds at the far end are useful:

- the $a=7$ extraction is at least $N_0+2$;
- the $a=11$ extraction stays strictly between $N_0$ and $P_0$;
- the $a=13$ extraction is at least $D+2$;
- the $a=1,3,5$ extractions are below the polynomial’s support.

These are exclusions in the actual finite coefficient ranges.

#### Step 3: prefix-to-$J$ digit

Let the prefix index be $0\le p\le a_0$, where


$$
a_0=\frac{P_0-1}{2},\qquad J_0=\frac{P_0}{3}-1.
$$


At precision $28$, the corrected-column comparison is again paid. The order-two terms already contribute $3^2$ times a moment divisible by $3^{26}$; the higher terms are excluded by the support grids.

The principal coefficient index is


$$
P_0-1-p-v.
$$


Its minimum over the present range is


$$
4Q+\frac b2+3,
$$


which is greater than $3Q+N_0=4Q-b$. It is also below $P_0$. Hence, modulo $9$, only the band beginning at $2P_0/3=6Q$ can contribute. This gives the actual divided cross-column


$$
(\mathsf B_1)_{p,v}
=[y^{J_0-p-v}]x^{N_0},
\qquad \ell\le v\le\tau-2.
\tag{3.9}
$$



#### Step 4: finite prefix correction

Using the accepted finite prefix inverse, the complete convolution is


$$
(\mathsf B_1^T\mathsf A_0^{-1}\mathsf B_1)_{u,v}
=[y^{C-u-v}](1-y)^{N_0},
\qquad C=\frac{3Q-3}{2}.
\tag{3.10}
$$


The finite bounds are the original prefix bounds; nonnegative coefficient indices force every contributing summand into those bounds.

By (3.2),


$$
C-u-v\ge N_0+2.
\tag{3.11}
$$


Thus (3.10) is zero on this entire strip.

Combining (3.8), the sign $U_c=-S_c/3^{26}$, and the zero prefix correction gives


$$
(\bar L_c)_{u,v-\ell}
=-[y^{E-u-v}]x^{N_0}.
$$


Since the extraction is below $Q$,


$$
-x^{N_0}=(1-y^Q)(1-y)^{-b}
$$


gives (3.1). ∎

---

## 4. New complete radical return pairing

Theorem 3.1 has a stronger consequence than the single boundary cancellation.

### 4.1 Only the actual terminal can remain

For $g_a=x^by^a$, $0\le a\le b/2$, and a nonterminal $v\in J$,


$$
\begin{aligned}
g_a^T\bar L_{c,\cdot,v-\ell}
&=[y^{E-v}](1-y)^{-b}x^by^a\\
&=[y^{E-v}]y^a.
\end{aligned}
\tag{4.1}
$$


Here $b$ is even. Moreover,


$$
E-v\ge E-(\tau-2)=\frac b2+2>a.
$$


Therefore every such contraction is zero.

Let


$$
\delta_J=e_{n_J-1},
\qquad
\gamma_c:=G^T\bar L_c\delta_J.
\tag{4.2}
$$


This is an exact definition of the retained terminal residue. We have proved


$$
\boxed{
G^T\bar L_c=\gamma_c\delta_J^T.
}
\tag{4.3}
$$



No value of $\gamma_c$ is inferred from leading units, and the terminal column has not been replaced by a nonterminal continuation.

### 4.2 Transfer to the actual producer

The accepted first producer digit gives


$$
\bar L_{\rm act}
=\bar L_c+\bar\kappa\,\bar t_K\delta_J^T,
$$


where


$$
t_i=\frac{[y^m]F_i}{3^{20}}
$$


is the actual terminal-coefficient vector.

Set


$$
\widehat t=G^T\bar t_K,
\qquad
\gamma_{\rm act}=\gamma_c+\bar\kappa\,\widehat t.
\tag{4.4}
$$


Then


$$
\boxed{
G^T\bar L_{\rm act}=\gamma_{\rm act}\delta_J^T.
}
\tag{4.5}
$$



### 4.3 The full matrix return is evaluated

The exact first-radical reductions are


$$
\mathcal R_{\alpha,JJ}=3B_\alpha,\qquad
\mathcal R_{\alpha,KJ}=9L_\alpha,
$$




$$
\mathcal S^{(2)}_\alpha
=\mathcal R_{\alpha,KK}
-27L_\alpha B_\alpha^{-1}L_\alpha^T.
\tag{4.6}
$$


The inverse cost is exactly $3^{-1}$.

The already proved physical-terminal identities are


$$
\bar B^{-1}\delta_J=-e_0,
\qquad
\delta_J^T\bar B^{-1}\delta_J=0.
\tag{4.7}
$$


Hence, for either $\alpha=c$ or $\alpha=\mathrm{act}$,


$$
\begin{aligned}
\overline{G^TL_\alpha B_\alpha^{-1}L_\alpha^TG}
&=\gamma_\alpha
\bigl(\delta_J^T\bar B^{-1}\delta_J\bigr)
\gamma_\alpha^T\\
&=0.
\end{aligned}
$$


We have obtained the new complete pairing


$$
\boxed{
27G^TL_\alpha B_\alpha^{-1}L_\alpha^TG\in81M.
}
\tag{4.8}
$$



This is not merely another expression for an unknown pairing: its residue has been evaluated as zero using the newly proved support of the actual finite coupling.

Equivalently,


$$
\boxed{
G^T\mathcal S^{(2)}_\alpha G
\equiv G^T\mathcal R_{\alpha,KK}G\pmod{81}.
}
\tag{4.9}
$$



### 4.4 The associated finite inverse direction

The exact first-radical displacement of these columns is


$$
\mathcal R_{\alpha,JJ}^{-1}\mathcal R_{\alpha,JK}G
=3B_\alpha^{-1}L_\alpha^TG.
$$


Its first nonzero possible digit is therefore


$$
\boxed{
\mathcal R_{\alpha,JJ}^{-1}\mathcal R_{\alpha,JK}G
\equiv-3e_0\gamma_\alpha^T\pmod9.
}
\tag{4.10}
$$


This localizes the actual displacement to the first finite $J$-coordinate. It is a statement about this paid $J$-solve, not a bound for the eventual block $C^{-1}z$.

---

## 5. Endpoint and diagonal returns are not canceled

The matrix cancellation in (4.8) does not remove the other channels.

Retain exactly


$$
f^{(2)}_\alpha
=f_{\alpha,K}-3L_\alpha B_\alpha^{-1}f_{\alpha,J},
\tag{5.1}
$$




$$
\lambda^{(2)}_\alpha
=\lambda_\alpha-\frac13f_{\alpha,J}^TB_\alpha^{-1}f_{\alpha,J}.
\tag{5.2}
$$



Let


$$
\varepsilon_0=(-1)^{R_*+\ell}.
$$


The accepted unit contraction is


$$
\delta_J^T\bar B^{-1}\bar f_J=-\varepsilon_0.
$$


Thus the newly localized coupling gives


$$
\boxed{
G^Tf^{(2)}_\alpha
\equiv G^Tf_{\alpha,K}
+3\varepsilon_0\gamma_\alpha\pmod9.
}
\tag{5.3}
$$


In particular, an unevaluated terminal amplitude remains in the endpoint channel even though its quadratic matrix return is zero.

The producer differences remain


$$
f^{(2)}_{\rm act}-f^{(2)}_c
\equiv3\bar\kappa\varepsilon_0\bar t_K\pmod9,
\tag{5.4}
$$




$$
\lambda^{(2)}_{\rm act}-\lambda^{(2)}_c
\equiv
-2\bar\kappa\varepsilon_0(\bar t_J^Tu_0)\pmod3,
\qquad u_0=\bar B^{-1}\bar f_J.
\tag{5.5}
$$


The complete diagonal valuation


$$
v_3(\lambda^{(2)})=-1
$$


is retained. No assertion about a final scalar follows from the matrix cancellation alone.

The subsequent rank-$b$ elimination still costs $3^{-2}$. Its matrix return on the radical begins at


$$
3^3\cdot3^{-2}\cdot3^3=3^4,
$$


so it does not alter the normalized order-$27$ matrix digit. Its endpoint and diagonal effects must nevertheless be retained in their exact formulas.

---

## 6. A new complete raw radical pairing through precision $30$

The preceding theorem pays the first-radical return. We can also evaluate the complete **uncorrected** core pairing on the radical combinations at the next precision.

Define


$$
(Z_G)_a=\sum_{u<\ell}(g_a)_u z_{R_*+u}
=x^{D+b}y^{R_*+a},
\qquad 0\le a\le b/2.
\tag{6.1}
$$



### Theorem 6.1


$$
\boxed{
G_c((Z_G)_a,(Z_G)_c)\in3^{30}\mathbb Z_3
\quad(0\le a,c\le b/2).
}
\tag{6.2}
$$



This theorem concerns the actual complete functional applied to specified original polynomials. It does not yet include their LOW/HIGH or prefix projections.

### 6.1 Complete moment formula at precision $30$

For $0\le s\le2D$, reuse the exact finite partial-fraction evaluation


$$
L_s=\mathcal M((y+1)x^Hy^s)
\equiv
-\frac{3^h2^HH!}{\prod_{k=0}^{H}(2s+1+2k)}
\pmod{3^{30}}.
\tag{6.3}
$$


The factorial part vanishes modulo $3^{30}$ only because its retained factor $3^h$ pays that precision.

For the rational expression in (6.3),


$$
v_3(L_s)=h-v_3(2s+1),
$$


and


$$
U_s:=\frac{(2s+1)L_s}{3^h}
=U_0\prod_{j=1}^s
\left(1+\frac{2H}{2j+1}\right)^{-1}.
\tag{6.4}
$$


On the present original window, every product factor is $1\pmod{81}$.

Also, for sufficiently large powers $H$ of $3$,


$$
4^H\equiv1\pmod{81},\qquad
\binom{2H}{H}\equiv20\pmod{81},\qquad
2H+1\equiv1\pmod{81}.
$$


Thus


$$
U_0=-\frac{4^H}{(2H+1)\binom{2H}{H}}
\equiv-\frac1{20}\equiv4\pmod{81}.
\tag{6.5}
$$


The binomial congruence follows by separating multiples of $3$; the base $\binom{18}{9}=48620$ is $20\pmod{81}$, the step at $H=27$ has unit-reciprocal sum zero modulo $3$, and subsequent steps are immediate modulo $81$.

Since $Q=3^{h-29}$ and $4D+1<40Q$, the surviving indices are precisely


$$
2s+1=dQ,\qquad d\in\{1,3,5,\ldots,39\}.
$$


Therefore, for integral $\deg P\le2D$,


$$
\boxed{
\mathcal M((y+1)x^HP)
\equiv
4\sum_{\substack{1\le d\le39\\d\text{ odd}}}
\frac{3^{29}}d\,P_{(dQ-1)/2}
\pmod{3^{30}}.
}
\tag{6.6}
$$


All divisions by $d$ are paid: $v_3(d)\le3$.

### 6.2 The relevant polynomial

For the pairing in (6.2), put $t=a+c$, so $0\le t\le b$. Since


$$
D+2b=10Q+b,
$$


the polynomial in (6.6) is


$$
P=x^{10Q+b}(\beta+3y)y^{9Q+1+t}.
\tag{6.7}
$$


Its degree is at most


$$
19Q+2b+2<2D.
$$


Thus the complete formula applies within the original finite cutoff.

The coefficient index in $x^{10Q+b}$ is


$$
k_d=\frac{(d-18)Q-3}{2}-t,
\tag{6.8}
$$


or $k_d-1$ for the $3y$-term.

### 6.3 A binomial valuation used in the proof

Write $Q=3^q$. If


$$
k=uQ+r,\qquad 0<r<Q,\quad 0\le u\le9,
$$


then


$$
\boxed{
v_3\binom{10Q}{k}
=q-v_3(r)+v_3\binom9u.
}
\tag{6.9}
$$


Indeed,


$$
\binom{10Q}{k}=\frac{10Q}{k}\binom{10Q-1}{k-1}.
$$


The lower $q$ ternary digits of $10Q-1$ are all $2$, so the lower-digit part contributes no further carries to the second binomial coefficient. Its remaining valuation is $v_3\binom9u$.

In particular,


$$
v_3\binom94=2.
\tag{6.10}
$$



### 6.4 Evaluation of every surviving layer

Expanding the factor $x^b$ in (6.7) shifts the index by an integer between $0$ and $b$. Thus all needed indices in $x^{10Q}$ lie between


$$
\frac{(d-18)Q-3}{2}-2b-1
\quad\text{and}\quad
\frac{(d-18)Q-3}{2}.
\tag{6.11}
$$



- **The $d=27$ layer.**  
  These indices lie strictly between
  

$$
4Q+\frac Q3
  \quad\text{and}\quad
  4Q+\frac{2Q}{3},
$$


  because $2b/Q<0.146<1/6$. Their remainders modulo $Q$ are not divisible by $Q/3$. Equation (6.9), with $u=4$, gives valuation at least $4$. This pays the weight $3^{26}$ through precision $30$.

- **The $d=9$ layer.**  
  Its extraction index is negative.

- **The remaining layers divisible by $3$.**  
  The indices for $d=3,15$ are negative. For $d=21,33$, they lie strictly inside the intervals with integer parts $Q$ and $7Q$, respectively. Since
  

$$
v_3\binom91=v_3\binom97=2,
$$


  their coefficients have valuation at least $3$, more than the two digits required by the weight $3^{28}$. The $d=39$ extraction is above the degree.

- **The layers with $3\nmid d$.**  
  Their weights are divisible by $3^{29}$. Every possible interior extraction lies strictly between consecutive multiples of $Q$. Since
  

$$
x^{10Q}\equiv(y^Q-1)^{10}\pmod3,
$$


  its coefficient there is zero modulo $3$. Exterior extractions vanish identically.

The one-step shift for $3y$ remains inside the same strict intervals. Every term of (6.6) is therefore zero modulo $3^{30}$, proving Theorem 6.1. ∎

---

## 7. What the next digit now depends on

The new results remove two potential sources of the normalized order-$27$ radical digit:

1. the complete raw core pairing on $Z_G$ is zero through $3^{30}$;
2. the complete first-radical matrix return on $G$ is zero modulo $81$.

They do **not** show that the exact corrected pairing is zero through $3^{30}$.

Let


$$
C_G=G_c(W,Z_G),
\qquad
\Gamma_G=C_G^TE_c^{-1}C_G.
\tag{7.1}
$$


The exact identity is


$$
G^T(S_c)_{KK}G
=G_c(Z_G,Z_G)-\Gamma_G.
\tag{7.2}
$$


After the original unit prefix,


$$
G^T\mathcal R_{c,KK}G
=
-\frac{G_c(Z_G,Z_G)-\Gamma_G}{3^{26}}
-G^T\mathsf B^T\mathsf A^{-1}\mathsf BG.
\tag{7.3}
$$



The known second-radical vanishing and the finite-prefix calculation imply that both terms requiring division below are divisible by the indicated powers. Using Theorem 6.1 and (4.9),


$$
\boxed{
\frac{G^T\mathcal S^{(2)}_cG}{27}
\equiv
\frac{\Gamma_G}{3^{29}}
-
\frac{G^T\mathsf B^T\mathsf A^{-1}\mathsf BG}{27}
\pmod3.
}
\tag{7.4}
$$



Equation (7.4) is an exact localization of the remaining obligation, **not an evaluation of its right-hand side**. The new evaluated statements are Theorems 3.1, 4.8 and 6.1; the remaining projection digit is open.

### Concrete follow-on lemma

A substantive next lemma is now:

> On the same infinite original subwindow, evaluate modulo $3$ the difference in (7.4), using the actual LOW/HIGH projection $E_c^{-1}C_G$ and the actual finite prefix. In particular, determine whether these two projection contributions cancel, or produce a nonzero operator on the endpoint-annihilating combinations
> 

$$
> (y+1)x^by^a,\qquad 0\le a<b/2.
>
$$


> The endpoint lifts and complete diagonal must be carried through the rank-$b$ elimination with its $3^{-2}$ inverse cost.

This is more specific than the former unknown boundary-column pairing: the entire nonterminal $J$-coupling and its matrix return have now been removed by proofs.

The precision-$15$ sufficiency lemma from Turn 17 remains useful **after** this analytic reduction. Certified precision-$15$ representatives of the actual corrected columns determine their core pairings modulo $3^{30}$, because the linear errors gain $3^{26}$ and the quadratic error gains $3^{30}$. This does not authorize replacing the actual projection by an auxiliary completion.

---

## 8. Complete source, resonances, and final scalar obligations

The actual producer remains


$$
Q_{\rm act}=3P_n=Q_c+3^7\mathscr R,
$$




$$
3^7\mathscr R=\sum_{a=0}^{A+1}e_ax^a,
\qquad
e_a=-\frac{(A+1)!}{a!}(t_a+\xi v_a),
$$


with complete force


$$
t=3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
\qquad b_{\rm force}=-n-66.
\tag{8.1}
$$


The signed scalar $\xi$, including its previously paid normalization, is unchanged. The endpoint charge and full return are


$$
\mathscr R(-1)=-\frac{\xi((A+1)!)^2}{3^7},
$$




$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{8.2}
$$



The complete moments still satisfy


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad 0\le t\le2n-2.
\tag{8.3}
$$


The actual forward resonance at


$$
t_*=\frac{3^h-5}{2}
$$


still requires a divisor of valuation $h$; no new argument here cancels it. Thus the new finite $J$-direction (4.10) is not a uniformly paid solution of the eventual endpoint-annihilator problem.

For the endpoint-adapted residual


$$
T=\begin{pmatrix}a&z^T\\z&C\end{pmatrix}\in27M,
\qquad v_3(\lambda)=-1,
$$


the outstanding hypotheses remain:

- nonsingularity of the actual $C$;
- an actual directional bound such as
  

$$
C^{-1}z\in3^{-1}\mathbb Z_3^{b/2};
$$


  or
- an evaluated critical-shell scalar
  

$$
\sigma=w^T\operatorname{adj}(B)w/\det B
$$


  sufficient to prove nonresonance.

None is established by the present fixed-depth return cancellation.

---

## 9. Divisions and arithmetic-scale ledger

The report uses no new unrecorded content division.

| Operation | Payment |
|---|---|
| Complete pole denominators | $3^h$ pays every pole on the original cutoff |
| Factorial omission in congruences | Only after retaining its $3^h$ factor |
| Original producer normalization | The existing $3^7$ division |
| Original LOW/HIGH inverse | $E_c^{-1},E_{\rm act}^{-1}\in3^{-1}M$ |
| Corrected representatives | Exact $3^{20}$ congruence and stationary error estimate |
| Normalization of the core | $S_c/3^{26}$ |
| Unit prefix | Integral unit inverse |
| First-radical block | $3^{-1}B_\alpha^{-1}$ |
| New complete return | $27$ times a pairing proved divisible by $3$ |
| Rank-$b$ elimination | Existing $3^{-2}$ cost |
| Precision-$30$ moments | Every $d^{-1}$ in (6.6) paid by $3^{29}$ |
| Eventual inverse $C^{-1}$ | Still not paid uniformly |

The common determinant depths produced by eliminated blocks are not primitive-denominator savings.

Retain the actual column contents and actual least simultaneous clearer $\ell_{\rm clr}$. No local ternary estimate replaces them. The final integers remain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


with the gcd over **all primes**


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
\tag{9.1}
$$


The whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{9.2}
$$



An irrationality proof still needs, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|\longrightarrow+\infty.
}
\tag{9.3}
$$


The present work does not discharge these obligations.

---

## 10. Bounded exact-arithmetic verification

No tool computation was performed. No repeated H2, nine-period, dense producer, or finite-surrogate calculation is requested.

The only optional arithmetic check for the new binomial valuation proof is a ten-entry universal integer check.

**Inputs**


$$
\binom9u,\qquad 0\le u\le9.
$$



**Expected exact output**


$$
(1,9,36,84,126,126,84,36,9,1),
$$


with ternary valuations


$$
\boxed{(0,2,2,1,2,2,1,2,2,0).}
\tag{10.1}
$$



These values can also be verified directly by the recurrence


$$
\binom9{u+1}=\binom9u\frac{9-u}{u+1},
$$


where every quotient is an exact integer. This finite check validates the small constants used in (6.9); it is not evidence about original-index infinitude or the final scalar.

A finite original-index evaluation of (7.4), if later undertaken, must use a specified admissible original $(j,h)$, certified actual corrected columns, the full functional (1.5), and declared finite representation and operation bounds. Its output would establish only that instance.

---

## 11. Proof-status ledger

| Statement | Status |
|---|---|
| A4 adjoining-column support extension | Validated against the accepted Turn 12 corrected-column argument |
| $L_ce_0$ and $G^T\bar L_ce_0$ at the stated digit | Closed |
| Complete first producer matrix-return difference modulo $81$ | Closed |
| All nonterminal $K$-to-$J$ core columns, Theorem 3.1 | **New proved original-object statement** |
| Terminal-only support $G^T\bar L_c=\gamma_c\delta_J^T$ | **New proved statement; actual terminal amplitude retained** |
| Each complete first-radical matrix return is zero modulo $81$ | **New evaluated complete pairing** |
| Endpoint and diagonal returns vanish | Not asserted |
| Complete raw radical core pairing modulo $3^{30}$ | **New proved statement** |
| Actual LOW/HIGH-plus-prefix projection digit (7.4) | Open |
| Entire next radical operator | Not yet evaluated |
| Final directional inverse or critical-shell nonresonance | Open |
| Growing relative-cofactor saving | Open |
| Same-index all-prime gcd versus nonzero whole error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The supplied A4 proof closes the information gap: its actual adjoining-column extension is valid. The next advance is not another calculation of that column. It is the evaluation of the entire nonterminal finite coupling strip, which proves


$$
G^T\bar L_\alpha=\gamma_\alpha\delta_J^T
$$


and hence the new complete cancellation


$$
\boxed{
27G^TL_\alpha B_\alpha^{-1}L_\alpha^TG\in81M
\quad(\alpha=c,\mathrm{act}).
}
$$


The physical terminal remains active in the endpoint channel.

In addition, the complete raw radical pairing is zero modulo $3^{30}$. The exact remaining next-digit bottleneck is therefore the actual LOW/HIGH-plus-prefix projection difference in (7.4), with the subsequent endpoint and diagonal lifts retained. Its residue has not been evaluated here; the entire next radical digit is consequently still open.

Even resolving that fixed digit would not by itself settle the global objective. The final requirement remains a growing relative-cofactor or other genuine arithmetic improvement, followed by the same-index comparison of the **actual all-prime gcd and primitive denominator** with the **nonzero whole evaluated error**.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


