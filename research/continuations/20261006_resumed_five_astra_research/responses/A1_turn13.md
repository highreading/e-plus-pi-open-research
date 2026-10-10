> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 turn13 — Exact phase-dependent Smith exponents and a seeded projective lifting rule

## Executive conclusion

I reuse the proved rank-four connection, the exact seeded recurrence, and the original-branch observation bound. The coordinator’s receipt corroborates those identities and the stated finite samples; it does not evaluate an original-window tuple.

The new result is an **exact local Smith analysis of the actual transition matrix $T(n)$**. For $n\ge1$, let


$$
e_1(n)\le e_2(n)
$$


be its Smith exponents over $\mathbb Z_3$, allowing negative exponents. Then


$$
\boxed{
\begin{array}{c|c}
\text{phase}&(e_1(n),e_2(n))\\ \hline
n\equiv0\pmod3&
\bigl(\varepsilon_n,\,
v_3(n)+v_3(2n+3)-\varepsilon_n\bigr)\\[2pt]
n\equiv1\pmod3&
\bigl(-1-v_3(2n+1),\,1\bigr)\\[2pt]
n\equiv2\pmod3&
\bigl(-v_3(n+1),\,0\bigr),
\end{array}}
$$


where


$$
\varepsilon_n=
\begin{cases}
1,&n\equiv3\pmod9,\\
0,&n\equiv0,6\pmod9.
\end{cases}
$$



This has several concrete consequences for the seeded solution:

* a phase-$2$ step cannot increase common state content;
* a phase-$1$ step increases it by at most one;
* every step $n\equiv3\pmod9$ necessarily adds at least one digit of common content;
* after extracting the displayed scalar factor, the remaining content increment is governed by **one explicit projective congruence, with an exact capped lifting rule**.

Thus the remaining cancellation problem can be stated in terms of specified projective rows, rather than unspecified inverse-entry losses.

I also verify the proposed characteristic-three simplifications on the correct unit branch. They give


$$
\overline{\mathcal A}=\bar\sigma,\qquad
\frac{\overline{\mathcal B}}{\overline{\mathcal A}}
=\frac{x}{\bar t^2},
$$


but do not, without further calculation, supply the requested evaluated observable on the forced prefix and suffix. In particular, I do **not** claim that the intervening middle word has been eliminated.

The progress is an exact local lifting theorem, not a compensated sublinear bound. The original-family primitive direction, the complete producers, and the whole primitive errors remain unresolved.

---

## 1. Scope and reused results

The original indices and real-window conditions remain


$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad A=2m-1,
$$




$$
H_{\rm win}=3^{h-1},\qquad D=H_{\rm win}-A,
$$




$$
\frac1{2C_{16}}<\frac D{H_{\rm win}}<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



Any use of the normalized scalar comparison retains, in addition,


$$
m\equiv851\pmod{6561},\qquad
r=\operatorname{cont}_3(J_m)=\operatorname{cont}_3(J_{m-1}),
$$




$$
s=h-2-2r,\qquad
\mathfrak a\equiv25\pmod{27},\qquad
N_m\in\mathbb Z_3^\times.
$$



I write


$$
V_n=\binom{w_n}{s_n},\qquad
V_0=\binom11,\qquad V_1=\binom{-5}{-4},
$$


for the exact two-coordinate coefficient state of turn12. In particular,


$$
V_{n+1}=T(n)V_n.
$$



The following results are reused, not reproved by generic algebraic closure:

1. the minimal differential rank is exactly four;
2. $V_n\in\mathbb Z_3^2$ for all $n\ge0$;
3. the exact same-index endpoint observation is
   

$$
\binom{a_m}{b_m}=O(m-1)V_{m-1};
$$


4. on the retained original branch,
   

$$
\boxed{c(V_{m-1})-6\le c_m\le c(V_{m-1})-4;}
$$


5. the cumulative inverse-entry estimate is already closed and is linear.

Here and below,


$$
c(z)=\min_i v_3(z_i).
$$



The finite receipt is consistent with these results. Its sample at $m=851$ says


$$
c(V_{850})=4,\qquad c_{851}=0,
$$


with no certified real window. It therefore remains an auxiliary seeded sample, not an original-tuple classification.

---

## 2. The actual transition, in a form suitable for local arithmetic

Set


$$
D_n=(6n+1)(6n+3),
$$


and write


$$
u_n=\alpha_nw_n+\beta_ns_n,\qquad
s_{n+1}=p_nw_n+q_ns_n,
$$


where


$$
\alpha_n=\frac{n(82n+27)}{D_n},
\qquad
\beta_n=-\frac{(10n+3)(3n-1)}{D_n},
$$




$$
p_n=
-\frac{7n(68n^2+68n+15)}{(n+1)D_n},
$$




$$
q_n=
\frac{(3n-1)(62n^2+59n+12)}{(n+1)D_n}.
$$



Then


$$
T(n)=
\begin{pmatrix}
\displaystyle\frac{(8n+7)p_n+(2n+3)\alpha_n}{6n+5}
&
\displaystyle\frac{(8n+7)q_n+(2n+3)\beta_n}{6n+5}
\\[6pt]
p_n&q_n
\end{pmatrix}.
\tag{2.1}
$$



The accepted determinant identity is


$$
\det T(n)=
\frac{n(3n-1)(3n+1)(2n+3)}
{(n+1)(6n+1)(2n+1)(6n+5)}.
\tag{2.2}
$$



Thus, for $n\ge1$,


$$
v_3(\det T(n))
=
v_3(n)+v_3(2n+3)-v_3(n+1)-v_3(2n+1).
\tag{2.3}
$$



For a nonsingular $2\times2$ rational matrix, the smaller Smith exponent is the minimum entry valuation; the sum of the two exponents is the determinant valuation. The substantive calculation is therefore the **exact** minimum entry valuation, not merely a lower bound for it.

---

## 3. Exact Smith exponents in all three phases

### Theorem 3.1

For every integer $n\ge1$, the Smith exponents of $T(n)$ are those displayed in the executive conclusion.

### Proof: phase $n\equiv0\pmod3$

Write $n=3k$, where $k\ge1$. Direct substitution gives


$$
p_{3k}
=
-\frac{21k(204k^2+68k+5)}
{(3k+1)(18k+1)(6k+1)},
\tag{3.1}
$$




$$
q_{3k}
=
\frac{(9k-1)(186k^2+59k+4)}
{(3k+1)(18k+1)(6k+1)}.
\tag{3.2}
$$


All displayed denominators are units.

Likewise,


$$
\alpha_{3k}
=
\frac{3k(82k+9)}{(18k+1)(6k+1)},
\qquad
\beta_{3k}
=
-\frac{(10k+1)(9k-1)}
{(18k+1)(6k+1)}.
\tag{3.3}
$$


Hence $T(3k)$ is integral.

Modulo $3$,


$$
186k^2+59k+4\equiv2k+1.
$$


Consequently $q_{3k}$ is a unit unless $k\equiv1\pmod3$. In those two unit cases, the minimum entry valuation is zero.

If $k\equiv1\pmod3$, then


$$
204k^2+68k+5\equiv2k+2\equiv1\pmod3.
$$


Equation (3.1) therefore gives


$$
v_3(p_{3k})=1.
$$


Meanwhile $q_{3k}$ is divisible by $3$, and both entries in the top row are divisible by $3$: the first follows from (3.3), and the second uses the factor $2n+3$, which is divisible by $3$. Thus the minimum entry valuation is exactly one.

Therefore


$$
e_1(3k)=
\begin{cases}
1,&k\equiv1\pmod3,\\
0,&k\equiv0,2\pmod3.
\end{cases}
$$


The determinant valuation in this phase is


$$
v_3(n)+v_3(2n+3).
$$


Subtracting $e_1$ proves the asserted second exponent.

### Proof: phase $n\equiv1\pmod3$

Put


$$
a=v_3(2n+1)\ge1.
$$


Both numerators defining $p_n,q_n$ are units modulo $3$. In fact,


$$
68n^2+68n+15\equiv1,\qquad
62n^2+59n+12\equiv1\pmod3.
$$


Their denominator has valuation $1+a$. Hence


$$
v_3(p_n)=v_3(q_n)=-1-a.
$$



Every other term in (2.1) has valuation at least $-1-a$, so


$$
e_1(n)=-1-a.
$$


Equation (2.3) gives determinant valuation $-a$, and therefore


$$
e_2(n)=1.
$$



### Proof: phase $n\equiv2\pmod3$

Write $n=3k-1$, with $k\ge1$, and put


$$
b=v_3(n+1)=1+v_3(k).
$$


The two relevant quadratic numerators factor as


$$
68n^2+68n+15
=
3(204k^2-68k+5),
\tag{3.4}
$$




$$
62n^2+59n+12
=
3(186k^2-65k+5).
\tag{3.5}
$$


The parenthesized expressions both reduce to $k+2$ modulo $3$.

It follows that $p_n,q_n$ have valuation at least $-b$, while


$$
v_3(\alpha_n)=v_3(\beta_n)=-1.
$$


Thus every entry of $T(n)$ has valuation at least $-b$.

If $b\ge2$, then $k\equiv0\pmod3$, so the parenthesized expressions in (3.4)–(3.5) are units. The second row then has entries of valuation exactly $-b$.

If $b=1$ and $k\equiv2\pmod3$, the same conclusion holds.

In the remaining case $b=1,\ k\equiv1\pmod3$, the second row is integral. But $2n+3$ is a unit, and the first-row terms involving $\alpha_n,\beta_n$ have valuation $-1$, whereas the terms involving $p_n,q_n$ are integral. They cannot cancel those valuation-$(-1)$ terms. Thus the minimum entry valuation is again $-1=-b$.

Therefore


$$
e_1(n)=-b.
$$


The determinant valuation is $-b$, giving $e_2(n)=0$. ∎

---

## 4. Immediate consequences for actual seeded content

For any nonsingular matrix with Smith exponents $e_1\le e_2$,


$$
c(z)+e_1\le c(Tz)\le c(z)+e_2.
\tag{4.1}
$$



Applied to the actual recurrence, Theorem 3.1 yields


$$
\boxed{
\begin{aligned}
n\equiv0\pmod3:\quad&
\varepsilon_n
\le c(V_{n+1})-c(V_n)
\le v_3(n)+v_3(2n+3)-\varepsilon_n,\\
n\equiv1\pmod3:\quad&
-1-v_3(2n+1)
\le c(V_{n+1})-c(V_n)\le1,\\
n\equiv2\pmod3:\quad&
-v_3(n+1)
\le c(V_{n+1})-c(V_n)\le0.
\end{aligned}}
\tag{4.2}
$$



These statements are stronger than the previously summed inverse-entry estimates.

In particular,


$$
\boxed{c(V_{3k+3})\le c(V_{3k+2})}
\tag{4.3}
$$


and


$$
\boxed{c(V_{9k+4})\ge c(V_{9k+3})+1\ge1\qquad(k\ge0).}
\tag{4.4}
$$



The latter is an obstruction arising from the **actual seeded coefficient sequence**, because its integrality is already proved. It rules out unrestricted state primitivity. It does not rule out a logarithmic content bound, and it does not classify endpoint primitivity.

A sharpened, but still only linear-scale, cumulative bound is


$$
c(V_N)\le\sum_{n=1}^{N-1}e_2(n),
\tag{4.5}
$$


using $c(V_1)=0$. Explicitly, only the phase-$0$ terms and one digit per phase-$1$ step occur in this upper bound; phase-$2$ steps contribute zero.

I do not relabel (4.5) as sublinear. Its importance here is the exact phase separation, not its asymptotic order.

---

## 5. An exact normalized projective lifting rule

The Smith exponents now give an explicit normalization procedure with fully paid scalar valuations.

For each $n\ge1$, define


$$
M_n=3^{-e_1(n)}T(n).
\tag{5.1}
$$


Then $M_n$ is an integral matrix with at least one unit entry. Its Smith exponents are


$$
(0,g_n),\qquad g_n=e_2(n)-e_1(n)\ge0.
\tag{5.2}
$$



Choose row and column permutations moving a unit entry to the top-left position, and write the resulting matrix as


$$
\widetilde M_n=
\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad a\in\mathbb Z_3^\times.
\tag{5.3}
$$


These permutations are fixed by the matrix at that index, not chosen from the unknown state.

Let $z=(z_1,z_2)^T$ be the correspondingly permuted primitive input. Define the exact projective row


$$
\lambda_n(z)=z_1+\frac ba z_2.
\tag{5.4}
$$



### Theorem 5.1 — Capped projective lifting

For a primitive $z\in\mathbb Z_3^2$,


$$
\boxed{
c(\widetilde M_nz)=
\min\{v_3(\lambda_n(z)),\,g_n\}.
}
\tag{5.5}
$$


The convention $v_3(0)=+\infty$ is used.

### Proof

Integral unit row elimination gives


$$
\begin{pmatrix}1&0\\-c/a&1\end{pmatrix}
\widetilde M_nz
=
\binom{a\lambda_n(z)}{(\det\widetilde M_n/a)z_2}.
$$


The determinant has valuation $g_n$.

If $\lambda_n(z)$ is a unit, the output content is zero. If $\lambda_n(z)$ is divisible by $3$, primitivity forces $z_2$ to be a unit: otherwise both $z_1$ and $z_2$ would be divisible by $3$. In that case the content is


$$
\min\{v_3(\lambda_n(z)),g_n\}.
$$


These cases prove the formula. ∎

### Exact seeded recursion

Put


$$
C_n=c(V_n),\qquad Z_n=3^{-C_n}V_n.
$$


Starting from


$$
C_1=0,\qquad Z_1=(-5,-4)^T,
$$


the following recursion is exact:


$$
r_n=\min\{v_3(\lambda_n(Z_n)),g_n\},
\tag{5.6}
$$


with the prescribed column permutation understood, and


$$
\boxed{
C_{n+1}=C_n+e_1(n)+r_n,
\qquad
Z_{n+1}=3^{-r_n}M_nZ_n.
}
\tag{5.7}
$$



Thus the content has the exact decomposition


$$
\boxed{
C_N=\sum_{n=1}^{N-1}e_1(n)+\sum_{n=1}^{N-1}r_n.
}
\tag{5.8}
$$



This is not merely a determinant argument. Each $r_n$ is the depth of an explicit projective congruence, capped at the known Smith gap.

### Precision cost

At a single step:

* determining $r_n$ requires at most $g_n$ digits of $\lambda_n(Z_n)$;
* once $r_n$ is determined, computing $Z_{n+1}\bmod3^K$ is guaranteed by knowing $Z_n\bmod3^{K+r_n}$, together with the matrix coefficients to the same precision.

The scalar $3^{e_1(n)}$ in $T(n)$ is already extracted in (5.1). No division by it is hidden in an alleged integral transition.

This gives a proved local precision cost. It does **not** bound the sum of the $r_n$, and therefore does not yet give a digit-compressed original-index algorithm.

### Lattice formulation

For $0\le r\le g_n$, the input condition


$$
\lambda_n(z)\equiv0\pmod{3^r}
\tag{5.9}
$$


defines an index-$3^r$ sublattice of $\mathbb Z_3^2$. Its underlying exact kernel is a saturated rank-one direct summand because the coefficient of $z_1$ is a unit.

The finite-index congruence lattice itself should not be called saturated in $\mathbb Z_3^2$. The normalized transfer formulation avoids that terminology error.

---

## 6. Three-step determinant compensation: exact, but insufficient

Consider the aligned block


$$
B(k)=T(3k+3)T(3k+2)T(3k+1),
\qquad k\ge0.
\tag{6.1}
$$



The nonunit parts of the determinant telescope:


$$
\boxed{
v_3(\det B(k))
=
v_3(2k+3)-v_3(2k+1).
}
\tag{6.2}
$$



Indeed, over three consecutive steps, (2.3) gives


$$
v_3(3k+1)-v_3(3k+4)
+
v_3(6k+9)-v_3(6k+3),
$$


which is exactly (6.2).

Across consecutive blocks, this telescopes again:


$$
\boxed{
v_3\!\left(\det\prod_{k=0}^{K-1}B(k)\right)
=v_3(2K+1).
}
\tag{6.3}
$$



There is therefore genuine determinant compensation, not a linear determinant loss.

However, (6.3) does not control the smaller Smith exponent of the block product, nor the seeded direction. A matrix can have a nearly unit determinant while having a deeply negative first Smith exponent and a compensating positive second exponent.

The exact scalar extracted by the three one-step normalizations is


$$
E_k=e_1(3k+1)+e_1(3k+2)+e_1(3k+3),
$$


hence


$$
\boxed{
E_k=-3-v_3(2k+1)-v_3(k+1)+\mathbf1_{k\equiv0\pmod3}.
}
\tag{6.4}
$$


Thus


$$
3^{-E_k}B(k)
=
M_{3k+3}M_{3k+2}M_{3k+1}
$$


is integral.

The missing compensation theorem is now precise: it must control the common factors and projective rows of these **actual normalized block products**, not infer state or endpoint primitivity from (6.2).

---

## 7. The characteristic-three branch check

The coordinator’s two proposed reductions are correct.

The distinguished branch is specified by


$$
P(x,t)=t^4-t^3+xt-2x=0,\qquad t(0)=1,
$$




$$
\sigma^2=t(2-t),\qquad \sigma(0)=1.
$$


Since $P_t(0,1)=1$, reduction modulo $3$ preserves a unique formal unit branch.

Now


$$
d(t)=-3t^2+10t-6\equiv t\pmod3.
$$


Because $t$ is a unit series,


$$
\boxed{\overline{\mathcal A}=\bar\sigma.}
\tag{7.1}
$$


Also


$$
x=\frac{t^3(t-1)}{2-t}
$$


gives, on the same branch,


$$
\boxed{
\frac{\overline{\mathcal B}}{\overline{\mathcal A}}
=\frac{t(t-1)}{2-t}
=\frac{x}{t^2}.
}
\tag{7.2}
$$



For the state coordinates, the identity


$$
P_t=\frac{t^2d(t)}{2-t}
$$


reduces to


$$
P_t=\frac{t^3}{2-t},
$$


so


$$
\boxed{
\bar W=\frac{\bar\sigma(2-\bar t)}{\bar t},
\qquad
\bar S=\bar\sigma(2-\bar t).
}
\tag{7.3}
$$



### A useful unit-branch coordinate

Set $u=t-1$. In characteristic $3$,


$$
\boxed{
u(1+u^3)=x(1-u),\qquad
\sigma^2=1-u^2,
}
\tag{7.4}
$$


with $u(0)=0,\ \sigma(0)=1$. Thus


$$
u=x-x^2+x^3+O(x^4),
\qquad
\sigma=1+u^2+O(u^4),
$$


and


$$
S=\sigma(1-u),\qquad
W=\sigma\frac{1-u}{1+u}.
\tag{7.5}
$$



These formulas determine the actual seeded reduction, not a freely chosen algebraic solution.

For example, they give


$$
(w_3,s_3)\equiv(0,2)\pmod3.
\tag{7.6}
$$


At $n=3$,


$$
p_3=-\frac{831}{76},\qquad q_3=\frac{498}{133},
$$


and therefore


$$
p_3/3\equiv2,\qquad q_3/3\equiv1\pmod3.
$$


It follows directly that


$$
s_4/3\equiv2\pmod3.
$$


Since every entry of $T(3)$ is divisible by $3$,


$$
\boxed{c(V_4)=1.}
\tag{7.7}
$$



This is a short symbolic illustration of the obligatory content gain in (4.4), not a request to rerun the accepted seeded computation.

### What is not evaluated

Equations (7.1)–(7.5) are not yet an explicitly evaluated Cartier observable for:

* the forced $25$-digit prefix;
* the known $8$-digit suffix;
* every intervening middle word.

No transition table, reachable/observable quotient, or annihilation certificate for that language is supplied by the attached receipt. I have not derived such a certificate here.

Moreover, even a uniform zero output modulo $3$ would establish only divisibility. It would not identify the primitive endpoint pair. The lifting rule (5.5) explains exactly the missing layer: one must control further projective congruence depths, not stop at a zero first digit.

---

## 8. A concrete next block lemma

The new local theorem reduces the next target to a specific statement.

> **Compensated seeded block lemma.**  
> For the exact blocks $B(k)$ in (6.1), derive normalized block pivot rows and prove a bound for their capped congruence depths along the seed $V_1=(-5,-4)^T$ that compensates the negative scalar sum (6.4). On the retained original indices $N=m-1$, the resulting bound must be substantially sublinear, or it must provide a digit-compressed evaluator with a proved precision budget.

There are two distinct obligations:

1. **Block arithmetic:** determine the entry-content and pivot rows of the rational matrix $B(k)$, including all factors at $k+1$, $2k+1$, and $2k+3$.
2. **Seed following:** prove how the actual primitive input lies relative to those rows.

Solving only the first does not establish the second.

The endpoint observation theorem then transfers any successful state theorem at a constant additional cost on the original family. It does not remove the need for a primitive projective calculation.

The already closed scalar classification continues to require avoidance of the two exceptional endpoint classes, or the stated approach bounds to the two scalar root lines. Nothing in the local Smith theorem proves that avoidance.

---

## 9. One new bounded symbolic calculation

No accepted calculation should be repeated. The useful new symbolic calculation is the **three-step block numerator reduction**, not a dense scan of original length.

### Inputs

Let


$$
\Lambda(n)=(n+1)(6n+1)(6n+3)(6n+5),
\qquad
A_T(n)=\Lambda(n)T(n).
$$


The entries of $A_T(n)$ are polynomials of degree at most four.

Form


$$
\mathcal N(k)
=
A_T(3k+3)A_T(3k+2)A_T(3k+1),
$$




$$
\mathcal D(k)
=
\Lambda(3k+3)\Lambda(3k+2)\Lambda(3k+1).
$$


Then


$$
B(k)=\mathcal N(k)/\mathcal D(k).
$$



### Degree budgets

* Each entry of $\mathcal N(k)$ has degree at most $12$.
* $\mathcal D(k)$ has degree $12$.
* A determinant identity after clearing denominators has degree at most $24$.

### Expected verifiable output

1. The four reduced rational entries of $B(k)$, with all common polynomial cancellations recorded.
2. The gcd over $\mathbb Q[k]$ of the four entries of $\mathcal N(k)$, and its gcd with $\mathcal D(k)$.
3. Taylor expansions of the reduced numerators at the possible nonunit linear factors, sufficient to identify their first nonzero $3$-adic layers.
4. Explicit unit-pivot charts for the block matrix, or a precise list of residue subcases where further lifting is required.
5. A verification of the telescoping determinant identity underlying (6.2).

This calculation is small and exact. It has not been executed in this response. Its output would establish block identities and local charts, **not** automatically prove the seeded compensation lemma.

The degree bounds make the intended calculation falsifiable and bounded; no generic differential-closure computation and no original-length recurrence scan is requested.

---

## 10. Full-producer and primitive-arithmetic boundaries

The local recurrence analysis does not alter the original finite spaces:


$$
0\le v\le2n-2,
$$




$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),\qquad
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$



Both corrected columns and the nonlinear term remain


$$
\widehat Z^{\,\mathrm{act}}
=\widehat Z^{\,c}-3^6WE_{\mathrm{act}}^{-1}T_R,
$$




$$
S_{\mathrm{act}}-S_c
=3^6K_Z-3^{12}T_R^TE_{\mathrm{act}}^{-1}T_R,
$$


with


$$
Q_{\mathrm{act}}=Q_c+3^6R_{\mathrm{prod}},
\qquad
R_{\mathrm{prod}}=R_{25}+3^{25}\Delta_{25}.
$$



All $\Delta_H$ layers, unpaired finite-cutoff contributions, exterior terms, both corrected factors, and nonlinear corrections remain required.

The complete forcing retains the full pole pair, both leading extractions, every permitted lower pole, factorial forcing, and LOW subtraction. The terminal return is still


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$




$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\mathrm{ret}}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


No moment beyond $D-4$ is introduced, and $\omega_{\nu-1}$ is retained.

All row contents, the actual multiplier, and the least actual clearer precede


$$
A_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the whole same-index error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\mathrm{clr}}^{m+1}}{g_\ell}
\det H_{\mathrm{complete}}.
}
$$



For the second producer,


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


and


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$



Neither whole error is evaluated here. No claim about its nonvanishing or decay follows from the selected-prime content analysis.

---

## 11. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Rank-four connection and exact seeded recurrence | Reused, proved |
| Original-branch observation exponents $(-6,-4)$ | Reused at their stated scope |
| Coordinator’s 120 endpoint checks and seeded recurrence through $851$ | Accepted finite corroboration |
| Exact Smith exponents of $T(n)$ in every phase | **Proved here** |
| Phase-$2$ nonincrease of seeded content | **Proved here** |
| Obligatory content gain at $n\equiv3\pmod9$ | **Proved here for the actual seed** |
| Exact capped projective lifting rule and local precision cost | **Proved here** |
| Three-step determinant compensation | **Proved here** |
| Characteristic-three unit-branch simplifications | **Verified here** |
| Evaluated Cartier observable on prefix/middle/suffix language | Not obtained |
| Compensated sublinear seeded content bound | Open |
| Original-family primitive line avoidance | Open |
| Original tuple evaluated | None |
| Complete producers and all-prime whole errors | Open |

### Final result

The new arithmetic result is the exact phase-dependent Smith table, together with the seeded normalization law


$$
\boxed{
C_{n+1}=C_n+e_1(n)
+\min\{v_3(\lambda_n(Z_n)),\,e_2(n)-e_1(n)\}.
}
$$



It identifies both the scalar valuation that must be paid and the precise projective congruence responsible for additional content. The determinant does compensate over aligned three-step blocks, but the proof does not yet show that the actual seeded direction realizes enough of that compensation to give a sublinear normalization budget.

The exact remaining local bottleneck is therefore:



$$
\boxed{
\text{Control the capped block-pivot congruence depths along the fixed seed,
at the retained original indices.}
}
$$



The proposed new bounded calculation concerns only four degree-$12$ block numerators and their local pivot charts. It does not repeat accepted work and does not stand in for the seeded proof.

Algebraic coefficient recurrences and finite-field extraction remain classical machinery, consistent with the literature gate. The present contribution is the specific integral transition analysis; no general novelty or complexity theorem is imported from the inspected abstracts.

Finally, even a successful local normalization theorem would still have to be followed by primitive endpoint line control, the complete finite producers, the all-prime final gcds, the actual primitive denominators, and the whole same-index errors.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved by this work.}}
$$


