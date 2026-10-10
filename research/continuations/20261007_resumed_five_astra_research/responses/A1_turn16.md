> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 Turn 16 — Separated interpolation, mixed exponential–period determinants, and the arithmetic obstruction

## Abstract

This report examines the complete supplied Family017 argument and tests a mixed construction under the temporary hypothesis


$$
e+\pi=r\in\mathbb Q.
$$


The two linked exponential evaluations are retained exactly:


$$
\omega=2\pi i=2i(r-e),\qquad \exp(\omega)=1,\qquad \exp(1)=e.
$$



The principal new result is a **quantitative obstruction to a direct transfer of the determinant argument**. It has three parts.

1. A valid mixed jet matrix can be constructed with entries in $\mathbb Q(i)[E]$, whose specialization at $E=e$ simultaneously uses the points $j\omega$ and $1+j\omega$. Under explicit strengthened interpolation hypotheses, it has a nonzero full-row minor. No algebraic-independence assumption is needed.

2. Its arithmetic normalization produces a polynomial
   

$$
F_N(E)\in\mathbb Z[i][E],
$$


   not a Gaussian integer after specialization at $E=e$. For $K\ge2$, every nonzero full-row minor in the construction has a forced polynomial factor arising from coalescence at $E=r$. Thus the missing arithmetic step is genuine, rather than merely a failure to choose a convenient clearer.

3. For a fixed nonconstant Gaussian-integer polynomial of degree $d\ge3$, replacing $e$ by increasingly accurate reduced rational approximants does not repair this step by ordinary rational clearing. Using the **actual least simultaneous clearer** of the evaluated real and imaginary parts, the cleared whole substitution error tends to infinity. The proof includes the exact denominator gcd and uses only the classical continued fraction of $e$.

These statements obstruct specified transfer procedures; they do **not** exclude every possible mixed determinant method. A family-uniform polynomial-value estimate, or a special exact polynomial cancellation with its full arithmetic cost, remains a concrete follow-on obligation.

The supplied Family017 proof is internally coherent under its stated standard geometric inputs. Its conclusion $\mu(\pi)=2$, even if accepted at that scope, does not imply irrationality of $e+\pi$. Indeed, under $e+\pi=r$, it is compatible with the classical equality $\mu(e)=2$.

For the original factorial-functional route, H2 is treated as accepted, as instructed. The turn14 nine-period theorem is not repeated or promoted beyond its separate audit status. The original boundary-column identity (8.2), the actual directional inverse bound, and the same-index all-prime primitive-denominator comparison remain open.

---

## 1. Scope, evidence, and proof status

### 1.1 Sources inspected here

The supplied complete Family017 mathematical files have all been considered:

- `main.tex`;
- `interpolation.tex`;
- `determinant.tex`;
- `conclusion.tex`;
- `series.tex`.

The complete supplied turn14 report and catalogue research-scope document have also been considered.

The primary mathematical proofs of Family005 and Family022, their bibliographies, and the remaining abstract shards are not included in this conversation. Accordingly:

- no claim is made here to have inspected those unavailable full proofs;
- no Family005 identity is imported into the factorial functional;
- no almost-everywhere conclusion from Family022 is applied to the fixed number $e+\pi$ or to the original sparse index families.

No tool was used and no computation was executed. The bounded calculation in §11 is an optional exact-arithmetic audit with specified inputs and outputs.

### 1.2 Distinctions maintained

The report separates:

- **proved statements:** the new mixed polynomial determinant identities, degree/height bounds, and rational-clearing obstruction;
- **conditional implications:** consequences of $e+\pi=r$, and consequences of prospective lower bounds for the mixed determinant polynomials;
- **finite checks:** the optional four-by-four polynomial calculation;
- **open obligations:** a successful mixed arithmetic comparison and the outstanding original-source arithmetic questions.

Nothing below proves either rationality or irrationality of $e+\pi$.

---

## 2. What the complete Family017 proof establishes at its stated scope

### 2.1 The center-uniform interpolation statement

For fixed


$$
m,K\ge1,\qquad w_0,v_0>0,\qquad 0<\theta<1,
$$


Family017 assumes


$$
K\theta^m<1,\qquad K\frac{w_0}{v_0}\theta^m<1.
$$


It then chooses $w_1,\ldots,w_m$ successively, before the centers are known.

With


$$
W=(w_0,w_1,\ldots,w_m),\qquad
V=(v_0,w_1/\theta,\ldots,w_m/\theta),
$$


the theorem gives surjectivity of


$$
P\longmapsto
\left(
P\bigl(1+t,c_{j1}+u_1+\log(1+t),\ldots,
c_{jm}+u_m+\log(1+t)\bigr)
\right)_{j<K}
$$


onto the packets


$$
v_0s+\sum_i\frac{w_i}{\theta}\beta_i<H.
$$



Its quantifiers matter:

- coordinatewise distinctness across $j$ is required;
- independence between different $X_i$-coordinates is not required;
- the weight-separation thresholds do not depend on the centers;
- the eventual degree threshold may depend on the centers;
- the theorem is over $\mathbb C$, not over $\mathbb Z$ or a number field.

In particular, it is an algebraic-rank theorem. It gives no arithmetic lower bound for the value of a determinant at transcendental centers.

### 2.2 Checks on the geometric proof

The principal geometric steps are compatible with their uses in the supplied argument.

**Local multiplicity.** The commuting frame gives transverse flow coordinates. Persistence of all derivatives below the weighted threshold forces containment in the corresponding monomial ideal. The isolated coordinate slice permits comparison with local complete-intersection length, and the weighted Bézout estimate is obtained through finite power substitutions. The uniformity in the equations and analytic frame is essential and is explicitly supplied.

**Separated normal bases.** The chosen inequalities between products of degree weights and derivative costs rule out a largest differing positive normal direction. The resulting differential identity


$$
dX_i=dY/Y
$$


forces $Y$ to be constant on an algebraic variety: restriction to a complete algebraic curve would otherwise equate an exact differential with a logarithmic differential having a nonzero residue.

**The fiber $Y=1$.** The second volume inequality is used separately. Coordinatewise distinctness then limits a persistent component with a constant coordinate to at most one center. The final zero–pole comparison uses


$$
\theta^{-1}>1+\sigma.
$$



**Passage to jets.** The proof uses an ordinary blowup of a finite-colength ideal. The displayed argument retains ordinary powers $I^n$, and invokes Proj recovery only for sufficiently large $n$. Its inclusion


$$
I^n\subseteq\{\text{weighted order at least }nR\}
$$


has the correct direction for obtaining the requested smaller jet quotient.

Thus no algebraic-independence assumption is hidden in the center-uniform theorem. Conversely, its complex-geometric nature does not supply one.

### 2.3 The determinant arithmetic is tied to rational centers

In Family017 the centers are


$$
c_{ji}=j\frac{2ip_i}{q_i}.
$$


After the stated column, row, and logarithmic-truncation clearings, a nonzero selected determinant becomes a Gaussian integer. This is exactly where


$$
|\text{nonzero Gaussian integer}|\ge1
$$


enters.

The analytic translation is then made to the exact periods $j\omega$. The discrepancy


$$
\frac{2ip_i}{q_i}-\omega
$$


provides the factors with exponent $\nu$. The proof keeps the truncation tails as well as those approximation errors.

The comparison therefore needs both:

1. rational centers for the integer lower bound;
2. approximations with a fixed exponent $\nu>2$ for the error saving.

Neither requirement can simply be replaced by the relation $e+\pi=r$.

### 2.4 The order of limits is valid and indispensable

The source fixes, in order:

1. $\nu>2$;
2. the dimension and auxiliary constants;
3. finitely many successively separated approximation denominators;
4. all centers and weights;
5. only then the polynomial degree $H\to\infty$.

The independence of the weight thresholds from the centers removes the stated circularity. It does not remove the need for the exceptionally accurate rational approximations.

The series arguments subsequently use only the resulting approximation bound and a standard spacing argument. They add no mixed information about $e+\pi$.

---

## 3. First obstruction: exponent two is compatible with the rationality hypothesis

Write the temporary rationality hypothesis as


$$
e+\pi=r=\frac{a_0}{b_0},
\qquad
a_0\in\mathbb Z,\quad b_0\ge1,\quad \gcd(a_0,b_0)=1.
$$


The subscript distinguishes this denominator from the original ternary parameter $b$.

For every rational $p/q$,


$$
\left|\pi-\frac pq\right|
=
\left|e-\frac{a_0q-b_0p}{b_0q}\right|.
$$


Rational translation and sign change preserve the irrationality exponent. Reduction of the displayed fraction can only decrease its denominator, and the fixed factor $b_0$ is absorbed when comparing strict exponents. Applying the inverse translation gives equality in both directions:


$$
\boxed{\mu(r-e)=\mu(e).}
$$



The classical continued fraction


$$
e=[2;1,2,1,1,4,1,1,6,1,\ldots]
$$


gives $\mu(e)=2$. Consequently,


$$
e+\pi=r\quad\Longrightarrow\quad \mu(\pi)=2.
$$



Thus the Family017 conclusion is compatible with, not contradictory to, the temporary rationality hypothesis.

There is also an explicit obstruction in the unchanged Family017 parameter budget. At exponent $\nu=2$, its approximation gap would require


$$
2(A-\theta)>1-\theta.
$$


Its parameter construction also requires $A^2<\theta$. But then


$$
2(A-\theta)-(1-\theta)
<
2\sqrt\theta-\theta-1
=
-(1-\sqrt\theta)^2<0.
$$


The two requirements cannot hold simultaneously.

This is a precise failure of the **unchanged exponent-two transfer**, not a general impossibility theorem for all mixed methods.

---

## 4. A genuine mixed jet matrix

A useful test should use both linked evaluations, not merely rename an approximation to $\pi$.

In this section $N$ is an auxiliary interpolation degree. It is unrelated to the original $H=3^{h-1}$.

Set


$$
\Omega(E)=2i\left(\frac{a_0}{b_0}-E\right).
$$


Under the rationality hypothesis,


$$
\Omega(e)=\omega.
$$



Take two sets of evaluation points:


$$
z_{j,k}=k+j\omega,
\qquad
0\le j<K,\quad k\in\{0,1\}.
$$


Their exponential values are exactly


$$
e^{z_{j,k}}=e^k.
$$



### 4.1 Exact entries

Choose fixed positive rational weights and a truncation parameter $F_0$, and put


$$
T_i=\left\lceil\frac{F_0w_i}{v_0}\right\rceil,
\qquad
G_i(t)=\sum_{1\le n<T_i}\frac{(-1)^{n+1}t^n}{n}.
$$


Assume $F_0>1/\theta$, so the omitted terms preserve the required weighted filtration.

Use columns


$$
P(Y,X)=Y^hX^\alpha,
\qquad
w_0h+w\alpha\le N,
$$


and rows


$$
(j,k,s,\beta),\qquad
v_0s+\frac{w\beta}{\theta}<N.
$$



The polynomial-parameter matrix has entries


$$
\begin{aligned}
\mathsf M_{(j,k,s,\beta),(h,\alpha)}(E)
={}&\binom{\alpha}{\beta}E^{kh}[t^s](1+t)^h\\
&\quad\cdot
\prod_{i=1}^m
\bigl(k+j\Omega(E)+G_i(t)\bigr)^{\alpha_i-\beta_i},
\end{aligned}
\tag{4.1}
$$


with entry zero unless $\alpha\ge\beta$.

At $E=e$, these are exactly the coefficients of


$$
P\bigl(e^k(1+t),
k+j\omega+G_1(t)+u_1,\ldots,
k+j\omega+G_m(t)+u_m\bigr).
$$


Thus both $\exp(\omega)=1$ and $\exp(1)=e$ are present.

### 4.2 A sufficient full-rank theorem

Family017 does not directly cover two different $Y$-fibers. The following elementary localization supplies a valid, though costly, extension.

Choose a rational number $\lambda$ such that


$$
\theta<\lambda<1,\qquad
\lambda+\frac{w_0}{v_0}<1,
\tag{4.2}
$$


and suppose


$$
K\left(\frac{\theta}{\lambda}\right)^m<1,
\qquad
K\frac{w_0}{\lambda v_0}
\left(\frac{\theta}{\lambda}\right)^m<1.
\tag{4.3}
$$


Choose the successive $w_i$ using Family017 with data


$$
w_0,\quad \lambda v_0,\quad \theta/\lambda.
$$



Then, under $e+\pi=r$, the specialization $\mathsf M(e)$ has full row rank for all sufficiently large, sufficiently divisible $N$.

#### Proof

Apply Family017 at degree $\lambda N$, with jet weights $\lambda V$. Its retained packet is exactly the desired packet because


$$
\lambda\left(v_0s+\frac{w\beta}{\theta}\right)<\lambda N
$$


is equivalent to the row inequality in (4.1).

Let


$$
S_N=\left\lceil N/v_0\right\rceil.
$$


To prescribe the first fiber and annihilate the second, multiply an interpolating polynomial by


$$
(Y-e)^{S_N}.
$$


At $Y=1+t$, this is a unit in the finite jet algebra because $e\ne1$. At $Y=e(1+t)$, it equals $e^{S_N}t^{S_N}$, which vanishes in every retained packet.

For the other fiber use $(Y-1)^{S_N}$, and apply the common-fiber theorem after replacing $Y$ by $Y/e$. This scaling does not change weighted degrees.

The degree cost is at most


$$
\lambda N+w_0S_N\le N
$$


for all sufficiently large $N$, by (4.2).

For each fiber the centers in every $X_i$-coordinate are


$$
k+j\omega.
$$


They are pairwise distinct because $\omega\ne0$. The filtered replacement of $\log(1+t)$ by $G_i(t)$ preserves surjectivity.

Therefore arbitrary packets on both fibers are realizable. ∎

This is an actual mixed nonvanishing construction. Its proof uses no algebraic independence.

---

## 5. Integerization produces a polynomial in $e$, not an integer

### 5.1 An explicit polynomial normalization

Put


$$
L_i=\operatorname{lcm}(1,\ldots,T_i-1),
\qquad
D_i=\operatorname{lcm}(b_0,L_i).
$$


These are sufficient polynomial coefficient clearers; they are not asserted to be the least clearers for every selected minor.

Scale a column $(h,\alpha)$ by $\prod_iD_i^{\alpha_i}$ and a row $(j,k,s,\beta)$ by $\prod_iD_i^{-\beta_i}$. The resulting entry is in $\mathbb Z[i][E]$.

Choose a nonzero full-row minor $\Delta_N(e)$, and denote its size by $M$. Then


$$
F_N(E)=C_N\Delta_N(E)\in\mathbb Z[i][E],
\tag{5.1}
$$


where


$$
C_N=\prod_iD_i^{\,\sum_{\rm columns}\alpha_i-\sum_{\rm rows}\beta_i}.
\tag{5.2}
$$


Each exponent in (5.2) is nonnegative: any nonzero determinant term matches rows and columns with $\alpha_i\ge\beta_i$, and summing gives the assertion.

The result is a nonzero polynomial evaluated at $e$. The inequality


$$
|F_N(e)|\ge1
$$


does not follow.

Indeed, if $F_N$ is nonconstant, then $F_N(e)$ is transcendental. Otherwise $e$ would satisfy the polynomial equation


$$
F_N(X)-F_N(e)=0
$$


over the algebraic numbers, contradicting the transcendence of $e$.

### 5.2 Every full-row minor has a forced coalescence factor

Let


$$
R_N=\#\left\{(s,\beta):
v_0s+\frac{w\beta}{\theta}<N\right\},
\qquad M=2KR_N.
$$


For fixed $k,s,\beta$, a row can be expanded in the center displacement:


$$
\mathsf R_j(E)=
\sum_{d\ge0}\bigl(j\Omega(E)\bigr)^d
\mathsf V_{d,k,s,\beta}(E).
$$


Inside the group of $K$ rows indexed by $j$, repeated degrees $d$ make the corresponding determinant term vanish. Every nonzero term therefore has total displacement degree at least


$$
0+1+\cdots+(K-1)=\frac{K(K-1)}2.
$$


There are $2R_N$ groups. Hence


$$
\boxed{
(b_0E-a_0)^{R_NK(K-1)}
\mid F_N(E)
}
\tag{5.3}
$$


in $\mathbb Z[i][E]$.

The divisibility first holds over $\mathbb Q(i)$; it holds over $\mathbb Z[i]$ by Gauss’s lemma because $b_0E-a_0$ is primitive.

In particular, for $K\ge2$,


$$
\deg F_N\ge R_NK(K-1)=\frac{M(K-1)}2.
\tag{5.4}
$$



This proves that the polynomial obstruction affects every nonzero full-row minor of this construction. It is not removed by choosing a different minor.

One may try to divide out the known factor (5.3). That is a legitimate proposed modification only if its full value and analytic cost are retained:


$$
|b_0e-a_0|=b_0\pi.
$$


It does not authorize treating the remaining polynomial value as an integer. A quotient could exceptionally be constant, but that would require an exact polynomial identity, not a rank argument.

### 5.3 Degree and height payments

A degree bound is


$$
\deg F_N
\le
\sum_{\rm columns}(h+|\alpha|)
-\sum_{\rm rows}|\beta|
\le
\frac{MN}{\min(w_0,w_*)}.
\tag{5.5}
$$



For an explicit coefficient bound, define


$$
B_i=
D_i\left(
1+2(K-1)(|r|+1)+\sum_{1\le n<T_i}\frac1n
\right),
$$


and


$$
\Gamma=
\max\left\{
\frac{\log2}{w_0},
\max_i\frac{\log(2B_i)}{w_i}
\right\}.
$$


Writing $\|F\|_1$ for the sum of the moduli of its Gaussian coefficients, coefficient extraction and determinant expansion give


$$
\boxed{
\|F_N\|_1\le M!\exp(MN\Gamma).
}
\tag{5.6}
$$



Thus the outstanding arithmetic object has degree of order at most $MN$ and logarithmic height of order at most $MN$. A lower bound for its value at $e$ must be proved at these growing parameters.

---

## 6. The accompanying analytic estimate, and the cost of the valid rank extension

The exact linked points eliminate the rational-approximation errors, but not the truncation tails.

Put


$$
\tau_i(t)=G_i(t)-\log(1+t).
$$


At $E=e$, the row translation uses


$$
z=k+j\omega+\log(1+t)
$$


and


$$
X_i=z+u_i+\tau_i(t).
$$


There is no $\epsilon_i$-term.

A nonzero term with transverse index $a\ge\beta$ requires


$$
\sum_i(a_i-\beta_i)T_i\le s.
$$


Consequently,


$$
w(a-\beta)<\frac N{F_0},
\qquad
wa<\left(\theta+\frac1{F_0}\right)N.
\tag{6.1}
$$


Choose $F_0$ also so that


$$
A_0:=\theta+\frac1{F_0}<1.
$$



The same entire functions as in Family017 occur:


$$
f_{a,P}(z)=[u^a]P(e^z,z+u_1,\ldots,z+u_m).
$$


Take


$$
R=100(K+1).
$$


All the test disks lie inside $|z|<R/2$. Repeating the source collision argument, now with all translated indices satisfying (6.1), gives


$$
\frac{\log|\Delta_N(e)|}{MN}
\le
-c\mathcal L+
E_{\rm mix}+o(1),
\tag{6.2}
$$


where


$$
c=\frac{\log2}{4},
\qquad
\mathcal L=
\frac{2K\theta^m}{(m+1)v_0A_0^m},
\tag{6.3}
$$


and a valid error bound is


$$
E_{\rm mix}
=
\frac{R}{w_0}
+\frac{\log(2R)+\log4}{w_*}
+\frac{2\log2}{v_0}.
\tag{6.4}
$$



The derivation uses:

- Cauchy’s bound $2^s$ on the tail coefficients;
- the binomial bound $4^{|a|}$;
- the same repeated-Taylor-degree cancellation as Family017;
- Cauchy–Schwarz over the indices $wa\le A_0N$;
- only polynomially many choices per row, whose normalized logarithm tends to zero.

These are genuine analytic estimates, but this particular rank extension does not make them competitive. Since $A_0>\theta$,


$$
\mathcal L<\frac{2K}{(m+1)v_0}.
$$


The localization condition (4.2) implies $w_0/v_0<1$, so


$$
\frac{c\mathcal L}{R/w_0}
<
\frac{2c}{100(m+1)}
\frac{K}{K+1}\frac{w_0}{v_0}
<1.
\tag{6.5}
$$


Thus the displayed uniform collision saving is smaller than the first positive term in the analytic error bound.

This is a second, quantitative limitation of the construction:

> The elementary two-fiber localization proves mixed rank, but its weight cost prevents the displayed uniform collision estimate from certifying exponential decay.

A sharper mixed interpolation theorem could avoid this localization cost. Even then, the polynomial-in-$e$ arithmetic obstruction of §5 would remain.

---

## 7. A new exact denominator and whole-error obstruction

The following result addresses the actual rational clearing, including its final gcd. It is independent of the original ternary route.

### 7.1 Exact evaluated denominator

Let


$$
F(X)=\sum_{j=0}^d c_jX^j\in\mathbb Z[i][X],
\qquad c_d\ne0,
$$


and let $p/q$ be reduced, with $q>0$. Define the Gaussian integer


$$
A_F(p,q)=\sum_{j=0}^d c_jp^jq^{d-j}.
$$


Then


$$
F(p/q)=\frac{A_F(p,q)}{q^d}.
$$



The **least positive integer simultaneously clearing the real and imaginary parts** is exactly


$$
\boxed{
\mathfrak c_F(p,q)=
\frac{q^d}
{\gcd\bigl(q^d,\Re A_F(p,q),\Im A_F(p,q)\bigr)}.
}
\tag{7.1}
$$


This is the actual clearer, not the convenient upper bound $q^d$.

Put


$$
\gamma=\gcd(|\Re c_d|,|\Im c_d|)>0.
$$


Then


$$
\boxed{
\gcd\bigl(q^d,\Re A_F,\Im A_F\bigr)\mid\gamma^d,
\qquad
\mathfrak c_F(p,q)\ge\frac{q^d}{\gamma^d}.
}
\tag{7.2}
$$



#### Proof of (7.2)

Fix a prime $\ell\mid q$, and write


$$
t=v_\ell(q),\qquad u=v_\ell(\gamma).
$$


Because $\ell\nmid p$, if $t>u$, at least one component of $c_dp^d$ has valuation exactly $u$, while every other term in $A_F$ has both components divisible by $\ell^t$. The common valuation of the two components of $A_F$ is therefore $u$.

If $t\le u$, the exponent contributed by the gcd in (7.1) is at most


$$
dt\le du.
$$


In either case it is at most $du$. This holds for every prime. ∎

For fixed $F$, ordinary evaluation denominators therefore retain the full exponent $d$, up to a constant depending on the leading coefficient.

### 7.2 A quantitative approximation bound for $e$

The classical continued fraction of $e$ gives, for some explicit absolute $c_e>0$,


$$
\boxed{
\left|e-\frac pq\right|
\ge
\frac{c_e}{q^2\log q}
\qquad(q\ge2).
}
\tag{7.3}
$$



For completeness, one may take $c_e=(\log2)/10$ with a harmless adjustment for any small initial convergents. If a reduced fraction is not a convergent, Legendre’s criterion gives error at least $1/(2q^2)$. For a convergent $p_n/q_n$,


$$
\left|e-\frac{p_n}{q_n}\right|
>
\frac1{(a_{n+1}+2)q_n^2}.
$$


The explicit partial quotients satisfy $a_{n+1}\le2(n+1)$, while


$$
q_n\ge2^{(n-1)/2}.
$$


Hence $a_{n+1}+2\le10\log_2q_n$ for $q_n\ge2$, giving (7.3).

### 7.3 Whole-error theorem

**Theorem 7.1.**  
Let $F\in\mathbb Z[i][X]$ be fixed and nonconstant, of degree $d\ge3$. For any sequence of reduced rationals $p/q\to e$,


$$
\boxed{
\mathfrak c_F(p,q)\,
\left|F(e)-F(p/q)\right|
\longrightarrow+\infty.
}
\tag{7.4}
$$



#### Proof

Since $F'$ is a nonzero polynomial with algebraic coefficients and $e$ is transcendental,


$$
F'(e)\ne0.
$$


Differentiability along the real line gives, for $x$ sufficiently close to $e$,


$$
|F(e)-F(x)|
\ge\frac{|F'(e)|}{2}|e-x|.
\tag{7.5}
$$


This also follows directly from Taylor’s formula: on $[0,3]$,


$$
|F''(x)|\le d(d-1)3^{d-2}\|F\|_1,
$$


so the quadratic remainder is at most half the linear term once $x$ is sufficiently close.

Combining (7.2), (7.3), and (7.5),


$$
\mathfrak c_F(p,q)|F(e)-F(p/q)|
\ge
\frac{c_e|F'(e)|}{2\gamma^d}
\frac{q^{d-2}}{\log q}.
$$


The right side tends to infinity for $d\ge3$. ∎

This theorem concerns the **whole evaluated polynomial difference**. It does not infer failure merely from an overlarge Lipschitz upper bound.

Its precise scope is important:

- it proves failure of increasingly fine rational replacement for each fixed polynomial of degree at least three;
- it uses the actual evaluated clearer (7.1), with all prime cancellations included;
- it does not rule out a diagonal family $F_N,p_N/q_N$ with specially correlated coefficients and small derivatives;
- such a family would require explicit, uniform control of that correlation.

That last requirement is exactly the missing new mathematics, not something supplied by center-uniform interpolation.

---

## 8. A fully evaluated mixed example

The arithmetic obstruction is visible in a four-by-four determinant.

Use the points


$$
0,\quad \omega,\quad 1,\quad1+\omega
$$


and columns


$$
1,\quad Y,\quad X,\quad YX.
$$


Put $w=\Omega(E)$. The matrix is


$$
\mathsf A(E)=
\begin{pmatrix}
1&1&0&0\\
1&1&w&w\\
1&E&1&E\\
1&E&1+w&E(1+w)
\end{pmatrix}.
$$


Subtract the first row from the second and third, and the third original row from the fourth. Direct expansion gives


$$
\det\mathsf A(E)=-(E-1)^2w^2,
$$


hence


$$
\boxed{
\det\mathsf A(E)
=
\frac4{b_0^2}(E-1)^2(a_0-b_0E)^2.
}
\tag{8.1}
$$



Let


$$
g_2=\gcd(b_0,2),\qquad B=b_0/g_2.
$$


The least simultaneous integer clearer of the polynomial entries is exactly $B$. The $X$ and $YX$ columns individually require $B$, and their cleared coefficient contents are one. The other two columns already have content one.

Clearing just those two columns gives determinant


$$
\frac4{g_2^2}(E-1)^2(a_0-b_0E)^2.
$$


Its coefficient content is exactly $4/g_2^2$, since


$$
\boxed{
F(E)=(E-1)^2(a_0-b_0E)^2
}
\tag{8.2}
$$


is primitive.

Under $e+\pi=r$,


$$
F(e)=(e-1)^2b_0^2\pi^2\ne0.
$$


It is not an integer, and no rational scalar clearing makes it one.

For a reduced $p/q$,


$$
F(p/q)=\frac{(p-q)^2(a_0q-b_0p)^2}{q^4},
$$


so its actual denominator is


$$
\boxed{
\frac{q^4}
{\gcd\bigl(q^4,(a_0q-b_0p)^2\bigr)}.
}
\tag{8.3}
$$


The factor $p-q$ contributes no gcd with $q$. In particular, the denominator is at least $q^4/b_0^4$. Theorem 7.1 applies.

This is an exact mixed determinant using both linked points. Its failure is not a nonvanishing problem: its determinant has been evaluated. The failure is the absent small integer quantity.

---

## 9. Concrete follow-on lemmas

The preceding results leave two specific mixed obligations.

### 9.1 Mixed interpolation without the localization loss

A useful replacement for §4.2 would prove two-fiber jet surjectivity at the original weighted degree budget, with hypotheses that do not impose the masking cost


$$
w_0N/v_0.
$$


It must apply to the actual points


$$
(e^k,k+j\omega,\ldots,k+j\omega),
\qquad k=0,1,
$$


and retain center-independent weight thresholds.

The present report does not prove such a theorem. The bound (6.5) explains quantitatively why the elementary masking extension is insufficient for the displayed collision estimate.

### 9.2 A family-uniform polynomial-value bound

Suppose a refined construction yields, after all specified polynomial coefficient contents and clearings,


$$
F_N\in\mathbb Z[i][E]\setminus\{0\},
$$


and proves


$$
\log|F_N(e)|\le-\sigma MN+o(MN).
$$


To obtain a contradiction one would need a compatible lower bound such as


$$
\boxed{
\log|F_N(e)|\ge-\tau MN+o(MN),
\qquad \tau<\sigma,
}
\tag{9.1}
$$


for the **actual selected polynomials**, after any exact forced-factor removal.

The degree and height inputs are explicitly bounded in (5.5)–(5.6). An assertion that $F_N(e)\ne0$ is not enough. Nor is an unspecified transcendence measure: its dependence on degree, height, and selected factors must fit (9.1).

An alternative is an exact determinant identity showing that the normalized polynomial quotient is constant. That identity would have to be proved and its complete factor payment inserted into the analytic estimate.

These are concrete follow-on lemmas. They do not assume Schanuel’s conjecture or any algebraic independence of $e$ and $\pi$.

---

## 10. Comparison with the unchanged factorial-functional route

The mixed obstruction above is a material result, so no unsupported evaluation of the original boundary column is substituted for it. The original local arithmetic problem remains separate.

### 10.1 Original domain and finite boundaries

Retain exactly


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


with


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



The finite coordinates remain


$$
U_u=(y-1)^u\quad(0\le u<D),
$$




$$
z_i=(y-1)^Dy^i\quad(0\le i<\nu),
\qquad \nu=D/2-1,
$$




$$
Y_a=y^a\quad(d\le a\le m),
\qquad d=D+\nu.
$$


The physical terminal is still $Y_m$.

On the turn14 interior subwindow,


$$
\frac{103}{1000}<\rho=\frac{N_0}{P_0}<\frac{104}{1000},
$$


retain


$$
P_0=243P=3^{h-27},\quad N_0=243r_{\rm idx},\quad D=P_0+N_0,
$$




$$
P=3^{h-32},\quad r_{\rm idx}\equiv2\pmod9,\quad r_{\rm idx}\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r_{\rm idx}+1.
$$


Here $r_{\rm idx}$ is the source’s original integer parameter, not the temporary rational value $r=e+\pi$.

The accepted original-index infinitude is reused only on this stated original subfamily.

### 10.2 Complete functional, source, and corrections

The functional remains


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!,
\tag{10.1}
$$


on degrees at most $2n-1$. Its largest pole denominator is $4n-3$.

The sources are unchanged:


$$
Q_c=(y+1)(y-1)^A(\beta+3y),\qquad \beta=-71-A,
$$




$$
Q_{\rm act}=Q_c+3^7\mathscr R,
$$




$$
3^7\mathscr R=\sum_{a=0}^{A+1}e_a(y-1)^a,
\qquad
e_a=-\frac{(A+1)!}{a!}(t_a+\xi v_a).
$$


The complete force is


$$
t=3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
\qquad b_{\rm force}=-n-66.
$$


The signed scalar $\xi$ retains its already paid common division.

The endpoint charge and finite return remain


$$
\mathscr R(-1)=-\frac{\xi((A+1)!)^2}{3^7},
$$




$$
J^T\varepsilon+\omega_{\rm ret}
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


The notation $\omega_{\rm ret}$ here denotes the source’s return vector, not the complex period.

The exact corrected columns are still


$$
F=Z-WE_c^{-1}C_c,\qquad G_c(W,F)=0.
$$


They are not replaced by arbitrary columns sharing a leading reduction.

The complete moment recurrence is retained:


$$
\mu_0=-3^h/4,
$$




$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\quad 0\le t\le2n-2.
$$


Thus the factorial component, initial charge, and every pole in the original finite range remain present.

### 10.3 H2 and the boundary column

H2 is **accepted** in this report. The old pending label in turn14 is not retained.

The turn14 nine-period theorem remains under its separate referee audit. It is neither repeated nor used here as an independently accepted asymptotic gain.

For the actual finite blocks, retain


$$
Q=P_0/9,\quad b=Q-N_0,\quad
\ell=3b/2+1,
$$




$$
R_*=(P_0+1)/2,\quad
\tau=(N_0-3)/2,\quad
n_J=(Q-4b-5)/2,
$$




$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\}.
$$



H2’s identification of the $K\times K$ operator does not, by itself, prove the adjoining boundary-column identity


$$
(\bar L_ce_0)_u
=
[y^{E-\ell-u}](1-y)^{-b},
\qquad
E=(Q-3)/2.
\tag{10.2}
$$


That remains an original-object assertion requiring the complete moment calculation and actual prefix correction.

If (10.2) is proved, its contraction with the actual columns


$$
g_a=(y-1)^by^a,\qquad 0\le a\le b/2,
$$


is indeed zero:


$$
[y^{E-\ell}](1-y)^{-b}g_a
=[y^{E-\ell}]y^a=0,
$$


because $b$ is even and


$$
E-\ell=n_J+b/2>b/2\ge a.
$$


This implication is elementary and rigorous. The identification (10.2) is still open.

### 10.4 All Schur returns remain

The finite reductions retain


$$
\mathcal S^{(2)}_\alpha
=
\mathcal R_{\alpha,KK}
-27L_\alpha B_\alpha^{-1}L_\alpha^T,
$$




$$
f^{(2)}_\alpha
=
f_{\alpha,K}-3L_\alpha B_\alpha^{-1}f_{\alpha,J},
$$




$$
\lambda^{(2)}_\alpha
=
\lambda_\alpha-\frac13
f_{\alpha,J}^TB_\alpha^{-1}f_{\alpha,J}.
$$


No matrix cancellation removes the endpoint or diagonal returns.

Likewise, the following payments are unchanged:

- the producer division by $3^7$;
- the previously paid normalization of $\xi$;
- the $3^{-1}$ original LOW/HIGH inverse cost;
- the unit-prefix inverse;
- the $3^{-1}B^{-1}$ finite $J$-block inverse;
- the $3^{-2}$ rank-$b$ elimination under accepted H2;
- the actual $3^h$-resonant recurrence division identified in turn14.

No inverse of the final $C$-block is assumed paid.

### 10.5 The actual local and global bottlenecks

Under H2, the outstanding directional statement remains


$$
C^{-1}z\in3^{-1}\mathbb Z_3^{b/2},
$$


with $C$ nonsingular, for the actual endpoint-adapted complete matrix


$$
T=\begin{pmatrix}a&z^T\\z&C\end{pmatrix}.
$$


The relative pair


$$
D_0=\det T,\qquad D_1=\det C-\lambda\det T
$$


retains the complete diagonal $\lambda$.

Neither a growing common radical nor a fixed extra digit proves this directional assertion or its required asymptotic primitive consequence.

The final arithmetic normalization is also unchanged. With the actual contents already incorporated and $\ell_{\rm clr}$ the actual least simultaneous clearer, retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{10.3}
$$



An irrationality proof still needs, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty.
}
\tag{10.4}
$$


No mixed auxiliary calculation in this report changes these actual contents, clearer, gcd, primitive denominator, or whole error.

---

## 11. Bounded exact-arithmetic audit

No new dense original computation is requested. The closed precision computations and the separately audited nine-period calculation need not be repeated.

An optional audit of the new mixed normalization has the following bounded inputs.

### Inputs

Take the auxiliary rational value


$$
r=17/3,
\qquad
w(E)=2i(17/3-E),
$$


and the four-by-four matrix in §8.

### Expected verifiable outputs

Define


$$
F(E)=(E-1)^2(17-3E)^2.
$$


Its exact expansion is


$$
\boxed{
F(E)=9E^4-120E^3+502E^2-680E+289.
}
$$



The expected outputs are:

1. **Uncleared determinant**
   

$$
\det\mathsf A(E)=\frac49F(E).
$$



2. **Least simultaneous polynomial-entry clearer**
   

$$
\ell_{\rm aux}=3.
$$



3. **Column clearing**
   
   Multiplying the $X$ and $YX$ columns by $3$ gives primitive cleared columns and determinant
   

$$
4F(E).
$$


   Its coefficient content is $4$, and its primitive polynomial is $F$.

4. **Uniform entry clearing**
   
   Multiplying every entry by $3$ gives determinant
   

$$
36F(E),
$$


   with coefficient content $36$.

5. **Actual evaluated denominator**
   
   At the reduced rational $19/7$,
   

$$
F(19/7)=\frac{553536}{2401},
   \qquad
   \gcd(553536,2401)=1.
$$


   Thus the actual denominator is $7^4=2401$.

This finite audit checks the determinant signs, coefficient content, and actual rational denominator. It says nothing about the original index family or the truth of $e+\pi=17/3$.

---

## 12. Conclusion and proof-status ledger

| Statement | Status |
|---|---|
| Complete supplied Family017 proof internally coherent under its stated standard inputs | Checked at that scope |
| $\mu(\pi)=2$ alone implies irrationality of $e+\pi$ | False implication |
| Under $e+\pi=r$, the exact relations $\omega=2i(r-e)$, $e^\omega=1$, $e^1=e$ | Retained |
| Explicit mixed polynomial jet entries | Constructed |
| Mixed full-row rank under (4.2)–(4.3) | Proved |
| Integerization into $\mathbb Z[i][E]$ | Proved |
| Forced coalescence factor for every full-row minor | Proved |
| Degree and coefficient-height payments | Explicitly bounded |
| Displayed masked-construction collision estimate is competitive | It is not; obstruction (6.5) proved |
| Fixed-polynomial rational clearing, using the actual denominator, makes the whole substitution error small for degree $d\ge3$ | Disproved by Theorem 7.1 |
| Family-uniform mixed polynomial-value lower bound | Open |
| H2 original precision29 identification | Accepted |
| Turn14 nine-period theorem | Separate audit; not repeated |
| Actual boundary identity (10.2) | Open |
| Actual directional bound $C^{-1}z\in3^{-1}\mathbb Z_3^{b/2}$ | Open |
| Same-index all-prime gcd versus nonzero whole error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### New result

The new mathematical advance is a precise mixed-transfer obstruction, not merely a request to generalize interpolation:

- the linked-point matrix and its integer polynomial normalization are explicit;
- its nonvanishing can be proved without algebraic independence;
- every full-row minor has a quantified forced polynomial factor;
- its polynomial degree and height are bounded;
- ordinary rational replacement of $e$ incurs an actual denominator payment that, for a fixed polynomial of degree at least three, makes the cleared **whole** substitution error diverge.

### Exact remaining bottleneck

A successful mixed route must supply both:

1. mixed jet generation and analytic decay without the demonstrated localization loss;
2. an arithmetic lower bound for the actual growing-degree determinant polynomial at $e$, or an exact constant-quotient identity with all factors paid.

The original factorial-functional route still requires an evaluated actual-source directional or relative-determinant theorem, followed by the all-prime primitive-denominator comparison against the nonzero complete error at the same infinite original indices.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


