> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 5 — Content-sensitive valuation, an extension obstruction, and an exact higher-kernel recurrence

## Executive conclusions

The complete modulus-$1024$ coefficient table is already being implemented. I neither request it again nor assume that its sufficient mixed identity passes.

**If it passes**, the proved scalar interface gives


$$
H-N\in128\mathbb Z_2
$$


on the original family


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


That would settle $\gamma=\alpha$ at indices with $\alpha=v_2(N)<7$. It would not determine the actual norm depth or $H/N$ on the branch $N\in128\mathbb Z_2$.

The structural progress here is independent of that table:

1. **A content-sensitive exact classification of relative valuation.** After stripping the actual contents of $X$ and $Y-X$, positive excess $\gamma-\alpha>0$ can arise only on one precisely identified cancellation branch.

2. **A rigorous arbitrary-extension obstruction.** In dimension at least five, a fixed finite cylinder can contain primitive integer vector pairs with positive norm, nonzero mixed contraction, arbitrarily deep norm, and arbitrarily large positive relative valuation. Common coordinate-content stripping does not remove this obstruction. This disproves unrestricted unit conclusions based only on such finite-cylinder data—not conclusions restricted by the actual exponential construction.

3. **An exact skew-bilinear factorization criterion.** The desired unit theorem is equivalent, after the appropriate normalization, to a concrete integral divisibility statement. This identifies what an actual structural proof must establish and why merely displaying a skew factorization over $\mathbb Q_2$ would be circular.

4. **An exact recurrence and a finite-state, all-digit content algorithm for the actual higher kernel**
   

$$
\mathcal B_t=\binom Ct\binom{2C+D-t}{D-t},\qquad 0\le t\le D.
$$


   The algorithm retains every binary digit of the actual exponentially reachable $D$. It computes kernel content, not scalar cancellation, and therefore does not overclaim an all-depth theorem for $N,H$.

5. **A denominator/error comparison with the correct direction.** Even $\gamma=\alpha$ does not make the proved dyadic denominator lower bound dominate the whole error. The supplied results do not uniformly exclude this metric family. They give a sufficient exclusion criterion for branches with a sufficiently negative relative valuation, but do not establish that any such infinite branch occurs.

No unconditional proof or disproof of irrationality of $e+\pi$ follows.

---

## 1. Scope and source audit

Retain


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532,
$$


with


$$
D=D_u=\frac{9^{18+32u}-81}{128}.
$$


All actual contact inverse indices remain


$$
0\le i,j<b,
$$


and the scalar coordinates remain


$$
0\le j\le b.
$$



The actual normalized weighted columns and contractions are


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},
\qquad N=X^TX>0,\qquad H=X^TY\ne0.
$$


I reuse the accepted original-family results


$$
X,Y\in2\mathbb Z_2^{b+1},
\qquad H-N\in64\mathbb Z_2.
$$



The source hierarchy matters:

- The contact certificate supplies exact bounded coefficient vectors and finite matrix checks. Its arbitrary-size use still depends on the supplied coefficient-valued transfer proof.
- The joint probe certificate establishes only its listed low states and four auxiliary complete sums. In particular, its auxiliary $D=1,3,5,7$ are not original exponentially reachable indices.
- Turn 3’s asserted independent period $512$ was withdrawn in Turn 4. The safe separate periods and proved diagonal symmetry of Turn 4 are the applicable statements.
- The vectors $p,\delta,\beta$ determine the scalar congruences at their proved precision. Their chosen integer representatives are **not the full exact columns at all depths**.
- The logarithmic force, later factorial tails, and the exterior endpoint may be suppressed only at precisions covered by their complete bounds. An all-depth argument must restore them when that precision is exceeded.

In particular, the nine-entry exterior truncation and degree-$15$ coefficient representatives must not be promoted to an exact all-depth model.

No tools, source searches, or calculations are executed here.

---

## 2. What follows if the mixed coefficient identity passes

The complete scalar interface is


$$
8(H-N)\equiv
\sum_{t=0}^{D-1}\mathcal B_t^2\mathcal D_{\rm full}(D,t)
+\mathcal B_D^2\mathcal D_{\rm end}(D)
\pmod{1024}.
$$


Thus a complete verified zero table proves


$$
H-N\in128\mathbb Z_2.
$$



Put


$$
\alpha=v_2(N),\qquad
\gamma=v_2(H),\qquad
\eta=v_2(H-N),
$$


with $\eta=\infty$ allowed when $H=N$.

The exact valuation alternatives are


$$
\boxed{
\begin{array}{c|c}
\text{condition}&\gamma-\alpha\\ \hline
\eta>\alpha&0\\
\eta<\alpha&\eta-\alpha<0\\
\eta=\alpha&
v_2\!\left(N/2^\alpha+(H-N)/2^\alpha\right)\ge1 .
\end{array}}
\tag{2.1}
$$


In the last row the valuation is finite because $H\ne0$.

### Proof

Write $H=N+(H-N)$. When the two summands have different valuations, the valuation of their sum is their minimum. When their valuations agree, their normalized units are both odd and hence have even sum. ∎

Consequently, a passing table gives:

- $\gamma=\alpha$ whenever $\alpha\le6$;
- no finite upper bound on $\gamma-\alpha$ merely from $\alpha,\gamma\ge7$;
- positive excess valuation only when the defect and norm have **exactly the same depth**.

This last point narrows the outstanding problem. Deep norm alone is not the dangerous case. The dangerous case is equal-depth norm/defect cancellation.

---

## 3. Strip actual coordinate content before asking for a unit

Let


$$
E=Y-X.
$$


If $E=0$, then $H=N$ and the relative valuation is already zero. Otherwise define the actual dyadic contents


$$
c=\min_{0\le j\le b}v_2(X_j),\qquad
d=\min_{0\le j\le b}v_2(E_j).
$$


Set


$$
x=2^{-c}X,\qquad z=2^{-d}E.
$$


Both $x,z$ are primitive vectors over $\mathbb Z_2$: each has at least one unit coordinate.

Define


$$
A=x^Tx,\qquad B=x^Tz.
$$


Then, exactly,


$$
N=2^{2c}A,\qquad H-N=2^{c+d}B,
$$


and


$$
\boxed{\frac HN=1+2^{d-c}\frac BA.}
\tag{3.1}
$$



Writing


$$
a=v_2(A),\qquad \beta=v_2(B),
$$


we obtain


$$
\alpha=2c+a,\qquad
\eta=c+d+\beta.
$$



### Theorem 1 — Content-sensitive branch classification

Put


$$
r=d-c+\beta-a.
$$


Then:

1. If $r>0$, $H/N\in1+2\mathbb Z_2$, so $\gamma-\alpha=0$.
2. If $r<0$, then $\gamma-\alpha=r<0$.
3. If $r=0$, write
   

$$
A=2^aA_0,\qquad B=2^\beta B_0
$$


   with $A_0,B_0$ odd. Then
   

$$
\boxed{\gamma-\alpha=v_2(A_0+B_0).}
   \tag{3.2}
$$



### Proof

Equation (3.1) is exact. Its second summand has valuation $r$. In the equal-depth case,


$$
2^{d-c}B/A=B_0/A_0,
$$


and $A_0$ is a unit. The conclusions follow. ∎

This is an all-depth identity, not a fixed-precision congruence. It also shows precisely what content stripping does **not** solve: a primitive sum of squares $A$ can still have arbitrarily large dyadic valuation.

---

## 4. An arbitrary-extension obstruction survives primitive normalization

A statement that “every finite cylinder has uncontrolled relative valuation” would be false. For example, if a cylinder already fixes a unit norm and an odd mixed contraction, the ratio is a unit throughout that cylinder.

The valid obstruction is more precise: **there are degenerate finite cylinders in which primitive normalization, positive real norm, nonzero mixed contraction, and arbitrarily strong fixed alignment do not bound relative valuation.**

### Theorem 2 — Primitive extension obstruction

For every $m\ge2$, there is a fixed cylinder of pairs of vectors in $\mathbb Z_2^5\times\mathbb Z_2^5$, modulo $2^m$, with the following property.

For every $L\ge m+1$ and every $J\ge m$, the cylinder contains integer vectors $x,y$ such that



$$
\min_i v_2(x_i)=\min_i v_2(y_i)=0,
$$




$$
x^Tx>0,\qquad x^Ty=2^J\ne0,
$$




$$
v_2(x^Tx)=L.
$$



Hence


$$
v_2(x^Ty)-v_2(x^Tx)=J-L
$$


is unbounded above within one fixed cylinder. The norm depth is also unbounded.

### Proof

Because


$$
-7\equiv1\pmod8,
$$


there exists an odd $\zeta\in\mathbb Z_2$ with


$$
\zeta^2=-7.
$$


Thus


$$
x_*=(1,1,1,2,\zeta)
$$


is primitive and isotropic:


$$
x_*^Tx_*=1+1+1+4+\zeta^2=0.
$$



Fix the pair cylinder


$$
x\equiv y\equiv x_*\pmod{2^m}.
$$



For $L\ge m+1$, choose an integer $z$ satisfying


$$
z\equiv \zeta+2^{L-1}\pmod{2^L}.
$$


Then


$$
v_2(z-\zeta)=L-1,
\qquad
v_2(z+\zeta)=1,
$$


because $L\ge3$. Therefore


$$
v_2(z^2+7)=L.
$$



Set


$$
x=(1,1,1,2,z),\qquad A=x^Tx=7+z^2.
$$


This is a positive integer of valuation $L$, and $x\equiv x_*\pmod{2^m}$.

For any $J\ge m$, define


$$
y=x+(2^J-A)e_1.
$$


Since $x_1=1$,


$$
x^Ty=A+(2^J-A)=2^J.
$$


Both $2^J$ and $A$ are divisible by $2^m$, so $y\equiv x\pmod{2^m}$. Both vectors remain primitive because their second coordinate is $1$. ∎

### Consequences and exact limitations

Taking $m\ge7$ gives examples with


$$
x^Ty-x^Tx\in128\mathbb Z_2
$$


but unbounded positive relative valuation.

Multiplying both vectors by $2$ makes both complete columns even, without changing the relative valuation. Their common dyadic content is then exactly $2$, and stripping it returns the primitive examples above.

Zero coordinates may be appended, so this obstruction exists in every dimension at least five.

**These examples are not actual columns of the assigned metric family.** They do not preserve its finite inverse equations, full forcing, factorial structure, or exponential reachability. Their role is to prove that those additional structural constraints are indispensable. Low alignment plus primitivity is not enough.

---

## 5. A factorized bilinear identity: useful criterion, not a hidden proof

The natural all-depth target is


$$
E=\lambda X+SX,
\qquad S^T=-S,
$$


because


$$
X^TSX=0
$$


and therefore


$$
H-N=\lambda N.
$$



There is an exact integral criterion behind this idea.

### Theorem 3 — Integral skew-factorization criterion

Let $x\in\mathbb Z_2^r$ be primitive, $e\in\mathbb Z_2^r$, and $A=x^Tx\ne0$. For a specified $\lambda\in\mathbb Z_2$, the following are equivalent:

1. $x^Te=\lambda A$.
2. There exists $S\in M_r(\mathbb Z_2)$, $S^T=-S$, such that
   

$$
e=\lambda x+Sx.
$$



### Proof

The reverse implication follows from $x^TSx=0$.

For the forward implication, choose $w\in\mathbb Z_2^r$ with


$$
w^Tx=1;
$$


such a vector exists because $x$ is primitive. Put


$$
z=e-\lambda x,\qquad S=zw^T-wz^T.
$$


Then $S^T=-S$, and


$$
Sx=z(w^Tx)-w(z^Tx)=z,
$$


since $z^Tx=0$. ∎

In particular,


$$
x^Te\in2A\mathbb Z_2
$$


is equivalent to such a factorization with $\lambda\in2\mathbb Z_2$, and then


$$
\frac{x^T(x+e)}{x^Tx}=1+\lambda\in\mathbb Z_2^\times.
$$



### Why this is not yet the desired theorem

Over $\mathbb Q_2$, one can always take


$$
\lambda=\frac{x^Te}{A}.
$$


That proves nothing about its integrality or parity. The substantive assertion is


$$
x^Te\in2A\mathbb Z_2,
$$


or the appropriately content-adjusted version from §3.

Thus a useful follow-on factorization must construct $\lambda,S$ **from the actual finite operators and complete forces**, with their integrality proved independently of the desired divisibility.

The full endpoint must be included in that construction:


$$
X_b=\frac{W_b\,b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4}.
$$


Its $+1$ cannot disappear from an all-depth identity merely because it vanished in the modulus-$1024$ scalar calculation.

---

## 6. Exact higher-kernel recurrence with all finite endpoints retained

The higher kernel itself admits a particularly simple exact recurrence.

Write


$$
\mathcal B_t=\binom Ct\binom{2C+D-t}{D-t},
\qquad 0\le t\le D.
$$


Since $C>D$, every kernel value in this range is a positive integer.

### Theorem 4 — Division-free higher-kernel recurrence

For $0\le t<D$,


$$
\boxed{
(t+1)(2C+D-t)\mathcal B_{t+1}
=(C-t)(D-t)\mathcal B_t.
}
\tag{6.1}
$$


Consequently,


$$
\boxed{
(t+1)^2(2C+D-t)^2\mathcal B_{t+1}^2
=(C-t)^2(D-t)^2\mathcal B_t^2.
}
\tag{6.2}
$$



The exact endpoints are


$$
\mathcal B_0=\binom{2C+D}{D},
\qquad
\mathcal B_D=\binom CD.
$$



### Proof

Use


$$
\frac{\binom C{t+1}}{\binom Ct}=\frac{C-t}{t+1}
$$


and, with $d=D-t$,


$$
\frac{\binom{2C+d-1}{d-1}}{\binom{2C+d}{d}}
=\frac d{2C+d}.
$$


Multiplication gives the recurrence. Clearing denominators gives (6.1), so no modular inversion of an even number is used. ∎

If


$$
e_t=v_2(\mathcal B_t),
$$


then this also yields the exact valuation recurrence


$$
\boxed{
e_{t+1}-e_t
=
v_2(C-t)+v_2(D-t)
-v_2(t+1)-v_2(2C+D-t).
}
\tag{6.3}
$$



This is an all-depth identity for the kernel. It is not a claim that the current low coefficient representatives give the actual norm at all depths.

### Terminal adjustment remains mandatory

For any full-block coefficient sequence $a_t$ and actual terminal coefficient $a_{\rm end}$,


$$
\boxed{
\sum_{t=0}^{D-1}\mathcal B_t^2a_t
+\mathcal B_D^2a_{\rm end}
=
\sum_{t=0}^{D}\mathcal B_t^2a_t
+\mathcal B_D^2(a_{\rm end}-a_D).
}
\tag{6.4}
$$


Any summation-by-parts or creative-telescoping use of (6.2) must retain this final correction. At all depths, the separate exterior coordinate must also be added unless independently shown to vanish at the target precision.

---

## 7. A concrete all-digit result: exact kernel content in logarithmic digit length

Define


$$
\mu(C,D)=\min_{0\le t\le D}v_2(\mathcal B_t).
$$


Then


$$
2^{\mu(C,D)}
$$


is the greatest common dyadic divisor of all higher-kernel entries.

This quantity can be computed without enumerating $0\le t\le D$.

### Theorem 5 — Eight-state carry algorithm for kernel content

For any actual nonnegative $C\ge D$, $\mu(C,D)$ is the minimum path cost in the following binary carry system, with eight carry states and $O(\log(C+D))$ digit layers.

At digit $i$, let $C_i,D_i,A_i$ be the bits of $C,D,2C$. A state is


$$
(a,h,w)\in\{0,1\}^3,
$$


representing incoming carries for


$$
t+r=C,\qquad t+d=D,\qquad 2C+d.
$$



Choose bits


$$
\tau,\rho,\delta\in\{0,1\}
$$


subject to


$$
\tau+\rho+a=C_i+2a',
$$




$$
\tau+\delta+h=D_i+2h'.
$$


Set


$$
w'=\left\lfloor\frac{A_i+\delta+w}{2}\right\rfloor.
$$


The transition cost is


$$
a'+w'.
$$



Start in $(0,0,0)$, and finish in $(0,0,0)$ after sufficiently many leading-zero layers; for example,


$$
L=1+\operatorname{bitlength}(2C+D)
$$


layers suffice.

The minimum total cost is $\mu(C,D)$.

### Proof

Every admissible completed path defines nonnegative integers $t,r,d$ satisfying


$$
t+r=C,\qquad t+d=D.
$$


Thus $0\le t\le D$, $r=C-t$, $d=D-t$. Conversely, each such $t$ gives exactly its binary addition path.

By Kummer’s theorem,


$$
v_2\binom Ct
$$


is the number of carries in $t+r=C$, namely the sum of the $a'$. Similarly,


$$
v_2\binom{2C+d}{d}
$$


is the number of carries in $2C+d$, namely the sum of the $w'$. Their sum is $v_2(\mathcal B_t)$.

Minimizing over the paths therefore minimizes over the entire original finite interval $0\le t\le D$. The leading-zero layers clear the final carries and exclude an artificial overflow path. ∎

### Why this advances the structural problem

This is not another low-modulus table. It computes an **unbounded valuation quantity** from **all digits of the actual parameters**.

In particular, it can be applied directly to


$$
D_u=\frac{9^{18+32u}-81}{128},
\qquad C_u=4002D_u+2532,
$$


without substituting a small congruent auxiliary $D$.

The exact reachability recurrence remains


$$
D_{u+1}
=
9^{32}D_u+\frac{81(9^{32}-1)}{128}.
\tag{7.1}
$$



### What it does not compute

Kernel content is not coordinate content of the actual $X$, and neither is automatically the valuation of the contracted norm. After stripping kernel content, scalar cancellation may create further depth.

Likewise, the present low-coefficient contraction is an interface modulo $1024$; it is not an exact all-depth expression for the full columns. Thus Theorem 5 does not by itself establish $\alpha$, $\gamma$, or their difference.

It does, however, isolate a genuine higher-digit contribution that can now be tracked exactly rather than treated as arbitrary.

---

## 8. The appropriate next all-depth lemma

The next structural target should explicitly combine content and reachability.

> **Actual-family content-relative lemma.**  
> For the actual complete columns at $D=D_u$, define $c,d,A,B$ as in §3. Prove either:
> 

$$
> d-c+v_2(B)>v_2(A),
> \tag{8.1}
>
$$


> or, on the equal-depth branch,
> 

$$
> v_2(A_0+B_0)\le L(u)
> \tag{8.2}
>
$$


> for an explicit bound $L(u)$ adequate for the intended denominator comparison.

Equation (8.1) would prove a unit ratio. Equation (8.2) addresses exactly the only branch permitting positive excess relative valuation.

A plausible operator-based route is to prove the integral skew factorization of §5 with an even coefficient after actual content normalization. A plausible kernel-based route is to combine (6.2), the content automaton, and a complete finite-boundary summation identity.

Neither route is supplied by fixed alignment. Both must incorporate:

- the complete actual force at the required depth;
- growing boundary tails when their valuations become relevant;
- all original coordinates;
- the shortened $t=D$ block;
- the exterior $+1$;
- the actual exponentially reachable $D_u$.

The extension theorem shows why replacing this problem by arbitrary primitive columns in a cylinder loses essential information.

---

## 9. Primitive denominator and whole signed error: what is actually excluded?

Keep the least actual clearer $d_B$, and define


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,
\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),
\qquad
q_n=\frac{A_B}{g_B}>0,\qquad
p_n=\frac{H_B}{g_B}.
$$


The gcd is the full integer gcd, including every odd prime. The primitive multiplier is $d_B^2/g_B$.

Put


$$
\Delta_n=\gamma-\alpha.
$$


The retained exact binary interface is


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-\Delta_n
\right\}.
\tag{9.1}
$$



Since $b=n/4002$ and $v_2(b!)=b-s_2(b)$,


$$
v_2(q_n)=
\max\left\{
0,
\left(\frac32-\frac1{4002}\right)n
-\Delta_n+O(\log n)
\right\}.
\tag{9.2}
$$



The retained whole signed error is


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0
$$


eventually, with


$$
\log|\epsilon_n|=-\kappa n+o(n),
\qquad
\kappa=\left(2+\frac1{4002}\right)\log(1+\sqrt2).
$$


Thus the whole evaluated form is


$$
L_n=q_n(e+\pi)-p_n=-q_n\epsilon_n>0
$$


eventually.

### 9.1 The dyadic statement is a lower bound on $q_n$

Because


$$
q_n\ge2^{v_2(q_n)},
$$


we obtain


$$
\boxed{
\log L_n\ge
(\log2)\max\left\{
0,
\left(\frac32-\frac1{4002}\right)n-\Delta_n+O(\log n)
\right\}
-\kappa n+o(n).
}
\tag{9.3}
$$



This is a lower bound, not an upper bound.

### 9.2 Even a unit ratio does not yield dyadic exclusion

If $\Delta_n=0$, the exponential coefficient in this lower bound is


$$
\left(\frac32-\frac1{4002}\right)\log2-\kappa<0.
\tag{9.4}
$$



The strict inequality needs no numerical approximation: the first term is less than $\tfrac32\log2$, while


$$
\kappa>2\log(1+\sqrt2)>2\log2.
$$



Therefore, even a proved all-depth unit theorem would **not** show from the dyadic factor alone that $L_n$ stays away from zero or diverges.

Nor would it prove $L_n\to0$: an exponentially decreasing lower bound says nothing of that kind.

### 9.3 A rigorous branchwise exclusion criterion

Define


$$
a_*=\frac32-\frac1{4002},
\qquad
\delta_*=
a_*-\frac{\kappa}{\log2}<0.
$$


If an infinite actual branch satisfies, for some $\varepsilon>0$,


$$
\boxed{\frac{\Delta_n}{n}\le\delta_*-\varepsilon}
\tag{9.5}
$$


eventually on that branch, then (9.3) gives


$$
\log L_n\ge\varepsilon(\log2)n+o(n),
$$


so


$$
L_n\longrightarrow+\infty.
$$



That branch is therefore excluded from a small-linear-form irrationality proof using these primitive approximants.

The supplied results do not establish an infinite branch satisfying (9.5). They also do not exclude the rest of the actual family.

### 9.4 Why the odd-prime gcd remains essential

The dyadic interface gives only the exponent of $2$ in the actual denominator. The odd part can make $q_n$ much larger.

For a small-error irrationality argument, one needs a same-index **upper bound** on the full $q_n$, sufficiently strong that


$$
q_n|\epsilon_n|\to0.
$$


For exclusion by growth, a sufficiently strong lower bound can suffice.

These directions must not be interchanged. In particular, an upper bound on $\Delta_n$ supplies a lower bound on the dyadic denominator; it is not by itself an upper bound on the full primitive denominator.

---

## 10. A bounded exact calculation beyond another modulus

No repeat contact calculation and no repeat low-coefficient table is needed.

The useful new bounded calculation is an audit of the all-digit kernel-content algorithm.

### Inputs

Use the four actual original indices


$$
u=0,1,2,3,
$$


with exact integers


$$
D_u=\frac{9^{18+32u}-81}{128},
\qquad
C_u=4002D_u+2532.
$$



For each pair $(C_u,D_u)$, run the eight-state minimum-cost carry algorithm of §7.

### Expected verifiable output

For each $u$, output:

1. The exact value
   

$$
\mu(C_u,D_u).
$$


2. A minimizing witness $t_u$, with
   

$$
0\le t_u\le D_u.
$$


3. The three carry sequences.
4. The layer-by-layer eight-state minimum-cost arrays.
5. Independent verification of the witness by the digit-sum identity
   

$$
\begin{aligned}
   v_2(\mathcal B_{t_u})
   ={}&
   s_2(t_u)+s_2(C_u-t_u)-s_2(C_u)\\
   &+s_2(D_u-t_u)+s_2(2C_u)
   -s_2(2C_u+D_u-t_u).
   \end{aligned}
   \tag{10.1}
$$



The dynamic-programming arrays certify minimality; the witness formula certifies attainment. No enormous factorial or complete $t$-sum is required.

This computation concerns only four actual indices. Any apparent pattern in its outputs remains a conjecture until proved along recurrence (7.1). Its purpose is to distinguish kernel-content growth from subsequent coordinate and scalar cancellation, not to substitute finite evidence for a global theorem.

---

## 11. Final ledger

### New rigorous results

- Exact content-sensitive classification of $H/N$.
- Identification of equal-depth norm/defect cancellation as the sole source of positive excess relative valuation.
- A primitive integer extension obstruction, with positive norm and nonzero mixed contraction, showing that fixed alignment and content stripping alone cannot control deep relative valuation.
- An exact integral skew-factorization criterion.
- A division-free recurrence for the actual higher kernel, with both finite endpoints retained.
- An eight-state all-digit algorithm computing the exact dyadic content of that kernel over the entire interval $0\le t\le D$.
- A correct branchwise denominator/error exclusion criterion, with full primitive normalization and the lower-bound direction preserved.

### Conditional result

If the coordinator’s complete sufficient mixed table passes, then


$$
H-N\in128\mathbb Z_2,
$$


and hence $\gamma=\alpha$ wherever $\alpha<7$. No deeper valuation conclusion is assigned in advance.

### Exact remaining bottleneck

The central unresolved arithmetic problem is now sharply expressible:



$$
\boxed{
\text{Control }v_2(A_0+B_0)
\text{ on the actual equal-depth, content-stripped branch at }D=D_u.
}
$$



That control must arise from the actual complete finite equations or an exact boundary-corrected higher-kernel identity. Arbitrary primitive extensions are too flexible, and the present finite coefficient representatives do not encode all higher forces.

Beyond that lies the full odd-prime gcd and a same-index comparison of the actual primitive denominator with the whole signed error.



$$
\boxed{\text{Irrationality of }e+\pi\text{ remains unresolved.}}
$$


