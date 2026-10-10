> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 continuation: a first-layer reduction that uses the derangement equations, and the exact obstruction caused by degree drops

I do not obtain an unconditional odd-denominator growth bound in this turn. I obtain a more explicit reduction of the high-prime problem: in a specified degree window, the two residual Schur determinants can be computed **directly from the reduction of the actual orthogonal polynomial modulo $p$**, without constructing a rational Schur complement. Outside that window, I identify the precise additional coefficient-lift data needed.

This is a bounded follow-on lemma, not a claim that the residual determinants are units. I also independently confirm A4’s improved stationary inequality and spectral floor, including their scaling factors.

Throughout,


$$
n=4^j+1,\quad j\ge1,\qquad r=\frac{n-1}{2},\quad k=r+1,
\qquad 3n<p\le4n-3,
$$


and $Q$ is the **actual primitive integer polynomial** defined by the derangement orthogonality equations. No assertion about infinitely many primes attached to $4^j$ is used.

## 1. An explicit characteristic-$p$ form of the actual orthogonality equations

Define the truncated exponential


$$
\mathscr E_p(T)=\sum_{a=0}^{p-1}\frac{(-T)^a}{a!}\in\mathbf F_p[T].
$$


For $f\in\mathbf F_p[y]$, put


$$
\mathscr M_p(f)
=-[T^{p-1}]\mathscr E_p(T)f((1-T)^2).
\tag{1}
$$



### Lemma 1 — The actual derangement functional modulo $p$

For every integer polynomial $f$,


$$
\mu(f)\equiv \mathscr M_p(\bar f)\pmod p,
\qquad
\mu(y^a)=D_{2a}.
\tag{2}
$$


Consequently, the actual nonzero reduction $\bar Q$ satisfies


$$
\boxed{
[T^{p-1}]\mathscr E_p(T)(1-T)^{2s}
       \bar Q((1-T)^2)
=-(-1)^s\bar Q(-1),
\quad 0\le s<n.
}
\tag{3}
$$



**Proof.** Write


$$
f((1-T)^2)=\sum_{b\ge0}c_bT^b.
$$


The integral defining $\mu$ gives


$$
\mu(f)=\sum_{b\ge0}c_b b!
\equiv\sum_{b=0}^{p-1}c_b b!\pmod p.
$$


Wilson’s theorem implies, for $0\le b<p$,


$$
\frac{(-1)^{p-1-b}}{(p-1-b)!}\equiv-b!\pmod p.
$$


Taking the coefficient in (1) therefore gives (2). The defining equations
$\mu(y^sQ)=(-1)^sQ(-1)$ give (3). ∎

This is a concrete constraint on the reduction of the specific primitive polynomial, not an independent choice of a pole polynomial. Primitivity guarantees $\bar Q\ne0$, but **does not** guarantee that (3) has a one-dimensional solution space. That distinction matters when reconstructing the primitive ray modulo $p$.

The factorial moments and the derangement moments also have distinct, explicit reductions:


$$
\sum_a Q_a(2(v+a))!
\equiv
\sum_{\substack{a\\2(v+a)<p}}Q_a(2(v+a))!\pmod p.
\tag{4}
$$


Thus equations (3) and (4) give a finite-field implementation using precisely the two moment functionals occurring in this construction.

## 2. Direct residual matrices: when $Q\bmod p$ is sufficient

Reuse the established highest-pole rank and Schur normalization. Write


$$
d=\deg\bar Q,\qquad
t_p=\frac{p+1}{2},\qquad
h=n+d-t_p>0,\qquad
s=k-h=t_p-d-r.
$$


Let


$$
f_0(y)=1,\qquad f_i(y)=y^i-(-1)^i,\quad 1\le i<k,
$$


and let $I=\{0,\ldots,s-1\}$ be the low-coordinate block.

Write $\ell=pu$, with $u\in\mathbf Z_p^\times$. The established exact Schur construction gives


$$
\mathcal E=
\frac1p\left(\mathcal T_{II}
-\mathcal T_{IJ}\mathcal D^{-1}\mathcal T_{JI}\right),
\qquad \mathcal T=\ell R_{\rm end}.
$$



### Lemma 2 — Pole-free residual window

Suppose


$$
\boxed{d>\frac{p-1}{4}.}
\tag{5}
$$


Then every entry of $(R_{\rm end})_{II}$ is $p$-integral without using divisibility of any coefficient of $Q$, and


$$
\boxed{
\mathcal E\equiv u(R_{\rm end})_{II}\pmod p.
}
\tag{6}
$$


The analogous identity holds after deleting coordinate $0$.

**Proof.** For $i,j<s$,


$$
\deg(Qf_if_j)\le n+2s-2=p-2d.
$$


Under (5),


$$
p-2d<t_p.
$$


Hence every arctangent denominator in this entry is strictly less than $p$. The factorial part is integral as well.

The established pole-rank calculation shows that $\mathcal T_{IJ}$ and
$\mathcal T_{JI}$ are divisible by $p$, whereas $\mathcal D^{-1}$ is integral. Therefore


$$
\frac1p\mathcal T_{IJ}\mathcal D^{-1}\mathcal T_{JI}
\equiv0\pmod p.
$$


Also $\mathcal T_{II}/p=u(R_{\rm end})_{II}$, proving (6). ∎

In particular, (5) holds whenever $d=n$, throughout the assigned prime window. More generally, it allows substantial leading-coefficient drops; it is not a disguised full-degree assumption.

### Explicit finite-field matrix

For a polynomial $F(y)=\sum_v F_vy^v$ of degree less than $t_p$, define


$$
\mathscr R_p(F)
=
-\sum_{\substack{v\\2v<p}}F_v(2v)!
+
4\sum_vF_v\sum_{a=1}^{v}\frac{(-1)^{v-a}}{2a-1}
\quad\in\mathbf F_p.
\tag{7}
$$


Every denominator in (7) is a unit.

Set


$$
N_{ij}=\mathscr R_p(\bar Q f_if_j),
\qquad 0\le i,j<s,
\tag{8}
$$


where the degree bound in Lemma 2 permits using the actual polynomial products before reduction. Let $N_0$ delete coordinate $0$. Then


$$
\det\mathcal E\equiv u^s\det N,\qquad
\det\mathcal E_0\equiv u^{s-1}\det N_0\pmod p.
\tag{9}
$$



Thus the first residual layer is obtained from:

1. the derangement constraints (3);
2. the actual reduction $\bar Q$;
3. the explicit rational-moment functional (7).

No large exact Schur fractions are needed.

For example, the following is an exact, readily certifiable consequence:


$$
\boxed{
\det N\ne0,\quad \bar Q(-1)\det N_0\ne0
\ \Longrightarrow\
v_p(g)=s,\qquad v_p(q^{\rm cen})=0.
}
\tag{10}
$$


This follows from the established all-depth formulas, not from interpreting a row clearer as the denominator.

**Status:** (10) is a conditional certificate. I have not proved its two nonvanishing premises uniformly for the actual $Q$.

## 3. Exact obstruction when the degree drops farther

The preceding reduction explains a concrete failure of a purely mod-$p$ approach.

For $v\le2n-1$, define the pole functional


$$
\mathscr P_p(y^v)=
\begin{cases}
0,&v<t_p,\\
4(-1)^{v-t_p},&v\ge t_p.
\end{cases}
\tag{11}
$$


Remove the unique possible $p$-denominator from each arctangent moment and denote the resulting $p$-integral functional by $\mathscr R_p^{\rm reg}$, including the complete factorial contribution.

Then, exactly over $\mathbf Z_p$,


$$
R_{\rm end,ij}
=
\mathscr R_p^{\rm reg}(Qf_if_j)
+\frac1p\mathscr P_p(Qf_if_j).
\tag{12}
$$



Choose any integral coefficient lift $Q^{(0)}$ of $\bar Q$ with degree $d$, and write


$$
Q=Q^{(0)}+pQ^{(1)}.
$$


For $i,j<s$,


$$
d+i+j\le d+2s-2=p-n-d<t_p,
$$


where the last inequality follows from $h=n+d-t_p>0$. Hence
$\mathscr P_p(Q^{(0)}f_if_j)=0$. Formula (12) gives


$$
\boxed{
R_{\rm end,ij}\equiv
\mathscr R_p^{\rm reg}(\bar Qf_if_j)
+\mathscr P_p(\overline{Q^{(1)}}f_if_j)
\pmod p.
}
\tag{13}
$$



The second term involves only coefficient indices


$$
a+i+j\ge t_p.
$$


These necessarily have $a>d$. Thus it depends precisely on the residues


$$
\boxed{Q_a/p\bmod p,\qquad a>d,}
\tag{14}
$$


of the vanished leading coefficients.

This is a **family-specific arithmetic obstruction**: when (5) fails, the residual matrix may depend on the primitive polynomial modulo $p^2$, even though its highest-pole rank depends only on $Q\bmod p$. Reducing the derangement equations only modulo $p$ discards exactly this information.

The bounded next algebraic problem is therefore clear:

* solve the actual orthogonality equations modulo $p^2$, with primitive-ray normalization;
* extract only the coefficients (14) that enter (13);
* test the resulting small residual matrix.

This is more specific than the residual determinant gate, but it does not yet bound those determinants or their higher valuations.

## 4. Independent audit of A4’s analytic improvements

### 4.1 The $\theta^{-1}$ stationary bound passes

In an absolute-weight orthonormal basis beginning with the normalized Christoffel minimizer, A4 has


$$
A=\begin{pmatrix}a&h^T\\h&C\end{pmatrix},\qquad \|A\|\le1.
$$


The lower block of $I-A^2\ge0$ gives


$$
hh^T+C^2\le I.
$$


Congruence by $C^{-1}$ yields


$$
(C^{-1}h)(C^{-1}h)^T\le C^{-2}-I.
$$


Since the largest eigenvalue of the right side is at most
$\theta^{-2}-1$,


$$
\|C^{-1}h\|^2\le\theta^{-2}-1.
$$


For $x=(1,-C^{-1}h)^T$,


$$
Ax=(a-h^TC^{-1}h,0)^T.
$$


Consequently


$$
|a-h^TC^{-1}h|\le\|x\|\le\theta^{-1}.
$$



The endpoint-one stationary polynomial is $\sqrt{\lambda_{\mathcal M}}$ times this normalized vector, so the quadratic scaling is exactly


$$
\boxed{|\mathcal J(F^2)|\le\lambda_{\mathcal M}/\theta.}
$$


There is no missing square root or extra factor.

### 4.2 The spectral floor and determinant monotonicity pass

The eigenvalues of $C$ have absolute values at most one, so


$$
|\det C|\le\min_i|\lambda_i(C)|=\theta.
$$


Thus


$$
\theta\ge\frac{|\det H|}{\det G}.
$$



For positive definite matrices, $0<A\le B$ implies
$\det A\le\det B$: apply the congruence $B^{-1/2}$ and multiply the resulting eigenvalues, all at most one. This justifies both determinant comparisons in A4’s argument.

The weight bound is


$$
G\le7C_nW.
$$


Dividing $u_i$ by $y+1$ gives a monic triangular basis with determinant-one transition. The bound $(y+1)^2\le4$ therefore gives


$$
\det W\le4^r\det\mathsf H_r.
$$


Finally $\det H=\det(LH)/L^r$, so the constant is indeed


$$
\boxed{
\theta\ge
\frac{|\det(LH)|}{(28LC_n)^r\det\mathsf H_r}.
}
$$


The Cauchy determinant displayed by A4 has the correct numerator factors $4(j-i)^2$.

These proofs establish the finite-index inequalities. They do not give a useful asymptotic spectral budget.

## 5. Primitive denominator and whole error retained

Nothing above changes the center or its normalization:


$$
g=\gcd(|A|,|B|),\qquad
p^{\rm cen}=-\frac{\operatorname{sgn}(B)A}{g},
\qquad
q^{\rm cen}=\frac{|B|}{g}>0.
$$


The complete evaluated error remains


$$
q^{\rm cen}(e+\pi)-p^{\rm cen}
=
\frac{q^{\rm cen}}{Q(-1)}
\int_0^1
\left(e^x+\frac4{1+x^2}\right)
Q(x^2)F_n(x^2)^2\,dx.
$$


Both periods, the final gcd, and the actual denominator are retained.

On the regular domain, the inherited dyadic theorem makes the centers pairwise distinct and hence implies that at most one whole error vanishes. This dependency is unchanged; the new modular lemmas alone do not prove nonvanishing.

## Concluding handoff

### (1) New result and proof status

**Proved here:**

* the coefficient-extraction form (3) of the actual derangement orthogonality equations;
* the pole-free residual window $d_p>(p-1)/4$, in which the first Schur layer is the explicit small matrix (8);
* the exact lift correction (13), identifying the lost primitive-coefficient data when the degree drops farther;
* independent confirmation of A4’s stationary improvement, determinant monotonicity, and all spectral-floor scaling factors.

No uniform residual-unit theorem or odd-$q$ bound is claimed.

### (2) Exact remaining bottleneck

The missing family-specific statement is a nonvanishing or controlled-valuation theorem for the explicit matrix (8), subject to the actual equations (3); in the deeper degree-drop case it must additionally incorporate (14).

More globally, no adequate bound has been proved for the actual odd denominator multiplied by the whole signed approximation error. The irrationality of $e+\pi$ remains unresolved.

### (3) Bounded computation request

One new diagnostic, rather than a repeat of the $n=5,p=17$ audit:

* **Input:** $n=17$, and primes $p=53,59,61$.
* **Compute:** the actual primitive orthogonal ray modulo $p^2$, certifying its normalization against the exact rational ray or a saturated integer-kernel computation; its degree $d_p$; the constraints (3); and the residual matrix from (8) or (13), as appropriate.
* **Expected verifiable output:** $d_p$, $\bar Q(-1)$, the two residual determinants modulo $p$, and verification against the first layer of the exact Schur construction.
* **Bound:** one defining $17\times18$ integer kernel and three local reductions. With no degree drop, the residual sizes are respectively $2,5,6$.

These outputs would test the new reduction and identify the next algebraic obstruction. They would not prove an infinite prime or index assertion.
