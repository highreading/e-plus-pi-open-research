> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 281 — isolated $j=1$ collisions, the normalized Fitting generator, and a finite-form scalar no-go

Checked: 2026-08-31 (Beijing time)

## 1. Scope, admission audit, and verdict

Retain the actual fixed common-log cell



$$
p=4h+6s+3,\qquad h,s\ge1,\qquad M=3h+4s+2,              \tag{1.1}
$$



and its full simultaneous divided gate



$$
Q_0(p,h,s)=Q_1(p,h,s)=0\pmod p.                           \tag{1.2}
$$



Fix any bounded isolation diameter $D$.  Item 279 proves that the
ambient prime rows having another prime row within $D$ parameter steps
have total log weight $o(M)$.  Thus, at linear scale, controlling the
$D$-isolated collision primes is equivalent to controlling the full
fixed-$j=1$ collision set.  No cluster calculation is repeated here.

This item first asks for the smallest natural integral scalar attached to
the two-condition gate and then audits its height.

> **PROVED — the canonical integral scalar is already the target gcd.**
> Let $F_M$ be Item 200's squarefree forced Cartier product, put
> $\overline C_\nu(M)=C_\nu(M)/F_M$, and define
>
> 

$$
> g_M=\gcd(\overline C_0(M),\overline C_1(M)).              \tag{1.3}
>
$$


>
> The ideal
> $(\overline C_0,\overline C_1)=g_M\mathbb Z$ is the
> zeroth Fitting ideal and first Smith ideal of the specialized one-row
> gate.  For every actual $j=1$ prime,
>
> 

$$
> \boxed{p\mid g_M
> \iff p^2\mid C_0(M),C_1(M)
> \iff \text{the full gate collides at }p.}                 \tag{1.4}
>
$$



> Thus the Fitting generator does not create a new invariant: it is the
> arithmetic common-divisor problem itself.

> **PROVED — no state-free rank-two resultant exists.**  Over the generic
> rank-two chart, the collision ideal in the four state variables is two
> independent linear forms.  Its elimination to the parameter field is
> zero: two hyperplanes in $\mathbb P^3$ always meet in a line.  Every
> state-free resultant of only those two forms is therefore identically
> zero.  After substituting the actual arithmetic state, scalarization
> returns exactly to (1.3).

> **PROVED — sharply scoped finite-form no-go.**  No finite library of
> fixed integral homogeneous binary forms can give a fiberwise exact
> one-scalar encoding of the origin in $\mathbb F_p^2$ for every actual
> prime row.  Chebotarev supplies infinitely many actual primes at which
> every form in the library has a nonzero projective zero.  This closes
> fixed-coefficient norm/resultant libraries; it does not close
> parameter-dependent forms or a scalar exploiting special distribution
> of the arithmetic state.

> **PROVED — height admission fails.**  Even after removing all forced
> Cartier content, the inherited component height constant is
>
> 

$$
> H-\kappa=3.99058003744209\ldots,                           \tag{1.5}
>
$$


>
> while the raw $j=1$ prime-log mass is only $1/6$ per $M$.
> Every bounded-degree homogeneous scalar has the same inherited
> height-to-valuation ratio $H-\kappa$; a nonhomogeneous one is weaker.
> The raw-coordinate estimate $H/2$ from Item 264 is still better, but
> also far above $1/6$.

No isolated-prime weighted bound is obtained.  Item 149 already books the
first post-Cartier copy, so



$$
\boxed{\text{new fixed-\(j=1\) capacity reduction}=0,\qquad
        \text{new unconditional Route-1 rate}=0.}           \tag{1.6}
$$



The raw ceiling remains $1/36$ per $6M$.

## 2. Exact normalized Smith/Fitting generator

The fixed integers are



$$
C_\nu(M)=[z^{4M+\nu}]
 { (1-z)^{6M}(1+z)^{1+3\nu}
  \over(1+z^2)^{4M+1+\nu}},\qquad \nu=0,1.                 \tag{2.1}
$$



Item 200 proves that the squarefree product



$$
F_M=\prod_{p\in\mathcal P_M}p                              \tag{2.2}
$$



divides both coordinates.  Every actual $j=1$ prime belongs to
$\mathcal P_M$, and Item 197's residue bridge says



$$
Q_0=Q_1=0\pmod p
 \iff p^2\mid C_0(M),C_1(M).                               \tag{2.3}
$$



Because $F_M$ is squarefree and contains $p$ exactly once,



$$
p^2\mid C_0,C_1
 \iff p\mid\overline C_0,\overline C_1,                    \tag{2.4}
$$



which proves (1.4).

Consider the specialization map



$$
\mathbb Z^2\longrightarrow\mathbb Z,qquad
 (a,b)\longmapsto a\overline C_0+b\overline C_1.           \tag{2.5}
$$



Its image is



$$
(\overline C_0,\overline C_1)=g_M\mathbb Z.               \tag{2.6}
$$



Thus $g_M$ is simultaneously:

* the positive generator of the integral gate ideal;
* the first Smith divisor of the one-row matrix
  $(\overline C_0\ \overline C_1)$; and
* the zeroth Fitting generator of its cokernel.

This is the canonical minimal positive element obtainable by integral
Bézout recombination.  Its Bézout coefficients depend on $M$ and can
have large height; writing the gcd as a combination is not a uniform
low-height identity.

Let



$$
B_M^{(1)}=\prod_{(4M+3)/3\le p\le(3M-1)/2}p.              \tag{2.7}
$$



If the pair $(\overline C_0,\overline C_1)$ is not identically zero,
the full collision radical is exactly



$$
R_M^{(1)}=\gcd(\operatorname{rad}|g_M|,B_M^{(1)}).         \tag{2.8}
$$



Equation (2.8) is an exact recognition, but it is tautological from the
viewpoint of density: factoring the Fitting generator on the target prime
interval is precisely the problem to be bounded.  If both coordinates
vanish as integers, the height route supplies no estimate and the raw
prime-interval ceiling remains valid.

## 3. Isolated primes differ by only $o(M)$

Let $R_{M,D}^{\mathrm{iso}}$ be the subproduct of (2.8) over primes
having no other actual prime row within $D$ fixed-$M$ steps.  Item 279
gives



$$
0\le\log R_M^{(1)}-\log R_{M,D}^{\mathrm{iso}}
 \le O_D\!\left({M\over\log M}\right)=o(M).                \tag{3.1}
$$



Therefore a bound



$$
\log R_{M,D}^{\mathrm{iso}}\le cM+o(M),\qquad c<1/6,      \tag{3.2}
$$



would be equivalent, for capacity purposes, to the same bound for the
full radical.  Conversely, Item 279's bounded-cluster theorem by itself
does not change the $1/6$ raw coefficient.  All remaining linear
capacity sits in the isolated target (3.2).

## 4. Fitting and Plücker rank stratification

Let $K$ be the generic parameter field on a unit transport chart and
write the reduced gate as



$$
Gx=0,\qquad G\in K^{2\times4},\qquad
 x=(x_1,x_2,x_3,x_4)^{\mathsf T}.                           \tag{4.1}
$$



Put $q_0,q_1$ for the two coordinates of $Gx$.  The complete rank
stratification is



$$
\begin{array}{c|c|c|c}
\operatorname{rank}G&\text{normal form of }(q_0,q_1)
 &\text{collision ideal}&\dim\ker G\\ \hline
2&(x_1,x_2)&(x_1,x_2)&2\\
1&(x_1,0)&(x_1)&3\\
0&(0,0)&(0)&4.
\end{array}                                                 \tag{4.2}
$$



On the rank-two chart, $(q_0,q_1)$ is a height-two prime ideal and is
not principal.  Its Plücker encoding is the codimension-two flag
incidence from Item 275.  Eliminating the state gives



$$
(q_0,q_1)\cap K=(0),                                      \tag{4.3}
$$



because $x=0$ is a solution for every parameter and, projectively, the
kernel is always a $\mathbb P^1$.  Hence the classical resultant of two
linear forms in four variables has no nonzero parameter-only generator.
Adding their $2\times2$ minors only records the moving kernel plane; it
does not test whether the actual arithmetic section lies in that plane.

Rank one makes the fiber ideal principal and rank zero makes it zero, but
no all-prime theorem bounds either rank-drop stratum.  They cannot be
discarded, and multiplying by rank minors would only add extra zeros.
The denominator-free specialized Fitting statement (2.4)--(2.8) includes
all three ranks and every transport-singular row.

## 5. The smallest exact local scalar has degree two

Fix an odd prime $p$ and consider a scalar polynomial on the two gate
values $(u,v)\in\mathbb F_p^2$.

* A degree-zero polynomial that vanishes at the origin is the zero
  polynomial and vanishes everywhere.
* Every nonzero linear form $au+bv$ has a one-dimensional kernel, so it
  vanishes at a nonzero pair.
* If $d$ is a quadratic nonresidue modulo $p$, then

  

$$
N_d(u,v)=u^2-dv^2                                      \tag{5.1}
$$



  vanishes only at $(0,0)$.

Thus degree two is the exact local minimum.  The obstacle is uniformity:
the required nonresidue generally depends on $p$.

For the global integral gate, use



$$
\mathcal N_d(M)=\overline C_0(M)^2-d\overline C_1(M)^2.   \tag{5.2}
$$



If $d$ is a nonresidue modulo an actual prime $p$, then



$$
p\mid\mathcal N_d(M)
 \iff p\mid\overline C_0(M),\overline C_1(M),              \tag{5.3}
$$



and a collision in fact gives $p^2\mid\mathcal N_d(M)$.
This is an exact local scalarization, but not one fixed scalarization for
all actual primes.

## 6. Exact actual false positives for standard fixed norms

Let



$$
U_\nu={C_\nu(M)\over p}\pmod p.                            \tag{6.1}
$$



Since $F_M=p(F_M/p)$ and $F_M/p$ is a $p$-unit, the normalized
pair $(\overline C_0,\overline C_1)$ is a common nonzero scalar multiple
of $(U_0,U_1)$ modulo $p$.  Hence the homogeneous norm relation is
the same for both pairs.

The checker recomputes the following exact actual rows:



$$
\begin{array}{c|c|c|c|c}
d&(p,h,s,M)&(U_0,U_1)&U_0^2-dU_1^2&\text{full collision}\\ \hline
-1&(61,10,3,44)&(32,47)&0&\text{no}\\
 2&(89,8,9,62)&(88,32)&0&\text{no}\\
 3&(37,4,3,26)&(35,10)&0&\text{no}\\
 5&(59,5,6,41)&(52,36)&0&\text{no}\\
 7&(37,1,5,25)&(15,14)&0&\text{no}.
\end{array}                                                 \tag{6.2}
$$



Every zero in the fourth column is modulo its displayed prime.  Neither
coordinate in the third column is simultaneously zero.  Thus each of the
five standard constant norms has an actual arithmetic false positive; a
norm zero cannot be substituted for the simultaneous gate on its split
rows.

These witnesses do not prove a density statement and do not exclude a
row-dependent choice among several norms.

## 7. No finite fixed-form library is fiberwise exact

The norm obstruction has a general fixed-coefficient form.

> **Finite-form theorem.**  Let
> $\mathcal F=\{F_1,\ldots,F_k\}$ be any finite set of nonzero
> homogeneous forms of positive degree in $\mathbb Z[U,V]$.  There are
> infinitely many actual phase primes $p$ such that every reduction
> $F_i\bmod p$ has a nonzero zero in $\mathbb F_p^2$.

To prove it, first discard the finite set of primes dividing all
coefficients of a form.  If $F_i(T,1)$ is nonconstant, let $L_i$ be
its splitting field.  If it is constant, homogeneity forces
$F_i(U,V)=cV^{d_i}$, which already vanishes at $[1:0]$ modulo every
good prime.  Let $L$ be the compositum of the finitely many $L_i$.
Chebotarev's density theorem gives infinitely many primes splitting
completely in $L$.  At every such good prime, each nonconstant
$F_i(T,1)$ has a root in $\mathbb F_p$, so every $F_i$ has a
projective zero.

Every prime $p\ge13$ occurs on the actual tied family.  Explicitly,



$$
(h,s)=
 \begin{cases}
 ((p-9)/4,1),&p\equiv1\pmod4,\\
 ((p-15)/4,2),&p\equiv3\pmod4,
 \end{cases}                                                \tag{7.1}
$$



with the second line valid for $p\ge19$.  Hence the Chebotarev primes
are actual phase primes, proving the theorem.

As a portable witness, at the actual row



$$
(p,h,s,M)=(1009,250,1,756),                                \tag{7.2}
$$



all five discriminants $-1,2,3,5,7$ are squares.  Respective square
roots are



$$
469,\ 439,\ 149,\ 244,\ 45\pmod{1009}.                    \tag{7.3}
$$



The theorem is deliberately scoped.  It excludes a finite library of
fixed-coefficient forms as a **fiberwise** exact compression of the two
gate values.  It does not exclude:

* coefficients depending rationally on $(h,s)$ or on $M$;
* a prime-dependent nonresidue or a growing-degree finite-field
  indicator;
* a scalar whose false-positive fibers are nevertheless avoided by the
  special arithmetic state; or
* a sheaf, trace, or distribution theorem for the original
  codimension-two incidence.

## 8. Height of the normalized Fitting and scalar routes

Item 200's forced prime intervals have total PNT length



$$
\kappa=
 \sum_{j\ge0}\left({6\over3j+1}-{4\over2j+1}\right)
 =-4\log2+{\pi\over\sqrt3}+3\log3
 =2.33704750799876\ldots.                                  \tag{8.1}
$$



Consequently



$$
\log F_M=\kappa M+o(M).                                   \tag{8.2}
$$



Item 264's direct componentwise Cauchy constant is



$$
H=6.327627545440858\ldots.                                 \tag{8.3}
$$



For every nonzero normalized coordinate,



$$
\log|\overline C_\nu(M)|
 \le(H-\kappa)M+o(M)
 =3.99058003744209\ldots M+o(M).                            \tag{8.4}
$$



This immediately bounds $|g_M|$, but gives only



$$
{\log R_M^{(1)}\over M}\le H-\kappa+o(1),                \tag{8.5}
$$



which is much weaker than the raw $1/6$ interval ceiling.

More generally, let $P(U,V)$ have coefficient height
$\exp(o(M))$, maximum total degree $d$, and minimum occurring total
degree $e\ge1$.  A collision prime divides both normalized coordinates,
so



$$
(R_M^{(1)})^e\mid
 P(\overline C_0(M),\overline C_1(M)).                      \tag{8.6}
$$



The inherited componentwise estimate is



$$
\log|P(\overline C_0,\overline C_1)|
 \le d(H-\kappa)M+o(M).                                    \tag{8.7}
$$



If the scalar is nonzero, (8.6)--(8.7) give



$$
{\log R_M^{(1)}\over M}
 \le{d\over e}(H-\kappa)+o(1)
 \ge H-\kappa+o(1).                                       \tag{8.8}
$$



If it is zero, this route gives no bound.  Homogeneous forms, including
every anisotropic norm, attain $d/e=1$; nonhomogeneous forms are worse.
Even a hypothetical simultaneous nonresidue $d_M$ of
subexponential height would therefore leave the ratio (1.5).  An
exponential-height $d_M$ only increases it.

The raw coordinates carry collision valuation two and give Item 264's
better ratio $H/2=3.1638137727\ldots$, still far above $1/6$.  At
the normalized height, at least



$$
t>6(H-\kappa)=23.9434802246\ldots,
 \qquad\text{hence }t\ge24,                                \tag{8.9}
$$



independent normalized valuation copies would be needed merely to beat
the raw support.  No such lift is proved.

The scope is the inherited componentwise estimate.  A separately proved
subexponential bound for the normalized gcd, or genuine exponential
cancellation in a particular scalar, remains open.

## 9. Admission and de-overlap

The master admission test now has an exact answer.

1. **Actual-family implication.**  Equations (1.4) and (2.8) identify the
   collision radical exactly inside the normalized Fitting generator.
   Every rank and transport branch is included.
2. **De-overlap.**  $F_M$ removes the already forced Cartier copy, and
   Item 149 already books the first post-Cartier copy on these same rows.
   A norm or bounded-degree recombination gives no independent valuation
   beyond its algebraic power of the same two-coordinate ideal.
3. **Height and capacity.**  The best existing raw ratio is $H/2>1/6$;
   the normalized Fitting/form ratio $H-\kappa$ is worse.  No estimate
   with coefficient $c<1/6$ is proved for the isolated radical.

Thus no retained ceiling below $1/36$ per $6M$ and no new Route-1
rate follow.

## 10. Replay and proof labels

The standard-library checker verifies:

* the forced divisor, normalized Bézout/Fitting generator, and exact
  bridge (2.4) on every actual $j=1$ row through $M\le120$;
* the three canonical rank strata in (4.2);
* the degree-one obstruction and anisotropic quadratic norm on six exact
  finite fields;
* all five actual false positives in (6.2);
* the split-library actual phase witness (7.2)--(7.3);
* the displayed height constants and integer threshold $t\ge24$.

Every bounded row or finite-field replay is **EXACT FINITE ONLY**.  The
all-prime finite-form theorem uses Chebotarev, and the height asymptotic
uses the prime number theorem; neither is inferred from a finite replay.

### PROVED

* The normalized Smith/Fitting generator and exact collision-prime
  recognition.
* The rank-two elimination/resultant obstruction and all rank strata.
* Degree two as the smallest exact local scalar degree.
* Actual false positives for the five standard fixed norms.
* The Chebotarev no-go for every finite fixed-form fiberwise library.
* The normalized height constant, bounded-degree inherited-estimate
  barrier, Item 149 de-overlap, and zero booking.

### EXACT FINITE ONLY

* The bounded coefficient/Fitting replay and displayed finite-field
  witnesses.

### OPEN

* Any $c<1/6$ weighted bound for isolated or full $j=1$ collision
  primes.
* A subexponential theorem for the relevant part of the normalized gcd.
* A parameter-dependent scalar, growing-degree indicator, or arithmetic
  section theorem outside the fixed-form class.
* Any positive fixed-$j=1$ capacity reduction or new Route-1 rate.
