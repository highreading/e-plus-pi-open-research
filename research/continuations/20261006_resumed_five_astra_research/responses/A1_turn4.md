> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 4 — Resonance normalization, exact digit transitions, and a quotient-free collision certificate

## Executive conclusion

The normalization issue can be resolved on an infinite subfamily of the **original indices**. Deep resonance implies


$$
j\equiv81\pmod{243},
$$


not just $v_3(j)=4$. Moreover, the resonance progression can be made to meet the precise $C_{16}$ window while retaining


$$
\log(j+1)=O(t),\qquad t=v_3(4^{j+1}-247)\longrightarrow\infty.
$$


Consequently, the moving-base logarithm theorem and its proved tail apply on that intersection. The unit-normalized inverse formula and the depth-$32$ Schur comparison therefore apply simultaneously there.

There is a second, algebraic advance. The collision calculation need not form the Christoffel quotient $Z$, or stream its coefficients recursively. For the actual normalization $A=2m-1$, the monomial coefficients $c_i=[X^i]J_m$ and $d_i=[X^i]J_{m-1}$ satisfy the particularly simple identity


$$
\boxed{\frac{d_i}{c_i}=-\frac{3(m-i)}{6m+2i-3}\qquad(0\le i\le m),}
$$


where $d_m=0$. Together with the coefficient recurrence for $J_m$, this turns the complete inverse-content problem into a minimum over two indices of valuations of explicitly bounded-degree rational expressions. It retains the actual Christoffel scalar and all cancellation.

This is a **quotient-free, bounded-degree certificate**, and it admits a finite digit realization. It is not yet a proved small-state realization at the original moving threshold.

I do **not** obtain a uniform decision


$$
\operatorname{cont}_3(\mathcal E)<h-33
\quad\text{or}\quad
\operatorname{cont}_3(\mathcal E)\ge h-33.
$$


In particular, no original-subfamily exclusion of the depth-$32$ inverse method is proved below. The eight-state content program is made exact, including initialization, termination, and compression of the leading block. What remains missing is a proved uniform estimate for the possible middle-digit products—or an exact reachable-state separation showing how they change the threshold decision.

No computation was executed. No previously accepted terminal, Schur, or normalization computation is requested again.

---

## 1. Normalization scope comes first

Write


$$
t=v_3(4^{j+1}-247)
$$


for the **deep-resonance depth**. This is distinct from the fixed valuation $v_3(A)=5$.

### 1.1 Deep resonance forces the required residue class

For $t\ge6$,


$$
4^{j+1}\equiv247\pmod{729}.
$$


Consequently


$$
4^j\equiv \frac{247}{4}
=1+\frac{243}{4}
\equiv1+243\pmod{729}.
$$



On the other hand,


$$
4^{81}=(1+3)^{81}\equiv1+243\pmod{729}.
$$


The order of $4$ modulo $3^6$ is $3^5=243$, by


$$
v_3(4^q-1)=1+v_3(q).
$$


Therefore


$$
\boxed{j\equiv81\pmod{243}.}
\tag{1.1}
$$


In particular $v_3(j)=4$, and


$$
v_3(A)=v_3(4^j-1)=5.
$$



Thus the residue-class part of the normalization intersection was already implicit in OLDturn1’s resonance hypothesis. It should not have remained an open scope question in Turn 3.

### 1.2 The precise real window

Put


$$
L=h-1,\qquad H=3^L,\qquad
a=\frac1{2C_{16}},\qquad b=\frac1{C_{16}}.
$$


The required condition is


$$
a<1-\frac{4^j-1}{3^L}<b.
\tag{1.2}
$$



OLDturn1 explicitly retains “all the original real-window conditions,” but the supplied text does not reproduce the numerical constants in the underlying reachability lemma. I therefore do not claim to have recovered those absent constants from the report. Instead, the following simultaneous adjustment proves the exact window intersection, including the growth condition needed by its tail argument.

Choose a closed interval


$$
I\subset\bigl(\log_3(1-b),\,\log_3(1-a)\bigr)
$$


with positive length and strictly interior endpoints. For sufficiently large $j$, the condition


$$
j\log_3 4-L\in I
\tag{1.3}
$$


implies (1.2): the correction $3^{-L}$ in $(4^j-1)/3^L$ tends to zero, and the interval has a fixed margin from both boundaries.

For each $t$, exact resonance is obtained by choosing one of the two residue classes


$$
j\equiv a_t\pmod{3^t}
$$


for which


$$
v_3(4^{j+1}-247)=t.
$$


Indeed, $4$ generates $1+3\mathbb Z/3^{t+1}\mathbb Z$; the solution modulo $3^{t-1}$ has three lifts modulo $3^t$, exactly one of which raises the valuation above $t$.

It remains to hit the fixed real interval along


$$
j=a_t+3^t n.
$$



Here is a quantitative reachability argument making the required dependence explicit. Use the standard effective real two-logarithm consequence


$$
\|q\log_3 4\|\ge c q^{-K}\qquad(q\ge1),
\tag{1.4}
$$


for some effective constants $c>0,K>0$. This is a classical real logarithm input, separate from the already closed moving-base $3$-adic theorem.

Let $\ell>0$ be a fixed sufficiently small fraction of the length of $I$, and choose a fixed integer $M>4/\ell$. Dirichlet’s approximation theorem supplies $1\le q\le M$ with


$$
0<\delta=\|q3^t\log_3 4\|\le M^{-1}<\ell/4.
$$


By (1.4),


$$
\delta\ge c(M3^t)^{-K}.
$$


The first $O(\delta^{-1})$ multiples of this small signed rotation form a $\delta$-net of the circle. Hence some


$$
0\le n\ll M\delta^{-1}\ll 3^{Kt}
$$


hits the prescribed translate of $I$. Thus


$$
j\ll3^{(K+1)t},
\qquad
\boxed{\log(j+1)=O(t).}
\tag{1.5}
$$



The selected indices tend to infinity: a fixed integer $j$ cannot have arbitrarily large finite valuation $v_3(4^{j+1}-247)$.

This proves an infinite original subfamily satisfying, simultaneously,


$$
\boxed{
\begin{gathered}
v_3(4^{j+1}-247)=t\to\infty,\qquad
j\equiv81\pmod{243},\\
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},\qquad
\log(j+1)=O(t).
\end{gathered}}
\tag{1.6}
$$



No change to the original power-of-two parameter is made:


$$
m=2^{2j-1}.
$$



### 1.3 Consequence for the inverse comparison

Reuse OLDturn1’s moving-base logarithm theorem and its proved tail at their stated scope. Conditions (1.6) retain precisely the growth and resonance properties used there. Thus, for sufficiently large members of this intersection,


$$
v_3(a_m)=1,\qquad
\mathfrak a=a_m/3\equiv25\pmod{27},
$$


and


$$
N_m=9\kappa_m^2h_m\in\mathbb Z_3^\times.
$$



The accepted depth-$32$ transfer applies on the same indices. Therefore


$$
\boxed{
s_c=h-2-\operatorname{cont}_3(\mathcal E),\qquad
s_c<32\iff\operatorname{cont}_3(\mathcal E)\ge h-33.
}
\tag{1.7}
$$



This resolves the normalization scope **on the constructed original subfamily**. It does not extend the resonant unit law to every index in the real window.

---

## 2. Exact one-digit min-plus matrices

A common notation handles both adjacent polynomials. Let


$$
s\in\{m,m-1\},\qquad
N=s+A,\qquad \alpha=s-\tfrac12.
$$


Then


$$
\operatorname{cont}_3(J_s)
=
\min_{k+r=s}
\left\{
v_3\binom Nk+v_3\binom{\alpha}{r}
\right\}.
\tag{2.1}
$$



The state set is


$$
\mathscr S=\{(c,b,e):c,b,e\in\{0,1\}\},
$$


ordered, for example, lexicographically. Here:

- $c$ is the incoming carry in $k+r=s$;
- $b$ is the incoming borrow in $N-k$;
- $e$ is the incoming borrow in $\alpha-r$.

For digits $\sigma,\nu,\gamma\in\{0,1,2\}$, define the $8\times8$ min-plus matrix


$$
\boxed{
M_{\sigma,\nu,\gamma}
[(c,b,e),(c',b',e')]
=
\min_{\substack{x,y\in\{0,1,2\}\\
x+y+c=\sigma+3c'\\
b'=\mathbf1_{\{x+b>\nu\}}\\
e'=\mathbf1_{\{y+e>\gamma\}}}}
(b'+e'),
}
\tag{2.2}
$$


with the minimum of the empty set equal to $+\infty$.

This is an explicit matrix definition involving at most nine tests per entry-row. Every finite entry is $0,1,$ or $2$.

### Proof of the transition rule

The first constraint is exactly addition of the current digits of $k,r$. The next two are exactly the subtraction-borrow rules. Kummer’s theorem counts the borrows for the ordinary binomial coefficient. For $\alpha\in\mathbb Z_3$, use integer truncations of $\alpha$: after sufficiently many digits the finite subtraction borrow pattern stabilizes, and its count gives $v_3\binom{\alpha}{r}$. Summing the outgoing borrow bits gives the valuation in (2.1).

Taking the minimum over all paths takes the minimum over all $k+r=s$. ∎

### 2.1 Exact digits of the half-integer parameters

There is no floating-point interpretation of $\alpha$. Generate its digits by adding


$$
-\tfrac12=(111\ldots)_3
$$


to the ordinary integer $s$.

Starting with $q_0=0$, set


$$
w_i=s_i+1+q_i,\qquad
\alpha_i=w_i\bmod3,\qquad
q_{i+1}=\lfloor w_i/3\rfloor.
\tag{2.3}
$$


Here $q_i\in\{0,1\}$.

This gives exactly:

- $s=m$: $\alpha=m-\tfrac12$;
- $s=m-1$: $\alpha=m-\tfrac32$.

The digit stream of $N=s+A$ must likewise be the actual stream, including its final carry.

### 2.2 Initialization and termination

Initialize


$$
v_0(0,0,0)=0,\qquad
v_0(\text{other states})=+\infty.
\tag{2.4}
$$



Choose $B$ with $s,N<3^B$. Process positions $0,\ldots,B-1$ using (2.2). Beyond $B-1$, force the chosen digits $x=y=0$; do not continue allowing arbitrary trial digits.

After all finite integer digits have ended:

1. a nonzero addition carry is rejected;
2. a borrow in $N-k$ cannot clear through zero digits and is rejected;
3. an $\alpha-r$ borrow clears at the next eventual digit $1$ of $\alpha$.

The accepted terminal state is $(0,0,0)$. Equivalently, append the forced-digit transitions until the half-integer digit stream has reached its eventual $1$-tail and all admissible borrows have cleared.

These rules prevent false paths corresponding to $k>s$, $r>s$, or artificial nonzero high digits.

---

## 3. Compression of the leading block of ones

Let $L=h-1$. Since


$$
m=\frac{3^L-D+1}{2},
\qquad
\frac{3^L-1}{2}=(\underbrace{11\cdots1}_{L})_3,
$$


we have


$$
m=\frac{3^L-1}{2}-\frac{D-2}{2}.
\tag{3.1}
$$



The exact $C_{16}$ window forces the **first 26 most significant ternary digits** of $m$ to equal $1$, for sufficiently large indices.

Indeed,


$$
D<\frac{3^L}{C_{16}}<3^{L-26},
$$


because


$$
C_{16}=147968\,3^{15}>3^{26}
\quad\Longleftrightarrow\quad
147968>3^{11}=177147
$$


would be false; thus that particular inequality cannot be used.

The correct estimate includes the factor $2$ from (3.1). A block of $B$ leading ones is retained when


$$
\frac{D-2}{2}\le \frac{3^{L-B}-1}{2},
$$


namely $D\le3^{L-B}+1$. Since


$$
3^{25}<C_{16}<3^{26},
$$


the window uniformly certifies **25 leading ones**, not 26:


$$
\boxed{\text{the first 25 most significant ternary digits of }m\text{ are }1.}
\tag{3.2}
$$


Some, but not all, of the window can give a longer block.

This distinction matters at a threshold only a few dozen digits below $h$.

For either adjacent-polynomial evaluator, consider the interior of any actual block of ones, away from its two boundaries. There the digit of $N$ is $1$. Equation (2.3) gives:

- incoming $q=0$: $\alpha_i=2$, and $q$ stays $0$;
- incoming $q=1$: $\alpha_i=0$, and $q$ stays $1$.

Hence a homogeneous interior block of length $B$ is compressed exactly by


$$
\boxed{M_{1,1,2}^{\otimes B}
\quad\text{or}\quad
M_{1,1,0}^{\otimes B},}
\tag{3.3}
$$


where $\otimes$ denotes min-plus multiplication. Boundary digits are processed separately.

Repeated squaring evaluates this block in $O(\log B)$ matrix products. This is an exact compression rule, not an assertion that both incoming half-integer carries have the same effect.

### What this does not yet prove

The resonance fixes a long **low** block. The window fixes a **high** block. The middle word is still the actual middle word of $2^{2j-1}$.

I have not established a bound on all compatible middle products strong enough to decide


$$
2\min(r,4+u)\gtreqless h-33.
$$


Nor have I established, by exact joint-state reachability, that two compatible middle words give opposite decisions at this threshold.

Those alternatives require proof. Neither follows from the existence of the eight-state evaluator, and arbitrary suffix experiments do not settle original-family applicability.

---

## 4. A quotient-free advance on the collision branch

Write


$$
J_m(X)=\sum_{i=0}^m c_iX^i,\qquad
J_{m-1}(X)=\sum_{i=0}^{m-1}d_iX^i,
$$


with $d_m=0$. All $c_i$ are nonzero rational numbers.

### 4.1 Actual coefficient recurrences

The hypergeometric representation compatible with the supplied normalization gives


$$
\boxed{
\frac{c_i}{c_{i-1}}
=
\frac{(i-1-m)(6m+2i-3)}{i(2i-1)}
\qquad(1\le i\le m).
}
\tag{4.1}
$$


Equivalently, define


$$
Q_i=-\frac{i(2i-1)}
{(m+1-i)(6m+2i-3)},\qquad Q_0=0;
$$


then $c_{i-1}=Q_ic_i$.

For the adjacent polynomial with the **same** parameter $A=2m-1$,


$$
\boxed{
d_i=-\frac{3(m-i)}{6m+2i-3}c_i
\qquad(0\le i\le m).
}
\tag{4.2}
$$



#### Derivation of (4.2)

At zero,


$$
\frac{d_0}{c_0}
=
-\frac{\binom{m-\frac32}{m-1}}
{\binom{m-\frac12}{m}}
=
-\frac{2m}{2m-1}.
$$


In the hypergeometric coefficient ratio, decreasing the degree from $m$ to $m-1$ contributes


$$
\frac{m-i}{m}
\cdot
\frac{m+A-\frac12}{m+A+i-\frac12}.
$$


Substituting $A=2m-1$ yields (4.2), including $i=m$. ∎

The denominator $6m+2i-3$ is retained. It is not generally a $3$-adic unit.

### 4.2 Avoiding polynomial division by $3X-\eta$

Put


$$
L(X)=3X-\eta,\qquad \eta=A+71,
$$




$$
F(X)=L(X)Z(X)
=(X-b_m-a_m)J_m(X)-\rho J_{m-1}(X).
\tag{4.3}
$$


Define


$$
V(X)=L(X)J_m(X),\qquad
\mathcal T(X)=XF(X)+\mathfrak a V(X).
\tag{4.4}
$$



Multiplying the complete inverse-kernel identity gives


$$
\boxed{
(X-Y)L(X)L(Y)\mathcal E(X,Y)
=
\mathcal T(X)F(Y)-F(X)\mathcal T(Y).
}
\tag{4.5}
$$



Both $X-Y$ and $L$ have $3$-adic content zero on the original resonant family. Gauss’s lemma therefore gives


$$
\boxed{
\operatorname{cont}_3(\mathcal E)
=
\min_{i<k}v_3(\tau_i f_k-f_i\tau_k),
}
\tag{4.6}
$$


where $f_i=[X^i]F$, $\tau_i=[X^i]\mathcal T$.

Unlike the previous pivot certificate, this one does not require computing the quotient $Z$.

### 4.3 Bounded-degree formulas for every interior coefficient

For $0\le i\le m$, set


$$
R_i
=
Q_i-(b_m+a_m)
+\frac{3\rho(m-i)}{6m+2i-3},
\tag{4.7}
$$


and


$$
S_i
=
Q_iR_{i-1}
+\mathfrak a(3Q_i-\eta).
\tag{4.8}
$$


At $i=0$, the product $Q_0R_{-1}$ is defined to be zero.

Then


$$
\boxed{f_i=c_iR_i,\qquad \tau_i=c_iS_i.}
\tag{4.9}
$$


Consequently every interior minor is


$$
\boxed{
\tau_i f_k-f_i\tau_k
=
c_ic_k\bigl(S_iR_k-R_iS_k\bigr).
}
\tag{4.10}
$$



The rational functions $R_i,S_i$ have degrees bounded independently of $m$. Their parameters are the **actual**


$$
m,\ b_m,\ a_m,\ \rho,\ \eta,\ \mathfrak a.
$$


In particular, $a_m$ is not replaced by $75$, by its residue modulo $27$, or by an arbitrary unit lift.

The remaining boundary coefficients are exactly


$$
\begin{array}{c|cc}
i&f_i&\tau_i\\ \hline
m+1&c_m&c_m(R_m+3\mathfrak a)\\
m+2&0&c_m.
\end{array}
\tag{4.11}
$$


Thus (4.6) includes all boundary minors without extending the original inverse matrix: the extra degrees arise only from multiplying its polynomial identity by $L(X)L(Y)(X-Y)$.

### Proof status and significance

Equations (4.6)–(4.11) are exact, including in the collision


$$
r=4+u.
$$


They eliminate the long polynomial-division/pivot stream as a necessary representation of the problem. They do not, by themselves, bound the resulting minimum.

---

## 5. A finite digit certificate for the quotient-free formula

The coefficient valuations in (4.10) also have an exact factorial description. With


$$
v_0=v_3\binom{m-\frac12}{m},
$$


one has


$$
\begin{aligned}
v_3(c_i)={}&v_0+v_3\binom mi\\
&+v_3((6m+2i-2)!)-v_3((3m+i-1)!)\\
&-v_3((6m-2)!)+v_3((3m-1)!)\\
&-v_3((2i)!)+v_3(i!).
\end{aligned}
\tag{5.1}
$$


Powers of $2$ cancel from the valuation. This follows by writing the ratio


$$
\frac{(3m-\frac12)_i}{(\frac12)_i}
$$


as a ratio of odd products.

After clearing the fixed rational parameter denominators and the displayed linear denominators in $R,S$, write


$$
S_iR_k-R_iS_k=\frac{P(i,k)}{D(i,k)}
\tag{5.2}
$$


as an **exact identity**, without dropping common factors. Here $P,D$ have degrees bounded independently of $m$.

Thus the interior part of the certificate is


$$
\min_{0\le i<k\le m}
\left\{
v_3(c_i)+v_3(c_k)+v_3(P(i,k))-v_3(D(i,k))
\right\}.
\tag{5.3}
$$



For any fixed working modulus, this admits a finite digit realization:

- ternary addition automata generate all affine arguments of the factorials;
- Legendre’s formula evaluates their valuations by digit sums;
- a comparison automaton enforces $0\le i<k\le m$;
- residues of $i,k$ modulo $3^B$ evaluate the cleared polynomials modulo $3^B$;
- boundary terms (4.11) are handled separately.

This is a constructive finite-state specification. It is not evidence of a feasible state count. Residue tracking alone can require $3^{2B}$ states, and the precision needed for exact cancellation can depend on the actual Christoffel scalar.

Accordingly, the new result is a **bounded-degree digit certificate**, not a proved eight-state collision minimizer. It does not justify calling the original calculation small.

---

## 6. The precise outstanding local lemma

On the original intersection (1.6), the noncollision branches remain rigorously


$$
\operatorname{cont}_3(\mathcal E)=
\begin{cases}
2r,&r<4+u,\\
2(4+u),&r>4+u.
\end{cases}
\tag{6.1}
$$


The collision is now governed by (4.6)–(4.11).

A concrete next lemma is:

> **Original-window middle-product and collision lemma.**  
> For the actual $m=2^{2j-1}$ on (1.6), combine the resonance suffix, the certified leading-one prefix, and the intervening digit products to determine the comparison of $r$ and $4+u$. In the collision case, bound the minimum (5.3), including all boundary minors, at $h-33$.

Two distinct achievements would suffice:

1. a uniform automaton inequality valid for **all** middle words compatible with the fixed boundaries; or
2. an original-power-of-two theorem restricting the reachable middle words sufficiently to obtain the inequality.

An arbitrary compatible middle word is not an original power of two. Conversely, a short binary exponent description does not supply its ternary digits at low cost.

I have proved neither of these achievements here. Therefore the exact inverse-transfer branch is still undecided.

---

## 7. What remains available if inverse transfer fails

An exclusion of $s_c<32$, if eventually proved, would exclude this **uniform inverse-loss comparison**, not the entire determinant construction.

The directional method still retains the actual endpoint vector and the whole scalar. The direct whole-pair method retains


$$
\Theta=-S_{\rm act}/3^{26},
\qquad
D_0=\det\Theta,
$$




$$
\boxed{
D_1=e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
-3^{26}d_{\rm act}\det\Theta.
}
\tag{7.1}
$$


The accepted six-digit complete-pair transfer does not require a preliminary inverse bound. It remains potentially useful if the two actual pair valuations become visible within that interval. No such visibility is proved here.

---

## 8. Finite boundaries and global arithmetic are unchanged

Nothing above changes the original columns


$$
U_u=(y-1)^u,\quad 0\le u<D,
$$




$$
z_i=(y-1)^Dy^i,\quad0\le i<\nu,
$$




$$
Y_b=y^b,\quad d\le b\le m.
$$


Both corrected-column representatives remain necessary in the complete bilinear core calculation.

The complete functional is still


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1}.
$$


All finite pole terms, both leading extractions, the factorial force, and the LOW subtraction remain.

The terminal equations retain exactly their original ranges:


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


There is no extra moment beyond $D-4$, and $\omega_{\nu-1}$ is retained.

All row contents, the actual multiplier, and the least actual clearer must still be restored. With


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


retain


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**, and, when $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The same-index whole error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{8.1}
$$



No local content conclusion can replace this normalization or establish nonvanishing and decay of (8.1).

---

## 9. Bounded arithmetic interface and final proof status

The coordinator’s already planned new bounded power-of-two tests need no replacement or repetition. Their outputs remain finite corroboration, not real-window certificates.

The genuinely new bounded check supplied by this report is the quotient-free identity.

**Inputs:** any new bounded actual power-of-two $m$, $A=2m-1$, the exact Jacobi polynomials, and the exact Christoffel scalar


$$
a_m=p_{m+1}(r_0)/p_m(r_0),
\qquad r_0=(A+71)/3.
$$



**Expected verifiable output:**

1. zero rational discrepancy in (4.1) and (4.2), including $d_m=0$;
2. zero discrepancy in every coefficient identity (4.9) and boundary identity (4.11);
3. zero polynomial discrepancy in (4.5);
4. equality between direct $\mathcal E$-content and the complete minor minimum (4.6).

Outside the resonant original family, scalar-unit simplifications must not be presumed. The rational identities themselves remain testable. No favorable valuation is predicted.

### Final ledger

| Result | Status |
|---|---|
| Deep resonance implies $j\equiv81\pmod{243}$ | Proved |
| Exact $C_{16}$-window intersection with $\log(j+1)=O(t)$ | Proved using quantitative real-logarithm reachability |
| Moving-base theorem and proved tail on that intersection | Reused at their established scope |
| Simultaneous unit normalization and depth-$32$ comparison | Established on the constructed original subfamily |
| Explicit one-digit $8\times8$ min-plus matrices | Proved |
| Exact half-integer initialization and terminal rules | Proved |
| Leading-one block compression | Proved |
| Uniformly guaranteed leading block | 25 digits; no blanket 26-digit claim |
| Uniform threshold decision from suffix and prefix | Not proved |
| Original-family dependence on middle digits | Not decided by reachability here |
| Adjacent monomial coefficient ratio | Proved |
| Quotient-free whole-content certificate, including collision | Proved |
| Small collision automaton at the moving threshold | Not proved |
| New original-subfamily exclusion of inverse transfer | Not obtained |
| All-prime primitive denominator and whole-error theorem | Unresolved |

The principal new algebraic result is


$$
\boxed{
\operatorname{cont}_3(\mathcal E)
=
\min_{i<k}v_3(\tau_i f_k-f_i\tau_k),
}
$$


with $f_i,\tau_i$ given by bounded-degree rational expressions in the index and the actual Jacobi coefficients, rather than by a Christoffel quotient stream.

The exact remaining local bottleneck is the threshold minimum on the actual original power-of-two family, including middle-digit behavior and collision cancellation. Beyond it remain the directional whole pair, all row contents, the final all-prime gcd, and infinitely many same-index nonzero whole errors tending to zero.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ has been obtained.}}
$$


