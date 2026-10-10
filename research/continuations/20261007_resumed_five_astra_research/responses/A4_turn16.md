> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Audit of the even-contact moment lattice and new arithmetic information for the actual compact determinant

## 1. Executive conclusion and proof status

The parent’s even-contact lattice note is mathematically sound at its stated structural scope. In particular:

- the contact functional is the **complete signed functional**
  

$$
\lambda=\mu-\delta_{-1},
$$


  not a factorial approximation to it;
- $C_k=B_k-vv^{T}$ is nonsingular for every $k\ge2$, has negative determinant, and has inertia $(k-1,1,0)$;
- the stated primitive polynomial row clearers and high-coefficient lattice index are correct;
- both bounds proving
  

$$
\log|\det C_k|=2k^2\log k+O(k^2)
$$


  are valid, including the box restriction, permutation factor, and cofactor estimate.

There are, however, two important limitations.

1. The JSON file supplies numerical assertions, not independently inspectable Smith transformations or equivalent arithmetic certificates. I audit its interpretation and consequences below, but do **not** claim to have independently reproduced its large determinants and invariant factors. No closed table is rerun.
2. Nonsingularity of $C_k$ is not nonvanishing of the actual compact determinant. The two determinants represent different pairings.

This report adds three results concerning the **actual compact determinant**, rather than only its contact matrix.

### New proved results

1. **Exact frame-index factor in the final scalar gcd.**  
   The integer rows obtained by individually clearing the monic contact rows have index
   

$$
J_k=\frac{\prod_{m=k}^{2k-1}d_m}{I_k},
   \qquad
   I_k=\frac{|\det C_k|}{\delta_k},
$$


   in the saturated integer contact lattice. After a specified common moment clearing, $J_k$ divides **both actual scalar coefficients** of the compact determinant. More precisely, their gcd is exactly $J_k$ times the gcd obtained from a saturated basis. This is an ALL-prime identity.

2. **An exact whole signed-integral formula.**  
   The actual compact determinant is a difference of two explicitly specified multiple integrals, one from the positive measure $\mu$, and one from the negative mass at $-1$. The identity includes the full compact weight. It also identifies precisely why ordinary Gram positivity does not prove its sign.

3. **A unique-boundary-pole lemma, with a new finite arithmetic consequence at $k=3$.**  
   If $p=6k-5$ is prime and $p\nmid\det C_k$, then the only possible $p$-pole among the complete rational entries occurs in the physical bottom-right entry. Its residue is $4$, and the determinant residue is $4$ times a specified leading minor. At $k=3$, an explicit calculation modulo $13$ gives
   

$$
13\,\mathcal D_3(X)\equiv X+7\pmod {13}.
$$


   Consequently the actual affine determinant has nonzero slope, its coefficient pair has an exact simultaneous $13$-denominator of exponent one, and its primitive rational zero has denominator prime to $13$, with residue $6\bmod13$.

The last result is a finite arithmetic theorem for the actual coefficient pair. It is **not** a proof that $\mathcal D_3(e+\pi)\ne0$, and none of the new results establishes primitive whole-error decay on an infinite sequence.

The rationality or irrationality of $e+\pi$ remains unresolved.

---

## 2. Exact objects, domains, and degree boundaries

Throughout the compact construction,


$$
k\ge2,\qquad 0\le i,j<k,\qquad k\le m\le2k-1.
$$


These are the parent’s compact-family indices. They are not identified with the original binary producer or with A2’s different Laguerre construction.

Define


$$
a_d=\sum_{j=0}^{d}(-1)^j\frac{d!}{(d-j)!}.
$$


For a polynomial $P$,


$$
\mathcal A(P)=\sum_{j=0}^{\deg P}(-1)^jP^{(j)}(1).
$$


The supplied gamma-integral identity, which also follows immediately by finite Taylor expansion, is


$$
\mathcal A(P)
=\int_0^\infty e^{-u}P(1-u)\,du
=e^{-1}\int_{-\infty}^{1}e^tP(t)\,dt.
$$



Let $\mu$ be the pushforward of $e^{t-1}\,dt$ on $(-\infty,1]$ under $x=t^2$. Then


$$
\int x^\ell\,d\mu(x)=a_{2\ell}.
$$


It is a positive probability measure of infinite support on $[0,\infty)$.

For a polynomial $p(x)$, put


$$
\lambda(p)=\int p\,d\mu-p(-1).
$$


Thus


$$
c_\ell=\lambda(x^\ell)=a_{2\ell}-(-1)^\ell.
$$


The contact equations are exactly


$$
\lambda(x^jp)=0,\qquad 0\le j<k.
$$



The compact positive measure used for the **evaluated** determinant is


$$
\int f(x)\,d\nu(x)
=
\int_0^1
\left(e^t+\frac4{1+t^2}\right)f(t^2)\,dt.
$$


Its support is $[0,1]$.

Define


$$
C=C_k=(c_{i+j})_{0\le i,j<k},
\qquad
w_m=(c_m,\ldots,c_{m+k-1})^T,
$$


and


$$
p_m(x)=x^m-(1,x,\ldots,x^{k-1})C^{-1}w_m.
$$



The actual compact matrix and determinant are


$$
H_{rj}=\int p_{k+r}(x)x^j\,d\nu(x),
\qquad
\mathcal D_k=\det H,
\qquad 0\le r,j<k.
$$



### Exact degree audit

| Object | Largest $x$-moment index | Largest corresponding $t$-degree |
|---|---:|---:|
| $C_k$ | $2k-2$ | $4k-4$ |
| $w_{2k-1}$, hence $[C_k\mid W]$ | $3k-2$ | $6k-4$ |
| $p_m$ | $m\le2k-1$ | $2m\le4k-2$ |
| $p_m(x)x^j$ in the compact matrix | $m+j\le3k-2$ | $6k-4$ |
| Low-degree correction in $p_mx^j$ | $2k-2$ | $4k-4$ |

No successor row or additional moment is needed beyond these boundaries.

---

## 3. Audit of the complete contact matrix

### 3.1 The signed rank-one modification is exact

Let


$$
B_k=(a_{2i+2j})_{0\le i,j<k},
\qquad
v=(1,-1,\ldots,(-1)^{k-1})^T.
$$


For coefficient vectors $\alpha,\beta$, representing polynomials $f,g$ of degree below $k$,


$$
\alpha^TB_k\beta=\int fg\,d\mu,
$$


and


$$
\alpha^Tvv^T\beta=f(-1)g(-1).
$$


Therefore


$$
C_k=B_k-vv^T
$$


is the Gram matrix of the complete signed functional $\lambda$.

This validates the parent’s central identification. Omitting $vv^T$ would change the problem.

### 3.2 Positive definiteness of $B_k$

For nonzero $f$ of degree below $k$,


$$
\int f^2\,d\mu>0,
$$


because $\mu$ has infinite support and a nonzero polynomial has only finitely many zeros. Hence $B_k$ is positive definite at every size.

### 3.3 Reproducing-kernel monotonicity

The evaluation norm is


$$
K_k=v^TB_k^{-1}v
=
\sup_{\substack{f\ne0\\\deg f<k}}
\frac{|f(-1)|^2}{\int f^2\,d\mu}.
$$


Nested polynomial spaces immediately give $K_{k+1}\ge K_k$.

In fact the monotonicity is strict. Let $\pi_j$ be the monic orthogonal polynomial of degree $j$ for $\mu$, and let


$$
h_j=\int\pi_j^2\,d\mu>0.
$$


Orthogonal expansion gives


$$
K_k=\sum_{j=0}^{k-1}\frac{\pi_j(-1)^2}{h_j}.
$$


Moreover $\pi_j(-1)\ne0$. Otherwise


$$
\pi_j(x)=(x+1)q(x),\qquad \deg q=j-1,
$$


and orthogonality would imply


$$
0=\int\pi_jq\,d\mu
=\int(x+1)q^2\,d\mu>0,
$$


a contradiction. Thus


$$
K_{k+1}-K_k=\frac{\pi_k(-1)^2}{h_k}>0.
$$



The parent needs only weak monotonicity; its use is valid.

### 3.4 The exceptional size $k=1$

Here


$$
B_1=(1),\qquad K_1=1,\qquad C_1=(0).
$$


Thus the low-degree pivot matrix is singular.

This does **not** mean that the complete one-contact functional vanishes on all polynomials. For example $c_1=2$. Rather, the particular monic pivot construction using $C_1^{-1}$ is unavailable. On polynomials of degree at most one, the contact equation forces the coefficient of $x$ to vanish, so the contact space consists of constants.

The parent correctly excludes this size from its inverse construction.

### 3.5 All-size determinant sign and inertia

At $k=2$,


$$
B_2=\begin{pmatrix}1&1\\1&9\end{pmatrix},
\qquad
K_2=\frac32.
$$


Hence $K_k\ge3/2$ for every $k\ge2$.

The determinant lemma gives


$$
\det C_k=(1-K_k)\det B_k<0.
$$


Also


$$
B_k^{-1/2}C_kB_k^{-1/2}=I-ww^T,
\qquad w=B_k^{-1/2}v.
$$


Its eigenvalues are $1$, with multiplicity $k-1$, and $1-K_k<0$. Congruence preserves inertia, so


$$
\operatorname{inertia}(C_k)=(k-1,1,0).
$$



These conclusions are rigorous for every $k\ge2$.

---

## 4. Contact rows, primitive clearers, and saturation

### 4.1 Verification of every contact equation

Write


$$
\alpha_m=C^{-1}w_m.
$$


For $0\le j<k$,


$$
\lambda(x^jp_m)
=c_{m+j}-\sum_{i=0}^{k-1}(\alpha_m)_i c_{i+j}
=0.
$$


Thus all $k$ equations are satisfied.

The rows $p_k,\ldots,p_{2k-1}$ have distinct monic leading terms. They are linearly independent. The contact map from polynomials of degree at most $2k-1$ has rank $k$, since its first $k$ columns form $C$. Its kernel therefore has dimension $k$, proving that these rows form a rational basis.

### 4.2 Actual primitive polynomial clearer

Let $D=\det C$, and set


$$
b_m=\operatorname{adj}(C)w_m\in\mathbb Z^k.
$$


Then the exact least coefficient clearer is


$$
\boxed{
d_m=
\frac{|D|}
{\gcd\bigl(|D|,(b_m)_0,\ldots,(b_m)_{k-1}\bigr)}.
}
$$


This is equivalent to the lcm of the reduced denominators of $C^{-1}w_m$.

The polynomial $d_mp_m$ is primitive. If an integer $g>1$ divided all its coefficients, it would divide its leading coefficient $d_m$, and $(d_m/g)p_m$ would be integral, contradicting minimality.

The least simultaneous polynomial clearer for these monic rows is therefore


$$
\operatorname{lcm}_{k\le m<2k}d_m.
$$


Neither $|D|$ nor $\prod d_m$ is automatically that least clearer.

### 4.3 Saturated contact lattice and its projection

Put


$$
W=(w_k,\ldots,w_{2k-1}),
\qquad T=[C\mid W].
$$


Let $\delta=\delta_k$ be the gcd of all maximal minors of $T$. Since $T$ has rank $k$,


$$
[\mathbb Z^k:\operatorname{im}T]=\delta.
$$



The allowed high-coefficient lattice is


$$
L_k=\{h\in\mathbb Z^k:Wh\in C\mathbb Z^k\}.
$$


The map


$$
h\longmapsto Wh+C\mathbb Z^k
$$


has kernel $L_k$ and image


$$
\operatorname{im}T/C\mathbb Z^k.
$$


Consequently


$$
\boxed{
I_k:=[\mathbb Z^k:L_k]
=\frac{|\det C_k|}{\delta_k}.
}
$$



This proves the parent’s index formula.

### 4.4 Independent primitive rows are generally not a saturated basis

Let


$$
\mathscr K_k=\ker_{\mathbb Z}T\subset\mathbb Z^{2k}.
$$


Projection onto the high coefficients identifies $\mathscr K_k$ with $L_k$.

The rows $d_mp_m$ project to


$$
d_ke_0,\ldots,d_{2k-1}e_{k-1}.
$$


Therefore their row lattice has index


$$
\boxed{
J_k=
[\mathscr K_k:\langle d_kp_k,\ldots,d_{2k-1}p_{2k-1}\rangle_{\mathbb Z}]
=
\frac{\prod_{m=k}^{2k-1}d_m}{I_k}.
}
$$


In particular $J_k$ is an integer.

This is the additional index that must not be confused with $I_k$. The parent’s statement that its rows need not be saturated is correct; the displayed formula makes that distinction quantitative.

---

## 5. Audit of both raw-height bounds

### 5.1 Lower bound by restriction of the positive measure

For a polynomial $f(x)$,


$$
\int f(x)^2\,d\mu(x)
=e^{-1}\int_{-\infty}^{1}e^t f(t^2)^2\,dt.
$$


Restricting to $t\le0$, and writing $t=-s$, gives


$$
\int f^2\,d\mu
\ge e^{-1}\int_0^\infty e^{-s}f(s^2)^2\,ds.
$$


Thus


$$
B_k\succeq e^{-1}E_k,
\qquad
E_k=((2i+2j)!)_{0\le i,j<k}.
$$


Both matrices are positive definite, so


$$
\det B_k\ge e^{-k}\det E_k.
$$



The finite Gram determinant identity gives


$$
\det E_k
=
\frac1{k!}
\int_{[0,\infty)^k}
e^{-\sum_i s_i}
\prod_{i<j}(s_j^2-s_i^2)^2\,ds_1\cdots ds_k.
$$



Restrict first to


$$
s_i\in[i,i+\tfrac14],\qquad 1\le i\le k.
$$


The integrand is symmetric. The $k!$ permutations of this box are disjoint except on null boundaries and have equal integrals. Therefore their sum cancels the prefactor $1/k!$.

For $i<j$,


$$
s_j-s_i\ge j-i-\frac14\ge\frac34(j-i),
\qquad
s_i+s_j\ge i+j.
$$


The box has volume $4^{-k}$, and


$$
e^{-\sum_i s_i}
\ge
\exp\!\left(-\frac{k(k+1)}2-\frac k4\right).
$$


It follows that


$$
\begin{aligned}
\log\det E_k
\ge{}&
2\sum_{i<j}\log(j-i)
+
2\sum_{i<j}\log(i+j)
-O(k^2)\\
\ge{}&
2\sum_{j=1}^{k-1}\log(j!)
+
2\sum_{j=2}^{k}(j-1)\log j
-O(k^2).
\end{aligned}
$$


The two displayed sums each have leading term $k^2\log k$:


$$
2\sum_{j=1}^{k-1}\log(j!)
=k^2\log k+O(k^2),
$$




$$
2\sum_{j=2}^{k}(j-1)\log j
=k^2\log k+O(k^2).
$$


Hence


$$
\log\det B_k\ge2k^2\log k-O(k^2).
$$


Finally,


$$
|\det C_k|=(K_k-1)\det B_k\ge\frac12\det B_k.
$$



The box and permutation arguments are valid exactly as stated in the parent note.

### 5.2 Upper bound by cofactors

Since $B_k$ is positive definite,


$$
\operatorname{adj}(B_k)=\det(B_k)B_k^{-1}
$$


is positive definite. Therefore


$$
|\operatorname{adj}(B_k)_{ij}|
\le
\sqrt{\operatorname{adj}(B_k)_{ii}
      \operatorname{adj}(B_k)_{jj}}.
$$


Hadamard’s inequality on each principal cofactor gives


$$
\operatorname{adj}(B_k)_{ii}
\le\prod_{\ell\ne i}a_{4\ell}.
$$


All $a_{4\ell}\ge1$, so every absolute cofactor is at most


$$
P_k=\prod_{\ell=0}^{k-1}a_{4\ell}.
$$


Also $\det B_k\le P_k$. Thus


$$
|\det C_k|
=
\left|\det B_k-v^T\operatorname{adj}(B_k)v\right|
\le(1+k^2)P_k.
$$


Since $a_{4\ell}\le(4\ell)!$,


$$
|\det C_k|
\le(1+k^2)\prod_{\ell=0}^{k-1}(4\ell)!.
$$


Stirling’s formula yields


$$
\sum_{\ell=0}^{k-1}\log((4\ell)!)
=2k^2\log k+O(k^2).
$$



Combining both bounds proves


$$
\boxed{\log|\det C_k|=2k^2\log k+O(k^2).}
$$



This is a theorem about **raw contact height only**. It does not estimate $\delta_k$, $I_k$, the least clearers, or the final primitive scalar denominator.

---

## 6. Audit of the bounded saturation file

The intended interpretation of `full_contact_invariants` must be the nonzero Smith invariants of the rectangular matrix


$$
[C_k\mid W].
$$


They cannot be the Smith invariants of $C_k$: their products are the listed $\delta_k$, not generally $|\det C_k|$.

At that interpretation, the file’s claims have the correct logical form:

- the product of the rectangular Smith invariants is $\delta_k$;
- $\delta_k\mid|\det C_k|$;
- $I_k=|\det C_k|/\delta_k$;
- every $d_m$ divides $I_k$, because $d_m$ is the order of a coordinate generator in the finite quotient $\mathbb Z^k/L_k$.

The displayed invariant sequences have the required divisibility ordering. Nothing in the file’s format contradicts the proved lattice identities.

However, the supplied JSON contains neither unimodular Smith transformations nor another independently checkable certificate establishing its large integer outputs. Its `all_contact_checks_passed` flags are assertions, not proofs. Under the instruction not to rerun the closed table, the correct status is:

> **Finite receipts supplied by the parent; their mathematical interpretation is validated here, but their large numerical outputs are not independently recertified in this response.**

### Conditional consequences of those finite receipts

If the listed clearers are correct, then for every listed size


$$
\operatorname{lcm}_m d_m=I_k.
$$


Moreover, because at least one coordinate generator has order $I_k$, the quotient $\mathbb Z^k/L_k$ is cyclic at those sizes.

The corresponding independent-row indices are


$$
J_k=I_k^{\,k-1}
$$


for the listed sizes other than $k=7$, while at $k=7$ the last clearer is $I_7/13$, giving


$$
J_7=\frac{I_7^6}{13}.
$$



These are finite conditional deductions. They do not prove eventual cyclicity, an asymptotic formula for $I_k$, or a formula for the final scalar gcd.

---

## 7. Complete affine formula for the actual compact matrix

Define the full rational moment term


$$
r_\ell
=-(2\ell)!
+
4\sum_{h=0}^{\ell-1}
\frac{(-1)^h}{2\ell-1-2h},
\qquad r_0=-1.
$$


Both endpoint contributions are present.

The exact raw even moment is


$$
\int_0^1
\left(e^t+\frac4{1+t^2}\right)t^{2\ell}\,dt
=
a_{2\ell}e+(-1)^\ell\pi+r_\ell.
$$


Let $\rho$ be the rational functional defined by


$$
\rho(x^\ell)=r_\ell.
$$


For a contact row,


$$
\int p_m(x)x^j\,d\nu(x)
=
p_m(-1)(-1)^j(e+\pi)+\rho(p_mx^j).
$$


Therefore, with an indeterminate $X$,


$$
H_k(X)_{rj}
=
u_rv_jX+R_{rj},
\quad
u_r=p_{k+r}(-1),
\quad
R_{rj}=\rho(p_{k+r}x^j),
$$


and


$$
\mathcal D_k(X)=\det H_k(X)
$$


is affine. The evaluated determinant is $\mathcal D_k(e+\pi)$.

The rank-one period matrix is in fact nonzero at every size. For $m=k$, let $\pi_k$ be the monic $\mu$-orthogonal polynomial. If $K_k(x,-1)$ denotes the reproducing-kernel polynomial, then


$$
p_k(x)
=
\pi_k(x)+
\frac{\pi_k(-1)}{1-K_k}K_k(x,-1).
$$


Evaluation at $-1$ gives


$$
p_k(-1)=\frac{\pi_k(-1)}{1-K_k}\ne0.
$$


Thus the period matrix has rank exactly one.

Nevertheless, the determinant’s slope can vanish even when its period matrix has rank one. The relevant cofactors can cancel. No determinant nonvanishing follows from this observation alone.

---

## 8. New arithmetic theorem: the frame index is an exact scalar-gcd factor

Set


$$
\mathscr L_k=\operatorname{lcm}\{1,3,5,\ldots,6k-5\}.
$$


Every $r_\ell$ needed by the complete finite matrix has denominator dividing $\mathscr L_k$.

For an integer contact row $f$, all coefficients of


$$
\mathscr L_k\bigl(f(-1)(-1)^jX+\rho(fx^j)\bigr)
$$


are integers.

### Theorem 8.1 — Exact gcd change under passage to a saturated contact basis

Let $f_r=d_{k+r}p_{k+r}$, and let $g_0,\ldots,g_{k-1}$ be any integer basis of the saturated lattice $\mathscr K_k$. Form the two integer affine determinants


$$
F_k(X)
=
\det_{r,j}
\left[
\mathscr L_k
\bigl(f_r(-1)(-1)^jX+\rho(f_rx^j)\bigr)
\right]
$$


and


$$
S_k(X)
=
\det_{r,j}
\left[
\mathscr L_k
\bigl(g_r(-1)(-1)^jX+\rho(g_rx^j)\bigr)
\right].
$$


Then


$$
F_k(X)=\pm J_kS_k(X).
$$


If


$$
F_k(X)=U_FX-V_F,\qquad S_k(X)=U_SX-V_S,
$$


then


$$
\boxed{
\gcd(|U_F|,|V_F|)
=
J_k\,\gcd(|U_S|,|V_S|).
}
$$



#### Proof

Because the $g_r$ form an integer basis of $\mathscr K_k$, there is an integer matrix $M$ such that


$$
(f_0,\ldots,f_{k-1})^T=M(g_0,\ldots,g_{k-1})^T.
$$


The index calculation gives


$$
|\det M|=J_k.
$$


The complete compact pairing is linear in each row, including both its rational and period coefficients. Hence its matrices satisfy


$$
N_F(X)=MN_S(X),
$$


and their determinants differ by $\det M=\pm J_k$. The gcd identity follows prime by prime, or directly from multiplication of both integers by the same integer. ∎

This is not an assertion that the actual row clearers are small. It identifies a compulsory cancellation in the **actual two scalar coefficients** when one uses the nonsaturated primitive-row frame.

### A basis-free version

Define the $2k\times2k$ integer polynomial matrix


$$
\mathcal B_k(X)=
\begin{pmatrix}
(c_{i+\ell})_{\substack{0\le i<k\\0\le\ell<2k}}\\[1mm]
\bigl(\mathscr L_k[r_{j+\ell}+(-1)^{j+\ell}X]\bigr)_
{\substack{0\le j<k\\0\le\ell<2k}}
\end{pmatrix}.
$$


A Schur complement in its first $k$ columns gives


$$
\boxed{
\det\mathcal B_k(X)
=
\det C_k\,\mathscr L_k^k\,\mathcal D_k(X).
}
$$


Laplace expansion along its top $k$ rows shows that every coefficient of $\det\mathcal B_k(X)$ is divisible by $\delta_k$.

More precisely, up to a common sign,


$$
\frac{\det\mathcal B_k(X)}{\delta_k}
=
S_k(X).
$$


Thus division by $\delta_k$ is not a guessed cancellation: it is exactly the transition to the saturated contact volume.

What remains unknown is the gcd of the two coefficients **after** that division. The theorem exposes a forced part of the gcd, not the complete answer.

---

## 9. New exact whole signed-integral identity

The block determinant also gives an exact integral representation for the whole evaluated determinant.

For a tuple $z=(z_1,\ldots,z_m)$, write


$$
V(z)=\prod_{i<j}(z_j-z_i).
$$



Define


$$
\begin{aligned}
\mathcal I_k={}&
\frac1{k!^2}
\int
V(x)^2V(y)^2
\prod_{i=1}^{k}\prod_{j=1}^{k}(y_j-x_i)\,
d\mu^k(x)\,d\nu^k(y),
\\[1mm]
\mathcal J_k={}&
\frac1{(k-1)!k!}
\int
V(x)^2V(y)^2
\prod_{i=1}^{k-1}(x_i+1)^2
\prod_{j=1}^{k}(y_j+1)
\\
&\hspace{24mm}\cdot
\prod_{i=1}^{k-1}\prod_{j=1}^{k}(y_j-x_i)\,
d\mu^{k-1}(x)\,d\nu^k(y).
\end{aligned}
$$



### Theorem 9.1 — Whole signed integral

For every $k\ge2$,


$$
\boxed{
\det C_k\,\mathcal D_k(e+\pi)
=
\mathcal I_k-\mathcal J_k.
}
$$



#### Derivation

Consider the block moment determinant with top rows $\lambda(x^i\cdot)$ and bottom rows $\nu(x^j\cdot)$, both for $0\le i,j<k$, acting on monomials of degree $0,\ldots,2k-1$. Its Schur complement is $H_k(e+\pi)^T$, so its determinant is


$$
\det C_k\,\mathcal D_k(e+\pi).
$$



Expanding the two row groups by the finite determinant integral identity gives


$$
\frac1{k!^2}
\int
V(x)^2V(y)^2
\prod_{i,j}(y_j-x_i)\,
d\lambda^k(x)\,d\nu^k(y).
$$


Now use $\lambda=\mu-\delta_{-1}$.

Terms with two or more coordinates equal to $-1$ vanish because of $V(x)^2$. The term with no atom is $\mathcal I_k$. There are $k$ equal terms with one atom, each carrying a minus sign. Fixing that atom at $-1$ produces


$$
\prod_i(x_i+1)^2\prod_j(y_j+1),
$$


and changes the factor $1/k!^2$ to $1/((k-1)!k!)$. This is exactly $-\mathcal J_k$. All integrals converge because only finite polynomial moments occur. ∎

### Precise positivity obstruction

Neither $\mathcal I_k$ nor $\mathcal J_k$ is automatically nonnegative. Although $V(x)^2$, $V(y)^2$, and the factors involving $x_i+1,y_j+1$ are nonnegative, the cross product


$$
\prod_{i,j}(y_j-x_i)
$$


changes sign: $\mu$ has support both inside and outside the support $[0,1]$ of $\nu$.

Moreover, the atom contribution must be subtracted. Dropping it would replace the complete contact functional by a different one.

Thus a Gram or Christoffel identity does expose the whole signed integral, but ordinary norm positivity does not settle its sign. A sufficient new analytic lemma would be a strict comparison


$$
\mathcal I_k\ne\mathcal J_k
$$


on a specified infinite set, preferably with a quantitative estimate surviving the final primitive normalization.

---

## 10. New boundary-pole theorem for the actual coefficient pair

The complete rational terms permit a local arithmetic statement that does not follow from contact nonsingularity.

### Theorem 10.1 — Unique physical-corner pole

Suppose


$$
p=6k-5
$$


is prime and


$$
p\nmid\det C_k.
$$


Let $\mathbb Z_{(p)}$ denote the rationals with denominator prime to $p$.

Then:

1. all coefficients of every $p_m$, $k\le m<2k$, belong to $\mathbb Z_{(p)}$;
2. every entry of $H_k(X)$, except possibly the bottom-right entry, lies in $\mathbb Z_{(p)}[X]$;
3. the bottom-right entry has the form
   

$$
H_{k-1,k-1}(X)=\frac4p+h(X),
   \qquad h(X)\in\mathbb Z_{(p)}[X];
$$


4. if
   

$$
M_k(X)=
   \det H_k(X)_{\{0,\ldots,k-2\},\{0,\ldots,k-2\}},
$$


   then
   

$$
\boxed{
   p\,\mathcal D_k(X)\equiv4M_k(X)\pmod p.
   }
$$



#### Proof

The first assertion follows from $C^{-1}=\operatorname{adj}(C)/\det C$.

The largest rational moment index is


$$
\ell=3k-2.
$$


In $r_{3k-2}$, the first arctangent denominator is


$$
2(3k-2)-1=6k-5=p,
$$


and its coefficient is $4/p$. Every other denominator in that moment is a smaller positive odd number. Every moment $r_\ell$ with $\ell<3k-2$ has all its denominators below $p$.

The index $3k-2$ occurs only from the monic leading term of $p_{2k-1}x^{k-1}$, namely in the bottom-right entry. All low-degree corrections have moment index at most $2k-2$, so none can contribute a $p$-pole.

Expansion along the bottom-right entry now gives


$$
\mathcal D_k(X)=\frac4pM_k(X)+N_k(X),
\qquad N_k(X)\in\mathbb Z_{(p)}[X].
$$


Multiplication by $p$ and reduction proves the congruence. ∎

This retains the physical corner and the complete rational forcing. It would be false to replace the bottom-right entry by a truncated moment.

---

## 11. A new finite consequence at $k=3$

Here $p=13$. The following is a small hand derivation for the new boundary-residue question, not a rerun of the closed saturation table.

Modulo $13$, the recurrence


$$
a_d=1-da_{d-1}
$$


gives


$$
C_3\equiv
\begin{pmatrix}
0&2&8\\
2&8&6\\
8&6&12
\end{pmatrix},
\qquad
\det C_3\equiv9\ne0.
$$


Solving the contact equations modulo $13$ gives


$$
\begin{aligned}
p_3(x)&\equiv x^3+4x^2+7x+6,\\
p_4(x)&\equiv x^4+11x^2+2x+2,\\
p_5(x)&\equiv x^5+9x^2+7x+12.
\end{aligned}
$$


Their evaluations at $-1$ are


$$
p_3(-1)\equiv2,\qquad
p_4(-1)\equiv12,\qquad
p_5(-1)\equiv0.
$$



From the complete formula for $r_\ell$,


$$
(r_0,r_1,r_2,r_3,r_4,r_5,r_6)
\equiv(12,2,8,8,1,11,8)\pmod {13}.
$$


Only $r_7$ has a $13$-pole, with residue $4$.

For the leading $2\times2$ minor, direct linear combination gives


$$
\begin{pmatrix}
\rho(p_3)&\rho(xp_3)\\
\rho(p_4)&\rho(xp_4)
\end{pmatrix}
\equiv
\begin{pmatrix}
9&10\\
0&2
\end{pmatrix}.
$$


Including the complete period coefficients,


$$
M_3(X)\equiv
\det
\begin{pmatrix}
9+2X&10-2X\\
12X&2-12X
\end{pmatrix}
\equiv5+10X.
$$


The boundary-pole theorem therefore gives


$$
\boxed{
13\,\mathcal D_3(X)\equiv4(5+10X)\equiv7+X\pmod {13}.
}
$$



### Exact arithmetic consequences

Write


$$
\mathcal D_3(X)=A_3+B_3X,\qquad A_3,B_3\in\mathbb Q.
$$


Then


$$
v_{13}(A_3)=v_{13}(B_3)=-1.
$$


In particular,


$$
B_3\ne0.
$$



Let $h$ be the actual least simultaneous denominator clearer of $A_3,B_3$, and write


$$
h\mathcal D_3(X)=a+bX,\qquad a,b\in\mathbb Z.
$$


Then $v_{13}(h)=1$, while both $a$ and $b$ are $13$-adic units. Hence the final ALL-prime gcd $\gcd(a,b)$ has no factor $13$.

The primitive rational zero $-a/b$ consequently has denominator prime to $13$, and


$$
-\frac ab\equiv-7\equiv6\pmod {13}.
$$



This is genuine information about the actual final coefficient pair. It does not prove that the evaluated number $\mathcal D_3(e+\pi)$ is nonzero: it only restricts the rational number at which this particular affine polynomial could vanish.

---

## 12. Exact contents, simultaneous clearer, primitive denominator, and whole error

The preceding structural gcd factor must not replace the remaining exact payments.

For clarity, the complete bookkeeping can be specified without assuming those quantities are small.

Let


$$
f_r=d_{k+r}p_{k+r},\qquad
u_r=f_r(-1),\qquad
E_{rj}=\mathscr L_k\,\rho(f_rx^j)\in\mathbb Z.
$$



### 12.1 Actual least coefficient-pair clearers

For the original monic row $p_{k+r}$, its period and rational coefficients have the common presentation


$$
\frac{\mathscr L_ku_r}{\mathscr L_kd_{k+r}},
\qquad
\frac{E_{rj}}{\mathscr L_kd_{k+r}}.
$$


Thus its actual least row clearer is


$$
\boxed{
h_r=
\frac{\mathscr L_kd_{k+r}}
{\gcd\bigl(
\mathscr L_kd_{k+r},
\mathscr L_ku_r,
E_{r0},\ldots,E_{r,k-1}
\bigr)}.
}
$$


The actual least simultaneous clearer of all scalar entry coefficients is


$$
\boxed{\mathcal H_k=\operatorname{lcm}_{0\le r<k}h_r.}
$$



This is distinct from the least polynomial clearer and from $|\det C_k|$.

### 12.2 Contents after a specified paid route

Starting instead from the primitive integer polynomial rows $f_r$, let


$$
\ell_r=
\frac{\mathscr L_k}
{\gcd(\mathscr L_k,E_{r0},\ldots,E_{r,k-1})}
$$


be their least rational-entry clearer. After multiplying row $r$ by $\ell_r$, its actual scalar-pair content is


$$
\kappa_r=
\gcd\left(
\ell_ru_r,\,
\frac{\ell_rE_{r0}}{\mathscr L_k},\ldots,
\frac{\ell_rE_{r,k-1}}{\mathscr L_k}
\right).
$$


A zero coefficient row would make the determinant identically zero and must be detected rather than divided by zero.

After removing nonzero row contents, let $\gamma_j$ be the gcd of all integer scalar coefficients in column $j$. Removing these column contents gives an integer affine determinant


$$
D_k^{\mathrm{paid}}(X)=U_kX-V_k.
$$


Its exact multiplier relative to the original monic-row determinant is


$$
T_k=
\frac{\prod_{r=0}^{k-1}d_{k+r}\ell_r}
{\prod_{r=0}^{k-1}\kappa_r\prod_{j=0}^{k-1}\gamma_j},
$$


so


$$
D_k^{\mathrm{paid}}(X)=T_k\mathcal D_k(X).
$$



If $U_k\ne0$, define the final ALL-prime gcd


$$
G_k=\gcd(|U_k|,|V_k|).
$$


Then the actual primitive denominator and numerator are


$$
q_k=\frac{|U_k|}{G_k},
\qquad
p_k=\frac{\operatorname{sgn}(U_k)V_k}{G_k}.
$$


The whole error is exactly


$$
\boxed{
q_k(e+\pi)-p_k
=
\frac{\operatorname{sgn}(U_k)T_k}{G_k}
\,\mathcal D_k(e+\pi).
}
$$



These formulas retain every payment. They are not estimates and do not by themselves prove that the error is nonzero or tends to zero.

---

## 13. Separation from the other supplied constructions

### 13.1 A2’s factorial-compatible Laguerre matrix

A2’s contact rows, degree window, and mixed matrix are different. Its proved least full-contact clearer $m!$, finite-window small-prime contents, $29$-adic cost, and paid determinant budget cannot be substituted for $d_m$, $I_k$, or $G_k$ here.

Conversely, the present saturation identity does not remove A2’s outstanding final gcd obligation. Its whole-error obstruction for the immediate scalar remains valid at its stated scope.

### 13.2 Raw arctangent endpoint family

The supplied raw-arctangent note correctly distinguishes:

- the nonzero endpoint coefficient;
- the whole endpoint remainder;
- primitive polynomial normalization;
- primitive endpoint-pair normalization.

Its all-degree coefficient nonvanishing theorem does not prove endpoint remainder nonvanishing. Its complete exponential and arctangent tail formulas are not altered by anything in this report.

### 13.3 Original binary producer

The original indices remain


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


The contact range is $0,\ldots,b-1$, while physical reconstruction includes $0,\ldots,b$, with


$$
z_b=0.
$$


The complete corrected columns remain


$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad
x=2^ax_0.
$$


In particular, neither $h^F$, the $e_0$ correction, the factor $4b!$, nor the physical terminal is removed.

The scalar acceptance remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
\qquad
S/2^{a+1}\in\mathbb Z.
$$


Any return estimate


$$
v_2(S)\ge1+\chi
$$


would yield only the paid estimate


$$
v_2(S/2^{a+1})\ge\chi-a.
$$


The known original denominator valuation


$$
v_3(q)=n-\frac{b+15}{2}
$$


is unaffected.

The previous binary and ternary boundary results under parent review are not re-proved or promoted here. No identity has been established between their corrected finite objects and the compact determinant studied above.

---

## 14. Acceptance ledger

| Claim or obligation | Status after this audit |
|---|---|
| Complete contact functional $\mu-\delta_{-1}$ | Proved and accepted |
| $B_k$ positive definite | Proved for every size |
| Kernel monotonicity | Accepted; strengthened to strict monotonicity |
| Exceptional $C_1=(0)$ | Accepted, with precise scope explained |
| $\det C_k<0$, inertia $(k-1,1,0)$ | Proved for every $k\ge2$ |
| Contact of all $p_m$ over the stated column range | Proved |
| Rational basis through degree $2k-1$ | Proved |
| Exact primitive polynomial clearer $d_m$ | Proved |
| Independent rows versus saturated basis | Distinguished explicitly |
| $I_k=|\det C_k|/\delta_k$ | Proved |
| Independent-row index $J_k=\prod d_m/I_k$ | New explicit proved formula |
| Raw-height lower bound | Accepted, including boxes and $k!$ cancellation |
| Raw-height upper bound | Accepted, including cofactor estimate |
| JSON large numerical outputs | Supplied finite receipts; not independently recertified here |
| Asymptotic conclusions from $k=2,\ldots,10$ | Not accepted |
| Actual compact determinant affine in $e+\pi$ | Proved |
| Period matrix has rank exactly one | Proved |
| Actual determinant slope nonzero for all $k$ | Open |
| Mandatory frame-index factor in actual scalar gcd | New ALL-prime theorem |
| Whole signed-integral identity | New proved identity |
| Positivity/nonvanishing from that identity | Open; overlap and subtraction obstruct a Gram argument |
| Unique physical-corner pole lemma | New proved local arithmetic theorem |
| $13\mathcal D_3(X)\equiv X+7\pmod{13}$ | New finite arithmetic theorem |
| $\mathcal D_3(e+\pi)\ne0$ | Not established by the modular result |
| Primitive whole-error decay on an infinite set | Open |
| Unconditional rationality or irrationality of $e+\pi$ | Unresolved |

---

## 15. A bounded calculation that would distinguish a new structural hypothesis

No closed saturation, modular-pivot, or real-enclosure table should be rerun.

The new boundary-pole lemma suggests the concrete hypothesis:

> For $k\ge3$ with $p=6k-5$ prime and $p\nmid\det C_k$, the slope of the boundary minor $M_k(X)$ is nonzero modulo $p$.

The result at $k=3$ verifies one instance only. There is no proof of this hypothesis, and it is not being asserted as a theorem.

A first discriminating calculation is $k=4,\ p=19$.

### Bounded inputs

- $a_0,\ldots,a_{20}$, generated by
  

$$
a_0=1,\qquad a_d=1-da_{d-1};
$$


- the $4\times4$ matrix $C_4\bmod19$;
- the three contact rows $p_4,p_5,p_6\bmod19$, each with low correction degree at most three;
- the complete rational moments $r_0,\ldots,r_8\bmod19$;
- the $3\times3$ minor with these rows and columns $j=0,1,2$.

All rational denominators needed for this minor are units modulo $19$.

### Expected verifiable output

1. a certificate that $C_4$ is invertible modulo $19$;
2. the three low coefficient vectors solving their stated contact systems;
3. the two residues $(\alpha,\beta)$ such that
   

$$
M_4(X)\equiv\alpha+\beta X\pmod{19};
$$


4. an explicit verdict whether $\beta\ne0$, and whether $(\alpha,\beta)\ne(0,0)$.

A nonzero $\beta$ would verify one further instance of the slope hypothesis. A zero $\beta$ would refute that hypothesis at once. Either output would have only its stated finite scope.

This calculation is not needed to validate the proofs above.

---

## 16. Final conclusion and exact remaining bottleneck

The parent’s contact-matrix theorem survives independent mathematical audit. Its exceptional size, finite degree boundaries, signed functional, primitive row clearers, saturation index, and two-sided raw-height estimate are all correct.

The principal new advance is arithmetic: **nonsaturation of the individually primitive contact rows produces an exact, compulsory factor in the actual compact determinant’s final coefficient-pair gcd**. This factor is


$$
J_k=\frac{\prod d_m}{|\det C_k|/\delta_k},
$$


not an inferred small clearer. The basis-free block determinant identifies the same cancellation through exact division by $\delta_k$.

The new signed-integral formula includes the complete negative point mass and the full compact weight. It shows precisely why contact nonsingularity and Gram positivity do not establish actual evaluated nonvanishing.

Finally, the physical bottom-right moment supplies a new local arithmetic mechanism. At $k=3$, it proves


$$
13\mathcal D_3(X)\equiv X+7\pmod{13},
$$


thereby establishing actual slope nonvanishing and exact information about the primitive coefficient pair at $13$.

The remaining mathematical bottleneck is still substantial:

1. prove actual slope and evaluated nonvanishing on one specified infinite index set;
2. control the residual ALL-prime scalar gcd after the forced lattice-index cancellation;
3. estimate the **whole** evaluated determinant after every actual content and clearer;
4. obtain, at those same indices,
   

$$
0<|q_k(e+\pi)-p_k|\longrightarrow0.
$$



For the original binary producer, the corresponding obligation must be solved in its own corrected finite objects and original index domain; the present compact family has not been identified with it.

Accordingly, the report proves new structural arithmetic and one new finite local coefficient theorem, but **does not prove either rationality or irrationality of $e+\pi$**.
