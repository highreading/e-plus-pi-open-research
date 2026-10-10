> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 6 — Content-relative cancellation in the Newton kernel model, and the precise obstruction to transferring it to the actual norm

## Executive summary

The new certificates have two different scopes.

1. The complete safe-period mixed table, combined with the established scalar reduction and its force and endpoint bounds, proves
   

$$
\boxed{H-N\in128\mathbb Z_2}
$$


   on every original index.

2. The sixteen all-digit computations prove the stated minimum kernel costs at exactly $u=0,\ldots,15$. They do not establish eventual growth. In particular, kernel content must not be identified with coordinate content of the actual columns.

The principal new result below is an **all-depth, content-relative cancellation theorem for the integer polynomial contraction furnished by the Newton certificate**. It uses the actual higher kernel, not a congruent auxiliary index.

Let


$$
\mathcal B_t=\binom Ct\binom{2C+D-t}{D-t},\qquad
\mu=\min_{0\le t\le D}v_2(\mathcal B_t),
$$


and let $S(C,D)$ be the integer contraction obtained from the supplied Newton polynomial, with the shortened terminal coefficient retained. Then, for every odd positive $D$ and $C=4002D+2532$,


$$
\boxed{S(C,D)\in 2^{2\mu+2}\mathbb Z.}
$$


More precisely, if


$$
M=\#\{\,0\le t\le D:\ v_2(\mathcal B_t)=\mu\,\},
\qquad \xi=\frac{D-1}{2},
$$


then


$$
\boxed{
\frac{S(C,D)}{2^{2\mu+2}}\equiv \xi M\pmod2.
}
\tag{E1}
$$



This is cancellation **after stripping the exact kernel content**. Its proof pairs each even index with the following odd index and includes $t=D$. It is neither another fixed-alignment assertion nor an arbitrary-vector obstruction.

However, the established relation to the actual norm is only


$$
\boxed{N=2S(C,D)+256R_u,\qquad R_u\in\mathbb Z_2.}
\tag{E2}
$$


At all sixteen certified original indices, $\mu\ge7$. Thus the newly identified kernel-model cancellation lies well above the precision at which $R_u$ is controlled. Dividing the old congruence by the kernel content would be invalid.

I also give an exact terminating hypergeometric representation of $S$, including its terminal correction. It supplies a mathematically distinct summation route, but is not an all-depth formula for the complete actual columns.

**No unconditional proof or disproof of irrationality of $e+\pi$ follows.**

---

## 1. Original domain and source audit

Throughout,


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


and


$$
D=D_u=\frac{9^{18+32u}-81}{128},\qquad
C=4002D+2532.
$$


Thus $D$ is odd and $C\equiv2\pmod4$.

The actual finite inverse indices remain


$$
0\le i,j<b,
$$


while the scalar coordinates remain


$$
0\le j\le b.
$$


The interior decomposition consists of


$$
0\le t<D,\quad 0\le\rho<128,
$$


and the shortened final block


$$
t=D,\quad 0\le\rho\le80.
$$


The exterior coordinate $j=b=128D+81$ is separate.

Retain


$$
X=\frac{Z_w}{2R},\qquad
Y=\frac{V_w}{4b!},\qquad
N=X^TX>0,\qquad H=X^TY\ne0.
$$



### 1.1 What is accepted from the certificates

The safe separate period $1024$, not the withdrawn proof of separate period $512$, justifies transfer of the exhaustive low-state tables. The new exhaustive checks also verify separate half-periods for these evaluated coefficient functions; that is a new finite-table conclusion, not a repair of the old incorrect proof.

The complete mixed table therefore gives, through the established scalar interface,


$$
8(H-N)\equiv0\pmod{1024}.
$$


Hence


$$
\boxed{H-N\equiv0\pmod{128}}
\tag{1.1}
$$


on the entire original family.

The minimum costs


$$
7,17,26,32,53,69,96,96,99,119,130,153,157,190,201,206
$$


are accepted as finite exact computations on the stated sixteen actual indices. Their algorithm minimizes over the complete original interval $0\le t\le D_u$.

The complete force estimates and exterior bounds remain valid only at their proved precisions. In particular, the exterior formulas remain


$$
X_b=\frac{W_b\,b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4}.
\tag{1.2}
$$


The $+1$ is not discarded in any proposed all-depth identity.

No tools or external sources have been accessed for this report.

---

## 2. The integer Newton contraction

To avoid confusing the original index $u$ with the Newton variable, put


$$
\xi=\frac{D-1}{2}.
$$


Define the integer-valued polynomial


$$
P_D(t)=
\sum_{i=0}^{3}\sum_{j=0}^{4}
c_{ij}\binom{\xi}{i}\binom tj,
$$


where


$$
(c_{ij})=
\begin{pmatrix}
44&95&70&96&64\\
52&76&80&0&0\\
24&32&64&0&0\\
64&0&0&0&0
\end{pmatrix},
$$


and define


$$
Q_D=11+120\xi+32\binom{\xi}{2}.
$$



Use these displayed integer representatives to define


$$
\boxed{
S(C,D)=
\sum_{t=0}^{D-1}\mathcal B_t^2P_D(t)
+\mathcal B_D^2Q_D.
}
\tag{2.1}
$$


This is an exact integer, not merely a residue class.

The certificate and scalar interface imply


$$
4N\equiv8S(C,D)\pmod{1024},
$$


so


$$
\boxed{N\equiv2S(C,D)\pmod{256}.}
\tag{2.2}
$$



Equation (2.1) is an exact definition of a kernel model. Equation (2.2), and not an equality $N=2S$, is its established relationship to the actual norm.

---

## 3. Adjacent kernel costs: every minimum occurs at an even index

Write


$$
e_t=v_2(\mathcal B_t).
$$



The exact adjacent recurrence is


$$
t(2C+D-t+1)\mathcal B_t
=(C-t+1)(D-t+1)\mathcal B_{t-1},
\qquad 1\le t\le D.
\tag{3.1}
$$



### Lemma 1 — Odd-index cost increment

For every odd $t\in[1,D]$,


$$
\boxed{e_t-e_{t-1}=v_2(C-t+1)\ge1.}
\tag{3.2}
$$



#### Proof

For odd $t$, the three numbers


$$
t,\qquad D-t+1,\qquad 2C+D-t+1
$$


are odd. Taking valuations in (3.1) leaves exactly


$$
e_t-e_{t-1}=v_2(C-t+1).
$$


Since $C$ is even, $C-t+1$ is even. ∎

Consequently,


$$
\boxed{
\mu=\min_{\substack{0\le t<D\\t\ \mathrm{even}}}e_t.
}
\tag{3.3}
$$


In particular, the terminal index $D$, which is odd, is never a minimizing index.

Writing $t=2k+1$, the increment is


$$
h_k=v_2(C-2k).
$$


Because $C\equiv2\pmod4$,


$$
\boxed{
h_k=
\begin{cases}
1,&k\ \text{even},\\
\ge2,&k\ \text{odd}.
\end{cases}}
\tag{3.4}
$$



This is a relation between neighboring admissible paths in the **actual kernel**, not a statement about arbitrary carry systems.

---

## 4. Content-relative scalar cancellation, including the terminal block

### Theorem 2 — Two forced normalized bits and the next exact bit

For $D$ odd and $C=4002D+2532$, let $S,\mu,M,\xi$ be as above. Then


$$
S\in2^{2\mu+2}\mathbb Z,
$$


and


$$
\boxed{
S/2^{2\mu+2}\equiv \xi M\pmod2.
}
\tag{4.1}
$$



#### Proof

First reduce the supplied polynomial coefficients modulo $4$:


$$
P_D(t)\equiv3t+2\binom t2
=t(t+2)\pmod4.
\tag{4.2}
$$


Thus $P_D(t)$ is divisible by $4$ for even $t$, and is odd for odd $t$. Also


$$
Q_D\equiv3\pmod4.
\tag{4.3}
$$



Every even-index summand in $S$ is consequently divisible by $2^{2\mu+2}$. Every odd index has $e_t\ge\mu+1$, by Lemma 1, so its squared kernel supplies the same divisibility, including at the endpoint. This proves the first assertion.

For the next bit, reduction modulo $8$ gives


$$
P_D(t)\equiv
4+7t+6\binom t2+4\xi(1+t)\pmod8.
\tag{4.4}
$$


At $t=2k$,


$$
P_D(2k)\equiv4(1+k+\xi)\pmod8.
\tag{4.5}
$$



Pair the indices


$$
(2k,2k+1),\qquad 0\le k\le(D-1)/2.
$$


For the final pair, the odd coefficient is $Q_D$, not $P_D(D)$. Both are odd, which is all that is needed for this bit.

If $e_{2k}>\mu$, the even term vanishes after division by $2^{2\mu+2}$ and reduction modulo $2$; its odd partner vanishes as well.

Suppose $e_{2k}=\mu$. The normalized kernel $\mathcal B_{2k}/2^\mu$ is odd, so its square is $1\pmod2$. The even contribution is


$$
1+k+\xi\pmod2.
$$


The odd partner contributes $1$ precisely when


$$
e_{2k+1}=\mu+1,
$$


and contributes $0$ otherwise. By (3.4), that additional contribution is $1$ precisely when $k$ is even.

Thus each minimizing pair contributes


$$
1+k+\xi+\mathbf1_{k\text{ even}}
\equiv\xi\pmod2.
$$


There are $M$ minimizing pairs, because all minima occur at even indices. Summing proves (4.1). ∎

### Consequences

If $\xi M$ is odd, the model valuation is determined exactly:


$$
\boxed{v_2(S)=2\mu+2.}
\tag{4.6}
$$


If $\xi M$ is even,


$$
\boxed{v_2(S)\ge2\mu+3.}
\tag{4.7}
$$



The theorem does not need growth of $\mu$, a digital sparsity theorem, or evaluation of the enormous full sum.

It is also stable under changing $P_D(t)$ and $Q_D$ by multiples of $128$: such changes alter $S$ by a multiple of $2^{2\mu+7}$, beyond the bits considered here.

---

## 5. Exact hypergeometric summation of the Newton model

The polynomial compression permits an exact finite special-function representation.

Put


$$
a_j(D)=\sum_{i=0}^{3}c_{ij}\binom{\xi}{i},
\qquad
F_j(C,D)=\sum_{t=0}^{D}\binom tj\mathcal B_t^2.
$$


For $0\le j\le\min(4,D)$,


$$
\boxed{
F_j(C,D)=\mathcal B_j^2
\,{}_4F_3\!\left(
\begin{matrix}
j-C,\ j-C,\ j-D,\ j-D\\
j-2C-D,\ j-2C-D,\ j+1
\end{matrix};1
\right),
}
\tag{5.1}
$$


where the series is explicitly truncated at $s=D-j$.

### Derivation

For $0\le s\le D-j$,


$$
\frac{\mathcal B_{j+s}}{\mathcal B_j}
=
\frac{(j-C)_s(j-D)_s}
     {(j+1)_s(j-2C-D)_s}.
$$


Also


$$
\binom{j+s}{j}=\frac{(j+1)_s}{s!}.
$$


Squaring the first identity and multiplying by the second gives exactly the $s$-th term in (5.1).

No denominator in this finite range vanishes: the potential zero in
$(j-2C-D)_s$ occurs beyond the termination point. ∎

Hence


$$
\boxed{
S(C,D)=
\sum_{j=0}^{\min(4,D)}a_j(D)F_j(C,D)
+\binom CD^2\bigl(Q_D-P_D(D)\bigr).
}
\tag{5.2}
$$



The final correction is mandatory. It replaces the artificial full terminal coefficient by the actual shortened coefficient of the model.

Equation (5.2) is an exact summation identity, but not a claimed classical closed-product evaluation. Nor does it restore the omitted higher force terms. Its useful role is to place the certified polynomial model into a finite-dimensional family of exact terminating sums, where contiguous relations or creative telescoping can be investigated without losing the finite boundary.

---

## 6. The decisive scoped obstruction: absolute precision cannot be divided by content

Combining Theorem 2 with (2.2) gives the exact decomposition


$$
\boxed{
N=2S(C,D)+256R_u,\qquad R_u\in\mathbb Z_2.
}
\tag{6.1}
$$


Here $R_u$ is the actual residual. It contains everything not determined by the proved raw precision, including any relevant higher reconstruction terms, force tails and exterior contribution.

The model term satisfies


$$
v_2(2S)\ge2\mu+3.
\tag{6.2}
$$



### Proposition 3 — Information supplied at the sixteen certified indices

At each certified original index $u=0,\ldots,15$,


$$
\boxed{N\in256\mathbb Z_2,\qquad H\in128\mathbb Z_2.}
\tag{6.3}
$$


The established scalar interfaces do not determine the first nonzero bit of $N$, $H$, or $H/N$ at those indices.

#### Proof

Each certified $\mu$ is at least $7$, so $2S\in2^{17}\mathbb Z$. Equation (6.1) gives $N\in256\mathbb Z_2$. Equation (1.1) then gives $H\in128\mathbb Z_2$.

The term $256R_u$ is not controlled beyond integrality by the supplied scalar interface. It can therefore occur below the content-relative model scale. ∎

The last assertion is a statement about what the established interface determines, not an assertion that the actual residual is arbitrary.

### Exact precision required for transfer

To transfer the parity in Theorem 2 to


$$
N/2^{2\mu+3}\pmod2,
$$


it would suffice to prove


$$
v_2(256R_u)\ge2\mu+4,
$$


or equivalently


$$
\boxed{v_2(R_u)\ge2\mu-4.}
\tag{6.4}
$$



Merely proving that $N$ is divisible by $2^{2\mu+3}$ through (6.1) would require


$$
v_2(R_u)\ge2\mu-5.
$$



At $u=0$, where $\mu=7$, the parity-transfer target already requires $R_0\in2^{10}\mathbb Z_2$. The present interface supplies only $R_0\in\mathbb Z_2$.

Thus:

> **An exact summation of the Newton model, however successful, does not by itself lift the actual norm beyond the established absolute precision. The missing theorem is a content-relative bound for the complete residual.**

This is the scoped impossibility result relevant to the new certificates. It does not rule out such a residual theorem.

---

## 7. Why the digital-expansion route is not yet a substitute

The exact kernel valuation is


$$
\begin{aligned}
e_t={}&s_2(t)+s_2(C-t)-s_2(C)\\
&+s_2(D-t)+s_2(2C)-s_2(2C+D-t).
\end{aligned}
\tag{7.1}
$$


Since $s_2(2C)=s_2(C)$, this simplifies to


$$
\boxed{
e_t=s_2(t)+s_2(C-t)+s_2(D-t)-s_2(2C+D-t).
}
\tag{7.2}
$$



A lower bound on the number of nonzero digits of $D_u$ does not directly lower-bound the minimum of (7.2). The final digit sum is subtracted, and $t$ is optimized over the whole interval. The missing bridge must control these simultaneous digit patterns.

Lemma 1 provides a genuine, but limited, bridge: it removes all odd $t$ from the minimization and quantifies their extra cost. It does not bound the minimum cost of the remaining even paths in terms of the digit count or run complexity of $D_u$.

No Stewart-type or S-unit result supplied in the packet has the exact hypothesis and conclusion needed to fill that gap. Accordingly, no such theorem is invoked here.

Moreover, even a future proof that $\mu(D_u)\to\infty$ would not alone control $R_u$ in (6.1). Kernel-content growth and complete-column cancellation are separate obligations.

---

## 8. A distinct next route: lift the paired contraction with its residual

The useful next lemma is now more specific than another alignment congruence.

> **Complete content-relative norm-lift lemma.**  
> On the original family, prove
> 

$$
> N-2S(C,D)\in2^{2\mu+4}\mathbb Z_2,
> \tag{8.1}
>
$$


> by reconstructing the complete actual columns at that precision, with all finite boundaries, the full logarithmic force, every relevant factorial-tail term and the exterior $+1$ retained.

If established, it would yield


$$
\frac{N}{2^{2\mu+3}}\equiv \xi M\pmod2.
\tag{8.2}
$$


Where $\xi M$ is odd, it would determine


$$
\alpha=2\mu+3.
$$



A corresponding complete mixed-contraction identity would still be needed to determine $\gamma-\alpha$. A norm theorem alone does not settle relative cancellation.

There are two concrete structural ways to attempt (8.1):

* reconstruct a full higher-precision block coefficient expansion and prove that its correction has additional content-relative divisibility;
* derive a finite-operator bilinear identity whose boundary terms reproduce the correction in (5.2) and whose remainder can be estimated before scalar normalization.

In either case, the pairing proof in §4 identifies a cancellation mechanism worth preserving. The objective is not simply a larger table: it is a divisibility statement for the **whole residual relative to the actual kernel content**.

---

## 9. Primitive denominator and whole evaluated error

Retain the least actual clearer $d_B$, and set


$$
N_B=d_B[u,v].
$$


With the original metric,


$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2}.
$$


The final normalization is


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B}>0,\qquad
p_n=\frac{H_B}{g_B}.
$$


This is the full integer gcd, including every odd prime; the primitive multiplier remains $d_B^2/g_B$.

For


$$
\alpha=v_2(N),\qquad \gamma=v_2(H),\qquad
\Delta_n=\gamma-\alpha,
$$


the retained exact interface is


$$
\boxed{
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-\Delta_n
\right\}.
}
\tag{9.1}
$$



Neither the certified minimum costs nor Theorem 2 supplies $\Delta_n$. In particular, substituting $2\mu+3$ for $\alpha$ in (9.1) would be unjustified without a complete residual theorem.

The accepted whole signed error remains


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0
\quad\text{eventually},
$$


with


$$
\log|\epsilon_n|
=-\kappa n+o(n),\qquad
\kappa=\left(2+\frac1{4002}\right)\log(1+\sqrt2).
$$


Thus the entire evaluated form is


$$
\boxed{
L_n=q_n(e+\pi)-p_n=-q_n\epsilon_n>0
}
\quad\text{eventually}.
\tag{9.2}
$$



To obtain irrationality by this family, one needs a same-index argument implying $L_n\to0$, while retaining its nonvanishing. An upper bound on the full primitive denominator would be relevant. The dyadic denominator interface alone is not that upper bound.

---

## 10. Bounded exact computation: minimum-path multiplicity, not another modulus

No repeat of the sixteen minimum-cost computations is needed merely to reconfirm their values. The useful extension is to compute the parity of the number of minimizers.

### Inputs

Use exactly


$$
u=0,\ldots,15,\qquad
D_u=\frac{9^{18+32u}-81}{128},\qquad
C_u=4002D_u+2532.
$$



Augment the existing eight-state carry algorithm. At each state store:

1. the minimum accumulated cost;
2. the number of paths attaining that minimum, modulo $2$.

For a transition:

* replace the stored cost and count if a smaller cost is found;
* add counts modulo $2$ if an equal cost is found;
* ignore a larger cost.

Keep the original start state, all digit layers and the final zero-carry state. Each completed path corresponds uniquely to its $t$, since $C-t$, $D-t$ and all carries are then determined.

### Expected verifiable output

For each actual $u$, report


$$
\left(
u,\ \mu_u,\ M_u\bmod2,\ \xi_u\bmod2,\
\xi_uM_u\bmod2
\right).
$$


The previous $\mu_u$ must be reproduced. The final bit gives the rigorous model conclusion


$$
\begin{cases}
v_2(S(C_u,D_u))=2\mu_u+2,
&\xi_uM_u\text{ odd},\\
v_2(S(C_u,D_u))\ge2\mu_u+3,
&\xi_uM_u\text{ even}.
\end{cases}
$$



The calculation has eight carry states and a number of layers linear in the input bit length. It does not enumerate the original $t$-interval or construct factorials.

Its output remains a statement about these sixteen kernel models. It is not an actual norm valuation certificate without (8.1).

---

## 11. Final ledger

### New rigorous results

1. Every minimum-cost kernel index is even; the extra cost at the following odd index is exactly $v_2(C-t+1)$.
2. After stripping the exact kernel content, the Newton contraction has two forced zero bits:
   

$$
S\in2^{2\mu+2}\mathbb Z.
$$


3. Its next bit is explicitly
   

$$
S/2^{2\mu+2}\equiv ((D-1)/2)\,M\pmod2,
$$


   with the shortened terminal block retained.
4. The Newton contraction has an exact terminating ${}_4F_3$ representation with the necessary terminal correction.
5. The precise content-relative residual bound needed to transfer that bit to the actual norm is identified.

### Certificate-dependent conclusions now established

* $H-N\in128\mathbb Z_2$ for every original index.
* At the sixteen certified original indices,
  

$$
N\in256\mathbb Z_2,\qquad H\in128\mathbb Z_2.
$$



### Exact remaining bottleneck

The first unresolved transfer is


$$
\boxed{
v_2\!\bigl(N-2S(C_u,D_u)\bigr)\ge2\mu_u+4,
}
$$


or another complete actual-column identity strong enough to replace it. It must include the full force, relevant growing tails, shortened terminal block and exterior $+1$.

After that remain actual mixed cancellation, the full final gcd, and the same-index comparison between the primitive denominator and the whole evaluated error.



$$
\boxed{\text{Irrationality of }e+\pi\text{ remains unresolved.}}
$$


