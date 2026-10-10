> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The large-prime norm-one equation: a fixed torus with a primitive moving factorial coefficient family

## Status

The boundary-resultant theorem reduces every nonzero large-prime
cancellation to



$$
\frac{\iota(\mathcal N_{p,r})}{\mathcal N_{p,r}}
 =
 -\frac{\chi_pW_{c,r}}
        {\iota(\chi_p)\iota(W_{c,r})}
 \quad\text{in }\mathcal O_F/p\mathcal O_F,
\tag{1}
$$



where $F=\mathbb Q(\sqrt5)$, $\iota$ is its nontrivial conjugation,
$r=p-1-d$, and both displayed denominators are nonzero.

This note answers three structural questions about (1).

1. The known factorial scalar can be removed exactly.
2. After that removal, the resultant input obeys a bounded-dimensional
   recurrence in $r$, but its terminal condition still moves with $p$.
3. In every nonconstant case, the normalized coefficient polynomial is
   primitive and has
   projective height
   

$$
\log\frac{(p-1)!}{r!}+O(\log p).
$$


   Thus its lifted coefficient vector is not made small by content
   division.

Equation (1) is an equality on a fixed norm-one torus, but Hilbert 90
shows that the quotient map producing its left side is surjective. Torus
membership alone therefore imposes no restriction. These facts explain
precisely why a standard fixed-$S$ application does not follow from the
norm-one reformulation, and why the most direct small-moving-coefficient
formulation fails.  The intrinsic height of the evaluated torus point is
kept separate below.

This is an obstruction theorem, not a proof that the large-prime gcd is
large or small. It proves nothing about the arithmetic nature of
$e+\pi$.

The exact companion is
<scripts/cyclotomic_unit_large_prime_norm_one_certificate.py>, with output
<results/cyclotomic_unit_large_prime_norm_one_certificate.json>.

## 1. A canonical integer lift of the modular quotient

For a prime $p\nmid20$ and $0\le r\le p-1$, put



$$
\widehat S_{p,r}(Y)=\sum_{k=r}^{p-1}k!Y^k\in\mathbb Z[Y]
\tag{2}
$$



and define its divided difference at $1$:



$$
\begin{aligned}
 \widehat Q_{p,r}(Y)
   &=\frac{\widehat S_{p,r}(Y)-\widehat S_{p,r}(1)}{Y-1}\\
   &=\sum_{k=r}^{p-1}k!L_k(Y),
 \qquad
 L_k(Y)=\frac{Y^k-1}{Y-1}
       =\sum_{j=0}^{k-1}Y^j.
 \end{aligned}
\tag{3}
$$



If the derangement condition



$$
S_{p,r}(1)=0\pmod p
\tag{4}
$$



holds, then reduction of $\widehat Q_{p,r}$ modulo $p$ is exactly the
polynomial $Q_{p,r}$ in the boundary-resultant theorem. Indeed,
$\widehat S_{p,r}(1)$ then vanishes modulo $p$, and division by the
monic polynomial $Y-1$ commutes with reduction.

Every summand in (3) is divisible by $r!$. Define the normalized
integer polynomial



$$
\boxed{
 R_{p,r}(Y)=\frac{\widehat Q_{p,r}(Y)}{r!}
 =\sum_{k=r}^{p-1}\frac{k!}{r!}L_k(Y)\in\mathbb Z[Y].}
\tag{5}
$$



Let



$$
f_z(Y)=Y^2-zY+z,\qquad z=q^{-1},
$$



and put



$$
\mathcal M_{p,r}
   =\operatorname {Res}_Y(f_z,R_{p,r})\in\mathcal O_F.
\tag{6}
$$



Since $f_z$ has degree $2$, (5) gives, modulo $p$,



$$
\boxed{
 \mathcal N_{p,r}=(r!)^2\mathcal M_{p,r}.}
\tag{7}
$$



The scalar $(r!)^2\in\mathbb F_p^\times$ is fixed by $\iota$, so it
cancels from the conjugate ratio:



$$
\boxed{
 \frac{\iota(\mathcal N_{p,r})}{\mathcal N_{p,r}}
 =
 \frac{\iota(\mathcal M_{p,r})}{\mathcal M_{p,r}}.}
\tag{8}
$$



Thus (5) removes the known factorial unit exactly, not just up to height.

## 2. A bounded-order recurrence with a moving boundary

The polynomials in (5) satisfy



$$
\boxed{
 R_{p,p}(Y)=0,\qquad
 R_{p,r}(Y)=L_r(Y)+(r+1)R_{p,r+1}(Y).}
\tag{9}
$$



This follows by separating the $k=r$ summand and factoring $r+1$
from every later factorial quotient. Also



$$
L_{r+1}(Y)=L_r(Y)+Y^r,\qquad Y^{r+1}=Y\cdot Y^r.
\tag{10}
$$



Consequently, after evaluation at the two fixed quadratic points
$a=\eta^{-1}$ and $b=\bar\eta^{-1}$, the state



$$
\bigl(R_{p,r}(a),R_{p,r}(b),
       L_r(a),L_r(b),a^r,b^r\bigr)
\tag{11}
$$



obeys a fixed-dimensional first-order system with coefficients rational
in $r$. Tensoring this state gives a bounded-order recurrence for the
resultant



$$
\mathcal M_{p,r}=R_{p,r}(a)R_{p,r}(b).
\tag{12}
$$



The recurrence order is bounded, but the terminal condition is imposed
at the moving index $r=p$. Thus (9) is not one fixed recurrence sequence
in $r$ as $p$ varies; it is a triangular family with a moving
boundary.

## 3. Exact coefficient primitivity and projective height

Assume



$$
0\le r\le p-2
\tag{13}
$$



and write



$$
R_{p,r}(Y)=\sum_j c_jY^j.
$$



From (5),



$$
c_j=\sum_{k=\max(r,j+1)}^{p-1}\frac{k!}{r!},
\tag{14}
$$



where an empty sum is $0$. If $r\ge1$, then



$$
c_{r-1}-c_r=1.
\tag{15}
$$



If $r=0$, the corresponding adjacent difference is
$c_0-c_1=1$. Therefore, in all cases covered by (13),



$$
\boxed{\gcd_j(c_j)=1.}
\tag{16}
$$



No positive integer content remains after the $r!$ division.

The leading coefficient is



$$
c_{p-2}=\frac{(p-1)!}{r!}.
\tag{17}
$$



All coefficients are positive. There are $d+1=p-r$ summands in (5),
and each factorial quotient is at most the value in (17). Hence the primitive
projective height



$$
H(R_{p,r})=\max_j|c_j|
$$



satisfies the exact elementary bounds



$$
\boxed{
 \frac{(p-1)!}{r!}
 \le H(R_{p,r})
 \le (d+1)\,\frac{(p-1)!}{r!}.}
\tag{18}
$$



Equivalently,



$$
\boxed{
 \log H(R_{p,r})
 =\sum_{k=r+1}^{p-1}\log k+O(\log(d+1)).}
\tag{19}
$$



The $O(\log(d+1))$ has an absolute implied constant and follows
directly from (18).

For a proportional boundary $r/p\to\rho\in(0,1)$, (19) gives



$$
\log H(R_{p,r})=\Theta(p\log p).
\tag{20}
$$



By contrast, the characteristic-zero height of the fixed unit-trace
sequence $W_{c,r}$ is $O(r)$. Thus in every proportional regime the
**coefficient polynomial** $R_{p,r}$ is not a small moving coefficient
vector relative to the unit orbit. This is an exact projective
statement: (15)--(16) show that no common coefficient content can remove
its leading height.

This coefficient-height statement must not be confused with a lower
bound for the intrinsic height of the evaluated point
$\delta_p(\mathcal M_{p,r})$. Evaluation at $a,b$, formation of the
resultant, and the conjugate quotient can create additional
archimedean or finite-place cancellation. No comparison
$h(\delta(\mathcal M_{p,r}))\asymp\log H(R_{p,r})$ is asserted here.
What (20) rules out is only a direct small-moving-**coefficient**
application before those evaluations.

For $d=o(p)$, (19) instead reads



$$
\log H(R_{p,r})
               =d\log p+O(d^2/p+\log(d+1)).
\tag{21}
$$



Some very thin boundary regimes could therefore have smaller relative
coefficient height. Equation (21) does not solve them, because (1) remains a
congruence in varying characteristic and $W_{c,r}$ is a sum of two unit
monomials rather than a single $S$-unit.

## 4. The fixed norm-one torus

For each $p\nmid20$, let



$$
\mathbb T_p=
 \{t\in(\mathcal O_F/p\mathcal O_F)^\times:
             t\iota(t)=1\}.
\tag{22}
$$



This is the group of $\mathbb F_p$-points of the fixed norm-one torus
$\operatorname {Res}^{\,1}_{F/\mathbb Q}\mathbb G_m$. Define



$$
\delta_p:(\mathcal O_F/p\mathcal O_F)^\times\longrightarrow\mathbb T_p,
\qquad
 \delta_p(x)=\frac{\iota(x)}x.
\tag{23}
$$



### Proposition 1 (surjectivity)

The map $\delta_p$ is surjective for every $p\nmid20$.

#### Proof

If $p$ splits in $F$, write
$\mathcal O_F/p\simeq\mathbb F_p\times\mathbb F_p$, with $\iota$
interchanging the factors. Then



$$
\delta_p(x_+,x_-)
   =\left(\frac{x_-}{x_+},\frac{x_+}{x_-}\right),
\tag{24}
$$



which gives every pair $(t,t^{-1})$.

If $p$ is inert, identify the quotient with $\mathbb F_{p^2}$. Then



$$
\delta_p(x)=x^{p-1}.
\tag{25}
$$



Its image has order



$$
\frac{p^2-1}{\gcd(p^2-1,p-1)}=p+1,
$$



which is exactly the order of the norm-one subgroup. ∎

At every nonzero cancellation, (1) is therefore the equality of two
points of $\mathbb T_p$:



$$
\boxed{
 \delta_p(\mathcal M_{p,r})
 =
 -\frac{\chi_pW_{c,r}}
        {\iota(\chi_pW_{c,r})}.}
\tag{26}
$$



This does put the problem on a fixed torus. But Proposition 1 shows that
membership in the torus, or representation as a conjugate ratio, cannot
confine the left side to a proper subgroup. Any restriction must use the
specific factorial recurrence (9), not Hilbert 90 alone.

## 5. Why a fixed-$S$ formulation is not yet available

The integer coefficient family in (5) is not supported on any fixed
finite set of rational primes. For example, at $r=1$, its leading
coefficient is $(p-1)!$, whose prime support grows with $p$. More
intrinsically, (17) contains every prime factor occurring in the interval
product



$$
\prod_{k=r+1}^{p-1}k.
\tag{27}
$$



Thus the full ambient family has no fixed coefficient set $S$. This
statement concerns the coefficient family before imposing the root
condition (4); it does not claim that the unknown subsequence of
nondegenerate roots has any prescribed prime support.

Even if coefficient primes were ignored, a standard characteristic-zero
$S$-unit theorem would still not apply directly:

1. equation (26) is a congruence in a quotient whose characteristic
   varies with $p$;
2. the left point is a resultant of a primitive polynomial with the
   moving height (19);
3. the right point contains $W_{c,r}$, a sum of two conjugate unit
   monomials; and
4. the recurrence (9) has a terminal condition at the moving index $p$.

These are exact missing hypotheses, not a claim that every possible
Subspace-theorem refinement must fail.

## 6. Conclusion

Dividing the known factorial unit produces the canonical primitive
polynomial $R_{p,r}$. Its recurrence has bounded dimension, but its
boundary and primitive projective height move with $p$. The norm-one
equation lies on a fixed torus, yet the conjugate-ratio map is surjective.
Consequently neither the explicitly removable factorial content,
bounded recurrence dimension, nor torus membership supplies a uniform
restriction on the large-prime solutions. The large primitive
coefficient height also blocks a direct small-moving-coefficient
argument, while leaving the intrinsic height of the evaluated torus
point unresolved.

The unresolved task is now precise: exploit the **specific values** of
the primitive factorial recurrence (9) at the two quadratic points,
simultaneously with the derangement root condition (4), strongly enough
to restrict the equality (26) as $p$ and $r$ vary.
