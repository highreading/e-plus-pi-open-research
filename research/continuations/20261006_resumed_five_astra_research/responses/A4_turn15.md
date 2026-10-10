> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, turn 15 — Independent audits and a linear-depth complete-source criterion

## Executive conclusions

The three advances have different mathematical roles and must remain on their respective original families.

1. **A1’s new full-content results pass the audit.** The trailing-residue bijection gives the stated
   

$$
O\!\left((1+\log X)X^{\log_3 2}\right)
$$


   split-language exception bound without a leading-digit theorem. The $20$-forcing argument applies to both full same-parameter Jacobi polynomials. The Bernstein-to-monomial transformation is unimodular, and the eight-state and sixteen-state constructions correctly retain the generalized half-integer borrow, signs, finite indices, and terminal carries.

   The complete-factorial/finite-pole congruence is also valid, but it is **not an evaluation of the normalized complete forcing**. Its factorial term remains unevaluated, and homogeneous polynomial content does not establish divisibility of the externally forced corrected-column source.

2. **A2’s new $29$-adic lift passes the structural audit at the retained complete-normal-form scope.** In particular, the eight-interface radical is valid: the one denominator introduced by the interface ratios is a unit on the support where it is used. The finite cutoff can be completed at the required precision, and the full $2p\,z_1^Tz_2$ term is retained before being annihilated. I give below an explicit digit-level justification of the lifted reflection, including the $231$-path count and the cancellation of high-parameter derivatives.

   Thus the new implication
   

$$
u\equiv2\pmod{29^9}\quad\Longrightarrow\quad d\ge10
$$


   follows from the retained complete $p^6$ normal form and the accepted tail receipt. It does not determine $c$, the first nonzero primitive norm digit, or the mixed-to-norm valuation gap.

3. **A5’s exact final normalization passes.** Its prime-$3$ theorem is the historical A2 turn 8 theorem, not a new discovery:
   

$$
v_3(q_n)=\frac{8003b-15}{2}.
$$


   The genuinely new consequence is correct. Under the retained whole-error theorem, every infinite original sequence satisfying the shallow binary guards has
   

$$
|q_n\epsilon_n|\longrightarrow\infty.
$$


   Equal binary depths, bounded positive gaps, and additional fixed-depth witnesses cannot repair that route.

4. **New scale-relevant result.** For the even family, I derive an exact complete-source criterion for a binary gap $v_2(H)-v_2(N)\ge k$. At the necessary scale $k\sim0.54109n$, it requires a cancellation between the **whole exponential residual, its actual terminal term, and the whole logarithmic source** at a further depth of at least
   

$$
0.04134n+\text{primitive-content/norm corrections}.
$$


   The accepted absolute logarithmic-force protection is only about $0.49975n$ after the actual $4b!$ normalization. It therefore cannot justify deleting the logarithmic source at the new denominator-relevant target.

No computation was executed. No accepted producer, endpoint gcd, denominator, error, modulo-$81$ calculation, or factor split is proposed for repetition.

---

## 1. Scope and retained arithmetic objects

I keep the three infinite domains separate.

- **A1:** $m=2^{2j-1}$, the original congruence conditions on $j$, and the exact real window, including its $3^{-k}$ correction.
- **A2:** $n=2001b$, with the specified $29$-adic parametrization of $b$ and $u$.
- **A5 and historical A2’s even audit:**
  

$$
b=3^{36+64u},\qquad n=4002b,\qquad u\ge0.
$$



The prime-$3$ denominator theorem for the last family is not imported into either of the first two families.

For the final weighted producer, the prescribed columns and metric remain


$$
N_B=d_B[u,v],\qquad
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


with


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
$$


The gcd is over **all primes**. Actual row contents are retained; no independent row primitivization is introduced.

The evaluated error is always the whole same-index expression


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$



The retained turn 14 reference-intersection certificate stays at its stated scope $p>n+2$. The NEW3375 receipt reports


$$
H_{\rm ref}=V_0=V_3=W_{\rm ref}=1.
$$


That is a finite retained-data result, not an infinite reference-content bound. The compact receipt does not itself supply the additional $G/K_{\rm ref}$ integers, so I make no numerical assertion about them and do not repeat the existing once-only retained-data request.

---

# Part I. Audit of A1 turn 18

## 2. The trailing-residue bijection and the exception count

On the fixed-tail progression,


$$
j=j_*+3^{12}t,\qquad j_*=84645,
$$


we have


$$
m(t)=2^{2j_*-1}\left(4^{3^{12}}\right)^t.
$$


LTE gives


$$
v_3\!\left(4^{3^{12}}-1\right)=13.
$$


Therefore, modulo $3^{13+a}$, the element $4^{3^{12}}$ has order $3^a$ and generates the entire principal-unit subgroup


$$
1+3^{13}\mathbb Z/3^{13+a}\mathbb Z.
$$



Multiplication by the fixed unit $m(0)$ identifies that subgroup with the residue class


$$
m\equiv1194953\pmod{3^{13}}.
$$


Because $0<1194953<3^{13}$, writing


$$
m=1194953+3^{13}U
$$


gives exactly


$$
U=\left\lfloor m/3^{13}\right\rfloor.
$$


Thus


$$
t\bmod3^a\longmapsto U(t)\bmod3^a
$$


is a bijection.

This proves the needed statement about **trailing quotient digits**, not merely an equidistribution statement.

The split language


$$
\{0,1\}^{*}\{1,2\}^{*}
$$


has at most $(a+1)2^a$ words of length $a$. It is closed under taking contiguous subwords and under prepending zeros. With


$$
a=\lfloor\log_3 T\rfloor,
$$


each residue class modulo $3^a$ occurs at most three times in $T$ consecutive progression parameters. Hence


$$
\#\{\text{split quotient words among }t<T\}
\le3(a+1)2^a.
$$



Using the retained turn 17 implication from exact endpoint content $3$ to the split high word gives


$$
\#\{j\le X:j\in\mathcal W,\ c_m=3\}
=
O\!\left((1+\log X)X^{\log_3 2}\right).
$$



### Window audit

The exact identity is


$$
\frac{D}{3^k}
=
1-3^{\{j\log_3 4\}-1}+3^{-k}.
$$


A1 retains the last term in its moving interval. Squeezing by fixed inner and outer intervals proves the positive window density on a fixed compatible progression. Subtracting the sublinear exception count therefore gives relative density one of $c_m\ge4$.

**Status:** proved from the retained turn 17 language theorem and the displayed exact parametrization. No numerical irrationality-measure exponent is needed.

---

## 3. Both full Jacobi contents: the valuation mechanism

Write


$$
J_s^{[A]}(y)
=
\sum_{k=0}^s
\binom nk\binom{s-\tfrac12}{s-k}
y^k(y-1)^{s-k},
\qquad n=s+A.
$$



### 3.1 The half-integer borrow is correct

Let $r=s-k$ and $P=3^h$. In


$$
\binom{s-\tfrac12}{r}
=
\frac{\prod_{t=0}^{r-1}(s-\tfrac12-t)}{r!},
$$


the numerator factor indexed by $t$ is divisible by $P$ precisely when


$$
t\equiv s+\frac{P-1}{2}\pmod P.
$$


Put


$$
\alpha_P(s)=\left(s+\frac{P-1}{2}\right)\bmod P.
$$


The number of such numerator factors is


$$
\left\lfloor\frac rP\right\rfloor+
\mathbf1_{\{r\bmod P>\alpha_P(s)\}}.
$$


After subtracting the $P$-level contribution of $r!$, the contribution is exactly


$$
\mathbf1_{\{r\bmod P>\alpha_P(s)\}}.
$$



Thus A1’s generalized borrow is not a heuristic extension of ordinary Kummer theory. It follows directly from the finite numerator product.

### 3.2 Simultaneous forcing from $20$

Let $M=m\bmod P$, with the relevant $20$-occurrence giving


$$
\frac{2P}{3}+1\le M\le\frac{5P-3}{6}.
$$


For the degree-$m$ polynomial,


$$
n\bmod P=3M-2P-1,\qquad
\alpha_P(m)=M-\frac{P+1}{2}.
$$


If both valuation events were absent, then


$$
k\bmod P\le3M-2P-1,\qquad
r\bmod P\le M-\frac{P+1}{2}.
$$


Their sum would be strictly smaller than $M$, whereas $k+r=m$ requires that sum to be $M$ or $M+P$. Contradiction.

For the adjacent degree $s=m-1$, with the **same** $A=2m-1$,


$$
n=3m-2,
$$


and the corresponding bounds become


$$
k\bmod P\le3M-2P-2,\qquad
r\bmod P\le M-\frac{P+3}{2}.
$$


Their sum is strictly smaller than $M-1$, again impossible.

Distinct occurrences act at distinct powers $P$, so their contributions add. A bottom occurrence with zero remaining suffix cannot occur in a $3$-adic unit.

Consequently,


$$
\operatorname{cont}_3J_m^{[A]}\ge N_{20}(m),\qquad
\operatorname{cont}_3J_{m-1}^{[A]}\ge N_{20}(m).
$$



### 3.3 The full content really is the Bernstein minimum

The polynomials


$$
y^k(y-1)^{s-k},\qquad 0\le k\le s,
$$


form an integral basis of $\mathbb Z[y]_{\le s}$: the coefficient matrix is triangular with diagonal $(-1)^{s-k}$. Its inverse is integral.

Therefore the Bernstein coefficients and monomial coefficients generate the same ideal over $\mathbb Z_3$, and


$$
\operatorname{cont}_3J_s^{[A]}
=
\min_{0\le k\le s}
v_3\!\left(\binom nk\binom{s-\tfrac12}{s-k}\right).
$$



This is stronger than merely proving a common divisor of the Bernstein coefficients.

---

## 4. The eight-state and sixteen-state evaluators

### 4.1 Min-plus evaluator

The three state bits have distinct purposes:

- addition carry in $k+r=s$;
- ordinary borrow in $n-k$;
- generalized borrow in $\alpha-r$.

The input-only carry producing the digits of


$$
s+\frac{3^h-1}{2}
$$


does not need to be an optimization state.

For the target values $n\ge s$, choosing


$$
3^L>\max(n,2s)
$$


has three consequences:

1. accepted paths describe exactly $k+r=s$, $0\le k,r\le s$;
2. the ordinary subtraction is finished;
3. the generalized comparison is finished because
   

$$
s\le s+\frac{3^L-1}{2}<3^L.
$$



Thus no valuation contribution is lost beyond the final digit. Minimizing the accumulated outgoing borrows gives the exact content.

### 4.2 Sign audit

The exact coefficient identity is


$$
\binom nk\binom{s-\tfrac12}{s-k}
=
\frac{n!(2s)!}
{(n-k)!(2k)!s!(s-k)!\,4^{s-k}}.
$$


At $y=-1$, its evaluation multiplier is


$$
(-1)^s2^{s-k}.
$$


Modulo $3$, the latter contributes the sign $(-1)^k$.

The factorial-unit formula


$$
3^{-v_3(N!)}N!
\equiv(-1)^{v_3(N!)+d_2(N)}\pmod3
$$


then gives exactly A1’s sign


$$
(-1)^{
e+k+d_2(n)+d_2(2s)
-d_2(n-k)-d_2(2k)-d_2(s)-d_2(s-k)
}.
$$


The local transition sign accumulates these terms correctly. The extra state bit is precisely the carry needed to produce the digits of $2k$, and its terminal value is zero since $2k\le2s<3^L$.

A zero signed minimum sum must remain a zero residue attached to an existing minimum-cost path set. A1 correctly makes that distinction.

**Status:** both evaluator proofs pass. They determine full content and the first endpoint residue after full-content division; they do not determine arbitrary deeper endpoint cancellation.

---

## 5. Density-one deep content and its scale

The $20$-avoiding transition matrix has spectral radius


$$
\rho=\frac{3+\sqrt5}{2}<3.
$$


Decomposition at at most $R$ nonoverlapping occurrences gives


$$
A_R(L)=O_R((L+1)^R\rho^L).
$$


The exact power-residue bijection


$$
j\bmod3^{L-1}\longmapsto2^{-1}4^j\bmod3^L
$$


then proves


$$
\#\{j\le X:g_m\le R\}
=
O_R\!\left((1+\log X)^R X^{\log_3\rho}\right).
$$



So both full contents tend to infinity in density, including relative density inside a fixed positive-density original window progression.

There is, however, an important scale qualification. Taking $k=0$ gives


$$
g_m\le
v_3\binom{2m}{m}
\le1+\lfloor\log_3(2m)\rfloor.
$$


In particular,


$$
3^{g_m}\le6m,\qquad 3^{2g_m}\le36m^2.
$$



Therefore the common factor extracted from this **single polynomial pair**, or its square extracted from a single bilinear contraction, has logarithmic size $O(\log m)$. Its density-one divergence does not itself provide an exponentially large cancellation in the degree $m$.

This does not rule out amplification through other operations. Such amplification would require its actual multiplicity, row contents, and complete normalization to be proved; it is not supplied by the two-polynomial content theorem.

---

## 6. The finite-pole congruence is valid but does not finish normalization

Let


$$
L_{\rm pole}=\lfloor\log_3(4n-3)\rfloor,\qquad
v_*=\frac{3^{L_{\rm pole}}-1}{2}.
$$


Among the retained odd denominators $2v+1\le4n-3$, the only one of valuation $L_{\rm pole}$ is $3^{L_{\rm pole}}$. The next possible odd multiple is $3^{L_{\rm pole}+1}$, outside the cutoff.

For integral normalized coefficients this proves


$$
3^{L_{\rm pole}}\sum_{v=0}^{2n-2}
\frac{C_v(P,Q)}{2v+1}
\equiv C_{v_*}(P,Q)\pmod3.
$$


Consequently A1’s complete relation


$$
3^{L_{\rm pole}-h}\mathcal T(PQ)
+
\frac{3^{L_{\rm pole}}}{4}\mathfrak f(Q_{\rm act}PQ)
\equiv3^6C_{v_*}(P,Q)\pmod{3^7}
$$


is correct.

But the factorial contribution has been moved to the other side of an exact identity; it has not been evaluated. Separate integrality of its two displayed left-hand summands is also not established merely by integrality of their sum.

Likewise,


$$
C^T\Delta C=3^{2g}\widetilde C^T\Delta\widetilde C
$$


is a valid homogeneous bilinear factorization. It does not prove


$$
T_R=3^g\widetilde T_R,\qquad
K_Z=3^{2g}\widetilde K_Z
$$


for the actual inhomogeneous source and its terminal charges.

The actual equations remain


$$
3^{-g}\widehat Z^{\,\rm act}
=
3^{-g}\widehat Z^{\,c}
-
3^{6-g}WE_{\rm act}^{-1}T_R,
$$


and


$$
3^{-2g}(S_{\rm act}-S_c)
=
3^{6-2g}K_Z-
3^{12-2g}T_R^TE_{\rm act}^{-1}T_R.
$$


The negative powers exposed by normalization are a real precision obligation.

**Audit conclusion:** the congruence passes; the claimed limitation is necessary. It does not normalize the complete inhomogeneous corrected columns.

---

## 7. What the modulo-$81$ receipt establishes

The supplied source compares:

- forty exact finite endpoint values, for the two polynomials at $m=221,\ldots,240$;
- all $121$ high words of length at most four;
- the prescribed divided endpoint pair and split-language test.

Its direct formula is the Bernstein endpoint sum with the summation index reversed, so it uses the correct adjacent parameter.

The receipt corroborates precisely those comparisons. It does not evaluate an eligible original power or prove an infinite language theorem by computation. The all-word theorem remains the retained symbolic result.

The planned min-plus/sign checks at $m=241,\ldots,260$ concern a different output and need not repeat this calculation.

---

# Part II. Audit of A2 turn 12

## 8. Closing the head hypothesis and retaining the terminal

The head identity


$$
f_i^0=\frac{(n+i)!}{n!}J_i
$$


gives, by Frobenius and $29\mid n$,


$$
f_i^0\equiv
\begin{cases}
J_0i!&0\le i<29,\\
0&i\ge29
\end{cases}
\pmod{29}.
$$


Hence


$$
f^0=J_0h^{[0]}+29h^{[1]}
$$


in the required integral coordinates. There is no need to evaluate a head table, and no justification for deleting $h^{[1]}$.

Using the retained complete $p^6$ normal form, the shift box and row-factor bounds are sufficient for A2’s uniform event argument. The terminal remains


$$
Z_{w,b}=bW_bx_{b-1},
$$


not an algebraically continued interior atom. Its valuation is at least six on the stated phase.

Thus the already closed result remains unconditional:


$$
u\equiv2\pmod{29^3}
\quad\Longrightarrow\quad
Z_w\in29^4\mathbb Z_{29}^{b+1},\qquad d\ge9.
$$



Here and below, the complete finite normal-form theorem is a reused premise. The new audit checks its subsequent precision use rather than claiming to reconstruct an omitted Turn 0 coefficient list.

---

## 9. Low-unit affinity and all eight interfaces

The factorial-strip identity is exact. It never divides by a possibly nonunit high binomial.

At precision $p^2$, the block formula


$$
F_p(pq+r)
\equiv((p-1)!)^q r!\left(1+pq\,\mathsf H_r\right)
\pmod{p^2}
$$


shows that only the last low level can introduce first-order dependence on the high index. In a balanced factorial ratio, the block powers cancel up to fixed low carries. Therefore


$$
L(J)\equiv L(0)+pJ L^{[1]}\pmod{p^2}
$$


is justified.

The row-factor guard is also sufficient:


$$
\binom{j+p^3}{r}\equiv\binom jr\pmod{p^2}
\qquad(r<p^2).
$$


Thus no additional high-index dependence comes from the retained row factors.

After division by $p^4$, terms whose coefficient order plus low-event count is:

- one require their unit lift modulo $p^2$;
- two require only their leading unit modulo $p$;
- at least three vanish modulo $p^2$, because the upper factor contributes $p^3$.

This is the correct reason that higher-head, second-lower, crossed-return, and second-return contributions are covered by


$$
F_j\equiv(-1)^{b-\ell-J}
\left[
(\widetilde a_\ell+pJb_\ell)K(J)
+p\sum_s c_{\ell,s}K_s(J)
\right]\pmod{p^2}.
$$


The argument does not require these coefficients to vanish.

---

## 10. The enlarged radical is valid on its exact support

For the first upper digit,


$$
(W_0,B_0,A_0)=(7,28,15).
$$


The minimal branches are:

- $J_0=0,\ldots,7$: no weight borrow, one addition carry;
- $J_0=15,\ldots,28$: one weight borrow, no addition carry.

The middle interval $8,\ldots,14$ has an extra event. At the next digit, $J_1=0$ resets the two minimal branches to the same outgoing interface.

This explains why inserting any function of $J_0$ changes only the first low scalar:


$$
\sum_J R(J_0)K(J)^2=0\pmod p.
$$


The remaining contraction is still the retained vanishing branch difference.

For $k=0$, the interface ratios are polynomial. For $k=1$, the only potential denominator is


$$
A+B-J\equiv14-J_0\pmod p.
$$


It is a unit on the support just listed: $J_0=14$ is excluded.

Hence the ratios may legitimately be reduced modulo $p$ **on the support of $K\bmod p$**. Off that support, $K K_s\equiv0$ because every $K_s$ is integral. Therefore


$$
\sum_JK(J)K_s(J)=0\pmod p
$$


for all eight interfaces, and


$$
\sum_JJ K(J)^2=0\pmod p.
$$



This proves the elimination of the whole cross term after it has been included.

### Cutoff completion

The interior cutoff is


$$
J\le B\quad(\ell<5044),\qquad
J\le B-1\quad(\ell\ge5044).
$$


At the missing endpoint,


$$
K(B)\in p\mathbb Z_p.
$$


Thus:

- $K(B)^2$ is zero modulo $p^2$;
- $pK(B)K_s(B)$ is zero modulo $p^2$;
- the physical terminal has $F_b\in p^2\mathbb Z_p$.

So all terms used in the squared expansion admit the stated completion. There is no double counting of the terminal.

The result is


$$
\frac{Z_w^TZ_w}{p^9}
=
\mathscr L\,
\frac{\sum_{J=0}^{B}U(J)^2}{p^7}
\pmod p.
$$



---

## 11. Explicit audit of the lifted reflection

The potentially delicate point is not the ordinary reflection modulo $p$, but whether its high-parameter derivatives also vanish.

At


$$
C_*=20916,\qquad X_*=41854298,
$$


the low digits are


$$
C_*=(7,25,24)_{29},\qquad
X_*=(19,8,3)_{29},\qquad
2X_*=(9,17,6)_{29}.
$$



For a low path of valuation one, write the first digits of $q$ and $C-q$ as $d_0,k_0$. They satisfy


$$
d_0+k_0=7+29\varepsilon,\qquad d_0,k_0\le19.
$$


There are:

- eight first-digit choices when $\varepsilon=0$;
- three when $\varepsilon=1$.

At the second digit, exactly one event is necessary.

- **Type A:** no weight borrow, one addition carry. There are nine choices, and the third-digit bridge is
  

$$
(d_2,k_2)=(3,21).
$$


- **Type B:** one weight borrow, no addition carry. There are twelve choices, and the bridge is
  

$$
(d_2,k_2)=(2,22).
$$



Thus the number of surviving low paths is


$$
(8+3)(9+12)=231.
$$


All outgoing interfaces are zero.

The first-digit squared weight is symmetric under $d_0\leftrightarrow k_0$: modulo $29$,


$$
\binom{9+k_0}{k_0}
=(-1)^{k_0}\binom{19}{k_0},
$$


and the sign disappears upon squaring.

Meanwhile the difference multiplier is


$$
\Delta(q)\equiv4(d_0-7/2)\pmod{29}.
$$


It changes sign under that reflection.

For fixed $\varepsilon$ and type, the third-digit bridge is independent of the first-digit choice. Therefore every first-order dependence of the low unit on the high parameters or high index has a coefficient constant across the reflected first-digit pair. Its contraction against the antisymmetric multiplier is zero.

This proves the important assertion:


$$
\frac{\mathcal B(C)}p=\gamma\,\mathcal H(t)\pmod p,
$$


with the ordinary tail $\mathcal H$, not a derivative tail.

The moment substitutions also check:


$$
E_3=22,\quad
H_{\rm I}=H_{\rm II}=13\mathcal H,
$$




$$
H_{\rm I}^{[1]}=11\mathcal H,\qquad
H_{\rm II}^{[1]}=22\mathcal H.
$$


Hence


$$
\frac{Z_w^TZ_w}{p^9}
=
\mathscr L\,\Xi\,\mathcal H(t)\pmod p.
$$



**Audit conclusion:** the new factorization is valid at the stated complete-normal-form scope. The value of $\Xi$ is not needed when $\mathcal H(t)=0$.

---

## 12. Consequences and limits

The accepted six-digit tail annihilation, together with the original principal-unit parametrization, gives


$$
u\equiv2\pmod{29^9}
\quad\Longrightarrow\quad
Z_w^TZ_w\in29^{10}\mathbb Z_{29}.
$$



The precision is sufficient: $Z_w\bmod p^6$, together with $Z_w\in p^4$, determines its norm modulo $p^{10}$.

This says neither


$$
c=2
$$


nor that a particular divided primitive norm residue is nonzero. A vanishing $\Xi$ would also not prove an all-depth theorem; it would only show that this next norm layer vanishes more broadly.

The accepted unbounded-content theorem excludes a nonempty full original cylinder with fixed finite $c$. It does not exclude thin subsequences, individual original indices, or a growing-depth mixed-to-norm relation.

The missing denominator-relevant quantity remains a **relative complete mixed contraction**, not another absolute norm lower bound.

---

# Part III. Audit of A5 and the historical prime-$3$ theorem

## 13. Every normalization factor survives correctly

The exact bridges are


$$
x=\frac{Z_w}{2R},\qquad
y=\frac{V_w}{4b!},\qquad
N=x^Tx,\qquad H=x^Ty.
$$


The prescribed weighted rows satisfy


$$
u_j=\frac{2\lambda R}{\omega_j}x_j,\qquad
v_j=\frac{4b!}{\omega_j}y_j.
$$


Therefore


$$
A_B=d_B^2\,4\lambda^2R^2N,\qquad
H_B=d_B^2\,8\lambda Rb!H.
$$


Their ratio is


$$
\frac{H_B}{A_B}
=
\frac{2b!}{\lambda R}\frac HN
=
\frac{H}{\mathscr D_nN},
$$


where


$$
\mathscr D_n=\frac{\lambda R}{2b!}
=\frac{(n!)^2\binom n{n/2}}{2^{n/2+1}b!}.
$$



At $2$,


$$
v_2(\mathscr D_n)
=
\frac{3n}{2}-v_2(b!)-s_2(n)-1=C_n.
$$


At every odd prime, integrality follows from the retained factorial expression. Thus $\mathscr D_n$ is an integer.

For every prime $\ell$,


$$
v_\ell(q_n)
=
\max\{v_\ell(\mathscr D_n)+v_\ell(N)-v_\ell(H),0\}.
$$


This is a statement about the genuine reduced ratio of the actual integer pair. The common clearer cancels from this difference, but it has not been replaced, estimated away, or confused with the final gcd.

---

## 14. The ternary theorem is old, and the formulas agree

Historical A2 turn 8 already establishes the complete norm and mixed contractions at their paid depths and obtains


$$
v_3(q_n)=n-\frac{b+15}{2}
=\frac{8003b-15}{2}.
$$



A5’s alternative derivation gives


$$
Z_w^TZ_w\equiv6\pmod9,\qquad
Z_w^T(V_w/b!)\equiv3\pmod9.
$$


With


$$
v_3(R)=3,
$$


this yields


$$
v_3(N)=-5,\qquad v_3(H)=-2.
$$


Thus the reduced raw numerator cancels exactly three powers of $3$ from $\mathscr D_n$.

The final gcd valuation in A5 is


$$
2v_3(d_B)+2v_3(n!)+v_3(b!)+1.
$$


Using the historical conclusion $v_3(d_B)=0$, this is exactly


$$
n+\frac{b-15}{2},
$$


as in historical A2.

There is no discrepancy and no new prime-$3$ discovery.

---

## 15. The shallow-binary no-go consequence is correct

On the retained shallow binary guards,


$$
v_2(N)=v_2(H),
$$


so


$$
v_2(q_n)=C_n
=
\left(\frac32-\frac1{4002}\right)n+O(\log n).
$$


Together with the exact ternary denominator,


$$
\log q_n\ge\kappa n+O(\log n),
$$


where


$$
\kappa=
\left(\frac32-\frac1{4002}\right)\log2+
\left(1-\frac1{8004}\right)\log3
\approx2.13802260.
$$


The retained whole-error coefficient is


$$
\beta=
\left(2+\frac1{4002}\right)\log(1+\sqrt2)
\approx1.76296741.
$$


Hence


$$
\kappa-\beta\approx0.37505519>0.
$$



Under the retained whole-error theorem,


$$
\log|\epsilon_n|=-\beta n+o(n),
$$


and therefore, on every infinite original sequence satisfying those guards,


$$
\log|q_n\epsilon_n|
\ge(\kappa-\beta)n+o(n)\longrightarrow+\infty.
$$



This is a no-go result for that approximation route, not a decision about $e+\pi$.

### Exact all-prime budget

Put


$$
\delta_2=v_2(H)-v_2(N),\qquad
\mathcal O_n=\sum_{\ell\ne2,3}v_\ell(q_n)\log\ell\ge0.
$$


Then the denominator identity is


$$
\log q_n
=
\bigl(C_n-\min(\delta_2,C_n)\bigr)\log2
+\frac{8003b-15}{2}\log3+\mathcal O_n.
$$


Consequently


$$
\log|q_n\epsilon_n|
=
(\kappa-\beta)n
-\min(\delta_2,C_n)\log2
+\mathcal O_n+o(n).
$$



Thus a necessary scale condition for $|q_n\epsilon_n|\to0$ is


$$
\delta_2\ge\eta n+o(n),
\qquad
\eta=\frac{\kappa-\beta}{\log2}\approx0.541090.
$$


Every surviving other-prime contribution makes the required binary saving larger.

---

# Part IV. New result: the complete source at the necessary linear depth

## 16. Exact decomposition with the original boundary

This section stays on


$$
b=3^{36+64u},\qquad n=4002b.
$$



Let $A$ be the actual finite $b\times b$ contact matrix and $\mathcal R$ the actual reconstruction into coordinates $0,\ldots,b$. Let


$$
\mathbf f=(j!)_{0\le j<b}.
$$


The finite boundary identity is


$$
\mathcal R\mathbf f=-e_0+b!W_be_b.
$$



Split the complete normalized second column as


$$
y=y^E+y^F,
$$


where


$$
y^E=
\frac{
\mathcal RA^{-1}(h^e-A\mathbf f)+b!W_be_b
}{4b!},
$$


and


$$
y^F=\frac{\mathcal RA^{-1}h^F}{4b!}.
$$



These are exact identities. The first part contains:

- the whole exponential force;
- subtraction by the actual finite matrix;
- every contact row $0\le i<b$;
- the actual exterior coordinate $b$.

The second part contains the whole logarithmic force. There is no recurrence step beyond the boundary.

The historical integral audit gives $A^{-1}\in M_b(\mathbb Z_2)$ and $x,y\in\mathbb Z_2^{b+1}$.

---

## 17. How much logarithmic protection survives the actual normalization?

The retained whole-force estimate is


$$
v_2(h_i^F)\ge
\frac n2+1-2\left\lfloor\log_2(2n+b-1)\right\rfloor.
$$


Since the finite inverse and reconstruction are $2$-integral,


$$
y^F\in2^{B_n}\mathbb Z_2^{b+1},
$$


where


$$
\boxed{
B_n=
\frac n2-v_2(b!)-1
-2\left\lfloor\log_2(2n+b-1)\right\rfloor.
}
$$


On the original family $B_n>0$, and


$$
B_n=
\left(\frac12-\frac1{4002}\right)n+O(\log n)
\approx0.499750125\,n+O(\log n).
$$



This is the correct normalized protection depth. The division by $4b!$ cannot be omitted.

Because $y$ and $y^F$ are integral, $y^E$ is integral as well.

---

## 18. A complete-source criterion for any desired binary gap

Write


$$
x=2^{a_n}x_0,
$$


with $x_0$ primitive over $\mathbb Z_2$, and put


$$
\nu_n=v_2(x_0^Tx_0).
$$


Then


$$
v_2(N)=2a_n+\nu_n.
$$



Define the exact complete-source contractions


$$
E_n=x_0^Ty^E,
\qquad
L_n=x_0^T(2^{-B_n}y^F).
$$


Both lie in $\mathbb Z_2$. Since


$$
H=2^{a_n}(E_n+2^{B_n}L_n),
$$


we obtain the exact relation


$$
\boxed{
\delta_2
=
v_2(E_n+2^{B_n}L_n)-a_n-\nu_n.
}
\tag{18.1}
$$



This separates actual first-column content from genuine mixed cancellation. In particular, increasing first-column content alone does not improve the gap: it also increases the required mixed depth.

### Theorem — Complete-source linear-depth criterion

For any integer $k$ such that


$$
a_n+\nu_n+k>B_n,
$$


one has


$$
\boxed{
\delta_2\ge k
}
$$


if and only if both


$$
\boxed{E_n\in2^{B_n}\mathbb Z_2}
\tag{18.2}
$$


and


$$
\boxed{
\frac{E_n}{2^{B_n}}+L_n
\in2^{\,a_n+\nu_n+k-B_n}\mathbb Z_2.
}
\tag{18.3}
$$



**Proof.** By (18.1), the required condition is


$$
E_n+2^{B_n}L_n
\in2^{a_n+\nu_n+k}\mathbb Z_2.
$$


Since the target exponent is larger than $B_n$, reduction modulo $2^{B_n}$ first forces (18.2). Dividing the whole expression by $2^{B_n}$ then gives (18.3). The converse follows by multiplication. ∎

This is a relation for the **complete source**, not a homogeneous reference identity.

---

## 19. An adjoint form that exposes every charge and the precision bill

For clarity, the contractions above can be written entirely in the original finite source coordinates. Set


$$
w=A^{-T}\mathcal R^Tx_0\in\mathbb Z_2^b.
$$


Then


$$
E_n=
\frac{
w^T(h^e-A\mathbf f)+b!W_bx_{0,b}
}{4b!},
$$


and


$$
L_n=
\frac{w^Th^F}{2^{B_n+2}b!}.
$$



Thus (18.3) is explicitly a congruence involving


$$
w^T(h^e-A\mathbf f),\qquad
w^Th^F,\qquad
b!W_bx_{0,b}.
$$


The terminal term is visible and is not absorbed into an invented extra source row.

At a target gap $k$, the combined unnormalized source numerator must be controlled modulo


$$
2^{\,v_2(b!)+2+a_n+\nu_n+k}.
$$


Relative to the accepted logarithmic-force bound, the additional required depth is exactly


$$
a_n+\nu_n+k-B_n.
$$



No selected entrywise congruence at fixed precision pays this bill.

---

## 20. Quantified obstruction at the denominator-relevant scale

The denominator comparison requires at least


$$
k=\eta n+o(n),\qquad \eta\approx0.541090,
$$


even before controlling primes other than $2,3$.

But


$$
B_n\approx0.499750125\,n.
$$


Therefore


$$
k-B_n
=
\left(
\eta-\frac12+\frac1{4002}
\right)n+o(n)
\approx0.041340\,n+o(n).
$$



The exact criterion consequently requires


$$
v_2\!\left(\frac{E_n}{2^{B_n}}+L_n\right)
\ge
0.041340\,n+a_n+\nu_n+o(n).
$$



This gives a concrete next target:

> **Linear complete-residual lemma.**  
> Prove, or rule out on the relevant original infinite families, the two conditions (18.2)–(18.3) with a modulus growing at least as
> 

$$
> 0.041340\,n+a_n+\nu_n+o(n)
>
$$


> after the paid $B_n$-division, while retaining the whole exponential residual, whole logarithmic source, and physical terminal.

The conclusion is deliberately precise:

- the accepted logarithmic bound does **not** prove that the logarithmic contribution is nonzero at depth $B_n$;
- it does **not** prove cancellation with the exponential source is impossible;
- it does prove that the existing absolute bound is insufficient to delete that source at the new target;
- any route that deletes it must supply additional contraction divisibility on a **linear**, not fixed, scale.

This is the normalization obstruction that low-precision witnesses cannot resolve.

---

# Part V. Proof status and remaining arithmetic

## 21. Finite work already in progress

No new finite computation is required for the proofs above.

The already planned new calculations have well-defined outputs.

### A. Min-plus/sign checks, $m=241,\ldots,260$

For both


$$
(s,n)=(m,3m-1),\qquad(m-1,3m-2),
$$


the verifiable outputs are:

- minimum Bernstein valuation;
- minimum monomial valuation;
- eight-state answer and a minimizing finite index;
- sixteen-state signed residue;
- exact endpoint divided by the reported full content, modulo $3$;
- all terminal carries.

Required equalities are


$$
r_{\rm Bernstein}=r_{\rm monomial}=r_{\rm module}
$$


and


$$
\text{signed residue}=3^{-r_{\rm module}}J_s^{[A]}(-1)\pmod3.
$$



These are forty new polynomial checks. They do not repeat the modulo-$81$ receipt.

### B. A2’s already specified $\Xi$-lift

The existing bounded specification should return


$$
(\alpha_{\rm I},\alpha_{\rm II},
\beta_{\rm I},\beta_{\rm II},\gamma,\Xi),
$$


with:

- branch counts $220,242$;
- the $231$-path count;
- $\alpha_{\rm I}\equiv4$, $\alpha_{\rm II}\equiv25\pmod{29}$;
- the stated paid divisibilities before division by $29$.

Its value distinguishes possibilities within the next norm layer. It does not by itself evaluate the actual mixed gap or exact $c$.

### C. Retained NEW3375 data

The receipt’s unit reference filters are accepted at $n=3375$. No producer, final gcd, denominator, or error should be regenerated. Any remaining $G/K_{\rm ref}$ extraction is the coordinator’s existing once-only retained-data operation.

---

## 22. Final ledger

| Statement | Status |
|---|---|
| A1 exact trailing-residue exception bound | **Proof verified**, using retained turn 17 language theorem |
| $20$-forcing for both full Jacobi polynomials | **Proof verified**, including half-integer comparison |
| Full content equals Bernstein minimum | **Proof verified by integral unimodularity** |
| Eight-state and sixteen-state evaluators | **Proof verified at their stated finite-index scope** |
| Density-one divergence of both full contents | **Proof verified** |
| Modulo-$81$ receipt | **Finite corroboration only**, accepted without rerun |
| A1 complete factorial/pole congruence | **Valid**, but factorial contraction remains unevaluated |
| A1 complete inhomogeneous source divisibility | **Outstanding** |
| A2 head closure and $c\ge2,d\ge9$ | **Closed unconditional results reused** |
| A2 complete $p^6$ eight-interface norm lift | **Structural proof verified at retained normal-form scope** |
| A2 lifted reflection and ordinary-tail factorization | **Proof verified**, with explicit bridge audit above |
| $d\ge10$ on $u\equiv2\pmod{29^9}$ | **Consequence of that proof and accepted tail receipt** |
| Exact $c$, first nonzero primitive norm digit, complete mixed gap | **Not determined** |
| A5 final scalar and all-prime denominator identity | **Proof verified** |
| $v_3(q_n)=(8003b-15)/2$ | **Historical theorem reused**, not new |
| Shallow-binary whole-error growth | **Conditional on the retained whole-error theorem**, correctly deduced |
| Exact linear-depth complete-source criterion (18.1)–(18.3) | **New proved result** |
| Existence or impossibility of the required linear cancellation | **Open** |
| Irrationality or rationality of $e+\pi$ | **Unresolved** |

---

## Conclusion

The new local advances survive the substantive audits, with their actual scopes preserved. A1 provides genuine density-one full-content growth and exact small evaluators. A2 provides a genuine complete next norm zero, not merely an extrapolation of a shallower contraction. A5’s correctly normalized denominator exposes a decisive scale failure of the shallow-binary route.

The new result of this turn is the exact complete-source criterion


$$
\delta_2
=
v_2(E_n+2^{B_n}L_n)-a_n-\nu_n,
$$


and its divided form (18.2)–(18.3). It converts the necessary binary gap into a concrete obligation on the original complete sources and terminal.

The exact remaining bottleneck is now:



$$
\boxed{
\begin{gathered}
\text{prove or rule out a binary mixed-to-norm gap of at least }0.54109n+o(n),\\
\text{including the resulting additional }0.04134n\text{-scale complete-source cancellation},\\
\text{then control every remaining prime in the actual primitive denominator.}
\end{gathered}}
$$



Further fixed-gap or fixed-block witnesses cannot settle that obligation. Nor can homogeneous reference content justify deleting a complete inhomogeneous force after normalization.

No infinite original sequence with


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0
$$


has been established, and no argument here proves rationality. The irrationality or rationality of $e+\pi$ remains unresolved.
