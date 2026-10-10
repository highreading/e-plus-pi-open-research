> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 7 — Closing operator continuity and transferring the separator theorem to the complete original family

## Executive conclusions

The supplied operator formulas close OPC. No new evaluation of the accepted $u_0$ arrays is needed.

More precisely, the formulas imply the following sufficient bounds:



$$
\boxed{
b\equiv b_0\pmod{2^{39}}
\quad\Longrightarrow\quad
\text{all precision-32 operator and finite-Schur input arrays agree}.
}
$$



For the complete downstream formulas, including both forces, both finite returns, the exterior principal part and reconstruction, a sufficient bound is



$$
\boxed{
b\equiv b_0\pmod{2^{40}}.
}
$$



Thus the coordinator’s proposed **41-bit guard is valid**. The bounds $39$ and $40$ are sufficient bounds proved below, not claims of optimality.

After reviewing the zero-separator argument, I retain its conclusion and supply a more explicit justification of its unsupported-row step. It now transfers unconditionally, within the established complete-producer identities, to the original family


$$
b(u)=9^{18+32u},\qquad u\ge0.
$$


The transfer retains the physical range


$$
\boxed{0\le j\le b(u)}
$$


and includes the complete forcing and terminal exterior.

Three further arithmetic advances follow.

1. **Complete-original-family noncontinuity.** Infinitely many original parameters in arbitrarily small binary neighborhoods of $b_0$ satisfy
   

$$
v_2(D_{\rm raw})\ge34,\qquad v_2(E_{\rm raw})\ge35,
$$


   whereas the accepted depths at $b_0$ are $33,34$. Consequently, the complete raw norm—and the norm divided by the fixed factor $2^{18}$—is not $2$-adically continuous at $b_0$ on the original parameter set. This is not a claim about normalization by the *actual varying* row content.

2. **A content-paid common-factor theorem.** If the high block has coordinate content $2^c$ and norm depth $t$, the physical comparison improves to
   

$$
D_{\rm raw}(b)\equiv S D_{\rm raw}(b_0)\pmod{2^{42+c}},
   \qquad
   E_{\rm raw}(b)\equiv S E_{\rm raw}(b_0)\pmod{2^{41+c}},
$$


   for $c\le22$. The first physical content is then exactly $9+c$. Every division by the high norm pays its true depth $t$.

3. **A target-specific high-block observable.** The first three bits of the high norm after removal of its exact coordinate content can be obtained from an **eight-state valuation counter**, without evaluating any odd factorial units. This uses the actual finite high-block summand and endpoint. In particular, for $h=4H+3$,
   

$$
\boxed{
   S_{L,h}\equiv
   2\binom{4003H+3002}{H}\pmod4.
   }
$$


   Therefore
   

$$
\boxed{
   v_2(S_{L,h})=1
   \iff
   H\mathbin{\&}(4002H+3002)=0.
   }
$$


   This condition depends on the entire relevant high word. The hypothesis $h\equiv3\pmod4$ alone proves only evenness.

These results do not evaluate the final all-prime gcd or the whole same-index real error. Irrationality of $e+\pi$ remains unresolved.

No code was executed for this report. No accepted $u_0$ operator, numerator, witness, block or Gram calculation is proposed for repetition.

---

# 1. Preserved objects and accepted finite information

Write


$$
b_0=9^{18}=150094635296999121,\qquad
n_0=4002b_0.
$$


The accepted complete physical columns at this word are $X_0,Y_0$, over


$$
0\le j\le b_0.
$$


Their established binary contents and whole contractions are


$$
v_2(\operatorname{content}X_0)=9,\qquad
v_2(\operatorname{content}Y_0)\ge10,
$$




$$
D_0=X_0^TX_0,\qquad E_0=X_0^TY_0,
$$




$$
\boxed{
D_0\equiv285\,2^{33}\pmod{2^{42}},\qquad
E_0\equiv13\,2^{34}\pmod{2^{41}}.
}
\tag{1.1}
$$


Thus


$$
v_2(D_0)=33,\qquad v_2(E_0)=34,
$$


and


$$
\boxed{\frac{E_0}{2D_0}\equiv49\pmod{128}.}
\tag{1.2}
$$



The short numerator arrays of orders $63,62$ remain precision-32 presentations of the complete columns, not characteristic-zero identities for those short orders.

## 1.1 The new direct witness/block receipt

The independently authored small-table calculation corroborates, without importing the Gram transport,



$$
X_0(j_*)\equiv512\pmod{1024},
$$


the normalized octet weights


$$
433\pmod{512},
$$


and


$$
\frac{\text{specified sixteen-row norm}}{2^{22}}
\equiv41\pmod{256}.
$$



The unit-table method has the correct scope: the combined atom valuation is at least $8$, so twelve unit bits suffice for twenty coordinate bits. The squared-coordinate comparison then supports the reported block modulus $2^{30}$.

This is independent finite corroboration of that witness and block. It is not a second proof of the complete norm depth $33$, and it supplies no all-prime normalization. I accept its stated finite outputs without rerunning them.

---

# Part I. OPC is closed

# 2. The integer-valued binomial continuity lemma

For $r\ge1$, integral $x,t$, and $L\ge0$, Vandermonde’s identity gives


$$
\binom{x+2^Lt}{r}-\binom xr
=
\sum_{i=1}^{r}\binom{2^Lt}{i}\binom{x}{r-i}.
$$


Using


$$
\binom{2^Lt}{i}
=\frac{2^Lt}{i}\binom{2^Lt-1}{i-1},
$$


we obtain


$$
v_2\!\left(\binom{2^Lt}{i}\right)\ge L-v_2(i).
$$


Therefore


$$
\boxed{
v_2\!\left(\binom{x+2^Lt}{r}-\binom xr\right)
\ge L-\lfloor\log_2r\rfloor.
}
\tag{2.1}
$$



For an affine top $ab+d$, the corresponding bound is


$$
\boxed{
v_2\!\left(
\binom{ab'+d}{r}-\binom{ab+d}{r}
\right)
\ge
L+v_2(a)-\lfloor\log_2r\rfloor
}
\tag{2.2}
$$


when $b'-b\in2^L\mathbb Z$ and $a\ne0$. For $r=0$, the difference is zero.

These formulas apply to generalized binomials with negative integral top as well. All such binomials are integers. There is no additional factorial-denominator loss after passing to this integer-valued form.

---

# 3. The exact divided-power symbol and inverse

Set


$$
M=32,\qquad m=4(M-1)=124,\qquad h=2001b.
$$



Let $V$ be the fixed divided-power polynomial with coefficient vector


$$
(0,-1,2,-3,3).
$$


If $d_{a,s}$ denotes the coefficient of its $a$-th divided-power product, then the source recurrence is


$$
d_{0,0}=1,
$$




$$
d_{a+1,s}
=
\sum_{\substack{0\le j\le4\\0\le s-j\le4a}}
\binom sj d_{a,s-j}v_j.
\tag{3.1}
$$


Thus


$$
d_{a,s}\in\mathbb Z,\qquad d_{a,s}=0\quad(s>4a),
$$


and the source symbol is exactly


$$
\boxed{
\lambda_s(b)
=
\sum_{a=0}^{31}2^a\binom{2001b}{a}d_{a,s}
\pmod{2^{32}},
\qquad 0\le s\le124.
}
\tag{3.2}
$$



The omitted terms $a\ge32$ have an explicit factor $2^{32}$. Their omission is uniform in the integral parameter $b$.

Since $v_0=0$,


$$
\lambda_0=1.
$$


For $s>0$, only $a\ge\lceil s/4\rceil$ occur, so


$$
\boxed{v_2(\lambda_s)\ge\lceil s/4\rceil.}
\tag{3.3}
$$



The inverse coefficients satisfy the integral convolution


$$
CC_0=1,
$$




$$
\boxed{
CC_s
=
-\sum_{t=1}^{s}\binom st\lambda_tCC_{s-t},
\qquad1\le s\le124.
}
\tag{3.4}
$$


Induction gives


$$
v_2(CC_s)\ge\lceil s/4\rceil.
\tag{3.5}
$$


The same filtration proves that coefficients beyond $124$ vanish modulo $2^{32}$: their depth is at least


$$
\lceil125/4\rceil=32.
$$



Consequently the finite convolution identities are not merely numerical accidents at $b_0$. The finite precision-32 truncation is uniform.

## 3.1 Parameter continuity of both coefficient arrays

In (3.2), the affine coefficient $2001$ is odd. For $a\ge1$,


$$
v_2\!\left(
2^a\left[\binom{2001b'}a-\binom{2001b}a\right]
\right)
\ge L+a-\lfloor\log_2a\rfloor\ge L+1.
$$


Hence


$$
\lambda(b')-\lambda(b)\in2^{L+1}\mathbb Z^{125}.
\tag{3.6}
$$


The integral recurrence (3.4) then gives the same bound for $CC$.

No inversion, nonunit division or parameter-dependent sign occurs in these two stages.

---

# 4. Every finite operator and Schur array

It is useful to rewrite the source formulas with their actual indices.

Define


$$
\mathrm{neg}_r=\binom{-4002b}{r},
\qquad0\le r\le371,
$$




$$
\mathrm{pos}_r=\binom{4002b}{r},
\qquad0\le r\le123.
$$



For $0\le i\le247$, put $d=248-i$. Then


$$
\boxed{
F_{i,r}
=
-\sum_{v=0}^{r}
\binom{-4002b}{d+v}\binom{4002b}{r-v},
\qquad0\le r\le123.
}
\tag{4.1}
$$


The leading minus sign is retained. The largest lower index is


$$
d+v\le248+123=371.
$$



For $0\le r,t\le123$, write $s=124+r-t$. The exact finite crossing matrix is


$$
\boxed{
\overline K_{r,t}
=
\begin{cases}
\lambda_s\binom{b+r}{s},&1\le s\le124,\\
0,&\text{otherwise}.
\end{cases}
}
\tag{4.2}
$$



The other finite factor is


$$
\boxed{
G_{t,r}
=
\sum_{s=0}^{124}
CC_s\binom{b-124+t}{s}F_{124+t-s,r},
\qquad0\le t,r\le123.
}
\tag{4.3}
$$


The row index of $F$ is always between $0$ and $247$. There is no out-of-range completion implicit in this formula.

Finally,


$$
\boxed{S_{\rm end}=I+G\overline K.}
\tag{4.4}
$$



## 4.1 Explicit continuity budget

The affine coefficients and sufficient losses are:

| Array/input | Affine top coefficient | Largest lower index | Guaranteed difference depth |
|---|---:|---:|---:|
| $\mathrm{neg}$ | $-4002$, depth $1$ | $371$ | $L-7$ |
| $\mathrm{pos}$ | $4002$, depth $1$ | $123$ | $L-5$ |
| $\binom{b+r}{s}$ | $1$ | $124$ | $L-6$ |
| $\binom{b-124+t}{s}$ | $1$ | $124$ | $L-6$ |
| $\lambda,CC$ | as in §3 | $31$ | $L+1$ |
| $F$ | integral sum/products | — | $L-7$ |
| $\overline K$ | integral products | — | at least $L-6$ |
| $G$ | integral sum/products | — | $L-7$ |
| $S_{\rm end}$ | integral products | — | at least $L-7$ |

These conservative bounds already show that $L=39$ suffices for precision $32$.

The filtration gives stronger bounds for some entries, but those improvements are unnecessary for closing OPC.

## 4.2 Uniform integrality of the Schur inverse

Every nonzero entry of $\overline K$ contains $\lambda_s$ with $s\ge1$, and therefore is even. Hence, uniformly in the integral parameter,


$$
\boxed{S_{\rm end}\equiv I\pmod2.}
\tag{4.5}
$$


In particular, $S_{\rm end}$ is invertible over $\mathbb Z_2$.

The exact inverse-difference identity is


$$
S_{\rm end}(b')^{-1}-S_{\rm end}(b)^{-1}
=
S_{\rm end}(b')^{-1}
\bigl(S_{\rm end}(b)-S_{\rm end}(b')\bigr)
S_{\rm end}(b)^{-1}.
\tag{4.6}
$$


Both outside factors are integral. Inversion loses no binary precision.

This also explains why the source’s pivot strategy is legitimate: Gaussian elimination starting from a matrix congruent to $I\pmod2$ continues to have odd diagonal pivots.

---

# 5. The padded finite boundary and adjoint check

The source’s auxiliary inverse solve has exactly $372$ rows and $124$ columns:


$$
\operatorname{origin}=b-372,\qquad j=b-372+i,\quad0\le i\le371.
$$


Its terminal injections are at


$$
j=b-124+t,\qquad0\le t\le123.
$$


The recurrence is


$$
Z_{i,t}
=
\mathbf1_{j=b-124+t}
-
\sum_{s=1}^{\min(124,371-i)}
\lambda_s\binom{j+s}{s}Z_{i+s,t}.
\tag{5.1}
$$


The upper boundary is the actual finite boundary $371$, not an infinite extension.

The variable top in the weights is


$$
j+s=b-372+i+s,
$$


with affine coefficient $1$ and lower index at most $124$. Thus this entire finite recursion also varies integrally with the parameter.

Moreover, the lower padded zero block has an algebraic explanation. The divided-power inverse entry from row $j$ to $j+r$ is


$$
CC_r\binom{j+r}{r}.
$$


For a row $i<124$ and a terminal source $t$, the required shift is


$$
r=248+t-i\ge125.
$$


Its inverse coefficient vanishes modulo $2^{32}$. Therefore


$$
\boxed{Z_{i,t}=0\pmod{2^{32}}\qquad(i<124)}
\tag{5.2}
$$


uniformly—not only at the inspected word.

The adjoint expression


$$
I+\overline K^T F^T Z[124:]
$$


has the stated finite shapes. Its agreement with $S_{\rm end}^T$ at $b_0$ is accepted finite evidence; its parameter continuity follows from the same integral formulas. No new boundary assertion is inferred merely from the receipt.

### OPC conclusion

All required inputs


$$
\lambda,\quad CC,\quad\overline K,\quad S_{\rm end}^{-1}
$$


and the auxiliary arrays $F,G,S_{\rm end},Z$ are unchanged modulo $2^{32}$ whenever


$$
\boxed{b\equiv b_0\pmod{2^{39}}.}
\tag{5.3}
$$



This closes the previously outstanding operator-parameter lemma.

---

# 6. Complete downstream continuity, with all parameter dependence recorded

The supplied downstream source uses the fixed dimensions


$$
I=72,\quad m=124,\quad R=160,\quad L_0=284,\quad K_0=196,
$$




$$
\mathrm{JET}=247,\qquad \mathrm{MAX}=371.
$$



The following list accounts for the variable parameter inputs.

### Central series and first force

The central binomials have tops


$$
2001b-j-\delta,\qquad2001b+j,
$$


and lower index $s\le35$. Their affine coefficient is $2001$, which is odd.

The central prefactors use


$$
4002b+2t\pm1,\qquad2001b-t.
$$


The first-force products use


$$
4002b+t.
$$


All are integral products.

The fixed rational central factors have odd reduced denominators and nonnegative binary valuations. They introduce no loss.

### Exterior and complete exterior load

The retained factorial exterior is


$$
v_t=(b+1)\cdots(b+t),\qquad0\le t\le35.
$$


The upper exterior uses


$$
\binom{4002b}{t-r},\qquad t-r\le35.
$$


The complete $160$-entry load uses


$$
\lambda_s\binom{b+r}{s},\qquad s\le124.
$$



### Laurent construction and jets

The variable-top binomial tables are exactly:



$$
\begin{array}{c|c|c}
\text{table or expression}&\text{top}&\text{lower-index bound}\\ \hline
\mathrm{POS}&4002b&159\\
\mathrm{TP}&4002b+k-1&531\\
\mathrm{TP2}&8004b+196+k-1&531\\
\text{reconstructed TP}&4002b+k&531\\
\text{reconstructed TP2}&8004b+196+k&531\\
\mathrm{CHOOSE}&b-1-k&124\\
\mathrm{RISING\_CHOOSE}&b-r+s-1&124\\
\mathrm{DERIV}&4002b+\mathrm{extra}+e-1&124\\
F_f\text{ and polynomial source}&b-1-k\text{ or }b-1-dd&71
\end{array}
$$


Here $\mathrm{extra}\in\{0,72\}$, and all other indices have the source’s finite ranges.

The only lower indices reaching $531$ occur with affine coefficients $4002$ or $8004$, of depths $1,2$. Thus their worst loss is


$$
9-1=8.
$$


The coefficient-$1$ binomials have lower index at most $124$, with loss at most $6$.

Consequently $L=40$ suffices for every scalar downstream input.

### Signs, both returns and reconstruction

The finite terminal selection is


$$
(-1)^{b-124+t}\,\mathrm{terminal}_{123-t}.
$$


For odd $b$, this sign is $(-1)^{1+t}$, independent of the higher digits of $b$. The reversal is unchanged.

Both returns are separately retained:


$$
\eta_f=\overline K S_{\rm end}^{-1}(\text{selected first terminal}),
$$




$$
\eta_e=\overline K S_{\rm end}^{-1}(\text{selected exterior terminal}).
$$


The exponential source remains


$$
h_{\rm out}-\eta_e
$$


on its complete $160$-entry support, not on a shortened support.

Reconstruction contains the affine coefficients


$$
j-b-284,\qquad \rho\,4002b+\delta,
$$


where $\rho=1,2$ and $\delta=0,196$ as appropriate.

The exterior principal part continues to satisfy


$$
(-r-b)(-1)^{r-1}v_{r-1}-(-1)^rv_r=0,
$$


including the last retained step using $v_{36}=0\pmod{2^{32}}$. At zero it gives


$$
\boxed{-b\,g_0-1,}
$$


not $-b\,g_0$.

### Uniform tail scope

The central and first-force tail bounds are parameter-uniform:


$$
v_2(36!)=34,\qquad
v_2\!\left(\left\lfloor72/2\right\rfloor!\right)=34.
$$


Likewise $v_2(v_t)\ge v_2(t!)$.

For the absolute logarithmic omission, one may retain the actual parameter-dependent bound


$$
1+2000b-s_2(2001b)+s_2(b)
-\lfloor\log_2(8005b-1)\rfloor.
\tag{6.1}
$$


It exceeds $32$ for every $b\ge b_0$. A fixed numerical constant from the bit length of $b_0$ is not silently reused for arbitrarily larger $b$.

## Theorem 1 — Complete precision-32 producer continuity

For original parameters $b\ge b_0$,


$$
\boxed{
b\equiv b_0\pmod{2^{40}}
}
$$


implies agreement modulo $2^{32}$ of the complete supplied bounded producer, including:

- both complete force inputs;
- the entire exterior load;
- both finite endpoint returns;
- both Laurent branches and full prefix subtraction;
- reconstruction and the terminal $-b\,g_0-1$;
- the coefficientwise branch-zero and contact tests;
- the resulting short numerator arrays after the accepted unit-polynomial divisions.

In particular, the proposed modulus $2^{41}$ is sufficient.

The maximal factor counts $134,135$ transfer only as statements about these modular presentations. They are not promoted to exact characteristic-zero multiplicities.

---

# Part II. Independent review and physical transfer of the separator theorem

# 7. The separator and its high block

Retain


$$
T=103,\qquad L\ge135,\qquad g=L-T\ge32,
$$


and set


$$
b=b_0+2^Lh,\qquad h\ge1,
$$




$$
M=2^T,\qquad m_h=2^gh.
$$


The exact high entries are


$$
H_{L,h}(k)=
\binom{4002m_hM}{kM}
\binom{(8005m_h-k)M}{(m_h-k)M},
\qquad0\le k\le m_h,
$$


and


$$
\boxed{
S_{L,h}=\sum_{k=0}^{m_h}H_{L,h}(k)^2.
}
\tag{7.1}
$$



The high norm is a positive integer. It is not assumed to be odd or shallow.

---

# 8. Review of the whole-row theorem

The supported-binomial splitting in turn 6 is valid. Every low factorial argument is below $2^{71}$. With $M=2^{103}$, the exact factorial-ratio unit differs from $1$ by a multiple of $2^{33}$, which is sufficient for the claimed modulus $2^{32}$.

The unsupported-row step deserves a more explicit carry justification.

For one short-numerator atom, put


$$
B_r=b_0-r,\qquad
C_R=2n_0+R-1,\qquad
S_r=B_r+C_R.
$$


The three subtraction borrows are those for


$$
N_0-j_0,\qquad B_r-j_0,\qquad S_r-j_0.
$$


Since


$$
B_r<N_0<S_r<2^{71},
$$


an unsupported low shift $j_0>B_r$ enters the separator in one of the states


$$
010,\qquad110,\qquad111.
$$



Across a position where all three fixed parameter digits are zero, each borrow bit becomes its old value OR the current row digit. Thus such a state either stays unchanged or becomes $111$.

On these positions, the sum of the two binomial valuations has incremental cost


$$
\alpha+\beta-\gamma.
$$


The values in the three possible states are respectively


$$
1,\qquad2,\qquad1.
$$


This expression agrees there with the actual sum of the first binomial’s subtraction borrow and the second binomial’s addition carry: the fixed addition $B_r+C_R=S_r$ has no carry in the separator.

Therefore the two-binomial atom acquires at least $g\ge32$ valuation events across the separator. The argument is about actual binomial carry counts, so no negative low contribution is being allowed to cancel these $g$ events.

This repairs the exposition of that step without changing the result.

## Theorem 2 — Complete physical whole-row tensorization

Let $b=b(u)$ be an original parameter of the form above. Write


$$
j=j_0+Mk,\qquad0\le j_0<M.
$$


Then the complete physical columns satisfy, modulo $2^{32}$,


$$
X_j(b)\equiv H_{L,h}(k)X_{0,j_0},
\qquad
Y_j(b)\equiv H_{L,h}(k)Y_{0,j_0}
\tag{8.1}
$$


when $j_0\le b_0$, and both coordinates vanish modulo $2^{32}$ when $j_0>b_0$.

All supported model rows


$$
0\le j_0\le b_0,\qquad0\le k\le m_h
$$


lie in the actual range


$$
0\le j\le b_0+Mm_h=b.
$$


In particular, $k=m_h,j_0=b_0$ is retained.

### Proof of physical transfer

Since $L\ge135>40$, Theorem 1 identifies the complete modular numerator arrays at $b$ with the retained $b_0$ arrays. The reviewed atomwise separator argument then applies. The accepted complete forcing and exterior are already incorporated before the short numerator presentation is formed. ∎

Consequently,


$$
\boxed{
D_{\rm raw}(b)\equiv S_{L,h}D_0\pmod{2^{42}},
}
\tag{8.2}
$$




$$
\boxed{
E_{\rm raw}(b)\equiv S_{L,h}E_0\pmod{2^{41}}.
}
\tag{8.3}
$$



This is now a theorem for the complete original producers, not merely for retained payloads.

---

# 9. An unconditional infinite-original-family consequence

Put $q=9^{32}$. The exact lifting formula is


$$
v_2(q^u-1)=8+v_2(u)\qquad(u\ne0).
$$


Thus $q$ generates the subgroup $1+256\mathbb Z$ modulo every sufficiently large power of $2$.

For each fixed $L\ge135$, the congruence


$$
b_0q^u\equiv b_0+3\cdot2^L\pmod{2^{L+2}}
$$


has a residue class of solutions modulo $2^{L-6}$, containing infinitely many original nonnegative indices. Their high parameter satisfies


$$
h\equiv3\pmod4.
$$



The high-block parity identity remains


$$
S_{L,h}\equiv\binom{4003h}{h}\pmod2.
$$


For $h\equiv3\pmod4$, a binary carry occurs in $h+4002h$, so $S_{L,h}$ is even. Therefore every such original index satisfies


$$
\boxed{
v_2(D_{\rm raw}(b(u)))\ge34,\qquad
v_2(E_{\rm raw}(b(u)))\ge35.
}
\tag{9.1}
$$



Choosing such an original index for each increasing $L$ yields $b(u_L)\to b_0$ in $\mathbb Z_2$, but


$$
v_2(D_{\rm raw}(b(u_L))-D_0)=33.
$$


Hence:

### Corollary 3 — Complete-original norm noncontinuity

The maps


$$
b(u)\longmapsto D_{\rm raw}(b(u)),
\qquad
b(u)\longmapsto D_{\rm raw}(b(u))/2^{18}
$$


are not $2$-adically continuous at $b_0$ on the original parameter set.

The second normalization is by the **fixed certified factor** $2^{18}$. This corollary does not assert noncontinuity after division by the actual, possibly growing, first-column content.

---

# Part III. Paying the high content and true norm depth

# 10. A sharper common-factor theorem

Define the exact high content and norm depth


$$
c=\min_{0\le k\le m_h}v_2(H_{L,h}(k)),
\qquad
t=v_2(S_{L,h}).
$$


Write


$$
S_{L,h}=2^{2c}\Sigma,\qquad
\nu=v_2(\Sigma)=t-2c.
\tag{10.1}
$$


Always $t\ge2c$.

The model first column has exact content $9+c$: choose a high coordinate attaining $c$ and the accepted low witness attaining $9$. The second model content is at least $10+c$.

Suppose $c\le22$. The physical coordinate errors are divisible by $2^{32}$, so they cannot destroy the first attaining valuation $9+c<32$. Therefore


$$
\boxed{
v_2(\operatorname{content}X(b))=9+c,
\qquad
v_2(\operatorname{content}Y(b))\ge10+c.
}
\tag{10.2}
$$



Expanding the quadratic errors gives


$$
v_2(D_{\rm raw}(b)-S_{L,h}D_0)\ge42+c,
$$




$$
v_2(E_{\rm raw}(b)-S_{L,h}E_0)\ge41+c.
\tag{10.3}
$$


The squared-error term has depth $64$, sufficient throughout $c\le22$.

Since the uncertainties in (1.1), after multiplication by $S$, have depths $42+t$ and $41+t$, and $t\ge2c$, we obtain:

## Theorem 4 — Content-paid complete Gram transfer

For $c\le22$,


$$
\boxed{
D_{\rm raw}(b)\equiv285\,2^{33}S_{L,h}\pmod{2^{42+c}},
}
\tag{10.4}
$$




$$
\boxed{
E_{\rm raw}(b)\equiv13\,2^{34}S_{L,h}\pmod{2^{41+c}}.
}
\tag{10.5}
$$



In particular:

- if $t-c\le8$, then
  

$$
v_2(D_{\rm raw}(b))=33+t;
$$


- if $t-c\le6$, then also
  

$$
v_2(E_{\rm raw}(b))=34+t,
$$


  and
  

$$
\boxed{
  \frac{E_{\rm raw}(b)}{2D_{\rm raw}(b)}
  \equiv49\pmod{2^{\,7+c-t}}.
  }
  \tag{10.6}
$$



Under the first condition, the first primitive binary norm loss is


$$
\boxed{
(33+t)-2(9+c)=15+\nu.
}
\tag{10.7}
$$



This separates two effects that must not be conflated:

- $c$ is high **coordinate content**;
- $\nu$ is the additional high **normalized norm cancellation**.

The ratio precision is


$$
7+c-t=7-c-\nu.
$$


Both losses are paid.

---

# 11. An undivided relative observable and a local gcd consequence

From (1.2),


$$
E_0-98D_0\in2^{41}\mathbb Z.
$$


The physical transfer therefore proves, without cancelling the high norm,


$$
\boxed{
E_{\rm raw}(b)-98D_{\rm raw}(b)\in2^{41}\mathbb Z.
}
\tag{11.1}
$$


With the content refinement $c\le22$,


$$
\boxed{
E_{\rm raw}(b)-98D_{\rm raw}(b)\in2^{41+c}\mathbb Z.
}
\tag{11.2}
$$



This is a whole-contraction relative congruence. It remains meaningful even when $t$ is unknown or too large for quotient extraction.

For the precisely specified **raw** pair, put


$$
g_{\rm raw}=\gcd(D_{\rm raw},|E_{\rm raw}|).
$$


Then


$$
\boxed{
v_2(g_{\rm raw})\ge
\min(33+t,\,41+c).
}
\tag{11.3}
$$


If $t-c\le8$, the norm depth is visible and $v_2(E_{\rm raw})\ge v_2(D_{\rm raw})$. Hence


$$
\boxed{
v_2(D_{\rm raw}/g_{\rm raw})=0.
}
\tag{11.4}
$$



This extends the detectable local denominator conclusion beyond the range where a positive-precision ratio is available.

It is not an evaluation of the final denominator $q_n$. The exact conversion from these raw columns to the prescribed final row-normalized pair must still be retained; neither an odd-prime gcd nor the actual clearer is determined here.

---

# Part IV. A concrete high-block arithmetic advance

# 12. A valuation-only formula for the normalized high norm

For an arbitrary finite integer vector $H_k$, let


$$
c=\min_k v_2(H_k),
\qquad
N_r=\#\{k:v_2(H_k)=r\}.
$$


Odd squares are $1\pmod8$. It follows immediately that


$$
\boxed{
2^{-2c}\sum_kH_k^2
\equiv N_c+4N_{c+1}\pmod8.
}
\tag{12.1}
$$



Thus the first three normalized norm bits require **only two valuation-level counts**, not the odd units.

For the present high block, scaling both arguments of a binomial by a power of two leaves its valuation unchanged. Set


$$
m=m_h,\quad A=4002m,\quad C=8004m,\quad S=C+m=8005m.
$$


Then


$$
v_2(H_{L,h}(k))
=
v_2\binom Ak+
v_2\binom{S-k}{m-k}.
\tag{12.2}
$$


The parameter $M=2^{103}$ disappears from the valuation calculation, without disappearing from the actual integer norm.

---

# 13. An explicit eight-state counter for the actual finite summand

Let $B_X(k)$ be the total number of subtraction borrows in $X-k$, with sufficient leading zero digits and terminal borrow zero. The binary digit-sum identity gives


$$
s_2(X-k)=s_2(X)-s_2(k)+B_X(k).
$$


Therefore (12.2) becomes


$$
\boxed{
v_2(H_{L,h}(k))
=
v_2\binom Sm+B_A(k)+B_m(k)-B_S(k).
}
\tag{13.1}
$$



Use the eight states


$$
(\alpha,\beta,\gamma)\in\{0,1\}^3,
$$


the incoming borrows for $A-k,m-k,S-k$. At a position whose parameter digits are $a,b,s$, choose the row digit $d\in\{0,1\}$ and update


$$
\alpha'=\mathbf1_{d+\alpha>a},\qquad
\beta'=\mathbf1_{d+\beta>b},\qquad
\gamma'=\mathbf1_{d+\gamma>s}.
\tag{13.2}
$$


Give the transition weight


$$
z^{\alpha'+\beta'-\gamma'}.
\tag{13.3}
$$



Start at $000$, process enough digits to contain $S$, and retain only terminal $000$. Terminal zero enforces all three subtractions, in particular


$$
\boxed{0\le k\le m.}
$$


The generating polynomial, multiplied by $z^{v_2\binom Sm}$, has coefficient $N_r$ at $z^r$.

This is an explicit target-dependent realization, not an appeal to generic automaticity.

## 13.1 Computing only the required observable

At each state one need retain only:

1. the least reachable exponent;
2. the count at that exponent modulo $8$;
3. the count one exponent above it modulo $8$.

The least exponent is tracked by reachability, not by whether its count happens to vanish modulo $8$. When paths merge, the two coefficients are rebased to the new minimum. Discarded terms cannot later overtake retained terms from the same state, since they have identical possible continuations.

Thus the required observable is computed with eight states and constant-size count data per state, in a number of steps linear in the number of input digits.

### Theorem 5 — Three normalized high-norm bits

The complete high word determines, by (13.1)–(13.3),

- the exact high coordinate content $c$;
- $N_c\bmod8$;
- $N_{c+1}\bmod2$;

and hence


$$
\boxed{
\Sigma=S_{L,h}/2^{2c}
\equiv N_c+4N_{c+1}\pmod8.
}
\tag{13.4}
$$



If this residue is nonzero, it determines $\nu=v_2(\Sigma)$ exactly when $\nu\le2$. If it is zero, the conclusion is only $\nu\ge3$.

This supplies a concrete normalized observable for the previously unspecified high norm. It does not claim that the high word of an enormous original power is available at bounded cost independent of that word.

---

# 14. A sharper formula when $h\equiv3\pmod4$

For odd high entries, Lucas’s theorem first forces


$$
k=2^g\ell.
$$


Their parity is the parity of


$$
\binom{4002h}{\ell}\binom{8005h-\ell}{h-\ell}.
$$



Now write


$$
h=4H+3.
$$


Then


$$
4002h=4(4002H+3001)+2,
$$




$$
8004h=4(8004H+6003).
$$


The first binomial can be odd only when


$$
\ell=4r+e,\qquad e\in\{0,2\}.
$$


For both choices,


$$
h-\ell=4(H-r)+(3-e),
$$


with no low borrow. Consequently both low choices have the same high parity conditions:


$$
r\subseteq 4002H+3001,
\qquad
(H-r)\mathbin{\&}(8004H+6003)=0.
$$


Thus the number of odd high entries is twice the number of high admissible $r$.

The latter count, modulo $2$, is the coefficient of $z^H$ in


$$
(1+z)^{4002H+3001}
(1-z)^{-8004H-6004}.
$$


Modulo $2$, this coefficient equals


$$
\binom{4003H+3002}{H}.
$$



Since even squares vanish modulo $4$, we have proved:

## Theorem 6 — Exact depth-one high-block test

For $h=4H+3$,


$$
\boxed{
S_{L,h}\equiv
2\binom{4003H+3002}{H}\pmod4.
}
\tag{14.1}
$$


Equivalently,


$$
\boxed{
v_2(S_{L,h})=1
\iff
H\mathbin{\&}(4002H+3002)=0.
}
\tag{14.2}
$$



This is strictly stronger than the previous evenness statement, but its exact-depth condition uses the whole integer $H$. No finite low residue is being substituted for it.

Whenever an original parameter passes this test, $c=0$, and the complete physical conclusions are


$$
v_2(\operatorname{content}X)=9,
$$




$$
v_2(D_{\rm raw})=34,\qquad v_2(E_{\rm raw})=35,
$$




$$
\boxed{\frac{E_{\rm raw}}{2D_{\rm raw}}\equiv49\pmod{64}.}
\tag{14.3}
$$



I have not proved that infinitely many original indices pass (14.2).

---

# 15. Two small exact high-block evaluations

These are new hand-derived arithmetic controls, not reruns of accepted calculations and not evaluations of new original powers.

## 15.1 $h=3$

For the aligned indices $\ell=0,1,2,3$, the valuations of


$$
\binom{12006}{\ell}
\binom{24015-\ell}{3-\ell}
$$


are


$$
0,\ 1,\ 0,\ 2.
$$


Thus there are two valuation-zero entries and one valuation-one entry.

Any unaligned $k$, with $v_2(k)<g$, satisfies


$$
v_2\binom{4002\cdot2^gh}{k}
\ge g+1-v_2(k)\ge2.
$$


It cannot affect the square sum modulo $8$. Therefore


$$
\boxed{
S_{L,3}\equiv2+4=6\pmod8.
}
\tag{15.1}
$$


In particular, $c=0,t=1$, recovering and slightly sharpening the earlier exact-depth calculation.

## 15.2 $h=11$: content and norm cancellation are different

For the aligned indices $\ell=0,\ldots,11$, use


$$
A=44022,\qquad C=88044.
$$


The valuations of


$$
\binom{44022}{\ell}
\binom{88055-\ell}{11-\ell}
$$


are


$$
\boxed{
1,2,1,3,2,3,2,6,1,2,1,3.
}
\tag{15.2}
$$


Hence the aligned counts at depths one and two are both $4$.

Unaligned indices have depth at least two. To have depth exactly two, they must have


$$
k=2^{g-1}r,\qquad r\ \text{odd}.
$$


The first binomial then has depth exactly two only for


$$
r\in\{1,3,9,11\}.
$$


For these four choices, the second binomial has positive valuation: with high reduced parameters $m=22,C=176088$, the lower values are $21,19,13,11$, each overlapping a nonzero binary digit of $C$. Thus there are no additional depth-two entries.

Consequently


$$
c=1,\qquad N_1=4,\qquad N_2=4.
$$


Formula (12.1) gives


$$
\frac{S_{L,11}}4\equiv4+4\cdot4\equiv4\pmod8.
$$


Therefore


$$
\boxed{
c=1,\qquad v_2(S_{L,11})=4,\qquad
v_2(S_{L,11}/4)=2.
}
\tag{15.3}
$$



This example demonstrates why neither high coordinate content nor high-block parity alone determines the normalized norm loss.

The integers $b_0+3\cdot2^L$ and $b_0+11\cdot2^L$ are not asserted to belong to the original power family. Their role here is to evaluate the high-block arithmetic and verify the distinctions in Theorem 4.

---

# Part V. Scope, remaining arithmetic, and the irrationality objective

# 16. What has now become unconditional

Using the accepted complete-producer identities at their stated scope, the following are now proved for the complete original family:

- uniform operator/Schur continuity with an explicit sufficient guard;
- complete downstream continuity, including both corrected columns and the exterior;
- whole-row separator transfer over the original inclusive cutoff;
- common-factor congruences for the whole norm and mixed form;
- infinite original residue classes with depths at least $34,35$;
- noncontinuity of the complete raw norm at $b_0$;
- content-paid norm and relative-ratio statements;
- an explicit high-block valuation counter and a normalized three-bit norm observable;
- the exact depth-one criterion (14.2).

The following remain conditional or unresolved:

- exact high norm depth on an infinite original sequence;
- a proof that the full-word condition (14.2) holds infinitely often on the original powers;
- arbitrary-precision complete-producer transfer beyond the supplied precision-32 construction;
- any all-prime conclusion about the prescribed final primitive pair;
- the required whole-error estimate and nonvanishing.

The eight-state counter does not make the full high contraction a function of a fixed low prefix. Its inputs include the entire finite high word.

---

# 17. The final gcd and actual denominator are unchanged

Retain exactly


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,
\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


and


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad
p_n=H_B/g_B.
}
\tag{17.1}
$$


This gcd is over all primes.

With the least actual two-column clearer $d_B$, the primitive multiplier remains


$$
\boxed{d_B^2/g_B.}
\tag{17.2}
$$



The new binary common-factor theorem does not replace $g_B$ by:

- first-column content;
- a selected-prime norm divisor;
- the high-block norm $S_{L,h}$;
- or the raw gcd before the exact prescribed normalization.

In particular, a congruence


$$
D_{\rm raw}\equiv SD_0,\qquad E_{\rm raw}\equiv SE_0
$$


at finite precision is not an exact integral factorization by $S$, and it supplies no odd-prime divisibility by $S$.

A concrete next arithmetic obligation is therefore:

> **Complete separated Gram-ideal lifting problem.**  
> Relate the ideal $(A_B,H_B)$, after the actual row normalization and least common clearing, to the separated model and its complete correction terms, with explicit prime-by-prime bounds on the correction ideal.

The present report solves a binary finite-precision portion of that problem, including its true-content and true-norm guards. It does not solve its all-prime part.

---

# 18. The whole same-index error remains decisive

The approximation identity stays


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n,
}
\tag{18.1}
$$


with the actual primitive $q_n$ and the **whole evaluated error at the same original index**.

Neither the absolute logarithmic omission used for modular production nor the local relation $E_{\rm raw}\approx98D_{\rm raw}$ deletes a term from this real identity.

An irrationality proof would require an infinite original sequence on which


$$
0<|q_n\epsilon_n|\longrightarrow0.
$$


The strict nonzero condition and the actual all-prime denominator are both outstanding.

No result here proves rationality either.

---

# 19. Bounded arithmetic status and a new checkable certificate

No bounded calculation remains necessary to close OPC: the proof is the explicit integral formula audit in §§2–6.

No accepted $u_0$ calculation should be repeated.

For independent verification of the **new high-block observable**, a genuinely small optional certificate can use:

### Inputs



$$
m=6,\qquad m=22,
$$


and, in each case, the exact finite atoms


$$
a_k=
\binom{4002m}{k}
\binom{8005m-k}{m-k},
\qquad0\le k\le m.
$$


Use the eight-state transitions (13.2), with terminal $000$.

### Expected verifiable outputs

For $m=6$:


$$
\min v_2(a_k)=0,\qquad N_0=2,\qquad N_1=1,
$$




$$
\sum a_k^2\equiv6\pmod8.
$$



For $m=22$:


$$
\min v_2(a_k)=1,\qquad N_1=4,\qquad N_2=4,
$$




$$
2^{-2}\sum a_k^2\equiv4\pmod8.
$$



These expected outputs have been derived above. No execution receipt is claimed. Such a certificate would corroborate only these bounded inputs and the implemented transitions; the all-$g$ assertions rest on the valuation proof, not on that finite check.

For an actual original parameter, the new counter’s required input is the complete high integer


$$
h=\frac{b(u)-b_0}{2^L},
$$


or the corresponding full binary parameter word. No bounded low-residue substitute has been established.

---

# 20. Proof-status ledger

| Statement | Status |
|---|---|
| Accepted $u_0$ norm $33$, mixed depth $34$, ratio $49\bmod128$ | Reused; not recomputed |
| New direct witness and sixteen-row block receipt | Accepted finite independent corroboration |
| OPC with sufficient operator guard $39$ | **Proved from supplied formulas** |
| Complete downstream guard $40$, hence proposed $41$ | **Proved** |
| Uniform Schur integrality and precision-preserving inversion | **Proved** |
| Finite padded boundary and terminal selection preserved | **Explicitly audited** |
| Unsupported-row separator argument | **Reviewed and expanded** |
| Complete-original whole-row/full-contraction transfer | **Proved** |
| Infinite original classes with depths at least $34,35$ | **Proved** |
| Complete raw-norm noncontinuity at $b_0$ | **Proved** |
| Content-paid comparison and ratio guards | **Proved** |
| Undivided whole relation $E-98D\in2^{41}$ | **Proved** |
| Eight-state normalized high-norm observable | **Proved** |
| Full-word depth-one test for $h=4H+3$ | **Proved** |
| $h=3$ and $h=11$ high-block evaluations | Explicit small arithmetic proofs; not original-power evaluations |
| Infinitely many original depth-one high blocks | Open |
| Final all-prime gcd and actual primitive denominator | Open |
| Whole nonzero same-index error tending to zero after primitive normalization | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The former producer bottleneck is closed:


$$
\boxed{
\text{OPC is proved, and the proposed 41-bit guard is sufficient.}
}
$$



The separator theorem now applies to the **complete physical original family**, not just retained numerator arrays. It gives an unconditional infinite-family failure of naive norm continuity and a common-factor law with explicitly paid content and norm-depth losses.

The additional arithmetic advance is the high-block normalized observable


$$
\boxed{
S_{L,h}/2^{2c}\equiv N_c+4N_{c+1}\pmod8,
}
$$


with an explicit eight-state computation of the required valuation counts and the sharper full-word criterion


$$
\boxed{
h=4H+3:\quad
v_2(S_{L,h})=1
\iff H\mathbin{\&}(4002H+3002)=0.
}
$$



The exact remaining bottleneck is no longer unspecified operator continuity. It is


$$
\boxed{
\text{actual all-prime normalization, including complete corrections,
versus the whole nonzero same-index error on an infinite original sequence}.
}
$$



The present work advances the arithmetic structure of that problem, but does not supply an unconditional proof or disproof of the irrationality of $e+\pi$.
