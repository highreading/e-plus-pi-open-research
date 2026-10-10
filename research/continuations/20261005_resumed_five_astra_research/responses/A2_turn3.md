> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — A normalized higher-tail functional, and the remaining all-depth obstruction

## Executive summary

I use the supplied 406-entry initializer and the coordinator’s completed exact-arithmetic certificate. I do **not** request a duplicate initializer. No tools were executed.

The main new result is an explicit scalar formula for the entire higher-tail contribution to


$$
\frac{\mathcal T}{29^3}\pmod{29}.
$$


It uses the actual initializer, incorporates its harmonic entries, and retains both shifted finite endpoints. After writing


$$
H=20+29z+29^2R,\qquad 0\le z<29,
$$


put


$$
C=2001R+69z+47,\qquad E=2C+1.
$$


Define the finite sums


$$
\mathscr T_L(C,E)
=\sum_{u=0}^{L}
\binom Cu^2\binom{E+L-u}{L-u}^2,
$$




$$
\mathscr V_L(C,E)
=\sum_{u=0}^{L}(2u-L)
\binom Cu^2\binom{E+L-u}{L-u}^2,
$$


with both sums defined as zero when $L=-1$. Then


$$
\boxed{
\frac{\mathcal T}{29^3}
\equiv
a_0(z)\mathscr T_R+b_0(z)\mathscr V_R
+a_1(z)\mathscr T_{R-1}+b_1(z)\mathscr V_{R-1}
\pmod{29}.
}
\tag{A}
$$


All four coefficient functions are evaluated below.

A substantial simplification occurs for $9\le z\le28$:


$$
\boxed{
\frac{\mathcal T}{29^3}
\equiv \lambda_z\,\mathscr T_R(C,2C+1)\pmod{29},
\qquad \lambda_z\ne0.
}
\tag{B}
$$


This is a unit multiplier of a **whole higher-tail convolution**, not a unit theorem for that convolution. The $+1$ in $2C+1$ is essential.

I also give:

1. An equivalent finite polynomial-product formula retaining every higher digit of $C$ and $2C+1$.
2. An exact, all-depth, eight-state minimum-carry classification of the common $29$-content of the auxiliary column $(X_k)$, together with a proved bridge from the original powers $3^a$ to its complete input strings.
3. A proof that arbitrarily deep auxiliary common-content refinements remain originally reachable. This does **not** promote the precision-three actual-column reconstruction to an all-depth factorization.
4. A precise separation of common column content from the additional valuation caused by cancellation in a primitive norm.
5. A concrete all-depth follow-on target: an actual finite-boundary telescoping identity for the mixed defect. I prove that such an identity would track the **full actual norm valuation**, however deep. Its existence for the supplied columns remains open.

The new functional evaluates the outstanding norm digit as a genuine higher-tail scalar. It does not prove that this scalar is nonzero at infinitely many original indices, nor does it control the full actual relative valuation when that scalar vanishes.

**The irrationality or rationality of $e+\pi$ remains unresolved.**

---

## 1. Original domain and accepted scope

Throughout,


$$
p=29,\qquad L=p^4=707281,\qquad b_*=687936,
$$




$$
a=432827+682892t,\qquad t\ge0,\qquad b=3^a,\qquad n=2001b.
$$


The actual column coordinates remain


$$
0\le j\le b,
$$


and every contact inverse retains


$$
0\le i,j<b.
$$



The metric is the falling metric


$$
\omega_j=j!\binom{n+2}{j}=(n+2)_{\underline j}.
$$


For the already weighted reconstructed columns,


$$
P=\frac{Z_w}{p^2},\qquad
Q=\frac{Y}{p^3},\qquad
Y=\frac{V_w}{b!},
$$


write


$$
D=P^TP,\qquad M=P^TQ,\qquad \rho_n=(6C_n)^{-1}.
$$



I work principally on the accepted original cylinder


$$
t\equiv364\pmod{841}.
\tag{1.1}
$$


There,


$$
b=b_*+p^5H,\qquad H\equiv20\pmod p,
$$


and


$$
A=2001H+67.
$$


The auxiliary terms and norm are


$$
X_k=\binom Ak\binom{2A+H-k}{H-k},
\qquad 0\le k\le H,
$$




$$
\mathcal T=\sum_{k=0}^{H}X_k^2.
$$



The accepted A2 turn 2 results, independently audited in A4 turn 6, give


$$
p\mid X_k\quad(0\le k\le H),\qquad
\mathcal T\in p^3\mathbb Z,
\tag{1.2}
$$


and, for the complete actual columns,


$$
\boxed{
D\equiv5C_n^2\mathcal T\pmod{p^4},
\qquad
M-\rho_nD\equiv0\pmod{p^4}.
}
\tag{1.3}
$$



These conclusions retain the full reconstruction dependencies:

- the safe positive support before graded reduction;
- the complete factorial boundary at the precision used;
- the unfrozen $LJ\,W_jB_{-2}(j)$ insertion;
- removal of the logarithmic contribution only by its complete-force valuation bound;
- the actual endpoint
  

$$
Z_{w,b}=W_b\,b\theta^P_{b-1},\qquad
  Y_b=W_b(1+b\theta^Q_{b-1});
$$


- the actual high ranges
  

$$
0\le J\le h\quad(x\le b_*),\qquad
  0\le J\le h-1\quad(x>b_*).
$$



Nothing in the new auxiliary reduction changes those hypotheses or extends their precision.

### Status of the newly supplied arithmetic

The coordinator’s certificate supplies:

- $28!\equiv521\pmod{841}$;
- all 58 boundary weights divisible by $29$;
- 38 nonzero normalized weights and 140 nonzero harmonic entries;
- agreement of the full recurrence with direct complete sums at the stated 33 auxiliary values.

The 33 comparisons establish their stated finite scope. The uniform formula below follows instead from the proved recurrence and the complete initializer.

---

## 2. Extracting the actual tail after the two initialized digits

Write


$$
G=z+pR,\qquad 0\le z<p,
$$


so that


$$
H=20+pz+p^2R.
\tag{2.1}
$$



The affine parameters are then exactly


$$
A=9+19p+p^2C,
\qquad
C=2001R+69z+47,
\tag{2.2}
$$


and


$$
2A=18+9p+p^2E,
\qquad E=2C+1.
\tag{2.3}
$$



Thus the higher second-binomial parameter is $2C+1$, not $2C$. The added $1$ is the retained carry from doubling the digit $19$.

After the first two digits, the accepted one-carry recurrence has states


$$
(\sigma,\beta,\gamma,v)=(\sigma,0,0,1),
\qquad \sigma\in\{0,1\}.
$$


Here $\sigma$ is the carry in the summation identity $k+(H-k)=H$.

If $u$ is the remaining high part of $k$, the remaining high part of $H-k$ is


$$
R-u-\sigma.
$$


Consequently the actual high ranges are


$$
0\le u\le R\quad(\sigma=0),
\qquad
0\le u\le R-1\quad(\sigma=1).
\tag{2.4}
$$


The second range is empty when $R=0$.

This is the source of the shifted endpoint in (A).

---

## 3. Compression of the supplied harmonic states

### 3.1 A structural pattern in the actual table

Every supplied initializer row has the form


$$
Z_\sigma(z)
=
(0,h_\sigma(z),j_\sigma(z),h_\sigma(z),0,-j_\sigma(z))
\quad\text{in }\mathbb F_{29}^6.
\tag{3.1}
$$


This statement is a direct evaluation of the finite supplied table.

Let


$$
r_\sigma(z)=W_\sigma(z)/p\pmod p.
$$


The division is legitimate by the established boundary-state divisibility.

At the next digit, let the digit tuple be


$$
\tau=(c,s,u_0,r,e,\ell_0),
$$


in the ordering used by the audited recurrence. Since the unique binomial carry has already been spent, a surviving continuation must have


$$
r=c-u_0,\qquad s=e+\ell_0
$$


with no new borrow or carry. Therefore


$$
\begin{aligned}
\tau\cdot Z_\sigma
&=h_\sigma(s+r)+j_\sigma(u_0-\ell_0)\\
&=h_\sigma(c+e)
 +(j_\sigma-h_\sigma)(u_0-\ell_0).
\end{aligned}
\tag{3.2}
$$



Modulo $p$,


$$
c+e\equiv C+E=3C+1,
$$


and


$$
u_0-\ell_0\equiv2u-(R-\sigma).
$$


Hence


$$
\boxed{
\tau\cdot Z_\sigma
=
h_\sigma(3C+1)
+(j_\sigma-h_\sigma)(2u-(R-\sigma))
\quad\text{in }\mathbb F_p.
}
\tag{3.3}
$$



### 3.2 Why no later harmonic correction survives

The initialized weight is $W_\sigma=pr_\sigma\pmod{p^2}$. The next update gives


$$
W_{\rm new}/p
=
g\,[r_\sigma+2\tau\cdot Z_\sigma]\pmod p.
\tag{3.4}
$$


At the same step, the new harmonic accumulator is zero, because its update contains $W_\sigma\bmod p=0$.

Every later step therefore uses only its ordinary carry-free squared-binomial weight modulo $p$. This is not a deletion of later digits: all later digits still contribute through those weights and through their terminal conditions.

---

## 4. The normalized higher-tail scalar

For $L\ge0$, define


$$
B_{L,u}(C,E)
=\binom Cu\binom{E+L-u}{L-u},
\qquad 0\le u\le L,
$$




$$
\mathscr T_L(C,E)=\sum_{u=0}^{L}B_{L,u}(C,E)^2,
\tag{4.1}
$$




$$
\mathscr V_L(C,E)
=\sum_{u=0}^{L}(2u-L)B_{L,u}(C,E)^2.
\tag{4.2}
$$


Set


$$
\mathscr T_{-1}=\mathscr V_{-1}=0.
$$



### Theorem 1 — complete normalized higher-tail functional

For every nonnegative auxiliary $H=20+29z+29^2R$, with $A=2001H+67$, and therefore in particular for every actual $H$ on (1.1),


$$
\boxed{
\frac{\mathcal T}{p^3}
\equiv
\sum_{\sigma=0}^{1}
\left[
a_\sigma(z)\mathscr T_{R-\sigma}(C,E)
+b_\sigma(z)\mathscr V_{R-\sigma}(C,E)
\right]\pmod p,
}
\tag{4.3}
$$


where $C,E$ are given by (2.2)–(2.3), and


$$
a_\sigma(z)
=r_\sigma(z)+2h_\sigma(z)(3C+1),
\tag{4.4}
$$




$$
b_\sigma(z)=2(j_\sigma(z)-h_\sigma(z)).
\tag{4.5}
$$


Since


$$
C\bmod p=11z+18\bmod p,
$$


these coefficients depend only on $z$.

#### Proof

Put


$$
S=\sum_{k=0}^{H}(X_k/p)^2.
$$


By (1.2), $p\mid S$, and $\mathcal T/p^3=S/p$.

Terms with at least two binomial carries contribute zero to $S\bmod p^2$. On the preferred auxiliary family there are no zero-carry terms. Thus the audited recurrence selects exactly the necessary terms.

After the two initialized digits, the unique carry has been used. For each $\sigma$, every surviving continuation corresponds to one


$$
0\le u\le R-\sigma
$$


with no higher carry in either binomial. Its remaining product of digit weights is


$$
B_{R-\sigma,u}(C,E)^2\pmod p.
$$


If a higher carry occurs, this binomial product is zero modulo $p$; consequently the summation may include every $u$ in the displayed finite range.

Equations (3.3)–(3.4) give its normalized initialized coefficient


$$
a_\sigma(z)+b_\sigma(z)(2u-(R-\sigma)).
$$


Summing proves (4.3). The accepted terminal conditions enforce the ranges (2.4), and the harmonic accumulator has already been discharged exactly as in Section 3. ∎

---

## 5. Evaluation of all coefficient functions

### 5.1 The first nine $z$-classes

The supplied table gives:



$$
\begin{array}{c|rrrr}
z&a_0&b_0&a_1&b_1\\ \hline
0&11&3&5&26\\
1&25&5&10&24\\
2&2&26&8&3\\
3&17&6&17&23\\
4&17&7&22&22\\
5&17&6&27&23\\
6&9&26&5&3\\
7&18&5&11&24\\
8&7&3&27&26
\end{array}
\tag{5.1}
$$



In each of these rows,


$$
b_1=-b_0.
$$


Thus another useful form is


$$
\boxed{
\frac{\mathcal T}{p^3}
\equiv
a_0\mathscr T_R+a_1\mathscr T_{R-1}
+b_0(\mathscr V_R-\mathscr V_{R-1})
\pmod p.
}
\tag{5.2}
$$



For example, at $z=0$, the first table row has


$$
r_0=2,\quad h_0=13,\quad j_0=0,
$$


and $C\equiv18$, so $3C+1\equiv26$. Therefore


$$
a_0=2+26\cdot26=11,\qquad b_0=-26=3.
$$


The $\sigma=1$ row similarly gives $a_1=5,b_1=26$.

### 5.2 The twenty single-convolution classes

For $9\le z\le28$, all $\sigma=1$ entries vanish, and the $\sigma=0$ entries satisfy $j_0=h_0$. Hence both centered-moment coefficients vanish.

The result is


$$
\boxed{
\frac{\mathcal T}{p^3}
\equiv\lambda_z\mathscr T_R(C,2C+1)\pmod p,
}
\tag{5.3}
$$


with


$$
\begin{array}{c|rrrrrrrrrr}
z&9&10&11&12&13&14&15&16&17&18\\ \hline
\lambda_z&7&9&25&2&27&7&9&8&27&9
\end{array}
$$




$$
\begin{array}{c|rrrrrrrrrr}
z&19&20&21&22&23&24&25&26&27&28\\ \hline
\lambda_z&1&9&19&13&10&26&10&25&10&14.
\end{array}
\tag{5.4}
$$


Every $\lambda_z$ is a unit.

This is the strongest direct simplification supplied by the new initializer. It does not remove the higher-tail convolution.

### Two arithmetic consistency checks, not new extrapolations

For $G=29$, one has $z=0,R=1$. Here $C\equiv18,E\equiv8$, so


$$
\mathscr T_1\equiv18^2+9^2=28,\qquad
\mathscr V_1\equiv18^2-9^2=11.
$$


Formula (5.1) gives


$$
11\cdot28+3\cdot11+5=27\pmod{29},
$$


matching the supplied receipt.

For $G=57$, one has $z=28,R=1$, $C\equiv7,E\equiv15$. Thus


$$
\lambda_{28}\mathscr T_1
=14(7^2+16^2)=7\pmod{29},
$$


again matching the supplied receipt.

These checks illustrate the shifted and higher-tail formulas; their proof is Theorem 1.

---

## 6. An equivalent formula retaining every higher digit

The finite sums in Theorem 1 can be evaluated by a particularly transparent polynomial product.

For $0\le m<p$, define


$$
\Pi_m(x)=\sum_{j=0}^{m}\binom mj^2x^j
\quad\text{in }\mathbb F_p[x].
\tag{6.1}
$$


Let $\theta=x\,d/dx$.

Write the **complete** base-$p$ expansions


$$
C=\sum_{i=0}^{N-1}c_ip^i,\qquad
E=\sum_{i=0}^{N-1}e_ip^i,
$$


choosing $p^N>\max(C,E,R)$. Put


$$
c=c_0,\qquad f=p-1-e_0.
$$



Lucas/Kummer factorization gives, through degree $R$,


$$
\sum_{L\ge0}\mathscr T_L(C,E)x^L
=
\prod_{i=0}^{N-1}
\Pi_{c_i}(x^{p^i})\Pi_{p-1-e_i}(x^{p^i})
\quad\text{in }\mathbb F_p[[x]].
\tag{6.2}
$$


More globally, the right side is multiplied by $1/(1-x^{p^N})$; that factor has no effect through degree $R<p^N$.

To verify the second-binomial factor, a nonzero term requires no carry in $E+\ell$, and then


$$
\binom{e_i+\ell_i}{\ell_i}^2
=
\binom{p-1-e_i}{\ell_i}^2\pmod p.
$$


The omitted higher zero digits of $E$ contribute the exact telescoping product


$$
\prod_{i\ge N}\Pi_{p-1}(x^{p^i})
=\frac1{1-x^{p^N}}.
$$


Thus the terminal contribution is accounted for rather than discarded.

Only the lowest digit factors contribute to differentiation in characteristic $p$. Define


$$
\begin{aligned}
\Lambda_z(x)={}&
(a_0+a_1x)\Pi_c(x)\Pi_f(x)\\
&+(b_0+b_1x)
\left((\theta\Pi_c)\Pi_f-\Pi_c(\theta\Pi_f)\right).
\end{aligned}
\tag{6.3}
$$



### Corollary 2 — full-digit scalar product

With the coefficients from Section 5,


$$
\boxed{
\frac{\mathcal T}{p^3}
\equiv
[x^R]\,
\Lambda_z(x)
\prod_{i=1}^{N-1}
\Pi_{c_i}(x^{p^i})\Pi_{p-1-e_i}(x^{p^i})
\pmod p.
}
\tag{6.4}
$$



The factor $x$ multiplying the $\sigma=1$ coefficients is precisely the endpoint shift $R-1$. The digits $e_i$ are those of the complete integer $2C+1$, including all its carries.

The seed degree is at most $43$. This produces a small scalar initialization, but the remaining product still depends on the actual complete higher word.

---

## 7. What this proves for the actual norm—and what it does not

Let


$$
\Phi_z(R)
$$


denote the right side of (4.3), equivalently (6.4). The accepted actual reconstruction now gives the fully evaluated reduction


$$
\boxed{
D/p^3\equiv5C_n^2\Phi_z(R)\pmod p.
}
\tag{7.1}
$$


Moreover,


$$
\boxed{
M/p^3\equiv\rho_n\,5C_n^2\Phi_z(R)\pmod p.
}
\tag{7.2}
$$



Therefore:

- If $\Phi_z(R)\ne0$ at an actual index, then
  

$$
v_p(D)=v_p(M)=3.
$$


- If $\Phi_z(R)=0$, then
  

$$
v_p(D),v_p(M)\ge4.
$$


  No deeper relative valuation follows from these formulas.

### A concrete warning supplied by the new functional

At $z=9$,


$$
C=2001R+668,\qquad C\equiv1,\qquad E\equiv3,
$$


and


$$
\Phi_9(R)=7\mathscr T_R(C,E)\pmod p.
\tag{7.3}
$$


If $R\equiv28\pmod p$, a unit summand would require


$$
u_0\le1,\qquad \ell_0\le25,
$$


where $u+\ell=R$. But


$$
u_0+\ell_0\le26<28.
$$


Thus every summand is divisible by $p$, and


$$
\Phi_9(R)=0.
\tag{7.4}
$$



By the accepted original-parameter lifting bijection, the finite condition


$$
H\equiv20+29\cdot9+29^2\cdot28\pmod{29^3}
$$


is attained on a nonempty original $t$-class, with infinitely many nonnegative representatives.

So even the particularly simple nonzero seed $7$ is followed by an originally reachable annihilating tail. A nonzero initializer cannot be promoted to an original norm unit.

---

## 8. An exact all-depth classification of auxiliary common content

The next result is not a classification of the actual Gram pair. It is an exact classification of the common content of the auxiliary binomial column, applicable to every original index without any fixed carry budget.

Define


$$
\kappa_X(A,H)=\min_{0\le k\le H}v_p(X_k).
\tag{8.1}
$$



### Theorem 3 — eight-state minimum-carry recurrence

Process the digits of $A,H,2A$ from low to high. Use states


$$
(\sigma,\beta,\gamma)\in\{0,1\}^3,
$$


initialized at $(0,0,0)$, with initial cost zero.

For given input digits $a_i,\eta_i,c_i$, choose $k_i\in\{0,\ldots,p-1\}$, and determine $\ell_i,\sigma'$ by


$$
k_i+\ell_i+\sigma=\eta_i+p\sigma',
\qquad 0\le\ell_i<p.
$$


Determine $\beta',r_i,\gamma',s_i$ by


$$
r_i=a_i-k_i-\beta+p\beta',
\qquad 0\le r_i<p,
$$




$$
s_i=c_i+\ell_i+\gamma-p\gamma',
\qquad 0\le s_i<p.
$$


Assign this transition cost


$$
\beta'+\gamma'.
\tag{8.2}
$$


At each next state retain the minimum total cost over all incoming transitions.

Process the complete inputs, append the safe zero-digit drain, and accept only


$$
\sigma=\beta=\gamma=0.
$$


Then the terminal minimum is exactly


$$
\boxed{\kappa_X(A,H).}
\tag{8.3}
$$



#### Proof

Every terminal path corresponds uniquely to integers


$$
k+\ell=H,\qquad r=A-k,\qquad s=2A+\ell,
$$


with $k,\ell,r,s\ge0$. Thus it corresponds exactly to $0\le k\le H$; here $A>H$.

Kummer’s formula, or the digit-sum form of Legendre’s formula, gives


$$
v_p\binom Ak=\sum_i\beta_{i+1},
$$




$$
v_p\binom{2A+\ell}{\ell}=\sum_i\gamma_{i+1}.
$$


Therefore the total path cost is $v_p(X_k)$. Minimization gives (8.3).

The terminal sum carry rejects $k>H$. The borrow and addition carries are drained and checked, rather than ignored. There is no upper bound imposed on the accumulated valuation. ∎

This is classical carry arithmetic used as an exact minimum-content recurrence, not a claim of new general automaticity theory.

### Explicit bridge from the original growing digit strings

On the preferred original cylinder,


$$
H=\frac{3^a-b_*}{p^5}.
$$


For every $m\ge1$,


$$
\boxed{
H\bmod p^m
=
\frac{(3^a\bmod p^{m+5})-b_*}{p^5}.
}
\tag{8.4}
$$


The division is exact, and the quotient is the least residue modulo $p^m$.

Once $p^{m+5}>3^a$, this formula returns the complete integer $H$, not just a prefix. For example, $m=a$ is a crude finite bound because $p>3$.

The digits of $A=2001H+67$ can then be generated exactly by


$$
a_i\equiv2001\eta_i+\xi_i\pmod p,
\qquad
\xi_{i+1}=\left\lfloor\frac{2001\eta_i+\xi_i}{p}\right\rfloor,
\qquad \xi_0=67,
$$


and those of $2A$ by the ordinary doubling carry. The multiplier carry lies in the fixed range $0\le\xi_i\le2000$.

Thus Theorem 3 classifies $\kappa_X$ at every original $t$ after processing its actual complete finite string. It requires neither an assumed infinite pattern nor a substitution of an auxiliary $H$ for the original one.

It does **not** yet classify $v_p(D)$, because $D$ includes actual reconstruction corrections and scalar cancellation.

---

## 9. Arbitrarily deep auxiliary content is compatible with original reachability

The accepted depth-two refinement argument iterates at the auxiliary level.

### Theorem 4 — arbitrary auxiliary content refinements

Fix a finite original congruence refinement inside an accepted population cylinder. For every integer $r\ge1$, there is a further nonempty original congruence refinement on which


$$
\kappa_X(A,H)\ge r.
\tag{9.1}
$$


There are also refinements on which the whole high column


$$
F(J)=\binom NJ\binom{2N+h-J}{h-J},
\qquad 0\le J\le h,
$$


has arbitrarily large common $p$-content.

#### Proof

Suppose the current refinement fixes $H\bmod p^m$. Since


$$
A=p(69H)+67
$$


on the preferred cylinder, the digit $A_{m+1}$ depends affinely on the free digit $H_m$, with coefficient $69\equiv11\pmod p$.

Choose $H_m$ so that


$$
A_{m+1}=2,
$$


then choose


$$
H_{m+1}=28.
$$


At this digit the digit of $2A$ is $4$ or $5$.

For any $k+\ell=H$, absence of an outgoing borrow in $A-k$ would require $k_{m+1}\le2$. Absence of an outgoing carry in $2A+\ell$ would require $\ell_{m+1}\le24$. Even allowing the incoming sum carry,


$$
k_{m+1}+\ell_{m+1}+\sigma\le27,
$$


which cannot produce the digit $28$ of $H$.

Thus every $X_k$ acquires a carry at this new position. Repeating at distinct higher positions forces any prescribed number of carries.

For $F(J)$, the corresponding digit is shifted by one:


$$
N=3+pA,\qquad h=d+pH,\qquad 2N=6+p(2A).
$$


The same blocking argument applies at those shifted positions.

Finally, each construction prescribes only finitely many additional digits. The accepted LTE bijection transfers each such finite prescription to a nonempty original $t$-class. ∎

### The quantifiers matter

This proves


$$
\text{for every }r,\ \text{there are original indices with content at least }r.
$$


It does not produce one finite original index with infinite content. Nor does a compatible infinite digit prescription have to correspond to a nonnegative integer $t$, rather than merely a $29$-adic parameter.

### Why this does not prove arbitrary actual-column content

The retained natural representations are only


$$
P_{LJ+x}\equiv(-1)^{j+1}F(J)P_x(J)\pmod{p^3},
$$




$$
Q_{LJ+x}\equiv(-1)^{j+1}F(J)Q_x(J)\pmod{p^3}.
$$


Consequently, $p^r\mid F(J)$ implies from this interface only


$$
P,Q\in p^{\min(r,3)}\mathbb Z_p^{b+1}.
\tag{9.2}
$$


The unspecified errors modulo $p^3$ cannot be credited with an additional factor.

An all-depth actual-column factorization would need a new proof with the full force and boundary retained at its varying precision. Repeated auxiliary blockers alone do not provide that proof.

---

## 10. Common content is not the full norm valuation

Suppose the actual columns have common content at least $c$, and write


$$
P=p^c x,\qquad Q=p^c y.
$$


If $c$ is the exact content of $P$, then $x$ is primitive over $\mathbb Z_p$. Put


$$
\nu=v_p(x^Tx),\qquad
\eta=y-\rho_nx.
$$


Then


$$
\boxed{
v_p(D)=2c+\nu,
}
\tag{10.1}
$$


and


$$
\boxed{
v_p(M-\rho_nD)=2c+v_p(x^T\eta).
}
\tag{10.2}
$$



Thus full relative alignment requires control of


$$
v_p(x^T\eta)
$$


against the **primitive norm valuation** $\nu$, not merely against the removed column content $c$.

### A rigorous obstruction to content-only reasoning

Since $12^2\equiv-1\pmod{29}$, Hensel lifting gives, for every $s\ge1$, an integer $u$ with


$$
v_p(1+u^2)=s.
$$


Fix $r<s$, and take integer vectors


$$
P=p^c(1,u),\qquad
Q=P+p^{c+r}(1,0).
$$


Then


$$
D=p^{2c}(1+u^2)>0,
$$


but


$$
M=D+p^{2c+r}.
$$


Therefore


$$
v_p(D)=2c+s,\qquad
v_p(M)=2c+r,
$$


so


$$
v_p(D)-v_p(M)=s-r
$$


is arbitrarily large.

These are not claimed to be members of the actual family. They prove the logical obstruction: positivity, exact common content, and any fixed number of digits of column alignment do not imply a bounded relative norm/mixed valuation.

### Precision required by a deep actual norm

If $P,Q\in p^c\mathbb Z_p^{b+1}$, and both columns are known modulo $p^N$, with $N\ge c$, their scalar products are determined modulo


$$
p^{N+c}.
$$


To decide a defect at depth $v_p(D)+1$, the column precision must therefore reach at least


$$
\boxed{
N\ge v_p(D)-c+1.
}
\tag{10.3}
$$


A fixed absolute-precision reconstruction cannot handle arbitrarily deep primitive-norm cancellation without an additional structural identity.

---

## 11. A concrete all-depth follow-on lemma

The finite-depth result has a useful blockwise formulation.

For each actual high block $J$, let


$$
I_J=
\begin{cases}
\{0,\ldots,L-1\},&0\le J<h,\\
\{0,\ldots,b_*\},&J=h,
\end{cases}
$$


and define the complete actual block contractions


$$
d_J=\sum_{x\in I_J}P_{LJ+x}^2,
$$




$$
e_J=\sum_{x\in I_J}
P_{LJ+x}\bigl(Q_{LJ+x}-\rho_nP_{LJ+x}\bigr).
\tag{11.1}
$$


Then


$$
D=\sum_{J=0}^{h}d_J,\qquad
M-\rho_nD=\sum_{J=0}^{h}e_J.
$$



The accepted ordinary-polynomial defect identity and the whole-column $p$-content imply, block by block,


$$
\boxed{
e_J\equiv p\lambda_n d_J\pmod{p^4},
\qquad
\lambda_n=\frac{27C_n+20J_{29}}{C_n^2}\pmod p.
}
\tag{11.2}
$$


Indeed, the leading norm density is $C_n^2F(J)^2K_d(J)$, while the leading defect density is


$$
p(27C_n+20J_{29})F(J)^2K_d(J).
$$


The actual-column representation errors contribute only modulo $p^4$. At the last block, the proved $h-J$ factors justify the same calculation with the actual shorter range.

Equation (11.2) is still an absolute-precision statement.

### Proposed all-depth relative-contraction lemma — open

Construct, directly from the complete finite reconstruction, a $J$-independent


$$
\alpha_n\in p\mathbb Z_p
$$


and finite currents $\mathcal B_J$ satisfying


$$
\boxed{
e_J=\alpha_n d_J+\mathcal B_{J+1}-\mathcal B_J
\qquad(0\le J\le h),
}
\tag{11.3}
$$


with the actual boundary conditions


$$
\boxed{\mathcal B_0=\mathcal B_{h+1}=0.}
\tag{11.4}
$$


A construction should begin compatibly with (11.2), and must not define $\alpha_n$ retrospectively by dividing by $D$.

The complete exponential/contact forcing, factorial boundary, logarithmic forcing and exterior endpoint must all enter the identity. An interior telescoping identity without (11.4) would not suffice.

### Proposition 5 — why this target solves the all-depth local problem

If (11.3)–(11.4) hold, then


$$
M-\rho_nD=\alpha_nD.
$$


Hence


$$
\boxed{
v_p(M-\rho_nD)\ge v_p(D)+1,
\qquad
v_p(M)=v_p(D).
}
\tag{11.5}
$$



#### Proof

Sum (11.3) over the actual finite range $0\le J\le h$. The current telescopes to zero by (11.4). Since $\alpha_n\in p\mathbb Z_p$ and $\rho_n$ is a unit,


$$
M=(\rho_n+\alpha_n)D
$$


has the same valuation as $D$. ∎

This is an all-depth target: common content and primitive-norm cancellation are both carried by the same complete factor $D$. It does not require certifying an exact norm depth on a finite cylinder.

**What is proved here is the criterion and its available blockwise initial congruence. The required all-depth current and scalar have not been constructed.** The initializer supplies no mixed-defect data capable of establishing them.

---

## 12. Full gcd, actual primitive denominator, and whole error

Retain the actual least two-column denominator


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0.
$$


With the falling metric,


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The final gcd and primitive pair are


$$
g_B=\gcd(A_B,|H_B|),
$$




$$
p_n=H_B/g_B,\qquad q_n=A_B/g_B>0.
\tag{12.1}
$$



No auxiliary common content replaces this full gcd.

Let


$$
F_n=v_{29}(n!),\qquad F_b=v_{29}(b!),
$$




$$
\delta=v_{29}(D),\qquad \mu=v_{29}(M).
$$


The exact retained interface is


$$
\boxed{
v_{29}(g_B)
=
\min\{4F_n+4+\delta,\;2F_n+F_b+5+\mu\},
}
\tag{12.2}
$$




$$
\boxed{
v_{29}(q_n)
=
\max\{0,\;2F_n-F_b-1+\delta-\mu\}.
}
\tag{12.3}
$$



If the new scalar $\Phi_z(R)$ is nonzero at an actual index, then $\delta=\mu=3$, giving


$$
v_{29}(q_n)=\max\{0,2F_n-F_b-1\}.
$$


If it vanishes, $\delta-\mu$ remains unresolved. If the proposed all-depth relative-contraction lemma were proved, it would give $\delta-\mu=0$ at every index in its scope—but still only settle the local $29$-part.

Across all primes,


$$
\log q_n
=
\sum_{\ell}
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell,
\tag{12.4}
$$


with the usual convention when $H_B=0$. A local $29$-adic theorem does not evaluate this sum.

For the complete real error,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the whole evaluated form remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{12.5}
$$


At the retained hypotheses and proof status of the supplied signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
\tag{12.6}
$$



Norm nonvanishing follows from the supplied nonzero first column and positivity. Mixed nonvanishing retains its original-family dependency; no vanishing residue proves a vanishing integer mixed product. Eventual nonvanishing of the whole form retains the complete signed-error theorem’s status.

For this approach to prove irrationality, one needs an infinite sequence of original indices on which the complete nonzero form (12.5) tends to zero. A sufficient denominator estimate would be


$$
\limsup \frac{\log q_n}{n}
<
\left(2+\frac1{2001}\right)\log(1+\sqrt2)
$$


along that same sequence. No such all-prime estimate is proved here.

---

## 13. Bounded exact arithmetic that is now useful

### No duplicate initializer is needed

The supplied initializer and the 33 complete auxiliary comparisons are accepted at their stated scope. No rerun is required for the proofs above.

### Optional new compression certificate

A genuinely different, small calculation would certify the scalar seeds $\Lambda_z(x)$ in (6.3).

**Inputs**

- The coefficient tables (5.1) and (5.4).
- For each $z=0,\ldots,28$,
  

$$
c=(11z+18)\bmod29,\qquad
  e=(2c+1)\bmod29,\qquad f=28-e.
$$


- The polynomials
  

$$
\Pi_m(x)=\sum_{j=0}^{m}\binom mj^2x^j
$$


  over $\mathbb F_{29}$, and the ordinary operator $\theta=x\,d/dx$.

**Expected verifiable output**

For every $z$:

1. The coefficients of $\Lambda_z(x)$, of degree at most $43$.
2. Verification of (6.3).
3. For $9\le z\le28$, the exact polynomial identity
   

$$
\Lambda_z(x)=\lambda_z\Pi_c(x)\Pi_f(x).
$$


4. For $0\le z\le8$, verification that $b_1=-b_0$, giving the factor $1-x$ in the centered-moment part.

This requires at most $29\cdot44=1276$ returned field coefficients and only small polynomial arithmetic. It does not reconstruct any large column, rerun the 406-entry initializer, or claim original infinite reachability.

No finite coefficient calculation currently specified can certify the missing all-depth identity (11.3). That remains a mathematical proof obligation, not a request to sample deeper norms.

---

# Conclusion and proof-status ledger

## New established results

Using the accepted recurrence and the supplied exact initializer:

1. **Complete scalar compression**
   

$$
\mathcal T/29^3
$$


   is given by the two-tail functional (4.3), with every coefficient explicitly evaluated.

2. **Twenty single-convolution reductions**
   

$$
\mathcal T/29^3
   \equiv\lambda_z\mathscr T_R(C,2C+1)\pmod{29},
   \qquad 9\le z\le28,
$$


   with every $\lambda_z$ a unit.

3. **Full-digit polynomial formula**
   The whole higher-tail functional is the coefficient extraction (6.4), including the $R-1$ shift and every digit of $2C+1$.

4. **All-depth auxiliary content classification**
   The eight-state minimum-carry recurrence computes the exact common $29$-content of $(X_k)$ for every actual original index. Equation (8.4) supplies an explicit bridge from the original power $3^a$ to the complete input word.

5. **Arbitrarily deep auxiliary refinements**
   Every finite population cylinder has originally reachable refinements with arbitrarily deep auxiliary common content. This is not an all-depth actual-column factorization.

6. **Precise all-depth local target**
   The finite-boundary telescoping criterion (11.3)–(11.4), if constructed for the actual complete columns, would prove
   

$$
v_{29}(M-\rho_nD)\ge v_{29}(D)+1
$$


   at arbitrary norm depth.

## Exact remaining bottleneck

The initializer is no longer missing. Nor is the normalized higher-tail scalar.

The unresolved local problem is now:

> Control the actual mixed defect relative to the **full actual norm**, after both common column content and any additional primitive-norm cancellation, on the complete original growing digit strings.

The new scalar decides the depth-three norm digit, but a zero leaves this all-depth problem open. The auxiliary minimum-content classification does not bridge through the unavailable all-depth actual reconstruction.

Separate obligations remain:

- nonvanishing at the retained original-family scope;
- the **full final gcd** across all primes;
- a bound for the **actual primitive denominator** $q_n$;
- comparison with the **whole evaluated error** $-q_n\epsilon_n$ on the same original indices.

Accordingly, this report advances the higher-tail reduction and makes the deeper-content obstruction explicit. It does **not** supply an unconditional proof or disproof of irrationality of $e+\pi$.
