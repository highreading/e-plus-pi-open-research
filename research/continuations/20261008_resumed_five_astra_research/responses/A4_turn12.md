> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the complete second kernel and evaluation of the sixth-order terminal-aware $J$-return

## Abstract and status

The rationality or irrationality of $e+\pi$ remains unresolved.

This report establishes the following local results on the original retained index family.

1. **The new gray-range rank, complete-kernel, and endpoint-unit argument in A1 Turn 7 passes independent audit.** Its selected graded map, largest admissible ternary scale, minimal-syzygy coefficients, equal-exponent involution, Frobenius transport, degree bounds, and saturated lifts are compatible with the original parameters. Consequently the gray-range endpoint-unit question is no longer open.

2. **The parent’s second-kernel-pivot candidate passes, with the stated distinction between frames.** In the endpoint-adapted first frame one must use
   

$$
v_3(\lambda_{\mathrm{new}})\ge -2,
$$


   not the unproved assertion $\lambda_{\mathrm{new}}=\eta/3$ with $\eta$ a unit. The corresponding border thresholds are $8$ and $10$, not $9$ and $11$. In the parent’s monomial-first frame, the complete additional $3^{-4}$ diagonal return remains present, and the bound is
   

$$
v_3(\lambda_4)\ge -4.
$$



3. **The complete terminal-aware $J$-return at physical order $3^6$ is zero.** In fact, a stronger statement holds on the whole first radical, not just on its second kernel:
   

$$
\boxed{
   \mathscr L_\alpha^{\,T}B_\alpha^{-1}\mathscr L_\alpha
   \in 9\,\operatorname{Mat}(\mathbb Z_3),
   \qquad \alpha=c,\mathrm{act}.
   }
   \tag{A}
$$


   Here $B_\alpha$ is the actual finite $J$-block, including its last row and column, and
   

$$
\mathscr L_\alpha=\frac{L_\alpha^TG_0\mathscr G}{3}.
$$


   Therefore
   

$$
\boxed{
   R_{J,\alpha}
   :=\frac{\mathscr L_\alpha^{\,T}B_\alpha^{-1}\mathscr L_\alpha}{3}
   \equiv0\pmod3.
   }
   \tag{B}
$$



The proof of (A) does **not** extend compression to the last middle column. It computes the next interior $B$-digit, the first-coordinate jet of $\mathscr L$, the finite interior inverse images, and all contributions of the actual terminal coordinate to the divided quadratic. The terminal coupling itself is retained as an actual boundary parameter; its coefficient in this particular divided quadratic is proved to be zero. This is a new next-digit cancellation, not a reuse of the old leading quadratic zero.

The whole physical $3^6$ matrix and force are still not evaluated. In the classified ranges, the previously four unevaluated finite returns are reduced to three: the prefix return, the rank-$b$ return, and the first physical-$4$ complementary return. The moment contribution may be reused at its established scope. No final primitive-denominator improvement follows from these fixed-depth results.

---

## 1. Original domain, finite objects, and permitted reuse

### 1.1 The original indices remain unchanged

All uniform assertions concern sufficiently large indices satisfying exactly


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$




$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15},
$$


and


$$
\frac{103}{1000}<\frac{N_0}{P_0}<\frac{104}{1000}.
$$



Retain


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1.
$$


Write


$$
x=y-1,\qquad Q=27P,\qquad b=Q-N_0=2R,\qquad \chi=P-R,
$$


and put


$$
c=2\chi.
$$


Then


$$
b=2P-c,\qquad N_0=25P+c,\qquad D=268P+c.
$$



For sufficiently large original indices,


$$
v_3(\chi)=5,\qquad \chi/243\equiv1\pmod9.
\tag{1.1}
$$


These follow directly from $\chi=(243r-25P)/2$. They are not conditions imposed on freely chosen auxiliary parameters.

### 1.2 Complete corrected columns and physical terminal

The finite spaces remain


$$
U_s=x^s\quad(0\le s<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),\qquad \nu=D/2-1,
$$




$$
Y_t=y^t\quad(d\le t\le m),\qquad d=D+\nu,\qquad W=[U\ Y].
$$


The physical HIGH terminal is $Y_m$.

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad \mathfrak f(y^t)=(2t)!.
\tag{1.2}
$$


The physical cutoff is $2n-2$, with largest pole denominator


$$
4H-4D+5<3^{h+1}.
$$



For $\alpha=c,\mathrm{act}$,


$$
G_\alpha(f,g)=\mathcal M(Q_\alpha fg),
$$




$$
E_\alpha=G_\alpha(W,W),\qquad
F_\alpha[p]
=x^Dp-WE_\alpha^{-1}G_\alpha(W,x^Dp).
\tag{1.3}
$$


The core is


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
$$



The boundaries used below are exactly


$$
R_*=\frac{9Q+1}{2},\qquad a_0=R_*-1,
$$




$$
\tau=\frac{N_0-3}{2},\qquad \ell=3R+1,
$$




$$
K=\{0,\ldots,\ell-1\},\qquad J=\{\ell,\ldots,\tau-1\}.
$$


Write


$$
N=n_J=\tau-\ell
=\frac{Q-4b-5}{2}
=\frac{19P+8\chi-5}{2}.
\tag{1.4}
$$


The last $J$-coordinate is the actual last middle column:


$$
R_*+\tau-1=\nu-1.
$$



### 1.3 Established results reused without repeating their calculations

I reuse:

- the finite projection and terminal theorems;
- the complete-core compression through modulus $3^{32}$, for ordinary polynomial inputs of degree at most $\nu-2$;
- the finite prefix inverse and the exact relation $X=3P_G+9Z$;
- the unit property of the complete finite $J$-block;
- the complete actual/core comparisons, including the adopted general/one bound $3^{32}$;
- the endpoint modulo $9$ and same-label synchronization already independently confirmed;
- the original support gap
  

$$
\boxed{
  c+2\delta-2\le L_*-120,
  \qquad L_*=\frac{P-1}{2},
  }
  \tag{1.5}
$$


  where
  

$$
\delta=\min\left\{\chi-1,\frac{P+3}{2}-3\chi\right\}.
$$



The new $J$-proof below needs no compression precision beyond the already established modulus $3^{32}$. In particular, it does not depend on treating the locally checked physical-$33$ moment calculation as an independent terminal theorem.

---

## 2. Independent audit of A1 Turn 7’s gray-range theorem

Put


$$
\Pi=P/3,\qquad \kappa_1=(\Pi-1)/2.
$$


The full divided first-radical matrix is


$$
\mathsf D_{uv}
=[y^{\kappa_1-u-v}](1-y)^c,
\qquad 0\le u,v<\delta.
\tag{2.1}
$$



The gray range is


$$
B_1>\delta,\qquad \varepsilon\le0,
$$


equivalently, on the original arithmetic family,


$$
\Pi/6<\chi<\Pi/3,\qquad \delta=\chi-1.
\tag{2.2}
$$



### 2.1 The selected graded map is the correct original map

Set


$$
a_H=\frac{\Pi+1}{2},\qquad
b_H=4\chi-\frac{\Pi+5}{2},\qquad
c_H=2\chi.
$$


In $S=\mathbb F_3[X,Y]$, multiplication by $(Y-X)^{c_H}$ gives


$$
S_{\chi-2}\longrightarrow
\bigl(S/(X^{a_H},Y^{b_H})\bigr)_{3\chi-2}.
\tag{2.3}
$$



At total target degree $3\chi-2$, the surviving exponents of $X$ are precisely


$$
\frac{\Pi+3}{2}-\chi,\ldots,\frac{\Pi-1}{2}
=
\kappa_1-\delta+1,\ldots,\kappa_1.
$$


There are $\delta$ of them, and their coefficient matrix is (2.1), up to row order.

The original congruence buffer makes


$$
a_H,b_H>\chi-2
$$


and all three strict triangle inequalities valid:


$$
a_H+b_H-c_H=2\chi-2>0,
$$




$$
a_H+c_H-b_H=\Pi+3-2\chi>0,
$$




$$
b_H+c_H-a_H=6\chi-\Pi-3>0.
\tag{2.4}
$$


Also


$$
a_H+b_H+c_H=6\chi-2.
$$



A syzygy using only $X^{a_H},Y^{b_H}$ has total degree at least


$$
a_H+b_H=4\chi-2>3\chi-2.
$$


Thus taking the third component is injective at the selected degree. The use of a syzygy-gap theorem here concerns the correct finite graded map, not an ungraded rank surrogate.

### 2.2 The largest admissible scale is correctly identified

Let


$$
\zeta=4\chi-\Pi,\qquad \Delta=|\zeta|,
$$


and let $\mathfrak q$ be the least power of $3$ strictly greater than $\Delta$. From (1.1),


$$
v_3(\zeta)=5,\qquad \zeta/243\equiv4\pmod9.
\tag{2.5}
$$


Hence $\zeta\ne0$, $\Delta$ is not a power of $3$, and


$$
\Delta<\mathfrak q<3\Delta,\qquad
2187\le\mathfrak q\le\Pi/3.
$$



Set


$$
M_*=\Pi/\mathfrak q,\qquad
\omega_*=(-1)^{\log_3M_*},\qquad
\epsilon_*=\operatorname{sgn}(\zeta),
$$




$$
a_\circ=\frac{M_*+\omega_*}{2},\qquad
c_\circ=\frac{M_*+\epsilon_*}{2}.
$$


The integer $a_\circ$ is odd, because $3^e\equiv(-1)^e\pmod4$. Thus


$$
z_\circ=(a_\circ,c_\circ,c_\circ)
$$


belongs to the odd-sum lattice.

The coordinate differences are exactly


$$
d_a=\frac{1-\omega_*\mathfrak q}{2},
\quad
d_b=\epsilon_*\Delta-\frac{\epsilon_*\mathfrak q+5}{2},
\quad
d_c=\frac{\epsilon_*(\Delta-\mathfrak q)}2.
$$


Their distance deficit is


$$
\boxed{
g_*=\mathfrak q-(|d_a|+|d_b|+|d_c|)
=
\frac{\Delta+\omega_*
-|2\Delta-\mathfrak q-5\epsilon_*|}{2}.
}
\tag{2.6}
$$



The nearest-odd-lattice argument passes. For any larger power $Q_3\le\Pi$, the nearest integers to the second and third normalized coordinates are both


$$
\frac{\Pi/Q_3+\epsilon_*}{2}.
$$


Changing either costs more than the possible $1/Q_3$ saving from changing the first rounding. The original multiples-of-$243$ buffers make these inequalities strict. Hence the nearest odd point is the one used in the source.

If $Q_3>\mathfrak q$, then $Q_3\ge3\mathfrak q>3\Delta$, and its deficit is


$$
\frac{3\Delta-Q_3+(-1)^{\log_3(\Pi/Q_3)}-5\epsilon_*}{2}<0.
$$


For $Q_3\ge3\Pi$, the strict triangle inequalities exclude the one-hot odd vertices, while the sum of the normalized coordinates excludes $(1,1,1)$. More distant lattice points cannot have distance below $1$.

Thus $\mathfrak q$ really is the largest admissible scale.

Using the established ternary syzygy-gap theorem at this scope, the generator degrees are


$$
d_1=3\chi-1-g_*/2,\qquad
d_2=3\chi-1+g_*/2.
$$


At degree $3\chi-2$, only the first generator contributes, with multiplicity $g_*/2$. Therefore


$$
\boxed{
k_2=\operatorname{nullity}\mathsf D
=
\frac{\Delta+\omega_*
-|2\Delta-\mathfrak q-5\epsilon_*|}{4}.
}
\tag{2.7}
$$


The parity is also consistent: $g_*$ is even because the original exponent sum is even and the chosen scaled odd-lattice sum is odd.

### 2.3 The auxiliary minimal-syzygy coefficients are valid

For the smaller triple $(a_\circ,c_\circ,c_\circ)$, a larger admissible scale would, by the triangle inequality, produce a scale larger than $\mathfrak q$ for the original triple. Consequently its gap is exactly $1$.

Put


$$
n_\circ=(a_\circ-1)/2,\qquad d_\circ=n_\circ+c_\circ.
$$


The integers


$$
J_i=
\binom{2n_\circ-i}{n_\circ-i}
\binom{c_\circ-n_\circ-1+i}{i},
\qquad 0\le i\le n_\circ,
\tag{2.8}
$$


are well-defined. The second upper parameter is nonnegative on the smaller triples in question.

The source’s Rodrigues calculation proves the exact integral identity


$$
[y^{n_\circ+1}],\ldots,[y^{2n_\circ}]
\quad\text{of}\quad
(1-y)^{c_\circ}\sum_iJ_i y^i
\quad\text{are zero}.
\tag{2.9}
$$


The integration-by-parts step is legitimate as a formal Laurent-series residue: after $n_\circ$ integrations by parts, the derivative of $y^u$ is zero for $u<n_\circ$.

If


$$
\nu_\circ=\min_i v_3(J_i),
$$


division by $3^{\nu_\circ}$ is coefficientwise integral. The low/high coefficient split of (2.9) has the same divisibility, so it gives a nonzero syzygy modulo $3$ of total degree $d_\circ$. Since that degree is the proved minimal degree, this syzygy spans the minimal line and is primitive.

This is an auxiliary coefficient normalization. It is not a division of any original column content.

### 2.4 The equal-exponent endpoint proof passes

The involution


$$
\iota(X,Y)=(-X,Y-X)
$$


preserves $X^{a_\circ}$ up to sign and interchanges


$$
Y^{c_\circ},\qquad (Y-X)^{c_\circ}.
$$


It therefore acts by a nonzero scalar on the one-dimensional minimal-syzygy line.

At


$$
p=(-1,1)\in\mathbb F_3^2,
$$


one has $\iota(p)=-p$. The equality is in characteristic $3$, which is essential.

The last two syzygy components have the same homogeneous degree. If the third vanished at $p$, the involution would force the second to vanish there. The syzygy identity, whose three generating forms are nonzero at $p$, would force the first to vanish as well. All components would then have the common factor $X+Y$, contradicting primitivity.

Hence the third component $W_\circ$ satisfies


$$
W_\circ(-1,1)\ne0.
\tag{2.10}
$$


Normalizing it to $W_\circ(-1)=1$ uses only a ternary unit.

### 2.5 Frobenius transport, degree, and saturation pass

With the source’s positive and negative parts of $d_a,d_b,d_c$, Frobenius transport gives the third component


$$
W_2(y)
=y^\alpha(1-y)^{\gamma_-}W_\circ(y^{\mathfrak q}).
\tag{2.11}
$$


Its total syzygy degree is exactly $d_1$, and


$$
\deg W_2\le d_1-c_H=\delta-k_2.
$$


Thus


$$
\boxed{
\ker\mathsf D=W_2\,\mathbb F_3[y]_{<k_2}.
}
\tag{2.12}
$$


Its endpoint is


$$
\boxed{
W_2(-1)=(-1)^{\alpha+\gamma_-}\ne0.
}
\tag{2.13}
$$



Lifting the normalized coefficients of $W_\circ$ to $0,\pm1$ makes the first nonzero coefficient of the literal lift of $W_2$ equal to $\pm1$. The indicated shifted columns therefore have a triangular minor with diagonal $\pm1$. This proves saturation and the claimed integral complementary basis.

Finally, the established actual endpoint is


$$
\overline f(\mathcal G[p])=\sigma p(-1),
\qquad
\mathcal G[p]=(1-y)^cy^{L_*}p,\qquad
\sigma=(-1)^{R_*+L_*}.
$$


Consequently (2.13) proves a unit for the **actual retained endpoint**, not merely for an unrelated evaluation functional.

### Audit conclusion

The gray-range theorem passes, including the complete kernel and actual endpoint-unit claim. The complete leading annihilator kernel is


$$
(1+y)W_2\,\mathbb F_3[y]_{<k_2-1}
$$


in the full-radical polynomial coordinates.

These are kernels of reduced leading digits. They are **not** asserted to be exact $3$-adic nullspaces. The accepted uniform bounds


$$
k_2\ge242,\qquad k_2-1\ge241
$$


remain valid at their stated scope.

---

## 3. Audit of the new second-kernel pivot and its payments

### 3.1 Valid pivots in every range

The following choices now have proved unit endpoint on the complete second kernel:


$$
W_2=
\begin{cases}
1,&\text{Ranges I–II},\\
(1-y)^{\Pi-c},&\text{Range III},\\
\text{the polynomial in (2.11)},&\text{gray range}.
\end{cases}
$$


In any one of the exact retained frames, take


$$
v_2=\frac{W_2}{F(W_2)}.
\tag{3.1}
$$


This is a unit division.

The parent candidate’s Ranges I–III application therefore passes. The audited gray theorem extends that application to the remaining range; no new subwindow or density assertion is needed.

### 3.2 The new physical-$5$ directional return begins at $7$

Choose the physical-$5$ complement inside the exact endpoint kernel. Since the pivot and retained columns all reduce to the complete second kernel,


$$
A_5=3^5A_{5,0},\qquad A_{5,0}\in\operatorname{GL}(\mathbb Z_3),
$$


and both its retained cross block and its mixed pivot column belong to $3^6M$.

Thus the matrix and directional returns both begin at


$$
6-5+6=7.
\tag{3.2}
$$


This does not contradict the old-pivot Range III return at physical $6$: that old complementary mixed column can start at $5$.

### 3.3 Exact pivot-change transport, not equality of raw directions

Let $H$ be an exact integral basis for the endpoint kernel. If


$$
v_{\mathrm{new}}=v_{\mathrm{old}}+Ht,\qquad t\in\mathbb Z_3^s,
$$


then the unbordered annihilator matrix is unchanged and the mixed force changes by


$$
\boxed{w_{\mathrm{new}}=w_{\mathrm{old}}+Bt.}
\tag{3.3}
$$


Accordingly


$$
Bx=w_{\mathrm{old}}
\quad\Longleftrightarrow\quad
B(x+t)=w_{\mathrm{new}}.
$$


The allowance $x\in3^{-1}\mathbb Z_3^s$ is preserved.

For a complementary elimination, the exact equation remains


$$
(V-X^TA^{-1}X)x_R
=c_R-X^TA^{-1}c_C,
$$




$$
x_C=A^{-1}(c_C-Xx_R).
\tag{3.4}
$$


With $A=3^kA_0$, $X\in3^{k+1}M$, $c_C\in3^kM$, and $x_R\in3^{-1}\mathbb Z_3$, the recovered $x_C$ is integral. The stronger $c_C\in3^{k+1}M$ holds in the new kernel-pivot frame.

Thus the old nonzero Range III weights and $w_*$ remain valid in their old frame. They are not identified with the new raw direction.

### 3.4 Correct diagonal bounds

A1 Turn 7 does not prove its premise


$$
\lambda_{\mathrm{new}}=\eta/3,\qquad \eta\in\mathbb Z_3^\times.
$$


The sufficient accepted bound is


$$
\lambda_{\mathrm{new}}\in3^{-2}\mathbb Z_3.
$$


At physical levels $5$ and $6$, its rank-one border returns therefore begin at $8$ and $10$.

In the parent’s monomial-first frame,


$$
\lambda_4
=\lambda_{\mathrm{new}}
-\frac1{3^4}f_C^TA_{4,0}^{-1}f_C
\in3^{-4}\mathbb Z_3.
\tag{3.5}
$$


After the new physical-$5$ complement, $a,r,S\in3^6M$, and


$$
S^\sharp
=S+\frac{\lambda_4}{1-\lambda_4a}rr^T.
$$


Here $\lambda_4a\in9\mathbb Z_3$, the denominator is a unit, and the return belongs to $3^8M$.

For the $3^{-1}$-allowed directional conversion, the relevant rank-one scalar has valuation at least $2$. Multiplication by $w^Tx$, whose valuation is at least $-1$, still gives a multiple of $3$. Thus the unit conversion remains valid with the weaker bounds.

All previous $1/3$, $1/9$, and monomial-first $3^{-4}$ diagonal returns remain present.

### 3.5 Same-label synchronization

In the common monomial-first frame, the actual and core matrices differ by $3^7M$. Their normalized kernel pivots and endpoint-adapted columns differ by $3$ times the same kernel direction. Pairings with that direction start at $6$, so these changes affect retained pairings only in $3^7M$.

The changed-cross return starts at $7-5+6=8$, and the changed-inverse return starts at $9$. The parent’s physical-$6$ synchronization argument therefore passes, now also in the gray range.

---

## 4. Exact $J$-normalization and the new target

For the core, let


$$
\mathsf H=-G_c(F,F)/3^{26},
$$


and let $\mathsf A$ be its prefix block. Write $\mathsf B_v$ for the prefix-to-tail column labelled by $v$.

The normalized finite $J$-block is


$$
B=\frac{\mathsf H_{JJ}-\mathsf B_J^T\mathsf A^{-1}\mathsf B_J}{3}.
\tag{4.1}
$$


This is the unit-normalized block whose physical inverse costs $3^{-1}$.

For $z\in\mathbb Z_3[y]_{<\delta}$, put


$$
C_z(y)=(1-y)^c z(y),\qquad
\mathcal G[z]=y^{L_*}C_z(y),
$$


and let


$$
l_z=\mathscr L z,\qquad \mathscr L=L_c^TG_0\mathscr G/3.
$$


The exact prefix relation gives


$$
\boxed{
(l_z)_v
=
-\frac{G_c(F_{R_*+v},\mathcal F[\mathcal G[z]])}{3^{29}}
+
(\mathsf B_v/3)^TZ\mathscr Gz.
}
\tag{4.2}
$$


Indeed, $X=3P_G+9Z$ and $\mathsf A Z=d$ give precisely the second term in (4.2). This is not an unreturned moment in place of the full coupling.

Define


$$
t=P+3\chi-2,\qquad
a=\frac{13P+6\chi-3}{2},\qquad
V(y)=1+y^P+y^{2P}.
\tag{4.3}
$$


The inequalities needed below are


$$
\delta\le\chi-1,\qquad
3\chi+\delta\le\frac{P+3}{2},
$$




$$
\deg C_z\le c+\delta-1,\qquad
\deg((1-y)^czw)\le L_*-120.
\tag{4.4}
$$



Only rows $0,\ldots,N-2$ will be compressed. Row $N-1$ remains the actual last middle coordinate.

---

## 5. The next finite $B$-digit

Let


$$
U(y)=(1-y)^{N_0},\qquad U_r=[y^r]U,
$$


with $U_r=0$ outside its actual coefficient interval.

### Proposition 5.1 — Interior $J$-block modulo $9$

For $0\le i,j\le N-2$, set


$$
S=N_0+N-1.
$$


Then


$$
\boxed{
B_{ij}\equiv
\rho U_{S-i-j}
+3U_{S-Q-i-j}
+3U_{S-1-i-j}\pmod9,
\qquad
\rho=K_N\beta-3.
}
\tag{5.1}
$$


In particular, $\rho\equiv1\pmod3$.

#### Derivation

Since


$$
D=9Q+N_0,
$$


the compact factor is


$$
(1-y)^{9Q}U(y).
$$


Modulo $27$,


$$
(1-y)^{9Q}\equiv(1-y^Q)^9.
$$


In the finite tail-tail extraction interval, only its $3Q$ and $4Q$ bands contribute at the required precision:


$$
-84\,U_{S-i-j}+126\,U_{S-Q-i-j}.
$$


After division by the physical $3^{27}$ normalization, inclusion of $\beta+3y$, and the overall minus sign, this gives


$$
K_N\beta U_{S-i-j}
+3U_{S-Q-i-j}
+3U_{S-1-i-j}\pmod9.
$$



The unit-$3Q$ layer has the two possible poles $21Q$ and $39Q$. Their coefficients are opposite and their reciprocal units agree modulo $3$; their complete contribution is zero modulo $9$ after normalization. The $9Q$ extraction is negative. Lower-valuation pole weights are too deep for this digit.

The prefix Schur correction contributes


$$
-3U_{S-i-j}\pmod9,
$$


using the established leading selector and $\overline{\mathsf A}=A_0$. This proves (5.1).

All participating ordinary inputs have degree at most $\nu-2$. No value from the last row or column was supplied by this formula. ∎

---

## 6. Actual leading inverse images, with the terminal retained

The known leading interior coupling is


$$
\overline{(l_z)_i}
=-[y^{t-i}]C_z,\qquad 0\le i\le N-2.
\tag{6.1}
$$


Its support lies strictly inside $J$, so its first coordinate is zero.

Order the actual leading block as first, interior, last:


$$
\overline B=
\begin{pmatrix}
0&0&a_\partial\\
0&B_I&w\\
a_\partial&w^T&c_\partial
\end{pmatrix}.
\tag{6.2}
$$


The finite unit property implies $a_\partial\ne0$. The actual $w,c_\partial,a_\partial$ are retained.

The accepted finite inverse is


$$
(B_I^{-1})_{ij}
=-[y^{N-1-i-j}]U^{-1},
\qquad 1\le i,j\le N-2.
$$



### Proposition 6.1 — Explicit interior inverse image

Define the integral coefficient vector $X_z$ by


$$
\boxed{
X_z(y)=y^aV(y)z(y).
}
\tag{6.3}
$$


It is supported strictly inside $J$, and


$$
\overline{B_I^{-1}(l_z)_I}=\overline{(X_z)_I}.
\tag{6.4}
$$



#### Proof

Using the symmetry of $(1-y)^c$, since $c$ is even, the finite convolution gives


$$
(B_I^{-1}\overline l_z)_i
=
\sum_u z_u
[y^{s-i+u}](1-y)^{-25P},
\qquad
s=\frac{17P+6\chi-3}{2}=a+2P.
$$


Modulo $3$,


$$
(1-y)^{-25P}
=\frac{1+y^P+y^{2P}}{1-y^{27P}}.
$$


The largest index observed in this finite inverse application is below $9P$. Thus only coefficients at $0,P,2P$ occur. This is exactly (6.3).

The support satisfies


$$
a>0,\qquad
a+2P+\delta-1\le9P-1<N-2.
$$


Therefore no inverse convolution has crossed a finite boundary. ∎

The complete leading inverse image is consequently


$$
\boxed{
\overline{B^{-1}l_z}
=
\theta_z e_0+\overline{X_z},
\qquad
\theta_z=
a_\partial^{-1}
\bigl(\overline{(l_z)_{N-1}}-w^T\overline{X_z}\bigr),
}
\tag{6.5}
$$


with last coordinate zero.

Equation (6.5) explicitly retains the actual last-middle coupling. It is generally not legitimate to set $\theta_z=0$.

---

## 7. The next coupling digit, including the prefix return

The following calculation evaluates the couplings needed in the divided quadratic. It also supplies the first-coordinate jet that was missing in the earlier argument.

### 7.1 A new finite leading prefix calculation

For a monomial amplitude $y^u$, the complete leading prefix residual is


$$
\boxed{
\overline d_{p,u}
=
2\,\mathbf1_{p+u+1=Q}
+\mathbf1_{p+u+1=2Q}
+2\,\mathbf1_{p+u+1=4Q}.
}
\tag{7.1}
$$



Here all contributions of $\beta+3y$, the $3$-weighted low one-lift term, and the relevant pole layers have been included.

A bounded verification of its universal coefficients is as follows. Put


$$
c_k=(-1)^k\binom{30}{k},\qquad c_k=0\quad(k<0).
$$


At $p+u+1=j(9P)$, $1\le j\le13$, the residue is


$$
\frac{c_{j+3}+3c_{j-6}}9+\mathbf1_{j=9}-\mathbf1_{j=6}\pmod3.
\tag{7.2}
$$


The resulting vector is


$$
(0,0,2,0,0,1,0,0,0,0,0,2,0).
$$


The possible $p+u+2$ residues are


$$
c_{j+3}/3+c_{j-6}\pmod3,
$$


and all are zero.

The reduction to this bounded row is uniform. Repeated ternary scaling preserves the normalized binomial units. For the modulus $27$ reduction, one can use


$$
\binom{3a}{3b}
\equiv
\binom ab\left(1+\frac92ab(a-b)\right)\pmod{27},
$$


whose correction is zero modulo $27$ at the required divisible top indices. This identity follows by grouping the nonmultiples of $3$ in the factorials.

Applying the finite inverse


$$
(A_0^{-1})_{pq}=[y^{p+q-a_0}]U^{-1}
$$


to (7.1), and then contracting with $\mathcal G[z]$, gives


$$
\boxed{
\overline{Z\mathscr Gz}(y)
=
2\bigl(y^{14P}+y^{41P}+y^{95P}\bigr)V(y)z(y).
}
\tag{7.3}
$$


For example, before collecting bands this is the truncation of


$$
(2y^{95P}+y^{68P}+2y^{14P})(1-y)^{-25P}z.
$$


The next omitted band starts at $122P>a_0$. All displayed bands lie inside the actual prefix.

### 7.2 The prefix selector through its next digit

For an interior tail label $v=\ell+i$, put $s_v=k_0+v$. The finite expansion of $\mathsf B_v/3$, combined with the already known $\mathsf A\bmod9$, gives


$$
\begin{aligned}
\mathsf A^{-1}(\mathsf B_v/3)
\equiv{}&
\frac12e_{s_v}\\
&+\frac32\left(
2A_0^{-1}b_{5,v}
+e_{s_v-Q}+2e_{s_v+Q}+e_{s_v+2Q}
\right)\pmod9,
\end{aligned}
\tag{7.4}
$$


where


$$
(b_{5,v})_p=U_{5Q-1-p-v}.
$$


Every displayed ordinary selector lies in the actual prefix. The $b_{5,v}$ term is the genuine finite correction for the negative virtual selector $s_v-2Q$; it has not been replaced by an infinite Toeplitz rule.

The three shifted $d$-selectors in (7.4) are zero modulo $3$, by (7.1) and the strict finite inequality


$$
0<\frac{Q-3}{2}-(v+u)<\frac Q2.
$$


The unshifted one satisfies


$$
d_{s_v,\bullet}\mathscr Gz
\equiv3[y^{t-i}]C_z\pmod9.
\tag{7.5}
$$



For the virtual selector, (7.3) gives


$$
U\,\overline{Z\mathscr Gz}
=
2\bigl(y^{14P}-y^{68P}+y^{95P}-y^{122P}\bigr)C_z
\quad\text{in }\mathbb F_3[y].
\tag{7.6}
$$


Its observed index is $132P+3\chi-2-i$. Even after the largest shift $122P$, the smallest relevant residual, at $i=N-2$, exceeds $\deg C_z$ by at least


$$
\frac{P+7}{2}-3\chi-\delta\ge2.
$$


Hence this complete finite virtual-selector contraction is zero.

Thus the prefix contribution in (4.2), through modulus $9$, is supported only in the old $t-i$ band.

### 7.3 Complete interior support through modulus $9$

For the raw moment in (4.2), put


$$
r=\frac{Q-3}{2}-(v+u).
$$


For every admitted interior input, $r\ge2$. The relevant new pole audit is:

| Contribution | Possible band after radical contraction |
|---|---|
| $27Q$, high coefficient at $117P$, including its next unit digit | $t-i$ |
| $27Q$, high coefficients at $114P,111P$ | $t+3P-i,\ t+6P-i$, each with an extra $3$ |
| $27Q$, high $3y$ term | $t-1-i$, with an extra $3$ |
| $27Q$, $3$-weighted low term at $198P$ | $t-i$, with an extra $3$ |
| $9Q$ | no admissible extraction |
| Unit-$3Q$ layer | too deep |
| Unit-$Q$ layer | the two old-band contributions cancel |
| Unit-$Q/3$ layer | the four old-band coefficients $1,-1,-1,1$ cancel |
| Lower layers | too deep for modulus $9$ after division by $3^{29}$ |

Together with §7.2, this proves that the **complete** interior coupling modulo $9$ has the form


$$
\begin{aligned}
(l_z)_i\equiv{}&
u_0[y^{t-i}]C_z
+3u_1[y^{t-1-i}]C_z\\
&+3u_3[y^{t+3P-i}]C_z
+3u_6[y^{t+6P-i}]C_z
\pmod9,
\end{aligned}
\tag{7.7}
$$


for integral scalars $u_0,u_1,u_3,u_6$. Their unused unit digits are immaterial to the following evaluations: every corresponding coefficient contraction is individually zero.

The finite restriction $r\ge2$ is important. At the last middle column the $3y$-shift can reach a boundary extraction not covered by this calculation. Formula (7.7) is deliberately not asserted there.

### Proposition 7.1 — Evaluated first jet and mixed contractions

For every $z,w\in\mathbb Z_3[y]_{<\delta}$,


$$
\boxed{
(l_z)_0\equiv0\pmod9,
\qquad
l_z^TX_w\equiv0\pmod9.
}
\tag{7.8}
$$



#### Proof

At $i=0$, all four indices in (7.7) exceed $\deg C_z$.

For contraction with $X_w=y^aVw$, the first three bands have negative resulting extraction index. The remaining band gives


$$
t+6P-a=L_*.
$$


Thus its contraction is a multiple of


$$
[y^{L_*}]\,V(y)(1-y)^czw.
$$


Since $L_*<P$, only the constant band of $V$ could contribute; (1.5) makes that coefficient zero. ∎

In particular, the actual first-coordinate jet of $L/3$ on this radical is zero. This is not an inference from its preceding digit.

---

## 8. Evaluation of the next $B$-digit on the actual inverse-image directions

### Proposition 8.1

For all $z,w\in\mathbb Z_3[y]_{<\delta}$,


$$
\boxed{
B_{00}\equiv0,\qquad
e_0^TBX_z\equiv0,\qquad
X_z^TBX_w\equiv0\pmod9.
}
\tag{8.1}
$$



#### First corner

In (5.1), only the shifted-$Q$ term can contribute to $B_{00}$. By coefficient reversal it observes


$$
U_{Q-N+1}.
$$


But


$$
Q-N+1=\frac{35P-8\chi+7}{2}\equiv125\pmod{243},
$$


whereas $U\bmod3$ has support only at multiples of $243$. Thus $B_{00}\equiv0\pmod9$.

#### First row against the interior inverse image

The unshifted and one-step-shifted terms in (5.1) are out of range. The remaining contraction, modulo $3$ before its explicit factor $3$, is a sum of


$$
U_{(24+k)P-\chi+2+u},\qquad k=0,1,2.
$$


For $0\le u<\delta$,


$$
-\chi+2+u\le0.
$$


If it is negative, its residue modulo $P$ is above $c$, so all coefficients vanish. If it is zero, the three coefficients sum to


$$
[t^{24}](1-t)^{25}
+[t^{25}](1-t)^{25}
+[t^{26}](1-t)^{25}
=1-1+0=0
$$


in $\mathbb F_3$. Hence $e_0^TBX_z\equiv0\pmod9$.

#### Interior inverse images against one another

Put


$$
C=(1-y)^czw,\qquad D_*=21P+L_*.
$$


The three terms of (5.1) become


$$
\rho[y^{D_*}]UV^2zw,\quad
3[y^{D_*-Q}]UV^2zw,\quad
3[y^{D_*-1}]UV^2zw.
\tag{8.2}
$$


The middle index is negative. The last term is zero modulo $9$ by (1.5) and the modulo-$3$ $P$-band structure.

For the first term, use


$$
(1-y)^P
\equiv1-y^P+3(-y^\Pi+y^{2\Pi})\pmod9.
$$


Then


$$
(1-y)^{25P}
\equiv
(1-y^P)^{25}
+3(1-y^P)^{24}(-y^\Pi+y^{2\Pi})\pmod9.
$$


The unshifted part has only $P$-bands and observes $C_{L_*}=0$.

In the extra term, $V^2\equiv(1-y^P)^4\pmod3$. The $2\Pi$-shift observes a residue above $\deg C$. The $\Pi$-shift could observe $C_{\kappa_1}$, but its band coefficient is


$$
[t^{21}](1-t)^{28}=0\quad\text{in }\mathbb F_3,
$$


because $28=27+1$. Therefore the first expression in (8.2) is also zero modulo $9$. ∎

This evaluates the next finite $B$-digit on all directions that can occur in the actual leading inverse images, including their $e_0$ component.

---

## 9. The complete divided quadratic, with every cross and inverse-change term

Choose any integral lift of $\theta_z$ in (6.5), and set


$$
x_z=\theta_z e_0+X_z.
$$


Then


$$
Bx_z\equiv l_z\pmod3.
$$


Consequently


$$
r_z=\frac{l_z-Bx_z}{3}
$$


is integral. The following identity is exact:


$$
\boxed{
l_z^TB^{-1}l_w
=
l_z^Tx_w+x_z^Tl_w-x_z^TBx_w
+9r_z^TB^{-1}r_w.
}
\tag{9.1}
$$



This identity is the invariant form of the expansion in A4 Turn 11, equation (7.10). It includes:

- both changes of the coupling vector;
- the change of the inverse;
- the divided base-lift quadratic;
- the actual terminal-dependent first-coordinate components.

By Propositions 7.1 and 8.1,


$$
l_z^Tx_w\equiv0,\qquad
x_z^Tl_w\equiv0,\qquad
x_z^TBx_w\equiv0\pmod9.
$$


The last term in (9.1) belongs to $9\mathbb Z_3$, since $B^{-1}$ is integral. Hence


$$
\boxed{
l_z^TB^{-1}l_w\in9\mathbb Z_3
\quad\text{for all }z,w\in\mathbb Z_3[y]_{<\delta}.
}
\tag{9.2}
$$



### What happened to the terminal coupling?

It has not been deleted. Its exact leading contribution is $\theta_z$ in (6.5). In the divided quadratic, every occurrence of $\theta_z$ multiplies one of


$$
(l_w)_0,\qquad e_0^TBX_w,\qquad B_{00},
$$


all now evaluated as zero modulo $9$.

Thus the complete terminal contribution to this digit is zero **for the actual boundary values**, because the calculation proves zero for every boundary value compatible with the established finite unit border.

There is also a next inverse-image consequence:


$$
\boxed{
(B^{-1}l_z)_{N-1}\in9\mathbb Z_3.
}
\tag{9.3}
$$


Indeed, the first component of $l_z-Bx_z$ belongs to $9\mathbb Z_3$; the leading bordered solve then makes the last component of the correction divisible by an additional $3$.

The literal scalar $(l_z)_{N-1}\bmod3$ is not numerically evaluated here. What is evaluated is its entire contribution to the assigned divided quadratic, and that contribution is zero. Its separate value can matter at a later physical digit.

### Transfer to the actual complete producer

The adopted comparisons give, on the nonterminal interior,


$$
B_{\mathrm{act}}-B_c\in9M.
$$


Also $X_{\mathrm{act}}-X_c\in3^4M$ implies


$$
Z_{\mathrm{act}}-Z_c\in9M.
$$


Using the general/one comparison $3^{32}$ in (4.2), together with


$$
\delta(\mathsf B/3)\in9M,
$$


gives


$$
(l_{\mathrm{act},z})_i-(l_{c,z})_i\in9\mathbb Z_3,
\qquad 0\le i\le N-2.
$$


The terminal integrality and finite unit-block property are retained inputs. Since the proof of (9.2) allowed arbitrary actual terminal values, it applies unchanged to the actual block.

Therefore (A) and (B) hold for both core and actual complete objects.

---

## 10. Consequences for the new second-kernel tests and pivot

Choose


$$
z_i=(1+y)W_2y^i,\qquad 0\le i<k_2-1,
$$


and the leading endpoint-normalized kernel pivot


$$
z_*=\frac{W_2}{W_2(-1)}.
$$


Exact endpoint normalization uses the actual unit endpoint and is paid as in §3.

Equation (9.2) gives, in every range,


$$
\boxed{
\mathcal J(z_i,z_j)=0,\qquad
\mathcal J(z_i,z_*)=0
\quad\text{in }\mathbb F_3.
}
\tag{10.1}
$$


It also gives zero for the old Range III pivot $w_*$, because the theorem holds on the whole first-radical coefficient space.

In the new kernel-pivot frame, the physical-$5$ complementary directional return starts at $7$. At physical $6$, the whole force is therefore assembled from


$$
\boxed{
\mathcal M_6+\mathcal P+\mathcal B_b+\mathcal C_4,
}
\tag{10.2}
$$


with the same signs and endpoint normalization as the exact source assembly.

The first physical-$4$ complementary return $\mathcal C_4$ remains active at $6$. Neither (9.2) nor the new pivot eliminates it.

The accepted moment formulas can be reused:

- Ranges I–II:
  

$$
\mathcal M_6(z,w)=[y^{\kappa_2}](1-y)^czw;
$$


- Range III, $z=Ua,\ w=Ub$, $U=(1-y)^{\Pi-c}$:
  

$$
\mathcal M_6(z,w)=2[y^{\kappa_2}]Uab.
$$



In particular, using the new Range III pivot $z_*=2^{-(\Pi-c)}U$ changes the directional moment accordingly. It is not the old $w_*$-direction.

No value of the sum (10.2) is claimed. The gray-range $J$-term is now evaluated, but this report does not supply a gray-range evaluation of every other sixth-layer contribution.

---

## 11. Division and boundary ledger

| Operation | Status |
|---|---|
| Original $W$-projection inverse | Retained at its paid $3^{-1}$ scope |
| Compact moment compression used here | Only ordinary inputs of degree $\le\nu-2$; modulus $3^{32}$ suffices |
| Prefix normalization | $3^{26}$, unchanged |
| $d=G(F_{\rm pref},\mathcal F)/3^{28}$ | Paid and its needed leading residues evaluated in (7.1) |
| $J$-block normalization | Physical $3^{27}$; unit-normalized inverse integral |
| $\mathscr L=L^TG_0\mathscr G/3$ | Integral by the established complete boundary payment |
| Next $\mathscr L$-digit | Evaluated on all required tests; first coordinate is $0\bmod9$ |
| Last middle $J$-column | Retained by the actual finite border; never compressed beyond the admitted range |
| Complete $J$-quadratic | Strengthened from divisibility by $3$ to divisibility by $9$ |
| Physical $J$-matrix return on first radical | Now begins at $3^7$ |
| Rank-$b$ inverse and return | Full $3^{-2}$ payment retained; sixth-order contraction still open |
| First physical-$4$ complement | Full $3^{-4}$ payment and sixth-order matrix return retained |
| New physical-$5$ complement | Inverse $3^{-5}$; matrix and new-pivot directional returns begin at $7$ |
| Complete diagonal | All $1/3$, $1/9$, and, in the monomial-first frame, $3^{-4}$ returns retained |
| Auxiliary $J_i/3^{\nu_\circ}$ | Coefficientwise paid auxiliary division only |
| Original contents and primitive pair | Not altered |

---

## 12. New bounded exact-arithmetic receipt

No computation was performed. No original dense matrix or unspecified original tuple is requested.

The uniform proof above is symbolic. An optional new receipt can check its small universal arithmetic.

### Inputs

1. Integers $0\le k\le30$, modulus $27$, and
   

$$
c_k=(-1)^k\binom{30}{k}.
$$


2. Indices $1\le j\le13$.
3. Polynomial arithmetic in $\mathbb F_3[t]/(t^{122})$.

### Expected verifiable outputs

First, every numerator below is divisible by $9$, and


$$
\left(
\frac{c_{j+3}+3c_{j-6}}9
+\mathbf1_{j=9}-\mathbf1_{j=6}
\right)_{j=1}^{13}
=
(0,0,2,0,0,1,0,0,0,0,0,2,0)
$$


in $\mathbb F_3$, with $c_k=0$ for $k<0$.

Also,


$$
\left(c_{j+3}/3+c_{j-6}\right)_{j=1}^{13}=0
\quad\text{in }\mathbb F_3^{13}.
$$



Second,


$$
(1-t)^{25}(1+t+t^2)=1-t^{27}
\quad\text{in }\mathbb F_3[t],
$$




$$
[t^{21}](1-t)^{28}=0,
$$


and


$$
\begin{aligned}
&(2t^{95}+t^{68}+2t^{14})(1-t)^{-25}\\
&\hspace{1cm}\equiv
2(t^{14}+t^{41}+t^{95})(1+t+t^2)
\pmod{t^{122}}
\end{aligned}
$$


over $\mathbb F_3$.

These are bounded universal coefficient checks. They do not represent an admissible original index and do not establish an infinite-family conclusion by experimentation. The original-family conclusion follows from the finite-boundary and support arguments above.

---

## 13. Complete forcing and unchanged global normalization

The producer remains


$$
Q_{\mathrm{act}}=Q_c+3^7\mathscr R.
$$


Retain


$$
F_{\mathrm{fac}}=(n-1)!,
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
\qquad
\gamma_0=1,\quad\gamma_1=0,\quad
\gamma_{k+1}=(4k+2)\gamma_k+4\gamma_{k-1},
$$




$$
h_{\mathrm{vec}}
=T_n^{-1}\left(\binom{n+a}{a}\gamma_{n+a}\right)_{a=0}^{n-1},
$$




$$
u_a=\frac{F_{\mathrm{fac}}(-2)^a}{a!},\qquad v=T_n^{-1}u,
$$




$$
b_{\mathrm{force}}=-n-66,
$$




$$
t=
3nh_{\mathrm{vec}}
+(b_{\mathrm{force}}+6)e_{n-1}
+\frac{2b_{\mathrm{force}}}{n-1}e_{n-2},
\qquad
\xi=\frac{u^Tt}{F_{\mathrm{fac}}^2-u^Tv}.
$$


The exact signed coefficients remain


$$
[x^a](3^7\mathscr R)
=-\frac{F_{\mathrm{fac}}}{a!}(t_a+\xi v_a),
\qquad 0\le a\le A+1,
$$




$$
\mathscr R(-1)=-\frac{\xi F_{\mathrm{fac}}^2}{3^7}.
$$



The full forcing identity is still


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\mathrm{ret}}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{13.1}
$$


Both displayed forcing terms, including the terminal coordinate, remain present.

The complete-source recurrence is unchanged:


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad 0\le t\le2n-2,
$$


with its genuine resonant divisor at


$$
t_*=(3^h-5)/2.
$$



No local saturated change, dyadic unit normalization, or auxiliary syzygy division changes the actual original integer column contents or the actual least simultaneous clearer $\ell_{\mathrm{clr}}$.

Retain


$$
A_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
G=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$, the actual primitive pair is


$$
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G},
\qquad
q=\frac{|B_\ell|}{G}.
$$


The whole error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\mathrm{clr}}^{m+1}}
{G}\det H_{\mathrm{complete}}.
}
\tag{13.2}
$$



An irrationality proof still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\mathrm{complete}}\ne0,
$$


and


$$
\log G-(m+1)\log\ell_{\mathrm{clr}}
-\log|\det H_{\mathrm{complete}}|
\longrightarrow+\infty.
\tag{13.3}
$$


These conditions would make the nonzero whole errors tend to zero, contradicting rationality. None is established by the fixed local rank and return calculations in this report.

---

## Conclusion

### New proved statements

- A1 Turn 7’s gray-range rank, complete leading kernel, saturated lift, and actual endpoint-unit theorem pass independent audit.
- The new second-kernel-pivot payment passes and extends to the gray range.
- Its diagonal estimates require the repaired bounds:
  

$$
v_3(\lambda_{\mathrm{new}})\ge-2,\qquad
  v_3(\lambda_4)\ge-4
$$


  in their respective frames.
- The complete terminal-aware $J$-quadratic satisfies
  

$$
\boxed{
  \mathscr L_\alpha^{\,T}B_\alpha^{-1}\mathscr L_\alpha\in9M,
  \qquad
  R_{J,\alpha}\equiv0\pmod3,
  \quad \alpha=c,\mathrm{act}.
  }
$$


  This holds on the whole first radical and hence on every complete second-kernel test and its unit pivot.

### Exact remaining local bottleneck

The sixth-order whole matrix and force still require the evaluated contractions of


$$
\boxed{\mathcal P+\mathcal B_b+\mathcal C_4}
$$


together with the appropriate complete moment term. The first physical-$4$ return remains active. The new physical-$5$ complement contributes only from order $7$ in the kernel-pivot frame.

The individual last-middle coupling has not been assigned a numerical residue. Its **entire contribution to the presently assigned $J$-contraction** has been evaluated as zero; its value may become necessary at a later digit.

### Exact remaining global bottleneck

One still needs same-index nonvanishing and decay of the nonzero **whole** error after the actual contents, least simultaneous clearer, all-prime gcd, and actual primitive denominator have been used. No unbounded primitive saving or unconditional conclusion about $e+\pi$ follows here.



$$
\boxed{\text{The global rationality/irrationality objective remains open.}}
$$


