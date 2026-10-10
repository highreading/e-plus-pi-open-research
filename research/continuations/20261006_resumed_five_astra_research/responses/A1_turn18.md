> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 turn18 — Density-one deep full content, an exact small content module, and the normalized complete-force obstruction

## Executive conclusion

The higher-density conclusion is valid. In fact, the original fixed-tail progression permits a stronger elementary estimate than the proposed leading-cylinder estimate.

Retain


$$
M=531441=3^{12},\qquad j_*=84645,
$$


and the original indices


$$
j>0,\qquad j\equiv j_*\pmod M,\qquad m=2^{2j-1}.
$$


Let $\mathcal W$ denote the exact real-window subset of this progression, with the original $3^{-k}$ correction retained.

Then the established turn17 classification implies


$$
\boxed{
\#\{j\le X:j\in\mathcal W,\ c_m=3\}
=O\!\left((\log X)X^{\log_3 2}\right).
}
\tag{E.1}
$$


Since $\log_3 2<1$ and $\mathcal W$ has positive density, this proves


$$
\boxed{
c_m\ge4
\quad\text{on a relative-density-one subset of }\mathcal W.
}
\tag{E.2}
$$



The proof does **not** require an infinite exact-$c_m=3$ branch. It uses the exact principal-unit parametrization of the trailing digits on this progression. I also reconstruct the leading-cylinder argument separately, including its floors and prefix length; its extension to the split language is valid. I do not need to import the numerical $0.9725$ exponent to obtain (E.1).

The second coordinator deduction is also correct. Write $N_{20}(m)$ for the number of consecutive occurrences of $20$ in the ordinary ternary expansion of $m$. For every positive $m$ with $3\nmid m$,


$$
\boxed{
\begin{aligned}
\operatorname{cont}_3 J_m^{[\,2m-1\,]}&\ge N_{20}(m),\\
\operatorname{cont}_3 J_{m-1}^{[\,2m-1\,]}&\ge N_{20}(m).
\end{aligned}
}
\tag{E.3}
$$


Moreover, if


$$
\rho=\frac{3+\sqrt5}{2},
\qquad d_{20}=\log_3\rho<1,
$$


then, for each fixed $R\ge0$,


$$
\boxed{
\#\left\{j\le X:
\min\!\left(
\operatorname{cont}_3J_m^{[A]},
\operatorname{cont}_3J_{m-1}^{[A]}
\right)\le R
\right\}
=O_R\!\left((1+\log X)^R X^{d_{20}}\right),
}
\tag{E.4}
$$


where $m=2^{2j-1}$ and $A=2m-1$. Thus **both full polynomial contents, and hence the common endpoint content, tend to infinity in density**, including relative density on every fixed original progression with a positive-density exact window.

There is also an exact, small full-content evaluator:

* an **eight-state min-plus module** computes the actual full content of each same-parameter Jacobi polynomial;
* adjoining the doubling carry gives a **sixteen-state signed module** which computes its endpoint divided by that full content, modulo $3$;
* both modules preserve the finite range $0\le k\le s$, the ordinary and generalized binomial borrows, and all final carries.

This is an exact full-content formula, not an asserted closed formula solely in terms of $20$-occurrences. It also gives an exact test for whether endpoint evaluation loses an additional digit beyond full polynomial normalization.

Finally, common polynomial content cancels in the exact homogeneous Christoffel source identity and factors quadratically out of a complete bilinear force contraction. It does **not**, without another divisibility statement, cancel from an inhomogeneous corrected-column residual. I derive below a target-specific divided finite-pole congruence which retains the entire factorial term and the original cutoff. The actual complete residual, scalar-root approach, all-prime gcd, primitive denominator, and whole nonzero same-index error remain unresolved.

No code was executed, and no result of the announced modulo-$81$ computation is assumed.

---

## 1. Scope, normalization, and proof status

The domain remains


$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad A=2m-1.
$$


Set


$$
H_{\rm win}=3^{h-1},\qquad D=H_{\rm win}-A,
$$


and retain the exact window


$$
\frac1{2C_{16}}
<
\frac{D}{H_{\rm win}}
<
\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
\tag{1.1}
$$



The Jacobi normalization is


$$
J_s^{[A]}(y)
=
\sum_{k=0}^{s}
\binom{s+A}{k}
\binom{s-\tfrac12}{s-k}
y^k(y-1)^{s-k}.
\tag{1.2}
$$


It lies in $\mathbb Z[1/2][y]$, hence in $\mathbb Z_3[y]$. No ordinary-integer normalization is silently substituted.

The exact endpoint identities remain


$$
X_m=J_m^{[\,2m-1\,]}(-1),\qquad
Y_m=J_{m-1}^{[\,2m-1\,]}(-1).
\tag{1.3}
$$


In particular, the adjacent degree uses the **same** parameter $A=2m-1$.

Write


$$
r_+(m)=\operatorname{cont}_3 J_m^{[A]},\qquad
r_-(m)=\operatorname{cont}_3 J_{m-1}^{[A]},
$$




$$
g_m=\min(r_+(m),r_-(m)),\qquad
c_m=\min(v_3(X_m),v_3(Y_m)).
\tag{1.4}
$$


Always


$$
c_m\ge g_m.
\tag{1.5}
$$


Equality is an additional evaluation statement, not a definition.

I reuse the proved turn17 results:

1. the fixed-tail full-polynomial divisibility by $27$;
2. the divided endpoint observable $\psi(H)$;
3. its exact nonvanishing language
   

$$
\psi(H)\ne0
   \iff H\in\{0,1\}^{*}\{1,2\}^{*};
$$


4. the instantiated original progression $j\equiv84645\pmod{531441}$;
5. its positive-density exact-window realization.

The new modulo-$81$ calculation remains independent corroboration when received. Nothing below assumes its output.

---

# Part I. The higher-density conclusion

## 2. Reconstructing the leading-cylinder proof

The proposed extension of the primary proof is sound. It is useful to state precisely what is being generalized.

I reconstruct the continued-fraction spacing argument from the supplied Section 2 ingredients rather than treating the theorem’s digit-omission statement as a theorem about arbitrary languages. I have not independently retrieved and checked the primary text’s numerical linear-form constant in this turn; consequently, the numerical exponent $0.9725$ is not a premise of any result claimed here.

### 2.1 Exact leading cylinders, including the floor

Fix $\lambda>0$, and put


$$
z_n=\lfloor\lambda2^n\rfloor,\qquad
\theta=\log_3 2.
$$


Suppose $z_n$ has at least $d$ ternary digits. Let $a$ be a $d$-digit ternary integer:


$$
3^{d-1}\le a<3^d.
$$


Then $z_n$ begins with the digits of $a$ exactly when


$$
\{\log_3\lambda+n\theta\}
\in
I_a:=
\left[
\log_3\frac a{3^{d-1}},
\log_3\frac{a+1}{3^{d-1}}
\right).
\tag{2.1}
$$



There is no approximation here. If the total digit length is $L$, then


$$
a3^{L-d}\le\lambda2^n<(a+1)3^{L-d}
$$


is equivalent to the same inequalities for its integer floor, because both endpoints are integers.

The cylinder length satisfies


$$
|I_a|
=
\log_3(1+1/a)
<
\frac{3^{1-d}}{\log 3}.
\tag{2.2}
$$



The indices for which $z_n$ has fewer than $d$ digits form an initial segment of length $O_\lambda(d)$. They must be excluded before applying (2.1), and can then be counted separately.

### 2.2 Six orbit points per cylinder

Let $q$ be a sufficiently large continued-fraction denominator of $\theta$, and take


$$
d=\lceil\log_3 q\rceil.
\tag{2.3}
$$


The standard best-approximation inequality gives, for
$1\le t<q$,


$$
\|t\theta\|>\frac1{2q}.
\tag{2.4}
$$


Thus any translated block of $q-1$ consecutive orbit points is separated on the circle by more than $1/(2q)$.

By (2.2)–(2.3),


$$
|I_a|<\frac{3}{q\log 3}.
$$


Hence a cylinder contains at most six points from such a block:


$$
\boxed{
\#\{n\text{ in a block of length }q-1:
\{\log_3\lambda+n\theta\}\in I_a\}\le6.
}
\tag{2.5}
$$


The translation $\log_3\lambda$ does not change the separation.

This recovers the relevant classical cylinder estimate, with its finite block length preserved.

### 2.3 Replacing the prefix count

Let $B(d)$ be an upper bound for the number of allowable leading words of length $d$. If membership in the full-word language implies that its leading $d$-word is allowable, then (2.5) gives


$$
\boxed{
\#\{n\le N:z_n\text{ is in the language}\}
\ll_\lambda
d+\left(\frac Nq+1\right)B(d).
}
\tag{2.6}
$$



This is the exact point at which the original single-digit-omitting prefix count may be replaced. Nothing else in the argument depends on the omitted digit.

For the split language


$$
\mathcal L_{\rm split}=\{0,1\}^{*}\{1,2\}^{*},
$$


one has


$$
B(d)\le(d+1)2^d.
\tag{2.7}
$$


Indeed, choose a split position and choose each digit from the corresponding two-letter alphabet. Overcounting is harmless.

If $q\le N<q_{\rm next}$, and a fixed finite irrationality-measure bound supplies


$$
q_{\rm next}\le Cq^\tau
\tag{2.8}
$$


for some fixed $\tau<\infty$, then (2.6) becomes


$$
\boxed{
O_\lambda\!\left(
(\log N)N^{\,1-(1-\log_3 2)/\tau}
\right).
}
\tag{2.9}
$$


A finite $\tau$ for $\log_3 2$ follows from the classical lower bounds for nonzero linear forms in $\log2,\log3$. Thus this already gives a fixed exponent below one, without a normality assertion.

If the numerical continued-fraction growth input used in the primary proof is retained with its verified constants, the corresponding numerical exponent follows through exactly the same calculation. I do not infer that numerical input merely from the theorem statement.

### 2.4 Density zero needs even less

For completeness, equidistribution at each fixed $d$ gives upper density at most


$$
\sum_{\text{allowable }a}|I_a|
\ll B(d)3^{-d}.
$$


For the split language this is


$$
O\!\left((d+1)(2/3)^d\right)\longrightarrow0.
$$


Thus the density-zero consequence requires only the fixed-cylinder argument and irrational rotation. The quantitative estimate requires the additional continued-fraction growth input.

---

## 3. Applying the leading argument to the exact original window

Here the fixed multiplier is precisely


$$
\boxed{\lambda=3^{-13}.}
\tag{3.1}
$$


At an original index,


$$
\left\lfloor3^{-13}2^{2j-1}\right\rfloor
=
\left\lfloor\frac m{3^{13}}\right\rfloor.
\tag{3.2}
$$



On the fixed-tail progression,


$$
m\equiv1194953\pmod{3^{13}},
\qquad0<1194953<3^{13}.
$$


For sufficiently large exact-window indices, turn17 gives


$$
m=(1^{25}H\,20202\,01011112)_3.
$$


Therefore


$$
\boxed{
\left\lfloor\frac m{3^{13}}\right\rfloor=(1^{25}H)_3.
}
\tag{3.3}
$$


The floor removes exactly the fixed thirteen digits. It does not remove a variable number of digits or introduce a moving multiplier.

If $c_m=3$, turn17 gives $\psi(H)\ne0$, hence $H\in\mathcal L_{\rm split}$. Prepending $1^{25}$ preserves this language. Consequently the **entire** high word in (3.3), and hence each sufficiently short leading prefix, is in the split language.

The restriction to odd exponents $n=2j-1$, to the progression, and to the window only reduces the count in (2.6). A bound for all $n\le2X$ is therefore a valid upper bound for the relevant $j\le X$.

### 3.1 The real-window correction remains exact

Let


$$
a_0=\frac1{2C_{16}},\qquad b_0=\frac1{C_{16}},
\qquad \alpha=\log_3 4,\qquad k=h-1.
$$


For sufficiently large window indices,


$$
k=\lceil j\alpha\rceil,
$$


and


$$
\frac D{3^k}
=
1-3^{\{j\alpha\}-1}+3^{-k}.
\tag{3.4}
$$


Thus the exact rotation interval is


$$
1+\log_3(1-b_0+3^{-k})
<
\{j\alpha\}
<
1+\log_3(1-a_0+3^{-k}).
\tag{3.5}
$$


Squeezing by fixed inner and outer intervals yields


$$
\delta=
\log_3\frac{1-a_0}{1-b_0}>0
\tag{3.6}
$$


as the relative window density on every fixed compatible progression.

On $j\equiv j_*\pmod M$, therefore,


$$
\#\{j\le X:j\in\mathcal W\}
=
\frac{\delta}{M}X+o(X).
\tag{3.7}
$$



Subtracting any of the sublinear bounds above proves relative density one of $c_m\ge4$. The exact-window correction has not been dropped.

---

## 4. A stronger target-specific bound from trailing digits

The original progression has more structure than an arbitrary fixed-$\lambda$ real orbit. It gives a stronger count by an elementary finite residue argument.

### Lemma 4.1 — Exact quotient-digit parametrization

Write


$$
j=j_*+Mt,\qquad t\ge0,
$$


and


$$
m(t)=2^{2j-1}.
$$


For every $a\ge0$, the map


$$
t\bmod3^a
\longmapsto
\left\lfloor\frac{m(t)}{3^{13}}\right\rfloor\bmod3^a
\tag{4.1}
$$


is a bijection.

**Proof.**
By LTE,


$$
v_3(4^M-1)=1+v_3(M)=13.
$$


Consequently $4^M$ generates the subgroup


$$
1+3^{13}\mathbb Z/3^{13+a}\mathbb Z,
$$


which has order $3^a$. Multiplication by the unit $m(0)$ maps this subgroup bijectively onto the residue class


$$
m\equiv1194953\pmod{3^{13}}.
$$


Writing


$$
m=1194953+3^{13}u
$$


identifies that class with $u\bmod3^a$. Since the fixed residue lies between $0$ and $3^{13}-1$, this $u$ is exactly $\lfloor m/3^{13}\rfloor$. ∎

The split language is closed under taking contiguous subwords and under prepending zeros. Therefore, whenever the high word $1^{25}H$ is split, its lowest $a$ digits, padded on the left if necessary, are split.

Let $T$ be the number of progression indices under consideration, and choose


$$
a=\lfloor\log_3 T\rfloor.
$$


Each residue class $t\bmod3^a$ occurs at most three times among $T$ consecutive values of $t$. Lemma 4.1 and (2.7) therefore give the explicit finite bound


$$
\#\{t<T:\text{high word is split}\}
\le3(a+1)2^a.
\tag{4.2}
$$



### Theorem 4.2 — Sublinear exact-$c_m=3$ exceptions

On the original fixed-tail exact-window family,


$$
\boxed{
\#\{j\le X:j\in\mathcal W,\ c_m=3\}
=
O\!\left((1+\log X)X^{\log_3 2}\right).
}
\tag{4.3}
$$


Hence $c_m\ge4$ with relative density one in $\mathcal W$.

**Proof.**
Apart from finitely many indices before the established prefix condition applies, exact content three implies the split high word by turn17. Apply (4.2), with $T=O(X/M)$, and then (3.7). ∎

This is stronger than the proposed $O(\log X\,X^{0.9725})$ count. It does not contradict the scope of the primary theorem: it exploits the special triadic multiplier and the exact principal-unit progression, which are unavailable for an arbitrary positive real $\lambda$.

It also does not prove that the exceptional exact-$c_m=3$ set is infinite—or finite.

---

# Part II. Full polynomial content

## 5. Every $20$-occurrence forces a full coefficient digit

The turn17 forcing lemma applies at every appropriate level, not merely the three fixed levels.

Let $P=3^h$. If the top two digits of $m\bmod P$ are $20$, then


$$
m\bmod P=\frac{2P}{3}+u,
\qquad0\le u<\frac P9.
\tag{5.1}
$$


If $3\nmid m$, then $u\ne0$. Thus


$$
\frac{2P}{3}+1
\le m\bmod P
\le\frac{7P}{9}-1
\le\frac{5P-3}{6}.
\tag{5.2}
$$


This is inside the proved simultaneous forcing interval.

The final two digits of a $3$-adic unit cannot themselves be $20$, so no unhandled $u=0$ occurrence remains at the bottom.

Distinct occurrences correspond to distinct powers $P$. At each such level, every Bernstein coefficient of each of the two same-parameter polynomials receives at least one valuation contribution. Contributions at other levels are nonnegative.

### Theorem 5.1 — Global $20$-pattern lower bound

For every positive integer $m$ with $3\nmid m$,


$$
\boxed{
r_+(m)\ge N_{20}(m),\qquad
r_-(m)\ge N_{20}(m).
}
\tag{5.3}
$$



This is a full-polynomial theorem. It does not rely on endpoint cancellation.

For the fixed thirteen-digit tail, its three occurrences of $20$ recover the turn17 bound $r_+,r_-\ge3$. Additional occurrences anywhere above that tail supply additional common full content.

---

## 6. Why Bernstein coefficient minima give the actual content

Let


$$
B_{s,k}(y)=y^k(y-1)^{s-k},\qquad0\le k\le s.
$$


The smallest monomial degree in $B_{s,k}$ is $k$, and its coefficient is


$$
(-1)^{s-k}.
$$


Thus the coefficient matrix from the ordered Bernstein family to the monomial family is triangular with diagonal entries $\pm1$. Its inverse is integral.

Consequently the two coefficient families generate the same ideal over $\mathbb Z_3$.

### Proposition 6.1 — Exact full-content formula

For $n=s+A$,


$$
\boxed{
\operatorname{cont}_3J_s^{[A]}
=
\min_{0\le k\le s}
v_3\!\left[
\binom nk\binom{s-\tfrac12}{s-k}
\right].
}
\tag{6.1}
$$



There is no possible cancellation of a common factor in passing between these bases. This is why a min-plus evaluator can determine full content exactly, while an endpoint evaluator must still sum units.

---

## 7. An explicit factorial and digit-sum formula

Put $r=s-k$. The exact Bernstein coefficient is


$$
\boxed{
\binom nk\binom{s-\tfrac12}{s-k}
=
\frac{n!(2s)!}
{(n-k)!(2k)!s!r!\,4^r}.
}
\tag{7.1}
$$


The dyadic denominator is a $3$-adic unit and must not be confused with an ordinary integral normalization.

Let $S_3(N)$ be the sum of the ternary digits of $N$. Legendre’s formula gives


$$
\boxed{
e_s(k):=
v_3\!\left[
\binom nk\binom{s-\tfrac12}{s-k}
\right]
=
\frac{
S_3(n-k)+S_3(2k)+S_3(s)+S_3(s-k)
-S_3(n)-S_3(2s)
}{2}.
}
\tag{7.2}
$$


Therefore


$$
\boxed{
\operatorname{cont}_3J_s^{[A]}
=
\min_{0\le k\le s} e_s(k).
}
\tag{7.3}
$$



For the target pair:


$$
(s,n)=(m,3m-1),\qquad (m-1,3m-2).
\tag{7.4}
$$


The latter is equivalently $n=3s+1$, not $3s-1$.

Formula (7.3) is already exact, but a direct minimization has $s+1$ candidates. The following digit module reduces it to a fixed number of states per ternary digit.

---

## 8. An eight-state min-plus module for exact full content

Choose $L$ so that


$$
3^L>\max(n,2s).
\tag{8.1}
$$


Write $s_i,n_i$ for the ternary digits, $0\le i<L$.

### 8.1 Generalized-binomial comparison digits

Define


$$
a_0=0,\qquad
\alpha_i=(s_i+1+a_i)\bmod3,\qquad
a_{i+1}=\left\lfloor\frac{s_i+1+a_i}{3}\right\rfloor.
\tag{8.2}
$$


Then the lowest $h$ digits $\alpha_0,\ldots,\alpha_{h-1}$ represent


$$
\alpha_{3^h}(s)
=
\left(s+\frac{3^h-1}{2}\right)\bmod3^h.
\tag{8.3}
$$


The carry $a_i$ is determined entirely by the input $s$; it need not enlarge the optimization state.

### 8.2 The optimization states and transitions

Use states


$$
(c,b,g)\in\{0,1\}^3,
$$


where

* $c$ is the carry in $k+r=s$;
* $b$ is the borrow in $n-k$;
* $g$ is the borrow in the generalized comparison $\alpha-r$.

At digit $i$, choose $x,y\in\{0,1,2\}$, the digits of $k,r$, subject to


$$
x+y+c=s_i+3c',\qquad c'\in\{0,1\}.
\tag{8.4}
$$


Set


$$
b'=\mathbf1_{\{x+b>n_i\}},\qquad
g'=\mathbf1_{\{y+g>\alpha_i\}}.
\tag{8.5}
$$


The transition cost is


$$
\boxed{b'+g'.}
\tag{8.6}
$$



Start at


$$
(c,b,g)=(0,0,0)
$$


with cost zero, and accept only the terminal state


$$
(c,b,g)=(0,0,0)
$$


after $L$ digits.

### Theorem 8.1 — Exactness of the content module

The minimum accepted path cost is exactly


$$
\operatorname{cont}_3J_s^{[A]}.
\tag{8.7}
$$



**Proof.**
The initial and terminal addition carries in (8.4) make accepted choices correspond exactly to


$$
k+r=s,\qquad0\le k,r\le s.
$$


No index outside the finite Bernstein sum is admitted.

The outgoing borrow $b'$ at level $3^{i+1}$ is exactly


$$
\mathbf1_{\{k\bmod3^{i+1}>n\bmod3^{i+1}\}},
$$


the ordinary binomial’s valuation contribution.

Likewise $g'$ is exactly


$$
\mathbf1_{\{r\bmod3^{i+1}>
\alpha_{3^{i+1}}(s)\}},
$$


the generalized binomial’s valuation contribution.

Their sums therefore give $e_s(k)$. Condition (8.1) ensures that all later contributions vanish: $n-k\ge0$, $2s<3^L$, and


$$
s\le s+\frac{3^L-1}{2}<3^L.
$$


In particular, there is no unfinished generalized borrow to be charged beyond the terminal digit.

Minimizing over accepted paths is exactly the minimum in (6.1). ∎

The module has eight states, at most nine digit choices per state, and $L=O(\log s)$ steps. It is an exact target-specific dynamic formula.

It is **not** a proof that the answer equals $N_{20}(m)$. Other valuation events can force additional content, and the module retains them.

### 8.3 A simple logarithmic upper bound

Taking $k=0$ gives


$$
\operatorname{cont}_3J_s^{[A]}
\le
v_3\binom{2s}{s}.
\tag{8.8}
$$


The right side is the number of carries when doubling $s$ in base three, hence is at most the number of digits of $2s$.

Thus full polynomial content is always $O(\log s)$ in this normalization. This does not bound the additional valuation created by endpoint summation.

---

## 9. A sixteen-state signed module for the endpoint/full-content gap

The min-plus result can be enhanced without discarding the dyadic units.

Let $d_2(N)$ count ternary digits equal to $2$. For the $3$-adic unit part of $N!$,


$$
3^{-v_3(N!)}N!
\equiv(-1)^{v_3(N!)+d_2(N)}\pmod3.
\tag{9.1}
$$


The endpoint summand is


$$
(-1)^s
\binom nk\binom{s-\tfrac12}{s-k}2^{s-k}.
$$


If its valuation is $e=e_s(k)$, its unit residue is


$$
\boxed{
(-1)^{
e+k+d_2(n)+d_2(2s)
-d_2(n-k)-d_2(2k)-d_2(s)-d_2(s-k)
}.
}
\tag{9.2}
$$


This includes the evaluation sign and the dyadic endpoint unit.

Adjoin to the eight states the carry $d\in\{0,1\}$ in doubling $k$. For a digit choice $x$, put


$$
t_i=(2x+d)\bmod3,\qquad
d'=\left\lfloor\frac{2x+d}{3}\right\rfloor,
\tag{9.3}
$$


and let


$$
z_i=n_i-x-b+3b'
$$


be the digit of $n-k$.

Attach the local sign


$$
\boxed{
(-1)^{
b'+g'+x-\mathbf1_{\{z_i=2\}}
-\mathbf1_{\{t_i=2\}}
-\mathbf1_{\{y=2\}}
}.
}
\tag{9.4}
$$


Multiply the accepted path sum by the fixed input sign


$$
(-1)^{d_2(n)+d_2(2s)-d_2(s)}.
\tag{9.5}
$$


The doubling carry starts and ends at zero.

For each state, store:

1. the minimum path cost;
2. the sum in $\mathbb F_3$ of the signs of paths attaining that cost.

A zero sign sum must **not** be treated as absence of paths. It means cancellation at the known minimum coefficient valuation.

### Theorem 9.1 — Paid endpoint residue at full content

If


$$
r_s=\operatorname{cont}_3J_s^{[A]},
$$


the signed module computes exactly


$$
\boxed{
3^{-r_s}J_s^{[A]}(-1)\pmod3.
}
\tag{9.6}
$$



**Proof.**
Every coefficient valuation is at least $r_s$, by Theorem 8.1. After division by $3^{r_s}$, only minimum-cost summands can contribute modulo $3$. Their units are precisely (9.2), factored digit by digit in (9.4)–(9.5). All index and final-carry conditions are unchanged. ∎

This gives an exact common-gap criterion for the target pair. Compute $r_+,r_-$, let $g=\min(r_+,r_-)$, and set the residue of a polynomial with content $>g$ to zero. Then


$$
\boxed{
c_m=g
\iff
\left(3^{-g}X_m,\ 3^{-g}Y_m\right)\not\equiv(0,0)\pmod3.
}
\tag{9.7}
$$


If both residues vanish, the conclusion is $c_m\ge g+1$, not an exact higher value.

Thus the full-content normalization and the first endpoint cancellation after that normalization are now separated by an explicit small computation. Determining deeper endpoint cancellation still requires further paid unit precision.

---

# Part III. Full content tends to infinity in density

## 10. Counting words with boundedly many occurrences of $20$

Let $A_R(L)$ count ternary words of length $L$, allowing leading zeros, with at most $R$ occurrences of $20$.

For zero occurrences, distinguish words ending in $2$ from those ending in another digit. The transition matrix may be written


$$
\begin{pmatrix}
2&1\\
1&1
\end{pmatrix},
\tag{10.1}
$$


with characteristic polynomial


$$
z^2-3z+1.
$$


Its spectral radius is


$$
\rho=\frac{3+\sqrt5}{2}<3.
$$


Therefore


$$
A_0(L)=O(\rho^L).
\tag{10.2}
$$



Occurrences of $20$ do not overlap with themselves. A word with exactly $r$ occurrences can be decomposed at those occurrences into $r+1$ zero-occurrence pieces, separated by $r$ marked copies of $20$. Counting lengths and then pieces gives


$$
\boxed{
A_R(L)\le C_R(L+1)^R\rho^L.
}
\tag{10.3}
$$


This is an upper bound; possible extra boundary restrictions only reduce the count.

The leading-cylinder argument of §2 consequently applies with


$$
B(d)\le C_R(d+1)^R\rho^d.
$$


It yields a sublinear fixed-exponent count under the same finite irrationality-measure input, and density zero from fixed-cylinder equidistribution alone.

For the original integer powers, however, the trailing-digit parametrization again gives a stronger direct estimate.

---

## 11. A quantitative original-power count

For every $L\ge1$, the map


$$
j\bmod3^{L-1}
\longmapsto
2^{-1}4^j\bmod3^L
\tag{11.1}
$$


is a bijection onto the residues congruent to $2\pmod3$.

Choose


$$
L=1+\lfloor\log_3 X\rfloor.
$$


Every residue class $j\bmod3^{L-1}$ occurs at most three times among $1\le j\le X$.

If $N_{20}(m)\le R$, the lowest $L$ digits of $m$, padded with leading zeros if necessary, also have at most $R$ occurrences. Hence


$$
\#\{j\le X:N_{20}(2^{2j-1})\le R\}
\le3A_R(L).
$$


Using (10.3),


$$
\boxed{
\#\{j\le X:N_{20}(2^{2j-1})\le R\}
=
O_R\!\left((1+\log X)^R X^{\log_3\rho}\right).
}
\tag{11.2}
$$



### Theorem 11.1 — Density-one deep full content

For every fixed $R\ge0$,


$$
\boxed{
\#\{j\le X:g_m\le R\}
=
O_R\!\left((1+\log X)^R X^{\log_3\rho}\right).
}
\tag{11.3}
$$



**Proof.**
Theorem 5.1 gives $g_m\ge N_{20}(m)$. Thus $g_m\le R$ implies $N_{20}(m)\le R$, and (11.2) applies. ∎

Since


$$
\log_3\rho<1,
$$


both full polynomial contents tend to infinity in density. By $c_m\ge g_m$, so does endpoint content.

The conclusion remains true in relative density on every fixed original arithmetic progression whose exact window has positive density: intersecting the exceptional set with that family cannot enlarge its sublinear count, while its denominator count is asymptotically a positive constant times $X$.

This is not eventual divergence at every index, and it does not produce a primitive endpoint direction.

---

# Part IV. What common deep content does—and does not—cancel

## 12. Exact homogeneous Christoffel normalization

Retain the scalar identity


$$
(3y-\eta)Z_{\rm src}(y)
=
(y-\beta_m-\chi_m)J_m^{[A]}(y)
-\rho_mJ_{m-1}^{[A]}(y),
\tag{12.1}
$$


where


$$
\eta=A+71,\qquad
\rho_m=\frac{A(3A+1)}{(4A+1)(4A+3)}.
$$


On the stated integral scalar branch,


$$
\beta_m,\chi_m\in3\mathbb Z_3,\qquad v_3(\rho_m)=4,
$$


and $\eta$ is a unit.

Take any common full-content factor $3^g$, in particular $g=g_m$, and write


$$
J_m^{[A]}=3^gP,\qquad
J_{m-1}^{[A]}=3^gQ.
\tag{12.2}
$$


Gauss content multiplicativity over $\mathbb Z_3[y]$, applied to the primitive polynomial $3y-\eta$, gives


$$
Z_{\rm src}=3^g\widetilde Z_{\rm src},
$$


with


$$
\boxed{
(3y-\eta)\widetilde Z_{\rm src}
=
(y-\beta_m-\chi_m)P-\rho_mQ.
}
\tag{12.3}
$$



Thus the common deep full content **does cancel exactly in this homogeneous source identity**.

Modulo $3$, $A\equiv0$, $\eta\equiv2$, and $-\eta\equiv1$. Hence


$$
\boxed{\widetilde Z_{\rm src}(y)\equiv yP(y)\pmod3.}
\tag{12.4}
$$


In particular,


$$
\widetilde Z_{\rm src}(-1)\equiv-P(-1)\pmod3.
\tag{12.5}
$$



This does not assert that $P$, $Q$, or their endpoint pair is primitive when $g$ is only a lower bound. Taking $g=g_m$ makes the polynomial pair primitive, but endpoint evaluation can still annihilate both first residues.

### 12.1 The four-digit inverse loss survives

At the endpoint,


$$
\widetilde Z_{\rm src}(-1)
=
\lambda_m P(-1)+\mu_mQ(-1),
$$


with


$$
\lambda_m\equiv-1\pmod3,\qquad v_3(\mu_m)=4.
$$


The common factor $3^g$ has disappeared, but the normalized map still has Smith exponents $(0,4)$.

Therefore:

* normalized inverse recovery of $Q(-1)\bmod3^K$ still requires the relevant transformed numerator modulo $3^{K+4}$;
* in unnormalized coordinates the corresponding absolute precision is $3^{g+K+4}$;
* deeper common content does not improve scalar-root separation.

The split scalar quadratic and its root valuations $3$ and $4$ remain unchanged after removing a homogeneous common factor. The scalar congruence $\mathfrak a\equiv25\pmod{27}$, and original endpoint approach to its exceptional root lines, remain separate hypotheses.

---

## 13. Complete bilinear force: exact content factorization

Define the exact finite functional


$$
\begin{aligned}
\mathcal T(F)
={}&-\frac{3^h}{4}\mathfrak f(Q_{\rm act}F)\\
&+3^{h+6}
\sum_{v=0}^{2n-2}
\frac{
[y^v]\displaystyle
\frac{R_{\rm prod}(y)F(y)-R_{\rm prod}(-1)F(-1)}{y+1}
}{2v+1}.
\end{aligned}
\tag{13.1}
$$


This is exactly the retained perturbation:


$$
\Delta_{ad}=\mathcal T(y^{a+d}),
\qquad0\le a,d\le m.
\tag{13.2}
$$



It retains:

* the whole factorial functional $\mathfrak f$;
* $Q_{\rm act}=Q_c+3^6R_{\rm prod}$;
* $R_{\rm prod}=R_{25}+3^{25}\Delta_{25}$;
* every allowed pole through $2v+1\le4n-3$;
* the entire LOW subtraction;
* all unpaired finite-boundary terms represented by this finite sum.

If $F=3^{g_1}P$ and $G=3^{g_2}Q$, linearity gives the exact relation


$$
\boxed{
\mathcal T(FG)=3^{g_1+g_2}\mathcal T(PQ).
}
\tag{13.3}
$$


Thus common full content factors quadratically out of a complete bilinear contraction, not merely its leading pole.

For a two-column coefficient matrix $C=3^g\widetilde C$,


$$
\boxed{
C^T\Delta C=3^{2g}\widetilde C^T\Delta\widetilde C.
}
\tag{13.4}
$$



This is the precise sense in which the common deep content cancels in the homogeneous complete-force comparison. It is not yet an inhomogeneous corrected-column theorem.

---

## 14. A target-specific divided finite-pole congruence

The finite boundary yields an additional exact normalized congruence.

Put


$$
L_{\rm pole}=\lfloor\log_3(4n-3)\rfloor,
\qquad
v_*=\frac{3^{L_{\rm pole}}-1}{2}.
\tag{14.1}
$$


Among the odd denominators $2v+1\le4n-3$, the unique one of valuation $L_{\rm pole}$ is


$$
2v_*+1=3^{L_{\rm pole}}.
$$


Indeed, any other odd multiple would be at least $3\cdot3^{L_{\rm pole}}$, outside the cutoff.

For integral normalized $P,Q,R_{\rm prod}$, define


$$
C_v(P,Q)=
[y^v]\frac{
R_{\rm prod}(y)P(y)Q(y)
-R_{\rm prod}(-1)P(-1)Q(-1)
}{y+1}.
\tag{14.2}
$$


Then


$$
\boxed{
3^{L_{\rm pole}}
\sum_{v=0}^{2n-2}\frac{C_v(P,Q)}{2v+1}
\equiv C_{v_*}(P,Q)\pmod3.
}
\tag{14.3}
$$



Combining this with the **whole** factorial contribution in (13.1) gives


$$
\boxed{
3^{L_{\rm pole}-h}\mathcal T(PQ)
+
\frac{3^{L_{\rm pole}}}{4}\mathfrak f(Q_{\rm act}PQ)
\equiv
3^6C_{v_*}(P,Q)\pmod{3^7}.
}
\tag{14.4}
$$


The combined left side is integral by its exact finite-pole representation. No separate integrality of the two displayed summands is inferred if the factorial functional has denominators.

For raw inputs $F=3^{g_1}P$, $G=3^{g_2}Q$, this is equivalently


$$
\boxed{
3^{L_{\rm pole}-h-g_1-g_2}\mathcal T(FG)
+
\frac{3^{L_{\rm pole}}}{4}\mathfrak f(Q_{\rm act}PQ)
\equiv
3^6C_{v_*}(P,Q)\pmod{3^7}.
}
\tag{14.5}
$$



This is a target-specific complete-source relation after content removal. It is not the generic adjugate criterion.

Its limitation is equally explicit: the factorial term has **not** been evaluated or discarded. To deduce a valuation for the complete contraction, one must compare that retained term with the finite-pole residue. At higher precision, the lower poles of the necessary valuations return and must all be included.

---

## 15. Why this does not yet normalize both actual corrected columns

The actual equations remain


$$
\widehat Z^{\,\rm act}
=
\widehat Z^{\,c}-3^6WE_{\rm act}^{-1}T_R,
\tag{15.1}
$$




$$
S_{\rm act}-S_c
=
3^6K_Z-3^{12}T_R^TE_{\rm act}^{-1}T_R.
\tag{15.2}
$$



If the reference columns have a common factor $3^g$, division gives


$$
\boxed{
3^{-g}\widehat Z^{\,\rm act}
=
3^{-g}\widehat Z^{\,c}
-
3^{6-g}WE_{\rm act}^{-1}T_R.
}
\tag{15.3}
$$


This is the exact equation; it does not allow $T_R$ to be replaced by $3^g\widetilde T_R$ unless that divisibility is proved for the **complete actual source**.

Likewise,


$$
\boxed{
3^{-2g}(S_{\rm act}-S_c)
=
3^{6-2g}K_Z
-
3^{12-2g}T_R^TE_{\rm act}^{-1}T_R.
}
\tag{15.4}
$$



If the complete definitions prove


$$
T_R=3^g\widetilde T_R,\qquad
K_Z=3^{2g}\widetilde K_Z,
\tag{15.5}
$$


then the common content cancels from these equations as well. The polynomial-content theorem alone does not establish (15.5), because externally forced charges and terminal terms need not be homogeneous in the reference pair.

Let


$$
\iota_E=\max\{0,-\min_{a,b}v_3((E_{\rm act}^{-1})_{ab})\}.
$$


With integral $W$, a sufficient precision bill for the unscaled $T_R$ in (15.3), at normalized output precision $3^K$, is


$$
T_R\pmod{3^{\,g+K+\iota_E-6}},
\tag{15.6}
$$


when the exponent is positive. If the factorization (15.5) is proved first, the normalized source instead needs precision


$$
\widetilde T_R\pmod{3^{\,K+\iota_E-6}}.
\tag{15.7}
$$


Structured contractions can improve this worst-case bill, but an entrywise $3^6$ perturbation by itself cannot.

### Concrete follow-on lemma

The next complete-force target is therefore:

> **Normalized complete-source lemma.**  
> In the retained finite producer, express both columns of $T_R$, the quadratic term $K_Z$, and the terminal return in the full-content-normalized Jacobi/Christoffel coordinates. Prove the exact common factors in (15.5), or identify and evaluate the terms that prevent them. Then combine the whole factorial contraction with (14.4), at sufficient precision for the actual inverse transport.

This requires the actual factorial, pole, LOW, and terminal charges. It is not discharged by another statement that an adjugate exists.

---

# Part V. Finite boundaries and global arithmetic obligations

## 16. The finite producer and terminal return are unchanged

Retain


$$
0\le v\le2n-2,
$$




$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),
\qquad
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1.
\tag{16.1}
$$



The complete perturbation is still (13.1)–(13.2), with the original row range $0\le a,d\le m$. Neither the content module nor the density argument enlarges a matrix boundary.

The terminal return remains


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
\tag{16.2}
$$




$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{16.3}
$$


There is no moment beyond $D-4$, and $\omega_{\nu-1}$ is retained.

The new full polynomial contents are not automatically the contents of these actual finite rows.

---

## 17. Final gcd, actual denominator, and whole error

After the actual row contents, actual multiplier, and least actual clearer, retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**.

For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{17.1}
$$



The weighted producer likewise retains


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


and the whole same-index error


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{17.2}
$$



The density-one growth of selected-prime full content evaluates neither gcd. It supplies neither an actual primitive denominator estimate nor nonvanishing and decay of the whole error.

For an irrationality proof, a sufficient final outcome would be an infinite original sequence with integer primitive pairs and


$$
0<|q(e+\pi)-p|\longrightarrow0.
$$


No such whole-error theorem has been obtained here.

---

# Part VI. New bounded arithmetic and proof ledger

## 18. A genuinely new modest verification of the content module

No accepted modulo-$9$, modulo-$27$, discrete-log, or historical endpoint calculation should be repeated. The announced modulo-$81$ coefficient evaluation remains the coordinator’s separate new calculation, with its three-digit lookahead and ten paid ratio terms.

No finite computation is needed as a premise for the new proofs above.

A useful **different** bounded calculation would verify the new full-content and signed-minimum modules.

### Inputs

For


$$
m=221,\ldots,240,
$$


use both parameter pairs


$$
(s,n)=(m,3m-1),\qquad(s,n)=(m-1,3m-2).
$$


For each of the forty polynomials:

1. form the exact dyadic Bernstein coefficients in (7.1);
2. form the exact monomial polynomial using the unimodular basis;
3. run the eight-state module of §8;
4. run the sixteen-state signed enhancement of §9;
5. evaluate the exact finite endpoint sum.

### Expected verifiable output

For every case, record:

* the actual minimum Bernstein valuation;
* the minimum monomial-coefficient valuation;
* the min-plus answer;
* one minimizing $k$, with $0\le k\le s$;
* the signed-module residue;
* the exact endpoint divided by the reported full content, modulo $3$.

The required checks are


$$
\boxed{
r_{\rm Bernstein}=r_{\rm monomial}=r_{\rm module},
}
$$


and


$$
\boxed{
\text{signed output}
=
3^{-r_{\rm module}}J_s^{[A]}(-1)\pmod3.
}
$$


For the cases with $3\nmid m$, also verify


$$
r_+(m),r_-(m)\ge N_{20}(m).
$$



The certificate should retain the final addition, subtraction, generalized-comparison, and doubling carries. In particular, a zero signed sum must not be converted into “no minimum-cost path.”

This proposed computation concerns new full-coefficient normalization data. It has not been executed, and its output would establish only these forty finite comparisons.

---

## 19. Proof-status ledger

| Statement | Status |
|---|---|
| Turn17 fixed-tail divisibility, $\psi(H)$, and exact split language | Reused proved results |
| Announced modulo-$81$ evaluation | Pending; no output assumed |
| Extension of the leading-cylinder proof to prefix-counted languages | Derived in §2 |
| Numerical $0.9725$ constant from the primary proof | Not independently reverified here; not needed |
| Relative-density-one $c_m\ge4$ on the original fixed-tail exact window | **Proved** |
| Stronger $O(\log X\,X^{\log_3 2})$ exact-$c_m=3$ exception count | **Proved** |
| Every $20$-occurrence forces one digit of both full contents | **Proved** |
| Full content equals the minimum Bernstein valuation | **Proved by unimodularity** |
| Eight-state exact full-content module | **Proved** |
| Sixteen-state endpoint-at-full-content residue module | **Proved** |
| Closed formula depending only on the number of $20$-occurrences | Not asserted |
| Both full contents and endpoint content tend to infinity in density | **Proved**, with quantitative bound |
| Equality of endpoint and full common content at every original index | Not proved |
| Common-content cancellation in the homogeneous Christoffel source | **Proved on the stated integral scalar branch** |
| Complete bilinear force factorization and divided finite-pole congruence | **Derived**, with normalized integrality hypotheses explicit |
| Common factor in the complete inhomogeneous $T_R,K_Z$, terminal source | Outstanding |
| Scalar-root approach and actual inverse-transport control | Outstanding |
| All-prime final gcd, actual $q$, whole nonzero same-index error comparison | Outstanding |

---

## Conclusion

Three substantive targets are now advanced beyond turn17.

First, the higher-density conclusion should not be abandoned:


$$
\boxed{
c_m\ge4
\quad\text{with relative density one on the proved original-window AP}.
}
$$


The split-language extension of the classical leading-cylinder argument is valid. More strongly, the target’s exact trailing-digit parametrization gives the exception count


$$
\boxed{O(\log X\,X^{\log_3 2}).}
$$



Second, full polynomial content is now controlled globally from below:


$$
\boxed{
r_+(m),r_-(m)\ge N_{20}(m).
}
$$


Together with the exact finite residue parametrization, this proves that both full contents—and therefore common endpoint content—tend to infinity in density. It does not imply divergence at every index or choose a primitive endpoint line.

Third, actual full content is no longer left as an unevaluated search over all coefficients. It is given by an exact eight-state min-plus digit module, and the first endpoint residue after that normalization is given by a sixteen-state signed extension. The finite range, both binomial carry mechanisms, final carries, and dyadic units are preserved.

The remaining local bottleneck is now sharper:



$$
\boxed{
\begin{gathered}
\text{evaluate the primitive endpoint/scalar direction after the actual full content is removed,}\\
\text{and prove or evaluate the complete inhomogeneous source factorization and inverse transport.}
\end{gathered}
}
$$



Common deep content cancels from the homogeneous source and complete bilinear contraction, but it does not by itself normalize the externally forced corrected columns. The four-digit Christoffel inverse loss survives, and the actual finite inverse can impose a further loss.

After that local work, the global obligation remains the actual **all-prime** primitive denominator against the **whole nonzero same-index error** on an infinite original sequence.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


