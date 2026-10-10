> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An exact Hermite-resultant factorization and a height bound for the actual norm carrier

Date: 2026-09-13. Original bounded arithmetic continuation by
audit_sources. Independent root review in
raw_norm_resultant_height_root_review.md passes the complete proof.
The preceding exponential-pair Jacobian investigation
remains separately marked as an unresolved, pending-review attempt.

This note fixes an explicit small-prime denominator clearer for the
actual norm carrier and proves


$$
\log c_d\le\frac{19}{2}d^3\log d+O(d^3).
$$


The constant is deliberately crude. This does not improve the
quadratic-logarithmic bound obtainable directly from the original
extremal minors. The useful new identity is that the square of the
cleared norm is one specific homogeneous resultant, with its entire
factor at infinity evaluated explicitly. No unproved cancellation
of that resultant's content is used.

## 1. Prior normalization and the arithmetic target

The actual norm in raw_accessory_finite_algebra_and_norm_carrier.md is


$$
\mathcal N_d(t)=
\operatorname{Norm}_{\mathscr A_d/\mathbb Q}(R_0+tR_1),\qquad
\mathscr A_d=\mathbb Q[\beta,\gamma]/(E_1,E_0),
\tag{1}
$$


of rank $D_d=(d+1)(d+2)/2$. The equations retain


$$
E_1=d![z]L^{[1]}B^*,\qquad E_0=d![1]L^{[1]}B^*,
$$


and $R_0,R_1$ are the unscaled signed-cofactor residues.
They are integer polynomials. The already proved large-prime
comparison for any small-prime clearer is


$$
v_p(F_{d+1})\le v_p(c_d)\le D_dv_p(F_{d+1}),
\qquad p>3d+3.
\tag{2}
$$


An arbitrary extra small-prime multiplier can inflate $c_d$
without limit, so a full height statement must specify its clearer.
Here it is specified in (8) below. The large-prime part is
independent of that choice.

I inspected the original raw endpoint normalization, the exact
factorization $\mathcal E_n=(-1)^nF_nZ_n$, and the existing
cofactor/primitive-error notes. Their central warning is retained:
the content of an original Taylor matrix, the full polynomial
content, and the evaluated endpoint-pair gcd are different objects.
The bound here concerns $F_{d+1}$'s norm carrier through (2);
it is not directly a primitive endpoint-height estimate.

## 2. Turn the weighted system into a homogeneous resultant

Put $n=d+1$ for this section, and substitute $\gamma=y^2$.
Homogenize the following polynomials in $(x,y,Z)$:


$$
\begin{aligned}
f_1(x,y,Z)&=E_1(x,y^2)^{h_n},\\
f_0(x,y,Z)&=E_0(x,y^2)^{h_{n+1}},\\
g_t(x,y,Z)&=(R_0(x,y^2)+tR_1(x,y^2))^{h_{2n}}.
\end{aligned}
\tag{3}
$$


The superscript specifies the homogenizing degree, not a power.
Weighted degrees in $(\beta,\gamma)$, with weights $1,2$,
are precisely ordinary degrees after this substitution. Thus
the first two degrees are exactly $n,n+1$; the third is at
most $2n$, and is homogenized to that degree even if it is lower.

Let $P_r=r![u^r]\exp(xu+\gamma u^2/2)$, so


$$
P_r=xP_{r-1}+(r-1)\gamma P_{r-2}.
$$


The reviewed leading-form computation gives


$$
f_1(x,y,0)=P_n(x,y^2),\qquad
f_0(x,y,0)=y^2P_d(x,y^2).
\tag{4}
$$


The binary resultant of (4) is exactly


$$
\boxed{\Gamma_d=\prod_{k=1}^d k^k.}
\tag{5}
$$



Here is the sign and factor calculation. The binary form
$P_n(x,y^2)$ has value $1$ at $(1,0)$, so the factor
$y^2$ contributes $1$. For the monic univariate
$H_r(x)=P_r(x,1)$, set
$\rho_r=\operatorname{Res}(H_r,H_{r-1})$.
Swapping the two factors contributes
$(-1)^{r(r-1)}=1$; reduction by $H_{r-1}$ then gives


$$
\rho_r=(r-1)^{r-1}\rho_{r-1},\qquad \rho_1=1.
$$


This proves (5). In particular there are no intersection
points at infinity, and every prime divisor of $\Gamma_d$
is at most $d$.

Use the homogeneous resultant normalized by
$\operatorname{Res}(x^a,y^b,Z^c)=1$, and set


$$
\mathcal T_d(t)=\operatorname{Res}_{x,y,Z}(f_1,f_0,g_t)
\in\mathbb Z[t].
$$


Then


$$
\boxed{\mathcal T_d(t)=
\Gamma_d^{\,2n}\mathcal N_d(t)^2.}
\tag{6}
$$



For clarity, the precise product-formula argument includes
multiplicities and points on the coordinate axes. On the
affine patch $Z=1$, the intersection algebra is


$$
\mathscr A_d[y]/(y^2-\gamma),
$$


free of rank two over $\mathscr A_d$. Multiplication by
$R_0+tR_1$, an element of the base algebra, therefore has
norm $\mathcal N_d(t)^2$, including the branch $\gamma=0$
and any nonreduced local algebra. The homogeneous Poisson
formula multiplies that affine norm by the binary resultant
at infinity to the degree $2n$ of $g_t$. Its sign and
constant can also be fixed by putting $g_t=Z^{2n}$;
both sides then equal $\Gamma_d^{2n}$.

One may establish the product formula first for generic
coefficients, where the affine intersection is simple and
misses the axes, and extend it on the open set where the
binary resultant is nonzero. This gives (6) without
assuming that the actual affine points are simple or in
the algebraic torus. The multiplicity-sensitive Poisson
formula is supported by D'Andrea–Sombra,
[primary PDF](https://arxiv.org/pdf/1310.6617), Theorem 1.1,
printed p. 3. Its torus statement requires nonzero
directional resultants; here it is used on that generic
open set before the described homogeneous specialization.

## 3. An explicit integral clearer and exact content square

Equation (6) implies


$$
\boxed{\mathcal Q_d(t):=\Gamma_d^{\,n}\mathcal N_d(t)
\in\mathbb Z[t].}
\tag{7}
$$


Indeed a rational polynomial whose square is integral is
integral. For each prime, the Gauss valuation of its square
is twice its Gauss valuation; a negative integral valuation
could not have a nonnegative double. This proof avoids
choosing a denominator by reducing multiplication matrices.

Henceforth choose exactly


$$
q_d=\Gamma_d^{d+1},\qquad
c_d=\operatorname{content}(\mathcal Q_d)>0.
\tag{8}
$$


The norm is nonzero by the already proved characteristic-zero
full residue incompatibility. Gauss's content lemma and (6)
give the additional exact identity


$$
\boxed{\operatorname{content}(\mathcal T_d)=c_d^2.}
\tag{9}
$$


This keeps all valuations. No large-prime factor at infinity
has been introduced. A minimal common denominator of
$\mathcal N_d$ divides $q_d$, so the same upper bounds
also hold for the content defined using that minimal clearer.
The explicit denominator cost is


$$
\log q_d=(d+1)\sum_{k=1}^d k\log k
=\tfrac12d^3\log d+O(d^3).
\tag{10}
$$



## 4. Elementary bounds for the actual input coefficients

All norms below are coefficient $\ell^1$-norms in all their
displayed polynomial variables. Put


$$
H=32(d+1)^3,\qquad
H_E=d!\,H(1+H)^d,\qquad
H_R=(10d+4)(d+1)(4H)^d.
\tag{11}
$$


Then


$$
\|E_1\|_1+\|E_0\|_1\le H_E,\qquad
\|R_0\|_1+\|R_1\|_1\le H_R.
\tag{12}
$$



Here are direct bounds, rather than assumptions about spectral
root locations. For every $0\le m\le d$, the coefficient
norm of $L^{[1]}z^m$ is at most $H$. Its five possible
coefficients are the ones displayed in the cokernel recurrence
of raw_exponential_pair_jacobian_and_pole_pairing.md, together
with its top coefficient $m-d$. Bounding their integer
coefficients by the triangle inequality gives the chosen
$32(d+1)^3$.

Write $B^*=\sum_{r=0}^d b_rz^{d-r}$, $b_0=1$.
At downward step $r$, the new pivot is $-r$, while every
other contribution comes from earlier $b_j$. Thus


$$
\|b_r\|_1\le H\sum_{j<r}\|b_j\|_1,\qquad
\sum_{r=0}^d\|b_r\|_1\le(1+H)^d.
$$


Multiplying by $L^{[1]}$ and by the retained $d!$ proves
the first inequality in (12).

Each row of the cofactor matrix $U_d$ has at most four
nonzero entries, each of coefficient norm at most $H$.
Expansion by permutations, bounded by the product of row
norms, therefore gives


$$
\sum_{j=0}^d\|[z^j]C^*\|_1\le(d+1)(4H)^d.
$$


The residue numerator is


$$
2(C^*)'-[(\beta+6d+2)z+\gamma-2d]C^*.
$$


Its norm is at most $10d+4$ times the preceding bound.
Reduction modulo $1+z^2$ only replaces powers of $z$ by
$\pm1,\pm z$ and cannot increase the norm. This proves
the second inequality of (12).

In particular,


$$
\log H_E=4d\log d+O(d),\qquad
\log H_R=3d\log d+O(d).
\tag{13}
$$


No factorial has been cancelled from the actual equations
when deriving these bounds.

## 5. Resultant height and the resulting carrier estimate

Sombra's
[primary paper](https://arxiv.org/pdf/math/0211449),
Lemma 1.3, printed p. 2, bounds the absolute value of a
specialized sparse resultant by the product of the input
coefficient $\ell^1$-norms raised to their partial degrees.
For the full degree simplexes in two variables, the lattice
index is one and those degrees are the products of the
other two polynomial degrees. Zero specialized coefficients
are allowed. Thus it applies to the ordinary homogeneous
resultant in (6), viewed on its affine coefficient chart.
This is a height theorem, not a root-separation assumption.

For $|t|=1$, substitution $\gamma=y^2$ and homogenization
preserve coefficient norms, and (12) gives


$$
|\mathcal T_d(t)|
\le H_E^{\,2n(n+1)+2n^2}\,H_R^{\,n(n+1)}
=H_E^{\,2n(2n+1)}H_R^{\,n(n+1)}.
$$


Cauchy's coefficient formula bounds every coefficient by
the same number. Since the nonzero integer polynomial
$\mathcal T_d$ has content $c_d^2$, we obtain the explicit
bound


$$
\boxed{\log c_d\le
n(2n+1)\log H_E+\frac{n(n+1)}2\log H_R,
\qquad n=d+1.}
\tag{14}
$$


Using (13),


$$
\boxed{\log c_d\le
\frac{19}{2}d^3\log d+O(d^3).}
\tag{15}
$$


The same bound holds for its large-prime part. This route
avoids the much larger denominators and coefficient growth
that can arise from naive monomial reduction of the
rank-$D_d$ multiplication matrices.

## 6. Comparison with original minors and the remaining gap

Even an elementary direct estimate on the original matrix
already has the smaller order $O(n^2\log n)$.
To make that comparison concrete, the $2n$ columns of
$X_n$ each have the explicit factor $j!$, for
$0\le j<n$, in both blocks:


$$
(k)_j/j!=\binom{k}{j},\qquad
\frac{k!\tau_{k-j}}{j!}
=\begin{cases}
\pm\binom{k}{j}(k-j-1)!,&k-j\text{ odd},\\
0,&k-j\text{ even}.
\end{cases}
$$


Removing these factors changes no prime valuation above
$3n$. A nonzero maximal minor of the remaining matrix
is bounded by Hadamard, using $k\le3n$, by


$$
(2n)^n\,2^{6n^2}\,((3n)!)^n.
$$


Its logarithm is $3n^2\log n+O(n^2)$. The large-prime
part of $F_n$ divides that minor, so it satisfies the
same bound. Sharper pre-existing determinant/content
arguments need not be repeated to see the comparison:
(15) is not a numerical growth improvement for $F_n$.

The exact Hermite factor (5) removes all uncertainty about
the contribution from infinity. It does **not** remove
the cost of multiplying the residue values at
$D_d\asymp d^2$ finite accessory points. A fixed small-prime
factor in the cofactor $C^*$ can be stripped without
changing the large-prime target, but no proved such
normalization eliminates this finite-product cost.

In particular, the pole identity
$4\operatorname{Res}(D,C)\operatorname{Res}(D,J)=\kappa^2$
holds only after imposing the full residue compatibility.
It is not an identity at every characteristic-zero
exponential accessory point used in (1).
Indeed there is no full characteristic-zero accessory
point at all. Taking its product over the exponential
points would therefore be an invalid extension of its
hypotheses.

A concrete next target is an exact factorization of the
integer polynomial $\mathcal T_d(t)$ separating its
coefficient content from its primitive $t$-dependent
part, beyond the known square in (6). An explicit product
of known small-prime factors accounting for all but
$\exp(o(n^2))$ of that content would be useful.
Alternatively one needs a small-prime Bézout certificate
for $R_0,R_1$ in the finite algebra whose height is on
that smaller scale. Generic resultant height inequalities
bound the entire product and cannot provide that
cancellation. Neither (15) nor the earlier Jacobian
transversality results close the required primitive
denominator/error-rate gap.
