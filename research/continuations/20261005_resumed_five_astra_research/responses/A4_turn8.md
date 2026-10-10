> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 8 — Audit of the all-digit certificates and their exact scalar consequences

## Executive conclusions

**Both new algorithms pass the source-level mathematical audit.** I accept the supplied computation receipts at their expressly bounded scope; I have not executed either program, recomputed the hashes, or inspected the first four binary layer arrays that are not reproduced in the packet.

The principal conclusions are:

1. **The $29$-adic initializer is a valid initialization of the complete one-carry recurrence.** The Wilson unit, signed harmonic state, divisions, and terminal conditions are correct. The 33 direct comparisons verify 33 auxiliary values of $H$, not original exponential indices.

2. **The binary dynamic program computes the exact kernel minimum over the entire finite interval $0\le t\le D$.** Its witnesses certify attainment; the minimum-cost recurrence certifies minimality. The sixteen reported values concern the actual original indices $u=0,\ldots,15$, not small congruent substitutes.

3. **The Newton compression is a complete finite-state identity, not an inference from a small interpolation sample.** The program computes candidate forward-difference coefficients and then checks the formula against all $524288$ full states and all $512$ terminal states. Its extension to actual coefficient arguments requires—and has—the appropriate periods. Its extension to actual scalars still uses the accepted raw reconstruction and finite contraction.

4. At every one of the sixteen tested actual binary indices, the present scalar interface forces
   

$$
\boxed{N\equiv0\pmod{256},\qquad H\equiv0\pmod{128}.}
$$


   In particular,
   

$$
\boxed{\alpha=v_2(N)\ge8,\qquad \gamma=v_2(H)\ge7.}
$$


   It does **not** force $\alpha=2\mu+1$, $\alpha\ge2\mu+1$, $\gamma=\alpha$, or any all-depth bound on $\gamma-\alpha$, where $\mu$ denotes kernel content.

5. I give below a **precision-dependent complete-column content lemma**. It includes all original coordinates, complete forces, finite inverse losses, the exterior $+1$, and actual least clearers. The lemma shows exactly what must be established to promote kernel content to complete-column content. The required arbitrary-precision factorization and remainder bounds are **not supplied by the current truncated representatives**.

The irrationality or rationality of $e+\pi$ remains unresolved.

---

## 1. Scope and notation

The two constructions must remain separate.

### 1.1 The $29$-adic construction

Retain


$$
a=432827+682892t,\qquad t\ge0,\qquad b=3^a,\qquad n=2001b,
$$


and the preferred cylinder


$$
t\equiv364\pmod{841}.
$$


The actual contact indices are $0\le i,j<b$; reconstructed coordinates are $0\le j\le b$.

On this cylinder,


$$
H=20+29G,\qquad A=2001H+67,
$$


and


$$
X_k=\binom Ak\binom{2A+H-k}{H-k},\qquad 0\le k\le H.
$$


Write


$$
\mathcal T=\sum_{k=0}^{H}X_k^2,\qquad
S=\sum_{k=0}^{H}(X_k/29)^2.
$$



The previously proved complete-column transfer is reused only at its stated precision:


$$
D\equiv5C_n^2\mathcal T\pmod{29^4},
\qquad
M-(6C_n)^{-1}D\equiv0\pmod{29^4}.
\tag{1.1}
$$



### 1.2 The binary construction

Retain


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$




$$
D=D_u=\frac{9^{18+32u}-81}{128},\qquad
C=4002D+2532.
$$


Here $D$ is a parameter, not the $29$-adic norm.

The higher kernel is


$$
\mathcal B_t=\binom Ct\binom{2C+D-t}{D-t},
\qquad 0\le t\le D,
$$


with content depth


$$
\mu(C,D)=\min_{0\le t\le D}v_2(\mathcal B_t).
$$



The complete normalized columns and scalars are


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},
\qquad N=X^TX>0,\qquad H=X^TY\ne0.
$$


The accepted original-family alignment is


$$
H-N\in128\mathbb Z_2.
\tag{1.2}
$$



I do not repeat the old contact audit or the passing universal mixed table.

---

# Part I. The $29$-adic certificate

## 2. Source-level audit of the one-carry recurrence

### 2.1 Carry selection and finite range

The state


$$
(\sigma,\beta,\gamma,\text{depth})
$$


has the stated meanings:

- $\sigma$: carry in $k+\ell=H$;
- $\beta$: borrow in $A-k$;
- $\gamma$: carry in $2A+\ell$;
- `depth`: accumulated valuation of the two binomial factors.

For each chosen digit $k_i$, the program determines the unique digit $\ell_i$ compatible with the incoming sum carry. It then computes the digit of $A-k$, the digit of $2A+\ell$, and the outgoing carries.

The update


$$
\text{depth}'=\text{depth}+\beta'+\gamma'
$$


is exactly the Kummer valuation count. Discarding depth greater than one is legitimate for computing $S\bmod29^2$: if $v_{29}(X_k)\ge2$, then


$$
(X_k/29)^2\equiv0\pmod{29^2}.
$$


On the preferred cylinder there are no zero-carry terms.

Accepting only


$$
(\sigma,\beta,\gamma,\text{depth})=(0,0,0,1)
$$


enforces both nonnegative differences and the original finite interval $0\le k\le H$. No fictitious terminal summand is admitted.

### 2.2 Wilson unit and factorial stripping

The reported Wilson unit is


$$
28!\equiv521=-1+18\cdot29\pmod{841}.
$$


It must not be replaced by $-1$ at this precision. For example,


$$
521^2\equiv639\pmod{841},
$$


not $1$.

The program correctly uses


$$
g_i=
(28!)^{2(\beta'+\gamma')}
\left(\frac{a_i!\,s_i!}{k_i!\,r_i!\,c_i!\,\ell_i!}\right)^2
\pmod{841}.
$$


All inverted factorials have indices below $29$, so every inverse exists.

The relevant stripping formula is for the factorial with multiples of $29$ removed:


$$
F_{29}(29m+r)
\equiv(28!)^m r!\bigl(1+29m\mathsf H_r\bigr)
\pmod{841}.
$$


The full factorial unit additionally includes recursive stripping at higher levels. The digit product in the program includes those levels; it does not mistake the first stripped block for the entire factorial unit.

### 2.3 Signed harmonic state

The stored vector is


$$
(\mathsf H_a,\mathsf H_s,-\mathsf H_k,
-\mathsf H_r,-\mathsf H_c,-\mathsf H_\ell).
$$


The signs match the numerator and denominator factorials.

For a new digit tuple


$$
\tau=(a,s,k,r,c,\ell),
$$


the update


$$
W'\mathrel{+}=g\bigl(W+2\cdot29\,\tau\cdot Z\bigr)\pmod{841}
$$


adds the adjacent-digit harmonic correction. The companion update


$$
Z'\mathrel{+}=(g\bmod29)(W\bmod29)
(\mathsf H_a,\mathsf H_s,-\mathsf H_k,
-\mathsf H_r,-\mathsf H_c,-\mathsf H_\ell)
$$


correctly uses the old leading weight. Products of two first-order corrections vanish modulo $29^2$.

These updates are linear under merging paths, so the compressed state has the same total weight as an enumeration of all retained paths.

### 2.4 Digit drain

`full_recurrence` first extracts every digit of the actual integers $H,A,2A$, until all three quotients are zero. It then appends four zero layers.

Thus it does not truncate the affine or doubling expansion. The extra layers close the last harmonic interaction and permit genuine carries to drain. Invalid sum or subtraction paths are rejected by the terminal state.

This is a safe finite drain. It is more than a test that the low digits agree.

---

## 3. The initializer and its divisions

The two input layers


$$
(H_0,H_1)=(20,z),\qquad
(A_0,A_1)=(9,19),\qquad
((2A)_0,(2A)_1)=(18,9)
$$


are correct for $H=20+29G$, $z=G\bmod29$.

After those layers, surviving paths have


$$
\beta=\gamma=0,\qquad \text{depth}=1.
$$


Only the sum carry $\sigma\in\{0,1\}$ remains.

The division


$$
r_\sigma(z)=W_\sigma(z)/29\bmod29
$$


is justified by the previously proved **branchwise finite antisymmetry**. It is not justified merely by observing that a later complete sum is divisible by $29$. The supplied initializer checks the stronger statement separately at all 58 boundary states.

The finite output has


$$
58(1+6)=406
$$


field entries, with the supplied counts


$$
38\text{ nonzero }r\text{-entries},\qquad
140\text{ nonzero harmonic entries}.
$$



The displayed table also has the useful shape


$$
Z_\sigma(z)=(0,\zeta,\xi,\zeta,0,-\xi).
\tag{3.1}
$$


At the next retained, carry-free binomial digit,


$$
r=a-k,\qquad s=c+\ell,
$$


so


$$
\tau\cdot Z
=\zeta(a+c)+(\xi-\zeta)(k-\ell).
\tag{3.2}
$$


Thus the six-component initializer can, for this certified table, be represented by two harmonic residues. Equation (3.2) is an exact algebraic simplification of the next transition, not a claim that the remaining tail disappears.

Because $W\bmod29=0$ at initialization, newly generated harmonic states vanish after that transition. Subsequent layers use ordinary carry-free weights modulo $29$, still with the actual sum-carry and terminal boundary.

---

## 4. What the 33 complete comparisons establish

The tested auxiliary values are exactly


$$
G\in\{0,1,\ldots,28,29,30,57,100\},
\qquad H=20+29G.
$$



The direct program evaluates each full finite sum using exact binomial integers, checks $29\mid X_k$ before division, and compares


$$
S\bmod841
$$


with the all-digit recurrence. It separately verifies the weighted cancellation modulo $29$.

The supplied receipt therefore provides bounded corroboration of:

- the unit weights;
- both one-carry branches;
- state merging;
- higher-digit continuation;
- terminal rejection and drainage;
- the normalized divisions.

All 33 reported values of $\mathcal T/29^3\bmod29$ are nonzero. That is a fact about those 33 auxiliary parameters only.

### A concrete demonstration that the higher tail matters

The receipt gives


$$
G=0:\quad \mathcal T/29^3\equiv11\pmod{29},
$$


but


$$
G=29:\quad \mathcal T/29^3\equiv27\pmod{29}.
$$


These have the same $G\bmod29$, hence the same two-layer initializer.

Similarly, $G=28$ and $G=57$ give different final digits despite having the same low digit.

Therefore even the supplied finite data explicitly rule out treating the initializer as the final answer.

### Transfer to actual norms

At an **actual preferred-cylinder index**, a nonzero terminal result would imply, by (1.1),


$$
v_{29}(D)=v_{29}(M)=3.
$$


No such actual-index terminal result is supplied by these 33 auxiliary tests.

Moreover, the accepted deeper-content refinement theorem already obstructs a universal exact-depth-three assertion on an unrestricted finite preferred subcylinder. Nonzero initializer entries do not evade that obstruction.

---

# Part II. Exact binary kernel minima

## 5. Proof of the all-digit minimum algorithm

At bit $i$, the state $(a,h,w)$ records incoming carries in


$$
t+r=C,\qquad t+d=D,\qquad 2C+d.
$$



The source chooses bits $\tau,\rho,\delta$ satisfying


$$
\tau+\rho+a=C_i+2a',
\qquad
\tau+\delta+h=D_i+2h',
$$


and sets


$$
w'=\left\lfloor\frac{(2C)_i+\delta+w}{2}\right\rfloor.
$$


Its cost increment is


$$
a'+w'.
$$



Every completed zero-terminal path gives


$$
r=C-t,\qquad d=D-t,\qquad0\le t\le D.
$$


Conversely, each such integer $t$ gives its unique completed addition path.

Kummer’s theorem therefore gives


$$
\sum_i(a_{i+1}+w_{i+1})
=
v_2\binom Ct+
v_2\binom{2C+D-t}{D-t}
=
v_2(\mathcal B_t).
\tag{5.1}
$$



### Minimum-cost merging

For a fixed layer and carry state, future admissible transitions and costs depend only on that state and the remaining input bits. They do not depend on the earlier witness bits.

Hence retaining the lowest-cost prefix at each state preserves the global minimum. Keeping just one representative on a tie is also valid: the discarded tied prefix has exactly the same possible future costs.

This proves the dynamic-programming minimum, rather than merely the valuation of a chosen witness.

### Terminal paths

The program uses


$$
L=1+\operatorname{bitlength}(2C+D).
$$


This includes a zero layer beyond every possible bit of the sums in a valid path.

A spurious overflow in the equations for $C$ or $D$ cannot be accepted as a zero-terminal path. The carry in $2C+d$ is also drained before acceptance. Both endpoints $t=0$ and $t=D$ are included.

### Witness identity

Legendre’s formula gives


$$
\begin{aligned}
v_2(\mathcal B_t)
={}&s_2(t)+s_2(C-t)-s_2(C)\\
&+s_2(D-t)+s_2(2C)-s_2(2C+D-t).
\end{aligned}
\tag{5.2}
$$


This is exactly the source’s independent witness check.

A witness alone proves an upper bound for the minimum. The minimum-cost computation supplies the matching lower bound.

### Implementation complexity qualification

The abstract eight-state minimum algorithm needs a linear number of bounded-state digit transitions. The supplied implementation copies witness sequences while progressing through the layers, so its literal list-copying work need not be linear in bit length. This is an efficiency qualification, not a correctness defect.

---

## 6. Scope of the sixteen actual computations

The reported minima are



$$
\begin{array}{c|rrrrrrrr}
u&0&1&2&3&4&5&6&7\\ \hline
\mu&7&17&26&32&53&69&96&96
\end{array}
$$





$$
\begin{array}{c|rrrrrrrr}
u&8&9&10&11&12&13&14&15\\ \hline
\mu&99&119&130&153&157&190&201&206.
\end{array}
$$



These use the exact original integers


$$
D_u=\frac{9^{18+32u}-81}{128},
$$


and therefore genuinely concern actual indices.

I accept the reported exact minima as bounded computational results supported by the audited algorithm. The packet includes the witnesses and summaries; it does not include the full layer arrays. I have not independently checked those absent arrays.

No conclusion follows here about:

- all $u\ge0$;
- monotonicity of $\mu(D_u,C_u)$;
- a positive asymptotic growth rate;
- complete-column content;
- norm cancellation after kernel-content removal.

The exact reachability recurrence remains


$$
D_{u+1}=9^{32}D_u+\frac{81(9^{32}-1)}{128}.
\tag{6.1}
$$


An infinite theorem must control the digit algorithm along this recurrence, not along arbitrary low-residue representatives.

---

# Part III. Newton compression and actual scalar consequences

## 7. The interpolation claim and its precise extension

To avoid confusing the original index $u$ with the Newton variable, put


$$
z=\frac{D-1}{2}.
$$


Define


$$
\Phi(z,t)=\sum_{i=0}^{3}\sum_{j=0}^{4}
c_{ij}\binom zi\binom tj\pmod{128},
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


and


$$
\Psi(z)=11+120\binom z1+32\binom z2\pmod{128}.
$$



The reported identity is


$$
\mathcal A_{\rm full}(D,t)\equiv8\Phi(z,t)\pmod{1024},
$$




$$
\mathcal A_{\rm end}(D)\equiv8\Psi(z)\pmod{1024}.
\tag{7.1}
$$



### Why this is more than an interpolation guess

The source first asserts divisibility by $8$ of every stored coefficient and only then forms the quotient arrays modulo $128$.

It computes the $4\times5$ candidate Newton coefficients by finite differences. A small finite-difference corner alone would not establish the degree bounds. The decisive additional step is the exhaustive comparison against the entire arrays:


$$
512\times1024\quad\text{and}\quad512.
$$



Thus the receipt certifies a complete finite-state compression.

The NumPy evaluation is safe at this stage: the binomial matrices are reduced modulo $128$, the coefficient matrix has bounded entries, and the short matrix products are far below signed $64$-bit limits. The forward differences are evaluated with Python integer arithmetic.

### Periods needed for extension

Under the already proved safe shift $D\mapsto D+1024$,


$$
z\mapsto z+512.
$$


For $i\le3$, binomial translation gives


$$
\binom{z+512}{i}-\binom zi\equiv0\pmod{128}.
$$


Likewise, for $j\le4$,


$$
\binom{t+1024}{j}-\binom tj\equiv0\pmod{128}.
$$


Indeed, the worst valuation loss is at most $\lfloor\log_2 i\rfloor$ or $\lfloor\log_2 j\rfloor$, leaving sufficient precision.

The polynomial right sides therefore possess the periods needed to match the accepted coefficient periods. This extends (7.1) from the complete representative table to admissible actual coefficient arguments.

It does **not** make the higher kernel periodic.

---

## 8. Complete norm contraction

The accepted raw scalar interface is


$$
4N\equiv
\sum_{t=0}^{D-1}\mathcal B_t^2\mathcal A_{\rm full}(D,t)
+\mathcal B_D^2\mathcal A_{\rm end}(D)
\pmod{1024}.
$$


Substituting (7.1), define


$$
\mathscr S(C,D)=
\sum_{t=0}^{D-1}\mathcal B_t^2\Phi(z,t)
+\mathcal B_D^2\Psi(z)\pmod{128}.
$$


Then exact division of the whole congruence gives


$$
\boxed{N\equiv2\mathscr S(C,D)\pmod{256}.}
\tag{8.1}
$$



The shortened terminal block is retained. Equivalently,


$$
\mathscr S(C,D)=
\sum_{t=0}^{D}\mathcal B_t^2\Phi(z,t)
+\mathcal B_D^2\bigl(\Psi(z)-\Phi(z,D)\bigr)
\pmod{128}.
\tag{8.2}
$$


The final correction must not be omitted.

The exterior coordinate, including its $+1$, is absent from (8.1) only because its **complete contribution has already been bounded to vanish at this raw precision**. It is not absent from the exact norm construction at higher precision.

---

## 9. New precision-capped consequence of kernel content

Every kernel entry is divisible by $2^\mu$. Therefore every summand in $\mathscr S$ is divisible by $2^{2\mu}$, giving


$$
\boxed{
v_2(N)\ge\min\{8,\,1+2\mu(C,D)\}.
}
\tag{9.1}
$$



This is a lower bound derived from the complete modulus-$1024$ scalar interface. The cap at $8$ is essential.

In particular, $\mu\ge4$ already saturates this interface. All sixteen tested values satisfy the stronger condition $\mu\ge7$, so


$$
\boxed{N\in256\mathbb Z_2.}
\tag{9.2}
$$


Combining this with $H-N\in128\mathbb Z_2$,


$$
\boxed{H\in128\mathbb Z_2.}
\tag{9.3}
$$



### Exactly what remains possible

Let


$$
\alpha=v_2(N),\qquad
\eta=v_2(H-N),\qquad
\gamma=v_2(H).
$$


At these indices, the established restrictions are


$$
\alpha\ge8,\qquad\eta\ge7,\qquad\gamma\ge7.
$$



The valuation alternatives remain:

- If $\eta<\alpha$, then $\gamma=\eta$.
- If $\eta>\alpha$, then $\gamma=\alpha$.
- If $\eta=\alpha$, cancellation may give $\gamma>\alpha$.

For example, if the as-yet-uncomputed defect digit has $\eta=7$, then


$$
\gamma=7<\alpha.
$$


The present certificate does not decide whether that occurs.

### Why the huge kernel minima do not give huge norm-depth bounds

The congruence determines $4N$ only modulo $2^{10}$. Once its kernel contraction vanishes modulo $2^{10}$, no further information follows from the size of $\mu$.

Dividing the congruence by $2^{2\mu}$ is impermissible: the unknown raw error has not been shown divisible by that quantity.

Consequently the following inferences are unsupported:


$$
\alpha\ge2\mu+1,\qquad
\alpha=2\mu+1,\qquad
\gamma=\alpha.
$$


The first of these is valid only with the precision cap in (9.1).

### Relevance of a fixed norm-unit certificate

A certificate for a unit at a low fixed norm depth may say nothing about these actual indices. In particular, the tested indices cannot have norm depth $6$ or $7$: (9.2) already excludes both.

A unit of an auxiliary low coefficient is also irrelevant when every actual kernel square annihilates it at the available modulus.

This does not prove that no fixed normalized norm digit could ever be useful. It proves that its relevance must be demonstrated after actual kernel contraction and at sufficient complete-force precision.

---

# Part IV. A complete-column lemma with explicit precision losses

## 10. Why truncated representatives alone cannot supply the bridge

The degree-$15$ coefficients and nine-entry exterior truncation encode the actual columns only through their proved weighted precision. At higher precision, later factorial terms, logarithmic forcing, reconstruction corrections, and endpoint terms can reappear.

There is also a finite-inverse issue: a small force error need not remain equally small after solving a rational finite system. The inverse can lose $p$-adic precision.

The following lemma separates these issues without presuming the desired factorization.

## 11. Precision-dependent content transfer lemma

Let $p$ be a prime. Fix one original index and its actual finite system. Let $V$ denote the complete reconstructed column array, including all coordinates and exterior terms. Suppose its exact dependence on the complete forcing array $f$ is


$$
V=e+Tf,
\tag{11.1}
$$


where $T$ is the actual rational finite reconstruction operator. It may contain the actual finite contact inverse. The array $e$ includes every exterior constant, in particular any $+1$.

Let $d_B$ be the actual least two-column clearer, and put


$$
\mathcal V=d_BV.
$$


Define


$$
\lambda=
\max\left\{0,\,-\min_{i,j}v_p((d_BT)_{ij})\right\}.
\tag{11.2}
$$



Choose finite approximations $e^{[K]},f^{[K]}$ satisfying


$$
v_p\!\left(d_B(e-e^{[K]})\right)\ge K,
\qquad
v_p(f-f^{[K]})\ge K+\lambda,
\tag{11.3}
$$


entrywise, and set


$$
\mathcal V^{[K]}=d_Be^{[K]}+d_BT f^{[K]}.
$$



Then:

1. **Complete precision transfer**
   

$$
\mathcal V\equiv\mathcal V^{[K]}\pmod{p^K}.
   \tag{11.4}
$$



2. If the retained reconstruction has a proved integral factorization
   

$$
\mathcal V^{[K]}=B^{[K]}\mathbf b+r^{[K]},
   \tag{11.5}
$$


   where $B^{[K]}$ is integral over $\mathbb Z_p$,
   

$$
\min_t v_p(b_t)=\mu,\qquad
   v_p(r^{[K]})\ge\rho,
$$


   then the actual complete-column content satisfies
   

$$
\boxed{
   c_p(\mathcal V)\ge\min\{K,\mu,\rho\}.
   }
   \tag{11.6}
$$



3. If a coordinate of $\mathcal V^{[K]}$ has valuation $c<K$, and every coordinate has valuation at least $c$, then
   

$$
c_p(\mathcal V)=c.
   \tag{11.7}
$$



Here $c_p$ is the minimum valuation over the **entire** column array.

### Proof

From (11.1),


$$
\mathcal V-\mathcal V^{[K]}
=d_B(e-e^{[K]})+d_BT(f-f^{[K]}).
$$


Every entry of the first term has valuation at least $K$. Every product in the second term has valuation at least


$$
-\lambda+(K+\lambda)=K.
$$


A finite sum cannot have smaller valuation, proving (11.4).

The factorized term in (11.5) has every coordinate divisible by $p^\mu$. Adding its remainder and then the error in (11.4) proves (11.6).

Finally, an error divisible by $p^K$ cannot change a coordinate valuation strictly below $K$. This proves (11.7). ∎

### Explicit finite-inverse loss

If $T=RC^{-1}$, one may bound its loss from


$$
C^{-1}=\frac{\operatorname{adj}(C)}{\det C}.
$$


For example,


$$
\min v_p(T_{ij})
\ge
\min v_p(R_{ij})
+\min v_p(\operatorname{adj}(C)_{ij})
-v_p(\det C).
\tag{11.8}
$$


This need not be sharp, but it is an explicit valid precision budget using the actual finite matrix.

### What the lemma requires of growing tails

For each requested $K$, (11.3) must be established for the **complete omitted force**, not just for each term of a conveniently selected positive kernel. In particular:

- factorial-tail cutoffs may need to grow with $K+\lambda$;
- logarithmic terms require their full denominator-sensitive bound;
- reconstruction overflow and negative moments must be retained when relevant;
- the endpoint and exterior $+1$ belong to $e^{[K]}$ or to its proved error bound;
- the least clearer is the actual one, not a substituted row clearer.

If the forcing is represented by finite sums at the fixed original index, keeping those sums in full is always a formal option. It may be computationally impractical, but no unjustified tail deletion is then involved.

---

## 12. The genuinely missing theorem

To use the binary kernel minimum in (11.6), one must prove, at arbitrary requested precision, a factorization of the **complete retained reconstruction** through the actual kernel vector—or prove a sufficiently divisible remainder:


$$
\boxed{
\mathcal V^{[K]}
=
B^{[K]}(\mathcal B_0,\ldots,\mathcal B_D)^T+r^{[K]},
}
$$


with integral $B^{[K]}$, a quantified bound for $r^{[K]}$, and the complete force precision (11.3).

That statement is not a consequence of the existing low coefficient representatives. Higher tails may produce shifted kernels or terms outside the ideal generated by the unshifted $\mathcal B_t$.

Even a successful content theorem would not determine norm valuation after content removal. For


$$
X=2^c x,
\qquad x\text{ primitive},
$$


one still has


$$
v_2(N)=2c+v_2(x^Tx),
$$


and the last valuation can be large because of dyadic cancellation.

Thus there are two separate remaining bridges:

1. **Kernel to complete columns:** arbitrary-precision factorization and complete remainder control.
2. **Complete columns to relative scalar valuation:** control of the normalized norm and mixed defect, particularly equal-depth cancellation.

Neither bridge has been proved by the new bounded computations.

---

# Part V. Primitive normalization and the research objective

## 13. Full gcd and actual denominator

For the binary construction retain the actual least clearer $d_B$,


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


and the full integer gcd


$$
g_B=\gcd(A_B,|H_B|).
$$


Then


$$
q_n=A_B/g_B>0,\qquad p_n=H_B/g_B.
$$


The rational Gram multiplier is $d_B^2/g_B$.

The exact dyadic interface remains


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\}.
\tag{13.1}
$$


The bounds $\alpha\ge8,\gamma\ge7$ do not determine $\gamma-\alpha$, so they do not simplify (13.1) to an exact new denominator valuation.

For the $29$-adic construction, the retained formula likewise depends on the relative scalar depth:


$$
v_{29}(q_n)=
\max\{0,2v_{29}(n!)-v_{29}(b!)-1+\delta-\mu_M\},
$$


where $\delta=v_{29}(D)$, $\mu_M=v_{29}(M)$. Auxiliary one-carry units do not assign these actual depths.

Neither local calculation controls the full all-prime gcd.

## 14. Whole evaluated error

The evaluated primitive form remains exactly


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$



For the binary construction, the retained complete signed-error result states, at its supplied scope,


$$
\epsilon_n<0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


No force component, factorial residual, contact boundary, or exterior endpoint is removed from this real error.

To prove irrationality by these approximants, one still needs a same-index sequence of nonzero primitive forms tending to zero. In particular, an adequate **upper bound on the full primitive denominator** is needed. A local denominator lower bound or a kernel-content lower bound does not provide that.

---

## 15. Bounded exact arithmetic for personal inspection

No repeat contact calculation or repeat universal mixed scan is needed.

### 15.1 Archival binary minimum check

For the existing four actual indices $u=0,1,2,3$, the coordinator can inspect the already generated arrays and verify, layer by layer:

1. the initial state has cost zero and all other states are absent;
2. each next-state cost is the minimum of all legal incoming transitions;
3. absent states really have no legal finite-cost predecessor;
4. the terminal zero-state costs are
   

$$
7,\ 17,\ 26,\ 32;
$$


5. the recorded carry paths obey every bit equation and attain those costs;
6. the witnesses satisfy (5.2).

This verifies the existing bounded certificate; it does not establish a pattern for later $u$.

### 15.2 A useful independent $29$-adic implementation check

The direct comparisons currently test `full_recurrence`, which starts from the empty state. A small additional cross-check could directly exercise the **exported normalized initializer**:

- Inputs: the supplied 58 initializer records and the same 33 auxiliary values $G$.
- Initialize from $z=G\bmod29$.
- Apply the third-digit normalized update, using (3.2).
- Continue with the remaining carry-free digit transfer and the true terminal condition.
- Expected output:
  

$$
\text{terminal normalized weight}
  =
  S/29
  =
  \mathcal T/29^3\pmod{29}
$$


  for every one of the 33 listed cases.

This is not needed for the algebraic proof of the normalization, but it directly checks use of the exported artifact rather than only its underlying unnormalized recurrence.

### 15.3 Next mathematical computation should follow a precision theorem

A higher-modulus binary calculation should not begin by extending the current polynomial representatives arbitrarily. Its necessary inputs are:

- a target complete-column or scalar precision;
- the actual finite-inverse loss;
- a complete-force cutoff justified at that precision;
- endpoint and exterior terms;
- the proposed kernel or shifted-kernel decomposition.

Its verifiable output should include complete residual divisibility receipts and, if exact content is claimed, a surviving normalized coordinate. Without those inputs, a larger table would still lack the missing transfer theorem.

---

# Final proof-status ledger

| Result | Status |
|---|---|
| One-carry recurrence, Wilson precision, signed harmonic state, finite drain | Source-level proof audit passes |
| 406-entry initializer | Accepted bounded coefficient computation; all divisions justified |
| 33 complete auxiliary comparisons | Accepted only for the listed auxiliary $H$ |
| Eight-state kernel minimum algorithm | Proved for the entire finite kernel interval |
| Sixteen actual-index minima and witnesses | Accepted bounded computations at $u=0,\ldots,15$ |
| Complete Newton norm compression | Accepted exhaustive finite-state identity, with justified period extension |
| $N\in256\mathbb Z_2,\ H\in128\mathbb Z_2$ at those sixteen indices | New rigorous deduction from the accepted interfaces |
| Arbitrary-precision content-transfer lemma | Proved with explicit hypotheses and inverse losses |
| Arbitrary-precision factorization of the actual complete columns through the kernel | Still a theorem to prove |
| All-depth relative valuations, full gcd, sufficient primitive-error decay | Unresolved |

**The new result is a precision-capped actual-index scalar consequence, not an infinite valuation theorem:** every tested actual binary index lies beyond the shallow norm-unit regime visible to the existing raw interface. The immediate mathematical bottleneck is now the complete arbitrary-precision kernel-to-column transfer, followed by normalized scalar cancellation. The global bottleneck remains the full primitive denominator versus the whole nonzero evaluated error.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


