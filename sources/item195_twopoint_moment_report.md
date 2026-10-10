> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 195 — two-point Hermite moments and the conductor obstruction

Checked: 2026-08-30 (Beijing time)

## 1. Scope and verdict

Stay in the frozen Item 174/180 rank-two cell (e=1,kappa=0).  Put



$$
N_p=\left\lfloor\frac{p-1}{3}\right\rfloor,
 \qquad
 Z_p=\{0\le s\le N_p:\Delta_{p,s}=0\},
 \qquad
 C_p(h)=\#\{s:s,s+h\in Z_p\}.
\tag{1.1}
$$



The requested collision bound remains open.

> **PROVED — exact bounded-jet moment representation.**  Every coefficient
> entering $\Delta_{p,s}$ is recovered from four Hasse-jet moments of one
> fixed rational map
> 

$$
> R(x)=\frac{x^3(1-x)^3}{(1+x+x^2+x^3)^2}.
> \tag{1.2}
>
$$


> Consequently both $\Delta_{p,s}$ and $\Delta_{p,s+h}$ are fixed finite
> linear combinations of double moments.  The shift only replaces
> $R(x)R(y)$ by its $h$-twist; see Sections 2--4.

> **PROVED — bounded Kummer conductor, but no zero-count consequence.**
> After Teichmuller lifting, every pure term is a rank-one tame Kummer sum
> on the same six-punctured projective line.  The number of punctures and
> the number of summands are independent of $p,s,h$.  Thus a genuinely
> bounded-conductor formulation exists.  However its reduction modulo the
> chosen prime above $p$, not its complex size, is the determinant.  The
> Jacobi family in Section 6 has the same bounded-conductor property and a
> linear interval of mod-$p$ zeros.  Bounded conductor alone therefore
> cannot prove $C_p(h)=O(h)$.

> **PROVED — exact algebraic collision polynomial and a growing-degree
> obstruction.**  The natural fixed-map extension has a forced tail of
> $p-1-N_p$ zeros.  Its interpolation polynomial has degree at least
> $p-1-N_p$, so a direct rational or additive-character realization in
> the exponent parameter has complexity $\Omega(p)$.  Removing the known
> tail leaves a residual polynomial $G_p$ of degree at most $N_p$, and
> $C_p(h)$ is bounded by
> $\deg\gcd(G_p(S),G_p(S+h))$.  No $O(h)$ bound for this gcd is proved.

> **FINITE EXACT ONLY.**  The certificate checks all 100 admissible pairs
> for the nine primes $17\le p\le47$: 12,464 rational-jet identities,
> 2,000 moment identities, 2,000 alias reconstructions, and 100 independent
> Item 180 determinant comparisons.  In this small scope the full
> interpolation degree is $p-1$ and the residual degree is $N_p$.
> These degree equalities are not extrapolated.

Thus this item supplies the exact two-point moment model and identifies the
missing arithmetic input: a determinant-specific theorem controlling
reduction at the distinguished prime above $p$.  It proves neither the
Sidon assertion nor any sublinear bound for $r_p$.

## 2. A degree-(4p-6) polynomial with the right coefficients

Retain



$$
Q=1+x+x^2+x^3,
 \qquad
 W_s=\frac{x^{3s}(1-x)^{5s+2}}{(1-x^4)^{2s+2}}
     =\sum_{n\ge0}w_n(s)x^n.
\tag{2.1}
$$



For an admissible pair and $p\ge17$, define



$$
\widetilde W_{p,s}
 =x^{3s}(1-x)^{5s+2}(1-x^4)^{p-2s-2}
 =\sum_{n=0}^{4p-6}\widetilde w_n(s)x^n.
\tag{2.2}
$$



In characteristic $p$,



$$
\widetilde W_{p,s}=W_s(1-x^4)^p=W_s(1-x^{4p}).
\tag{2.3}
$$



Hence $\widetilde w_n=w_n$ for every $n<4p$, in particular for all
indices in the Item 174 determinant.  Since $Z_s=QW_s$, that determinant
is



$$
\Delta_{p,s}
 =z_{p-1}w_{2p-1}-z_{2p-1}w_{p-1},
 \qquad
 z_n=w_n+w_{n-1}+w_{n-2}+w_{n-3}.
\tag{2.4}
$$



The replacement (2.2) is therefore exact, not an asymptotic truncation.

## 3. Four Hermite moments recover every needed alias

Write $D^{(j)}$ for the $j$-th Hasse derivative.  For a canonical
residue $0\le r\le p-2$, set



$$
M_{r,j}(s)=-\sum_{t\in\mathbf F_p^\times}
 t^{j-r}D^{(j)}\widetilde W_{p,s}(t),
 \qquad 0\le j\le3.
\tag{3.1}
$$



The power-sum identity on $\mathbf F_p^\times$ gives



$$
M_{r,j}(s)=
 \sum_{\ell=0}^{3}
 \binom{r+\ell(p-1)}{j}
 \widetilde w_{r+\ell(p-1)}(s),
\tag{3.2}
$$



where a coefficient beyond degree $4p-6$ is zero.  Only the residue
classes



$$
r\equiv0,1,-1,-2,-3\pmod{p-1}
\tag{3.3}
$$



are needed.  None of them has more than four aliases in (2.2).

Modulo $p$, the matrix in (3.2) is



$$
B_r=\left(\binom{r-\ell}{j}\right)_{0\le j,\ell\le3}.
\tag{3.4}
$$



The polynomials $\binom Xj$ have leading coefficient $1/j!$, and the
four evaluation points are $r,r-1,r-2,r-3$.  Their Vandermonde determinant
is $12$, while $\prod_{j=0}^3j!=12$.  Therefore



$$
\det B_r=1.
\tag{3.5}
$$



This proves uniform invertibility, with no exceptional prime for $p\ge5$.
Let $\mathcal C_{r,\ell}(s)$ denote the $\ell$-th entry of
$B_r^{-1}(M_{r,0},\ldots,M_{r,3})^T$.  Then, using negative subscripts on
$\mathcal C$ for the canonical residues in (3.3), namely
$\mathcal C_{-k,\ell}:=\mathcal C_{p-1-k,\ell}$,



$$
\begin{aligned}
 w_{p-1}&=\mathcal C_{0,1},
 &w_{2p-1}&=\mathcal C_{1,2},\\
 z_{p-1}&=\mathcal C_{0,1}+\mathcal C_{-1,0}
                    +\mathcal C_{-2,0}+\mathcal C_{-3,0},
 &z_{2p-1}&=\mathcal C_{1,2}+\mathcal C_{0,2}
                    +\mathcal C_{-1,1}+\mathcal C_{-2,1}.
\end{aligned}
\tag{3.6}
$$



Equations (2.4), (3.1), and (3.6) are the promised exact four-jet moment
formula for $\Delta_{p,s}$.

## 4. The fixed rational map and the two-point shift

At a point $t\ne0$ with $t^4\ne1$, put



$$
R(t)=\frac{t^3(1-t)^3}{Q(t)^2},
 \qquad B(t)=\frac{1-t}{Q(t)},
\tag{4.1}
$$



and define the bounded jet



$$
\begin{aligned}
 \Psi_j(t,s)=[T^j]&\left(1+\frac{T}{t}\right)^{3s}
 \left(1-\frac{T}{1-t}\right)^{5s+2}\\
 &\times\left(\frac{1-(t+T)^4}{1-t^4}\right)^{-2s-2}.
\end{aligned}
\tag{4.2}
$$



For $j\le3<p$, the truncated binomial coefficients of the last factor
only see



$$
p-2s-2\equiv-2s-2\pmod p.
\tag{4.3}
$$



The value of the un-differentiated $p$-th-power factor supplies one copy
of $1-t^4$.  Direct Hasse differentiation therefore gives



$$
D^{(j)}\widetilde W_{p,s}(t)=B(t)R(t)^s\Psi_j(t,s).
\tag{4.4}
$$



At a nonzero root of $1-t^4$, the exponent
$p-2s-2$ is greater than three for $p\ge17$, so all four jets vanish.
Thus (4.4), with zero contributions at the omitted points, is exact in
(3.1).

Each $\Psi_j$ is polynomial in $s$ of degree at most $j$ and is a
rational function of $t$ with poles only among



$$
0,1,-1,i,-i,\infty.
\tag{4.5}
$$



Expanding (4.2) through $j=3$ gives at most 25 pure rational monomials
across all four jets.  Hence every recovered coefficient in (3.6) is a
fixed finite linear combination of moments of the shape



$$
\sum_{t\in X_p}c_{\alpha,\beta,\gamma}(s)
 t^{3s+\alpha}(1-t)^{3s+\beta}Q(t)^{-2s+\gamma},
\tag{4.6}
$$



where $X_p$ is the complement of (4.5), the offsets are bounded, and
$\deg_s c_{\alpha,\beta,\gamma}\le3$.  Expanding (2.4) gives a fixed
finite sum of double moments on $X_p^2$ with base



$$
\mathcal R(t,u)=R(t)R(u).
\tag{4.7}
$$



A coarse count is already uniform: one recovered coefficient uses at most
25 pure sums, so expanding the two products in (2.4) uses at most 5,000
pure double sums.  This bound is intentionally not optimized.

For $0\le s\le N_p-h$, replacing $s$ by $s+h$ is legitimate in the
same formulas and



$$
\mathcal R(t,u)^{s+h}
                      =\mathcal R(t,u)^h\mathcal R(t,u)^s.
\tag{4.8}
$$



Thus the two-point map $(\Delta_{p,s},\Delta_{p,s+h})$ has one common
moment space.  No coefficient window grows with $p$, and the only new
twist is the explicitly tracked $h$-th power in (4.8).  As an ordinary
rational function, $R^h$ has numerator and denominator degree $6h$, so
$\mathcal R^h$ has bidegree $(6h,6h)$.  In the Kummer interpretation of
Section 6, this changes local characters but adds no singular point and
hence does not increase the tame conductor.

## 5. Exact algebraic collision polynomial

The moment formula is not the only exact representation.  Define for every
integer $0\le s\le p-1$



$$
\begin{aligned}
 U_r(s)&=[x^{p-r}]A_0(x)K(x)^s,\\
 V_r(s)&=[x^{p-r}]A_0(x)H(x)^s,\\
 \mathscr D_p(s)&=(U_2+U_3+U_4)V_5-(V_2+V_3+V_4)U_1,
\end{aligned}
\tag{5.1}
$$



with the fixed maps of Item 185.  On the admissible interval,
$\mathscr D_p(s)=(-1)^s\Delta_{p,s}$.  Since $K=x^3H$, every $U_r(s)$
vanishes once $3s>p-1$.  Hence



$$
\mathscr D_p(s)=0
                 \quad(N_p+1\le s\le p-1).
\tag{5.2}
$$



Item 174 gives $\mathscr D_p(0)=\pm1/4\ne0$.  Let $P_p(S)$ be the
unique polynomial of degree at most $p-1$ taking the values (5.1) on
$S=0,\ldots,p-1$.  The $p-1-N_p$ distinct roots in (5.2) prove



$$
\deg P_p\ge p-1-N_p.
\tag{5.3}
$$



This has two rigorous consequences.

1. If $P_p=A_p/B_p$ on all field nodes, $A_p\ne0$, and $B_p$ is
   nonzero at every field node, then $A_p$ has all roots in (5.2), so
   $\deg A_p\ge p-1-N_p$.  A bounded-degree rational parameterization in
   $s$ is impossible for this natural extension.
2. An additive-character treatment of the polynomial $P_p$ has Swan
   degree at infinity at least $p-1-N_p$, since $0<\deg P_p<p$.
   Its direct conductor therefore grows linearly with $p$.

The known tail can be removed exactly.  Set



$$
L_p(S)=\prod_{a=N_p+1}^{p-1}(S-a),
 \qquad P_p=L_pG_p.
\tag{5.4}
$$



Then $\deg G_p\le N_p$, and $L_p(s)\ne0$ for $0\le s\le N_p$.
Consequently



$$
C_p(h)=\#\{0\le s\le N_p-h:
             G_p(s)=G_p(s+h)=0\}
 \le\deg\gcd(G_p(S),G_p(S+h)).
\tag{5.5}
$$



Equation (5.5) is an exact algebraic two-point reduction.  The generic
degree bound is still $N_p$, not $O(h)$.  Proving the desired small gcd
requires new determinant-specific arithmetic; (5.3) does not prove that no
such arithmetic exists.

## 6. Why bounded Kummer conductor is insufficient

Let $\omega:\mathbf F_p^\times\to\mu_{p-1}$ be the Teichmuller character.
Every pure term in (4.6) is the reduction at the distinguished prime above
$p$ of a sum



$$
\sum_{t\in X_p}
 \omega(t)^{3s+\alpha}
 \omega(1-t)^{3s+\beta}
 \omega(Q(t))^{-2s+\gamma}.
\tag{6.1}
$$



This is a rank-one Kummer sheaf, tame on the complement of the six points
in (4.5).  With the convention `rank + number of singular points`, its
conductor is at most seven; all Swan conductors are zero.  Changing
$s$ to $s+h$ changes local characters but neither rank nor the singular
locus.  External products give a uniformly bounded family on $X_p^2$.

The obstruction is arithmetic rather than geometric.  Complex Weil bounds
control every conjugate of (6.1), while $\Delta_{p,s}=0$ asks whether a
particular algebraic integer is divisible by one selected prime above
$p$.  The following exact family shows that no implication from bounded
conductor to sparse mod-$p$ zeros is possible.

For



$$
J_{p,s}=\sum_{t\in\mathbf F_p}t^s(1-t)^s,
 \qquad 1\le s<\frac{p-1}{2},
\tag{6.2}
$$



the polynomial in the summand has degrees from $s$ through $2s<p-1$.
Every relevant power sum over $\mathbf F_p$ is zero, so



$$
J_{p,s}=0\quad\hbox{in }\mathbf F_p
\tag{6.3}
$$



for a linear interval of parameters.  Its Teichmuller lift is the Jacobi
sum $J(\omega^s,\omega^s)$, attached to a rank-one tame Kummer sheaf with
only $0,1,\infty$ singular.  In this range the two characters and their
product are nontrivial, so every complex embedding has absolute value
$\sqrt p$; nevertheless its reduction is zero.  For fixed $h$, this
example has exactly



$$
\frac{p-3}{2}-h
\tag{6.4}
$$



simultaneous zero pairs when $1\le h<(p-3)/2$.

Therefore neither bounded conductor, square-root cancellation, nor the
mere fact that (4.8) is an $h$-twist can imply $C_p(h)=O(h)$.  A future
proof must control the distinguished $p$-adic reduction or exploit a
special identity of the determinant that the Jacobi counterexample lacks.
In particular, the counterexample blocks inference from bounded conductor
alone; it does not rule out a determinant-specific monodromy theorem,
unit-root theorem, or $p$-adic noncancellation argument.

## 7. Certificate and final separation

The standard-library certificate constructs (2.2) exactly, evaluates all
four Hasse derivatives, checks (4.4) pointwise, inverts (3.4), reconstructs
all aliases in (3.6), and compares (2.4) with the independent Item 180
recurrence.  It also constructs $P_p,L_p,G_p$ and checks (5.2)--(5.4), and
verifies every finite Jacobi zero in (6.3).

Dependency identities are serialized only under the stable logical keys
`sources/item180_moving_residual_report.md`,
`sources/item185_moving_root_count_report.md`, and
`sources/item189_collision_route_report.md`.  Local resolution works both
beside the staged `work/` copies and from archived `scripts/` against
archived `sources/`; neither absolute paths nor the output location enter
the JSON.  A replay in a synthetic archived layout is byte-identical to the
canonical work-layout JSON.

Default finite scope:



$$
\begin{array}{l|r}
\text{primes }17\le p\le47&9\\
\text{admissible }(p,s)\text{ pairs}&100\\
\text{rational Hasse-jet checks}&12{,}464\\
\text{excluded-point zero-jet checks}&1{,}144\\
\text{moment identities}&2{,}000\\
\text{alias reconstructions}&2{,}000\\
\text{independent determinant comparisons}&100.
\end{array}
\tag{7.1}
$$



Portable artifacts:

- `sources/item195_twopoint_moment_report.md`
- `scripts/item195_twopoint_moment_certificate.py`
- `results/item195_twopoint_moment_certificate.json`
- `results/item195_twopoint_moment_certificate_replay.json`
- `results/item195_twopoint_moment_hashes.sha256`

Final status:

- **PROVED:** the four-jet inversion, exact fixed-map two-point moments,
  bounded six-puncture Kummer realization, interpolation lower bound, tail
  factorization, collision-gcd reduction, and the Jacobi obstruction.
- **FINITE EXACT ONLY:** every count and degree equality in the certificate.
- **OPEN:** $C_p(h)=O(h)$, the Sidon assertion, every uniform sublinear
  bound for $r_p$, and every consequence for the arithmetic nature of
  $e+\pi$.
