> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The genuine high-$m$ two-column survivor

## Secondary zero spaces, height ledgers, symmetry invariance, and a
## good-reduction search

Checked: 2026-08-27 UTC

## 1. Verdict

The preceding note,
sources/root_unity_noncanonical_two_column_module_audit.md, reduced
noncanonical two-column inheritance to the exact polynomial condition



$$
\Gamma_{C,D}(z)=C(z)\beta_D(z)-D(z)\beta_C(z)=0.               \tag{1}
$$



Here



$$
R_C=C+(1+e^z)T_C(z,e^z),\qquad
 \beta_C(z)=T_C(z,-1),                                        \tag{2}
$$



and similarly for $D$.  In the natural two-dimensional endpoint space,
both remainders vanish at zero to order at least



$$
L=m(n+1)+D-1.                         \tag{3}
$$



If (1) holds, then



$$
F=C T_D-D T_C=(y+1)H,\qquad
 H(z,e^z)=O(z^L),                                              \tag{4}
$$



with



$$
\deg_yH\leq m-2,\qquad \deg_zH\leq n+D.                       \tag{5}
$$



The elementary zero estimate proves polynomial-multiple degeneracy when
$n\geq(m-2)D$.  This leaves the genuine high-$m$ range



$$
n<(m-2)D.                         \tag{6}
$$



This audit finds no coupled family in (6), but it sharpens the survivor in
four ways.

1. The ambient secondary space has exact dimension

   

$$
N_H=(m-1)(n+D+1),                     \tag{7}
$$



   and its subspace of forms satisfying the order in (4) has exact
   dimension

   

$$
\Delta=N_H-L=(m-2)D-n>0.                      \tag{8}
$$



   Thus dimension counting genuinely permits $H$ in (6).  It does not
   imply that the unique exterior syzygy $C T_D-D T_C$ lands in that
   $\Delta$-dimensional space after division by $y+1$.

2. Exact height and content ledgers are given in Sections 3--4.  The
   secondary height is at most the product height of the two input pairs,
   but it is not the height seen by the polynomial measure for $e$.  That
   measure sees only the primitive endpoint Wronskian

   

$$
W_{C,D}=CD'-DC'.                      \tag{9}
$$



   A genuine proof must track both contents separately.

3. Basis changes, common frequency shifts, and scalar changes of splitting
   cannot create (1).  They multiply $\Gamma$ by a nonzero scalar/unit or
   leave it unchanged.  The obvious frequency symmetries therefore do not
   manufacture a second inherited column.

4. A good-reduction certificate checks 1,762 tuples lying strictly in (6):

   

$$
4\leq m\leq20,\quad2\leq n\leq16,\quad
    2\leq D\leq\min(12,n),\quad n<(m-2)D.                      \tag{10}
$$



   At the prime $1,000,000,007$, every interpolation matrix is
   invertible, every endpoint matrix has nullity two, and every
   $\Gamma$ has an explicitly recorded nonzero coefficient.  Good
   reduction proves $\Gamma\ne0$ over $\mathbb Q$ for every one of
   these 1,762 rational constructions.  This is rigorous for the finite
   grid and is not extrapolated to all parameters.

The high-$m$ branch therefore remains an exact missing normality theorem,
not a discovered construction.  One must either prove that the canonical
exterior syzygy never enters $(y+1)$ times the secondary kernel, or exhibit
an explicit tuple/family where it does and then pass the endpoint-only norm
criterion.  The present work proves neither statement for all $m,n,D$.

The replayable files are

* scripts/root_unity_high_m_two_column_modular_certificate.py;
* results/root_unity_high_m_two_column_modular_certificate.json.

## 2. Exact secondary origin-order space

Let



$$
\mathcal E_{m,n,D}=
 \sum_{j=0}^{m-2}\mathbb Q[z]_{\leq n+D}e^{jz}.                \tag{11}
$$



The functions $z^ae^{jz}$, with



$$
0\leq j\leq m-2,\qquad0\leq a\leq n+D,           \tag{12}
$$



form a basis, proving (7).  They are a fundamental solution basis for the
constant-coefficient operator



$$
\prod_{j=0}^{m-2}
                    \left(\frac d{dz}-j\right)^{n+D+1},        \tag{13}
$$



whose order is $N_H$.  Their first $N_H$ jets at zero form an invertible
confluent Vandermonde matrix.  Consequently, for every
$0\leq L\leq N_H$, the first $L$ jet rows are independent and



$$
\dim\{Q\in\mathcal E_{m,n,D}:\operatorname {ord}_0Q\geq L\}
                              =N_H-L.                          \tag{14}
$$



Substitution of (3) gives (8).  This is an equality, not merely a lower
bound from the variable count.

The secondary form in (4) is far from an arbitrary vector of the kernel in
(14).  Let $E_2$ be the two-dimensional rational endpoint space and let



$$
\mathcal T:E_2\longrightarrow
       \mathbb Q[z,y]_{\deg_z\leq n,\ \deg_y\leq m-1},
 \qquad C\longmapsto T_C                                      \tag{15}
$$



be the unique origin-interpolation map.  Its exterior syzygy is the
linear map on the one-dimensional space $\bigwedge^2E_2$,



$$
C\wedge D\longmapsto C T_D-D T_C.                            \tag{16}
$$



Two-column inheritance requires the image in (16) to lie in the principal
ideal $(y+1)$.  Only then may it be divided to obtain $H$, which must
also land in the exact kernel (14).  Thus the true intersection problem is



$$
{\rm image}(\bigwedge^2E_2)
 \cap (y+1)\,
 \ker\!\left(J_0^{L-1}:\mathcal E_{m,n,D}\to\mathbb Q^L\right)
 \ne\{0\}.                                                     \tag{17}
$$



The ambient dimension $\Delta$ says nothing by itself about the
one-dimensional image in (17).

For a larger endpoint space $E_\nu$, the same statement uses the exterior
map



$$
\Omega:\bigwedge^2E_\nu\to\mathbb Q[z],\qquad
 \Omega(C\wedge D)=C\beta_D-D\beta_C.                         \tag{18}
$$



A genuine pair exists exactly when $\ker\Omega$ contains a nonzero
decomposable two-vector whose full syzygy is not zero.  A nondecomposable
kernel vector does not define two endpoint polynomials.

## 3. Exact secondary height and content

Clear denominators in two pairs simultaneously and suppose



$$
C,D\in\mathbb Z[z],\qquad
 T_C,T_D\in\mathbb Z[z,y],                                    \tag{19}
$$



with coefficient bounds



$$
H(C),H(D)\leq A,\qquad H(T_C),H(T_D)\leq B.                  \tag{20}
$$



Every coefficient of a product $C T_D$ or $D T_C$ is a sum of at most
$D+1$ products.  Hence



$$
H(F)\leq2(D+1)AB.                     \tag{21}
$$



Write



$$
F(z,y)=\sum_{j=0}^{m-1}f_j(z)y^j,\qquad
 H(z,y)=\sum_{j=0}^{m-2}h_j(z)y^j.                            \tag{22}
$$



Division by $y+1$ is integral because the divisor is monic, and its
coefficient recurrence is



$$
f_0=h_0,\qquad f_j=h_{j-1}+h_j,\qquad f_{m-1}=h_{m-2}.       \tag{23}
$$



Thus each $h_j$ is an alternating partial sum of the $f_k$, and



$$
H(H)\leq
                   2(m-1)(D+1)AB.                             \tag{24}
$$



Let $\mathfrak c_H$ be the gcd of all coefficients of $H$.  Its
primitive secondary normalization satisfies



$$
H(H_{\rm prim})\leq
       \frac{2(m-1)(D+1)AB}{\mathfrak c_H}.                    \tag{25}
$$



The content $\mathfrak c_H$ is basis-independent after saturating the
input exterior line, but it is an auxiliary syzygy content.  It is not
automatically the content of the endpoint Wronskian (9).

Conversely, the existence of a low-height vector in the
$\Delta$-dimensional lattice from (14) is insufficient.  It must admit
the determinant factorization



$$
(y+1)H=C T_D-D T_C                     \tag{26}
$$



with $C,D$ spanning the constrained endpoint kernel and
$T_C,T_D$ equal to their unique interpolation images.  Equation (26) is
the missing structured syzygy, and its factor heights cannot be recovered
from a Siegel-lemma bound for an arbitrary $H$.

## 4. The height and value actually seen at $e$

Assume (1), so the two endpoint columns are inherited.  The ordinary
Wronskian (9) is a nonzero integer polynomial for independent $C,D$, with



$$
d=\deg W_{C,D}\leq2D-2.               \tag{27}
$$



Let



$$
\mathfrak c_W=\gcd\{[z^k]W_{C,D}\},\qquad
 \widetilde W=\mathfrak c_W^{-1}W_{C,D}.                      \tag{28}
$$



A direct coefficient convolution gives, under (20),



$$
H(\widetilde W)\leq
                    \frac{2D^2A^2}{\mathfrak c_W}.             \tag{29}
$$



If certified analytic estimates provide



$$
|R_C(\xi)|,|R_D(\xi)|\leq\epsilon_0,\qquad
 |R_C'(\xi)|,|R_D'(\xi)|\leq\epsilon_1,                        \tag{30}
$$



then determinant inheritance gives



$$
|\widetilde W(i\pi)|
                 \leq\frac{2\epsilon_0\epsilon_1}
                              {\mathfrak c_W}.                 \tag{31}
$$



Suppose now, for the endpoint norm comparison only, that
$s=e+\pi$ is algebraic of degree $r$.  The affine substitution



$$
P_W(X)=\delta^d\widetilde W(i(s-X))              \tag{32}
$$



is a degree-$d$ polynomial in $e$ over
$\mathcal O_{\mathbb Q(s,i)}$.  The exact finite-height criterion in
sources/root_unity_endpoint_exterior_power_audit.md applies without
change.  At fixed $d$, the asymptotic necessary comparison is



$$
-\log|\widetilde W(i\pi)|
 \leq(r^2d+r-1+o(1))\log H(\widetilde W).                      \tag{33}
$$



For growing $d$, any contradiction through the finite-height measure
must in particular beat the budget $r^2d\log H(P_W)$; the all-height
fallback also has a leading height exponent linear in $d$.

Equations (29)--(33) are the exact height requirement for a constructed
high-$m$ syzygy.  A large $\mathfrak c_H$ does not help unless it
induces a useful endpoint content $\mathfrak c_W$.  Likewise, a small
secondary $H$ does not replace the need for a small primitive endpoint
Wronskian.

## 5. Symmetries and gauges do not create $\Gamma=0$

Several natural transformations preserve the vanishing or nonvanishing of
the correction polynomial.

### 5.1 Endpoint basis

If



$$
\binom{\widetilde C}{\widetilde D}
 =U\binom CD,\qquad U\in\operatorname {GL}_2(\mathbb Q),       \tag{34}
$$



and the same change is made to $T_C,T_D$, then



$$
\Gamma_{\widetilde C,\widetilde D}
                          =(\det U)\Gamma_{C,D}.                \tag{35}
$$



Thus a clever rational basis cannot turn a nonzero correction into zero.

### 5.2 Common frequency shift

Multiplying both auxiliary Laurent polynomials by $y^c$ sends



$$
\beta_C\mapsto(-1)^c\beta_C,\qquad
                  \Gamma\mapsto(-1)^c\Gamma.                  \tag{36}
$$



The same is true for a common reflection
$T(z,y)\mapsto y^wT(z,y^{-1})$, up to the nonzero sign
$(-1)^w$.  Hence shifted or reflected integer frequency sets do not by
themselves produce (1).

### 5.3 Scalar change of splitting

Replacing the endpoint quotient map by



$$
\beta_C\mapsto\beta_C+\lambda(z)C     \tag{37}
$$



for a common $\lambda\in\mathbb Q(z)$ leaves



$$
C(\beta_D+\lambda D)-D(\beta_C+\lambda C)=\Gamma_{C,D}.      \tag{38}
$$



This is the two-column analogue of gauge invariance: adding the same scalar
multiple of the value column to the correction column changes no exterior
determinant.

These transformations exhaust the obvious frequency/basis symmetries.
They explain parity and sign changes in exact data, but none can force a
new zero of $\Gamma$.

## 6. Rigorous good-reduction search in the deficit range

The certificate works modulo



$$
p=1,000,000,007.                  \tag{39}
$$



For each tuple in (10), it performs the following exact operations over
$\mathbb F_p$.

1. It builds the $M$-by-$M$ confluent jet matrix for
   $\sum_{j=0}^{m-1}\mathbb F_p[z]_{\leq n}e^{jz}$ and solves all endpoint
   interpolation right sides simultaneously.
2. It builds the reduced $(D-1)$-by-$(D+1)$ endpoint matrix and verifies
   that its nullity is two.
3. It specializes the two auxiliary polynomials at $y=-1$, constructs
   $\Gamma$, and records its first nonzero coefficient.

The prime exceeds every factorial and frequency in the grid.  More
importantly, the script directly verifies invertibility and full endpoint
rank at that prime.  Therefore all rational maps have good reduction.  If
the rational $\Gamma$ were zero, its good reduction would be zero for
every basis of the reduced two-dimensional kernel.  A recorded nonzero
coefficient proves the rational $\Gamma$ is nonzero.

All 1,762 tuples pass.  Representative exact witnesses are:



$$
\begin{array}{c|c|c|c|c}
(m,n,D)&L&N_H&\Delta&
 [z^k]\Gamma\bmod p\\ \hline
(4,6,4)&31&33&2&[z^0]\Gamma=859171299\\
(4,12,8)&59&63&4&[z^0]\Gamma=24156043\\
(6,6,6)&47&65&18&[z^0]\Gamma=208696794\\
(8,8,8)&79&119&40&[z^0]\Gamma=277179567\\
(10,10,10)&119&189&70&[z^0]\Gamma=836605009\\
(12,12,12)&167&275&108&[z^0]\Gamma=98714220\\
(16,16,12)&283&435&152&[z^0]\Gamma=232547511\\
(20,16,12)&351&551&200&[z^0]\Gamma=789296220
\end{array}                                                     \tag{40}
$$



The deterministic witness digest is

    9f1f21465125c560681b6bc2c30ba41a61fc7d9fdeb4f9c2c1aad1093600332f

The replay hashes are

    script  92699040a33f0e8ccc3d15b66f03301ce35f01bac9db397e6d4478f983bbd180
    result  cab8e1c8b10f7a6a1131dd277a8bc6512d901383525b7f7aa40198d745c3ea5c

## 7. Exact remaining theorem

The finite certificate supplies no asymptotic theorem.  The missing
all-parameter assertion can now be stated without ambiguity:

> For $m\geq4$, $n\geq D\geq2$, let $E_2$ be the natural
> two-dimensional kernel (23) from the preceding audit and let
> $C,D$ be a basis.  Prove
> 

$$
>                  C(z)T_D(z,-1)-D(z)T_C(z,-1)\ne0,            \tag{41}
>
$$


> or classify every exception and show that its full syzygy is a
> polynomial-multiple degeneracy.

A proof of (41) likely needs a normality or total-positivity theorem for
the coupled interpolation map $\mathcal T$, not the ambient zero estimate:
the latter is exactly underdetermined by $\Delta$ in (8).  Conversely, a
counterexample to (41) would be a genuine local construction only if



$$
C T_D-D T_C\ne0;                                              \tag{42}
$$



otherwise Section 5 of the preceding audit reduces it to polynomial
multiples.  After (42), the analytic derivative bound (30), primitive
endpoint content (28), and strict norm comparison must still be proved.

No tuple or family satisfying these requirements is presently known.
