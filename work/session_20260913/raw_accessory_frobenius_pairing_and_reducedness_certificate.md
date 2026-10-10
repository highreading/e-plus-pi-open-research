> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An explicit accessory Frobenius pairing and the remaining reducedness certificate

Date: 2026-09-13. Original bounded continuation by audit_sources. Independent review passed: raw_accessory_frobenius_independent_review.md.

The actual exponential algebra has an explicit perfect symmetric pairing over $\mathbb Z[1/d!]$. Its Gram determinant, up to sign, is the fixed small-prime unit


$$
\prod_{a=0}^d(a!)^{d-a+1}.
$$


Both coordinate multiplication matrices are self-adjoint for this pairing. The pairing is generally indefinite and is not the trace pairing. It therefore does not establish reducedness.

The new normalized trace formula is


$$
\operatorname{Tr}(m_a)
=\lambda\!\left(a\,\det W_d\right),\qquad
\det W_d=\frac{(-1)^d}{d!}J_E
\quad\hbox{in the actual E algebra},
$$


where $W_d$ is the previously derived bordered matrix, $J_E=\det\partial(E_1,E_0)/\partial(\beta,\gamma)$, and $\lambda$ extracts the coefficient of $\gamma^d$ in the triangular normal form. This provides an explicit integral trace factorization with no unknown scalar or nonunit normalization.

The only new finite calculation is the predeclared degree $d=2$. It has two real joint roots and four nonreal ones, so a positive-definite real symmetrizer for both coordinate matrices is already impossible in that degree. It is reduced in characteristic zero. No higher-degree or prime scan is performed, and actual generic reducedness in all degrees remains unresolved.

## 1. Actual finite algebra and the top coefficient functional

Throughout take d>=2. Use the actual normalized equations


$$
E_1=d![z]L^{[1]}B^*,\qquad E_0=d![1]L^{[1]}B^*
$$


from raw_extremal_four_accessory_equations.md. Let


$$
R=\mathbb Z[1/d!],\qquad
\mathscr A=R[\beta,\gamma]/(E_1,E_0),\qquad
D_d=(d+1)(d+2)/2.
$$


The reviewed finite-free theorem supplies the basis


$$
\mathcal B=\{\beta^a\gamma^b:a,b\ge0,\ a+b\le d\}.
\tag{1}
$$


Assign weights $1,2$ to $\beta,\gamma$. Its filtered proof also supplies


$$
\operatorname{in}_w(E_1)=P_{d+1},\qquad
\operatorname{in}_w(E_0)=\gamma P_d,\qquad
P_r=r![t^r]e^{\beta t+\gamma t^2/2}.
\tag{2}
$$


The monic leading ideal has generators


$$
G_j=\gamma^jP_{d+1-j},\quad 0\le j\le d+1.
$$


Normal-form reduction never increases weight.

Define $\lambda:\mathscr A\to R$ as the coefficient of the basis monomial $\gamma^d$. It vanishes on every polynomial of weight less than $2d$. On a polynomial of weight exactly $2d$, it depends only on the leading homogeneous quotient; lower-weight coefficients of the actual equations cannot affect that value.

## 2. Exact top moments

Define a formal one-variable moment functional $M$ by


$$
M(X^{2k})=(-1)^k(2k-1)!!,\qquad M(X^{2k+1})=0,
$$


including $M(1)=1$. Its exponential generating identity is


$$
M(e^{tX})=e^{-t^2/2}.
$$


This is a finite-coefficient identity over $\mathbb Q$; it is not a positivity assumption or an analytic measure.

The generating identity for the $P_r(X,1)$ gives


$$
M(P_r(X,1)e^{uX})=(-u)^r e^{-u^2/2}.
\tag{3}
$$


Consequently $M(X^aP_r(X,1))=0$ for $a<r$, and


$$
M(P_r(X,1)P_s(X,1))
=\begin{cases}(-1)^r r!,&r=s,\\0,&r\ne s.\end{cases}
\tag{4}
$$


For example, the two-variable generating function for the left side of (4) is $e^{-tu}$. All identities used below involve polynomial expressions with integer moment values and hence descend to the stated localization.

For a homogeneous polynomial of weight $2d$, evaluate $\gamma=1,\beta=X$ and apply $M$. This functional annihilates the weight-$2d$ part of the leading ideal. Indeed a monomial multiple of $G_j$, where $r=d+1-j$, has multiplier weight $r-2$; its $\beta$-degree is therefore at most $r-2<r$, so (3) kills it. Generators of weight above $2d$ do not contribute.

The functional takes $\gamma^d$ to 1. The only standard monomial of weight $2d$ is $\gamma^d$, so it is exactly the top normal-form coefficient. Thus, for $0\le k\le d$,


$$
\boxed{\lambda(\beta^{2k}\gamma^{d-k})
=(-1)^k(2k-1)!!.}
\tag{5}
$$



## 3. A perfect pairing with fixed Gram determinant

For the basis (1), put


$$
G_{ij}=\lambda(b_i b_j).
\tag{6}
$$


Order the row basis by increasing weight. Order the column weight groups in the reverse order. An entry is zero when its two weights sum to less than $2d$. On complementary weight groups it is determined by (5). The resulting matrix is block triangular.

For a weight $w$, the possible exponents of $\beta$ are


$$
A_w=\{a:0\le a\le\min(w,2d-w),\ a\equiv w\pmod2\}.
$$


The complementary weight $2d-w$ has exactly the same set $A_w$. Its diagonal block in the above block ordering is the moment matrix


$$
\bigl(M(X^{a+a'})\bigr)_{a,a'\in A_w}.
$$


The monic polynomials $P_a(X,1)$, for $a\in A_w$, have the same parity and make a unit triangular change from these monomials. By (4), its determinant is


$$
\prod_{a\in A_w}(-1)^a a!.
$$


It follows that


$$
\boxed{\det G=\pm\prod_{a=0}^d(a!)^{d-a+1}.}
\tag{7}
$$


The sign depends only on the chosen basis ordering and is irrelevant to invertibility. Every integer inverted in (7) is supported on primes at most $d$.

This proves that the pairing $\lambda(ab)$ is perfect over $R$, not just over $\mathbb Q$. The proof applies to the actual lower-weight terms without omitting them: they occupy the off-diagonal blocks and cannot alter the block-triangular determinant.

For every $a\in\mathscr A$, its multiplication matrix obeys


$$
M_a^TG=GM_a.
\tag{8}
$$


This follows directly from commutativity and $\lambda((ab)c)=\lambda(b(ac))$. In particular it gives an explicit simultaneous symmetric realization of $M_\beta,M_\gamma$.

It is not a positive realization. Already $\lambda(1)=0$, while $\lambda(\gamma^d)=1$, so the vector 1 is a nonzero isotropic vector in this nondegenerate real form for $d\ge1$. An indefinite self-adjoint matrix can have nonreal eigenvalues and Jordan blocks. Neither (7) nor (8) implies reducedness.

## 4. Euler element and trace pairing

Let $b_i^\vee$ be the basis dual to $b_i$ for (6), and define


$$
\mathfrak e=\sum_i b_i b_i^\vee.
\tag{9}
$$


The inverse Gram matrix defining this element uses only units of $R$. The coefficient of $b_i$ in $ab_i$ is $\lambda(b_i^\vee ab_i)$, so


$$
\operatorname{Tr}(M_a)=\lambda(a\mathfrak e).
\tag{10}
$$


If $H$ is the ordinary trace Gram matrix


$$
H_{ij}=\operatorname{Tr}(M_{b_i b_j}),
$$


then, in the convention that multiplication matrices have images of basis vectors as columns,


$$
\boxed{H=G M_{\mathfrak e}.}
\tag{11}
$$


This separates the always-perfect Frobenius pairing $G$ from the potentially degenerate trace pairing $H$.

The Euler element has an exact normalization in terms of the actual equations. Introduce another variable pair $(\eta,\zeta)$, and form the divided-difference matrix with rows indexed by $f=E_1,E_0$:


$$
\left(
\frac{f(\beta,\gamma)-f(\eta,\gamma)}{\beta-\eta},
\quad
\frac{f(\eta,\gamma)-f(\eta,\zeta)}{\gamma-\zeta}
\right).
$$


Let its determinant be $\mathfrak B$, regarded in
$\mathscr A\otimes_R\mathscr A$. Each entry is a polynomial. The two columns telescope the difference $f(\beta,\gamma)-f(\eta,\zeta)$. Applying the adjugate matrix therefore gives


$$
(\beta-\eta)\mathfrak B=(\gamma-\zeta)\mathfrak B=0
\quad\hbox{in }\mathscr A\otimes_R\mathscr A.
\tag{12}
$$



For completeness, the diagonal-annihilator argument works over the ring $R$. The perfect pairing identifies $\mathscr A\otimes_R\mathscr A$ with $\operatorname{End}_R(\mathscr A)$ by


$$
u\otimes v:\ x\longmapsto u\lambda(vx).
$$


The two identities (12) mean that this endomorphism commutes with multiplication by the generators $\beta,\gamma$, hence is $\mathscr A$-linear. Every such endomorphism is multiplication by its value at 1. The tensor corresponding to the identity is
$\mathfrak C=\sum_i b_i\otimes b_i^\vee$. Thus


$$
\mathfrak B=(k\otimes1)\mathfrak C,\qquad
k=(\operatorname{id}\otimes\lambda)(\mathfrak B).
\tag{13}
$$



The total weighted degree of $\mathfrak B$, with weights $1,2,1,2$, is at most


$$
(d+1)+(d+2)-1-2=2d.
$$


Applying $\lambda$ in the second factor therefore leaves only a scalar: any positive weight in the first variables would force second-factor weight below $2d$. The scalar depends only on (2). Set the first variable pair to zero in the leading divided-difference determinant. It becomes


$$
\eta^dP_d(\eta,\zeta).
$$


Equations (3)–(4) show that its $\lambda$-value is $(-1)^d d!$. Hence $k=(-1)^d d!$.

Finally specialize the two tensor factors to the diagonal, by multiplication. The divided-difference determinant becomes
$J_E=\det\partial(E_1,E_0)/\partial(\beta,\gamma)$, while $\mathfrak C$ becomes $\mathfrak e$. Therefore


$$
\boxed{J_E=(-1)^d d!\,\mathfrak e.}
\tag{14}
$$


Combining this with the reviewed exact bordered identity
$J_E=(-1)^d d!\det W_d$ proves


$$
\boxed{\mathfrak e=\det W_d\quad\hbox{in }\mathscr A,\qquad
\operatorname{Tr}(M_a)=\lambda(a\det W_d).}
\tag{15}
$$


The relation (14) is in the actual quotient algebra; it is not an assertion that the unreduced polynomials $\mathfrak e$ and $J_E/((-1)^dd!)$ are identical before reduction.

## 5. The explicit trace factorization and its unresolved step

Equations (7), (11), and (15) give


$$
\boxed{
\det H
=\left(\pm\prod_{a=0}^d(a!)^{d-a+1}\right)
\operatorname{Norm}_{\mathscr A/R}(\det W_d).
}
\tag{16}
$$


Thus the trace certificate can be assembled from the actual triangular reduction and the existing $d+2$ by $d+2$ bordered polynomial matrix. The fixed Gram factor is an explicitly known unit. There is no unidentified residue normalization, denominator content, or assumption that a resultant has simple roots.

Over characteristic zero,


$$
\operatorname{Nil}(\mathscr A_{\mathbb Q})
=\ker M_{\det W_d}.
\tag{17}
$$


Indeed the radical of the trace pairing is exactly the nilradical: after extension to an algebraic closure, decompose into Artin local factors; on a factor of length $m$, multiplication trace is $m$ times its residue value. Since $m\ne0$ in characteristic zero, the trace radical on that factor is its maximal ideal. The invertible matrix $G$ and (11) then prove (17).

Consequently the rank of $M_{\det W_d}$ equals the number of geometric points, and actual characteristic-zero reducedness is equivalent to its invertibility. Formula (17) is not asserted in arbitrary positive characteristic, where a local length can vanish in the field.

The construction is more explicit than merely naming a discriminant: it supplies a fixed perfect pairing, a fully normalized Euler element equal to the existing small bordered determinant, and an exact matrix whose kernel is the nilradical. It still leaves the decisive nonvanishing


$$
\operatorname{Norm}_{\mathscr A_{\mathbb Q}/\mathbb Q}(\det W_d)\ne0
$$


unproved in general $d$. No positivity argument is available from (8).

The homogeneous Hermite leading algebra is a direct warning. It has the same perfect pairing and rank, but is supported only at the origin and is nonreduced for $d\ge1$. Its Euler element is $D_d\gamma^d$, which is nonzero in characteristic zero but has square zero. Therefore the fixed nonzero value
$\lambda(\mathfrak e)=\operatorname{Tr}(1)=D_d$ cannot be promoted to invertibility of $\mathfrak e$.

For the normalization-index theorem, if the actual generic algebra is reduced, (16) gives an explicit global discriminant valuation with no additional large-prime factor:


$$
v_p(\det H)=
v_p\operatorname{Norm}_{\mathscr A/R}(\det W_d),
\qquad p>d.
$$


This can be inserted into that theorem's conditional index bound. It does not establish its missing reducedness hypothesis or bound the resulting valuation.

## 6. The one predeclared exact degree: d=2

This degree is used to diagnose the positive-symmetrizer proposal and to check the new normalizations. The actual equations are


$$
\begin{aligned}
E_1={}&\beta^3-22\beta^2+3\beta\gamma+132\beta-18\gamma-224,\\
E_0={}&-2\beta^3+\beta^2\gamma+36\beta^2-18\beta\gamma
-180\beta+\gamma^2+54\gamma+288.
\end{aligned}
$$


Their exact lexicographic elimination gives


$$
\begin{aligned}
f(\beta)={}&\beta^6-38\beta^5+589\beta^4-4714\beta^3\\
&+20344\beta^2-44304\beta+37120,\\
12\gamma={}&\beta^5-32\beta^4+397\beta^3-2336\beta^2
+6416\beta-6336.
\end{aligned}
\tag{18}
$$


The eliminant is squarefree. One Sturm chain, with each member rescaled by a positive rational constant, is


$$
\begin{aligned}
&f,\\
&3\beta^5-95\beta^4+1178\beta^3-7071\beta^2+20344\beta-22152,\\
&38\beta^4-1169\beta^3+12285\beta^2-54256\beta+86808,\\
&-20015\beta^3+306665\beta^2-1543584\beta+2560696,\\
&-2243999\beta^2+25532744\beta-72357832,\\
&1173253\beta-153256292,\qquad 1.
\end{aligned}
\tag{19}
$$


These are positive rescalings of the ordinary signed-remainder Sturm sequence, not an independently altered sign sequence. The signs at minus infinity are $+,-,+,+,-,-,+$, with four changes. At plus infinity they are $+,+,+,-,-,+,+$, with two changes. Hence $f$ has exactly two real roots and four nonreal roots. Formula (18) identifies all six with the actual joint roots.

If a positive-definite real form made $M_\beta$ self-adjoint, its eigenvalues would all be real. Its characteristic polynomial here is $f$, since (18) makes $\mathscr A_{\mathbb Q}\cong\mathbb Q[\beta]/(f)$. Thus no such positive form exists at $d=2$, and in particular no simultaneous positive symmetrizer exists.

For the basis $1,\beta,\gamma,\beta^2,\beta\gamma,\gamma^2$, the exact single-degree control finds


$$
\det G=2,\qquad
\mathfrak e=
5\beta^2-14\beta\gamma+54\beta+6\gamma^2-21\gamma-104
\quad\hbox{in }\mathscr A,
$$


and


$$
\det H=2^{15}\cdot751\cdot318737\ne0.
$$


It verifies the self-adjoint identities, $H=GM_{\mathfrak e}$, and
$\mathfrak e=J_E/2$ exactly. Files:
accessory_trace_pairing_single_degree_check.py/.json.
The initial checker needed its polynomial domain explicitly set to $\mathbb Q$ to accept the inverse Gram entry $1/2$; after that implementation correction every exact check passed. This was not a mathematical change to the formulas.

The finite check establishes reducedness only for this degree. No inference to all $d$, no new actual four-equation prime exclusion, and no statement about the rationality of $e+\pi$ follows.
