> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform actual branch conditioning down to parameters of order the row cut

Date: 2026-09-13. Original bounded continuation by audit_computations.

This proves a new uniform estimate for the actual adjacent two-branch matrix,
including the previously untreated range where the positive parameter is only
of order the row cut. No numerical experiment, fixed-positive-ratio limit, or
unproved branch-root assertion enters the proof.

The exact row normalization, transfer, and Casoratian are those of
`raw_global_adjacent_branch_conditioning.md`. The local argument below replaces
the constants in its fixed-ratio theorem; those constants are not extended to
a shrinking ratio.

## 1. Statement and the preserved seed normalization

Let



$$
a_k=\frac{k^2}{\sqrt{4k^2-1}},\qquad a_0=0,
$$



and let the real symmetric row matrix have entries



$$
K_{kk}=a_k^2+a_{k+1}^2-k(k+1),\quad
K_{k,k+1}=-a_{k+1},\quad K_{k,k+2}=a_{k+1}a_{k+2}.
$$



Use the actual polynomial rows with seeds
$R_0=(1,0)$, $R_1=(\sqrt3/2,1)$, and write



$$
P_N(x)=\begin{pmatrix}R_N(x)\\R_{N+1}(x)\end{pmatrix}.
$$



There is an absolute constant $C$ such that, for all sufficiently large
$N$, uniformly for every real $x\ge2N$,



$$
\boxed{\log\operatorname{cond}_2 P_N(x)
\le C\left(1+(\log N)^2+\frac{N\log N}{\sqrt{x}}\right)
 +(N\bmod2)\log(1+x).}
\tag{1}
$$



In particular, for every fixed $C'>0$, uniformly on the nonempty interval
$2N\le x\le C'N^2$,



$$
\boxed{\operatorname{cond}_2 P_N(x)
\le \exp\{C_{C'}\sqrt N\log N\}.}
\tag{2}
$$



Both matrices are invertible in this range. More precisely, with



$$
D_N(x)=\frac{|\det(K_N-xI)|}
 {\prod_{h=0}^{N-1}a_{h+1}a_{h+2}},
$$



the exact Casoratian gives $|\det P_N|=D_N$. If $H_N(x)$ denotes the
right side of (1), the two actual singular values satisfy



$$
\boxed{D_N(x)^{1/2}e^{-H_N(x)/2}
 \le\sigma_i(P_N(x))\le D_N(x)^{1/2}e^{H_N(x)/2},
 \qquad i=1,2.}
\tag{3}
$$



Thus the theorem is an actual two-column bound, not merely a bound for a
boundary Weyl matrix. It retains the unequal polynomial powers of the odd
fixed-cut seed through the last term of (1).

The rational adjacent branch matrix $P_N^{\rm rat}$ satisfies


$$
P_N=\operatorname{diag}(\sqrt{2N+1},\sqrt{2N+3})
P_N^{\rm rat}\operatorname{diag}(1,1/\sqrt3)
$$

.
These diagonal transformations have condition-number product at most three.
Thus (1)--(2) hold for $P_N^{\rm rat}$ after adding $\log3$ to the
logarithmic bound. For the absolute singular-value assertion (3), its
determinant scale must also be changed to



$$
D_N^{\rm rat}(x)
=\frac{\sqrt3\,D_N(x)}{\sqrt{(2N+1)(2N+3)}}.
$$



Equation (3) then holds with $D_N^{\rm rat}$ and $H_N+\log3$.

## 2. Exact positive energy form of each uncoupled parity block

Write $K_j=K_{0,j}-J_j$, where $K_{0,j}$ is the principal compression
of $J^2-\Lambda$, and $\|J_j\|\le j$. Put



$$
d_l=a_l^2+a_{l+1}^2-l(l+1),\qquad c_l=a_{l+1}a_{l+2},
\quad c_{-2}=c_{-1}=0.
$$



The elementary coefficient bounds used in the previous local-resolvent proof
are



$$
a_l^2=l^2/4+\delta_l,\quad 0\le\delta_l\le1/12,
$$





$$
c_l=(l+1)(l+2)/4+\epsilon_l,\quad0\le\epsilon_l\le1/6.
$$



For negative subscripts in the second formula the corresponding error is
zero. Consequently



$$
V_l:=d_l+c_{l-2}+c_l
=3/4+\delta_l+\delta_{l+1}+\epsilon_{l-2}+\epsilon_l,
\qquad |V_l|\le2.
\tag{4}
$$



On either finite parity chain, with its boundary value beyond the largest
index set to zero, let $\mathcal D_j$ be the weighted graph Laplacian with
edge weights $c_l$. The missing outward edge at the largest index is a
Dirichlet edge and remains in its diagonal. The lower edge at original index
zero or one has weight zero. Then exactly



$$
K_{0,j}=-\mathcal D_j+\operatorname{diag}(V_l),\qquad
\mathcal D_j\succeq0.
\tag{5}
$$



This form, rather than an entrywise operator-norm perturbation, is what allows
the ratio $x/j^2$ to approach zero.

Let $\iota_j$ insert the last two coordinate vectors. Since
$-jI\preceq J_j\preceq jI$, (4)--(5) and order reversal under positive
inversion imply



$$
\iota_j^T(\mathcal D_j+(x+j+2)I)^{-1}\iota_j
\preceq\iota_j^T(xI-K_j)^{-1}\iota_j
\preceq
\iota_j^T(\mathcal D_j+(x-j-2)I)^{-1}\iota_j.
\tag{6}
$$



Here the outer matrices are diagonal in the two parity boundary coordinates.
For $x\ge2N$, $j\le N$, and $N\ge4$, both comparison masses
$y=x\pm j\pm2$ are at least $x/4$. In particular all the inverses in
(6) exist. The known bound $K_j\preceq(j+3/4)I$ also directly verifies
invertibility of the actual resolvent throughout the stated range.

## 3. Exact constant-chain boundary formulas

Fix a cut $j$, a mass $y>0$, and a constant edge weight $w=j^2/4$.
For the half-line Dirichlet Laplacian, whose diagonal is $2w$ and
off-diagonal is $-w$, set



$$
q=q(y/j^2)=\exp[-2\operatorname{arsinh}(\sqrt y/j)],
\qquad r_\infty(y)=q/w=\frac{m(y/j^2)}{j^2},\quad m=4q.
\tag{7}
$$



On vertices $0,\ldots,L-1$, retain the left Dirichlet edge. At the other
end either keep the edge to a zero value (Dirichlet), or delete that edge
(Neumann). The two boundary inverse entries are exactly



$$
r_D(y)=\frac q w\frac{1-q^{2L}}{1-q^{2L+2}},\qquad
r_N(y)=\frac q w\frac{1+q^{2L-1}}{1+q^{2L+1}}.
\tag{8}
$$



For example, solve the interior recurrence by $Aq^k+Bq^{-k}$; the right
conditions are respectively $v_L=0$ and $v_L=v_{L-1}$. The first row
then gives (8). These formulas hold also for $L=1$: their denominators
reduce to $y+2w$ and $y+w$, respectively. They yield the uniform bounds



$$
1-q^{2L}\le r_D/r_\infty\le1,
\qquad1\le r_N/r_\infty\le1+q^{2L-1}.
\tag{9}
$$



There is no factor $(1-q)^{-1}$ in (9).

## 4. Boundary-layer bracketing, uniformly at small positive ratios

Let $N$ be large and $x\ge2N$. For a cut $j\le N$, choose



$$
L=\left\lceil20(1+j/\sqrt x)\log N\right\rceil.
\tag{10}
$$



We use this construction only when $j\ge A\log N$, where $A$ is an
absolute constant chosen sufficiently large below. Then, for all sufficiently
large $N$, $L+2\le j/8$. Thus this boundary layer lies strictly inside
both actual parity chains.

Reverse one chain from its top original index $b=j-1$ or $j-2$.
The boundary Dirichlet edge and all the next $L$ edges have weights
$c_b,c_{b-2},\ldots,c_{b-2L}$. Their explicit coefficient formulas give



$$
(1-\delta)w\le c_{b-2r}\le(1+\delta)w\quad(0\le r\le L),
\qquad\delta=\frac{8(L+2)}j.
\tag{11}
$$



For the lower bound one may use
$(b-2r+1)(b-2r+2)\ge(j-2L-1)^2$; for the upper bound use
$(b+1)(b+2)\le j(j+1)$ and $\epsilon_l\le1/6$.
The deliberately loose constant in (11) covers both parities.

For a positive matrix $H$, its boundary inverse entry is the reciprocal
of the minimum energy subject to $v_0=1$. Deleting everything beyond
the layer, including the edge crossing its far end, decreases this minimum.
Restricting to vectors zero beyond the layer increases it. Consequently the
full variable-chain boundary inverse entry $r_{\rm var}(y)$ is bracketed
by the variable Dirichlet and Neumann entries. By (11), their positive energy
forms, including the mass term, are between $(1-\delta)$ and
$(1+\delta)$ times the respective constant forms. Thus



$$
\frac{r_D(y)}{1+\delta}\le r_{\rm var}(y)
\le\frac{r_N(y)}{1-\delta}.
\tag{12}
$$



This variational argument is valid even though the unexamined part of the
chain has very different coefficients. Only positivity of its edge and mass
energies was used.

Uniformly for the comparison masses in (6), $y\ge x/4$. The inequality
$\operatorname{arsinh}u\ge u/(1+u)$, together with (10), gives



$$
L\operatorname{arsinh}(\sqrt y/j)\ge10\log N,
\qquad q(y/j^2)^{2L-1}\le N^{-20}.
\tag{13}
$$



To see the first inequality, put $a=j/\sqrt x$ and use
$(1+a)\operatorname{arsinh}(1/(2a))\ge(1+a)/(2a+1)\ge1/2$.
For the second use $2L-1\ge L$. No lower fixed bound on $y/j^2$
has been imposed.

It remains to compare the constant-chain masses with $x$. From (7),



$$
\frac{d}{dy}\log r_\infty(y)=-\frac1{\sqrt{y(y+j^2)}}.
\tag{14}
$$



For $j\ge8$, all masses between $x$ and $x\pm(j+2)$ are at least
$x/4$, so



$$
\left|\log\frac{r_\infty(x\pm(j+2))}{r_\infty(x)}\right|
\le\frac{j+2}{\sqrt{(x/4)(x/4+j^2)}}\le\frac3{\sqrt x}.
\tag{15}
$$



Combining (6), (9), (12), (13), and (15), and then using the Loewner
sandwich to bound the norm of the symmetric two-by-two difference, proves



$$
\boxed{\iota_j^T(xI-K_j)^{-1}\iota_j
=\frac{m(x/j^2)}{j^2}(I+E_j^{\rm bd}),\qquad
\|E_j^{\rm bd}\|\le C_0\left(\frac{\log N}j+
\frac{\log N}{\sqrt x}\right).}
\tag{16}
$$



This holds for $A\log N\le j\le N$, uniformly in $x\ge2N$, once
$A$ and then the lower threshold on $N$ are large enough. For a fully
explicit intermediate estimate before collecting constants, one can take
$8\delta+10/\sqrt x+4N^{-20}$ on the right when $\delta\le1/8$.

## 5. Exact scalar-normalized transfer and accumulation

The exact coupling and transfer are



$$
\Gamma_j=\begin{pmatrix}a_{j-1}a_j&0\\-a_j&a_ja_{j+1}\end{pmatrix},
\quad T_j=\Gamma_j^{-1}
 [\iota_j^T(xI-K_j)^{-1}\iota_j]^{-1},\quad P_j=T_jP_{j-2}.
\tag{17}
$$



The explicit coefficients give



$$
\Gamma_j=(j^2/4)(I+H_j),\qquad\|H_j\|\le4/j\quad(j\ge8).
$$



Consequently (16) gives the actual ordered factorization



$$
\boxed{T_j(x)=\lambda(x/j^2)(I+E_j),\quad
\lambda(c)=4/m(c)=(\sqrt c+\sqrt{c+1})^2,
\quad\|E_j\|\le C_1\left(\frac{\log N}j+
\frac{\log N}{\sqrt x}\right).}
\tag{18}
$$



This is an error bound, not a claimed first-order expansion. Choose the
starting cut $J_N$ of the same parity as $N$ to be the least such
integer at least $A\log N$, with $A\ge16C_1$ also large enough for
Section 4. For all large $N$, the errors in (18) are at most $1/2$.
All scalar factors are positive. Since
$\log\operatorname{cond}(I+E)\le3\|E\|$ when $\|E\|\le1/2$,



$$
\log\operatorname{cond}
 [T_NT_{N-2}\cdots T_{J_N+2}]
\le C_2\left((\log N)^2+\frac{N\log N}{\sqrt x}\right).
\tag{19}
$$



The scalar product in (18) can also be removed explicitly; the norms of the
remaining ordered product and of its inverse are bounded by the exponential
of the right side of (19), after a constant enlargement. Neither the
noncommutativity nor the accumulated error has been discarded.

For completeness the growing initial cut $J_N$ does not require a new
seed estimate. The earlier exact uniform bound is



$$
T_j=\tau_j(I+\widetilde E_j),\quad \tau_j>0,\quad
\|\widetilde E_j\|\le64(1+j^2/x)(11/j+5j/x).
\tag{20}
$$



Its proof uses only $x\ge2(j+3/4)$, which holds for
$j\le J_N=O(\log N)$ and $x\ge2N$, for all sufficiently large $N$.
In the same range $j^2\le x$, so (20) is at most $2048/j$.
Start at one fixed sufficiently large even cut $J_*$, or $J_*+1$ for
odd parity. Accumulation to $J_N$ therefore costs only
$O(1+\log J_N)$ in logarithmic condition number.

At that fixed cut, the actual Casoratian and the entry-degree bound give



$$
\operatorname{cond}P_{J_*}(x)\le C_*,\qquad
\operatorname{cond}P_{J_*+1}(x)\le C_*(1+x)
\tag{21}
$$



for all sufficiently large $x$. Indeed the determinant has degree equal
to the cut, while each entry has degree at most the ceiling of half that
cut; its determinant is bounded below by a constant times that power of
$x$ outside the fixed row spectrum. These are the actual seed matrices,
with no replacement by a diagonal or freely rescaled starting matrix.

Equations (19)--(21) prove (1). The exact determinant then gives (3), and
the bounded quadratic upper range gives (2).

## 6. Scope for the rational-surrogate exceptional block

For the rational approximation in
`raw_rational_surrogate_rank_improvement.md`, the first bin center is
$\rho_0=3n$ and $M_n=2n+3/4$. Thus the repeated denominator nodes begin
at $x=5n+3/4$. With row cut $N=2n$, these satisfy $x>2N$; the largest
centers are of order $n^2$. Therefore (2) applies uniformly to every one
of those actual positive nodes, including the lowest ones that were outside
the previous compact-$x/N^2$ results.

The argument proves real-parameter branch conditioning and the scalar-normalized
transport bound (18)--(19). It does not yet give uniform high derivatives at
these nodes, a confluent interpolation inverse, or a lower bound for the
remaining growing exceptional determinant. In particular, repeated-node
interpolation cannot be declared stable merely from (2). Nor does this theorem
control the primitive arithmetic size or the whole endpoint remainder needed
to decide the rationality of $e+\pi$.
