> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A1 turn 8: actual triadic blocks give a uniform growing inverse-propagation bound

I obtain an unconditional, though not sharp, growing endpoint estimate. Put


$$
N=n-1=4^j,\qquad M=\frac{N-1}{3},\qquad j\ge1.
$$


Then


$$
\boxed{
v_3(c\xi_{\rm const}-b\xi_{\rm last})
\ge \left\lceil\frac M4\right\rceil
}
$$


and consequently


$$
\boxed{
v_3(Q_n(-1))
\ge v_3(N!)+\left\lceil\frac{N-1}{12}\right\rceil .
}
\tag{1}
$$



This improves the previously established fixed extra depth to a linearly growing extra depth. It does **not** establish or disprove the proposed doubled-factorial equality.

The essential additional input is indeed the actual disconnected triadic reduction. It permits a convergent inverse expansion in which every transition between distinct triads has positive depth, while long jumps retain the factorial-tail cost. Arbitrarily many returning paths are included.

### 1. Verify the actual triadic reduction

All valuations below are $3$-adic, with $v_3(0)=+\infty$.

Retain the exact transformed moments


$$
\widetilde G=T^{-1}GT^{-T},\qquad
\widetilde t=T^{-1}t,
\qquad T_{ij}=(-2)^i\binom ij.
$$


The moment formulas in the supplied source give


$$
b_s\equiv
\begin{cases}
1,&s\equiv0,2\pmod3,\\
0,&s\equiv1\pmod3.
\end{cases}
$$


Substitution into the exact formulas for $t_s,e_s$ gives


$$
t_s\equiv2,\qquad e_s\equiv-s\pmod3.
\tag{2}
$$


Since $-2\equiv1\pmod3$, Pascal conjugation therefore yields


$$
\widetilde t\equiv2e_0\pmod3,\qquad
\widetilde G\equiv-(2J+N_0+N_0^T)\pmod3,
\tag{3}
$$


where $(N_0)_{i,i-1}=i$.

In particular, the entry connecting indices $i-1,i$ is $-i$, and vanishes when $3\mid i$. The complete triads


$$
I_r=\{3r,3r+1,3r+2\}
$$


are consequently disconnected modulo $3$. Each has residue matrix


$$
D_*=
\begin{pmatrix}
0&2&0\\
2&1&1\\
0&1&2
\end{pmatrix},
\qquad \det D_*=-8\equiv1\pmod3.
\tag{4}
$$


Thus every complete triad is a unit block, uniformly in its position.

These statements also hold at the boundaries of every finite matrix: no infinite-matrix conjugation or missing boundary entry is used.

### 2. True long-jump costs, including the entire factorial tail

For a block or vector, write its valuation for the minimum valuation of its entries. Define


$$
w(r)=\left\lceil\frac r4\right\rceil,\qquad r\ge0.
\tag{5}
$$



I claim that the **actual**, untruncated transformed moments satisfy


$$
\boxed{
v_3(\widetilde G_{I_r,I_s})\ge w(|r-s|)
\quad(r\ne s),
}
\tag{6}
$$


and


$$
\boxed{
v_3(\widetilde t_{I_r})\ge w(r).
}
\tag{7}
$$


The same estimates apply if a final triad is only partially present.

Here is how the factorial tails enter these bounds. For triads at separation $h\ge1$, the minimum index separation is $3h-2$. The established all-depth locality estimate, obtained from the exact


$$
F_\ell(s)=\frac{(s-\ell+1)\cdots(s+\ell)}{\ell!},
$$


therefore gives


$$
v_3(\widetilde G_{I_r,I_s})
\ge v_3\!\left(\left\lfloor\frac{3h-3}{2}\right\rfloor!\right).
\tag{8}
$$


Indeed, taking $L=\lfloor(3h-3)/2\rfloor$, the retained polynomial terms vanish at these entries, and the **sum of all omitted terms** is divisible by $3^{v_3(L!)}$.

For $h\ge3$,


$$
v_3\!\left(\left\lfloor\frac{3h-3}{2}\right\rfloor!\right)
\ge
\left\lfloor\frac{h-1}{2}\right\rfloor
\ge \left\lceil\frac h4\right\rceil .
\tag{9}
$$


For $h=1,2$, (3) supplies depth at least one. This proves (6).

Similarly, indices in $I_r$ are at least $3r$, so locality gives


$$
v_3(\widetilde t_{I_r})
\ge v_3\!\left(\left\lfloor\frac{3r}{2}\right\rfloor!\right)
\ge\left\lfloor\frac r2\right\rfloor.
\tag{10}
$$


For $r\ge2$, this is at least $w(r)$. For $r=1$, use $\widetilde t\equiv2e_0\pmod3$; for $r=0$, integrality suffices.

Thus (6)–(7) retain all factorial-tail jumps. In particular, no polynomial coefficient with a factorial denominator has been assigned an unjustified termwise propagation cost.

### 3. Inverse propagation through the actual complete triads

Let $\mathcal E$ be the transformed principal block on indices


$$
0,\ldots,3M-1.
$$


Partition it into its $M$ complete triads. Let $\mathcal D$ be its exact block-diagonal part, and write


$$
\mathcal E=\mathcal D+\mathcal R
=\mathcal D(I+\mathcal U),
\qquad \mathcal U=\mathcal D^{-1}\mathcal R.
\tag{11}
$$


By (4), every diagonal block of $\mathcal D$ has integral inverse. By (6),


$$
\mathcal U_{rr}=0,\qquad
v_3(\mathcal U_{rs})\ge w(|r-s|)\ge1
\quad(r\ne s).
\tag{12}
$$


Consequently the exact $3$-adic inverse is


$$
\mathcal E^{-1}
=\sum_{m=0}^{\infty}(-\mathcal U)^m\mathcal D^{-1}.
\tag{13}
$$



This series controls all paths, not just paths with increasing block indices. A nonzero path


$$
r=r_0,r_1,\ldots,r_m=s
$$


has valuation at least


$$
\sum_{\nu=1}^{m}w(|r_\nu-r_{\nu-1}|)
\ge
\left\lceil
\frac{\sum_{\nu=1}^{m}|r_\nu-r_{\nu-1}|}{4}
\right\rceil
\ge w(|r-s|).
\tag{14}
$$


It also has valuation at least $m$. The latter bound proves convergence, including paths with arbitrarily many returns. Internal motion and all internal loops within a triad have already been incorporated in the exact integral inverse $\mathcal D_{rr}^{-1}$.

The nonarchimedean triangle inequality preserves (14) under every finite path sum and its convergent limit. Hence


$$
\boxed{
v_3((\mathcal E^{-1})_{rs})\ge w(|r-s|).
}
\tag{15}
$$



This is an inverse estimate with its actual hypotheses proved. The generic band-inverse counterexample from the previous turn is inapplicable because here all inter-triad transitions are divisible by $3$.

### 4. Constant-to-tail contractions acquire growing depth

Set


$$
u=\mathcal E^{-1}\widetilde t_E.
$$


For each block $r<M$, (7) and (15) imply


$$
\begin{aligned}
v_3(u_{I_r})
&\ge\min_{0\le s<M}\{w(|r-s|)+w(s)\}\\
&\ge w(r).
\end{aligned}
\tag{16}
$$



Now consider either of the two indices


$$
L=3M,\qquad U=3M+1,
$$


in the final partial triad $I_M$. Its constant coupling after eliminating $\mathcal E$ is


$$
\widehat t_i
=\widetilde t_i-\widetilde G_{i,E}\mathcal E^{-1}\widetilde t_E,
\qquad i=L,U.
\tag{17}
$$


The direct term has depth at least $w(M)$. Each block contribution in the contraction has depth at least


$$
w(M-r)+w(r)\ge w(M).
$$


Thus


$$
\boxed{
v_3(\widehat t_L),\ v_3(\widehat t_U)\ge w(M).
}
\tag{18}
$$



These are estimates for the actual eliminated moments, not just their direct couplings.

### 5. Transfer back to the requested Schur numerator

The Pascal transformation is lower triangular over $\mathbb Z_3$, with unit diagonal. It leaves the constant polynomial unchanged, and the first $3M$ transformed nonconstant polynomials span exactly the same module as the original elimination block.

Write $\phi=T\psi$ for the original and transformed nonconstant bases. Modulo the eliminated subspace,


$$
\phi_L=T_{LL}\psi_L,\qquad
\phi_U=T_{UL}\psi_L+T_{UU}\psi_U.
\tag{19}
$$


Here $T_{LL},T_{UU}$ are units and $T_{UL}$ is integral. Bilinearity of the residual pairing therefore gives


$$
b=T_{LL}\widehat t_L,\qquad
\xi_{\rm const}=T_{UL}\widehat t_L+T_{UU}\widehat t_U.
$$


Consequently,


$$
\boxed{
v_3(b),\ v_3(\xi_{\rm const})\ge w(M).
}
\tag{20}
$$



The other two residual quantities $c,\xi_{\rm last}$ are integral, because they are obtained by eliminating a unit block from integral divided moments. Hence


$$
v_3(c\xi_{\rm const}-b\xi_{\rm last})\ge w(M).
\tag{21}
$$


Combining this with the established exact primitive-content identity


$$
v_3(Q_n(-1))
=v_3(N!)+v_3(c\xi_{\rm const}-b\xi_{\rm last})
$$


proves (1).

The numerator in (21) is nonzero: the established orthogonal-modification identity gives $Q_n(-1)\ne0$, and its exact Schur expression has nonzero denominator.

### 6. Scope and arithmetic interface

The new bound is deliberately conservative:


$$
v_3(Q_n(-1))
\ge v_3(N!)+\frac{N}{12}-O(1),
\qquad N=4^j.
$$


It does not explain the reported finite values $2,12,60$, which are substantially stronger. In particular, it supplies no symbolic obstruction to doubled-factorial depth; that conjectural equality remains open.

For the complete rational-arctangent endpoint construction, retain


$$
A=t_R\det K-z^T\operatorname{adj}(K)z,\qquad
B=\ell Q_n(-1)\det K,
$$


and the **actual final normalization**


$$
g=\gcd(|A|,|B|),\qquad
q=\frac{|B|}{g},\qquad
p=-\frac{\operatorname{sgn}(B)A}{g}.
\tag{22}
$$


The new result implies


$$
v_3(B)\ge
v_3(\ell)+v_3(N!)
+\left\lceil\frac{N-1}{12}\right\rceil
+v_3(\det K).
\tag{23}
$$


It does not by itself bound


$$
v_3(q)=\max\{0,v_3(B)-v_3(A)\};
$$


the final gcd remains essential.

With $k=(n+1)/2$, the whole evaluated error is still


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B)}g\bigl(A+B(e+\pi)\bigr)
=
\frac{\operatorname{sgn}(B)\ell^k}{g}\det H_{\rm complete}.
}
\tag{24}
$$


Here $H_{\rm complete}$ is the full exponential-plus-arctangent integral matrix, including every rational arctangent term in its decomposition. On $n=4^j+1,\ j\ge1$, the accepted distinct-center and nonvanishing results give $B\ne0$ and nonzero whole error except possibly at one index. No decay conclusion for (24), and no decision on irrationality, follows from the new estimate.

## Closing ledger

### (1) New result and proof status

**Proved uniformly:** actual triadic inverse propagation (15), the constant-to-tail contraction bound (18), and


$$
\boxed{
v_3(Q_{4^j+1}(-1))
\ge v_3((4^j)!)+\left\lceil\frac{4^j-1}{12}\right\rceil,
\qquad j\ge1.
}
$$


All factorial tails and all inverse paths, including returning paths, are controlled. This is an infinite theorem, not an extrapolation from finite controls.

### (2) Exact remaining bottleneck

The coarse jump weight $w(r)=\lceil r/4\rceil$ loses substantial arithmetic information. Reaching doubled-factorial depth requires sharper actual jump costs or cancellations among paths; the present argument proves neither saturation nor the first nonzero endpoint unit.

Separately, even a sharp endpoint-depth theorem must be combined with the complete relative determinant valuations and the final gcd in (22) before it yields an actual-denominator or shrinking-whole-error theorem.

### (3) Computation request

**None.** The growing replacement follows symbolically from the exact moment tails and the verified triadic residue structure.
