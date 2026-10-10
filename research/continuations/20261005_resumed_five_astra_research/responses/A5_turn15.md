> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 15 — A normalized finite digit-transfer reduction

## Executive conclusion

The normalization bridge changes the interpretation of Turn 14 decisively:



$$
4Y=\mathcal R A^{-1}r+W_be_b,
\qquad
r=\frac{h^e+h^F-A(j!)_{0\le j<b}}{b!}.
$$



The raw computation of $V_w$ to precision $v_2(b!)+M$ is **not** a precision-sized computation of $4Y\bmod 2^M$. I withdraw that interpretation of the raw recurrence. Its raw-precision conclusions, within their stated hypotheses, do not solve the normalized problem.

This report gives a different reduction:

> **At normalized precision $2^M$, the complete two-column Gram pair admits a finite binary digit-transfer evaluation. Its state space can be bounded in terms of $M$, independently of $b$; its input includes the actual binary digits of $n$ and $b$.**

The construction retains high lower binomial indices. It does not replace them by bounded indices or fixed reference values. It uses:
- normalized forcing before inversion;
- a finite Neumann expansion of the actual finite matrix;
- explicit binomial formulas for every matrix factor;
- a finite digit transfer for bounded-dimensional sums of products of binomial coefficients.

This is **not an $O(\operatorname{poly}(M))$ algorithm**. The straightforward state bound is exponential in a polynomial in $M$, and the construction is not yet an efficient implementation. It does, however, give an actual finite digit-transfer evaluation rather than an unevaluated Gram matrix or an algorithm at raw factorial precision.

I also prove the binary saturation statement appropriate to the rational displacement identity. It concerns the unweighted reconstruction lattice. Weighting by $W_j$ must not be treated as a unimodular operation.

No scalar alignment law, unrestricted relative-valuation theorem, full primitive-denominator bound, or irrationality result follows merely from this evaluability theorem.

---

## 1. Domain and exact normalization

Throughout,


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


Write


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532.
$$



Contact indices are exactly


$$
0\le i,r<b,
$$


and reconstructed coordinates are exactly


$$
0\le j\le b.
$$



Thus a block decomposition consists of


$$
0\le t<D,\quad 0\le \rho<128,
$$


the shortened block


$$
t=D,\quad 0\le\rho\le80,
$$


and the separate endpoint $j=b$.

To avoid confusing a matrix with a reconstructed column, put


$$
\mathsf A=\widetilde N U,\qquad U=(I+S)^n,
$$


and


$$
\mathcal R=\operatorname{diag}(W_j)C,\qquad
W_j=\binom{n+2}{j},
$$


where


$$
(Cx)_j=jx_{j-1}-x_j,\qquad x_{-1}=x_b=0.
$$



Let


$$
R_{\rm cen}=2^{n/2}\binom n{n/2},\qquad f=f^0/R_{\rm cen}.
$$


The actual normalized columns are


$$
\boxed{
\mathsf a:=2X=\mathcal R\mathsf A^{-1}f,
\qquad
\mathsf b:=4Y=\mathcal R\mathsf A^{-1}r+W_be_b.
}
\tag{1.1}
$$



These give


$$
\mathsf a^T\mathsf a=4N,\qquad
\mathsf a^T\mathsf b=8H.
\tag{1.2}
$$



The endpoint term in (1.1) is obtained by the exact cancellation


$$
\mathcal R(j!)_{0\le j<b}=-e_0+b!W_be_b.
$$


It is not a relabelled exterior $e_0$.

---

## 2. Normalized complete-force truncation

Write


$$
\lambda_s=s![z^s]\phi(z)^n,\qquad
\phi(z)=1-z+\frac{z^2}{2}.
$$


The accepted complete symbol expansion supplies


$$
\lambda_s=\sum_{a\ge0}\lambda_s^{(a)},\qquad
v_2(\lambda_s^{(a)})\ge a,\qquad s\le4a.
\tag{2.1}
$$



The exact normalized exponential force is


$$
r_i^e
=
\sum_s\lambda_s\binom{n+i}{s}
\sum_{t\ge0}
\binom{2n+i-s}{b+t}\frac{(b+t)!}{b!}.
\tag{2.2}
$$


Invalid terms are zero. In particular, terms requiring negative upper factorial arguments are not introduced.

Since


$$
\frac{(b+t)!}{b!}=t!\binom{b+t}{t},
$$


the summand of expansion order $a$ and tail label $t$ has depth at least


$$
a+v_2(t!).
$$



Consequently,


$$
\boxed{
r_i^e\equiv
\sum_{\substack{a,t\ge0\\a+v_2(t!)<M}}
\ \sum_{s=0}^{4a}
\lambda_s^{(a)}
\binom{n+i}{s}
t!\binom{b+t}{t}
\binom{2n+i-s}{b+t}
\pmod{2^M}.
}
\tag{2.3}
$$



The ranges $a<M$, $t<2M$, $s<4M$ suffice. But the lower index


$$
b+t
$$


is still large. Formula (2.3) does not have bounded Newton degree in $i$, and I make no such claim.

### 2.1 Complete logarithmic budget after division

Turn 14’s whole-input estimate yields


$$
r^F\in2^{K_{\rm norm}}\mathbb Z_2^b,
$$


where


$$
\boxed{
K_{\rm norm}
=
1+v_2((n/2)!)-v_2(b!)
-\lfloor\log_2(2n+b-1)\rfloor.
}
\tag{2.4}
$$



Thus:
- if $M\le K_{\rm norm}$, the complete logarithmic force is zero modulo $2^M$;
- if $M>K_{\rm norm}$, it must be retained.

This second case does not force a return to a large raw-precision computation. On the original family,


$$
K_{\rm norm}\ge b.
\tag{2.5}
$$


For example, Legendre’s formula gives


$$
K_{\rm norm}
=
1+2000b-s_2(2001b)+s_2(b)
-\lfloor\log_2(8005b-1)\rfloor,
$$


and the elementary logarithmic bounds imply (2.5) already for $b\ge16$, far below the smallest original $b$.

Therefore


$$
M>K_{\rm norm}\quad\Longrightarrow\quad b<M,\qquad n<4002M.
\tag{2.6}
$$



In that branch the original finite system itself has dimension $O(M)$. The complete rational logarithmic coefficients can be generated directly from


$$
u_0=u_1=1,\qquad u_m=u_{m-1}-\tfrac12u_{m-2},
$$




$$
L_m=2m!\sum_{q=1}^m\frac{u_{q-1}}q,
$$


and the exact supplied force formula. This is a calculation whose size is controlled by $M$, not a hidden computation at precision proportional to an unrestricted $b$.

The remainder of the digit-transfer construction addresses the nontrivial branch


$$
M\le K_{\rm norm}.
$$



---

## 3. Explicit finite inverse without factorial precision

Let


$$
\mathsf P_{ir}=\binom{n+i}{r},\qquad 0\le i,r<b,
$$


and write


$$
\widetilde N=\mathsf P+\mathsf E.
$$


Because $\lambda_0=1$ and every $\lambda_s$, $s>0$, is even,


$$
\mathsf E\in2M_b(\mathbb Z_2).
$$



Let


$$
\mathsf L_{it}=\binom it.
$$


Finite Vandermonde convolution gives


$$
\mathsf P=\mathsf L U,
$$


so both $\mathsf P$ and $\mathsf A$ are invertible over $\mathbb Z_2$.

The exact finite inverse formula modulo $2^M$ is


$$
\boxed{
\mathsf A^{-1}
\equiv
U^{-1}\sum_{k=0}^{M-1}
(-\mathsf P^{-1}\mathsf E)^k\mathsf P^{-1}
\pmod{2^M}.
}
\tag{3.1}
$$



Every matrix here retains its actual $b\times b$ boundary.

The factors have explicit binomial entries:


$$
(U^{-1})_{rt}
=
\begin{cases}
\binom{-n}{t-r},&t\ge r,\\
0,&t<r,
\end{cases}
\tag{3.2}
$$


and


$$
\boxed{
(\mathsf P^{-1})_{ri}
=
\sum_{t=\max(r,i)}^{b-1}
\binom{-n}{t-r}
(-1)^{t-i}\binom ti.
}
\tag{3.3}
$$



At precision $M$,


$$
\mathsf E_{ir}
\equiv
\sum_{1\le a<M}\sum_{s=1}^{4a}
\lambda_s^{(a)}
\binom{n+i}{s}\binom{n+i-s}{r}
\pmod{2^M},
\tag{3.4}
$$


with the original validity restrictions.

Thus every term in an expanded entry of (3.1) is a bounded-dimensional finite sum of products of binomial coefficients. Its number of summation variables is $O(M)$. Crucially, no variable is enumerated one value at a time in the proposed digit-transfer evaluation.

Negative upper binomials in (3.2)–(3.3) are converted exactly:


$$
\binom{-n}{d}=(-1)^d\binom{n+d-1}{d}.
\tag{3.5}
$$



This preserves both their units and signs.

---

## 4. A high-index binary kernel-transfer lemma

The following elementary construction is the main new mechanism.

### Lemma 1 — Finite digit evaluation of binomial-product sums

Fix $M\ge1$. Consider a finite sum over a fixed number of nonnegative integer variables, subject to affine equalities and inequalities, whose summand is a product of:

1. binomial coefficients
   

$$
\binom{L_\nu}{K_\nu},
$$


   where $L_\nu,K_\nu$ are integer affine functions of the variables and input parameters;
2. integer polynomial factors;
3. signs determined by integer affine functions;
4. fixed coefficients in $\mathbb Z_2/2^M\mathbb Z_2$.

Assume the valid domain imposes $0\le K_\nu\le L_\nu$.

Then the sum modulo $2^M$ can be evaluated by a finite least-significant-digit binary transfer. Its state set depends on $M$, the number of variables and factors, and the affine coefficients—not on the magnitudes of the input parameters.

The transfer reads the actual parameter digits and enforces the exact finite bounds.

### Proof

There are two components: valuations and odd units.

#### Valuations

For a binomial coefficient,


$$
v_2\binom LK
$$


is the number of carries in


$$
K+(L-K)=L.
$$


Binary carry registers verify this equality and accumulate the valuation, clipped at $M$. Once the total valuation of the product reaches $M$, that branch contributes zero.

Affine relations and finite bounds are also checked by finite carry or borrow registers. With fixed affine coefficients and a fixed number of variables, these registers have bounded ranges.

#### Odd units

Define


$$
O_M(N)=\prod_{\substack{1\le j\le N\\j\ {\rm odd}}}j
\pmod{2^M}.
$$


This function has period $2^{M+1}$.

Indeed, an interval of length $2^{M+1}$ contains each odd residue modulo $2^M$ twice. Their product is the square of the product of all units modulo $2^M$, which is $1$.

Let


$$
F_M(N)=2^{-v_2(N!)}N!\pmod{2^M}.
$$


Separating odd and even factors gives


$$
F_M(N)=O_M(N)F_M(\lfloor N/2\rfloor),
$$


and hence


$$
\boxed{
F_M(N)=\prod_{\ell\ge0}O_M(\lfloor N/2^\ell\rfloor).
}
\tag{4.1}
$$



Each factor on the right depends only on a window of $M+1$ consecutive binary digits of $N$. A finite digit transfer can therefore accumulate $F_M(N)$ by storing those windows and multiplying their table values. A terminal flush of zero digits completes the windows.

Consequently


$$
\boxed{
\binom LK
=
2^{v_2\binom LK}
F_M(L)F_M(K)^{-1}F_M(L-K)^{-1}
\pmod{2^M}.
}
\tag{4.2}
$$


All inversions here are of odd units.

Polynomial factors need only the variables modulo $2^M$; signs need only parity. These require finitely many additional registers.

At each digit, sum the weights of all admissible choices of variable digits. Terminal states enforce the exact inequalities and carry termination. Every valid integer tuple has exactly one binary expansion with the prescribed padding, so it is counted once.

This constructs and evaluates the stated sum. ∎

### Scope and complexity

This is not a valuation-only automaton. Formula (4.2) retains the complete odd binomial units.

For the systems below, the number of variables and factors is polynomial in $M$. A deliberately loose implementation bound is


$$
2^{\operatorname{poly}(M)}
$$


states and transitions per input digit. No polynomial-in-$M$ claim is made.

The input length remains relevant: the actual digits of $n$ and $b$ must be read. The theorem does not assert a constant-time replacement of those digits by a short residue.

---

## 5. Application to the complete normalized Gram pair

Expand (3.1), use (3.3) for each occurrence of $\mathsf P^{-1}$, and use (3.4) for each contact correction.

For the second force insert (2.3). For the first force use the accepted complete central filtration. At fixed precision it provides a finite sum with:
- a factorially bounded force-index range;
- a factorially bounded central-sum range;
- small-index binomial and falling-factorial factors.

All odd denominators in those central scalar coefficients are inverted only after their powers of $2$ have been separated.

Every resulting term is of the form covered by Lemma 1.

Reconstruction adds only:


$$
W_j,\qquad j,\qquad
\theta_j,\qquad\theta_{j-1},
$$


with the boundary conventions in Section 1. Products of two reconstructed columns therefore remain in the same class.

### Theorem 2 — Complete normalized Gram digit transfer

For every original $n,b$ and every $M\ge1$, the three residues


$$
\boxed{
\mathsf a^T\mathsf a,\qquad
\mathsf a^T\mathsf b,\qquad
\mathsf b^T\mathsf b
\pmod{2^M}
}
\tag{5.1}
$$


have a finite binary digit-transfer evaluation with state bound depending only on $M$.

In the branch $M\le K_{\rm norm}$, this follows from the explicit formulas above. In the other branch, $b<M$, and the complete finite system may be evaluated directly with size controlled by $M$.

#### Endpoint terms

The second column is expanded as


$$
\mathsf b=\mathcal R\psi+W_be_b.
$$


Thus, for example,


$$
\mathsf a^T\mathsf b
=
\mathsf a^T\mathcal R\psi+W_b\mathsf a_b,
$$


and


$$
\mathsf b^T\mathsf b
=
(\mathcal R\psi)^T(\mathcal R\psi)
+2W_b(\mathcal R\psi)_b+W_b^2.
$$


No endpoint contribution is inferred from an interior formula.

#### Shortened block

The transfer may simply enforce


$$
0\le j<b
$$


for interior terms. If block variables are used, it enforces exactly


$$
t<D,\ 0\le\rho<128,
\quad\text{or}\quad
t=D,\ 0\le\rho\le80.
$$


It does not fill the shortened block.

### What this establishes

Theorem 2 supplies an evaluation mechanism for the complete normalized pair. It is stronger than leaving three Gram entries unspecified.

It does **not** evaluate those residues into a useful closed congruence on the original family. In particular, it does not prove


$$
\gamma-\alpha
$$


bounded, large, or aligned in any prescribed way.

---

## 6. Binary displacement and the correct saturation statement

The rational identities of A2turn6 transfer to this binary parameter line because their derivation is algebraic. Retain its operator $\mathcal D$, with rows


$$
1\le i\le b-2,
$$


and its matrix $\mathcal V$, with columns


$$
0\le k\le b.
$$


Then


$$
\boxed{
\mathcal D\mathsf A=-\mathcal VC,\qquad
\mathcal Df=0,\qquad
\mathcal Dr=\mathcal Ve_b.
}
\tag{6.1}
$$



The coefficients of $\mathcal D$ are binary integral: the numerators in its displayed half-integer expressions contain the required factor $2$. Its leading coefficient is $1$, so $\mathcal D$ is surjective over $\mathbb Z_2$.

The divided-power coefficients defining $\mathcal V$ are integral. Since $\mathsf A$ is unimodular, (6.1) implies that $\mathcal V$ is surjective over $\mathbb Z_2$.

There is also an explicit saturation proof.

Define the primitive charge


$$
\chi(q)=\sum_{j=0}^b\frac{b!}{j!}q_j.
$$


Then


$$
\chi(Cx)=0,\qquad\chi(e_b)=1.
$$


The top $b$ rows of $C$ form a triangular unimodular matrix. Hence


$$
\boxed{
\mathbb Z_2^{b+1}=C\mathbb Z_2^b\oplus\mathbb Z_2e_b.
}
\tag{6.2}
$$



Let $h^{(0)},h^{(1)}$ be the homogeneous recurrence solutions with initial values $(1,0)$, $(0,1)$, and let


$$
\mathcal D\tau=\mathcal Ve_b,\qquad \tau_0=\tau_1=0.
$$


Then


$$
C\mathsf A^{-1}h^{(0)},\quad
C\mathsf A^{-1}h^{(1)},\quad
C\mathsf A^{-1}\tau+e_b
\tag{6.3}
$$


form a $\mathbb Z_2$-basis of $\ker\mathcal V$.

Indeed, decompose $q=Cx+ce_b$ using (6.2). The equation $\mathcal Vq=0$ is equivalent to


$$
\mathcal D(\mathsf Ax-c\tau)=0,
$$


whose solutions are exactly the integral combinations of $h^{(0)},h^{(1)}$.

This proves saturation **before weighting**.

After multiplication by $\operatorname{diag}(W_j)$, the resulting basis describes the exact weighted image lattice, but need not be saturated in the ambient coordinate lattice. Binary contents must still be calculated from the actual weighted columns.

The complete logarithmic contribution remains in the two initial force entries $r_0,r_1$ in this displacement representation. It is omitted modulo $2^M$ only under (2.4), not because the interior recurrence is homogeneous.

---

## 7. Content and primitive-norm cancellation

Let


$$
a=\min_jv_2(\mathsf a_j),\qquad
c=\min_jv_2(\mathsf b_j).
$$


The accepted nonvanishing makes these finite.

A digit transfer can also search for coordinates at which a prescribed residue is nonzero: retain the coordinate digits instead of immediately summing the output, or use Boolean acceptance states. Thus adaptive content certification is possible without enumerating $b+1$ coordinates.

However, after writing


$$
\mathsf a=2^a\mathsf a_{\rm prim},
$$


the norm is


$$
\mathsf a^T\mathsf a
=
2^{2a}\mathsf a_{\rm prim}^T\mathsf a_{\rm prim}.
$$


The factor


$$
\mathsf a_{\rm prim}^T\mathsf a_{\rm prim}
$$


can have substantial binary valuation. Saturation and column primitivity do not remove it.

Accordingly:
- to obtain $N\bmod2^m$, evaluate $\mathsf a^T\mathsf a\bmod2^{m+2}$;
- to obtain $H\bmod2^m$, evaluate $\mathsf a^T\mathsf b\bmod2^{m+3}$;
- to resolve relative primitive quantities, add the actual content and primitive-norm losses.

The finite transfer gives access to these deeper residues. It does not prove a uniform bound on how deep one must go.

---

## 8. Concrete follow-on lemma

The remaining local theorem is no longer “represent the scalar by finitely many sums.” Theorem 2 does that with an explicit digit evaluation.

A useful next target is:

> **Original-family transfer invariant — open.**  
> For the transfer constructed from (2.3), (3.1)–(3.5), and reconstruction (1.1), identify an invariant relation between its norm and mixed output channels on
> 

$$
> b=9^{18+32u},\qquad n=4002b.
>
$$


> The relation must survive arbitrary additional digits and must retain the actual primitive-norm factor after removal of column content.

A successful proof could come from a quotient of the transfer state space, a conserved bilinear form, or an induction under the original update $b\mapsto9^{32}b$. None is proved here.

A finite table of output residues would not establish this invariant.

---

## 9. Bounded exact arithmetic for inspection

No tools were executed.

### Audit A — High-index unit transfer

Use


$$
M=1,\ldots,5,\qquad 0\le K\le L\le127.
$$



Compare direct exact binomial reduction with:
1. carry valuation;
2. the table $O_M$;
3. formula (4.1);
4. formula (4.2).

**Expected output:** zero discrepancies, including cases with $K>2^M$.

This checks the high-lower-index mechanism, not merely small binomial indices.

### Audit B — Complete normalized finite-system comparison

Use


$$
(n,b)\in\{(6,3),(10,5),(14,7)\},\qquad M\in\{2,3,4\}.
$$


These are auxiliary systems, not original-family indices.

Compute exactly:
- $\widetilde N,U,\mathsf A$;
- the complete $h^e,h^F$;
- $r=(h-\mathsf A\,\mathrm{facvec})/b!$;
- both sides of the normalization bridge;
- the finite Neumann expression (3.1);
- all reconstructed coordinates, including $j=b$.

Where a rational entry is not integral at the requested modulus, compare after exact valuation-safe clearing; do not silently reduce a nonintegral rational modulo $2^M$.

**Expected output:** exact normalization residual zero, and agreement of every integral modular comparison.

### Audit C — Digit-sum contraction

At the same auxiliary inputs, evaluate the full Gram residues both:
- by direct finite summation;
- by the digit-transfer expansion of the matrix words.

**Expected output:** identical three-entry Gram data, together with a separate certificate for the endpoint cross terms.

Passing these checks would certify only the stated finite cases. The all-index evaluation theorem rests on the symbolic constructions above.

---

## 10. Final gcd and whole evaluated error

The least actual clearer and full integer Gram pair remain


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}\ne0.
$$


The final reduction is exactly


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
$$


Every prime is included. The primitive multiplier is


$$
d_B^2/g_B.
$$



The old exact binary interface remains


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\},
$$


where


$$
\alpha=v_2(N),\qquad\gamma=v_2(H).
$$


The present theorem makes finite-depth evaluation of the relevant pair possible; it does not bound $\gamma-\alpha$.

With the retained signed-error theorem,


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
\quad\text{eventually},
}
$$


and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$



Irrationality by this route still requires a same-index estimate making this **whole nonzero expression** tend to zero.

---

## Concluding proof-status ledger

### New results proved here

1. A normalized-force truncation retaining the genuine large lower indices $b+t$.
2. A complete logarithmic precision split after division by $b!$; beyond its vanishing range, the actual system size is $O(M)$.
3. An explicit finite Neumann expansion of the original normalized inverse into binomial-product sums.
4. A high-index, unit-sensitive binary digit-transfer lemma.
5. A finite digit-transfer evaluation of the complete normalized Gram pair, with state bound depending on precision rather than factorial depth.
6. Binary saturation of the unweighted three-column displacement kernel, with weighted content kept separate.

### Limitations

- No polynomial-in-$M$ complexity bound is proved.
- No useful all-depth norm/mixed congruence is evaluated.
- No primitive-norm cancellation theorem is obtained.
- No full all-prime denominator estimate is obtained.

### Exact remaining bottleneck

The immediate mathematical bottleneck is an **original-family invariant of the actual norm and mixed digit-transfer channels**, strong enough to control their relative valuation after actual content and primitive-norm cancellation.

Beyond that remain the full final gcd and the comparison of the actual primitive denominator with the whole nonzero evaluated error.



$$
\boxed{\text{The irrationality of }e+\pi\text{ remains unresolved.}}
$$


