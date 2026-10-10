> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A1 turn 7: an all-depth factorial–Pascal locality lemma, but no proved endpoint displacement law

I do **not** establish the suggested equality


$$
v_3(Q_n(-1))=2v_3((n-1)!),\qquad n=4^j+1.
$$


The supplied depths $2,12,60$ remain finite evidence for it.

I obtain a different, unconditional growing-precision statement: after an explicit integral Pascal change of basis, the **actual moment matrix** has factorially divisible entries away from its diagonal, and its constant-coordinate coupling has factorially divisible entries at large indices. This is not a residue-rank calculation. It holds at every precision and every matrix size, with exact boundary formulas.

The obstruction is that this entrywise locality has not been shown to survive elimination at the depth needed for the endpoint. In particular, it does not justify replacing the actual inverse by its local truncation.

### 1. Actual moments and the transformation

Write


$$
\mu(F)=\int_0^\infty e^{-t}F((1-t)^2)\,dt,\qquad
\rho(F)=\mu(F)-F(-1).
$$


Use the divided nonconstant polynomials


$$
\phi_d(y)=\frac{(y+1)(y-1)^d}{d!},\qquad d\ge0.
$$


Then the constant/nonconstant couplings and nonconstant Gram entries are


$$
t_d=\rho(\phi_d)=2b_d+(d+1)b_{d+1},
$$




$$
G_{de}=\rho(\phi_d\phi_e)
=\binom{d+e}{d}e_{d+e},
$$


where


$$
b_s=\frac{\mu((y-1)^s)}{s!},\qquad
e_s=4b_s+4(s+1)b_{s+1}+(s+1)(s+2)b_{s+2}.
$$


These identities are exact: the negative point mass vanishes on every $\phi_d$.

For a block of size $D$, indexed by $0,\ldots,D-1$, put


$$
P_{ij}=\binom ij,\qquad S_{ii}=(-2)^i,\qquad T=SP.
$$


Both $T$ and $T^{-1}$ belong to $\operatorname{GL}_D(\mathbb Z_3)$. Define


$$
\widetilde G=T^{-1}GT^{-T},
\qquad
\widetilde t=T^{-1}t.
$$


The transformation is independent of the requested precision.

### 2. An exact factorial tail estimate

Set $a=-2$. The supplied actual moment formula can be written


$$
b_s=a^s\sum_{\ell\ge0}a^{-\ell}F_\ell(s),
\qquad
F_\ell(X)=\frac{(X-\ell+1)(X-\ell+2)\cdots(X+\ell)}{\ell!}.
\tag{1}
$$


Here $F_0=1$. For a nonnegative integer $s$, terms with $\ell>s$ vanish, so (1) is a finite identity, not a formal interchange with the integral.

For $\ell\le s$,


$$
F_\ell(s)=\binom{s}{\ell}\frac{(s+\ell)!}{s!}.
$$


The product of any $\ell$ consecutive integers is divisible by $\ell!$. Therefore


$$
v_3(F_\ell(s))\ge v_3(\ell!).
\tag{2}
$$



For $L\ge0$, truncate (1) to $\ell<L$, calling the result $b_s^{[L]}$. Equation (2) gives the uniform bound


$$
b_s-b_s^{[L]}\in 3^{v_3(L!)}\mathbb Z_3
\quad(s\ge0).
\tag{3}
$$


There is no exception when $s<L$: the omitted terms then vanish.

Apply the same truncation separately to each $b_s,b_{s+1},b_{s+2}$ in the actual formulas for $t_s,e_s$. It follows that


$$
t_s-t_s^{[L]},\quad e_s-e_s^{[L]}
\in3^{v_3(L!)}\mathbb Z_3
\tag{4}
$$


uniformly in $s$.

This estimate includes all branches and all boundary indices. It is not a fixed-modulus moment approximation.

### 3. Why Pascal conjugation makes each retained term local

Each retained summand in $a^{-s}t_s^{[L]}$ is a polynomial in $s$ of degree at most


$$
2\ell+1.
$$


Each retained summand in $a^{-s}e_s^{[L]}$ has degree at most


$$
2\ell+2.
$$


Consequently, for $L\ge1$,


$$
\deg(a^{-s}t_s^{[L]})\le2L-1,\qquad
\deg(a^{-s}e_s^{[L]})\le2L.
\tag{5}
$$



The vector assertion follows directly from finite differences:


$$
(P^{-1}f)_i
=\sum_{r=0}^i(-1)^{i-r}\binom ir f(r)
=\Delta^i f(0).
$$


Thus


$$
(T^{-1}t^{[L]})_i=0\qquad(i>2L-1).
\tag{6}
$$



For the matrix assertion, let


$$
B_{ij}=\binom{i+j}{i}= (PP^T)_{ij},
\qquad J=\operatorname{diag}(0,1,\ldots,D-1).
$$


Define the lower bidiagonal matrix $N$ by $N_{i,i-1}=i$. The binomial identity


$$
(i-j)\binom ij=(j+1)\binom i{j+1}
$$


gives, including the last row and column of every finite block,


$$
P^{-1}JP=J+N.
\tag{7}
$$



If $f$ has degree $r$, expand $f(i+j)$ into monomials $i^u j^v$, with $u+v\le r$. Then


$$
P^{-1}\bigl(B_{ij}i^u j^v\bigr)P^{-T}
=(J+N)^u(J+N^T)^v.
\tag{8}
$$


The right-hand side has lower bandwidth at most $u$ and upper bandwidth at most $v$. In particular, its entries vanish when $|i-j|>r$.

Using (5),


$$
(T^{-1}G^{[L]}T^{-T})_{ij}=0
\qquad(|i-j|>2L).
\tag{9}
$$


The polynomial coefficients used in this argument may have denominators divisible by $3$; this causes no problem. Equations (6) and (9) are exact identities over $\mathbb Q$, while the errors in (4) are independently controlled in $\mathbb Z_3$.

### 4. New all-depth locality theorem

Because $T^{-1}$ is integral over $\mathbb Z_3$, (4), (6), and (9) prove the following.

**Theorem.** For every $D\ge1$, every $L\ge0$, and all indices in the finite block,


$$
\boxed{\widetilde t_i\in3^{v_3(L!)}\mathbb Z_3
\quad\text{if }i\ge2L,}
\tag{10}
$$


and


$$
\boxed{\widetilde G_{ij}\in3^{v_3(L!)}\mathbb Z_3
\quad\text{if }|i-j|>2L.}
\tag{11}
$$


For $L=0$, these merely assert integrality.

In particular,


$$
\boxed{
v_3(\widetilde t_i)\ge
v_3\!\left(\left\lfloor\frac i2\right\rfloor!\right).
}
\tag{12}
$$


For $|i-j|\ge1$,


$$
\boxed{
v_3(\widetilde G_{ij})\ge
v_3\!\left(
\left\lfloor\frac{|i-j|-1}{2}\right\rfloor!
\right).
}
\tag{13}
$$



These are genuinely growing bounds for the actual moments. By Legendre’s formula, the bounds in (12) and (13) are respectively


$$
\frac i4-O(\log(i+2)),\qquad
\frac{|i-j|}{4}-O(\log(|i-j|+2)).
$$


They apply, in particular, to all block sizes needed for $n=4^j+1$, $j\ge1$.

An equivalent practical statement is that modulo $3^H$, with


$$
L_H=\min\{L:v_3(L!)\ge H\},
$$


the transformed constant coupling is supported in indices $<2L_H$, and the transformed Gram matrix has bandwidth at most $2L_H$. This is an exact consequence of factorial divisibility, not an empirically fitted sparsity pattern.

### 5. The precise obstruction: locality of the matrix is not locality of its inverse

The theorem does not yet control the endpoint Schur quantities


$$
b,\qquad \xi_{\rm const},
$$


because both involve elimination through the unit block $E$.

Even a unit triangular matrix can have a dense inverse modulo $3$. For example, if $U$ is the matrix with ones on its first superdiagonal, then


$$
(I-U)^{-1}=I+U+\cdots+U^{D-1}.
$$


The original matrix has bandwidth one, but its inverse has nonzero entries at arbitrarily large separation. Thus factorial decay away from the diagonal does **not**, without additional structure, imply factorial decay of inverse contractions.

Here that distinction is decisive. Equations (10)–(13) prove deep divisibility of the **direct transformed coupling** at large indices. They do not prove that a low-index coupling cannot propagate through the intervening block and reach its last coordinate with small valuation.

There is also a quantitative limitation. To reach precision


$$
H\asymp v_3((n-1)!)\asymp n/2
$$


by the uniform tail estimate alone requires


$$
L_H\asymp 3H,
$$


because $v_3(L!)\sim L/2$, more precisely $L_H\sim2H$. Thus $2L_H\asymp2n$, larger than the relevant matrix dimension. **At the target precision, the uniform locality bound alone becomes vacuous.** The approximation $L_H\sim2H$, rather than the coarser $3H$ scale, is the one relevant to this conclusion.

The missing lemma must therefore exploit cancellations specific to the actual transformed matrix—beyond the universal termwise factorial tail bound. Merely iterating a generic inverse expansion would not settle the endpoint.

The new theorem nevertheless narrows that task: all possible low-precision long-range propagation comes from inversion of the explicitly defined finite-band polynomial-moment truncations. It does not come from uncontrolled factorial tails or omitted boundary terms.

### 6. Consequences and limits for the actual endpoint pair

Let


$$
N=n-1=4^j,\qquad
\mathcal C_n=c\xi_{\rm const}-b\xi_{\rm last}.
$$


The established nonzero endpoint identity remains


$$
v_3(Q_n(-1))=v_3(N!)+v_3(\mathcal C_n).
\tag{14}
$$


The new locality theorem does not yet prove $v_3(\mathcal C_n)=v_3(N!)$, nor improve the established endpoint lower bound. Consequently it must not be reported as a denominator theorem.

For completeness, retain the actual complete rational endpoint matrix, including the rational arctangent contribution:


$$
R_{ij}=\sum_{t=0}^n Q_{n,t}
\left(
-(2(i+j+t))!
+4\sum_{a=1}^{i+j+t}\frac{(-1)^{i+j+t-a}}{2a-1}
\right).
$$


With the established endpoint-basis notation,


$$
A=t\det K-z^T\operatorname{adj}(K)z,\qquad
B=\ell Q_n(-1)\det K,
$$




$$
g=\gcd(|A|,|B|),\qquad
q=\frac{|B|}{g},\qquad
p=-\frac{\operatorname{sgn}(B)A}{g}.
$$


Thus any eventual evaluation of (14) enters through


$$
v_3(B)=v_3(\ell)+v_3(N!)+v_3(\mathcal C_n)+v_3(\det K),
$$


and only then through


$$
v_3(q)=\max\{0,v_3(B)-v_3(A)\}.
$$


No lower bounds on the two terms are subtracted.

The whole evaluated error is still


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B)\ell^k}{g}
\det H_{\rm complete}.
}
$$


On the regular domain, the supplied established dyadic theorem gives $B\ne0$ and distinct reduced centers. Hence the whole error is nonzero at all but at most one regular index, without assuming irrationality.

## Closing ledger

### (1) New result and proof status

**Proved:** the all-depth factorial–Pascal locality bounds (10)–(13), for the actual moment functional, uniformly in matrix size and precision. The proof includes the finite-block boundaries and the complete constant/nonconstant coupling.

**Not proved:** a growing improvement for $v_3(Q_n(-1))$, the suggested doubled-factorial equality, an actual odd-denominator law, or irrationality of $e+\pi$.

### (2) Exact remaining bottleneck

The required new input is a cancellation or propagation theorem for the **inverse contractions of the actual finite-band truncations**. Direct factorial decay does not survive inversion automatically, and at precision comparable to $v_3((n-1)!)$ the universal truncation bandwidth already exceeds the matrix size.

This is the precise point at which the present controlled all-depth approach stops. A successful continuation must prove extra cancellation in the actual matrix, rather than treat moment-tail divisibility as an inverse estimate.

### (3) Computation request

**None.** Another regular endpoint value would not resolve inverse propagation. The new locality statements are symbolic identities with uniform factorial error bounds and require no finite computation to establish them.
