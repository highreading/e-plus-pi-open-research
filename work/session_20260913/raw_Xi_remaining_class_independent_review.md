> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Dedicated independent review of the remaining Xi class

Date: 2026-09-13. Reviewer: audit_computations.

Reviewed `raw_Xi_remaining_class_mod_eight.md` against the exact interpolation reduction, the common top-block factorization, the original reconstruction rows, and the preceding coefficient-valuation theorems. **The proof passes, with no substantive correction required.**

For every $n\ge5$, $n\equiv1\pmod4$, it proves



$$
v_2(\Xi_n)=-2n-2v_2((n-1)!)+2.
$$



Together with the already separately reviewed classes and the exact $n=1$ case, this closes the nonvanishing gate for $\Xi_n$. Since $[z^3]Q_n=B_{n,n}\Xi_n$ and both factors are nonzero, $Q_n$ is cubic in every degree $n\ge1$. No simplicity of its roots, real size bound, or irrationality conclusion follows.

## 1. Exact row elimination and the common scale

Let the top exponential block have rows $2n+i$, $0\le i\le n$, and write the reversed C polynomial as $C(t)$. Its corresponding moment rows are



$$
L(t^{n-1+i}C).
$$



For the lower row $2n-d$, exact exponential elimination subtracts
$\sum_iM_{d,i}L(t^{n-1+i}C)$ from $L(t^{n-1-d}C)$. Retaining exactly rows $d=1,2$, columns $i=0,1,2,3$, yields the two displayed modified rows in the source note, with the claimed minus signs. All other lower rows are the unmodified moments of degrees zero through $n-4$. The retained C-border assignment gives the row $C(1)=0$.

The appended A reconstruction has Taylor index $n$, hence replacement index $d=n$; the H reconstruction has index $n-1$, hence $d=n+1$. Neither belongs to the retained block. Therefore their retained terms contain only their C entries. With



$$
S_C(t)=L_s\frac{C(t)-C(s)}{t-s},
$$



these entries are exactly $-S_C(0)$ and $-S_C'(0)-C(0)$. The latter extra $-C(0)$ is the modified $t_{-1}=1$ entry; its sign is correct.

Thus the effective A, H, C, D values are all evaluations of one and the same C cofactor vector, multiplied by the same top exponential determinant and divided by the same original endpoint determinant. This is a statement about the retained cofactor terms. It does **not** assume that pure-C reconstruction equals the full A/H reconstruction of an independently normalized effective B polynomial.

## 2. Why the truncation error survives the change of basis

The full retained two-by-four block generates one base term, eight single replacements, and six two-column replacement minors. It includes every one of the eight designated row sets. The two extra singles and five extra doubles have valuation at least $a+2$ relative to the top exponential determinant. For example, the upper-left double has valuation two and is retained; a double involving any other column pair has the higher bound proved in the eight-set reduction.

Every discarded term is estimated as a **full cofactor term** with its complementary Cauchy minor and its original denominator. The global bounds for the A/H and C/D complements are different and are retained separately. The -4 border assignment and an appended reconstruction row assigned to the exponential block have the already proved strict gaps. Consequently the four errors are exactly at least



$$
\alpha+a+2,\ \alpha+a+2,\ \chi+a+2,\ \chi+a+2,
\quad
\alpha=-n,\quad\chi=-n-2v_2((n-1)!).
$$



This is not an entrywise perturbation estimate for an inverse moment matrix. The cofactor error is proved first; the four-Legendre representation is then an exact analysis of the retained matrix. No inverse-Gram conditioning assumption is introduced by that representation.

## 3. Independent reconstruction of the moment equations

Put $b=\beta_{n-1}$, $c=\beta_{n-2}$, $d=\beta_n$. The low moment constraints put the effective polynomial in



$$
\kappa[uQ_n+vQ_{n-1}+bwQ_{n-2}+bxQ_{n-3}].
$$



The factor $b$ on both lower coefficients is essential. It compensates the norm ratio $h_{n-1}/h_{n-2}=-b$; omitting it would give incorrect valuations and an incorrect residue.

Expanding monomials in the monic Q basis gives



$$
t^j=Q_j-s_jQ_{j-2}+r_jQ_{j-4}+\cdots,
\quad r_j=s_js_{j-2}-[t^{j-4}]Q_j.
$$



The stated rational formula for $r_j$ follows by subtraction. Dividing by $\kappa b h_{n-3}$, I independently obtained the four upper moments



$$
cv-s_{n-1}x,\quad -cdu+s_ncw,\quad
-s_{n+1}cv+r_{n+1}x,\quad s_{n+2}cdu-r_{n+2}cw,
$$



and the two lower moments $x,-cw$. These give precisely equations (9), (11), and (12) of the reviewed note, including both off-diagonal signs.

All coefficients of the resulting two-by-two system are dyadically integral: $c,d$ are units, $v_2(s_n)=v_2(s_{n-1})=a-1$, and $v_2(r_{n+1})=v_2(r_{n+2})=a-2\ge0$. Its matrix is the identity modulo two; its right-hand coefficients of $u,v$ are even. The inverse is therefore dyadically integral, with $w,x$ even linear functions of $u,v$.

## 4. Endpoint rank and the v congruence

The endpoint ratios satisfy $\lambda=1+O(2^{2a+1})$, $\eta\in2\mathbb Z_{(2)}$, and $\zeta\in\mathbb Z_{(2)}^\times$. Substituting the even linear functions for $w,x$ into



$$
u\lambda+v+b(w\eta+x\zeta)=0
$$



makes its v coefficient a unit congruent to one modulo $2^{2a+1}$. The u coefficient is also congruent to one at that precision. Hence u zero forces all four coefficients zero, while u one gives uniquely



$$
v=-1+O(2^{2a+1}),\qquad w,x\in2\mathbb Z_{(2)}.
$$



The low orthogonality rows have independent pivots because every $h_j\ne0$. The remaining three equations have rank three on their four-dimensional complement. Thus the effective matrix has rank n, its cofactor vector is nonzero, its Q_n coefficient is nonzero, and one common nonzero $\kappa$ is legitimate. No assumed nonvanishing of the desired $\Xi$ is used in this argument.

## 5. Independent residue calculation

Writing $n=4u+1$, I also reduced the rational two-by-two system symbolically modulo eight, without evaluating any HP degree. The result is



$$
Z\equiv(1+4u)I,\qquad
R\equiv(2+4u)\binom11\pmod8.
$$



The inverse of $1+4u$ is itself modulo eight, and multiplication gives



$$
w\equiv x\equiv2+4u\pmod8.
$$



This matches the source's shorter valuation proof. In particular, the exceptional retained entries with valuations $a+1$ are multiplied only by dyadically integral coefficients, so their omission in this last reduction modulo eight is justified. The full two-by-two inverse includes the determinant and hence the essential double replacement; it is not a single-exchange approximation.

## 6. Six Legendre identities, the scale, and the final error comparison

Let $H=h_{n-1}$, $q=Q_{n-1}(0)$, $k=n^2/(2n-1)$, and $k_-=(n-2)^2/(2n-5)$. The three-term recurrence and the previously proved zero-value/second-kind identities give exactly



$$
Q_{n-3}(0)=q/c,\quad S_n(0)=H/q,\quad
S_{n-2}(0)=H/(bq),
$$




$$
Q_n'(0)=kq,\quad Q_{n-2}'(0)=k_-q/c,
$$




$$
Q_{n-1}(0)+S_{n-1}'(0)=(2n-1)H/q,
\quad
Q_{n-3}(0)+S_{n-3}'(0)=(2n-5)H/(bq).
$$



For example the last denominator follows from $h_{n-1}=bc\,h_{n-3}$ and $Q_{n-1}(0)=cQ_{n-3}(0)$; no factor of c is missing.

The resulting exact expressions are



$$
A_{\rm eff}=-\kappa H(1+w)/q,\quad
D_{\rm eff}=\kappa q[k+bk_-w/c],
$$




$$
C_{\rm eff,0}=\kappa q(v+bx/c),\quad
H_{\rm eff}=-\kappa H[(2n-1)v+(2n-5)x]/q.
$$



They produce the source's quadratic identity with the correct subtraction sign. Since $b$ is divisible by $2^{2a}$, v is minus one modulo eight, and w,x have the residues just proved, its quotient by $\kappa^2H$ is



$$
-5x-w\equiv4\pmod8.
$$



The valuation of $\kappa^2H$ is not borrowed from the unchanged top term. The established cofactor errors imply
$v_2(A_{\rm eff})=\alpha$ and $v_2(D_{\rm eff})=\chi$.
In their exact product above, both $1+w$ and $k+bk_-w/c$ are units. Therefore



$$
v_2(\kappa^2H)=\alpha+\chi.
$$



The effective Xi has valuation $\alpha+\chi+2$, while the actual-minus-effective error has valuation at least $\alpha+\chi+a+2\ge\alpha+\chi+4$. This is a strict gap; the error cannot cancel the residue. The argument applies uniformly to every $n\ge5$ in the stated class.

## 7. Verification boundary

The only computation in this review is fixed symbolic rational reduction with n left as $4u+1$. All bridges, scale choices, rank claims, and error comparisons were checked algebraically as above. No additional canonical triple, modular scan, or finite-index extrapolation was used. The new conclusion is arithmetic nonvanishing and cubic degree, not a bound on the real magnitude of the accessory coefficients or on the primitive mixed remainder.
