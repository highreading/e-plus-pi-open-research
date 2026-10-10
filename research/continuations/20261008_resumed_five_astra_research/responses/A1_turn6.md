> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The first divided complete-core radical digit

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

This report evaluates the first divided radical **matrix** digit left open in A1 Turn 5. The original index family, subwindow, corrected columns, finite prefix, $J$-window, rank-$b$ return, and physical HIGH boundary are unchanged.

Put


$$
\Pi=\frac P3,\qquad
\kappa_1=\frac{\Pi-1}{2},\qquad
L_*=\frac{P-1}{2},
$$


and retain


$$
\delta=\min\left\{\chi-1,\frac{P+3}{2}-3\chi\right\}.
$$


Number the complete radical basis by


$$
g_{L_*+u}(y)=(1-y)^{2\chi}y^{L_*+u},
\qquad 0\le u<\delta.
$$


Let $\mathscr G$ be its integer coefficient matrix and let
$\widehat{\mathscr G}$ be the exact paid orthogonal lift through the monomial complement from Turn 5.

The new matrix result is


$$
\boxed{
\frac{\widehat{\mathscr G}^{\,T}
T_{c,\mathrm{red}}\widehat{\mathscr G}}{3^5}
\equiv-\mathsf D\pmod3,
}
\tag{0.1}
$$


where


$$
\boxed{
\mathsf D_{uv}
=[y^{\kappa_1-u-v}](1-y)^{2\chi},
\qquad 0\le u,v<\delta.
}
\tag{0.2}
$$


Every entry is evaluated by the ternary-digit rule in Section 7.

The important new contribution is the band at $P/3$ in


$$
(1-y)^{2P}\pmod9.
$$


The leading-modulo-$3$ support gap does **not** make the divided digit zero. Its missing contribution is exactly the matrix in (0.2).

The proof also evaluates the two matrix returns that could have contributed at this digit:

* the radical-contracted second-prefix term is in $9M$, before multiplication by its physical factor $81$;
* the contracted first $J$-return is zero after division by $3^5$, modulo $3$.

The latter conclusion is proved without extending the compression theorem to the last middle column. An exact finite bordering argument retains that column and shows why its as-yet-unevaluated coupling is invisible to this particular quadratic matrix digit.

Several ranges admit an exact rank, complete radical, and explicit complement for $\mathsf D$. These yield corresponding exact second Smith-layer counts for the complete core.

**An outstanding part of the assignment remains open.** The complete core endpoint and diagonal are not numerically evaluated here. Their exact returns are retained, and Section 8 identifies the specific normalized boundary and complement data still required. In particular, neither the unreturned evaluation $g(-1)$ nor the matrix calculation (0.1) supplies those data. The report therefore closes the divided **matrix** digit, not the complete bordered directional problem.

---

## 1. Original objects and reused scope

### 1.1 The original indices are not replaced

All uniform statements below concern sufficiently large indices satisfying exactly


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$


The fixed subwindow remains


$$
\frac{103}{1000}<\rho=\frac{N_0}{P_0}<\frac{104}{1000}.
$$



The arithmetic identities are


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1.
$$


Set


$$
x=y-1,\qquad Q=27P,\qquad b=Q-N_0,\qquad R=\frac b2,
\qquad \chi=P-R.
$$


Thus


$$
D=10Q-b,\qquad
.064<\frac bQ<.073,
$$




$$
.0145<\frac{\chi}{P}<.136.
\tag{1.1}
$$



Every occurrence of $P,\chi,R,\delta$ below is obtained from such an original index. The piecewise rank statements do not substitute freely chosen auxiliary parameters for that index.

### 1.2 Finite spaces and corrected columns

The original finite coordinates are


$$
U_s=x^s\quad(0\le s<D),
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),
\qquad \nu=\frac D2-1,
$$




$$
Y_t=y^t\quad(d\le t\le m),
\qquad d=D+\nu,
\qquad W=[U\ Y].
$$


The physical HIGH terminal is $Y_m$.

The complete functional and core are


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),
\qquad
Q_c=(y+1)x^A(\beta+3y),
\qquad \beta=-71-A.
$$


The corrected columns are exactly


$$
E_c=G_c(W,W),\qquad
F_i=z_i-WE_c^{-1}G_c(W,z_i).
$$


The one-lift inputs remain


$$
\Psi_a=x^{D+b}y^{k_0+a}(y^{3Q}+3),
\qquad
k_0=\frac{3Q+1}{2},
\qquad 0\le a\le R,
$$


and $\mathcal F_a$ is the complete-core correction of $\Psi_a$ against this same $W$.

The retained finite boundaries are


$$
R_*=\frac{9Q+1}{2},\qquad
a_0=R_*-1=\frac{9Q-1}{2},
$$




$$
\tau=\frac{N_0-3}{2},\qquad
\ell=3R+1,
$$




$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\},
$$




$$
n_J=\frac{Q-4b-5}{2},\qquad R_*+\tau=\nu.
$$



### 1.3 Closed inputs reused, not recalculated

The following are used only at their accepted scope:

* the original mixed projection and one-digit inverse loss;
* the admitted $p=17$ filter and its stated finite degree range;
* the paid complete-core/pole comparison;
* the finite unit-prefix inverse and first-prefix lift;
* H2 and the original rank-$b$ quotient;
* the exact $J$- and rank-$b$-return formulas;
* the closed physical-terminal theorem
  

$$
[y^m]\mathcal F_a
  \equiv-3^{27}\delta_{a,R}\pmod{3^{28}},
  \qquad \gamma_c=0;
$$


* the complete radical, saturated lift, and monomial complement proved in Turn 5;
* $M_{b,c}\in3M$, with its physical rank-$b$ return in $3^6M$.

No Jacobi norm, $\binom{90}{40}$ table, dense auxiliary rank computation, or terminal theorem is repeated.

---

## 2. Two original-arithmetic facts needed at the new digit

For sufficiently large original indices, $P$ is divisible by $243$. Since


$$
\chi=\frac{243r-25P}{2},
$$


we have


$$
243\mid\chi.
\tag{2.1}
$$


At still larger original indices,


$$
\frac{\chi}{243}\equiv\frac r2\equiv1\pmod9.
\tag{2.2}
$$


In particular, these are not arbitrary amplitude parameters.

Write


$$
s=L_*+u,\qquad t=L_*+v,
\qquad 0\le u,v<\delta.
$$


The coefficient index occurring in the old $\kappa$-contraction is


$$
n_{uv}:=\kappa-s-t
=L_*-u-v,
\qquad
\kappa=\frac{3P-3}{2}.
\tag{2.3}
$$


Its smallest possible distance above $2\chi$ is


$$
\min_{u,v}(n_{uv}-2\chi)
=\frac{P+3}{2}-2\delta-2\chi.
\tag{2.4}
$$



If $\delta=\chi-1$, this is


$$
\frac{P+7}{2}-4\chi\equiv125\pmod{243}.
$$


If $\delta=(P+3)/2-3\chi$, it is


$$
4\chi-\frac{P+3}{2}\equiv120\pmod{243}.
$$


Both quantities are positive by the defining minimum for $\delta$. Hence


$$
\boxed{
2\chi+120\le n_{uv}\le L_*<P.
}
\tag{2.5}
$$



This strengthened, original-arithmetic gap will also pay the one- and two-step coefficient shifts in the prefix calculation. A merely asymptotic leading support statement would not be enough.

---

## 3. The corrected-pairing compression extends to $3^{32}$

Let


$$
N=3^{16},\qquad L=3^{h-17},\qquad H=NL.
$$


For integral $p_1,p_2$ with degrees at most $\nu-2$, the accepted $p=17$ trials are


$$
\widetilde F[p_i]=x^Dp_iR_N(y^L).
$$



The already paid errors remain:



$$
\begin{array}{c|c}
\text{error} & \text{valuation lower bound}\\ \hline
\text{stationary projection error} & 33\\
\text{exponential terms of order at least two} & 34\\
\text{bare macro-denominator replacement} & 35\\
\text{logarithmic reciprocal replacement} & 34\\
\text{complete-core transfer} & h
\end{array}
\tag{3.1}
$$



Only the active/inactive logarithmic macro split changes.

For a logarithmic term with $c=2s+1$, the potentially relevant scalar has valuation


$$
2h-1-v_3(c)-v_3(d_v),
\qquad v_3(c)\le h-26.
$$


To work modulo $3^{32}$, one must now retain


$$
v_3(d_v)\ge h-6,
\tag{3.2}
$$


including the layer $h-6$ previously omitted at valuation $31$. These denominators are still multiples of $L$. The reciprocal replacement has the same paid error $3^{34}$.

The newly inactive terms satisfy $v_3(d_v)\le h-7$, and therefore


$$
2h-1-(h-26)-(h-7)=32.
\tag{3.3}
$$


They may be added to the complete macro sum at the new precision.

All physical boundaries are unchanged:

* the trials still satisfy
  

$$
m-\deg\widetilde F[p_i]\ge\frac{L-4D+7}{2}>0;
$$


* the complete bare macro support satisfies
  

$$
(2N-1)L+\deg B
  \le2H-L+2D-5<K_{\mathrm{phys}};
$$


* the last nonzero completed macro term has denominator
  

$$
(4N-3)L<4H-4D+5;
$$


* the physical position $q_0=2N-1$ has the complete partial sum
  $A_0(1)=0$;
* the next macro position is outside the physical cutoff.

Thus the extra active layer is genuinely included rather than suppressed.

### Lemma 3.1 — Compression at precision $32$

On the same original indices,


$$
\boxed{
G_c(F[p_1],F[p_2])
\equiv K_N\mathcal J_h\!\left(
x^D(\beta+3y)p_1p_2
\right)\pmod{3^{32}},
}
\tag{3.4}
$$


where the established exact scalar $K_N$ is unchanged and


$$
K_N\equiv1\pmod3.
$$



The proof uses no filter beyond $p=17$.

All amplitude polynomials used in the double radical contraction remain in the admitted degree range. Indeed, $\deg g_s\le R$, and the one-lift polynomial part has degree at most


$$
b+k_0+R+3Q
=\frac{9Q+1}{2}+3R<\nu-2.
$$


The prefix columns also lie in that range. In Section 5, the last middle column is deliberately **not** brought into this compression lemma.

---

## 4. Evaluation of the double-radical pairing

### 4.1 Complete new pole-layer audit

Set


$$
X(y)=(y-1)^{10Q}.
$$


The polynomial before multiplication by the radical amplitudes is


$$
X(y)(\beta+3y)y^{3Q+1+w}(y^{3Q}+3)^2.
\tag{4.1}
$$


All its relevant degrees are below $2D$. Modulo $3^{32}$, the smallest relevant pole grid is now $Q/9$, not $Q/3$.

The complete layer list is:

| Denominator grid | Pole weight | New contribution that must be considered |
|---|---:|---|
| unit multiple of $Q/9$ | $3^{31}$ | coefficients of $X\bmod3$ |
| unit multiple of $Q/3$ | $3^{30}$ | none: coefficient valuation at least $2$ |
| unit multiple of $Q$ | $3^{29}$ | two high-term coefficients of valuation $2$ |
| unit multiple of $3Q$ | $3^{28}$ | valid bands have coefficient valuation at least $4$ |
| $9Q$ | $3^{27}$ | only the explicitly $9$-weighted low term can be in range; too deep |
| $27Q$ | $3^{26}$ | the old coefficient, its next neighboring $P$-bands, the $3y$ term, and the explicitly $6$-weighted middle term |

Here the fixed bound


$$
2b+4<\frac Q6
\tag{4.2}
$$


is retained.

At $27Q$, the high extraction is


$$
k=\frac{9Q-3}{2}-w.
$$


The coefficient of valuation $4$ is at $w=\kappa$. The additional coefficients of valuation $5$ are at


$$
w=\kappa-P,\qquad \kappa+P,\qquad \kappa+2P,
\tag{4.3}
$$


when those indices lie in the actual interval $0\le w\le2b$.

Their signed normalized units are, respectively,


$$
1,\qquad 2,\qquad 1.
\tag{4.4}
$$


For example, after stripping the common power of $3$, these are the signed normalized units of


$$
\binom{270}{121},\qquad
\binom{270}{119},\qquad
\binom{270}{118}.
$$


The factorial-unit calculation is recorded in Section 11.

The high $3y$ term contributes at valuation $31$, supported at


$$
w=\kappa-1.
\tag{4.5}
$$


The $6$-weighted middle term contributes at valuation $31$, supported at $w=\kappa$. The $9$-weighted low term is retained but is outside the possible contribution at this precision.

At the unit-$Q$ layer, the only valuation-$2$ high coefficients occur at the poles $19Q$ and $37Q$, both at $w=\kappa$. Their weighted normalized residues are $2$ and $1$, so their complete sum is zero modulo $3$.

At the newly active unit-$Q/9$ layer, an $X\bmod3$ coefficient can occur only at $w=\kappa$. Since


$$
X(y)\equiv1-y^Q-y^{9Q}+y^{10Q}\pmod3,
$$


the four denominators are


$$
(163+18u)\frac Q9,\qquad u=0,1,9,10.
$$


All four are physical and all four denominator units are $1\bmod3$. Their residues sum to


$$
1-1-1+1=0.
\tag{4.6}
$$


Thus this newly active layer cancels by a complete finite calculation, not by a support extrapolation.

### 4.2 What survives after the complete radical multiplication

For $s=L_*+u$, $t=L_*+v$, multiplication by the two radical amplitudes changes the finite factor to


$$
(1-y)^b g_s(y)g_t(y)
=y^{s+t}(1-y)^{2P+2\chi}.
\tag{4.7}
$$



Let


$$
F(y)=(1-y)^{2P+2\chi}.
$$


Modulo $3$,


$$
F(y)\equiv
(1+y^P+y^{2P})(1-y)^{2\chi}.
\tag{4.8}
$$


By (2.5), $n_{uv}$ lies in the gap above degree $2\chi$ and below $P$. Consequently:

* the valuation-$31$ terms supported at $w=\kappa$ vanish after contraction modulo $3$;
* those at $\kappa-P,\kappa+P,\kappa+2P$ also vanish, since they observe the corresponding gaps between the three bands in (4.8);
* the $3y$ term at $\kappa-1$ vanishes because $n_{uv}-1>2\chi$.

These observations do **not** dispose of the old valuation-$30$ term. Its coefficient is zero modulo $3$, and division by one further $3$ requires its value modulo $9$.

### 4.3 The extra Frobenius band modulo $9$

For a sufficiently large power $P$ of $3$,


$$
(1-y)^P
\equiv
1-3y^{P/3}+3y^{2P/3}-y^P\pmod9.
$$


Squaring gives


$$
(1-y)^{2P}
\equiv
(1-y^P)^2
+6(1-y^P)(-y^{P/3}+y^{2P/3})
\pmod9.
\tag{4.9}
$$



Since


$$
2\chi<n_{uv}\le L_*<\frac P2,
$$


only the band $-6y^{P/3}$ can contribute to the coefficient of $y^{n_{uv}}$. Therefore


$$
\frac{[y^{n_{uv}}]F(y)}3
\equiv
-2[y^{n_{uv}-P/3}](1-y)^{2\chi}
\equiv
[y^{\kappa_1-u-v}](1-y)^{2\chi}
\pmod3.
\tag{4.10}
$$


The division is paid because the coefficient was already proved divisible by $3$.

The old binomial normalized unit and $K_N$ are both $1\bmod3$. No new value of either modulo $9$ is needed: they multiply a coefficient already divisible by $3$.

### Theorem 4.1 — Evaluated double-radical complete pairing



$$
\boxed{
\frac{\mathscr G^T
G_c(\mathcal F,\mathcal F)\mathscr G}{3^{31}}
\equiv\mathsf D\pmod3,
}
\tag{4.11}
$$


with $\mathsf D$ given by (0.2).

This is the specific correction to the leading-support-gap argument. The first divided pairing digit is generally not zero.

---

## 5. The second-prefix return vanishes at the divided radical digit

The exact first-prefix relation is


$$
\mathsf A Z=d,
\qquad
d_{pa}=\frac{G_c(F_p,\mathcal F_a)}{3^{28}}.
$$


We prove the stronger radical-contracted statement


$$
\boxed{
\mathscr G^T Z^T\mathsf A Z\mathscr G\in9M.
}
\tag{5.1}
$$



### 5.1 The actual finite prefix through its next digit

Put


$$
U(y)=(1-y)^{N_0}.
$$


Define finite matrices, with $0\le p,q\le a_0$, by


$$
(A_0)_{pq}=U_{a_0-p-q},
$$




$$
(A_-)_{pq}=U_{a_0-1-p-q},
\qquad
(A_+)_{pq}=U_{a_0+3Q-p-q}.
$$


Negative coefficient indices are zero.

The same finite pole calculation, now modulo $9$ after the original $3^{26}$ normalization, gives


$$
\boxed{
\mathsf A\equiv
K_N\bigl(-2\beta A_0+3A_- -3\beta A_+\bigr)\pmod9.
}
\tag{5.2}
$$


For completeness, this uses


$$
x^{9Q}\equiv y^{9Q}-3y^{6Q}+3y^{3Q}-1\pmod9.
$$


At the $27Q$ pole, only the $y^{9Q}$ and $y^{6Q}$ bands can enter the finite prefix extraction. The $9Q$ pole supplies the additional $3\beta A_0$ term. All other poles have at least two normalized digits.

The exact finite inverse of $A_0$ is


$$
(A_0^{-1})_{pq}
=[y^{p+q-a_0}]U(y)^{-1}.
\tag{5.3}
$$


Its convolution boundaries are the original finite boundaries.

### 5.2 The residual support through modulo $9$

The new support statement is


$$
\boxed{
d_{pa}\equiv0\pmod9
\quad\text{unless}\quad
p+a+1\in\frac Q9\mathbb Z
\ \text{or}\
p+a+2\in\frac Q9\mathbb Z.
}
\tag{5.4}
$$


The previous support modulo $3$, with $Q/3$ in place of $Q/9$, is retained.

To check (5.4), consider the $27Q$ high extraction


$$
9Q-1-p-a-\epsilon,\qquad \epsilon=0,1.
$$


It lies in $4Q<k<9Q$. Outside the displayed $Q/9$-classes,


$$
v_3\binom{10Q}{k}\ge4,
$$


so the contribution is in $3^{30}$. The low extraction has its explicit factor $3$ and at least three coefficient digits. The other pole layers are still deeper at this precision. This proves (5.4) after the paid division by $3^{28}$.

The finite grid ranges are uniform in every allowed amplitude:


$$
p=k(3P)-a-\sigma,\qquad k=1,\ldots,40,
$$


or, for the leading support,


$$
p=k(9P)-a-\sigma,\qquad k=1,\ldots,13,
$$


where $\sigma\in\{1,2\}$. Both endpoints follow from
$0\le a\le R<P$ and $0\le p\le a_0$. Thus radical multiplication does not truncate these convolutions differently for different amplitudes.

Choose an integral lift $d_0$ of $d\bmod3$ on the $9P$-grid, and write


$$
d=d_0+3d_1.
$$


Modulo $3$, $d_1$ is supported on the $3P$-grid.

### 5.3 The inverse terms are all paid and evaluated

For the base inverse, the two radical factors change the generating function to


$$
U^{-1}(1-y)^{4\chi}
=(1-y)^{2P+2\chi-Q}.
\tag{5.5}
$$



For a cross term involving $d_0$ and $d_1$, its observed residue modulo $3P$ is


$$
n_{uv}-(\sigma+\tau-2).
$$


By (2.5), this lies above $2\chi$ and below $P$. But modulo $3$, the generating function in (5.5) has support only in


$$
[0,2\chi],\quad
[P,P+2\chi],\quad
[2P,2P+2\chi]
\pmod{3P}.
$$


Every cross coefficient is therefore zero.

For the $d_0$-$d_0$ term modulo $9$, the observed residue modulo $9P$ is


$$
3P+n_{uv}-(\sigma+\tau-2).
\tag{5.6}
$$


The numerator in


$$
\frac{(1-y)^{2P+2\chi}}{(1-y)^Q}
$$


has degree $2P+2\chi<3P$, while the denominator and its reciprocal modulo $9$ are series in $y^{Q/3}=y^{9P}$. The residue (5.6) is above that numerator degree. Hence the entire base contraction vanishes modulo $9$.

The $A_-$ correction shifts the inverse coefficient index by one. The gap in (2.5) still excludes it.

For the $A_+$ correction, let


$$
z_0=A_0^{-1}d_0\mathscr G.
$$


Because


$$
U^{-1}(1-y)^{2\chi}
=(1-y)^{2P-Q}
\equiv
\frac{1+y^P+y^{2P}}{1-y^Q}\pmod3,
$$


column $u$ of $z_0$ is supported on rows congruent to $u$ or $u+1$ modulo $P$.

Meanwhile,


$$
U(y)=(1-y)^{25P+2\chi}
\equiv(1-y^P)^{25}(1-y)^{2\chi}\pmod3.
$$


A potentially observed $A_+$ coefficient has residue


$$
n_{uv}-i-j,\qquad i,j\in\{0,1\},
$$


which remains above $2\chi$. Thus every such entry is zero.

Expanding the unit inverse in (5.2) modulo $9$ now proves (5.1). In particular,


$$
\boxed{
\frac{\mathscr G^T Z^T\mathsf A Z\mathscr G}{3}
\equiv0\pmod3.
}
\tag{5.7}
$$



---

## 6. The $J$-return, including the uncompressed finite boundary

Define the paid integral contracted coupling


$$
\mathscr L=\frac{L_c^TG\mathscr G}{3}.
\tag{6.1}
$$


Its integrality follows from the accepted $\gamma_c=0$.

We evaluate


$$
\mathscr L^T B_c^{-1}\mathscr L\pmod3
$$


without assuming a compression formula for $F_{\nu-1}$.

### 6.1 Interior $J$-couplings

For


$$
\ell\le v\le\tau-2,
$$


the tail column $F_{R_*+v}$ is within the admitted degree range.

Put


$$
\kappa_0=\frac{Q/3-3}{2}=\frac{9P-3}{2}.
$$


The required compressed cross polynomial is


$$
x^{10Q}(\beta+3y)y^{6Q+1+v+a}(y^{3Q}+3).
$$


Here


$$
v+a\le\frac{Q-7}{2}.
\tag{6.2}
$$


At the $27Q$ pole, the only valuation-$3$ high coefficient occurs at


$$
v+a=\kappa_0.
$$


Its signed normalized unit is $1$, obtained from
$\binom{30}{13}/3^3$. All other layers and the explicitly weighted terms are deeper. Therefore


$$
\frac{G_c(F_{R_*+v},\mathcal F_a)}{3^{29}}
\equiv\delta_{v+a,\kappa_0}\pmod3.
\tag{6.3}
$$



The finite prefix selector remains


$$
\left(\overline{\mathsf B_v/3}^{\,T}
\overline{\mathsf A}^{-1}\right)_p
=-\delta_{p,k_0+v}.
$$


At that selected row, a direct pole check gives


$$
d_{k_0+v,a}\equiv0\pmod3.
\tag{6.4}
$$


The upper bound (6.2) is important: it excludes the boundary extraction that appears at the last middle column.

Consequently, for interior $J$-rows,


$$
\boxed{
\overline{\mathscr L}_{v,u}
=
-[y^{\kappa_0-v-L_*-u}](1-y)^{2\chi}.
}
\tag{6.5}
$$



In coordinates $i=v-\ell$, this support lies in


$$
P+\chi-2-u\le i\le P+3\chi-2-u.
\tag{6.6}
$$


In particular, its first $J$-coordinate is zero, and all these finite coefficients lie strictly inside $J$.

### 6.2 The leading finite $J$-block

Let $N_J=n_J$. For rows and columns other than the last one, the accepted normalization gives


$$
\overline B_{c,ij}
=
[y^{N_0+N_J-1-i-j}](1-y)^{N_0}
=
-[y^{i+j-N_J+1}]U(y).
\tag{6.7}
$$


The prefix contribution to this leading $J$-block is zero because both prefix cross blocks are divisible by $3$.

The last row and column are not filled in by extrapolation. Write the actual leading matrix, ordered as first coordinate, interior coordinates, last coordinate, as


$$
\overline B_c=
\begin{pmatrix}
0&0&a\\
0&B_I&w\\
a&w^T&c
\end{pmatrix}.
\tag{6.8}
$$


Here $a,w,c$ are the actual boundary values. The established unit property of $B_c$ implies $a\ne0$, and


$$
(B_I^{-1})_{ij}
=-[y^{N_J-1-i-j}]U(y)^{-1},
\qquad 1\le i,j\le N_J-2.
\tag{6.9}
$$



This is a finite inverse: the interior block has dimension $N_J-2$.

### 6.3 Exact bordering identity

For any vector


$$
l=(0,l_I,l_\partial),
$$


direct elimination in (6.8) gives


$$
\boxed{
l^T\overline B_c^{-1}l
=l_I^TB_I^{-1}l_I.
}
\tag{6.10}
$$


Thus the unknown last coupling $l_\partial$, and the actual $w,c$, are retained but do not affect this quadratic expression.

For the supports in (6.6), all coefficient indices in (6.9) lie strictly between $b$ and $Q$. Yet


$$
U^{-1}=(1-y)^{b-Q}
\equiv\frac{(1-y)^b}{1-y^Q}\pmod3
$$


has no coefficients in that interval. Therefore


$$
\boxed{
\mathscr L^TB_c^{-1}\mathscr L\equiv0\pmod3.
}
\tag{6.11}
$$



This proves that the complete first $J$-matrix return is in $3^6M$ after double radical contraction:


$$
27\mathscr G^TG^TL_cB_c^{-1}L_c^TG\mathscr G
=3^5\mathscr L^TB_c^{-1}\mathscr L\in3^6M.
\tag{6.12}
$$



The argument does not evaluate the last coupling itself. Section 8 explains why that distinction matters for the endpoint.

---

## 7. The evaluated digit and its Smith consequences

### 7.1 Exact assembly of all matrix returns

The retained exact matrix identity is


$$
T_{c,\mathrm{red}}
=
-\frac{G_c(\mathcal F,\mathcal F)}{3^{26}}
-81Z^T\mathsf A Z
-27G^TL_cB_c^{-1}L_c^TG
-81M_{b,c}^TA_{b,c}^{-1}M_{b,c}.
\tag{7.1}
$$



The monomial complement from Turn 5 is


$$
\mathcal C=\{0,\ldots,R\}\setminus
\{L_*,\ldots,L_*+\delta-1\}.
$$


With


$$
K_c=T_{c,\mathrm{red}}/81,
$$




$$
A_c=E_{\mathcal C}^TK_cE_{\mathcal C},
\qquad
C_c=E_{\mathcal C}^TK_c\mathscr G,
$$


the exact lift is


$$
\widehat{\mathscr G}
=\mathscr G-E_{\mathcal C}A_c^{-1}C_c,
\qquad C_c\in3M.
$$


Its additional physical matrix return is


$$
81C_c^TA_c^{-1}C_c\in3^6M.
\tag{7.2}
$$



The rank-$b$ return is also in $3^6M$, since $M_{b,c}\in3M$. Combining (4.11), (5.7), (6.11), and (7.2) proves (0.1).

Every division in that assertion is now paid on the complete core.

### 7.2 Explicit value of every entry

For


$$
k=\kappa_1-u-v,
$$


the entry is zero if $k<0$ or $k>2\chi$. Otherwise, writing


$$
2\chi=\sum_i c_i3^i,\qquad k=\sum_i k_i3^i,
$$


gives


$$
\boxed{
\mathsf D_{uv}
=(-1)^k\prod_i\binom{c_i}{k_i}\quad\text{in }\mathbb F_3.
}
\tag{7.3}
$$


Thus it is zero if some $k_i>c_i$; otherwise it is


$$
(-1)^k2^{\,\#\{i:c_i=2,\ k_i=1\}}.
$$



The original arithmetic yields further evaluated support. From (2.1),


$$
\mathsf D_{uv}=0
\quad\text{unless}\quad
u+v\equiv121\pmod{243}.
\tag{7.4}
$$


Using (2.2), for sufficiently large original indices one has the sharper necessary condition


$$
u+v\equiv607,\ 850,\ \text{or }1093\pmod{2187}.
\tag{7.5}
$$



These are exact entry evaluations on the original parameters, not a numerical sample.

### 7.3 Exact ranks in the lower and upper ranges

Define


$$
B_1=2\chi+2\delta-1-\kappa_1,
\qquad
\varepsilon=2\chi+\delta-\Pi.
\tag{7.6}
$$



#### Range I: $B_1\le0$

All observed coefficient indices exceed $2\chi$. Hence


$$
\boxed{\mathsf D=0,\qquad \operatorname{nullity}\mathsf D=\delta.}
\tag{7.7}
$$



#### Range II: $0<B_1\le\delta$

Reverse both row and column orders. Since $2\chi$ is even, the coefficient sequence is symmetric, and the resulting entries are


$$
[y^{B_1-1-u-v}](1-y)^{2\chi}.
$$


Only the first $B_1$ reversed coordinates are active. Their block is anti-triangular with anti-diagonal $1$. Therefore


$$
\boxed{
\operatorname{rank}\mathsf D=B_1,\qquad
\ker\mathsf D
=\operatorname{span}\{e_0,\ldots,e_{\delta-B_1-1}\}.
}
\tag{7.8}
$$


The complementary last $B_1$ original monomials give an explicit unit block.

#### Range III: $\varepsilon>0$

In this range,


$$
\boxed{
\operatorname{nullity}\mathsf D=\varepsilon,\qquad
\operatorname{rank}\mathsf D=\Pi-2\chi.
}
\tag{7.9}
$$


A complete radical is


$$
\boxed{
(1-y)^{\Pi-2\chi}y^v,
\qquad 0\le v<\varepsilon,
}
\tag{7.10}
$$


in the $u$-coordinate polynomial space of degree at most $\delta-1$.

Here is the finite completeness proof.

Set


$$
a=\kappa_1+1=\frac{\Pi+1}{2},
\qquad b'=B_1,\qquad c=2\chi.
$$


The original inequalities and the definition of $\delta$ give


$$
a,b'>\delta-1,\qquad
a,b',c\le\Pi,\qquad
a+b'=2\chi+2\delta.
$$


The selected graded map has source degree $\delta-1$, multiplier degree $2\chi$, and target degree


$$
D_1=2\chi+\delta-1=\Pi+\varepsilon-1.
$$


Its surviving target interval is exactly


$$
[\kappa_1-\delta+1,\kappa_1].
$$



The three forms


$$
X^a,\quad Y^{b'},\quad (Y-X)^c
$$


have the primitive syzygy


$$
S=
\left(
X^{\Pi-a},\
-Y^{\Pi-b'},\
(Y-X)^{\Pi-c}
\right),
\tag{7.11}
$$


of total degree $\Pi$, because


$$
X^\Pi-Y^\Pi+(Y-X)^\Pi=0.
$$



If $T$ is any syzygy of degree $D_1$, the cross-product argument used in Turn 5 would give a polynomial multiplier of degree


$$
\Pi+D_1-(a+b'+c)
=-\varepsilon-1<0.
$$


It must vanish. Primitivity then forces


$$
T=fS,\qquad \deg f=\varepsilon-1.
$$


The third components give precisely (7.10). This proves completeness with the actual finite degrees and boundaries.

The first $\varepsilon$ coefficient rows of (7.10) are triangular with diagonal $1$. Thus these integer lifts are saturated, and the monomials with indices


$$
\varepsilon,\ldots,\delta-1
$$


give an explicit complement. Its restriction is a unit form modulo $3$.

#### Remaining range

The range


$$
B_1>\delta,\qquad \varepsilon\le0
\tag{7.12}
$$


has an explicitly evaluated matrix by (7.3), but a uniform closed rank formula is not proved here.

In that range $\delta=\chi-1$, and the precise remaining finite syzygy problem is the triple


$$
X^{(\Pi+1)/2},\qquad
Y^{\,4\chi-(\Pi+5)/2},\qquad
(Y-X)^{2\chi}
$$


at total degree $3\chi-2$. This is a concrete finite rank obligation, not an uncomputed Smith condition presented as an answer.

### 7.4 Exact improvement of the core Smith budget

Let


$$
r_1=\operatorname{rank}_{\mathbb F_3}\mathsf D.
$$


Then the complete-core matrix $T_{c,\mathrm{red}}$ has:

* exactly $R+1-\delta$ elementary divisors of valuation $4$;
* exactly $r_1$ elementary divisors of valuation $5$;
* all remaining elementary divisors of valuation at least $6$, or zero.

In Ranges I–III, $r_1$ is explicitly given above.

A unit complement of $-\mathsf D$ has physical inverse cost $3^{-5}$. Any new radical cross block is in $3^6M$, so its displacement is in $3M$ and its new matrix return is in $3^7M$.

This is a genuine complete-core Smith-layer improvement. It is not yet a directional estimate for the complete producer.

---

## 8. Complete core endpoint and diagonal: retained returns and the surviving obstruction

The matrix result does not determine the complete bordered result.

Let all endpoint symbols below denote the actual complete-core endpoints after the preceding prescribed returns—not bare polynomial evaluation.

Retain


$$
f_c^{(2)}
=f_{c,K}-3L_cB_c^{-1}f_{c,J},
$$




$$
\lambda_c^{(2)}
=\lambda_c-\frac13f_{c,J}^TB_c^{-1}f_{c,J},
$$




$$
f_{c,\mathrm{new}}
=f_{c,R}-3M_{b,c}^TA_{b,c}^{-1}f_{c,b},
$$




$$
\lambda_{c,\mathrm{new}}
=\lambda_c^{(2)}
-\frac19f_{c,b}^TA_{b,c}^{-1}f_{c,b}.
\tag{8.1}
$$



Put


$$
f_C=E_{\mathcal C}^Tf_{c,\mathrm{new}},
\qquad
f_G=\mathscr G^Tf_{c,\mathrm{new}}.
$$


The new monomial-complement return is exactly


$$
\boxed{
f_{\mathrm{rad}}
=f_G-C_c^TA_c^{-1}f_C,
}
\tag{8.2}
$$




$$
\boxed{
\lambda_{\mathrm{rad}}
=\lambda_{c,\mathrm{new}}
-\frac1{81}f_C^TA_c^{-1}f_C.
}
\tag{8.3}
$$



The physical $3^{-4}$ inverse is therefore present in the diagonal channel. The fact that its **matrix** return is in $3^6M$ does not make (8.3) negligible.

### 8.1 Why the finite terminal coupling cannot be discarded for the endpoint

For the actual leading $J$-block (6.8), write


$$
l=(0,l_I,l_\partial),\qquad
f=(f_0,f_I,f_\partial).
$$


Direct solution gives


$$
\boxed{
l^T\overline B_c^{-1}f
=
l_I^TB_I^{-1}\left(f_I-\frac wa f_0\right)
+\frac{l_\partial f_0}{a}.
}
\tag{8.4}
$$



Equation (6.10) made $l_\partial$ invisible to the matrix quadratic return. Equation (8.4) shows that it is generally visible to the endpoint return.

Thus the precise unresolved boundary datum is


$$
\left(\frac{L_c^TG\mathscr G}{3}\right)_{\tau-1,\bullet}
\pmod3
$$


together with the first actual $J$-endpoint coordinate and its returned interior combination. The closed terminal congruence at precision $28$, and $\gamma_c=0$, pay the division but do not evaluate this next residue.

This is a specific surviving obstruction, not a generic warning about endpoints.

### 8.2 The required complement data

Writing


$$
C_c=3C_1,
$$


equation (8.2) gives, for integral normalized endpoint data,


$$
f_{\mathrm{rad}}\equiv f_G\pmod3,
$$


but modulo $9$ it requires


$$
f_{\mathrm{rad}}
\equiv f_G-3C_1^TA_c^{-1}f_C\pmod9.
\tag{8.5}
$$


Hence the next endpoint digit requires the actual cross residue


$$
\boxed{
\overline{C_1}
=
\frac{E_{\mathcal C}^TT_{c,\mathrm{red}}\mathscr G}{3^5}
\pmod3,
}
\tag{8.6}
$$


not just the double-radical contraction evaluated in this report.

For the diagonal, set


$$
q_C=f_C^TA_c^{-1}f_C.
$$


The exact condition that the new diagonal retain the normalization
$\lambda_{\mathrm{rad}}\in3^{-1}\mathbb Z_3$ is


$$
\boxed{
81\lambda_{c,\mathrm{new}}-q_C\in27\mathbb Z_3.
}
\tag{8.7}
$$


If this is paid, its normalized unit digit is


$$
\boxed{
3\lambda_{\mathrm{rad}}
=\frac{81\lambda_{c,\mathrm{new}}-q_C}{27}.
}
\tag{8.8}
$$


Neither the divisibility in (8.7) nor the unit value in (8.8) follows from (0.1).

Without additional endpoint divisibility, evaluating (8.8) requires the numerator modulo $81$. This can expose more digits of the complementary inverse than the first radical matrix digit required.

### 8.3 Concrete follow-on core lemma

The complementary core task is now precise:

> **Core bordered-radical lemma.** On the same original indices:
>
> 1. evaluate the physical last-row residue in (8.4), using the actual finite corrected columns;
> 2. evaluate the complete returned $f_G,f_C$ and the cross digit (8.6), sufficiently to determine $f_{\mathrm{rad}}\bmod9$;
> 3. evaluate $81\lambda_{c,\mathrm{new}}-q_C\bmod81$, proving or disproving the three paid zero digits required by (8.7), and then determining (8.8);
> 4. only after these evaluations, adapt the evaluated matrix $-\mathsf D$ to the actual endpoint.

The supplied reports give exact return identities but do not supply the additional endpoint and diagonal residues in this lemma. Consequently, this report does not label (8.2)–(8.8) as an evaluated endpoint or diagonal answer.

This remaining task concerns the **core border**. It does not duplicate A4’s separate complete-producer calculation.

---

## 9. Why no unbounded mechanism has yet been proved

At the next matrix digit, valuation $6$, several returns become active simultaneously.

Set


$$
\mathscr M=\frac{M_{b,c}\mathscr G}{3},
\qquad C_1=C_c/3.
$$


The exact returned radical matrix contains the following terms:


$$
-\frac{\mathscr G^TG_c(\mathcal F,\mathcal F)\mathscr G}{3^{26}},
$$




$$
-81\,\mathscr G^TZ^T\mathsf A Z\mathscr G,
$$




$$
-3^5\,\mathscr L^TB_c^{-1}\mathscr L,
$$




$$
-3^6\,\mathscr M^TA_{b,c}^{-1}\mathscr M,
$$




$$
-3^6\,C_1^TA_c^{-1}C_1.
\tag{9.1}
$$


At valuation $6$, the corresponding divided quantities include


$$
\frac{\mathscr G^TZ^T\mathsf A Z\mathscr G}{9},
\qquad
\frac{\mathscr L^TB_c^{-1}\mathscr L}{3},
\qquad
\mathscr M^TA_{b,c}^{-1}\mathscr M,
\qquad
C_1^TA_c^{-1}C_1.
\tag{9.2}
$$



None may be deleted because it was invisible at valuation $5$. In particular, the Turn 5 monomial-complement return is now active.

There is a repeatable-looking Frobenius feature in the moment term, but a repeatable **returned arithmetic mechanism** has not been proved. Such a mechanism would have to evaluate (9.2), its directional forcing, the complete endpoint and diagonal, and all finite boundaries at each iteration.

There are also endpoint-independent obstructions already visible:

* in Range I, the entire first divided radical digit is zero;
* in Range III, its complete radical has dimension $\varepsilon$, so every endpoint-annihilator meets it in dimension at least $\varepsilon-1$.

For example, in the upper branch


$$
\delta=\frac{P+3}{2}-3\chi,
$$


one has


$$
\varepsilon=\frac{P/3+3}{2}-\chi
>\frac{23}{750}P+\frac32.
$$


Thus a further nonsingular-digit argument is again obstructed there, regardless of which endpoint functional is later inserted.

These are core obstructions. They do not decide whether the complete producer fills some of the radical.

---

## 10. Producer separation and the unchanged global normalization

### 10.1 The complete forcing is retained

The actual producer remains


$$
Q_{\mathrm{act}}=3P_n=Q_c+3^7\mathscr R,
$$




$$
3^7\mathscr R=\sum_{a=0}^{A+1}e_ax^a,
\qquad
e_a=-\frac{(A+1)!}{a!}(t_a+\xi v_a),
$$


with the complete force


$$
t=
3nh_{\mathrm{vec}}
+(b_{\mathrm{force}}+6)e_{n-1}
+\frac{2b_{\mathrm{force}}}{n-1}e_{n-2},
\qquad
b_{\mathrm{force}}=-n-66.
\tag{10.1}
$$


The signed, paid $\xi$ and the entire $t+\xi v$ remain present. Also retained are


$$
\mathscr R(-1)
=-\frac{\xi((A+1)!)^2}{3^7},
$$




$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\mathrm{ret}}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{10.2}
$$



The precision-$31$ supported multiplier from the coordinator ledger is not used to identify the actual producer with the core. It does not evaluate the returned producer residues or the bordered quantities above.

For $\alpha=c,\mathrm{act}$, all three return channels remain


$$
\mathcal S_\alpha^{(2)}
=\mathcal R_{\alpha,KK}
-27L_\alpha B_\alpha^{-1}L_\alpha^T,
$$




$$
f_\alpha^{(2)}
=f_{\alpha,K}-3L_\alpha B_\alpha^{-1}f_{\alpha,J},
$$




$$
\lambda_\alpha^{(2)}
=\lambda_\alpha-\frac13
f_{\alpha,J}^TB_\alpha^{-1}f_{\alpha,J},
$$


and


$$
T_{\alpha,\mathrm{red}}
=T_{\alpha,RR}
-81M_{b,\alpha}^TA_{b,\alpha}^{-1}M_{b,\alpha},
$$




$$
f_{\alpha,\mathrm{new}}
=f_{\alpha,R}
-3M_{b,\alpha}^TA_{b,\alpha}^{-1}f_{\alpha,b},
$$




$$
\lambda_{\alpha,\mathrm{new}}
=\lambda_\alpha^{(2)}
-\frac19f_{\alpha,b}^TA_{b,\alpha}^{-1}f_{\alpha,b}.
\tag{10.3}
$$



The complete-source recurrence and its genuine resonance divisor are likewise unchanged:


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad 0\le t\le2n-2,
$$


with


$$
t_*=\frac{3^h-5}{2}.
$$



### 10.2 Actual contents, least clearer, and all-prime gcd

No new global content division is asserted. The local unit inverses and saturated amplitude changes do not redefine the actual column contents or the least simultaneous clearer $\ell_{\mathrm{clr}}$.

Retain


$$
A_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_0,
\qquad
B_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|).}
$$


For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole error remains exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\mathrm{clr}}^{m+1}}
{g_\ell}\det H_{\mathrm{complete}}.
}
\tag{10.4}
$$



An irrationality proof still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad
\det H_{\mathrm{complete}}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\mathrm{clr}}
-\log|\det H_{\mathrm{complete}}|
\longrightarrow+\infty.
}
\tag{10.5}
$$



The new core Smith-layer information establishes none of these final nonvanishing or decay assertions. Determinant content from a growing radical can occur in both distinguished cofactors and disappear under the final primitive normalization.

---

## 11. Bounded exact-arithmetic receipt

No tool computation was performed. The proofs above are symbolic. No closed binomial-$(90,40)$ table or dense original matrix calculation is requested.

An optional new finite receipt checks the small normalized units used at the new pole layer.

### Inputs

The integers


$$
270,\ 118,\ 119,\ 121,\ 149,\ 151,\ 152,\ 30,\ 13,\ 17.
$$


For each, compute:

1. the finite Legendre sum $v_3(n!)$;
2. the factorial unit modulo $3$, using either
   

$$
\frac{n!}{3^{v_3(n!)}}
   \equiv(-1)^{v_3(n!)}\prod_i n_i!\pmod3,
$$


   or a single bounded factorial-unit pass through $1,\ldots,270$.

This requires no Pascal table and no large integer binomial expansion.

### Expected verifiable outputs



$$
\begin{array}{c|r|c}
n&v_3(n!)&n!/3^{v_3(n!)}\pmod3\\ \hline
270&134&1\\
118&57&2\\
119&57&1\\
121&58&1\\
149&71&2\\
151&72&1\\
152&72&2\\
30&14&1\\
13&5&2\\
17&6&1
\end{array}
$$


Consequently,


$$
\boxed{
\binom{270}{118}\equiv243\pmod{729},
\qquad
\binom{270}{119}\equiv243\pmod{729},
\qquad
\binom{270}{121}\equiv486\pmod{729},
}
$$


and


$$
\boxed{\binom{30}{13}\equiv54\pmod{81}.}
$$


After the coefficient signs are included, these give (4.4) and the unit in (6.3).

This receipt verifies only those bounded universal constants. It is not a computation of an original index or evidence for an infinite-family claim.

---

## 12. Division ledger and conclusion

| Operation | Exact status at the present digit |
|---|---|
| $p=17$ corrected-pairing compression | Extended to $3^{32}$, with the $h-6$ macro layer included |
| Physical pole cutoff | Unchanged: largest denominator $4H-4D+5$ |
| Double radical pairing | Division by $3^{31}$ paid and evaluated |
| Modulo-$9$ Frobenius band | Evaluated; produces $\mathsf D$ |
| Second-prefix radical contraction | In $9M$; its physical return is in $3^6M$ |
| First $J$-inverse | Physical cost $3^{-1}$, retained |
| Last middle boundary in $J$ | Retained by exact bordering, not compressed beyond the admitted range |
| First $J$-matrix return | Evaluated as zero at the $3^5$ digit |
| Rank-$b$ inverse | Physical cost $3^{-2}$; matrix return in $3^6M$ |
| Turn 5 monomial complement | Physical cost $3^{-4}$; matrix return in $3^6M$ |
| New unit complement of $\mathsf D$, where evaluated | Physical cost $3^{-5}$ |
| Endpoint returns | Full terms retained; numerical residues remain open |
| Diagonal returns | Full $1/3$, $1/9$, and new $1/81$ terms retained |
| Global contents and primitive quotient | Unchanged; no new global division claimed |

### New proved result

On the same sufficiently large original indices,


$$
\boxed{
\frac{\widehat{\mathscr G}^{\,T}
T_{c,\mathrm{red}}\widehat{\mathscr G}}{3^5}
\equiv
-\left(
[y^{(P/3-1)/2-u-v}](1-y)^{2\chi}
\right)_{0\le u,v<\delta}
\pmod3.
}
$$



The second-prefix and $J$-matrix returns have been evaluated at exactly the precision needed for this identity. The newly active pole layers and the extra Frobenius band modulo $9$ have been included. Exact second-layer ranks, radicals, and complements are proved in the ranges specified in Section 7.

### Exact remaining bottlenecks

1. **Core bordered arithmetic:** the actual terminal coupling in (8.4), the cross digit (8.6), the complete returned endpoint, and the divided diagonal numerator in (8.7)–(8.8).
2. **Further core layers:** all four complementary returns in (9.2), which become active at the next digit.
3. **Actual transfer:** A4’s complete returned producer and endpoint must be inserted; the core cannot replace them.
4. **Global irrationality:** same-index nonvanishing and decay of the whole error after the actual contents, least simultaneous clearer, all-prime gcd, and primitive denominator.

The first divided radical matrix obligation is therefore closed. The complete bordered directional obligation, the unbounded primitive saving, and the global objective are not.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


