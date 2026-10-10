> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 5 — Corrected adjacent normalization, a seven-row collision certificate, and an exact arbitrary-middle obstruction

## Executive conclusion

The coordinator’s normalization correction is necessary. With the displayed Jacobi normalization,


$$
\boxed{\frac{d_i}{c_i}=-\frac{6(m-i)}{6m+2i-3}.}
$$


The factor $2$ missing in Turn 4 affects $R_i$, $S_i$, every subsequently evaluated collision minor, and every residue certificate based on those expressions. I withdraw those dependent numerical or residue conclusions. The quotient-free multiplication identity itself remains valid.

This report makes two further advances.

1. **The corrected collision problem has an exact certificate involving at most seven coefficient rows.** Five interior indices can be selected using a weighted Vandermonde minimization that is independent of the Christoffel scalar. Those five rows, together with the two genuine polynomial boundary rows, generate all collision minors over $\mathbb Z_3$. The proof retains every rational denominator and the actual
   

$$
a_m=\frac{p_{m+1}(r_0)}{p_m(r_0)}.
$$


   Selecting the five indices uniformly at low cost remains a separate problem; the result does not silently convert a large search into a small computation.

2. **A universal favorable lower bound based only on the resonance suffix and real-window digits is impossible.** There are explicit arbitrary-middle integers satisfying the exact real window, arbitrarily deep exact resonance, and the original parity requirement, for which
   

$$
r=u=0.
$$


   Their two digit evaluators have explicit zero-cost paths, with exact boundary states given below. They are not asserted to be powers of two. Thus they disprove a universal arbitrary-middle argument for
   

$$
2\min(r,4+u)\ge h-33,
$$


   but do **not** disprove that inequality for the original powers, and do **not** settle the opposite uniform inequality sought for inverse-transfer exclusion.

The effective real two-logarithm input introduced in Turn 4 remains explicitly source-dependent. I have not visually checked the theorem page of Matveev’s 2000 paper at the supplied primary link.

No unconditional proof or disproof of irrationality of $e+\pi$ follows.

---

## 1. Scope, accepted computations, and the logarithm dependency

Retain the original indices and definitions:


$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad A=2m-1=4^j-1,
$$




$$
H=3^{h-1},\qquad D=H-A,\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$


Write $L=h-1$.

The supplied computations are accepted at their stated finite scopes:

- 115 exact coefficient checks support the **corrected** adjacent ratio and the unchanged $c_i$ recurrence;
- 320 bounded full-content comparisons corroborate the digit evaluators;
- the eleven genuine power inputs have the reported $(r,u)$ values, all with $r=u$, but none has certified real-window eligibility.

None needs repetition. In particular, those eleven inputs neither evaluate the original-window inverse loss nor establish a uniform relation $r=u$.

### 1.1 What is elementary and closed

LTE proves


$$
t=v_3(4^{j+1}-247)\ge6
\quad\Longrightarrow\quad
j\equiv81\pmod{243}.
$$


The window guarantees **25**, not 26, leading ternary ones in $m$.

### 1.2 What remains dependent on the real-logarithm source

Turn 4 used


$$
\|q\log_3 4\|\ge c q^{-K}\qquad(q\ge1)
\tag{1.1}
$$


with effective $c,K>0$.

The precise missing source check is a theorem giving a polynomial lower bound for the nonzero real linear form


$$
q\log4-p\log3,
$$


with integer $q\ge1$ and $p$ the nearest integer to $q\log_3 4$. Nonvanishing follows from unique prime factorization. A suitable effective logarithmic-form theorem would give (1.1), after division by $\log3$ and adjustment of finitely many small $q$.

Conditional on (1.1), the rotation argument in Turn 4 is sound: for a fixed small interval, a Dirichlet step of size $\delta$, together with the lower bound on $\delta$, gives a hitting index polynomial in $3^t$, hence


$$
\log(j+1)=O(t).
$$


This is enough for the already established moving-base tail argument at its stated scope.

However, the supplied primary identification
<https://www.mathnet.ru/eng/im314>
is not a substitute for checking the theorem statement and its hypotheses. I therefore label the **new exact-window quantitative intersection argument conditional on (1.1)** pending that review. This does not reopen the separately accepted Bugeaud–Laurent application.

---

## 2. Repair of the adjacent coefficient derivation

Use exactly


$$
J_s(X)=
\sum_{k=0}^s
\binom{s+A}{k}\binom{s-\tfrac12}{s-k}
X^k(X-1)^{s-k},
\qquad A=2m-1.
$$


Write


$$
J_m=\sum_{i=0}^m c_iX^i,\qquad
J_{m-1}=\sum_{i=0}^{m-1}d_iX^i,\qquad d_m=0.
$$



The unchanged recurrence is


$$
\frac{c_i}{c_{i-1}}
=
-\frac{(m+1-i)(6m+2i-3)}{i(2i-1)}.
\tag{2.1}
$$



At zero,


$$
\frac{d_0}{c_0}
=
-\frac{\binom{m-\frac32}{m-1}}
        {\binom{m-\frac12}{m}}
=
-\frac{2m}{2m-1}.
\tag{2.2}
$$


The ratio of the remaining hypergeometric factors is


$$
\frac{m-i}{m}\,
\frac{3m-\frac32}{3m+i-\frac32}.
$$


Consequently


$$
\begin{aligned}
\frac{d_i}{c_i}
&=
-\frac{2m}{2m-1}\,
\frac{m-i}{m}\,
\frac{6m-3}{6m+2i-3}\\
&=
\boxed{-\frac{6(m-i)}{6m+2i-3}}.
\end{aligned}
\tag{2.3}
$$


This includes $i=m$. At $m=2,i=0$, it gives $-4/3$, as independently verified.

The error in Turn 4 was in the final simplification of this very derivation; its own displayed constant term already contradicted the claimed answer.

---

## 3. Fully corrected quotient-free formulas

Keep the actual parameters


$$
b=b_m=
\frac{3(2A^2+4A+1)}{(4A+1)(4A+5)},
$$




$$
\rho=\frac{A(3A+1)}{(4A+1)(4A+3)},
\qquad
a=a_m=\frac{p_{m+1}(r_0)}{p_m(r_0)},
$$




$$
r_0=\frac{A+71}{3},\qquad
\eta=A+71,\qquad \mathfrak a=\frac a3.
$$


In particular, neither $a$ nor $\mathfrak a$ is replaced by a residue-class representative.

Define


$$
\mathscr L(X)=3X-\eta,
$$




$$
F=(X-b-a)J_m-\rho J_{m-1}=\mathscr L Z,
$$




$$
V=\mathscr L J_m,\qquad
\mathcal T=XF+\mathfrak a V.
$$


Then the structurally valid identity is


$$
\boxed{
(X-Y)\mathscr L(X)\mathscr L(Y)\mathcal E(X,Y)
=
\mathcal T(X)F(Y)-F(X)\mathcal T(Y).
}
\tag{3.1}
$$


On the original resonant family, $\mathscr L$ has content zero. Hence


$$
\boxed{
\operatorname{cont}_3(\mathcal E)
=
\min_{i<k}v_3(\tau_i f_k-f_i\tau_k),
}
\tag{3.2}
$$


where $f_i=[X^i]F$, $\tau_i=[X^i]\mathcal T$.

Put


$$
B_i=6m+2i-3,\qquad
E_i=(m+1-i)B_i,\qquad
q_i=-i(2i-1).
$$


For $0\le i\le m$,


$$
Q_i=\frac{q_i}{E_i},\qquad Q_0=0.
$$


The repaired expressions are


$$
\boxed{
R_i=
Q_i-(b+a)+\frac{6\rho(m-i)}{B_i},
}
\tag{3.3}
$$




$$
\boxed{
S_i=Q_iR_{i-1}+\mathfrak a(3Q_i-\eta).
}
\tag{3.4}
$$


At $i=0$, the first term in (3.4) is zero. Thus


$$
f_i=c_iR_i,\qquad \tau_i=c_iS_i,
\tag{3.5}
$$


and every interior minor is now


$$
\boxed{
c_ic_k(S_iR_k-R_iS_k).
}
\tag{3.6}
$$



The two boundary rows remain


$$
\begin{array}{c|cc}
i&f_i&\tau_i\\ \hline
m+1&c_m&c_m(R_m+3\mathfrak a)\\
m+2&0&c_m.
\end{array}
\tag{3.7}
$$


These are polynomial boundary coefficients, not additional original matrix rows.

### 3.1 Explicit denominator clearing

Define the degree-at-most-two polynomial in $i$


$$
H_i=q_i-(b+a)E_i+6\rho(m-i)(m+1-i).
$$


Then $R_i=H_i/E_i$. Set


$$
W_i=E_iE_{i-1},\qquad w_i=\frac{c_i}{W_i},
$$


and


$$
U_i=H_iE_{i-1},
$$




$$
V_i=q_iH_{i-1}
+\mathfrak a(3q_i-\eta E_i)E_{i-1}.
$$


Both $U_i,V_i$ have degree at most four in $i$, and


$$
\boxed{(f_i,\tau_i)=w_i(U_i,V_i).}
\tag{3.8}
$$


For $m\ge4$, all displayed $E_i,E_{i-1}$ are nonzero on $0\le i\le m$.

To work over $\mathbb Z_3$, choose an **actual** common denominator $\Delta$ of all coefficients of $U,V$, including the denominators of $b,\rho,a,a/3$. Put


$$
\widetilde U=\Delta U,\qquad \widetilde V=\Delta V.
$$


Then the exact interior minor is


$$
\frac{w_iw_k}{\Delta^2}
\bigl(\widetilde V(i)\widetilde U(k)
-\widetilde U(i)\widetilde V(k)\bigr).
\tag{3.9}
$$


No denominator has been declared a unit, and no common factor has been discarded.

---

## 4. New theorem: seven rows suffice for the entire collision content

The bounded degree in (3.8) has a stronger consequence than merely allowing residue tracking.

### Theorem 4.1 — Weighted Vandermonde row reduction

Assume $m\ge4$. For each $0\le i\le m$, let


$$
g_i=w_i(1,i,i^2,i^3,i^4)\in\mathbb Q_3^5.
$$


Choose five distinct indices


$$
P=\{p_1,\ldots,p_5\}
$$


minimizing


$$
\boxed{
\Phi(P)=
\sum_{p\in P}v_3(w_p)
+
\sum_{\substack{p,q\in P\\p<q}}v_3(q-p).
}
\tag{4.1}
$$


Then every interior row $(f_i,\tau_i)$ is a $\mathbb Z_3$-linear combination of the five selected interior rows.

Consequently, if $\mathscr R$ consists of those five rows and the two rows in (3.7), then


$$
\boxed{
\operatorname{cont}_3(\mathcal E)
=
\min_{\substack{R,R'\in\mathscr R\\R\ne R'}}
v_3\det(R,R').
}
\tag{4.2}
$$


There are at most $21$ minors.

#### Proof

The determinant of the five rows $g_p$, $p\in P$, is


$$
\left(\prod_{p\in P}w_p\right)
\prod_{p<q}(q-p),
$$


so its valuation is exactly $\Phi(P)$.

Express any $g_i$ in the selected basis. By Cramer’s rule, each coordinate is a quotient of two determinants. The denominator has minimum valuation among all five-row determinants; each numerator is either zero or another such determinant. Every coordinate therefore belongs to $\mathbb Z_3$.

Evaluation of the two fixed degree-at-most-four polynomials $U,V$ is a linear map


$$
\mathbb Q_3^5\longrightarrow\mathbb Q_3^2.
$$


Applying it preserves the integral linear-combination identities. Thus all interior coefficient rows are generated by the five selected rows.

After adjoining the two boundary rows, every full coefficient row is generated integrally. Bilinearity of the determinant expresses every full minor as an integral combination of the selected minors. The reverse inequality follows because selected minors are themselves full minors. This proves (4.2). ∎

### 4.1 What this proves—and what it does not

This is an exact fixed-number-of-indices collision certificate. Its index selection depends on $m$, but **not on $a_m$**. The actual $a_m$ enters only when the selected rows and their minors are evaluated.

It does not prove that five predetermined indices work for every $m$. Nor does it prove a constant-cost method for finding the minimizing five indices.

A directly verifiable certificate for a proposed $P$ is


$$
\boxed{
v_3(w_i)-v_3(w_p)
+\sum_{\substack{q\in P\\q\ne p}}
\bigl(v_3(i-q)-v_3(p-q)\bigr)\ge0
}
\tag{4.3}
$$


for all $i\notin P$ and $p\in P$. These are exactly the valuations of the weighted Lagrange coordinates. Unlike a claim of “small bounded degree,” (4.3) specifies the remaining universal index test.

### 4.2 Immediate rigorous bounds

Under the retained unit normalization,


$$
z=\operatorname{cont}_3(Z)\ge\min(r,4+u).
$$


The two terms of $\mathcal E$ therefore give


$$
\boxed{
\operatorname{cont}_3(\mathcal E)\ge2\min(r,4+u).
}
\tag{4.4}
$$


The minor of the two boundary rows is $-c_m^2$, so


$$
\boxed{
\operatorname{cont}_3(\mathcal E)\le2v_3(c_m)
=2v_3(\kappa_m).
}
\tag{4.5}
$$


These bounds include the collision. Equation (4.2), not an uncorrected residue certificate, resolves any gap between them.

---

## 5. Exact digit-state obstruction to a universal favorable threshold

Here is an explicit result about compatible middle words. It does not assume any independence of the ternary digits of powers of two.

### Lemma 5.1 — Zero-cost digit paths

Let $m$ be a positive integer whose ternary units digit is $2$, with every other ternary digit in $\{0,1\}$. Suppose its next digit is $1$, as in the resonance suffix. Then


$$
\boxed{
\operatorname{cont}_3(J_m)
=
\operatorname{cont}_3(J_{m-1})=0,
}
\tag{5.1}
$$


with the same parameter $A=2m-1$.

#### Proof by explicit augmented states

Augment the source’s state $(c,b,e)$ by:

- $q$, the carry generating the digits of $s-\tfrac12$;
- the previous digit of $m$, used to generate $3m-1$ or $3m-2$.

For $J_m$, at the units position,


$$
m_0=2,\qquad (3m-1)_0=2,\qquad
(m-\tfrac12)_0=0.
$$


Choose $(k_0,r_0)=(2,0)$. The evaluator state remains


$$
(c,b,e)=(0,0,0),
$$


with cost zero, and the half-integer carry becomes $q=1$.

At the next position, the three digits are $1,1,0$. Choose $(1,0)$, again at zero cost.

Thereafter:

- while $q=1$ and the current digit is $1$, the preceding digit is $1$; choose $(1,0)$;
- at the first digit $0$, choose $(0,0)$; this clears $q$;
- once $q=0$, the half-integer digit is $m_i+1$, so choose
  

$$
(k_i,r_i)=(0,m_i).
$$



All addition carries and subtraction borrows remain zero.

For $J_{m-1}$, the units digit of $s=m-1$ is $1$, that of $N=3m-2$ is $1$, and that of $s-\tfrac12$ is $2$. Choose $(1,0)$. The half-integer carry stays zero. At every later position choose


$$
(k_i,r_i)=(0,m_i).
$$


Again the cost is zero.

The forced high-digit termination accepts both paths with zero carry and zero borrows. Since all costs are nonnegative, both minima are exactly zero. ∎

### 5.1 Exact suffix exit states

The resonance suffix is the first $t$ digits of


$$
247/8=(2,1,1,1,\overline{1,0})_3
$$


read low to high.

For $t\ge6$, the paths just proved exit this suffix with


$$
\boxed{
(c,b,e,q)=(0,0,0,0)
}
\tag{5.2}
$$


for both evaluators. The previous-digit generator state is


$$
\boxed{
m_{t-1}=
\begin{cases}
0,&t\ \text{even},\\
1,&t\ \text{odd}.
\end{cases}}
\tag{5.3}
$$


Every subsequent $0$ or $1$ preserves the zero-cost evaluator state. Thus an all-one middle block is an explicit extremal block for the **minimum possible content**, not just an unspecified compatible word.

### 5.2 These words can satisfy the exact real window

The obstruction is not restricted to the coarse 25-digit prefix.

Fix $t\ge6$. Start from the $L$-digit all-one integer


$$
M_L=\frac{3^L-1}{2}.
$$


Change the digit at position $L-27$ from $1$ to $0$. Replace the low digits by the prescribed first $t$ resonance digits, and choose digit $t$ in $\{0,1\}$ different from the next digit of $247/8$.

Call the resulting integer $m_{L,t}$. If necessary, change one additional low-middle digit from $1$ to $0$ to make $m_{L,t}$ even. For $L$ sufficiently larger than $t$, all these changes are disjoint.

Then:

- the only digit $2$ is the units digit;
- $v_3(8m_{L,t}-247)=t$;
- $m_{L,t}$ is even;
- it has at least 26 leading ones;
- with $D_{L,t}=3^L-2m_{L,t}+1$,
  

$$
\frac{D_{L,t}}{3^L}\longrightarrow\frac2{3^{27}}
  \qquad(L\to\infty,\ t\text{ fixed}).
$$



The limiting value lies strictly inside the required window, because


$$
\frac12<
C_{16}\frac2{3^{27}}
=\frac{295936}{531441}
<1.
$$


Therefore, for all sufficiently large $L$,


$$
\frac1{2C_{16}}
<
\frac{D_{L,t}}{3^L}
<
\frac1{C_{16}}.
\tag{5.4}
$$



By Lemma 5.1,


$$
r=u=0.
$$


Thus, for $h>33$,


$$
2\min(r,4+u)=0<h-33.
\tag{5.5}
$$



### Consequence and limitation

This proves:

> No uniform favorable lower-bound argument using only compatible ternary middle words, the exact resonance suffix, parity, and the exact real window can establish  
> 

$$
> 2\min(r,4+u)\ge h-33.
>
$$



It does **not** prove that any $m_{L,t}$ is $2^{2j-1}$. Nor have the actual Christoffel-unit hypotheses been proved for these auxiliary integers. Accordingly, (5.5) is an automaton/content obstruction, not an original-family inverse-loss evaluation.

The opposite universal upper bound remains open here. In particular, I have not identified the middle words maximizing the content or proved a potential inequality strong enough to exclude $s_c<32$ on every compatible word.

---

## 6. A concrete bounded certificate for selecting the five collision indices

Theorem 4.1 has an implementable exact index-selection procedure.

Write


$$
a_i=v_3(w_i).
$$


For a five-element set $P$,


$$
\Phi(P)=\sum_{i\in P}a_i+
\sum_{\ell\ge1}
\sum_{r\bmod3^\ell}
\binom{\#\{i\in P:i\equiv r\pmod{3^\ell}\}}2.
\tag{6.1}
$$


This follows from


$$
v_3(i-k)=\sum_{\ell\ge1}\mathbf1_{i\equiv k\pmod{3^\ell}}.
$$



Use the ternary residue tree of $0,\ldots,m$. At each node store the minimum cost of choosing $k$ distinct indices, for


$$
k=0,1,\ldots,5.
$$


At an internal node, distribute $k$ among its three children and add


$$
\sum_{\text{children}}\binom{k_{\rm child}}2.
$$


At a singleton leaf $i$, choosing one index costs $a_i$; choosing more than one is forbidden. Backtracking produces a minimizing $P$.

This is an exact six-entry-per-node dynamic program, not an independence assumption. It terminates once $3^\ell>m$.

The weights retain the complete factorial valuation:


$$
\begin{aligned}
v_3(c_i)={}&
v_3\binom{m-\frac12}{m}
+v_3\binom mi\\
&+v_3((6m+2i-2)!)-v_3((3m+i-1)!)\\
&-v_3((6m-2)!)+v_3((3m-1)!)\\
&-v_3((2i)!)+v_3(i!),
\end{aligned}
$$


and


$$
a_i=v_3(c_i)-v_3(E_i)-v_3(E_{i-1}).
$$



A direct implementation is still large in $m$. Compressing its weight-decorated residue tree is a concrete follow-on lemma, not a completed feasibility result.

### New calculation interface

No accepted computation is to be rerun.

For one **new bounded input**, with its exact $m,b,\rho,a_m$:

1. compute the weights $a_i$;
2. run the six-entry residue-tree optimization;
3. output the five selected indices and $\Phi(P)$;
4. verify the weighted Lagrange inequalities (4.3);
5. evaluate the seven corrected rows;
6. output all 21 minor valuations and their minimum.

For a bounded input where direct polynomial construction is feasible, an optional independent comparison is with the direct whole-$\mathcal E$ content.

The expected output is an exact certificate of equality (4.2), not a predicted favorable threshold. No such calculation was executed in this response.

---

## 7. Preserved finite system and global arithmetic

The local reductions do not alter the original finite basis


$$
U_u=(y-1)^u,\quad0\le u<D,
$$




$$
z_i=(y-1)^Dy^i,\quad0\le i<\nu,
$$




$$
Y_b=y^b,\quad d\le b\le m,
\qquad
d=\frac{3D}{2}-1,\quad \nu=\frac D2-1.
$$


Both corrected-column representatives remain required.

The complete functional is still


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1}.
$$


Both leading extractions, every permitted lower pole, the factorial force, and the LOW subtraction remain. The terminal ranges remain


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$


and


$$
J^T\varepsilon+\omega
=
-\varepsilon-s\bigl(\theta e_{\nu-1}
+3^{26}b^{\langle26\rangle}\bigr).
$$


There is no moment beyond $D-4$, and $\omega_{\nu-1}$ is retained.

The directional guard and complete-pair alternative remain separate from the inverse test. In particular,


$$
D_0=\det\Theta,\qquad
D_1=e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
-3^{26}d_{\rm act}\det\Theta
$$


retain the full subtraction.

After restoring all row contents, the actual multiplier, and the actual clearer, set


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the same-index whole error remains


$$
\boxed{
q(e+\pi)-p=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{7.1}
$$



---

## 8. Final status and exact remaining bottlenecks

| Claim | Status |
|---|---|
| Corrected adjacent ratio with factor $6$ | Proved |
| Corrected $R_i,S_i$, interior minors, and boundary rows | Proved |
| Quotient-free multiplication identity | Retained and proved structurally |
| Whole collision content from at most seven selected rows | Proved |
| Uniform low-cost selection of the five interior indices | Not proved |
| Exact zero-cost suffix exit states and $0/1$-middle paths | Proved |
| Exact-window, exact-resonance arbitrary-middle examples with $r=u=0$ | Proved |
| Universal favorable arbitrary-middle threshold | Disproved |
| Universal opposite threshold or original-power threshold | Not decided |
| New real-window intersection with quantitative growth | Conditional on the explicitly identified real-logarithm input pending primary review |
| Original inverse-transfer exclusion | Not obtained |
| Primitive denominator and nonzero whole-error decay | Unresolved |

The principal new algebraic result is the seven-row collision theorem. The principal new digit result is an explicit boundary-compatible obstruction, including exact zero-cost states and a middle block realizing the minimum content even inside the exact real window.

The remaining local target is now precise:

1. prove a uniform **upper** potential inequality for the actual digit minima, or identify their maximizing reachable middle states;
2. on collision, compress or bound the weighted five-index selection and evaluate the corrected 21-minor certificate at $h-33$, using the actual $a_m$;
3. finish the primary-source review needed for the quantitative real-window intersection.

Beyond those local tasks remain the actual directional or complete-pair response, all row contents, the all-prime final gcd, the actual primitive denominator, and infinitely many same-index nonzero whole errors tending to zero.



$$
\boxed{\text{The irrationality of }e+\pi\text{ remains unresolved by this work.}}
$$


